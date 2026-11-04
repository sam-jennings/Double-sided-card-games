#!/usr/bin/env python3
"""LODGE v0.1 floor simulator.

Models the draft rulebook: 4-card lodges scored on the pressed face, stock
(whose top face is public) and pond, keep-by-choosing-the-pressed-face,
Eye peek / Mask blind swap / Star turn from stock discards, knock with one
final turn each, and the stock running out ending the round.

Rule switches:
  --recycle   when the stock first runs out, wash the pond (except its top
              card) into a new stock; the second exhaustion ends the round.
  --no-star   Still Water variant (Eye and Mask only).

Knowledge is tracked per player per lodge slot (who knows which pressed face),
including the public leak when a kept card's pressed face is the one the table
saw on top of the stock. Not modelled: table talk, bluffing, memory errors, and
bots do not exploit the pair registry beyond the shown face (a floor, not a
ceiling).

Usage:  python lodge_sim.py --players 4 --games 5000 --seed 1
"""

from __future__ import annotations

import argparse
import random
import statistics
from collections import Counter
from itertools import combinations

DECK = list(combinations(range(1, 10), 2))
EYE, MASK, STAR = 5, 6, 8
TURN_CAP = 400


def cond_est(shown: int) -> float:
    """Expected pressed pip given only the shown sign (partners average)."""
    return (45 - shown) / 8


class Game:
    def __init__(self, n, bots, rng, recycle=False, star=True):
        self.n, self.bots, self.rng = n, bots, rng
        self.recycle, self.recycled = recycle, False
        self.powers = {EYE, MASK} | ({STAR} if star else set())
        deck = DECK[:]
        rng.shuffle(deck)
        self.stock = [(c, rng.randrange(2)) for c in deck]  # (card, up index)
        # lodge[p][j] = [card, pressed index]; dealt by sliding, unturned
        self.lodge = []
        for _ in range(n):
            row = []
            for _ in range(4):
                c, up = self.stock.pop()
                row.append([c, 1 - up])
            self.lodge.append(row)
        c, up = self.stock.pop()
        self.pond = [(c, up, set())]  # (card, up index, players knowing both faces)
        # K[x][q][j] = pip x knows is pressed in q's slot j, else None
        self.K = [[[None] * 4 for _ in range(n)] for _ in range(n)]
        for p in range(n):
            for j in (0, 3):
                self.K[p][p][j] = self.pressed(p, j)
        self.power_uses = Counter()

    # --- views -------------------------------------------------------
    def pressed(self, q, j):
        c, pi = self.lodge[q][j]
        return c[pi]

    def shown(self, q, j):
        c, pi = self.lodge[q][j]
        return c[1 - pi]

    def est(self, x, q, j):
        k = self.K[x][q][j]
        return k if k is not None else cond_est(self.shown(q, j))

    def everyone(self):
        return set(range(self.n))

    # --- actions -----------------------------------------------------
    def place(self, p, j, card, pi, knowers):
        old_c, old_pi = self.lodge[p][j]
        # replaced card turned onto the pond: both faces now public
        self.pond.append((old_c, old_pi, self.everyone()))
        self.lodge[p][j] = [card, pi]
        for x in range(self.n):
            self.K[x][p][j] = card[pi] if x in knowers else None

    def swap(self, p, i, q, j):
        self.lodge[p][i], self.lodge[q][j] = self.lodge[q][j], self.lodge[p][i]
        for x in range(self.n):
            self.K[x][p][i], self.K[x][q][j] = self.K[x][q][j], self.K[x][p][i]

    def turn(self, q, j):
        self.lodge[q][j][1] ^= 1
        for x in range(self.n):
            self.K[x][q][j] = self.pressed(q, j)

    def take_turn(self, p):
        bot = self.bots[p]
        if bot.choose_pond(self, p):
            card, up, knowers = self.pond.pop()
            j, pi = bot.place_known(self, p, card, from_pond=True)
            k = knowers | {p}
            if pi == up:  # pressed the face the table could see
                k = self.everyone()
            self.place(p, j, card, pi, k)
            return
        card, up = self.stock.pop()
        act = bot.play_stock(self, p, card, up)
        if act[0] == "keep":
            _, j, pi = act
            self.place(p, j, card, pi, self.everyone() if pi == up else {p})
            return
        _, face, power = act
        knowers = {p} if face == up else self.everyone()
        self.pond.append((card, face, knowers))
        if power is None:
            return
        kind = power[0]
        self.power_uses[kind] += 1
        if kind == "peek":
            j = power[1]
            self.K[p][p][j] = self.pressed(p, j)
        elif kind == "swap":
            self.swap(p, power[1], power[2], power[3])
        elif kind == "turn":
            self.turn(power[1], power[2])

    def play(self, first=0):
        turns, knocker, final_left = 0, None, None
        p = first
        while True:
            self.take_turn(p)
            turns += 1
            if not self.stock:
                if self.recycle and not self.recycled and len(self.pond) > 1:
                    top = self.pond.pop()
                    rest = [c for c, _, _ in self.pond]
                    self.rng.shuffle(rest)
                    self.stock = [(c, self.rng.randrange(2)) for c in rest]
                    self.pond = [top]
                    self.recycled = True
                else:
                    return self.finish(turns, "stock")
            if final_left is not None:
                final_left -= 1
                if final_left == 0:
                    return self.finish(turns, "knock")
            elif self.bots[p].knock(self, p, turns):
                knocker, final_left = p, self.n - 1
            if turns >= TURN_CAP:
                return self.finish(turns, "stall")
            p = (p + 1) % self.n

    def finish(self, turns, reason):
        scores = [sum(self.pressed(q, j) for j in range(4)) for q in range(self.n)]
        return scores, turns, reason


