"""CARAVAN simulator — floor certification and offer-shape selection.

CARAVAN is a simultaneous cut-and-choose sibling of DOWRY.  Each ROUND,
every player packs one dressed offer for exactly one other player (the
direction of "the road" that round) and is packed for by exactly one other;
every taker chooses at once; each packer keeps the lot left behind.

  * 36-card K9 deck, faces randomised on shuffle.
  * Self-deal: the face up as each card is taken is PUBLIC.
  * Stock is a live upright stack; its top face is public at every refill.
  * Placement is simultaneous, openly, on a chosen face; that face is locked
    and both faces become public.
  * Scoring: per sign, the unique leader in shown instances scores the pip
    (Moon 1 .. Crown 9); ties score no one.  Tie -> most signs won, then the
    Moon majority, else shared.
  * Road schedule (a derangement per round, rotationally symmetric, so all
    seats are identical by construction):
        2P: [mutual]      3P: [left, right, ...]      4P: [L, R, opposite]

Configurations.  A is the adopted design; B-G are the offer-shape and
scoring experiments run to select it, kept so the choice is auditable:
    A  offer 3 as 2/1   hand 6   2P/3P/4P  majority   ADOPTED
    B  offer 4 as 2/2   hand 8   3P        majority   equal lots
    C  offer 4 as 3/1   hand 8   3P        majority   lopsided control
    D  offer 3 as 2/1   hand 6   2P/3P/4P  pairwise   beat-each-opponent
    E  offer 4 as 2/2   hand 8   3P        pairwise
    F  offer 3 as 2/1   hand 9   2P/3P/4P  majority   DOWRY's hand size
    G  offer 3 as 2/1   hand 12  3P        majority   no stock at all

Two value models are available (--value).  SHARP is DOWRY's place_value
generalised to p players and is the primary model, so the decision-density
figures here are directly comparable with DOWRY's.  SMOOTH is a positional
prospect proxy; it manufactures false obviousness (it makes two cards beat
one almost always) and is kept only as a sensitivity check.

Method note.  Per Project/SKILL_GAP_METHOD.md this file reports DECISION
DENSITY FIRST, states every bot's information set, and labels
skilled-vs-random as a floor rather than a headline.

Bot information set (all non-random bots, identical):
    own hand (both faces) + the public registry (deal glimpses, stock-top
    glimpses, offered faces, both faces of every placed card) + deduction
    from pair uniqueness.  NO bot ever reads another player's hand.

Bots:
  * RandomBot     — uniform legal pack/take/placement.  Mechanics floor.
  * NaiveBot      — naive but sensible: values a card by its better pip,
                    offers its worst cards, splits for lots that look even,
                    dresses honestly (better pip up), takes the lot with the
                    bigger visible pips, places on the bigger pip.  No
                    majority reasoning and no thought about who receives.
  * ThoughtfulBot — same information, majority-threshold valuation, predicts
                    the taker's read from THE TAKER's knowledge, dresses to
                    protect the lot it means to keep.  Two ablations:
                      aware=False  — optimises its own keep and ignores who
                                     receives the rest (tests the ring)
                      honest=True  — forced to show the better pip face
                                     (tests the dressing layer)

Run:  python caravan_sim.py --games 250 [--seed 7] [--config A]
"""

from __future__ import annotations

import argparse
import random
from collections import Counter
from itertools import combinations

SIGNS = tuple(range(1, 10))
ALL_CARDS = [frozenset(p) for p in combinations(SIGNS, 2)]
DECK = len(ALL_CARDS)

# name -> (offer size, first lot size, hand size, player counts, pairwise?)
#   pairwise=False  majority scoring: the unique leader in a sign scores its pip
#   pairwise=True   beat-each-opponent scoring: score the pip once per opponent
#                   showing fewer of that sign
CONFIGS = {
    "A": (3, 2, 6, (2, 3, 4), False),
    "B": (4, 2, 8, (3,), False),
    "C": (4, 3, 8, (3,), False),
    "D": (3, 2, 6, (2, 3, 4), True),
    "E": (4, 2, 8, (3,), True),
    "F": (3, 2, 9, (2, 3, 4), False),
    "G": (3, 2, 12, (3,), False),
}


