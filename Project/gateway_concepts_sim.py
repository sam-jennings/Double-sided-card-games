"""
Gateway game concepts — floor simulations.

Companion to GATEWAY_GAME_CONCEPTS.md. Reproduces every figure quoted there.

These are FLOOR sims with simple bots. They certify that the rules terminate,
scale across player counts, and are not degenerate (i.e. no single trivial
policy dominates). They say nothing about table feel.

Shared model
------------
The deck is the 36-card master deck: every unordered pair of pips 1-9 exactly
once. A card in play is [up_face, hidden_face]; playing it swaps the two.
Every concept uses the same physical frame: 3 cards face up per player, one
simultaneous push per round, 9 rounds, no draw deck.

Run:  python3 gateway_concepts_sim.py
"""

import itertools
import random
import statistics
from collections import Counter

DECK = [tuple(c) for c in itertools.combinations(range(1, 10), 2)]
ROUNDS = 9
GAMES = 8000
SEED = 42


def deal(n, hand=3):
    """Deal `hand` cards to each of n players, random orientation."""
    d = DECK[:]
    random.shuffle(d)
    hands = []
    for _ in range(n):
        h = []
        for _ in range(hand):
            a, b = d.pop()
            if random.random() < 0.5:
                a, b = b, a
            h.append([a, b])
        hands.append(h)
    return hands


