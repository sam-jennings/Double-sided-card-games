#!/usr/bin/env python3
"""DEADLOCK simulator (draft rulebook v0.1).

Models DEADLOCK_rulebook.md v0.1:
  * The full 36-card deck dealt into a 6x6 field, faces random, every card
    sideways ("open").
  * North and South alternate; North moves first. A move: choose any open
    card, show whichever of its two signs you like (keep or flip), and turn it
    to point at your seat. Claimed cards never move or flip again.
  * 36 moves, 18 each. Lines = 6 rows + 6 columns (+ 2 long diagonals in the
    Watchtower variant). A line is WON by whoever claimed 4+ of its 6 cards;
    3-3 lines score for nobody.
  * A won line scores the largest number of cards in it showing one sign
    (all six cards count, whoever claimed them).
  * Most points wins. Tie: more Crowns (sign 9) showing on your own claimed
    cards. Still tied: draw.

The shown face of an open card is only a default: the claimer may flip, so
both faces are always available. Everything is perfect information, so the
sim needs no face-memory model. Not modelled: knocked or mis-rotated cards,
misreading North vs South, the days between moves, table talk.

Bots:
  RandomBot  - uniform over (open card, face) - mechanics floor.
  GreedyBot  - the strategy notes as a one-ply score: each line is valued as
               P(win) - P(loss) times its likely value; flip to concentrate a
               sign in your lines and dilute it in theirs; poison lines you
               cannot win.
  SkilledBot - GreedyBot plus an exact search of the last ENDGAME claims.
  NoFlipBot  - SkilledBot forbidden to flip (must keep the shown face): the
               deck-necessity probe for value-setting. Its endgame search
               assumes the rival cannot flip either (a slight approximation).
  LookaheadBot - two-ply: the top LOOK_K one-ply moves, each scored against
               the rival's best one-ply reply; same endgame search. The depth
               check on seat fairness (a one-ply bot is a floor, not a ceiling).

Exact seat solve: not feasible. One deal has about 2.1e24 reachable positions
(sum over k of C(36,k) * C(k, ceil(k/2)) * 2^k: which cards are claimed, by whom,
showing which face), and every deal is a different game. Seat fairness is
measured by large seeded self-play instead, with a two-ply bot as a depth check.

Usage:  python deadlock_sim.py --run                    (all reports, a few minutes)
        python deadlock_sim.py --run --games 2000 --seed 1
"""

from __future__ import annotations

import argparse
import itertools
import math
import random
import time
from functools import lru_cache

TURN_CAP = 600   # guard: a game is exactly 36 claims, so it can never be hit
ENDGAME = 6      # SkilledBot searches exactly once this many cards remain
CROWN = 9
W_OPEN = 0.5     # GreedyBot: weight of an open card toward a sign's line value
LOOK_K = 12      # LookaheadBot: one-ply candidates examined two-ply
N, S = 1, 2

CARDS = list(itertools.combinations(range(1, 10), 2))  # the 36 pairs of K9


def make_lines(diagonals: bool):
    lines = [tuple(r * 6 + c for c in range(6)) for r in range(6)]
    lines += [tuple(r * 6 + c for r in range(6)) for c in range(6)]
    if diagonals:
        lines.append(tuple(i * 6 + i for i in range(6)))
        lines.append(tuple(i * 6 + (5 - i) for i in range(6)))
    return lines


@lru_cache(maxsize=None)
def race(n: int, s: int, t: int) -> tuple[float, float]:
    """(P North wins, P South wins) for a line at n-s with threshold t, if the
    open cards split as fair coin flips."""
    o = 6 - n - s
    a, b = t - n, t - s
    pn = sum(math.comb(o, k) for k in range(max(a, 0), o + 1)) / 2 ** o if a <= o else 0.0
    ps = sum(math.comb(o, k) for k in range(0, o - b + 1)) / 2 ** o if b <= o else 0.0
    if a <= 0:
        pn, ps = 1.0, 0.0
    if b <= 0:
        pn, ps = 0.0, 1.0
    return pn, ps


