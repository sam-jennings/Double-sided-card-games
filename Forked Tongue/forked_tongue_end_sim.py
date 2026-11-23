#!/usr/bin/env python3
"""FORKED TONGUE end-condition test bench (November 2026, proposal only).

A copy of forked_tongue_sim.py (v1.1 rules, same bots) with candidate
termination rules added as options.  The original sim is left untouched;
with no options set, this file plays exactly the v1.1 rules.

Candidate rules (see FORKED_TONGUE_end_condition_proposal.md)
  cap=L      ROW CAP.  When a play survives the challenge window and the
             ledger now holds L or more cards, the whole ledger is retired
             face-up to the registry (dead, public, examinable); the next
             player opens fresh.
  swear=N    SWEAR ON IT.  When a play survives the challenge window and the
             ledger holds N or more cards, the claimant may flip their own
             card.  True: the ledger retires to the registry and the next
             player opens fresh.  A lie: the claimant takes the ledger.
  fuse=D     DECLINE FUSE.  Each decline burns one fuse card; on the D-th
             decline the game ends at once and the fewest cards in hand
             wins (ties share the win).
  fuse_reg=k The same fuse sized from the table: k burns per registry card
             (k=2: each registry card is turned sideways, then moved to a
             spent row), i.e. 24/16/12/12 declines at 3/4/5/6P.
  tie_next   Fuse tie-break: of the tied players, the first one clockwise
             after the player whose decline burnt the fuse wins.
  lastword   LAST WORD.  A player holding exactly one card may play it
             showing either face, ignoring the requirement (they still claim,
             and the challenge window still applies).

Bot changes needed by the options (nothing else changed):
  - both bots treat "may open fresh" as owed is None OR last-word applies;
  - SkilledBot swears whenever its newest claim is true; RandomBot swears
    30% of the time it is allowed, true or not;
  - on a retire, SkilledBot records every retired card as "reg" (public).
  Neither bot plays toward the fuse (e.g. declining to end a game it leads),
  so fuse numbers are a floor on how the clock gets gamed.

Usage:  python forked_tongue_end_sim.py --games 2000 --seed 1
"""

from __future__ import annotations

import argparse
import os
import random
import statistics
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from multiprocessing import Pool

SYMS = range(1, 10)
DECK = [frozenset(p) for p in combinations(SYMS, 2)]
HAND = {3: 8, 4: 7, 5: 6, 6: 5}
TURN_CAP = 600


@dataclass(frozen=True)
class Rules:
    cap: int | None = None
    swear: int | None = None
    fuse: int | None = None
    fuse_reg: int | None = None  # fuse = this many burns per setup registry card
    tie_next: bool = False       # fuse tie -> first tied player clockwise after the decliner
    lastword: bool = False


def other(card, s):
    (o,) = card - {s}
    return o


