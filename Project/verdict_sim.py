"""
VERDICT - floor simulation.

Companion to GATEWAY_GAME_CONCEPTS.md part two.

The game: one card face up in the middle (the Accused), showing a sign (the
Charge). Everyone simultaneously calls HIGHER or LOWER on its hidden face.
Flip it. Everyone who was right scores 1 point per player who was wrong.
Nobody is dealt anything and nobody holds a card at any point.

The odds are exact and printed on the card: a card showing sign S has its
hidden face uniform over the other 8 signs, so P(higher) = (9 - S) / 8.

This script runs the checks in the order they should have been run on
CLAMOUR v1:
  1. Is the answer obvious?  (fictitious play - does a pure strategy dominate?)
  2. Only then, how big is the skill gap?
  3. Does skill survive the game length, or is it noise?

Run:  python3 verdict_sim.py
"""

import itertools
import random
import statistics

SIGNS = list(range(1, 10))
DECK = [tuple(c) for c in itertools.combinations(SIGNS, 2)]
NAMES = {1: "Moon", 2: "Leaf", 3: "Wave", 4: "Flame", 5: "Eye",
         6: "Mask", 7: "Key", 8: "Star", 9: "Crown"}
SEED = 9


def live_partners(shown, spent):
    """Signs the hidden face could still be, given the pairs already resolved."""
    return [x for x in SIGNS
            if x != shown and tuple(sorted((shown, x))) not in spent]


def printed_odds(shown):
    """P(hidden is higher) from the visible pip alone - no memory needed."""
    return (9 - shown) / 8


# ---------------------------------------------------------------------------
# 1. OBVIOUSNESS - the test that CLAMOUR v1 failed
# ---------------------------------------------------------------------------
def equilibrium_split(p, n, iters=600, lr=0.08):
    """Fictitious play on the fraction of the table calling HIGHER.

    Because a correct player scores in proportion to how many were WRONG,
    piling onto the favourite destroys its own payoff. Converging on the true
    odds (rather than on 0% or 100%) means no pure strategy dominates.
    """
    f = 0.5
    for _ in range(iters):
        ev_high = p * (1 - f) * (n - 1)
        ev_low = (1 - p) * f * (n - 1)
        f = (1 - lr) * f + lr * (1.0 if ev_high > ev_low else 0.0)
    return f


# ---------------------------------------------------------------------------
# 2/3. PLAY
# ---------------------------------------------------------------------------
def vote(policy, charge, spent):
    """True = call HIGHER."""
    if policy == "random":
        return random.random() < 0.5
    if policy == "odds":                     # reads the pip, ignores the table
        return printed_odds(charge) > 0.5
    if policy == "mixed":                    # bets in proportion to the odds
        return random.random() < printed_odds(charge)
    if policy == "contra":                   # always takes the underdog
        return printed_odds(charge) <= 0.5
    if policy == "count":                    # tracks which pairs are spent
        cand = live_partners(charge, spent)
        p = sum(1 for x in cand if x > charge) / len(cand)
        return p > 0.5 if p != 0.5 else random.random() < 0.5
    raise ValueError(policy)


def run(n, policies, rounds=12, games=20000):
    totals = [0.0] * n
    wins = [0.0] * n
    solo = played_total = 0
    for _ in range(games):
        d = DECK[:]
        random.shuffle(d)
        spent = set()
        sc = [0.0] * n
        played = i = 0
        while played < rounds and i < len(d):
            card = d[i]
            i += 1
            charge = card[0] if random.random() < 0.5 else card[1]
            hidden = card[1] if charge == card[0] else card[0]
            if charge in (1, 9):                 # Moon/Crown answer themselves
                charge, hidden = hidden, charge
                if charge in (1, 9):             # the single Moon/Crown card
                    continue
            played += 1
            played_total += 1
            votes = [vote(policies[q], charge, spent) for q in range(n)]
            truth = hidden > charge
            wrong = sum(1 for v in votes if v != truth)
            if wrong == n - 1:
                solo += 1
            for q in range(n):
                if votes[q] == truth:
                    sc[q] += wrong
            spent.add(tuple(sorted(card)))
        for q in range(n):
            totals[q] += sc[q]
        best = max(sc)
        tied = sum(1 for x in sc if x == best)
        for q in range(n):
            if sc[q] == best:
                wins[q] += 1 / tied
    return ([t / games for t in totals],
            [w / games for w in wins],
            solo / played_total)