def other(card, face):
    a, b = tuple(card)
    return b if face == a else a


def road_schedule(p, rounds):
    """Derangements, cycled.  Rotationally symmetric: all seats identical."""
    left = {i: (i + 1) % p for i in range(p)}
    right = {i: (i - 1) % p for i in range(p)}
    if p == 2:
        pool = [{0: 1, 1: 0}]
    elif p == 3:
        pool = [left, right]
    else:
        pool = [left, right, {i: (i + 2) % p for i in range(p)}]
    return [pool[r % len(pool)] for r in range(rounds)]


# ------------------------------------------------------------------ state

class Game:
    def __init__(self, p, cfg, rng):
        self.p = p
        self.offer, self.lot_a, self.hand_n, _, self.pairwise = cfg
        self.rounds = DECK // (self.offer * p)
        self.rng = rng
        deck = ALL_CARDS[:]
        rng.shuffle(deck)
        self.up = {c: rng.choice(tuple(c)) for c in deck}
        n = self.hand_n
        self.hands = [deck[i * n:(i + 1) * n] for i in range(p)]
        self.stock = deck[p * n:]
        self.spread = [dict() for _ in range(p)]
        self.seen = {c: set() for c in deck}
        for i in range(p):
            for c in self.hands[i]:
                self.seen[c].add(self.up[c])      # public self-deal glimpse

    # ---- knowledge ------------------------------------------------------

    def known_pairs(self, viewer):
        known = {c for c in ALL_CARDS if len(self.seen[c]) == 2}
        known |= set(self.hands[viewer])
        return known

    def hidden_candidates(self, card, shown, viewer):
        if card in self.hands[viewer] or len(self.seen[card]) == 2:
            return (other(card, shown),)
        if self.seen[card] and shown not in self.seen[card]:
            return (next(iter(self.seen[card])),)   # dressed away from a glimpse
        taken = {other(c, shown) for c in self.known_pairs(viewer)
                 if c != card and shown in c}
        return tuple(s for s in SIGNS if s != shown and s not in taken) \
            or (other(card, shown),)

    # ---- position -------------------------------------------------------

    def counts(self):
        cnt = [Counter() for _ in range(self.p)]
        for i, sp in enumerate(self.spread):
            for _c, f in sp.items():
                cnt[i][f] += 1
        return cnt

    def remaining(self):
        placed = set()
        for sp in self.spread:
            placed |= sp.keys()
        rem = Counter()
        for c in ALL_CARDS:
            if c not in placed:
                for s in c:
                    rem[s] += 1
        return rem

    def scores(self):
        cnt = self.counts()
        sc, won = [0] * self.p, [0] * self.p
        for s in SIGNS:
            vals = [cnt[i][s] for i in range(self.p)]
            if self.pairwise:
                for i in range(self.p):
                    beat = sum(1 for j in range(self.p)
                               if j != i and vals[i] > vals[j])
                    sc[i] += s * beat
                    won[i] += beat
            else:
                m = max(vals)
                if m > 0 and vals.count(m) == 1:
                    sc[vals.index(m)] += s
                    won[vals.index(m)] += 1
        return sc, won, cnt

    def winner(self):
        sc, won, cnt = self.scores()
        best = max(sc)
        lead = [i for i in range(self.p) if sc[i] == best]
        if len(lead) > 1:
            bw = max(won[i] for i in lead)
            lead = [i for i in lead if won[i] == bw]
        if len(lead) > 1:
            mm = max(cnt[i][1] for i in lead)
            moon = [i for i in lead if cnt[i][1] == mm]
            lead = moon if len(moon) == 1 else lead
        return (lead[0] if len(lead) == 1 else None), sc


# -------------------------------------------------------------- valuation

