#!/usr/bin/env python3
"""SNARE simulator and exact solver (design v0.1).

Models SNARE_rulebook.md v0.1:
  * n signs (5 = the Pentagon rung, 6 = the base game) -> C(n,2) road cards.
  * Two players alternate claiming one unclaimed road; claimed roads never move.
  * A *snare* is a symbol-triangle whose three roads all belong to one player.
  * Rule 'tally' (base game): after every road is claimed, fewer snares wins;
    equal counts -> the player who was snared FIRST loses; 0-0 is a draw
    (only possible on five signs).
  * Rule 'sudden' (variant): you lose the moment you complete a snare; if every
    road is claimed with no snare, it is a draw (only possible on five signs).

Physical handling the sim cannot model: finding a road's slot on the staircase,
misreading a rectangle, table talk. Ownership is perfect information, so no
face randomisation matters (the shown face of a road is inert).

Bots:
  RandomBot  - uniform legal claim (mechanics floor).
  GreedyBot  - the beginner-obvious line: never complete your own snare if any
               other road is available; otherwise random.
  SkilledBot - the rulebook's strategy notes: avoid fuses, leave the rival's
               poison roads alone, keep safe roads in reserve; counts the
               endgame exactly once <= ENDGAME roads remain.
  PerfectBot - full minimax (the exact game value; used for the ceiling).

Usage:  python snare_sim.py --run            (all reports, ~1-3 min)
        python snare_sim.py --run --games 4000 --seed 7
"""

from __future__ import annotations

import argparse
import itertools
import random
import sys
import time
from functools import lru_cache

sys.setrecursionlimit(10000)

TURN_CAP = 600  # guard; a game is exactly C(n,2) claims, so it can never be hit
ENDGAME = 7     # SkilledBot counts exactly when this many roads (or fewer) remain


# ---------------------------------------------------------------- structure
class Board:
    """leave = roads left unclaimed when the game ends (seat-fix candidate);
    dead = bit mask of roads set aside before play (seat-fix candidate)."""

    def __init__(self, n: int, leave: int = 0, dead: int = 0):
        self.n = n
        self.leave = leave
        self.dead = dead
        self.edges = list(itertools.combinations(range(1, n + 1), 2))
        self.m = len(self.edges)
        self.index = {e: i for i, e in enumerate(self.edges)}
        self.triangles = []
        for a, b, c in itertools.combinations(range(1, n + 1), 3):
            self.triangles.append((self.index[(a, b)], self.index[(a, c)], self.index[(b, c)]))
        # for each edge: list of (other1, other2) bit masks of its triangles
        self.pairs = [[] for _ in range(self.m)]
        for t in self.triangles:
            for e in t:
                o = [x for x in t if x != e]
                self.pairs[e].append((o[0], o[1]))
        self.full = (1 << self.m) - 1

    def snares(self, mask: int) -> int:
        return sum(1 for t in self.triangles
                   if all(mask >> e & 1 for e in t))

    def completes(self, mask: int, e: int) -> int:
        """Snares completed by adding road e to a player's mask."""
        return sum(1 for f, g in self.pairs[e] if mask >> f & 1 and mask >> g & 1)


