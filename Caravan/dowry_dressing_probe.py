"""Probe DOWRY's own simulator for the two numbers CARAVAN's floor run raised.

Imports ../Dowry/dowry_sim.py unchanged and re-measures it; it does not
modify DOWRY.  See CARAVAN_design_analysis.md sections 4 and 5b.

 1. DECISION DENSITY.  How often does the chooser take the pair, how often is
    one lot risk-free dominant, how often are the lots a wash?  These are the
    DOWRY reference figures CARAVAN's density table is compared against.

 2. A DRESSING-ONLY ABLATION.  DOWRY's published "dressing edge ~1.6-1.7x"
    comes from an arm whose HonestCutBot differs on TWO axes: it cuts for the
    most even TRUE split *and* it dresses informatively.  HonestDressBot below
    is identical to SkilledBot in every way except the dressing, which is the
    ablation that actually isolates the dressing layer.

Run:  python dowry_dressing_probe.py --games 150
"""
import sys, random, argparse, pathlib
from collections import Counter
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "Dowry"))
import dowry_sim as D


class HonestDressBot(D.SkilledBot):
    """Identical to SkilledBot except the dressing is forced informative."""
    deceptive = False

    def cut(self, g, me):
        you = 1 - me
        mine_c, yours_c = g.counts(me), g.counts(you)
        hand = g.hands[me]
        triples = list(D.combinations(hand, 3))
        if len(triples) > 30:
            triples = g.rng.sample(triples, 30)
        best, best_obj = None, -1e9
        for tri in triples:
            for single in range(3):
                lots = D.HonestCutBot._honest_dress(tri, single, mine_c, yours_c)
                obj = self._objective(g, me, you, lots, mine_c, yours_c)
                if obj > best_obj:
                    best_obj, best = obj, lots
        return best


STAT = Counter()


def _leaders(g, me, lot):
    mine, theirs = dict(g.counts(me)), g.counts(1 - me)
    for card, shown in lot:
        mine[D.best_face(card, mine, theirs)] += 1
    return tuple((0 if mine[s] > theirs[s] else 1 if theirs[s] > mine[s] else -1)
                 for s in D.SIGNS)


def instrumented_choose(orig):
    def choose(self, g, me, lots):
        pick = orig(self, g, me, lots)
        STAT["choices"] += 1
        STAT["pair"] += int(len(lots[pick]) == 2)
        # risk-free? worst case of one lot beats best case of the other
        band = []
        mine, theirs = g.counts(me), g.counts(1 - me)
        for lot in lots:
            lo = hi = 0.0
            for card, shown in lot:
                vals = [max(D.place_value(shown, mine, theirs),
                            D.place_value(h, mine, theirs))
                        for h in g.hidden_candidates(card, shown, me)]
                lo += min(vals); hi += max(vals)
            band.append((lo, hi))
        STAT["dominant"] += int(band[0][0] >= band[1][1] or band[1][0] >= band[0][1])
        e = [D.perceived_lot_value(g, lot, me) for lot in lots]
        _sc = max(1e-9, (abs(e[0]) + abs(e[1])) / 2)
        STAT["near_tie"] += int(abs(e[0] - e[1]) / _sc < 0.10)
        STAT["swing"] += int(_leaders(g, me, lots[pick]) != _leaders(g, me, lots[1 - pick]))
        return pick
    return choose


D.SkilledBot.choose = instrumented_choose(D.SkilledBot.choose)


def arm(name, b0, b1, games, seed):
    rng = random.Random(seed)
    wins, sc = [0, 0, 0], [0.0, 0.0]
    for _ in range(games):
        w, s, _t = D.play({0: b0, 1: b1}, rng)
        wins[2 if w is None else w] += 1
        sc[0] += s[0]; sc[1] += s[1]
    print(f"  {name:40s} P0 {wins[0]:4d} P1 {wins[1]:4d} shared {wins[2]:3d}"
          f" | avg {sc[0]/games:5.1f} v {sc[1]/games:5.1f}"
          f" | ratio {sc[0]/max(sc[1],1e-9):.2f}x")
    return sc[0] / games, sc[1] / games


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--games", type=int, default=300)
    a = ap.parse_args()
    print(f"DOWRY probe — {a.games} games/arm")
    arm("skilled mirror (for take-decision stats)", D.SkilledBot(), D.SkilledBot(), a.games, 11)
    c = STAT["choices"]
    print(f"    DOWRY take-decisions: {c}")
    print(f"    took the pair                 {100*STAT['pair']/c:5.1f}%")
    print(f"    risk-free / dominant takes    {100*STAT['dominant']/c:5.1f}%")
    print(f"    near-indifferent (<0.25 pip)  {100*STAT['near_tie']/c:5.1f}%")
    print(f"    takes that move a leader      {100*STAT['swing']/c:5.1f}%")
    STAT.clear()
    a0, b0 = arm("deceptive vs honest-CUT (published arm)", D.SkilledBot(), D.HonestCutBot(), a.games, 12)
    a1, b1 = arm("honest-CUT vs deceptive", D.HonestCutBot(), D.SkilledBot(), a.games, 13)
    print(f"    published-style dressing edge  {(a0+b1)/(b0+a1):.2f}x")
    STAT.clear()
    a2, b2 = arm("deceptive vs honest-DRESS only", D.SkilledBot(), HonestDressBot(), a.games, 14)
    a3, b3 = arm("honest-DRESS only vs deceptive", HonestDressBot(), D.SkilledBot(), a.games, 15)
    print(f"    dressing-ONLY edge             {(a2+b3)/(b2+a3):.2f}x")
