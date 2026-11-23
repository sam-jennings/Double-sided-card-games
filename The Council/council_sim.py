#!/usr/bin/env python3
"""THE COUNCIL v1.0 (+ v1.0a handling clarifications) floor simulator.

Models: hands of 4, issue deck of the rest (random faces), 4 rounds; each
round tables 3 issues (same-symbol issues join one stack, worth the sum of
its pips), everyone commits one card simultaneously, the committed cards'
other faces are then shown to the table (v1.0a), a turncoat phase in seat
order from the Speaker's left (Speaker last) where each player may flip once,
then resolution: a lone supporter takes the whole stack; deadlocked or
unsupported stacks roll over. Speaker rotates left each round. Scores are
pips carried; tiebreak most cards, then most recent carry.

Negotiation and table talk are NOT modelled -- this is a floor for the card
logic: termination (structural), skill gap, seat/flip-order fairness, and how
often stacks roll over.

Bots
  RandomBot   random card, random face; flips 30% of the time.
  SkilledBot  commits the card/face whose stack is biggest after discounting
              for how many rivals could plausibly reach it (by either face);
              in the turncoat phase it compares its two faces, simulating the
              later seats as greedy one-step players, and picks the better.

Usage:  python council_sim.py --games 5000 --seed 1
"""

from __future__ import annotations

import argparse
import math
import random
import statistics
from collections import Counter, defaultdict
from itertools import combinations

DECK = [frozenset(p) for p in combinations(range(1, 10), 2)]
ROUNDS, ISSUES_PER_ROUND, HAND = 4, 3, 4


def other(card, s):
    (o,) = card - {s}
    return o


def resolve(stacks, faces):
    """faces: {player: symbol}. Returns {player: (symbol, value)} for lone supporters."""
    sup = defaultdict(list)
    for p, s in faces.items():
        if s in stacks:
            sup[s].append(p)
    return {ps[0]: s for s, ps in sup.items() if len(ps) == 1}


class Game:
    def __init__(self, n, bots, rng):
        self.n, self.bots, self.rng = n, bots, rng
        deck = DECK[:]
        rng.shuffle(deck)
        self.hands = [set(deck[i * HAND:(i + 1) * HAND]) for i in range(n)]
        self.issue_deck = deck[n * HAND:]
        self.stacks = {}  # symbol -> [pips...]
        self.seen = set()  # cards whose both faces are public
        self.score = [0] * n
        self.carried = [0] * n
        self.last_carry = [-1] * n
        self.stats = Counter()

    def value(self, s):
        return sum(self.stacks.get(s, []))

    def play(self, speaker=0):
        for rnd in range(ROUNDS):
            for _ in range(ISSUES_PER_ROUND):
                card = self.issue_deck.pop()
                self.seen.add(card)
                s = self.rng.choice(sorted(card))  # random face lands as the issue
                self.stacks.setdefault(s, []).append(s)
            self.stats["stacks_tabled"] += len(self.stacks)
            # commitment (simultaneous)
            commits = {}
            for p in range(self.n):
                card, face = self.bots[p].commit(self, p)
                self.hands[p].remove(card)
                commits[p] = [card, face]
            for card, _ in commits.values():
                self.seen.add(card)  # v1.0a: other faces shown to the table
            # turncoat phase: left of speaker first, speaker last
            order = [(speaker + k) % self.n for k in range(1, self.n + 1)]
            for i, p in enumerate(order):
                if self.bots[p].flip(self, p, commits, order[i + 1:]):
                    c, f = commits[p]
                    commits[p][1] = other(c, f)
                    self.stats["flips"] += 1
            faces = {p: f for p, (c, f) in commits.items()}
            winners = resolve(self.stacks, faces)
            for p, s in winners.items():
                self.score[p] += self.value(s)
                self.carried[p] += len(self.stacks[s])
                self.last_carry[p] = rnd
                del self.stacks[s]
                self.stats["carries"] += 1
            self.stats["rollovers"] += len(self.stacks)
            speaker = (speaker + 1) % self.n
        self.stats["rotted_pips"] += sum(self.value(s) for s in self.stacks)
        key = [(self.score[p], self.carried[p], self.last_carry[p]) for p in range(self.n)]
        best = max(key)
        return [p for p in range(self.n) if key[p] == best]


class RandomBot:
    def __init__(self, rng):
        self.rng = rng

    def commit(self, g, p):
        card = self.rng.choice(sorted(g.hands[p], key=sorted))
        return card, self.rng.choice(sorted(card))

    def flip(self, g, p, commits, later):
        return self.rng.random() < 0.3