def choose(cards, policy, table=None, me=None):
    """Return the index of the card this policy pushes forward."""
    if policy == "random":
        return random.randrange(len(cards))
    if policy == "greedy":                      # loudest available front
        return max(range(len(cards)), key=lambda j: cards[j][0])
    if policy == "timid":                       # quietest available front
        return min(range(len(cards)), key=lambda j: cards[j][0])
    if policy == "mid":
        return sorted(range(len(cards)), key=lambda j: cards[j][0])[len(cards) // 2]
    if policy == "backgreedy":                  # best hidden pip, ignore front
        return max(range(len(cards)), key=lambda j: cards[j][1])
    if policy == "reader":
        # Rows are public. Assume opponents lean on their best front; discount
        # any pip the table is likely to crowd, then take the best survivor.
        threat = Counter()
        for q, row in enumerate(table):
            if q == me:
                continue
            ups = [c[0] for c in row]
            best = max(ups)
            for u in ups:
                threat[u] += 0.6 if u == best else 0.2
        return max(range(len(cards)),
                   key=lambda j: cards[j][0] * max(0.0, 1 - threat[cards[j][0]]))
    raise ValueError(policy)


def flip_back(row, idx):
    c = row[idx]
    c[0], c[1] = c[1], c[0]


# --------------------------------------------------------------------------
# CLAMOUR - every unique shown pip scores itself; clashes score nothing.
# --------------------------------------------------------------------------
def clamour(n, policies, games=GAMES):
    totals = [0.0] * n
    clashed = []
    for _ in range(games):
        rows = deal(n)
        for _ in range(ROUNDS):
            picks = [choose(rows[p], policies[p], rows, p) for p in range(n)]
            shown = [rows[p][picks[p]][0] for p in range(n)]
            seen = Counter(shown)
            clashed.append(sum(1 for v in shown if seen[v] > 1) / n)
            for p in range(n):
                if seen[shown[p]] == 1:
                    totals[p] += shown[p]
                flip_back(rows[p], picks[p])
    return [t / games for t in totals], statistics.mean(clashed)


# --------------------------------------------------------------------------
# CAULDRON - sum of shown pips vs the Brim (6 per player).
#   at/under: everyone scores their shown pip
#   over:     nobody scores; the loudest loses their HIDDEN pip (ties all pay)
# --------------------------------------------------------------------------
def cauldron(n, policies, games=GAMES, brim_per_player=6):
    totals = [0.0] * n
    boils = rounds = 0
    for _ in range(games):
        rows = deal(n)
        for _ in range(ROUNDS):
            picks = [choose(rows[p], policies[p], rows, p) for p in range(n)]
            shown = [rows[p][picks[p]][0] for p in range(n)]
            rounds += 1
            if sum(shown) <= brim_per_player * n:
                for p in range(n):
                    totals[p] += shown[p]
            else:
                boils += 1
                loudest = max(shown)
                for p in range(n):
                    if shown[p] == loudest:
                        totals[p] -= rows[p][picks[p]][1]
            for p in range(n):
                flip_back(rows[p], picks[p])
    return [t / games for t in totals], boils / rounds


# --------------------------------------------------------------------------
# HUSH - the quieter half of the table score their HIDDEN pip.
# --------------------------------------------------------------------------
def hush(n, policies, games=GAMES):
    totals = [0.0] * n
    for _ in range(games):
        rows = deal(n)
        for _ in range(ROUNDS):
            picks = [choose(rows[p], policies[p], rows, p) for p in range(n)]
            shown = [rows[p][picks[p]][0] for p in range(n)]
            order = sorted(range(n), key=lambda p: (shown[p], random.random()))
            safe = set(order[:max(1, n // 2)])
            for p in range(n):
                if p in safe:
                    totals[p] += rows[p][picks[p]][1]
                flip_back(rows[p], picks[p])
    return [t / games for t in totals]


# --------------------------------------------------------------------------
# CRITIQUE MODE (July 2026) - measures the three faults Sam identified in
# CLAMOUR v1. See GATEWAY_CONCEPTS section 7.
# --------------------------------------------------------------------------
def ceiling_distribution(trials=200000):
    """Your best sign is your scoring ceiling for the whole game."""
    ceil = Counter()
    for _ in range(trials):
        d = DECK[:]
        random.shuffle(d)
        row = [d.pop() for _ in range(3)]
        ceil[max(s for c in row for s in c)] += 1
    return {k: v / trials for k, v in sorted(ceil.items())}


def crown_monopoly(n, trials=60000):
    """How often does exactly one player hold Crown access?"""
    one = 0
    for _ in range(trials):
        rows = deal(n)
        holders = [p for p in range(n)
                   if any(9 in (c[0], c[1]) for c in rows[p])]
        if len(holders) == 1:
            one += 1
    return one / trials


def free_money_rate(n, trials=40000):
    """Public rows: how often can a player see a sign no rival can show?"""
    safe = slots = 0
    for _ in range(trials):
        rows = deal(n)
        for p in range(n):
            mine = set(c[0] for c in rows[p])
            theirs = set(c[0] for q in range(n) if q != p for c in rows[q])
            slots += 1
            if mine - theirs:
                safe += 1
    return safe / slots


# --------------------------------------------------------------------------
# THE REPAIR - hidden hand of 3; you choose the card AND which way round to
# play it. The shown face settles the clash, the hidden face is your score.
# --------------------------------------------------------------------------
def equilibrium_show_distribution(n, iters=60, samples=4000, lr=0.25):
    """Fictitious play over which sign players choose to SHOW.

    Returns the converged distribution. A near-uniform result means no pure
    strategy dominates - i.e. there is a real decision every round. A spike
    means the game is a lookup, which is what killed v1.
    """
    q = [0.0] + [1 / 9] * 9
    for _ in range(iters):
        counts = Counter()
        for _ in range(samples):
            hand = [random.choice(DECK) for _ in range(3)]
            best = None
            for (a, b) in hand:
                for show, pay in ((a, b), (b, a)):
                    ev = pay * (1 - q[show]) ** (n - 1)
                    if best is None or ev > best[0]:
                        best = (ev, show)
            counts[best[1]] += 1
        q = [0.0] + [(1 - lr) * q[s] + lr * counts[s] / samples
                     for s in range(1, 10)]
    return q[1:]


def repaired_spread(n, pass_left, games=6000):
    """Best/worst final score. Passing the played card left recirculates the
    deck, so a bad deal stops being a life sentence."""
    spread = []
    for _ in range(games):
        rows = [list(r) for r in
                [[tuple(c) for c in row] for row in
                 [[random.choice(DECK) for _ in range(3)] for _ in range(n)]]]
        sc = [0] * n
        for _ in range(ROUNDS):
            plays = []
            for p in range(n):
                best = None
                for i, (a, b) in enumerate(rows[p]):
                    for show, pay in ((a, b), (b, a)):
                        if best is None or pay > best[2]:
                            best = (i, show, pay)
                plays.append(best)
            shown = [pl[1] for pl in plays]
            seen = Counter(shown)
            for p in range(n):
                i, show, pay = plays[p]
                if seen[show] == 1:
                    sc[p] += pay
                rows[p].pop(i)
            source = ([plays[(p - 1) % n] for p in range(n)] if pass_left
                      else plays)
            for p in range(n):
                _, show, pay = source[p]
                rows[p].append((show, pay))
        spread.append((max(sc), min(sc)))
    return statistics.mean(a for a, _ in spread), statistics.mean(b for _, b in spread)


def edge(scores):
    """Seat 0 is the test policy; the rest are the field."""
    field = statistics.mean(scores[1:])
    return scores[0], field, (scores[0] / field if abs(field) > 0.5 else float("nan"))


def main():
    random.seed(SEED)

    print("Deck check: %d cards, each pip on %d of them"
          % (len(DECK), Counter(s for c in DECK for s in c)[1]))

    print("\n=== CARD ECONOMY (3 cards each, no draw deck) ===")
    print(f"{'P':>3} {'in rows':>8} {'spare':>6}")
    for p in range(3, 13):
        print(f"{p:>3} {p * 3:>8} {36 - p * 3:>6}")

    print("\n=== CLAMOUR ===")
    print("clash% and top score are measured on an all-greedy table "
          "(everyone reaching for their best front).")
    print(f"{'P':>3} {'skilled/random':>15} {'reader vs greedy table':>23} "
          f"{'clash%':>8} {'top score':>10}")
    for n in [3, 4, 5, 6, 8, 10]:
        s, _ = clamour(n, ["greedy"] + ["random"] * (n - 1))
        _, _, e1 = edge(s)
        s2, _ = clamour(n, ["reader"] + ["greedy"] * (n - 1))
        _, _, e2 = edge(s2)
        top, clash = clamour(n, ["greedy"] * n)
        print(f"{n:>3} {e1:14.2f}x {e2:22.2f}x {clash * 100:7.0f}% {max(top):10.0f}")

    print("\n=== CAULDRON (Brim = 6 per player) ===")
    print(f"{'P':>3} {'greedy vs random':>17} {'greedy vs timid':>16} "
          f"{'boil% (random)':>15} {'boil% (greedy)':>15}")
    for n in [3, 4, 6, 8, 10]:
        s1, _ = cauldron(n, ["greedy"] + ["random"] * (n - 1))
        s2, _ = cauldron(n, ["greedy"] + ["timid"] * (n - 1))
        _, br = cauldron(n, ["random"] * n)
        _, bg = cauldron(n, ["greedy"] * n)
        print(f"{n:>3} {edge(s1)[2]:16.2f}x {edge(s2)[2]:15.2f}x "
              f"{br * 100:14.0f}% {bg * 100:14.0f}%")
    print("  NOTE: greedy still leads everywhere -> the brake is too weak.")
    print("        See GATEWAY_GAME_CONCEPTS.md section 3 for candidate fixes.")

    print("\n=== HUSH ===")
    print(f"{'P':>3} {'timid':>8} {'backgreedy':>12}   (edge vs a random field)")
    for n in [4, 6, 10]:
        a = edge(hush(n, ["timid"] + ["random"] * (n - 1)))[2]
        b = edge(hush(n, ["backgreedy"] + ["random"] * (n - 1)))[2]
        print(f"{n:>3} {a:7.2f}x {b:11.2f}x")
    print("  Non-degenerate (greed is punished) but the gap is thin.")

    # ---------------- critique of CLAMOUR v1 ----------------
    print("\n" + "=" * 70)
    print("CRITIQUE MODE - why CLAMOUR v1 was refused (section 7)")
    print("=" * 70)

    print("\n1. YOUR CEILING IS FIXED AT THE DEAL")
    ceil = ceiling_distribution()
    print("   best sign in your row: " +
          "  ".join(f"{k}:{v * 100:.1f}%" for k, v in ceil.items()))
    print(f"   -> {sum(v for k, v in ceil.items() if k < 8) * 100:.1f}% "
          "of deals can never show an 8 or 9")

    print("\n2. CROWN MONOPOLY (exactly one player holds Crown access)")
    for n in [3, 4, 5, 6]:
        print(f"   {n:>2}P: {crown_monopoly(n) * 100:5.1f}%")

    print("\n3. FREE MONEY (public rows => a risk-free sign exists)")
    for n in [3, 4, 5, 6, 8, 10]:
        print(f"   {n:>2}P: {free_money_rate(n) * 100:5.1f}% of player-turns")
    print("   At 3-5P the round is a lookup, not a read. This is fatal.")

    # ---------------- the repair ----------------
    print("\n" + "=" * 70)
    print("THE REPAIR - show one face to survive, score the other")
    print("=" * 70)

    print("\nEquilibrium distribution over which sign to SHOW (fictitious play).")
    print("Near-uniform = no dominant pure strategy = a real decision.")
    print(f"{'P':>3} | " + " ".join(f"{s:>5}" for s in range(1, 10)) + " |  max")
    for n in [3, 5, 10]:
        q = equilibrium_show_distribution(n)
        print(f"{n:>3} | " + " ".join(f"{x * 100:4.0f}%" for x in q) +
              f" | {max(q) * 100:3.0f}%")

    print("\nDoes passing the played card left unlock the ceiling?")
    print(f"{'P':>3} {'keep (best/worst)':>19} {'pass left':>14} {'gap closed':>11}")
    for n in [4, 6, 8, 10]:
        w1, l1 = repaired_spread(n, False)
        w2, l2 = repaired_spread(n, True)
        print(f"{n:>3} {w1:9.0f} /{l1:6.0f} {w2:7.0f} /{l2:5.0f} "
              f"{(1 - (w2 - l2) / (w1 - l1)) * 100:10.0f}%")


if __name__ == "__main__":
    main()