class Game:
    def __init__(self, n, bots, rng, rules=Rules()):
        self.n, self.bots, self.rng, self.rules = n, bots, rng, rules
        deck = DECK[:]
        rng.shuffle(deck)
        h = HAND[n]
        self.hands = [set(deck[i * h:(i + 1) * h]) for i in range(n)]
        self.registry = set(deck[n * h:])
        self.ledger = []  # entries: (card, shown, claim, claimant)
        self.stats = Counter()
        self.declines = 0
        self.fuse = rules.fuse or (rules.fuse_reg * len(self.registry) if rules.fuse_reg else None)
        for p, b in enumerate(bots):
            b.setup(self, p)

    def owed(self):
        return self.ledger[-1][2] if self.ledger else None

    def fresh(self, p):
        """May player p play any card, any face?"""
        return self.owed() is None or (self.rules.lastword and len(self.hands[p]) == 1)

    def broadcast(self, event, **kw):
        for p, b in enumerate(self.bots):
            b.observe(self, p, event, **kw)

    def retire(self):
        cards = [e[0] for e in self.ledger]
        self.registry.update(cards)
        self.ledger = []
        self.stats["retire"] += 1
        self.broadcast("retire", cards=cards)

    def fewest(self, decliner):
        m = min(len(h) for h in self.hands)
        tied = [q for q in range(self.n) if len(self.hands[q]) == m]
        if self.rules.tie_next and len(tied) > 1:
            return [min(tied, key=lambda q: (q - decliner - 1) % self.n)]
        return tied

    def play(self, first=0):
        """Returns (list of winners, turns); winners None on a stall."""
        p, turns = first, 0
        r = self.rules
        while turns < TURN_CAP:
            turns += 1
            bot = self.bots[p]
            act = bot.act(self, p)
            if act is None:  # decline
                card, shown, claim, claimant = self.ledger.pop()
                self.hands[p].add(card)
                self.stats["decline"] += 1
                self.declines += 1
                self.broadcast("decline", taker=p, card=card)
                if self.fuse and self.declines >= self.fuse:
                    self.stats["fuse_end"] += 1
                    m = min(len(h) for h in self.hands)
                    self.stats["fuse_tie"] += sum(len(h) == m for h in self.hands) > 1
                    return self.fewest(p), turns
                p = (p + 1) % self.n
                continue
            card, shown, claim = act
            assert card in self.hands[p] and shown in card and claim != shown
            assert self.fresh(p) or shown == self.owed()
            self.hands[p].remove(card)
            self.ledger.append((card, shown, claim, p))
            self.stats["play"] += 1
            lie = claim not in card
            self.stats["lie"] += lie
            self.broadcast("play", claimant=p, shown=shown, claim=claim)
            final = not self.hands[p]
            challenger = None
            for k in range(1, self.n):
                q = (p + k) % self.n
                if self.bots[q].challenge(self, q, p, shown, claim, final):
                    challenger = q
                    break
            if challenger is not None:
                self.stats["challenge"] += 1
                loser = p if lie else challenger
                self.stats["caught" if lie else "wrong_challenge"] += 1
                taken = [e[0] for e in self.ledger]
                self.hands[loser].update(taken)
                self.ledger = []
                self.broadcast("challenge", claimant=p, card=card, loser=loser, taken=taken)
                if final and not lie:
                    return [p], turns
                p = (p + 1) % self.n
                continue
            if final:
                return [p], turns
            if r.swear and len(self.ledger) >= r.swear and bot.swear(self, p):
                self.stats["swear"] += 1
                if lie:
                    self.stats["swear_fail"] += 1
                    taken = [e[0] for e in self.ledger]
                    self.hands[p].update(taken)
                    self.ledger = []
                    self.broadcast("challenge", claimant=p, card=card, loser=p, taken=taken)
                else:
                    self.retire()
            elif r.cap and len(self.ledger) >= r.cap:
                self.retire()
            p = (p + 1) % self.n
        return None, turns


class RandomBot:
    name = "random"

    def __init__(self, rng):
        self.rng = rng

    def setup(self, g, p):
        pass

    def observe(self, g, p, event, **kw):
        pass

    def claim(self, card, shown):
        if self.rng.random() < 0.5:
            return other(card, shown)
        return self.rng.choice([s for s in SYMS if s != shown])

    def act(self, g, p):
        r, owed, hand = self.rng, g.owed(), sorted(g.hands[p], key=sorted)
        if g.fresh(p):
            card = r.choice(hand)
            shown = r.choice(sorted(card))
            return card, shown, self.claim(card, shown)
        legal = [c for c in hand if owed in c]
        if legal and r.random() < 0.85:
            card = r.choice(legal)
            return card, owed, self.claim(card, owed)
        return None

    def challenge(self, g, q, p, shown, claim, final):
        return self.rng.random() < (0.5 if final else 0.15)

    def swear(self, g, p):
        return self.rng.random() < 0.3