# --- bots ------------------------------------------------------------
class RandomBot:
    name = "random"

    def __init__(self, rng):
        self.rng = rng
        self.my_turns = 0

    def choose_pond(self, g, p):
        self.my_turns += 1
        return self.rng.random() < 0.5

    def place_known(self, g, p, card, from_pond=False):
        return self.rng.randrange(4), self.rng.randrange(2)

    def play_stock(self, g, p, card, up):
        r = self.rng
        if r.random() < 0.5:
            return ("keep", r.randrange(4), r.randrange(2))
        face = r.randrange(2)
        v = card[face]
        if v not in g.powers:
            return ("discard", face, None)
        q = r.choice([x for x in range(g.n) if x != p])
        if v == EYE:
            return ("discard", face, ("peek", r.randrange(4)))
        if v == MASK:
            return ("discard", face, ("swap", r.randrange(4), q, r.randrange(4)))
        tgt = r.choice([p, q])
        return ("discard", face, ("turn", tgt, r.randrange(4)))

    def knock(self, g, p, turns):
        return self.my_turns >= 3 and self.rng.random() < 0.08


class SkilledBot:
    """Public-information heuristic: keep low, use powers for clear gains,
    swap known-heavy cards for rival cards it can read, knock when light."""

    name = "skilled"

    def __init__(self, rng, knock_at=12, risk=0.15):
        self.rng, self.knock_at, self.risk = rng, knock_at, risk

    def own_total(self, g, p):
        return sum(g.est(p, p, j) for j in range(4))

    def best_keep(self, g, p, card):
        best = (-99.0, 0, 0)
        for j in range(4):
            old = g.est(p, p, j)
            old_risk = self.risk * max(0, g.shown(p, j) - old)
            for pi in (0, 1):
                new, sh = card[pi], card[1 - pi]
                gain = old - new - self.risk * max(0, sh - new) + old_risk
                if gain > best[0]:
                    best = (gain, j, pi)
        return best

    def choose_pond(self, g, p):
        card, up, knowers = g.pond[-1]
        if p in knowers:
            return self.best_keep(g, p, card)[0] > 1.0
        # only the visible face is known
        v = card[up]
        worst = max(g.est(p, p, j) for j in range(4))
        return worst - v > 2.5

    def place_known(self, g, p, card, from_pond=False):
        _, j, pi = self.best_keep(g, p, card)
        return j, pi

    def leader(self, g, p):
        rivals = [q for q in range(g.n) if q != p]
        return min(rivals, key=lambda q: sum(g.est(p, q, j) for j in range(4)))

    def power_options(self, g, p, v):
        opts = []
        rivals = [q for q in range(g.n) if q != p]
        lead = self.leader(g, p)
        if v == EYE:
            unk = [j for j in range(4) if g.K[p][p][j] is None]
            if unk:
                j = max(unk, key=lambda j: g.est(p, p, j))
                opts.append((1.2, ("peek", j)))
        elif v == MASK:
            for i in range(4):
                for q in rivals:
                    for j in range(4):
                        gain = g.est(p, p, i) - g.est(p, q, j)
                        gain += 0.3 * gain if q == lead else 0
                        opts.append((gain, ("swap", i, q, j)))
        elif v == STAR:
            for j in range(4):
                opts.append((g.est(p, p, j) - g.shown(p, j), ("turn", p, j)))
            for q in rivals:
                w = 0.6 if q == lead else 0.3
                for j in range(4):
                    opts.append((w * (g.shown(q, j) - g.est(p, q, j)), ("turn", q, j)))
        return opts

    def play_stock(self, g, p, card, up):
        gain, j, pi = self.best_keep(g, p, card)
        best = (gain, ("keep", j, pi))
        for face in (0, 1):
            v = card[face]
            if v in g.powers:
                for pg, act in self.power_options(g, p, v):
                    if pg > best[0]:
                        best = (pg, ("discard", face, act))
        if best[0] > 0.5:
            return best[1]
        return ("discard", 0, None)

    def knock(self, g, p, turns):
        mine = self.own_total(g, p)
        rivals = [sum(g.est(p, q, j) for j in range(4)) for q in range(g.n) if q != p]
        return mine <= self.knock_at and mine < min(rivals)


