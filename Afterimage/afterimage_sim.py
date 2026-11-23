"""AFTERIMAGE simulator -- concentration on a deck with no backs.

Rules modelled (see AFTERIMAGE_concept.md):
- Wash-shuffle (each card's up face is random) and lay all 36 cards flat. Every card
  shows one sign to everyone; the other face is pressed to the table.
- A GUESS: flip one card (its pressed face is revealed), then flip a second. If the two
  newly revealed signs are the same, take both cards, score 1 and guess again. If not,
  both cards STAY flipped (their old shown faces are now pressed) and the turn passes.
- Two ends are modelled:
    natural -- the game stops the moment no sign is pressed under two or more remaining
               cards (publicly countable; the "true end"). Used for the structural numbers.
    sweep   -- the real end rule. Instead of guessing you may SWEEP: flip every remaining
               card. If no two show the same sign the game ends and the sweeper scores
               SWEEP_PTS. Otherwise flip them all back; everyone has now seen every pressed
               face, and the turn passes. With fewer than 2 cards left, sweeping is the
               only move. The game ends ONLY by a successful sweep.
- Turn cap: CAP guesses -> counted as a stall.

What the sim cannot model: human memory (bots forget as "the last N cards flipped",
not by salience or position), table talk, misremembering with confidence, the feel of
counting, and whether a sideways-turn marker for "seen" cards helps. Those are table
questions.

Bots (all use only public information plus their own memory):
- random   -- flips two random cards. Mechanics floor.
- perfect  -- remembers every card that has ever been flipped (both faces were seen).
- forget-K -- remembers only the K most recently flipped cards.
  Memory bots: take a remembered pair if one exists; otherwise flip an unremembered card,
  then a remembered card pressing the same sign if there is one, else an unremembered card
  that does NOT show that sign (a card showing S cannot press S: its two faces differ).
- counter  -- perfect memory AND counts pressed signs (8 - cards showing it - taken faces),
  so it knows exactly when no pressed pair remains and sweeps then -- unless it is trailing
  and the sweep point would still not save it, in which case it REFUSES and makes the
  safest miss it can find. Mid-game it prefers flips that do not set up a pair for the
  next player.
- memory   -- perfect memory, no counting. Sweeps only once every remaining card is
  remembered and holds no pair.
- gambler  -- remembers its last 6 flips, no counting; sweeps when 4 or fewer cards remain
  and it knows no pair.

Usage:  python afterimage_sim.py --run            (default 2,000 games per configuration)
        python afterimage_sim.py --run --games 500 --seed 7
"""
import argparse
import itertools
import random
import statistics
from collections import Counter, deque

CAP = 2000
SIGNS = 9


# ---------------------------------------------------------------- the table
class Table:
    def __init__(self, rng, signs=SIGNS):
        self.rng = rng
        self.shown, self.pressed = {}, {}
        for card, (a, b) in enumerate(itertools.combinations(range(signs), 2)):
            if rng.random() < 0.5:  # wash-shuffle: random face up
                a, b = b, a
            self.shown[card], self.pressed[card] = a, b
        self.alive = set(self.shown)

    def flip(self, card):
        self.shown[card], self.pressed[card] = self.pressed[card], self.shown[card]
        return self.shown[card]

    def pressed_counts(self):
        """Publicly countable: 8 - cards showing the sign - taken faces with the sign."""
        return Counter(self.pressed[c] for c in self.alive)

    def truly_over(self):
        pc = self.pressed_counts()
        return not pc or max(pc.values()) < 2