class Game:
    def __init__(self, rng: random.Random, diagonals: bool = False, threshold: int = 4):
        cards = CARDS[:]
        rng.shuffle(cards)
        self.card = cards
        self.face = [c[rng.randrange(2)] for c in cards]
        self.owner = [0] * 36
        self.t = threshold
        self.lines = make_lines(diagonals)
        self.L = len(self.lines)
        self.cell_lines = [[] for _ in range(36)]
        for li, cells in enumerate(self.lines):
            for c in cells:
                self.cell_lines[c].append(li)
        self.n = [0] * self.L
        self.s = [0] * self.L
        self.cnt = [[0] * 10 for _ in range(self.L)]      # shown signs, claimed cells
        self.opencnt = [[0] * 10 for _ in range(self.L)]  # open cells containing sign
        for li, cells in enumerate(self.lines):
            for c in cells:
                a, b = cards[c]
                self.opencnt[li][a] += 1
                self.opencnt[li][b] += 1
        self.open = set(range(36))
        self.crowns = [0, 0, 0]
        self.moves = 0
        self.memo = {}          # endgame transposition table (shared, zero-sum)
        self.eg_cells = None

    def to_move(self) -> int:
        # The rulebook's turn check: equal North and South counts -> North.
        return N if self.moves % 2 == 0 else S

    def play(self, c: int, sign: int, p: int):
        self.owner[c] = p
        self.face[c] = sign
        self.open.discard(c)
        a, b = self.card[c]
        for li in self.cell_lines[c]:
            if p == N:
                self.n[li] += 1
            else:
                self.s[li] += 1
            self.cnt[li][sign] += 1
            self.opencnt[li][a] -= 1
            self.opencnt[li][b] -= 1
        if sign == CROWN:
            self.crowns[p] += 1
        self.moves += 1

    def undo(self, c: int):
        p, sign = self.owner[c], self.face[c]
        self.owner[c] = 0
        self.open.add(c)
        a, b = self.card[c]
        for li in self.cell_lines[c]:
            if p == N:
                self.n[li] -= 1
            else:
                self.s[li] -= 1
            self.cnt[li][sign] -= 1
            self.opencnt[li][a] += 1
            self.opencnt[li][b] += 1
        if sign == CROWN:
            self.crowns[p] -= 1
        self.moves -= 1

    # --------------------------------------------------------------- scoring
    def scores(self):
        pn = ps = 0
        won_n = won_s = dead = 0
        values = []
        for li in range(self.L):
            v = max(self.cnt[li])
            if self.n[li] >= self.t:
                pn += v; won_n += 1; values.append(v)
            elif self.s[li] >= self.t:
                ps += v; won_s += 1; values.append(v)
            else:
                dead += 1
        return pn, ps, won_n, won_s, dead, values

    def result_key(self) -> int:
        """North-perspective lexicographic value: points first, then Crowns."""
        pn, ps = 0, 0
        t = self.t
        for li in range(self.L):
            if self.n[li] >= t:
                pn += max(self.cnt[li])
            elif self.s[li] >= t:
                ps += max(self.cnt[li])
        return (pn - ps) * 20 + (self.crowns[N] - self.crowns[S])

    # ----------------------------------------------------------- heuristic
    def line_eval(self, li: int) -> float:
        cnt, oc = self.cnt[li], self.opencnt[li]
        v = max(cnt[x] + W_OPEN * oc[x] for x in range(1, 10))
        pn, ps = race(self.n[li], self.s[li], self.t)
        return (pn - ps) * v

    def move_delta(self, c: int, sign: int, p: int) -> float:
        before = sum(self.line_eval(li) for li in self.cell_lines[c])
        self.play(c, sign, p)
        after = sum(self.line_eval(li) for li in self.cell_lines[c])
        self.undo(c)
        d = after - before + (0.05 if sign == CROWN else 0.0) * (1 if p == N else -1)
        return d if p == N else -d

    def evaluate(self) -> float:
        return sum(self.line_eval(li) for li in range(self.L))


# --------------------------------------------------------------------- bots
def random_bot(g: Game, rng: random.Random):
    c = rng.choice(sorted(g.open))
    return c, rng.choice(g.card[c])


def greedy_choice(g: Game, rng: random.Random, flip: bool = True):
    p = g.to_move()
    best, bestv = [], -1e9
    for c in g.open:
        faces = g.card[c] if flip else (g.face[c],)
        for f in faces:
            v = g.move_delta(c, f, p)
            if v > bestv + 1e-9:
                best, bestv = [(c, f)], v
            elif abs(v - bestv) <= 1e-9:
                best.append((c, f))
    best.sort()
    return rng.choice(best)


def solve(g: Game, key: int, flip: bool) -> int:
    """Exact North-perspective result_key with optimal play from here."""
    memo = g.memo
    mk = (key, flip)
    if mk in memo:
        return memo[mk]
    if not g.open:
        v = g.result_key()
        memo[mk] = v
        return v
    p = g.to_move()
    best = -10 ** 9 if p == N else 10 ** 9
    for i, c in enumerate(g.eg_cells):
        if g.owner[c]:
            continue
        faces = g.card[c] if flip else (g.face[c],)
        for fi, f in enumerate(faces):
            code = 1 + (p - 1) * 2 + (g.card[c].index(f))
            g.play(c, f, p)
            v = solve(g, key + code * 5 ** i, flip)
            g.undo(c)
            if p == N:
                best = max(best, v)
            else:
                best = min(best, v)
    memo[mk] = best
    return best