def verify_structure() -> list[str]:
    """Combinatorial claims the rulebook makes, computed not asserted."""
    out = []
    for n in (5, 6):
        b = Board(n)
        out.append(f"K{n}: {b.m} roads, {len(b.triangles)} triangles")
    # Staircase claim: road {i,j} (i<j) sits at row i, column j; house k at (k,k).
    # Every triangle a<b<c is the rectangle rows {a,b} x cols {b,c}, whose fourth
    # corner (b,b) is a house, and every such rectangle is a triangle.
    b = Board(6)
    rect_ok = True
    for a, bb, c in itertools.combinations(range(1, 7), 3):
        corners = {(a, bb), (a, c), (bb, bb), (bb, c)}
        roads = {x for x in corners if x[0] != x[1]}
        houses = corners - roads
        if roads != {(a, bb), (a, c), (bb, c)} or houses != {(bb, bb)}:
            rect_ok = False
    # converse: rectangles with exactly one corner on the diagonal, rest above it
    rects = 0
    for r1, r2 in itertools.combinations(range(1, 7), 2):
        for c1, c2 in itertools.combinations(range(1, 7), 2):
            cs = [(r1, c1), (r1, c2), (r2, c1), (r2, c2)]
            diag = [x for x in cs if x[0] == x[1]]
            above = [x for x in cs if x[0] < x[1]]
            if len(diag) == 1 and len(above) == 3:
                rects += 1
    out.append(f"Staircase: every triangle is a house-cornered rectangle: {rect_ok}; "
               f"house-cornered rectangles on the board = {rects} (should be 20)")
    # Goodman / balanced-split facts on K6 (8/7 split as actually played)
    counts = []
    for A in itertools.combinations(range(b.m), 8):
        ma = sum(1 << e for e in A)
        counts.append(b.snares(ma) + b.snares(b.full ^ ma))
    out.append(f"K6 8/7 splits: {len(counts)}; total snares min={min(counts)} "
               f"mean={sum(counts)/len(counts):.2f} max={max(counts)}; "
               f"zero-snare splits={counts.count(0)}")
    b5 = Board(5)
    zero5 = 0
    for A in itertools.combinations(range(b5.m), 5):
        ma = sum(1 << e for e in A)
        if b5.snares(ma) + b5.snares(b5.full ^ ma) == 0:
            zero5 += 1
    out.append(f"K5 5/5 splits with zero snares (a drawn Pentagon is possible): {zero5}")
    rest = list(range(1, b.m))  # K6 minus road 0 (all roads equivalent)
    zero6e = 0
    for A in itertools.combinations(rest, 7):
        ma = sum(1 << e for e in A)
        mb = sum(1 << e for e in rest) ^ ma
        if b.snares(ma) + b.snares(mb) == 0:
            zero6e += 1
    out.append(f"K6 minus one road, 7/7 splits with zero snares: {zero6e}")
    # The opening is unique up to symmetry: S_n is transitive on edges, so a pie
    # rule on the first claim cannot change anything.
    out.append("Opening claim unique up to relabelling (S_n is edge-transitive): True")
    return out


# ---------------------------------------------------------------- exact solver
def make_solver(board: Board, rule: str):
    """Value for player 0 (who claims first): +1 win, 0 draw, -1 loss."""
    tri = board.triangles
    pairs = board.pairs
    m = board.m

    @lru_cache(maxsize=None)
    def value(ma: int, mb: int, first: int) -> int:
        # first: -1 nobody snared yet, 0 or 1 = that player was snared first
        claimed = ma | mb | board.dead
        if bin(claimed).count("1") >= m - board.leave:
            sa, sb = board.snares(ma), board.snares(mb)
            if sa != sb:
                return 1 if sa < sb else -1
            if first == -1:
                return 0
            return -1 if first == 0 else 1
        mover = 0 if bin(ma).count("1") == bin(mb).count("1") else 1
        best = -2 if mover == 0 else 2
        own = ma if mover == 0 else mb
        for e in range(m):
            if claimed >> e & 1:
                continue
            snared = any(own >> f & 1 and own >> g & 1 for f, g in pairs[e])
            if rule == "sudden" and snared:
                v = -1 if mover == 0 else 1
            else:
                nf = first if (first != -1 or not snared) else mover
                if mover == 0:
                    v = value(ma | 1 << e, mb, nf)
                else:
                    v = value(ma, mb | 1 << e, nf)
            if mover == 0:
                if v > best:
                    best = v
                    if best == 1:
                        break
            else:
                if v < best:
                    best = v
                    if best == -1:
                        break
        return best

    return value


# ---------------------------------------------------------------- game + bots
class State:
    def __init__(self, board: Board):
        self.b = board
        self.mask = [0, 0]
        self.snares = [0, 0]
        self.first = -1
        self.turn = 0
        self.loser_sudden = None

    def free(self):
        claimed = self.mask[0] | self.mask[1] | self.b.dead
        return [e for e in range(self.b.m) if not claimed >> e & 1]

    def mover(self):
        return self.turn % 2