# ---------------------------------------------------------------- the bots
class Bot:
    def __init__(self, kind, k=None):
        self.kind, self.score = kind, 0
        if kind == "gambler":
            k = 6
        self.k = k
        self.mem = deque(maxlen=k) if k else []  # cards whose pressed face I know

    def see(self, card):
        if self.kind == "random":
            return
        if card in self.mem:
            self.mem.remove(card)
        self.mem.append(card)

    def see_all(self, t):
        for c in sorted(t.alive):
            self.see(c)

    def known(self, t):
        return [c for c in self.mem if c in t.alive]

    def known_pair(self, t):
        by = {}
        for c in self.known(t):
            by.setdefault(t.pressed[c], []).append(c)
        for cards in by.values():
            if len(cards) >= 2:
                return cards[0], cards[1]
        return None

    # -- the decision: ("sweep",) / ("refuse",) / ("guess", first, second_or_None)
    def decide(self, t, scores, me, sweep_pts):
        if self.kind == "random":
            return ("guess", t.rng.choice(sorted(t.alive)), None)
        kp = self.known_pair(t)
        if kp:
            return ("guess", kp[0], kp[1])
        if sweep_pts is not None:
            if len(t.alive) < 2:
                return ("sweep",)
            if self.kind == "counter" and t.truly_over():
                best_other = max(s for j, s in enumerate(scores) if j != me)
                if self.score + sweep_pts < best_other:
                    return ("refuse",)
                return ("sweep",)
            if self.kind == "memory" and len(self.known(t)) == len(t.alive):
                return ("sweep",)
            if self.kind == "gambler" and len(t.alive) <= 4:
                return ("sweep",)
        return ("guess", self.first_flip(t), None)

    def _careful_order(self, t, cards):
        # Flipping c presses its shown face: avoid signs already pressed elsewhere.
        pc = t.pressed_counts()
        return sorted(cards, key=lambda c: (pc[t.shown[c]], t.rng.random()))

    def first_flip(self, t):
        kn = set(self.known(t))
        unknown = [c for c in sorted(t.alive) if c not in kn] or sorted(t.alive)
        if self.kind == "counter":
            return self._careful_order(t, unknown)[0]
        return t.rng.choice(unknown)

    def second_flip(self, t, first, sign):
        rest = [c for c in sorted(t.alive) if c != first]
        if self.kind == "random":
            return t.rng.choice(rest)
        kn = set(self.known(t))
        for c in self.known(t):
            if c != first and t.pressed[c] == sign:
                return c
        unknown = [c for c in rest if c not in kn]
        good = [c for c in unknown if t.shown[c] != sign] or unknown or rest
        if self.kind == "counter":
            return self._careful_order(t, good)[0]
        return t.rng.choice(good)

    def safest_miss(self, t):
        alive = sorted(t.alive)
        best, best_bad = None, 99
        for a, b in itertools.combinations(alive, 2):
            after = [t.pressed[c] for c in alive if c not in (a, b)] + [t.shown[a], t.shown[b]]
            bad = sum(v - 1 for v in Counter(after).values() if v > 1)
            if bad < best_bad:
                best, best_bad = (a, b), bad
                if bad == 0:
                    break
        return best


# ---------------------------------------------------------------- one game
def play(kinds, seed, sweep_pts=None, signs=SIGNS):
    """kinds: list of (kind, k). sweep_pts None = natural end."""
    rng = random.Random(seed)
    t = Table(rng, signs)
    ps = [Bot(*k) for k in kinds]
    seat = guesses = 0
    last_taker = None
    first_guess_match = None
    over_at = None
    reached = {}  # cards-left -> was a pressed pair still present when first reached
    failed_sweeps = refusals = 0
    while True:
        n = len(t.alive)
        if n not in reached:
            reached[n] = not t.truly_over()
        if over_at is None and t.truly_over():
            over_at = guesses
            if sweep_pts is None:
                return dict(guesses=guesses, left=n, scores=[p.score for p in ps],
                            first_match=first_guess_match, reached=reached)
        if guesses >= CAP:
            return None
        p = ps[seat]
        d = p.decide(t, [q.score for q in ps], seat, sweep_pts)
        if d[0] == "sweep":
            if t.truly_over():
                before = [q.score for q in ps]
                p.score += sweep_pts
                others = max(s for j, s in enumerate(before) if j != seat)
                decided = p.score > others and not before[seat] > others
                return dict(guesses=guesses, left=n, scores=[q.score for q in ps],
                            first_match=first_guess_match, reached=reached,
                            late=guesses - over_at, failed=failed_sweeps,
                            refusals=refusals, decided=decided,
                            sweeper=seat, last_taker=last_taker)
            failed_sweeps += 1
            for q in ps:
                q.see_all(t)
            seat = (seat + 1) % len(ps)
            continue
        guesses += 1
        if d[0] == "refuse":
            refusals += 1
            c1, c2 = p.safest_miss(t)
        else:
            _, c1, c2 = d
        s1 = t.flip(c1)
        for q in ps:
            q.see(c1)
        if c2 is None:
            c2 = p.second_flip(t, c1, s1)
        s2 = t.flip(c2)
        for q in ps:
            q.see(c2)
        if first_guess_match is None:
            first_guess_match = s1 == s2
        if s1 == s2:
            t.alive -= {c1, c2}
            p.score += 1
            last_taker = seat
        else:
            seat = (seat + 1) % len(ps)