def endgame_key(g: Game) -> int:
    key = 0
    for i, c in enumerate(g.eg_cells):
        if g.owner[c]:
            key += (1 + (g.owner[c] - 1) * 2 + g.card[c].index(g.face[c])) * 5 ** i
    return key


def searched_choice(g: Game, rng: random.Random, flip: bool = True):
    if g.eg_cells is None:
        g.eg_cells = sorted(g.open)
    p = g.to_move()
    key = endgame_key(g)
    best, bestv = [], None
    for i, c in enumerate(g.eg_cells):
        if g.owner[c]:
            continue
        faces = g.card[c] if flip else (g.face[c],)
        for f in faces:
            code = 1 + (p - 1) * 2 + g.card[c].index(f)
            g.play(c, f, p)
            v = solve(g, key + code * 5 ** i, flip)
            g.undo(c)
            v = v if p == N else -v
            if bestv is None or v > bestv:
                best, bestv = [(c, f)], v
            elif v == bestv:
                best.append((c, f))
    best.sort()
    return rng.choice(best)


def lookahead_choice(g: Game, rng: random.Random, k: int = LOOK_K):
    """Two-ply: take the top-k one-ply moves, and for each assume the rival
    answers with their best one-ply reply; pick the best net result."""
    p = g.to_move()
    q = S if p == N else N
    cands = []
    for c in g.open:
        for f in g.card[c]:
            cands.append((g.move_delta(c, f, p), c, f))
    cands.sort(key=lambda x: -x[0])
    best, bestv = [], -1e9
    for d, c, f in cands[:k]:
        g.play(c, f, p)
        reply = 0.0
        if g.open:
            reply = max(g.move_delta(c2, f2, q) for c2 in g.open for f2 in g.card[c2])
        g.undo(c)
        v = d - reply
        if v > bestv + 1e-9:
            best, bestv = [(c, f)], v
        elif abs(v - bestv) <= 1e-9:
            best.append((c, f))
    best.sort()
    return rng.choice(best)


def lookahead_bot(g, rng):
    if len(g.open) <= ENDGAME:
        return searched_choice(g, rng, True)
    return lookahead_choice(g, rng)


def greedy_bot(g, rng):
    return greedy_choice(g, rng, True)


def skilled_bot(g, rng):
    if len(g.open) <= ENDGAME:
        return searched_choice(g, rng, True)
    return greedy_choice(g, rng, True)


def noflip_bot(g, rng):
    if len(g.open) <= ENDGAME:
        return searched_choice(g, rng, False)
    return greedy_choice(g, rng, False)


BOTS = {"Random": random_bot, "Greedy": greedy_bot,
        "Skilled": skilled_bot, "NoFlip": noflip_bot, "Lookahead": lookahead_bot}


# --------------------------------------------------------------------- games
def play_game(bot_n, bot_s, rng, diagonals=False, threshold=4):
    g = Game(rng, diagonals, threshold)
    info = {}
    turns = 0
    mixed = bot_n is not bot_s
    while g.open and turns < TURN_CAP:
        if len(g.open) == 10:
            info["live10"] = sum(
                1 for li in range(g.L)
                if g.n[li] < threshold and g.s[li] < threshold
                and (6 - g.n[li] - g.s[li]) >= min(threshold - g.n[li], threshold - g.s[li]))
            info["lead10"] = g.evaluate()
        p = g.to_move()
        if mixed and len(g.open) == ENDGAME:
            g.memo.clear()      # bots search with different move sets (NoFlip)
            g.eg_cells = None
        c, f = (bot_n if p == N else bot_s)(g, rng)
        if g.owner[c] or f not in g.card[c]:
            raise RuntimeError("illegal move")
        g.play(c, f, p)
        turns += 1
        # integrity check from the rulebook: North count - South count is 0 or 1
        nn = g.owner.count(N); ss = g.owner.count(S)
        assert nn - ss in (0, 1)
    stalled = bool(g.open)
    pn, ps, wn, ws, dead, values = g.scores()
    cn, cs = g.crowns[N], g.crowns[S]
    if pn != ps:
        w = N if pn > ps else S
        tb = False
    elif cn != cs:
        w = N if cn > cs else S
        tb = True
    else:
        w, tb = 0, False
    info.update(dict(w=w, pn=pn, ps=ps, wn=wn, ws=ws, dead=dead, values=values,
                     tb=tb, stalled=stalled, turns=turns, cn=cn, cs=cs))
    return info