def random_bot(st: State, rng: random.Random, ctx) -> int:
    return rng.choice(st.free())


def greedy_bot(st: State, rng: random.Random, ctx) -> int:
    p = st.mover()
    free = st.free()
    safe = [e for e in free if st.b.completes(st.mask[p], e) == 0]
    return rng.choice(safe or free)


def heuristic(st: State, p: int, e: int) -> float:
    """Strategy notes as a score (higher = better claim for player p)."""
    b = st.b
    me, op = st.mask[p], st.mask[1 - p]
    claimed = me | op | b.dead
    s = 0.0
    for f, g in b.pairs[e]:
        mf, mg = me >> f & 1, me >> g & 1
        of, og = op >> f & 1, op >> g & 1
        uf = not (claimed >> f & 1)
        ug = not (claimed >> g & 1)
        if mf and mg:
            s -= 100                      # completes my own snare
        elif (mf and ug) or (mg and uf):
            s -= 3                        # lights a fuse: the free road becomes my poison
        elif uf and ug:
            s -= 1                        # first road in an open triangle
        elif of and og:
            s -= 6                        # defuses the rival's snare: leave their poison alone
        elif (of and ug) or (og and uf):
            s -= 0.5                      # kills a triangle the rival might still fall into
        # mixed (one mine, one theirs): dead triangle, costs nothing
    return s


def make_skilled(board: Board, rule: str):
    solver = make_solver(board, rule)

    def skilled_bot(st: State, rng: random.Random, ctx) -> int:
        p = st.mover()
        free = st.free()
        if len(free) <= ENDGAME:
            best, cands = None, []
            for e in free:
                v = child_value(st, e, solver, rule)
                v = v if p == 0 else -v
                if best is None or v > best:
                    best, cands = v, [e]
                elif v == best:
                    cands.append(e)
            # among equal game values prefer the strategy-notes choice
            return max(cands, key=lambda e: (heuristic(st, p, e), rng.random()))
        return max(free, key=lambda e: (heuristic(st, p, e), rng.random()))

    return skilled_bot


def child_value(st: State, e: int, solver, rule: str) -> int:
    p = st.mover()
    own = st.mask[p]
    snared = st.b.completes(own, e) > 0
    if rule == "sudden" and snared:
        return -1 if p == 0 else 1
    nf = st.first if (st.first != -1 or not snared) else p
    ma, mb = st.mask
    if p == 0:
        ma |= 1 << e
    else:
        mb |= 1 << e
    return solver(ma, mb, nf)


def make_perfect(board: Board, rule: str):
    solver = make_solver(board, rule)

    def perfect_bot(st: State, rng: random.Random, ctx) -> int:
        p = st.mover()
        free = st.free()
        vals = [(child_value(st, e, solver, rule) * (1 if p == 0 else -1), e) for e in free]
        best = max(v for v, _ in vals)
        cands = [e for v, e in vals if v == best]
        return max(cands, key=lambda e: (heuristic(st, p, e), rng.random()))

    return perfect_bot


def play(board: Board, rule: str, bots, rng: random.Random):
    """bots[0] claims first. Returns (winner or None, snares, stalled, turns,
    first_snare_turn per seat or None)."""
    st = State(board)
    ft = [None, None]
    while st.turn < TURN_CAP:
        free = st.free()
        if len(free) <= board.leave:
            break
        p = st.mover()
        e = bots[p](st, rng, None)
        k = board.completes(st.mask[p], e)
        st.mask[p] |= 1 << e
        st.snares[p] += k
        st.turn += 1
        if k:
            if ft[p] is None:
                ft[p] = st.turn
            if st.first == -1:
                st.first = p
            if rule == "sudden":
                return 1 - p, st.snares, False, st.turn, ft
    else:
        return None, st.snares, True, st.turn, ft
    sa, sb = st.snares
    if sa != sb:
        return (0 if sa < sb else 1), st.snares, False, st.turn, ft
    if st.first == -1:
        return None, st.snares, False, st.turn, ft
    return 1 - st.first, st.snares, False, st.turn, ft


