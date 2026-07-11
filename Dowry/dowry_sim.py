"""DOWRY simulator — floor certification for rulebook v0.1.

Models the real 2P ruleset:
  * 36-card K9 deck, faces randomised on shuffle.
  * Rung-2 self-deal (9 each): the face up as each card is taken is PUBLIC.
  * Stock of 18, live stack, top face public; refill glimpses are public.
  * 12 offers, alternating cutter: 3 hand cards as lots of 2/1, cutter
    chooses each card's shown face; chooser takes a lot; cutter keeps rest.
  * Placement: taker places each captured card on either face, OPENLY —
    both faces become public; the up face scores, locked.
  * Scoring: per sign, strict majority of shown instances scores the pip
    (Moon 1 .. Crown 9); ties score no one. Game tie -> Moon majority.

Bots (perfect memory — an upper bound on human registry tracking):
  * RandomBot        — uniform legal cut/choice/placement (mechanics floor).
  * SkilledBot       — deceptive cutter (searches cuts, predicts the
                       chooser's perceived values, maximises true kept
                       minus true given), registry-deducing chooser,
                       majority-greedy placement.
  * HonestCutBot     — as SkilledBot but cuts for the most even TRUE split
                       and dresses fully informatively (best face shown).
                       The honest-vs-deceptive arm answers the rulebook's
                       first-table question 1 (is the dressing layer alive?).

What the sim cannot model: human forgetting (glimpse memory), bluff reads,
table feel. It certifies termination, seat fairness, and strategy floors only.

Run:  python dowry_sim.py --games 1000 [--seed 7]
"""

from __future__ import annotations
import argparse
import random
from itertools import combinations

SIGNS = range(1, 10)  # pip == sign value; 1 Moon .. 9 Crown
ALL_CARDS = [frozenset(p) for p in combinations(SIGNS, 2)]  # 36 unique pairs


def other(card, face):
    (a, b) = tuple(card)
    return b if face == a else a


# ---------------------------------------------------------------- state

class Game:
    def __init__(self, rng):
        self.rng = rng
        deck = ALL_CARDS[:]
        rng.shuffle(deck)
        self.up = {c: rng.choice(tuple(c)) for c in deck}  # face-up after shuffle
        self.hands = {0: deck[:9], 1: deck[9:18]}
        self.stock = deck[18:]
        self.spread = {0: {}, 1: {}}          # card -> scoring face
        # public knowledge: card -> set of publicly seen faces
        self.seen = {c: set() for c in deck}
        for p in (0, 1):
            for c in self.hands[p]:
                self.seen[c].add(self.up[c])  # rung-2 deal glimpse
        # NB stock top face is public each refill (recorded at draw time)

    def fully_known(self, card):
        return len(self.seen[card]) == 2

    def known_pairs(self, viewer):
        """Pairs attributable by `viewer` (public registry + own hand)."""
        known = {c for c in ALL_CARDS if self.fully_known(c)}
        known |= set(self.hands[viewer])
        return known

    def hidden_candidates(self, card, shown, viewer):
        """Signs the hidden face of an offered card could be, for viewer."""
        if card in self.hands[viewer] or self.fully_known(card):
            return [other(card, shown)]
        if self.seen[card] and shown not in self.seen[card]:
            # dressing flipped away from the glimpsed face -> fully revealed
            return [next(iter(self.seen[card]))]
        taken = {other(c, shown) for c in self.known_pairs(viewer)
                 if c != card and shown in c}
        return [g for g in SIGNS if g != shown and g not in taken] or \
               [other(card, shown)]

    def counts(self, p):
        n = {g: 0 for g in SIGNS}
        for f in self.spread[p].values():
            n[f] += 1
        return n

    def score(self):
        s = [0, 0]
        c0, c1 = self.counts(0), self.counts(1)
        for g in SIGNS:
            if c0[g] > c1[g]:
                s[0] += g
            elif c1[g] > c0[g]:
                s[1] += g
        return s

    def winner(self):
        s = self.score()
        if s[0] != s[1]:
            return 0 if s[0] > s[1] else 1, s
        c0, c1 = self.counts(0), self.counts(1)
        if c0[1] != c1[1]:
            return (0 if c0[1] > c1[1] else 1), s
        return None, s  # shared


