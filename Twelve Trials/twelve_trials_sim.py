"""TWELVE TRIALS — exact solver and tier tuning.

The game: all 36 cards dealt face-up. Rearrange freely; flipping a card leaves it
upside-down (the flip count tracks itself physically). Goal: 12 triples, each the
three cards of one symbol-triangle, showing its three symbols (a "perfect cycle").
Score = number of upside-down cards at the end. Lower is better.

Facts this script verifies / uses:
- K9 has exactly 840 triangle partitions (Steiner triple systems on labeled points).
- Within a partition, a triple's three dealt faces either already form a cycle
  (cost 0) or can be fixed by flipping exactly one card (cost 1) — never more,
  because the clockwise and anticlockwise mismatch counts always sum to 3.
- Therefore: any deal is always completable in at most 12 flips, and the deal's
  true optimum = 12 minus the maximum number of already-perfect triples over all
  840 partitions. This script computes that optimum exactly.

Usage: python3 twelve_trials_sim.py [deals=2000] [seed=42]
"""
import random, sys
from itertools import combinations

pairs = list(combinations(range(9), 2))

def gen_sts():
    systems = []
    def rec(remaining, triples):
        if not remaining:
            systems.append(tuple(triples)); return
        a, b = min(remaining)
        for c in range(9):
            if c in (a, b): continue
            p1, p2 = tuple(sorted((a, c))), tuple(sorted((b, c)))
            if p1 in remaining and p2 in remaining:
                rec(remaining - {(a, b), p1, p2}, triples + [(a, b, c)])
    rec(set(pairs), [])
    return systems

def triple_cost(deal, a, b, c):
    f1 = deal[(a, b)]; f2 = deal[tuple(sorted((b, c)))]; f3 = deal[tuple(sorted((a, c)))]
    cw = (f1 == a) + (f2 == b) + (f3 == c)
    return 0 if cw in (0, 3) else 1

def optimal(deal, STS):
    best = 12
    for sys_ in STS:
        broken = 0
        for (a, b, c) in sys_:
            broken += triple_cost(deal, a, b, c)
            if broken >= best: break
        best = min(best, broken)
        if best == 0: break
    return best

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    STS = gen_sts()
    print(f"Triangle partitions of K9: {len(STS)} (literature: 840)")
    rng = random.Random(seed)
    opt_d, rnd_d = {}, {}
    for _ in range(N):
        deal = {p: p[rng.random() < 0.5] for p in pairs}
        o = optimal(deal, STS)
        r = sum(triple_cost(deal, *t) for t in rng.choice(STS))
        opt_d[o] = opt_d.get(o, 0) + 1
        rnd_d[r] = rnd_d.get(r, 0) + 1
    print(f"\nExact optimal flips over {N} deals:")
    for k in sorted(opt_d): print(f"  {k:>2}: {100*opt_d[k]/N:5.1f}%")
    print("avg optimal:", round(sum(k*v for k, v in opt_d.items())/N, 2))
    print("\nRandom-partition baseline (no optimisation):")
    for k in sorted(rnd_d): print(f"  {k:>2}: {100*rnd_d[k]/N:5.1f}%")
    print("avg random:", round(sum(k*v for k, v in rnd_d.items())/N, 2))