def selfplay(name, games, seed, **kw):
    rng = random.Random(seed)
    bot = BOTS[name]
    res = [play_game(bot, bot, rng, **kw) for _ in range(games)]
    return res


def headtohead(x, y, games, seed, **kw):
    """X and Y alternate seats. Returns list of (info, x_is_north)."""
    rng = random.Random(seed)
    bx, by = BOTS[x], BOTS[y]
    out = []
    for i in range(games):
        if i % 2 == 0:
            out.append((play_game(bx, by, rng, **kw), True))
        else:
            out.append((play_game(by, bx, rng, **kw), False))
    return out


def ci(p, n):
    return 1.96 * math.sqrt(max(p * (1 - p), 1e-12) / n)


def report_self(label, res):
    n = len(res)
    wn = sum(r["w"] == N for r in res) / n
    ws = sum(r["w"] == S for r in res) / n
    dr = sum(r["w"] == 0 for r in res) / n
    tb = sum(r["tb"] for r in res) / n
    st = sum(r["stalled"] for r in res) / n
    mpn = sum(r["pn"] for r in res) / n
    mps = sum(r["ps"] for r in res) / n
    dead = sum(r["dead"] for r in res) / n
    won = sum(r["wn"] + r["ws"] for r in res) / n
    live = [r["live10"] for r in res if "live10" in r]
    lead_ok = [((r["lead10"] > 0 and r["w"] == N) or (r["lead10"] < 0 and r["w"] == S))
               for r in res if r["w"] and "lead10" in r and r["lead10"] != 0]
    vals = [v for r in res for v in r["values"]]
    vdist = {k: vals.count(k) / max(len(vals), 1) for k in range(1, 7)}
    # North score margin
    print(f"  {label:<28} N {wn:5.1%}  S {ws:5.1%}  draw {dr:4.1%}  (±{ci(wn, n):.1%})"
          f"  pts N {mpn:4.1f} / S {mps:4.1f}  lines won {won:4.1f} dead {dead:4.1f}"
          f"  crown-tiebreak {tb:4.1%}  stalls {st:.1%}")
    print(f"  {'':<28} live lines at 10 left {sum(live)/len(live):4.1f}"
          f"  leader at 10 left wins {sum(lead_ok)/max(len(lead_ok),1):5.1%}"
          f"  line values " + " ".join(f"{k}:{vdist[k]:.0%}" for k in range(1, 7)))
    # Post-hoc South compensation ("komi"): valid because no bot knows the komi
    # (they maximise margin, which a komi does not change).
    parts = []
    for k in (0.5, 1, 1.5, 2, 2.5):
        nw = sw = 0
        for r in res:
            m = r["pn"] - r["ps"] - k
            if m > 0:
                nw += 1
            elif m < 0:
                sw += 1
            else:   # integer komi tie -> Crowns, then draw
                tb = r["cn"] - r["cs"]
                nw += tb > 0; sw += tb < 0
        parts.append(f"+{k:g}: N {nw/n:.1%} / S {sw/n:.1%}")
    margins = [r["pn"] - r["ps"] for r in res]
    ties1 = sum(1 for m in margins if m == 1) / n
    nodraw = (sum(1 for m in margins if m >= 2) / n, sum(1 for m in margins if m <= 0) / n)
    print(f"  {'':<28} North margin mean {sum(margins)/n:+.2f}; South komi " + " | ".join(parts))
    print(f"  {'':<28} komi +1: tied after komi {ties1:.1%} (Crowns decide);"
          f" if a tie were a draw instead: N {nodraw[0]:.1%} / S {nodraw[1]:.1%} / draw {ties1:.1%}"
          f"; lines won N {sum(r['wn'] for r in res)/n:.2f} / S {sum(r['ws'] for r in res)/n:.2f}")
    return dict(wn=wn, ws=ws, dr=dr)


def report_match(res):
    """Seat-swapped two-field match, built from consecutive self-play games:
    player A is North in the first field and South in the second."""
    a = b = tied = 0
    m = len(res) // 2
    for i in range(0, 2 * m, 2):
        x = res[i]["pn"] + res[i + 1]["ps"]
        y = res[i]["ps"] + res[i + 1]["pn"]
        if x == y:
            tied += 1
            x = res[i]["cn"] + res[i + 1]["cs"]
            y = res[i]["cs"] + res[i + 1]["cn"]
        a += x > y
        b += y > x
    print(f"  {'Skilled two-field match':<28} A {a/m:5.1%}  B {b/m:5.1%}  drawn {(m-a-b)/m:4.1%}"
          f"  tied on points {tied/m:4.1%} (Crowns decide)  (matches={m}, ±{ci(0.5, m):.1%})")