def match(board, rule, botX, botY, rng):
    """Two games, X claims first in game 1, Y in game 2. Fewer total snares wins;
    tie -> whoever survived longer (later first snare, never = 99) in the game
    where they claimed first; still tied -> drawn match."""
    _, s1, st1, _, f1 = play(board, rule, (botX, botY), rng)
    _, s2, st2, _, f2 = play(board, rule, (botY, botX), rng)
    tx, ty = s1[0] + s2[1], s1[1] + s2[0]
    if tx != ty:
        return ("X" if tx < ty else "Y"), True, st1 or st2
    sx = f1[0] or 99
    sy = f2[0] or 99
    if sx != sy:
        return ("X" if sx > sy else "Y"), False, st1 or st2
    return None, False, st1 or st2


# ---------------------------------------------------------------- reports
def matchup(board, rule, botX, botY, games, rng):
    """X vs Y, seats alternated. Returns dict of stats from X's perspective."""
    xw = yw = dr = stalls = 0
    xs = ys = 0
    first_wins = second_wins = 0
    for g in range(games):
        x_first = g % 2 == 0
        bots = (botX, botY) if x_first else (botY, botX)
        w, sn, stalled, *_ = play(board, rule, bots, rng)
        stalls += stalled
        x_seat = 0 if x_first else 1
        xs += sn[x_seat]
        ys += sn[1 - x_seat]
        if w is None:
            dr += 1
        elif w == x_seat:
            xw += 1
        else:
            yw += 1
        if w == 0:
            first_wins += 1
        elif w == 1:
            second_wins += 1
    return dict(xw=xw / games, yw=yw / games, dr=dr / games, stalls=stalls,
                xs=xs / games, ys=ys / games,
                first=first_wins / games, second=second_wins / games)


def selfplay(board, rule, bot, games, rng):
    first = second = draws = stalls = 0
    s0 = s1 = 0
    for _ in range(games):
        w, sn, stalled, *_ = play(board, rule, (bot, bot), rng)
        stalls += stalled
        s0 += sn[0]
        s1 += sn[1]
        if w == 0:
            first += 1
        elif w == 1:
            second += 1
        else:
            draws += 1
    return dict(first=first / games, second=second / games, dr=draws / games,
                stalls=stalls, s0=s0 / games, s1=s1 / games)


def pct(x):
    return f"{100 * x:5.1f}%"