def main():
    random.seed(SEED)

    print("=" * 68)
    print("VERDICT - the odds are printed on the card")
    print("=" * 68)
    print(f"\n{'Charge':>7} {'sign':>7} {'P(higher)':>10}")
    for s in SIGNS:
        p = printed_odds(s)
        tag = "  <- certainty: turn the card over" if p in (0.0, 1.0) else (
              "  <- perfect coin flip" if p == 0.5 else "")
        print(f"{s:>7} {NAMES[s]:>7} {p * 100:9.1f}% {'#' * round(p * 20)}{tag}")
    print("\nUsable ladder 12.5%-87.5%. No memory required to play.")

    print("\n" + "=" * 68)
    print("1. OBVIOUSNESS TEST (run FIRST - this is what CLAMOUR v1 failed)")
    print("=" * 68)
    print("Does the table converge on a fixed answer (bad) or on the odds (good)?\n")
    print(f"{'Charge':>7} {'true odds':>10} " +
          " ".join(f"{n:>8}P" for n in [4, 6, 10]))
    for s in [2, 3, 4, 5, 6, 7, 8]:
        p = printed_odds(s)
        print(f"{NAMES[s]:>7} {p * 100:9.1f}% " +
              " ".join(f"{equilibrium_split(p, n) * 100:8.0f}%"
                       for n in [4, 6, 10]))
    print("\n-> tracks the true odds at every count. No pure strategy exists.")

    print("\n" + "=" * 68)
    print("2. SKILL GAP")
    print("=" * 68)
    print(f"\n{'P':>3} {'test':>8} {'field':>8} {'test':>8} {'field':>8} {'edge':>7}")
    for n in [4, 6, 10]:
        for tp, fl in [("odds", "random"), ("contra", "odds"),
                       ("odds", "mixed"), ("contra", "mixed")]:
            s, _, _ = run(n, [tp] + [fl] * (n - 1), games=8000)
            o = statistics.mean(s[1:])
            e = s[0] / o if abs(o) > 0.05 else float("inf")
            print(f"{n:>3} {tp:>8} {fl:>8} {s[0]:8.2f} {o:8.2f} {e:6.2f}x")
        print()
    print("Reading the pip beats guessing. A table that ALL reads the pip is")
    print("exploitable by a contrarian. At the mixed equilibrium nothing")
    print("dominates (~1.00x) - playable on sight, not solvable.")

    print("\n" + "=" * 68)
    print("3. DOES SKILL SURVIVE THE GAME LENGTH?")
    print("=" * 68)
    print("One odds-reader against a table of guessers.\n")
    print(f"{'P':>3} {'rounds':>7} {'fair share':>11} {'wins':>8} {'lift':>7}")
    for n in [4, 6, 10]:
        for r in [9, 12, 16]:
            _, w, _ = run(n, ["odds"] + ["random"] * (n - 1),
                          rounds=r, games=8000)
            print(f"{n:>3} {r:>7} {100 / n:10.1f}% {w[0] * 100:7.1f}% "
                  f"{w[0] * n:6.2f}x")
        print()

    print("=" * 68)
    print("4. THE SIGNATURE MOMENT - one player against the whole table")
    print("=" * 68)
    for n in [4, 6, 10]:
        _, _, solo = run(n, ["mixed"] * n, rounds=12, games=8000)
        print(f"  {n:>2}P: {solo * 100:4.1f}% of rounds "
              f"({solo * 12:.1f} times per 12-round game)")
    print("\n  Rare at 10P - but worth 9 points when it lands.")


if __name__ == "__main__":
    main()