def report_h2h(x, y, out):
    n = len(out)
    xw = yw = d = 0
    xp = yp = 0
    for r, xn in out:
        px, py = (r["pn"], r["ps"]) if xn else (r["ps"], r["pn"])
        xp += px; yp += py
        if r["w"] == 0:
            d += 1
        elif (r["w"] == N) == xn:
            xw += 1
        else:
            yw += 1
    print(f"  {x+' v '+y:<20} {x} wins {xw/n:5.1%}  {y} wins {yw/n:5.1%}  draws {d/n:4.1%}"
          f"  points {xp/n:4.1f} : {yp/n:4.1f}  ratio {xp/max(yp,1e-9):4.2f}x  (n={n})")


# ---------------------------------------------------------------- structure
def verify_structure(seed: int) -> list[str]:
    out = []
    from collections import Counter
    deg = Counter(x for c in CARDS for x in c)
    out.append(f"Deck: {len(CARDS)} cards, every sign on {set(deg.values())} cards; "
               f"6x6 field uses all {6*6} exactly")
    lines = make_lines(False)
    per = Counter(c for l in lines for c in l)
    out.append(f"Rows+columns: {len(lines)} lines; every cell in {set(per.values())} lines")
    # Line value range over random 6-card lines: min and max achievable by face choice
    rng = random.Random(seed)
    mins, maxs = Counter(), Counter()
    samples = 20000
    for _ in range(samples):
        line = rng.sample(CARDS, 6)
        best_min, best_max = 7, 0
        for faces in itertools.product((0, 1), repeat=6):
            v = max(Counter(line[i][faces[i]] for i in range(6)).values())
            best_min = min(best_min, v); best_max = max(best_max, v)
        mins[best_min] += 1; maxs[best_max] += 1
    out.append("Random 6-card lines (n=%d): lowest achievable value " % samples
               + ", ".join(f"{k}: {v/samples:.1%}" for k, v in sorted(mins.items()))
               + " | highest achievable value "
               + ", ".join(f"{k}: {v/samples:.1%}" for k, v in sorted(maxs.items())))
    # Can a line ever be forced to 1 / reach 6? Exact over all C(36,6) is 1.9M lines;
    # theory: value 1 needs six distinct shown signs (a system of distinct reps);
    # value 6 needs six cards sharing one sign (each sign is on 8 cards).
    out.append(f"Value 6 possible: a sign is on 8 cards, so up to 6 can share a line: True")
    out.append("Turn check: North moves on equal counts, South when North has one more; "
               "any other difference means the field was disturbed (asserted every move)")
    return out


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--quick", action="store_true", help="smoke test, 100 games")
    a = ap.parse_args()
    if not a.run:
        ap.print_help(); return
    G = 100 if a.quick else a.games
    seed = a.seed
    t0 = time.time()
    total = 0
    print(f"DEADLOCK sim v0.1 - seed {seed}, {G} games per row, turn cap {TURN_CAP}, "
          f"endgame search {ENDGAME}\n")
    print("Structure checks")
    for line in verify_structure(seed):
        print("  " + line)

    for diag, label in ((False, "BASE (rows + columns, 12 lines)"),
                        (True, "WATCHTOWER variant (+ 2 diagonals, 14 lines)")):
        print(f"\n{label}\n Self-play seat spread")
        bots = ("Random", "Greedy", "Skilled") + (() if diag else ("Lookahead",))
        for b in bots:
            n = G * 2 if b == "Random" else G
            res = selfplay(b, n, seed + 11, diagonals=diag)
            report_self(b, res)
            total += n
            if b == "Skilled" and not diag:
                report_match(res)
        if not diag:
            report_self("Skilled (second seed)", selfplay("Skilled", G, seed + 101))
            total += G
        print(" Head-to-head, seats alternated")
        pairs = [("Greedy", "Random"), ("Skilled", "Random"), ("Skilled", "Greedy")]
        if not diag:
            pairs += [("Skilled", "NoFlip"), ("Lookahead", "Skilled")]
        for x, y in pairs:
            n = G
            report_h2h(x, y, headtohead(x, y, n, seed + 23, diagonals=diag))
            total += n
        print(f"  [{time.time()-t0:.0f}s elapsed]")
    print(f"\nTotal games: {total}, stalls: 0 possible (36 claims exactly), "
          f"time {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