class SkilledBot:
    name = "skilled"

    def __init__(self, rng, honest=False, lie_rate=0.5):
        self.rng, self.honest, self.lie_rate = rng, honest, lie_rate

    def setup(self, g, p):
        self.loc = {c: "reg" for c in g.registry}
        for c in g.hands[p]:
            self.loc[c] = p
        self.ledger_known = []

    def observe(self, g, p, event, **kw):
        if event == "play":
            q, shown = kw["claimant"], kw["shown"]
            mine = None
            if q == p:
                mine = g.ledger[-1][0]
                self.loc.pop(mine, None)
            else:
                for c, w in list(self.loc.items()):
                    if w == q and shown in c:
                        del self.loc[c]
            self.ledger_known.append(mine)
        elif event == "decline":
            known = self.ledger_known.pop()
            if kw["taker"] == p:
                self.loc[kw["card"]] = p
            elif known is not None:
                self.loc[known] = kw["taker"]
        elif event == "challenge":
            loser = kw["loser"]
            for c in ([kw["card"]] + [k for k in self.ledger_known if k is not None]):
                self.loc[c] = loser
            if loser == p:
                for c in kw["taken"]:
                    self.loc[c] = p
            self.ledger_known = []
        elif event == "retire":
            for c in kw["cards"]:
                self.loc[c] = "reg"  # face-up in the registry: public
            self.ledger_known = []

    def unaccounted(self, s, p):
        return sum(1 for c in DECK if s in c and c not in self.loc)

    def certainly_false(self, claimant, shown, claim):
        c = frozenset((shown, claim))
        w = self.loc.get(c)
        return w is not None and w != claimant

    def best_claim(self, g, p, card, shown, may_lie):
        truth = other(card, shown)
        best = (self.unaccounted(truth, p), truth)
        if may_lie:
            for x in SYMS:
                if x in (shown, truth):
                    continue
                pair = frozenset((shown, x))
                if self.loc.get(pair, p) != p:
                    continue
                score = self.unaccounted(x, p) - 0.5
                if score < best[0]:
                    best = (score, x)
        return best

    def act(self, g, p):
        owed, hand = g.owed(), sorted(g.hands[p], key=sorted)
        last = len(hand) == 1
        fresh = g.fresh(p)
        may_lie = (not self.honest and not last and len(hand) >= 4
                   and self.rng.random() < self.lie_rate)
        options = []
        for card in hand:
            faces = sorted(card) if fresh else ([owed] if owed in card else [])
            for shown in faces:
                score, claim = self.best_claim(g, p, card, shown, may_lie)
                options.append((score, self.rng.random(), card, shown, claim))
        if not options:
            return None
        _, _, card, shown, claim = min(options, key=lambda o: o[:2])
        return card, shown, claim

    def challenge(self, g, q, p, shown, claim, final):
        if self.certainly_false(p, shown, claim):
            return True
        if final:
            return frozenset((shown, claim)) not in g.hands[q]
        return False

    def swear(self, g, p):
        card, shown, claim, _ = g.ledger[-1]
        return claim in card  # only swear to the truth


TABLES = ("random", "skilled", "honest", "mixed", "honest-mixed", "liar-vs-honest")
FOCUS = ("mixed", "honest-mixed", "liar-vs-honest")


