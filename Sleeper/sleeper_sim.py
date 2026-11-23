#!/usr/bin/env python3
"""SLEEPER v0.1a floor simulator (no talk, no Unmask).

Models: each player takes one loyalty card (Blind Cut: an unseen card),
chooses one of its signs as Master and shows the other as cover; 3 opening
Court cards; each turn reveals the top Court-deck card (both faces public)
and either Decrees it (adds it to the row, either face up) or Turns a coat
(spends it, flips any one Court card). The game ends when the Court deck is
empty (see the vetting note: "finish the go-around" is impossible once the
deck is empty, so the sim ends on the last card). Ruling sign = most-shown,
tie to the higher pip. Every player whose Master rules wins.

Also measures the REGISTRY LEAK: every revealed card is public, and the only
cards never revealed are the loyalty cards. A player's Master must be a sign
X such that the card {cover, X} has not been seen, so the public candidate
set shrinks as the deck runs down. Reported: mean public candidates per
player at 25/50/75/100% of the deck, and the share of masters pinned to one
candidate at the end.

Bots
  RandomBot   random master; random action and face.
  SkilledBot  picks the Master that is stronger in the opening row (pip as
              tiebreak); each turn takes the decree or coat-turn that best
              makes its Master rule now (margin over the strongest rival
              sign, pip tiebreak). Ignores others' loyalties (a floor).

Usage:  python sleeper_sim.py --games 2000 --seed 1
        python sleeper_sim.py --fixes --games 2000 --seed 1   # opt-in fix-option
            sweep (simultaneous / sealed final round, rotating end seat, Court
            cards set aside unseen); see SLEEPER_fix_options_sim_note.md.
            The default run is unchanged by these modes.
"""

from __future__ import annotations

import argparse
import random
import statistics
from collections import Counter
from itertools import combinations

DECK = [frozenset(p) for p in combinations(range(1, 10), 2)]


def other(card, s):
    (o,) = card - {s}
    return o


def ruling(row):
    cnt = Counter(s for _, s in row)
    top = max(cnt.values())
    return max(s for s, v in cnt.items() if v == top)


def margin(row, master):
    """>0 if master would rule now; scaled closeness otherwise."""
    cnt = Counter(s for _, s in row)
    mine = cnt.get(master, 0)
    best_other = max((v, s) for s, v in cnt.items() if s != master) if len(cnt) > (master in cnt) else (0, 0)
    v, s = best_other
    if mine > v or (mine == v and master > s):
        return 1 + (mine - v)
    return mine - v - 0.5


class RandomBot:
    def __init__(self, rng):
        self.rng = rng

    def master(self, card, row):
        return self.rng.choice(sorted(card))

    def act(self, g, p, card):
        if self.rng.random() < 0.5 or not g.row:
            return ("decree", self.rng.choice(sorted(card)))
        return ("turn", self.rng.randrange(len(g.row)))

    def seal(self, g, p, card):
        return self.rng.choice(sorted(card))


class SkilledBot:
    def __init__(self, rng):
        self.rng = rng

    def master(self, card, row):
        cnt = Counter(s for _, s in row)
        return max(sorted(card), key=lambda s: (cnt.get(s, 0), s))

    def act(self, g, p, card):
        m = g.masters[p]
        best = None
        for s in card:
            row = g.row + [(card, s)]
            key = (margin(row, m), self.rng.random())
            if best is None or key > best[0]:
                best = (key, ("decree", s))
        for i, (c, s) in enumerate(g.row):
            row = g.row[:i] + [(c, other(c, s))] + g.row[i + 1:]
            key = (margin(row, m), self.rng.random())
            if key > best[0]:
                best = (key, ("turn", i))
        return best[1]

    def seal(self, g, p, card):
        """Sealed decree: best face against the visible row plus every sealed
        decree this bot can read (its own, and any the registry pins)."""
        m = g.masters[p]
        view = g.row + g.sealed_view(p)
        return max(sorted(card), key=lambda s: (margin(view + [(card, s)], m), self.rng.random()))