def resolve(r, rule):
    """Winner seat or 'tie' under a tiebreak rule: shared / sweeper / lastpair."""
    sc = r["scores"]
    top = max(sc)
    tied = [j for j, s in enumerate(sc) if s == top]
    if len(tied) == 1:
        return tied[0]
    if rule == "sweeper" and r["sweeper"] in tied:
        return r["sweeper"]
    if rule == "lastpair" and r["last_taker"] in tied:
        return r["last_taker"]
    return "tie"


def tiebreak_table(label, kinds, n, base, signs=SIGNS):
    res = [play(kinds, base + i, 1, signs) for i in range(n)]
    done = [r for r in res if r]
    cells = []
    for rule in ("shared", "sweeper", "lastpair"):
        w = Counter(resolve(r, rule) for r in done)
        seats = [100 * w[j] / len(done) for j in range(len(kinds))]
        decided = 100 - 100 * w["tie"] / len(done)
        spread = max(seats) - min(seats)
        cells.append(f"{rule}: ties {pct(w['tie'], len(done))}, seats "
                     + "/".join(f"{s:.0f}" for s in seats) + f" (spread {spread:.1f})")
    print(f"  {label:22s} " + " | ".join(cells))


def winners(scores):
    top = max(scores)
    w = [j for j, s in enumerate(scores) if s == top]
    return "tie" if len(w) > 1 else w[0]


def pct(x, n):
    return f"{100 * x / max(n, 1):.1f}%"


# ---------------------------------------------------------------- reports
def natural_table(label, kinds, n, base):
    res = [play(kinds, base + i) for i in range(n)]
    done = [r for r in res if r]
    g = [r["guesses"] for r in done]
    wins = Counter(winners(r["scores"]) for r in done)
    print(f"  {label:30s} ended {pct(len(done), n):>6}  guesses med {statistics.median(g):5.0f} "
          f"max {max(g):4d}  cards left mean {statistics.mean(r['left'] for r in done):4.1f}  "
          "wins " + ", ".join(f"{k}:{pct(v, len(done))}" for k, v in sorted(wins.items(), key=str)))
    return done


def head_to_head(label, a, b, n, base):
    """Seat-randomised: n games with A in seat 0, n with A in seat 1."""
    a_win = b_win = tie = 0
    for arm, kinds in enumerate(([a, b], [b, a])):
        for i in range(n):
            r = play(kinds, base + arm * 10**5 + i)
            w = winners(r["scores"])
            if w == "tie":
                tie += 1
            elif (w == 0) == (arm == 0):
                a_win += 1
            else:
                b_win += 1
    tot = 2 * n
    print(f"  {label:30s} A wins {pct(a_win, tot):>6}  B wins {pct(b_win, tot):>6}  ties {pct(tie, tot):>6}")


def sweep_table(label, kinds, n, base, pts):
    res = [play(kinds, base + i, pts) for i in range(n)]
    done = [r for r in res if r]
    stalls = n - len(done)
    wins = Counter(winners(r["scores"]) for r in done)
    late = [r["late"] for r in done]
    print(f"  {label:26s} stalls {stalls}/{n}  guesses med {statistics.median(r['guesses'] for r in done):4.0f}  "
          f"extra after true end mean {statistics.mean(late):.2f} max {max(late):2d}  "
          f"failed sweeps {statistics.mean(r['failed'] for r in done):.2f}  "
          f"refusals {statistics.mean(r['refusals'] for r in done):.2f}  "
          f"sweep decided {pct(sum(r['decided'] for r in done), len(done))}  "
          "wins " + ", ".join(f"{k}:{pct(v, len(done))}" for k, v in sorted(wins.items(), key=str)))
    return stalls