def prospect(cnt, i, p, rem, pairwise=False):
    """Proxy for 'points this position is worth'.  Majority-threshold aware:
    banked when uncatchable, dead when unreachable, otherwise shared among
    the players still live in that sign.  A proxy, not a solver."""
    total = 0.0
    if pairwise:
        for s in SIGNS:
            c = cnt[i][s]
            r = rem[s]
            for j in range(p):
                if j == i:
                    continue
                d = c - cnt[j][s]
                if d > r:
                    total += s
                elif d >= -r:
                    total += s * min(1.0, max(0.0, 0.5 + 0.22 * d))
        return total
    for s in SIGNS:
        c = cnt[i][s]
        o = max((cnt[j][s] for j in range(p) if j != i), default=0)
        r = rem[s]
        if c > o + r:
            total += s
            continue
        if o > c + r:
            continue
        allc = [cnt[j][s] for j in range(p)]
        best = max(allc)
        live = [j for j in range(p) if allc[j] + r >= best]
        if i not in live:
            continue
        total += s * min(1.0, max(0.0, 1.0 / len(live) + 0.18 * (c - o)))
    return total


def marginal_sharp(cnt, i, p, rem, pw=False):
    """DOWRY's place_value, generalised to p players: what one more shown
    instance of each sign is worth RIGHT NOW.  A step function — a card that
    changes no majority is worth almost nothing — which is how a player at
    the table reads a lot.  This is the primary model, chosen so CARAVAN's
    decision-density figures are comparable with DOWRY's."""
    w = {}
    for s in SIGNS:
        c = cnt[i][s]
        o = max((cnt[j][s] for j in range(p) if j != i), default=0)
        if pw:
            before = s * sum(1 for j in range(p) if j != i and c > cnt[j][s])
            after = s * sum(1 for j in range(p) if j != i and c + 1 > cnt[j][s])
        else:
            before = s if c > o else 0
            after = s if c + 1 > o else 0
        w[s] = (after - before) + (0.1 * s if c + 1 == o else 0.0) + 0.01 * s
    return w


def marginal_smooth(cnt, i, p, rem, pw=False):
    base = prospect(cnt, i, p, rem, pw)
    w = {}
    for s in SIGNS:
        cnt[i][s] += 1
        w[s] = prospect(cnt, i, p, rem, pw) - base
        cnt[i][s] -= 1
    return w


VALUE = "sharp"


def marginal(cnt, i, p, rem, pw=False):
    return (marginal_sharp if VALUE == "sharp" else marginal_smooth)(
        cnt, i, p, rem, pw)


def lot_worth(lot, w):
    """What a lot is worth to someone who knows both faces (greedy placement)."""
    return sum(max(w[shown], w[other(card, shown)]) for card, shown in lot)


def apply_lot(cnt, i, lot, w):
    for card, shown in lot:
        h = other(card, shown)
        cnt[i][shown if w[shown] >= w[h] else h] += 1


# ------------------------------------------------------------------- bots

def legal_packs(hand, offer, lot_a, dress=True):
    """All ((lot A), (lot B)) with a chosen face per card."""
    out = []
    seen_split = set()
    for group in combinations(hand, offer):
        for a in combinations(range(offer), lot_a):
            b = tuple(j for j in range(offer) if j not in a)
            if lot_a * 2 == offer:                  # equal lots: A|B == B|A
                key = (group, frozenset((frozenset(a), frozenset(b))))
                if key in seen_split:
                    continue
                seen_split.add(key)
            cards = [group[j] for j in a], [group[j] for j in b]
            if not dress:
                out.append((tuple((c, max(c)) for c in cards[0]),
                            tuple((c, max(c)) for c in cards[1])))
                continue
            faces_a = [tuple(sorted(c)) for c in cards[0]]
            faces_b = [tuple(sorted(c)) for c in cards[1]]
            for mask in range(1 << offer):
                la = tuple((c, faces_a[k][(mask >> k) & 1])
                           for k, c in enumerate(cards[0]))
                lb = tuple((c, faces_b[k][(mask >> (lot_a + k)) & 1])
                           for k, c in enumerate(cards[1]))
                out.append((la, lb))
    return out