class SkilledBot:
    def __init__(self, rng, k=1.0):
        self.rng, self.k = rng, k

    def reach(self, g, p, s):
        """Expected number of rivals able to show s (by either face) from unknown cards."""
        unknown = [c for c in DECK if c not in g.seen and c not in g.hands[p]]
        if not unknown:
            return 0.0
        frac = sum(1 for c in unknown if s in c) / len(unknown)
        hand = len(g.hands[p])  # rivals hold as many cards as I do
        return (g.n - 1) * (1 - (1 - frac) ** hand)

    def sym_value(self, g, p, s):
        v = g.value(s)
        if not v:
            return 0.0
        total = sum(g.value(t) for t in g.stacks) or 1
        rivals = self.reach(g, p, s) * (v / total) * len(g.stacks)
        return v * math.exp(-self.k * rivals)

    def commit(self, g, p):
        best = None
        for card in g.hands[p]:
            a, b = sorted(card)
            va, vb = self.sym_value(g, p, a), self.sym_value(g, p, b)
            face = a if va >= vb else b
            # spend the card whose best use is greatest now; keep weak cards for later
            score = (max(va, vb) + 0.25 * min(va, vb), self.rng.random())
            if best is None or score > best[0]:
                best = (score, card, face)
        return best[1], best[2]

    @staticmethod
    def payoff(g, faces, p):
        win = resolve(g.stacks, faces)
        return g.value(win[p]) if p in win else 0

    def greedy_rest(self, g, commits, faces, later):
        faces = dict(faces)
        for q in later:
            c, f = commits[q]
            alt = dict(faces)
            alt[q] = other(c, f)
            if self.payoff(g, alt, q) > self.payoff(g, faces, q):
                faces = alt
        return faces

    def flip(self, g, p, commits, later):
        faces = {q: f for q, (c, f) in commits.items()}
        c, f = commits[p]
        stay = self.payoff(g, self.greedy_rest(g, commits, faces, later), p)
        alt = dict(faces)
        alt[p] = other(c, f)
        go = self.payoff(g, self.greedy_rest(g, commits, alt, later), p)
        return go > stay


def run(n, games, table, seed):
    rng = random.Random(seed)
    seat_w, focus_w = Counter(), 0.0
    scores = defaultdict(list)
    tot = Counter()
    for i in range(games):
        speaker = i % n
        focus = (i // n) % n  # rotates independently of the first Speaker
        if table == "random":
            kinds = ["R"] * n
        elif table == "skilled":
            kinds = ["S"] * n
        else:
            kinds = ["R"] * n
            kinds[focus] = "S"
        bots = [SkilledBot(rng) if k == "S" else RandomBot(rng) for k in kinds]
        g = Game(n, bots, rng)
        winners = g.play(speaker)
        tot += g.stats
        for w in winners:
            # seat measured from the first Speaker: 0 = first Speaker (flips last in round 1)
            seat_w[(w - speaker) % n] += 1 / len(winners)
            if table == "mixed" and w == focus:
                focus_w += 1 / len(winners)
        for p in range(n):
            scores[kinds[p]].append(g.score[p])
    return {
        "seat": [seat_w[s] / games for s in range(n)],
        "focus": focus_w / games,
        "S": statistics.mean(scores["S"]) if scores["S"] else float("nan"),
        "R": statistics.mean(scores["R"]) if scores["R"] else float("nan"),
        "roll_pr": tot["rollovers"] / (games * ROUNDS),
        "carry_pr": tot["carries"] / (games * ROUNDS),
        "flips_pg": tot["flips"] / games,
        "rot": tot["rotted_pips"] / games,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    print(f"THE COUNCIL v1.0a sim · {a.games} games per row · seed {a.seed} · {ROUNDS} rounds (fixed: cannot stall)\n")
    print(f"{'P':>2} {'table':<8}{'S win':>7}{'x fair':>7}{'S pts':>7}{'R pts':>7}"
          f"{'carries/rd':>11}{'rollover stacks/rd':>19}{'flips/g':>8}{'rotted pips':>12}  seat wins (0 = first Speaker)")
    for n in (3, 4, 5, 6):
        for table in ("random", "skilled", "mixed"):
            r = run(n, a.games, table, a.seed)
            fw = r["focus"] if table == "mixed" else float("nan")
            print(f"{n:>2} {table:<8}{fw:>7.1%}{fw * n:>7.2f}{r['S']:>7.1f}{r['R']:>7.1f}"
                  f"{r['carry_pr']:>11.2f}{r['roll_pr']:>19.2f}{r['flips_pg']:>8.1f}{r['rot']:>12.1f}  "
                  + " ".join(f"{s:.0%}" for s in r["seat"]))
        print()


if __name__ == "__main__":
    main()
