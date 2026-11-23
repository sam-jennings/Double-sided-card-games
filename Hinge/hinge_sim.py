#!/usr/bin/env python3
"""HINGE floor simulator (2 players, draft rules v0.1).

Models the split-and-flip move from HINGE_concept.md with the concept's
recommended 2-player economy: strict alternation, no bonus move.

  Packet   the 15-card 6-sign sub-deck (signs 1-6), random faces, in a row.
  Move     choose k in 1..n-1, take the front k cards as a block and turn the
           block over: the block's order reverses AND every card in it shows
           its other face (the burnt-pancake flip).
  Claim    any run of 3+ adjacent cards showing the same sign is claimed by
           the mover; the gap closes. --cascade (default on) keeps claiming
           runs that form when the gap closes; --no-cascade claims only runs
           present right after the flip.
  End      fewer than 3 cards remain, or N consecutive moves without a claim
           (the "chordless" cap being tuned here), or a hard cap of 300 moves.
  Deal     if the dealt packet already shows a run, reshuffle.

Bots
  RandomBot   uniform random k.
  GreedyBot   1-ply: takes the move claiming the most cards (random tiebreak).
  SkilledBot  2-ply: maximises (cards I claim) - (best reply's claim), with
              the immediate claim weighted first; a lookahead floor, not a
              ceiling.

Usage:  python hinge_sim.py --games 2000 --seed 1
"""

from __future__ import annotations

import argparse
import random
import statistics
from collections import Counter
from itertools import combinations

CARDS = list(combinations(range(1, 7), 2))  # 15 cards, each sign on 5
HARD_CAP = 300


def show(packet):
    return [c[f] for c, f in packet]


def find_runs(packet):
    s = show(packet)
    runs, i = [], 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and s[j + 1] == s[i]:
            j += 1
        if j - i + 1 >= 3:
            runs.append((i, j))
        i = j + 1
    return runs


def resolve(packet, cascade):
    claimed = 0
    while True:
        runs = find_runs(packet)
        if not runs:
            return packet, claimed
        keep = [True] * len(packet)
        for i, j in runs:
            for x in range(i, j + 1):
                keep[x] = False
            claimed += j - i + 1
        packet = [c for c, k in zip(packet, keep) if k]
        if not cascade:
            return packet, claimed


def move(packet, k, cascade):
    block = [(c, 1 - f) for c, f in reversed(packet[:k])]
    return resolve(block + packet[k:], cascade)


def deal(rng):
    while True:
        cards = CARDS[:]
        rng.shuffle(cards)
        packet = [(c, rng.randrange(2)) for c in cards]
        if not find_runs(packet):
            return packet


class RandomBot:
    def __init__(self, rng):
        self.rng = rng

    def choose(self, packet, cascade):
        return self.rng.randrange(1, len(packet))


class GreedyBot:
    def __init__(self, rng):
        self.rng = rng

    def choose(self, packet, cascade):
        best = max(range(1, len(packet)),
                   key=lambda k: (move(packet, k, cascade)[1], self.rng.random()))
        return best


class SkilledBot:
    def __init__(self, rng):
        self.rng = rng

    def choose(self, packet, cascade):
        best, best_key = 1, None
        for k in range(1, len(packet)):
            nxt, got = move(packet, k, cascade)
            reply = 0
            if len(nxt) >= 3:
                reply = max(move(nxt, j, cascade)[1] for j in range(1, len(nxt)))
            key = (got - reply, got, self.rng.random())
            if best_key is None or key > best_key:
                best, best_key = k, key
        return best


def play_round(bots, rng, cap, cascade, first=0, bonus=False):
    packet = deal(rng)
    score = [0, 0]
    p, moves, dry = first, 0, 0
    while len(packet) >= 3 and moves < HARD_CAP:
        k = bots[p].choose(packet, cascade)
        packet, got = move(packet, k, cascade)
        score[p] += got
        moves += 1
        dry = 0 if got else dry + 1
        if cap and dry >= cap:
            return score, moves, "cap", len(packet)
        if not (bonus and got):  # claim-and-go-again keeps the turn
            p = 1 - p
    reason = "empty" if len(packet) < 3 else "hard"
    return score, moves, reason, len(packet)


def run(table, games, cap, cascade, seed, bonus=False):
    rng = random.Random(seed)
    make = {"R": RandomBot, "G": GreedyBot, "S": SkilledBot}
    wins, first_w, focus_w, draws = Counter(), 0.0, 0.0, 0
    moves_l, left_l, reasons, claimed_l = [], [], Counter(), []
    for i in range(games):
        first = i % 2
        if table[0] != table[2]:
            focus = (i // 2) % 2  # focus seat rotates independently of the first player
            a, b = table[0], table[2]
            kinds = [b, b]
            kinds[focus] = a
        else:
            focus = None
            kinds = [table[0], table[0]]
        bots = [make[k](rng) for k in kinds]
        score, moves, reason, left = play_round(bots, rng, cap, cascade, first, bonus)
        moves_l.append(moves)
        left_l.append(left)
        reasons[reason] += 1
        claimed_l.append(sum(score))
        if score[0] == score[1]:
            draws += 1
            continue
        w = 0 if score[0] > score[1] else 1
        if w == first:
            first_w += 1
        if focus is not None and w == focus:
            focus_w += 1
    dec = games - draws
    return {
        "moves": statistics.mean(moves_l),
        "p90": sorted(moves_l)[int(0.9 * games)],
        "left": statistics.mean(left_l),
        "claimed": statistics.mean(claimed_l),
        "cap%": reasons["cap"] / games,
        "empty%": reasons["empty"] / games,
        "hard%": reasons["hard"] / games,
        "draw%": draws / games,
        "first": first_w / max(dec, 1),
        "focus": focus_w / max(dec, 1),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    print(f"HINGE v0.1 sim · 2P · {a.games} rounds per row · seed {a.seed} · hard cap {HARD_CAP} moves\n")
    hdr = (f"{'cascade':<8}{'cap':>4} {'table':<6}{'moves':>7}{'p90':>5}{'claimed':>8}{'left':>6}"
           f"{'end:cap':>8}{'empty':>7}{'hard':>6}{'draw':>6}{'1st wins':>9}{'focus wins':>11}")
    print(hdr)
    cascade = True  # cascade on vs off measured identical within noise in the 200-round pilot
    for bonus in (False, True):
        print(f"--- turn economy: {'claim-and-go-again' if bonus else 'strict alternation (concept recommendation)'} ---")
        for cap in (6, 8, 10, 0):
            for table in ("RvR", "GvG", "SvS", "GvR", "SvR", "SvG"):
                if cap == 0 and "S" in table:
                    continue  # uncapped 2-ply rounds run to the 300-move hard cap; too slow at volume
                r = run(table, a.games, cap, cascade, a.seed, bonus)
                fw = f"{r['focus']:.1%}" if table[0] != table[2] else "-"
                print(f"{'on':<8}{cap if cap else 'inf':>4} {table:<6}"
                      f"{r['moves']:>7.1f}{r['p90']:>5}{r['claimed']:>8.1f}{r['left']:>6.1f}"
                      f"{r['cap%']:>8.0%}{r['empty%']:>7.0%}{r['hard%']:>6.1%}{r['draw%']:>6.0%}"
                      f"{r['first']:>9.1%}{fw:>11}")
            print()


if __name__ == "__main__":
    main()
