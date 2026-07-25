#!/usr/bin/env python3
"""COVENANT (version A) — chapter-mechanic scoping model.

Not a game simulator (there are no rules yet). This is a back-of-envelope
computation to answer one design question for the chapter-mechanic exploration:
*if a chapter is a purely BLIND permutation match, how luck-heavy is it, and how
much can skill (pure logical deduction from yes/no feedback) actually help?*

Setup modelled: in the chapter that admits a new sign S, there are k identical-
looking attackers whose hidden faces are a permutation of the k already-won
signs. A "claim" names (attacker, sign); flipping answers yes/no. A wrong claim
costs 1 card of health. Health budget = the current covenant deck = C(k,2).

Strategies compared:
  - random_legal: resolve attackers left-to-right; for the current attacker,
    guess uniformly among signs not yet placed; keep guessing it until a hit.
    (Only cross-constraint used: a placed sign is gone.)
  - deducer: full permutation constraint propagation (a row with one candidate,
    or a sign with one possible attacker, is placed for free); when nothing is
    forced, gamble on the smallest candidate set. This is the no-memory skill
    ceiling: every legal inference is taken.

Also reported for reference: memory (perfect recall => 0 misses) and
peek-and-commit (reveal k-1 faces, deduce the last => exactly k-1 spent, no
gambling).
"""

from __future__ import annotations

import random
from math import comb, factorial


def random_legal(perm: list[int]) -> int:
    """Misses under left-to-right blind guessing with placed-sign elimination."""
    k = len(perm)
    placed: set[int] = set()
    misses = 0
    for attacker in range(k):
        tried: set[int] = set()
        while True:
            candidates = [s for s in range(k) if s not in placed and s not in tried]
            guess = random.choice(candidates)
            if guess == perm[attacker]:
                placed.add(guess)
                break
            tried.add(guess)
            misses += 1
    return misses


def deducer(perm: list[int]) -> int:
    """Misses under full constraint propagation + smallest-set gambling."""
    k = len(perm)
    cand = [set(range(k)) for _ in range(k)]  # candidate signs per attacker
    placed = [False] * k
    misses = 0

    def propagate() -> None:
        changed = True
        while changed:
            changed = False
            # Row rule: an attacker with a single candidate must be that sign.
            for a in range(k):
                if not placed[a] and len(cand[a]) == 1:
                    s = next(iter(cand[a]))
                    place(a, s)
                    changed = True
            # Column rule: a sign with a single possible attacker goes there.
            for s in range(k):
                homes = [a for a in range(k) if not placed[a] and s in cand[a]]
                if len(homes) == 1 and not placed[homes[0]]:
                    place(homes[0], s)
                    changed = True

    def place(a: int, s: int) -> None:
        placed[a] = True
        cand[a] = {s}
        for other in range(k):
            if other != a:
                cand[other].discard(s)

    propagate()
    while not all(placed):
        # Gamble on the most-constrained unplaced attacker.
        a = min((x for x in range(k) if not placed[x]), key=lambda x: len(cand[x]))
        guess = random.choice(sorted(cand[a]))
        if guess == perm[a]:
            place(a, guess)
        else:
            cand[a].discard(guess)
            misses += 1
        propagate()
    return misses


def survives(misses: int, k: int) -> bool:
    return misses <= comb(k, 2)  # health budget = current deck size C(k,2)


def run(k: int, trials: int, seed: int) -> None:
    random.seed(seed)
    base = list(range(k))
    rl_miss = dl_miss = rl_win = dl_win = 0
    for _ in range(trials):
        perm = base[:]
        random.shuffle(perm)
        m1 = random_legal(perm)
        perm2 = base[:]
        random.shuffle(perm2)
        m2 = deducer(perm2)
        rl_miss += m1
        dl_miss += m2
        rl_win += survives(m1, k)
        dl_win += survives(m2, k)
    health = comb(k, 2)
    print(
        f"k={k:>2} attackers | perms k!={factorial(k):>7,} | health(deck)=C(k,2)={health:>2} "
        f"|| random-legal: {rl_miss/trials:5.2f} misses, win {100*rl_win/trials:5.1f}% "
        f"| deducer: {dl_miss/trials:5.2f} misses, win {100*dl_win/trials:5.1f}% "
        f"| memory:0  peek-commit:{k-1}"
    )


if __name__ == "__main__":
    TRIALS = 200_000
    print("COVENANT v.A — blind permutation-match scoping (health budget = deck = C(k,2))\n")
    for k in range(4, 9):  # chapters 2..6 admit signs with k = 4..8 won signs
        run(k, TRIALS, seed=1000 + k)
    print("\nNote: closed form for random-legal expected misses is C(k,2)/2.")