def sweep_h2h(label, a, b, n, base, pts):
    a_win = b_win = tie = 0
    for arm, kinds in enumerate(([a, b], [b, a])):
        for i in range(n):
            r = play(kinds, base + arm * 10**5 + i, pts)
            w = winners(r["scores"])
            if w == "tie":
                tie += 1
            elif (w == 0) == (arm == 0):
                a_win += 1
            else:
                b_win += 1
    tot = 2 * n
    print(f"  {label:26s} A wins {pct(a_win, tot):>6}  B wins {pct(b_win, tot):>6}  ties {pct(tie, tot):>6}")


def main(n, seed):
    R, P = ("random",), ("perfect",)
    F = lambda k: ("forget", k)
    C, M, G = ("counter",), ("memory",), ("gambler",)
    S = seed * 10**8

    print(f"=== A. Natural end (stops at the true end), {n} games per row ===")
    natural_table("2P random v random", [R, R], n, S + 1 * 10**6)
    pp = natural_table("2P perfect v perfect", [P, P], n, S + 2 * 10**6)
    natural_table("2P forget10 v forget10", [F(10), F(10)], n, S + 3 * 10**6)
    natural_table("2P forget6 v forget6", [F(6), F(6)], n, S + 4 * 10**6)
    natural_table("2P forget4 v forget4", [F(4), F(4)], n, S + 5 * 10**6)
    natural_table("3P perfect x3", [P] * 3, n, S + 6 * 10**6)
    natural_table("4P perfect x4", [P] * 4, n, S + 7 * 10**6)
    natural_table("4P forget6 x4", [F(6)] * 4, n, S + 8 * 10**6)

    print("\n  Ending distribution, 2P perfect v perfect (cards left at the true end):")
    dist = Counter(r["left"] for r in pp)
    print("   " + "  ".join(f"{k}: {pct(v, len(pp))}" for k, v in sorted(dist.items())))
    print("  Pressed pair still present when the table first reaches k cards (2P perfect):")
    cells = []
    for k in (2, 4, 6, 8, 10):
        hits = [r["reached"][k] for r in pp if k in r["reached"]]
        cells.append(f"{k}: {pct(sum(hits), len(hits))} of {len(hits)}")
    print("   " + "  ".join(cells))
    fm = [r["first_match"] for r in pp]
    print(f"  First guess of the game is a blind match: {pct(sum(fm), len(fm))}")

    print(f"\n=== B. Memory head-to-head, natural end, seat-randomised ({2 * n} games per row) ===")
    head_to_head("perfect(A) v random(B)", P, R, n, S + 11 * 10**6)
    head_to_head("perfect(A) v forget10(B)", P, F(10), n, S + 12 * 10**6)
    head_to_head("perfect(A) v forget6(B)", P, F(6), n, S + 13 * 10**6)
    head_to_head("perfect(A) v forget4(B)", P, F(4), n, S + 14 * 10**6)
    head_to_head("forget6(A) v random(B)", F(6), R, n, S + 15 * 10**6)

    total_stalls = total_games = 0
    for pts in (1, 2):
        print(f"\n=== C. Sweep end rule, sweep worth {pts}, {n} games per row ===")
        rows = [
            ("2P counter v counter", [C, C]),
            ("2P memory v memory", [M, M]),
            ("2P gambler v gambler", [G, G]),
            ("2P counter(s0) v memory", [C, M]),
            ("2P memory(s0) v counter", [M, C]),
            ("2P counter(s0) v gambler", [C, G]),
            ("2P gambler(s0) v counter", [G, C]),
            ("3P counter x3", [C] * 3),
            ("4P counter x4", [C] * 4),
        ]
        for i, (label, kinds) in enumerate(rows):
            total_stalls += sweep_table(label, kinds, n, S + (20 + 10 * pts + i) * 10**6, pts)
            total_games += n
        print("  Seat-randomised head-to-heads:")
        sweep_h2h("counter(A) v memory(B)", C, M, n, S + (60 + pts) * 10**6, pts)
        sweep_h2h("counter(A) v gambler(B)", C, G, n, S + (70 + pts) * 10**6, pts)
        sweep_h2h("memory(A) v gambler(B)", M, G, n, S + (80 + pts) * 10**6, pts)
    print(f"\nSweep-rule stalls across all section-C rows: {total_stalls} of {total_games} games")

    print(f"\n=== D. Tiebreak rules, sweep worth 1, {n} games per row (seat win % shown, ties left over) ===")
    print("  shared = tied players share the win; sweeper = the successful sweeper wins a tie they are in;")
    print("  lastpair = whoever took the most recent pair wins a tie they are in")
    tiebreak_table("2P counter x2", [C, C], n, S + 90 * 10**6)
    tiebreak_table("2P memory x2", [M, M], n, S + 91 * 10**6)
    tiebreak_table("2P gambler x2", [G, G], n, S + 92 * 10**6)
    tiebreak_table("3P counter x3", [C] * 3, n, S + 93 * 10**6)
    tiebreak_table("3P memory x3", [M] * 3, n, S + 94 * 10**6)
    tiebreak_table("4P counter x4", [C] * 4, n, S + 95 * 10**6)
    tiebreak_table("4P memory x4", [M] * 4, n, S + 96 * 10**6)

    print(f"\n=== E. Lighter subset: signs 1-7 only (21 cards), {n} games per row ===")
    for label, kinds in (("2P perfect v perfect", [P, P]), ("2P forget4 v forget4", [F(4), F(4)])):
        res = [r for r in (play(kinds, S + 100 * 10**6 + i, None, 7) for i in range(n)) if r]
        g = [r["guesses"] for r in res]
        fm = [r["first_match"] for r in res]
        print(f"  {label:26s} natural end: ended {pct(len(res), n)}  guesses med {statistics.median(g):.0f} "
              f"max {max(g)}  cards left mean {statistics.mean(r['left'] for r in res):.1f}  "
              f"first guess blind match {pct(sum(fm), len(fm))}")
    for label, a, b in (("perfect(A) v forget4(B)", P, F(4)), ("perfect(A) v forget2(B)", P, F(2))):
        a_win = b_win = tie = 0
        for arm, kinds in enumerate(([a, b], [b, a])):
            for i in range(n):
                r = play(kinds, S + 110 * 10**6 + arm * 10**5 + i, None, 7)
                w = winners(r["scores"])
                if w == "tie":
                    tie += 1
                elif (w == 0) == (arm == 0):
                    a_win += 1
                else:
                    b_win += 1
        print(f"  {label:26s} 7 signs: A wins {pct(a_win, 2 * n)}  B wins {pct(b_win, 2 * n)}  ties {pct(tie, 2 * n)}")
    sub_stalls = 0
    for label, kinds in (("2P counter v counter", [C, C]), ("2P counter(s0) v memory", [C, M]),
                         ("2P memory(s0) v counter", [M, C]), ("2P gambler v gambler", [G, G])):
        res = [play(kinds, S + 120 * 10**6 + i, 1, 7) for i in range(n)]
        done = [r for r in res if r]
        sub_stalls += n - len(done)
        wins = Counter(resolve(r, "sweeper") for r in done)
        print(f"  {label:26s} 7 signs, sweep 1, sweeper-wins-ties: stalls {n - len(done)}/{n}  "
              f"guesses med {statistics.median(r['guesses'] for r in done):.0f}  "
              "wins " + ", ".join(f"{k}:{pct(v, len(done))}" for k, v in sorted(wins.items(), key=str)))
    print(f"  Subset sweep stalls: {sub_stalls}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run", action="store_true", help="run the full report")
    ap.add_argument("--games", type=int, default=2000, help="games per configuration")
    ap.add_argument("--seed", type=int, default=0, help="base seed (results are reproducible)")
    args = ap.parse_args()
    if args.run:
        main(args.games, args.seed)
    else:
        ap.print_help()