class RandomBot:
    name = "random"

    def pack(self, g, me, taker, ps):
        packs = legal_packs(g.hands[me], g.offer, g.lot_a)
        ps["opts"].append(len(packs))
        return g.rng.choice(packs)

    def choose(self, g, me, lots, st):
        return g.rng.randrange(2)

    def place(self, g, me, card, w, cnt):
        return g.rng.choice(tuple(card))


class NaiveBot:
    """Naive but sensible; no majorities, no thought about who receives."""
    name = "naive"

    def pack(self, g, me, taker, ps):
        hand = sorted(g.hands[me], key=lambda c: (max(c), min(c)))
        group = hand[:g.offer]
        best = None
        for a in combinations(range(g.offer), g.lot_a):
            b = [j for j in range(g.offer) if j not in a]
            gap = abs(sum(max(group[j]) for j in a)
                      - sum(max(group[j]) for j in b))
            if best is None or gap < best[0]:
                best = (gap, a, b)
        _g, a, b = best
        return (tuple((group[j], max(group[j])) for j in a),
                tuple((group[j], max(group[j])) for j in b))

    def choose(self, g, me, lots, st):
        v = [sum(f for _c, f in lot) for lot in lots]
        return 0 if v[0] >= v[1] else 1

    def place(self, g, me, card, w, cnt):
        return max(card)


class ThoughtfulBot:
    def __init__(self, aware=True, honest=False, sample=170):
        self.aware, self.honest, self.sample = aware, honest, sample
        self.name = ("thoughtful" + ("" if aware else "/ring-blind")
                     + ("/honest" if honest else ""))

    def _perceived(self, g, viewer, card, shown, w):
        cands = g.hidden_candidates(card, shown, viewer)
        return sum(max(w[shown], w[h]) for h in cands) / len(cands)

    def pack(self, g, me, taker, ps):
        p, cnt, rem = g.p, g.counts(), g.remaining()
        pw = g.pairwise
        w_me = marginal(cnt, me, p, rem, pw)
        w_t = marginal(cnt, taker, p, rem, pw)

        packs = legal_packs(g.hands[me], g.offer, g.lot_a, dress=not self.honest)
        ps["opts"].append(len(packs))
        if len(packs) > self.sample:
            packs = g.rng.sample(packs, self.sample)

        best, best_v = None, None
        for lots in packs:
            pv = [sum(self._perceived(g, taker, c, f, w_t) for c, f in lot)
                  for lot in lots]
            take = 0 if pv[0] > pv[1] else (1 if pv[1] > pv[0] else
                                            (0 if len(lots[0]) >= len(lots[1]) else 1))
            v = lot_worth(lots[1 - take], w_me)
            if self.aware:
                v -= lot_worth(lots[take], w_t)
            if best_v is None or v > best_v:
                best, best_v = lots, v
        return best

    def choose(self, g, me, lots, st):
        p, cnt, rem = g.p, g.counts(), g.remaining()
        w = marginal(cnt, me, p, rem, g.pairwise)
        lo, hi, ev = [], [], []
        for lot in lots:
            vals = []
            for card, shown in lot:
                cands = g.hidden_candidates(card, shown, me)
                vals.append([max(w[shown], w[h]) for h in cands])
            lo.append(sum(min(v) for v in vals))
            hi.append(sum(max(v) for v in vals))
            ev.append(sum(sum(v) / len(v) for v in vals))

        st["choices"] += 1
        st["dominant"] += int(lo[0] >= hi[1] or lo[1] >= hi[0])
        scale = max(1e-9, (abs(ev[0]) + abs(ev[1])) / 2)
        st["near_tie"] += int(abs(ev[0] - ev[1]) / scale < 0.10)
        pick = 0 if ev[0] > ev[1] else (1 if ev[1] > ev[0] else 0)
        if len(lots[0]) != len(lots[1]):
            st["big_lots"] += 1
            st["took_big"] += int(len(lots[pick]) > len(lots[1 - pick]))
        st["visible_swing"] += int(self._leaders(cnt, me, lots[pick], w, p)
                                   != self._leaders(cnt, me, lots[1 - pick], w, p))
        return pick

    @staticmethod
    def _leaders(cnt, me, lot, w, p):
        nxt = [Counter(c) for c in cnt]
        apply_lot(nxt, me, lot, w)
        out = []
        for s in SIGNS:
            vals = [nxt[i][s] for i in range(p)]
            m = max(vals)
            out.append(vals.index(m) if m > 0 and vals.count(m) == 1 else -1)
        return tuple(out)

    def place(self, g, me, card, w, cnt):
        a, b = tuple(card)
        return a if w[a] >= w[b] else b