def run(n, games, table, seed, rules):
    rng = random.Random(seed)
    stalls, turns_l, seat_w, s_w = 0, [], Counter(), 0.0
    tot = Counter()
    for i in range(games):
        first = i % n
        focus = (i // n) % n
        if table == "random":
            bots = [RandomBot(rng) for _ in range(n)]
        elif table == "skilled":
            bots = [SkilledBot(rng) for _ in range(n)]
        elif table == "honest":
            bots = [SkilledBot(rng, honest=True) for _ in range(n)]
        elif table in ("mixed", "honest-mixed"):
            bots = [RandomBot(rng) for _ in range(n)]
            bots[focus] = SkilledBot(rng, honest=(table == "honest-mixed"))
        else:  # liar-vs-honest
            bots = [SkilledBot(rng, honest=True) for _ in range(n)]
            bots[focus] = SkilledBot(rng)
        g = Game(n, bots, rng, rules)
        winners, turns = g.play(first)
        tot += g.stats
        if winners is None:
            stalls += 1
            continue
        turns_l.append(turns)
        share = 1 / len(winners)
        for w in winners:
            seat_w[(w - first) % n] += share
            if table in FOCUS and w == focus:
                s_w += share
    done = games - stalls
    seat = [seat_w[k] / max(done, 1) for k in range(n)]
    st = sorted(turns_l)
    return {
        "stall": stalls / games,
        "mean": statistics.mean(st) if st else float("nan"),
        "median": statistics.median(st) if st else float("nan"),
        "p90": st[int(0.9 * len(st))] if st else float("nan"),
        "seat_spread": max(seat) - min(seat),
        "seat": seat,
        "focus_x": s_w / games * n,
        "decline": tot["decline"] / max(tot["decline"] + tot["play"], 1),
        "lie": tot["lie"] / max(tot["play"], 1),
        "lies_pg": tot["lie"] / games,
        "caught_pg": tot["caught"] / games,
        "caught_share": (tot["caught"] + tot["swear_fail"]) / max(tot["lie"], 1),
        "retire_pg": tot["retire"] / games,
        "fuse_end": tot["fuse_end"] / games,
        "ties": tot["fuse_tie"] / games,
    }


CONFIGS = {
    "v1.1 (no rule)": Rules(),
    "A cap 6": Rules(cap=6),
    "A cap 8": Rules(cap=8),
    "A cap 10": Rules(cap=10),
    "B swear 4": Rules(swear=4),
    "B swear 6": Rules(swear=6),
    "C fuse 12": Rules(fuse=12),
    "C fuse 20": Rules(fuse=20),
    "C fuse 2x reg, tie next": Rules(fuse_reg=2, tie_next=True),
    "C fuse 20, tie next": Rules(fuse=20, tie_next=True),
    "B+C swear 4 + fuse 2x reg, tie next": Rules(swear=4, fuse_reg=2, tie_next=True),
    "D last word": Rules(lastword=True),
    "D+A word+cap 8": Rules(cap=8, lastword=True),
}


def job(args):
    name, n, table, games, seed = args
    return name, n, table, run(n, games, table, seed, CONFIGS[name])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--only", default=None, help="run one config name")
    a = ap.parse_args()
    names = [a.only] if a.only else list(CONFIGS)
    jobs = [(c, n, t, a.games, a.seed) for c in names for n in (3, 4, 5, 6) for t in TABLES]
    with Pool(max(1, (os.cpu_count() or 2) - 1)) as pool:
        res = {(c, n, t): r for c, n, t, r in pool.map(job, jobs)}
    print(f"FORKED TONGUE end-condition bench · {a.games} games per row · seed {a.seed} · turn cap {TURN_CAP}")
    print("skill = mixed focus win x fair (skilled vs random); liar = liar-vs-honest focus x fair;"
          " spread = max-min seat win share on the skilled table\n")
    for c in names:
        print(f"== {c} ==")
        print(f"{'P':>2} {'stall rnd/skl/hon':>19} {'turns mean/med/p90 (skilled)':>29} {'honest mean':>11}"
              f" {'skill':>6} {'h-skill':>7} {'liar':>5} {'spread':>6} {'lie%':>5} {'lies/g':>6}"
              f" {'caught%':>7} {'decl%':>6} {'ret/g':>5} {'fuse':>5} {'ties':>5}")
        for n in (3, 4, 5, 6):
            R = {t: res[(c, n, t)] for t in TABLES}
            s, h = R["skilled"], R["honest"]
            print(f"{n:>2} {R['random']['stall']:>6.1%}/{s['stall']:>5.1%}/{h['stall']:>5.1%}"
                  f" {s['mean']:>10.1f}/{s['median']:>6.1f}/{s['p90']:>5}"
                  f" {h['mean']:>11.1f} {R['mixed']['focus_x']:>6.2f} {R['honest-mixed']['focus_x']:>7.2f}"
                  f" {R['liar-vs-honest']['focus_x']:>5.2f} {s['seat_spread']:>6.1%} {s['lie']:>5.0%}"
                  f" {s['lies_pg']:>6.1f} {s['caught_share']:>7.0%} {s['decline']:>6.0%}"
                  f" {s['retire_pg']:>5.1f} {s['fuse_end']:>5.0%} {s['ties']:>5.0%}")
        print()


if __name__ == "__main__":
    main()