# ---------------------------------------------------------------- bots

def place_value(g, mine, theirs):
    before = g if mine[g] > theirs[g] else 0
    after = g if mine[g] + 1 > theirs[g] else 0
    return (after - before) + (0.1 * g if mine[g] + 1 == theirs[g] else 0) + 0.01 * g


def best_face(card, mine, theirs):
    a, b = tuple(card)
    return a if place_value(a, mine, theirs) >= place_value(b, mine, theirs) else b


def true_lot_value(lot, mine, theirs):
    """Value of a lot to a player who knows both faces (greedy placement)."""
    v, m = 0.0, dict(mine)
    for card, _shown in lot:
        f = best_face(card, m, theirs)
        v += place_value(f, m, theirs)
        m[f] += 1
    return v


def perceived_lot_value(g, lot, viewer):
    """Chooser's expected lot value from shown faces + registry deduction."""
    mine, theirs = g.counts(viewer), g.counts(1 - viewer)
    v = 0.0
    for card, shown in lot:
        cands = g.hidden_candidates(card, shown, viewer)
        exp = 0.0
        for h in cands:
            exp += max(place_value(shown, mine, theirs),
                       place_value(h, mine, theirs))
        v += exp / len(cands)
    return v


class RandomBot:
    deceptive = None

    def cut(self, g, me):
        cards = g.rng.sample(g.hands[me], 3)
        faces = [g.rng.choice(tuple(c)) for c in cards]
        single = g.rng.randrange(3)
        lots = ([(cards[single], faces[single])],
                [(cards[i], faces[i]) for i in range(3) if i != single])
        return lots

    def choose(self, g, me, lots):
        return g.rng.randrange(2)

    def place(self, g, me, card):
        return g.rng.choice(tuple(card))


class SkilledBot(RandomBot):
    """Deceptive cutter + deducing chooser + greedy placement."""
    deceptive = True

    def place(self, g, me, card):
        return best_face(card, g.counts(me), g.counts(1 - me))

    def choose(self, g, me, lots):
        v0 = perceived_lot_value(g, lots[0], me)
        v1 = perceived_lot_value(g, lots[1], me)
        if abs(v0 - v1) < 1e-9:
            return g.rng.randrange(2)
        return 0 if v0 > v1 else 1

    def cut(self, g, me):
        you = 1 - me
        mine_c, yours_c = g.counts(me), g.counts(you)
        hand = g.hands[me]
        triples = list(combinations(hand, 3))
        if len(triples) > 30:
            triples = g.rng.sample(triples, 30)
        best, best_obj = None, -1e9
        for tri in triples:
            for single in range(3):
                for mask in range(8):
                    lots = self._dress(g, tri, single, mask)
                    obj = self._objective(g, me, you, lots, mine_c, yours_c)
                    if obj > best_obj:
                        best_obj, best = obj, lots
        return best

    @staticmethod
    def _dress(g, tri, single, mask):
        faces = []
        for i, c in enumerate(tri):
            a, b = tuple(c)
            faces.append(a if (mask >> i) & 1 else b)
        lot_a = [(tri[single], faces[single])]
        lot_b = [(tri[i], faces[i]) for i in range(3) if i != single]
        return (lot_a, lot_b)

    def _objective(self, g, me, you, lots, mine_c, yours_c):
        # predict chooser: perceived values from THEIR knowledge
        p0 = perceived_lot_value(g, lots[0], you)
        p1 = perceived_lot_value(g, lots[1], you)
        taken = 0 if p0 > p1 else 1 if p1 > p0 else g.rng.randrange(2)
        kept = 1 - taken
        return (true_lot_value(lots[kept], mine_c, yours_c)
                - true_lot_value(lots[taken], yours_c, mine_c))