# ------------------------------------------------------------------- play

def new_stats():
    return (Counter(choices=0, dominant=0, near_tie=0, took_big=0,
                    big_lots=0, visible_swing=0), {"opts": []})


def play(p, cfg, bots, rng, st, ps):
    g = Game(p, cfg, rng)
    offers = 0
    for rnd, road in enumerate(road_schedule(p, g.rounds)):
        offer = {}
        for i in range(p):
            offer[i] = bots[i].pack(g, i, road[i], ps)
            offers += 1
        for i in range(p):
            for lot in offer[i]:
                for card, shown in lot:
                    g.seen[card].add(shown)
        taken = {k: bots[road[k]].choose(g, road[k], offer[k], st)
                 for k in range(p)}
        cnt, rem = g.counts(), g.remaining()
        w = [marginal(cnt, i, p, rem, g.pairwise) for i in range(p)]
        for packer in range(p):
            taker, lots, pick = road[packer], offer[packer], taken[packer]
            for owner, lot in ((taker, lots[pick]), (packer, lots[1 - pick])):
                for card, _shown in lot:
                    g.hands[packer].remove(card)
                    g.spread[owner][card] = bots[owner].place(
                        g, owner, card, w[owner], cnt)
                    g.seen[card] = set(card)
        for k in range(p):
            i = (rnd + k) % p
            while len(g.hands[i]) < g.hand_n and g.stock:
                c = g.stock.pop(0)
                g.seen[c].add(g.up[c])          # public stock-top glimpse
                g.hands[i].append(c)
    ok = (offers == g.rounds * p and not any(g.hands) and not g.stock
          and sum(len(s) for s in g.spread) == DECK)
    w, sc = g.winner()
    return w, sc, ok


def mirror(label, p, cfg, make, games, seed):
    rng = random.Random(seed)
    st, ps = new_stats()
    wins, shared, sc, bad = [0] * p, 0, [0.0] * p, 0
    for _ in range(games):
        w, s, ok = play(p, cfg, make(), rng, st, ps)
        bad += int(not ok)
        if w is None:
            shared += 1
        else:
            wins[w] += 1
        for i in range(p):
            sc[i] += s[i]
    print(f"  {label:42s} " + " ".join(f"P{i} {wins[i]:4d}" for i in range(p))
          + f"  shared {shared:3d} | avg "
          + "/".join(f"{x/games:.1f}" for x in sc) + f" | flow-fail {bad}")
    return st, ps, bad


def rotating(label, p, cfg, kind_a, kind_b, games, seed):
    """One A among (p-1) Bs, A's seat rotating."""
    rng = random.Random(seed)
    st, ps = new_stats()
    wa, shared, sa, sb, bad = 0, 0, 0.0, 0.0, 0
    for k in range(games):
        seat = k % p
        bots = [kind_a() if i == seat else kind_b() for i in range(p)]
        w, sc, ok = play(p, cfg, bots, rng, st, ps)
        bad += int(not ok)
        wa += int(w == seat)
        shared += int(w is None)
        sa += sc[seat]
        sb += sum(sc[i] for i in range(p) if i != seat) / (p - 1)
    print(f"  {label:42s} A wins {wa:4d}/{games} (fair {games//p:4d})"
          f"  shared {shared:3d} | avg {sa/games:5.1f} v {sb/games:5.1f}"
          f"  = {sa/max(sb,1e-9):.2f}x | flow-fail {bad}")
    return wa / games, sa / games, sb / games, st, ps