# --- harness ---------------------------------------------------------
def run(n, games, table, recycle, star, seed):
    rng = random.Random(seed)
    turns_pp, reasons, seat_wins = [], Counter(), Counter()
    skilled_scores, random_scores, skilled_share = [], [], 0.0
    uses = Counter()
    for g_i in range(games):
        if table == "skilled":
            kinds = ["S"] * n
        elif table == "random":
            kinds = ["R"] * n
        else:  # one skilled seat, rotating
            kinds = ["R"] * n
            kinds[g_i % n] = "S"
        bots = [SkilledBot(rng) if k == "S" else RandomBot(rng) for k in kinds]
        game = Game(n, bots, rng, recycle=recycle, star=star)
        first = g_i % n
        scores, turns, reason = game.play(first)
        turns_pp.append(turns / n)
        reasons[reason] += 1
        uses += game.power_uses
        low = min(scores)
        winners = [q for q in range(n) if scores[q] == low]
        for q in winners:
            seat_wins[(q - first) % n] += 1 / len(winners)
            if kinds[q] == "S" and table == "mixed":
                skilled_share += 1 / len(winners)
        for q in range(n):
            (skilled_scores if kinds[q] == "S" else random_scores).append(scores[q])
    out = {
        "turns_pp": statistics.mean(turns_pp),
        "turns_p90": sorted(turns_pp)[int(0.9 * games)],
        "knock": reasons["knock"] / games,
        "stock": reasons["stock"] / games,
        "stall": reasons["stall"] / games,
        "seat": [seat_wins[s] / games for s in range(n)],
        "uses_pg": {k: uses[k] / games for k in ("peek", "swap", "turn")},
    }
    if skilled_scores:
        out["skilled_score"] = statistics.mean(skilled_scores)
    if random_scores:
        out["random_score"] = statistics.mean(random_scores)
    if table == "mixed":
        out["skilled_win"] = skilled_share / games
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--players", type=int, default=4)
    ap.add_argument("--games", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    n = a.players
    rules = [("base", False, True), ("recycle", True, True), ("still water", False, False)]
    print(f"LODGE v0.1 sim · {n} players · {a.games} games per row · seed {a.seed}\n")
    print(f"{'rules':<12}{'table':<9}{'turns/pl':>9}{'p90':>6}{'knock':>7}{'stock':>7}"
          f"{'stall':>7}{'S score':>9}{'R score':>9}{'S win':>7}  powers/game (peek swap turn)  seat wins")
    for rname, rec, star in rules:
        for table in ("skilled", "mixed", "random"):
            r = run(n, a.games, table, rec, star, a.seed)
            u = r["uses_pg"]
            print(f"{rname:<12}{table:<9}{r['turns_pp']:>9.1f}{r['turns_p90']:>6.1f}"
                  f"{r['knock']:>7.0%}{r['stock']:>7.0%}{r['stall']:>7.1%}"
                  f"{r.get('skilled_score', float('nan')):>9.1f}"
                  f"{r.get('random_score', float('nan')):>9.1f}"
                  f"{r.get('skilled_win', float('nan')):>7.0%}"
                  f"  {u['peek']:.1f} {u['swap']:.1f} {u['turn']:.1f}"
                  f"   {' '.join(f'{s:.0%}' for s in r['seat'])}")


if __name__ == "__main__":
    main()