class Game:
    def __init__(self, n, bots, rng, mode="base", aside=0):
        self.n, self.bots = n, bots
        self.mode = mode
        deck = DECK[:]
        rng.shuffle(deck)
        self.loyalty = deck[:n]  # blind cut: never seen by the table
        rest = deck[n:]
        self.row = []
        for _ in range(3):
            c = rest.pop()
            self.row.append((c, rng.choice(sorted(c))))
        # FIX OPTION (registry): `aside` Court cards set aside unseen at setup.
        self.aside = [rest.pop() for _ in range(aside)]
        self.seen = {c for c, _ in self.row}
        # FIX OPTION (rotate): burn d = (showing pip of the 3rd opening card) mod P
        # cards in public (both faces shown, onto the spent pile), so the seat
        # that takes the final turn varies game to game.
        self.burned = 0
        if mode == "rotate":
            self.burned = self.row[2][1] % n
            for _ in range(self.burned):
                self.seen.add(rest.pop())
        self.court = rest
        self.sealed = []  # (card, decree face, seat) laid pressed-face decrees
        self.masters = [bots[p].master(self.loyalty[p], self.row) for p in range(n)]
        self.covers = [other(self.loyalty[p], self.masters[p]) for p in range(n)]
        self.flips = 0

    def public_candidates(self, p, observer):
        """Masters still possible for p in the eyes of `observer` (who also knows own card)."""
        cover = self.covers[p]
        ruled_out = self.seen | ({self.loyalty[observer]} if observer != p else set())
        return [x for x in range(1, 10) if x != cover and frozenset((cover, x)) not in ruled_out]

    def play(self, first=0):
        total = len(self.court)
        marks = {int(total * f): f for f in (0.25, 0.5, 0.75)}
        cands = {}
        p, turn = first, 0
        final_round = self.mode in ("simul", "sealed")
        self.stalled = False
        while self.court and not (final_round and len(self.court) <= self.n):
            card = self.court.pop()
            self.seen.add(card)
            kind, x = self.bots[p].act(self, p, card)
            if kind == "decree":
                self.row.append((card, x))
            else:
                c, s = self.row[x]
                self.row[x] = (c, other(c, s))
                self.flips += 1
            turn += 1
            if turn in marks:
                cands[marks[turn]] = self.mean_cands()
            self.last_seat = p
            p = (p + 1) % self.n
            if turn > 600:  # termination guard (structurally unreachable)
                self.stalled = True
                break
        if final_round and self.court:
            turn = self._final_round(p, turn, marks, cands)
        self.turns = turn
        cands[1.0] = self.mean_cands()
        rule = ruling(self.row + [(c, f) for c, f, _ in self.sealed])
        winners = [q for q in range(self.n) if self.masters[q] == rule]
        pinned = sum(1 for q in range(self.n)
                     if len(self.public_candidates(q, (q + 1) % self.n)) == 1) / self.n
        return winners, rule, cands, pinned

    def _final_round(self, p, turn, marks, cands):
        """FIX OPTIONS (last mover): the last P Court cards are one final round,
        one card per player, dealt from p clockwise.
        simul  -- all P cards are revealed (both faces public); every player
                  chooses against the same pre-round row; all act at once.
                  Flips toggle the pre-round row (two flips on one card cancel).
        sealed -- each player in turn takes a card unseen by the others and
                  lays it in the row as a sealed decree, chosen sign pressed
                  DOWN (the public face is the sign it does NOT back); no
                  coat-turns this round; all sealed decrees flip up at the
                  reckoning."""
        n = self.n
        seats = [(p + k) % n for k in range(n)]
        cards = [self.court.pop() for _ in range(n)]
        if self.mode == "simul":
            self.seen.update(cards)
            acts = [self.bots[s].act(self, s, c) for s, c in zip(seats, cards)]
            toggles = Counter()
            for c, (kind, x) in zip(cards, acts):
                if kind == "decree":
                    self.row.append((c, x))
                else:
                    toggles[x] += 1
                    self.flips += 1
            for i, k in toggles.items():
                if k % 2:
                    c, s = self.row[i]
                    self.row[i] = (c, other(c, s))
        else:
            for s, c in zip(seats, cards):
                face = self.bots[s].seal(self, s, c)
                self.sealed.append((c, face, s))
        for _ in cards:
            turn += 1
            if turn in marks:
                cands[marks[turn]] = self.mean_cands()
        self.last_seat = seats[-1]
        return turn

    def sealed_view(self, observer):
        """Sealed decrees `observer` can read: their own, plus any whose pressed
        sign the public registry pins to a single candidate."""
        out = []
        own = {c for c, _, s in self.sealed if s == observer}
        for c, f, s in self.sealed:
            if s == observer:
                out.append((c, f))
                continue
            show = other(c, f)
            ruled = self.seen | {self.loyalty[observer]} | own
            cand = [x for x in range(1, 10) if x != show and frozenset((show, x)) not in ruled]
            if len(cand) == 1:
                out.append((c, cand[0]))
        return out

    def mean_cands(self):
        vals = [len(self.public_candidates(q, o)) for q in range(self.n) for o in range(self.n) if o != q]
        return statistics.mean(vals)