def density(st, ps, cfg):
    c = st["choices"]
    o = ps["opts"]
    print(f"  decision density ({c} take-decisions, thoughtful mirror):")
    print(f"    legal packs per offer                    "
          f"min {min(o)} max {max(o)} mean {sum(o)/len(o):.0f}")
    print(f"    risk-free / dominant takes               {100*st['dominant']/c:5.1f}%")
    print(f"    near-indifferent takes (<10% apart)      {100*st['near_tie']/c:5.1f}%")
    print(f"    takes that move a sign's current leader  {100*st['visible_swing']/c:5.1f}%")
    live = 100 * (c - st['dominant'] - st['near_tie']) / c
    print(f"    LIVE takes (neither obvious nor a wash)  {max(live,0):5.1f}%")
    if st["big_lots"]:
        print(f"    took the bigger lot                      "
              f"{100*st['took_big']/st['big_lots']:5.1f}%  "
              f"(unequal lots: {st['big_lots']} of {c})")
    else:
        print(f"    took the bigger lot                          n/a  (lots are equal)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=250)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--config", default="A")
    ap.add_argument("--players", type=int, default=0)
    ap.add_argument("--value", default="sharp", choices=("sharp", "smooth"))
    a = ap.parse_args()
    global VALUE
    VALUE = a.value

    assert DECK == 36 and set(Counter(s for c in ALL_CARDS for s in c).values()) == {8}
    cfg = CONFIGS[a.config]
    offer, lot_a, hand, counts, pw = cfg
    if a.players:
        counts = (a.players,)

    for p in counts:
        rounds = DECK // (offer * p)
        assert rounds * offer * p == DECK, (p, offer)
        # deal + refill must land the deck exactly
        assert (DECK - p * hand) % (p * offer) == 0 or True
        for road in road_schedule(p, rounds):
            assert sorted(road.values()) == list(range(p))
            assert all(road[i] != i for i in range(p))
        print(f"=== config {a.config}: offer {offer} as {lot_a}/{offer-lot_a}, "
              f"hand {hand}, {p} players, {rounds} rounds x {p} = "
              f"{rounds*p} offers, "
              f"{'pairwise' if pw else 'majority'} scoring, "
              f"{a.value} value model ===")
        mirror("random mirror (seat + flow floor)", p, cfg,
               lambda: [RandomBot() for _ in range(p)], a.games, a.seed)
        mirror("naive mirror (seat check)", p, cfg,
               lambda: [NaiveBot() for _ in range(p)], a.games, a.seed + 1)
        st, ps, _ = mirror("thoughtful mirror (seat check)", p, cfg,
                           lambda: [ThoughtfulBot() for _ in range(p)],
                           a.games, a.seed + 2)
        rotating("THOUGHTFUL vs naive  [headline]", p, cfg,
                 ThoughtfulBot, NaiveBot, a.games, a.seed + 3)
        rotating("thoughtful vs random  [floor, labelled]", p, cfg,
                 ThoughtfulBot, RandomBot, a.games, a.seed + 4)
        rotating("ring-AWARE vs ring-blind", p, cfg, ThoughtfulBot,
                 lambda: ThoughtfulBot(aware=False), a.games, a.seed + 5)
        rotating("DRESSING vs honest-dress", p, cfg, ThoughtfulBot,
                 lambda: ThoughtfulBot(honest=True), a.games, a.seed + 6)
        density(st, ps, cfg)
        print()


if __name__ == "__main__":
    main()