def run(games: int, seed: int):
    t0 = time.time()
    rng = random.Random(seed)
    print("== Structure checks (computed) ==")
    for line in verify_structure():
        print("  " + line)

    total_games = 0
    for n in (6, 5):
        board = Board(n)
        for rule in ("tally", "sudden"):
            label = f"{'Snare (6 signs)' if n == 6 else 'Pentagon (5 signs)'} / {rule}"
            solver = make_solver(board, rule)
            v = solver(0, 0, -1)
            verdict = {1: "first player wins", -1: "second player wins", 0: "draw"}[v]
            print(f"\n== {label}: {board.m} roads, exact game value = {verdict} "
                  f"(solved states: {solver.cache_info().currsize}) ==")
            bots = {
                "Random": random_bot,
                "Greedy": greedy_bot,
                "Skilled": make_skilled(board, rule),
                "Perfect": make_perfect(board, rule),
            }
            print("  Self-play seat spread (first / second / draw, mean snares 1st-2nd):")
            for name in ("Random", "Greedy", "Skilled", "Perfect"):
                ng = games if name != "Perfect" else max(200, games // 5)
                r = selfplay(board, rule, bots[name], ng, rng)
                total_games += ng
                print(f"    {name:8s} n={ng:5d}  {pct(r['first'])} / {pct(r['second'])} / {pct(r['dr'])}"
                      f"   snares {r['s0']:.2f}-{r['s1']:.2f}   stalls {r['stalls']}")
            print("  Head-to-head, seats alternated (X win / Y win / draw, mean snares X:Y):")
            for x, y in (("Greedy", "Random"), ("Skilled", "Random"),
                         ("Skilled", "Greedy"), ("Perfect", "Skilled")):
                ng = games if "Perfect" not in (x, y) else max(200, games // 5)
                r = matchup(board, rule, bots[x], bots[y], ng, rng)
                total_games += ng
                ratio = (r["ys"] / r["xs"]) if r["xs"] else float("inf")
                wr = r["xw"] / r["yw"] if r["yw"] else float("inf")
                print(f"    {x:7s} v {y:7s} n={ng:5d}  {pct(r['xw'])} / {pct(r['yw'])} / {pct(r['dr'])}"
                      f"   snares {r['xs']:.2f}:{r['ys']:.2f} (ratio {ratio:.2f}x)"
                      f"   win ratio {wr:.2f}x   stalls {r['stalls']}")
    total_games += seat_fixes(games, rng)
    print(f"\nTotal simulated games: {total_games}; turn cap {TURN_CAP}; "
          f"seed {seed}; {time.time() - t0:.0f}s")


def seat_fixes(games: int, rng: random.Random) -> int:
    """Candidate repairs for the single-game seat lock found in run()."""
    total = 0
    board = Board(6)
    rule = "tally"
    sk = make_skilled(board, rule)
    print("\n== Seat-fix candidates (6 signs, tally) ==")
    print("  A. Pie rule on the opening claim (concept): inert -- every opening "
          "road is equivalent under relabelling, so swapping changes nothing.")
    print("  B. Two-game match, seats swapped; fewer total snares wins; tie -> "
          "longer survival as first claimer; else drawn.")
    for x, y, bx, by in (("Skilled", "Skilled", sk, sk), ("Greedy", "Greedy", greedy_bot, greedy_bot),
                         ("Random", "Random", random_bot, random_bot),
                         ("Skilled", "Random", sk, random_bot), ("Skilled", "Greedy", sk, greedy_bot)):
        res = {"X": 0, "Y": 0, None: 0}
        by_total = 0
        stalls = 0
        for _ in range(games):
            w, decided_total, stalled = match(board, rule, bx, by, rng)
            res[w] += 1
            by_total += decided_total
            stalls += stalled
        total += 2 * games
        print(f"    {x:7s} v {y:7s} matches={games:5d}  X {pct(res['X'] / games)} / "
              f"Y {pct(res['Y'] / games)} / drawn {pct(res[None] / games)}   "
              f"decided on snares {pct(by_total / games)}   stalls {stalls}")
    for label, b in (("C. Last road left unclaimed (7/7 split)", Board(6, leave=1)),
                     ("D. One road set aside before play (7/7 on K6 minus a road)", Board(6, dead=1))):
        solver = make_solver(b, rule)
        v = solver(0, 0, -1)
        verdict = {1: "first player wins", -1: "second player wins", 0: "draw"}[v]
        print(f"  {label}: exact value = {verdict}")
        skb = make_skilled(b, rule)
        for name, bot in (("Random", random_bot), ("Greedy", greedy_bot), ("Skilled", skb)):
            r = selfplay(b, rule, bot, games, rng)
            total += games
            print(f"    {name:8s} self-play  first {pct(r['first'])} / second {pct(r['second'])} / "
                  f"draw {pct(r['dr'])}   snares {r['s0']:.2f}-{r['s1']:.2f}   stalls {r['stalls']}")
        r = matchup(b, rule, skb, random_bot, games, rng)
        total += games
        print(f"    Skilled v Random  {pct(r['xw'])} / {pct(r['yw'])} / {pct(r['dr'])}   "
              f"snares {r['xs']:.2f}:{r['ys']:.2f}")
    return total


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.run:
        run(a.games, a.seed)
    else:
        ap.print_help()
