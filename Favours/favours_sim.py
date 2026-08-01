"""FAVOURS — design simulation.

Checks the three questions the concept left open:
  1. Does the scoring fix actually price spoiling? (the fatal bug in the sketch)
  2. Is the 6P/8P spare-card removal fair?
  3. What do scores, ties and forced plays look like at each count?

Run: python3 favours_sim.py
"""
import random, itertools
from collections import Counter

DECK = [(a, b) for a, b in itertools.combinations(range(1, 10), 2)]  # 36 cards, pip = sign
SIGNS = {1:'Moon',2:'Leaf',3:'Wave',4:'Flame',5:'Eye',6:'Mask',7:'Key',8:'Star',9:'Crown'}


def matching(p):
    """The perfect matching removed at even counts: p/2 disjoint cards covering every sign once."""
    return [(i + 1, p - i) for i in range(p // 2)]


def subdeck(p, fair=True):
    d = [c for c in DECK if c[0] <= p and c[1] <= p]
    if p % 2 == 0 and fair:
        rm = set(matching(p))
        d = [c for c in d if c not in rm]
    return d


def deal(p, fair=True):
    d = subdeck(p, fair)[:]
    random.shuffle(d)
    h = len(d) // p
    return [list(d[i * h:(i + 1) * h]) for i in range(p)], h


# ---------------------------------------------------------------- 1. spoiling
def price_of_spoiling(p=7, trials=40000):
    """A player who can see this round's other gifts chooses: land it, or crowd it.
    Returns what crowding costs them under each scoring rule."""
    out = {}
    for mode in ('sketch', 'snub'):
        denied = cost = n = 0
        for _ in range(trials):
            hands, _h = deal(p)
            gifts = {i: random.choice([s - 1 for s in hands[i][0] if s - 1 != i]
                                      or [s - 1 for s in hands[i][0]]) for i in range(1, p)}
            opts = [s - 1 for s in hands[0][0] if s - 1 != 0]
            if len(opts) < 2:
                continue
            base = Counter(gifts.values())
            if not [o for o in opts if base[o] == 0] or not [o for o in opts if base[o] == 1]:
                continue
            n += 1
            denied += 1                              # crowding always denies exactly one favour
            cost += 1 if mode == 'snub' else 0       # ...and under 'snub' the card comes back as -1
        out[mode] = (denied / n, cost / n)
    return out


# ---------------------------------------------------------------- 2. fairness
def fairness(p, trials=5000):
    """Spread in how often each player's sign appears, arbitrary removal vs perfect matching."""
    arb = 0
    for _ in range(trials):
        d = [c for c in DECK if c[0] <= p and c[1] <= p]
        random.shuffle(d)
        used = d[len(d) % p:]
        c = Counter(s for card in used for s in card)
        arb += max(c.values()) - min(c.values())
    c = Counter(s for card in subdeck(p) for s in card)
    return arb / trials, max(c.values()) - min(c.values())


# ---------------------------------------------------------------- 3. the game
def play(p, mode='counter', spoilers=(), trials=20000):
    wins, ties, spread, forced, neg = Counter(), 0, 0, 0, 0
    for _ in range(trials):
        hands, h = deal(p)
        forced += sum(1 for hd in hands for c in hd if (hands.index(hd) + 1) in c) / (p * h)
        sc, got = Counter(), Counter()
        for _r in range(h):
            gifts = {}
            for i in range(p):
                c = random.choice(hands[i]); hands[i].remove(c)
                opts = [s - 1 for s in c if s - 1 != i] or [s - 1 for s in c]
                gifts[i] = (max(opts, key=lambda x: got[x]) if (i in spoilers and len(opts) > 1)
                            else random.choice(opts))
            cnt = Counter(gifts.values())
            for g, r in gifts.items():
                got[r] += 1
                if cnt[r] == 1:
                    sc[r] += 1                       # recipient keeps the card
                    if mode == 'counter':
                        sc[g] += 1                   # giver takes a counter
                elif mode == 'snub':
                    sc[g] -= 1                       # variant: refused card returns as a snub
        vals = [sc[i] for i in range(p)]
        top = max(vals); w = [i for i in range(p) if sc[i] == top]
        if len(w) > 1: ties += 1
        for i in w: wins[i] += 1 / len(w)
        spread += top - min(vals); neg += sum(1 for v in vals if v < 0) / p
    return ({i: wins[i] / trials for i in range(p)}, ties / trials,
            spread / trials, forced / trials, neg / trials, top)


if __name__ == '__main__':
    random.seed(2026)
    print("=" * 68)
    print("1. THE PRICE OF SPOILING  (7P, spoiler who can see the other gifts)")
    print("=" * 68)
    for mode, (d, c) in price_of_spoiling().items():
        label = "sketch (recipient only)" if mode == 'sketch' else "adopted (giver takes a counter)"
        print(f"  {label:32s} denies {d:.2f} | costs the spoiler {c:.2f}"
              f"  -> {'FREE: spite is dominant' if c == 0 else 'priced: a real trade-off'}")

    print("\n" + "=" * 68)
    print("2. SPARE-CARD FAIRNESS AT EVEN COUNTS")
    print("=" * 68)
    for p in (6, 8):
        arb, fair = fairness(p)
        names = ' / '.join(f"{SIGNS[a]}-{SIGNS[b]}" for a, b in matching(p))
        print(f"  {p}P  arbitrary removal: sign-frequency spread {arb:.2f}")
        print(f"      remove {names}: spread {fair}")

    print("\n" + "=" * 68)
    print("3. THE GAME  (random play, adopted scoring: recipient keeps card, giver takes counter)")
    print("=" * 68)
    print(f"  {'':4s} {'cards':>5s} {'rounds':>6s} {'ties':>6s} {'spread':>7s} {'forced':>7s} {'below 0':>8s}")
    for p in (5, 6, 7, 8, 9):
        d = subdeck(p); h = len(d) // p
        _w, t, s, f, n, _ = play(p)
        _w2, t2, s2, _f, n2, _ = play(p, mode='snub')
        print(f"  {p}P   {h:5d} {h:6d} {t:5.0%} {s:7.1f} {f:7.0%} {n:8.0%}"
              f"   | snub variant: ties {t2:.0%}, {n2:.0%} finish below zero")

    print("\n  One spoiler vs a random table (does spite pay?):")
    for p in (7, 9):
        w, *_ = play(p, spoilers={0})
        others = sum(w[i] for i in range(1, p)) / (p - 1)
        print(f"    {p}P: spoiler wins {w[0]:.1%} vs table average {others:.1%}")