class HonestCutBot(SkilledBot):
    """Cuts for the most even true split; dresses best-face-up (no lies)."""
    deceptive = False

    def cut(self, g, me):
        you = 1 - me
        mine_c, yours_c = g.counts(me), g.counts(you)
        hand = g.hands[me]
        triples = list(combinations(hand, 3))
        if len(triples) > 30:
            triples = g.rng.sample(triples, 30)
        best, best_gap = None, 1e9
        for tri in triples:
            for single in range(3):
                lots = self._honest_dress(tri, single, mine_c, yours_c)
                gap = abs(true_lot_value(lots[0], yours_c, mine_c)
                          - true_lot_value(lots[1], yours_c, mine_c))
                if gap < best_gap:
                    best_gap, best = gap, lots
        return best

    @staticmethod
    def _honest_dress(tri, single, mine_c, yours_c):
        faces = [best_face(c, yours_c, mine_c) for c in tri]  # informative
        lot_a = [(tri[single], faces[single])]
        lot_b = [(tri[i], faces[i]) for i in range(3) if i != single]
        return (lot_a, lot_b)


# ---------------------------------------------------------------- engine

def play(bots, rng, turn_cap=40):
    g = Game(rng)
    cutter, turns = 0, 0
    while g.hands[0] or g.hands[1]:
        turns += 1
        if turns > turn_cap:
            return None, None, turns  # stall (bug)
        me, you = cutter, 1 - cutter
        lots = bots[me].cut(g, me)
        for lot in lots:                      # offer faces become public
            for card, shown in lot:
                g.seen[card].add(shown)
        pick = bots[you].choose(g, you, lots)
        for owner, lot in ((you, lots[pick]), (me, lots[1 - pick])):
            for card, _shown in lot:
                g.hands[me].remove(card)
                f = bots[owner].place(g, owner, card)
                g.spread[owner][card] = f
                g.seen[card] = set(card)      # placement reveals both faces
        while len(g.hands[me]) < 9 and g.stock:
            c = g.stock.pop(0)
            g.seen[c].add(g.up[c])            # public stock-top glimpse
            g.hands[me].append(c)
        cutter = you
    w, s = g.winner()
    return w, s, turns


def arm(name, bot0, bot1, games, seed):
    rng = random.Random(seed)
    wins, scores, stalls, turn_tot = [0, 0, 0], [0, 0], 0, 0
    for _ in range(games):
        w, s, t = play({0: bot0, 1: bot1}, rng)
        if w is None and s is None:
            stalls += 1
            continue
        turn_tot += t
        wins[2 if w is None else w] += 1
        scores[0] += s[0]
        scores[1] += s[1]
    n = games - stalls
    print(f"{name:38s} P0 {wins[0]:4d}  P1 {wins[1]:4d}  shared {wins[2]:3d}"
          f"  | avg score {scores[0]/n:5.1f} v {scores[1]/n:5.1f}"
          f"  | stalls {stalls}  offers/game {turn_tot/n:.1f}")
    return wins, (scores[0] / n, scores[1] / n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()

    # structural assertions (never assert combinatorics, compute them)
    assert len(ALL_CARDS) == 36
    from collections import Counter
    deg = Counter(g for c in ALL_CARDS for g in c)
    assert all(v == 8 for v in deg.values())

    print(f"DOWRY sim — {a.games} games/arm, seed {a.seed}\n")
    arm("random vs random (seat check)", RandomBot(), RandomBot(), a.games, a.seed)
    w, s = arm("SKILLED (P0) vs random", SkilledBot(), RandomBot(), a.games, a.seed + 1)
    print(f"{'':38s} skill edge: win {w[0]/max(1,w[1]):.2f}x, score {s[0]/s[1]:.2f}x")
    arm("random (P0) vs SKILLED", RandomBot(), SkilledBot(), a.games, a.seed + 2)
    arm("skilled vs skilled (seat check)", SkilledBot(), SkilledBot(), a.games, a.seed + 3)
    wd, sd = arm("DECEPTIVE (P0) vs honest-cut", SkilledBot(), HonestCutBot(), a.games, a.seed + 4)
    print(f"{'':38s} dressing edge: win {wd[0]/max(1,wd[1]):.2f}x, "
          f"score {sd[0]/sd[1]:.2f}x")
    arm("honest-cut (P0) vs DECEPTIVE", HonestCutBot(), SkilledBot(), a.games, a.seed + 5)


if __name__ == "__main__":
    main()