def run(n, games, table, seed, mode="base", aside=0):
    rng = random.Random(seed)
    seat_w, focus_w = Counter(), 0.0
    nowin = shared = 0
    last_w = stalls = 0
    turns_l = []
    rules = Counter()
    cands = {f: [] for f in (0.25, 0.5, 0.75, 1.0)}
    pinned_l = []
    for i in range(games):
        first = i % n
        focus = (i // n) % n
        if table == "random":
            bots = [RandomBot(rng) for _ in range(n)]
        elif table == "skilled":
            bots = [SkilledBot(rng) for _ in range(n)]
        else:
            bots = [RandomBot(rng) for _ in range(n)]
            bots[focus] = SkilledBot(rng)
        g = Game(n, bots, rng, mode, aside)
        winners, rule, c, pinned = g.play(first)
        rules[rule] += 1
        for f, v in c.items():
            cands[f].append(v)
        pinned_l.append(pinned)
        turns_l.append(g.turns)
        stalls += g.stalled
        if g.last_seat in winners:
            last_w += 1
        if not winners:
            nowin += 1
        if len(winners) > 1:
            shared += 1
        for w in winners:
            seat_w[(w - first) % n] += 1
        if table == "mixed" and focus in winners:
            focus_w += 1
    return {
        "nowin": nowin / games, "shared": shared / games,
        "focus": focus_w / games,
        "seat": [seat_w[s] / games for s in range(n)],
        "crown": rules[9] / games, "high": (rules[8] + rules[9]) / games,
        "cands": {f: statistics.mean(v) for f, v in cands.items()},
        "pinned": statistics.mean(pinned_l),
        "last": last_w / games, "turns": statistics.mean(turns_l),
        "stalls": stalls,
    }


FIX_ROWS = [
    ("baseline", "base", 0),
    ("(a) simultaneous final round", "simul", 0),
    ("(b) sealed final round", "sealed", 0),
    ("(c) rotating end seat", "rotate", 0),
    ("set aside 2 unseen", "base", 2),
    ("set aside 3 unseen", "base", 3),
    ("set aside 4 unseen", "base", 4),
    ("(a) + set aside 3", "simul", 3),
    ("(b) + set aside 3", "sealed", 3),
]


def fixes(games, seed):
    print(f"SLEEPER fix-option sweep · {games} games per table · seed {seed} · "
          "last mover = seat taking the final Court card (in deal order for (a)/(b))\n")
    hdr = (f"{'option':<30}{'P':>2}{'last-mover win':>15}{'others mean':>12}{'seat spread':>12}"
           f"{'skill x':>8}{'pinned':>8}{'turns':>7}{'no win':>8}{'shared':>8}{'stalls':>7}   skilled per-seat (from first)")
    print(hdr)
    for label, mode, aside in FIX_ROWS:
        for n in (4, 5, 6):
            r = {t: run(n, games, t, seed, mode, aside) for t in ("random", "skilled", "mixed")}
            sk = r["skilled"]
            others = (sum(sk["seat"]) - sk["last"]) / (n - 1)
            spread = max(sk["seat"]) - min(sk["seat"])
            base_rate = statistics.mean(r["random"]["seat"])
            mult = r["mixed"]["focus"] / base_rate if base_rate else float("nan")
            stalls = sum(x["stalls"] for x in r.values())
            print(f"{label:<30}{n:>2}{sk['last']:>15.1%}{others:>12.1%}{spread:>12.1%}{mult:>8.1f}"
                  f"{sk['pinned']:>8.0%}{sk['turns']:>7.1f}{sk['nowin']:>8.1%}{sk['shared']:>8.1%}{stalls:>7}   "
                  + " ".join(f"{s:.0%}" for s in sk["seat"]))
        print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--fixes", action="store_true",
                    help="run the opt-in fix-option sweep (see SLEEPER_fix_options_sim_note.md)")
    a = ap.parse_args()
    if a.fixes:
        fixes(a.games, a.seed)
        return
    print(f"SLEEPER v0.1a sim · {a.games} games per row · seed {a.seed} · ends when the Court deck empties (cannot stall)\n")
    print(f"{'P':>2} {'table':<8}{'no winner':>10}{'shared win':>11}{'focus wins':>11}{'Crown rules':>12}{'8/9 rules':>10}"
          f"   public master candidates @25/50/75/100%   pinned at end   per-seat win rate (from first)")
    for n in (4, 5, 6):
        for table in ("random", "skilled", "mixed"):
            r = run(n, a.games, table, a.seed)
            c = r["cands"]
            fw = f"{r['focus']:.1%}" if table == "mixed" else "-"
            print(f"{n:>2} {table:<8}{r['nowin']:>10.1%}{r['shared']:>11.1%}{fw:>11}{r['crown']:>12.1%}{r['high']:>10.1%}"
                  f"   {c[0.25]:.2f} / {c[0.5]:.2f} / {c[0.75]:.2f} / {c[1.0]:.2f}"
                  f"{r['pinned']:>17.0%}   " + " ".join(f"{s:.0%}" for s in r["seat"]))
        print()


if __name__ == "__main__":
    main()
