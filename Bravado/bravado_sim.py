#!/usr/bin/env python3
"""BRAVADO -- exact deck facts and a floor simulation.

Three jobs, in order:

1. **Exact enumeration** of every combinatorial claim the rulebook makes:
   the distribution of the pip you are shown, the printed odds table
   P(higher | shown S) = (9 - S) / 8, the accuracy of ignoring the Caller and
   simply calling the favourite, and the six-player card-supply bound.

2. **The value of a read.** The Caller's one word is adversarial cheap talk,
   so at equilibrium it carries no information and the sim models it as noise.
   Section 2 instead measures the Bayesian ceiling: how much accuracy a player
   gains as a function of how reliably they can call the Caller truthful.
   That is the number only a table test can fill in.

3. **Floor simulation** of the round: termination, card supply, the
   bank-versus-push curve, seat fairness, the skill gap between policies, and
   how much the shrinking pair-registry is actually worth.

All bots rotate through every seat so that skill figures are not contaminated
by seat effects; seat effects are measured separately with identical bots.

Run: python bravado_sim.py
"""

from __future__ import annotations

import itertools
import random
from collections import Counter

DECK: list[tuple[int, int]] = [tuple(c) for c in itertools.combinations(range(1, 10), 2)]
STREAK_CAP = 6
DEFAULT_TARGET = 4          # the EV-maximising push depth, derived in section 3
ROUNDS = 40_000


# --------------------------------------------------------------------------
# 1. Exact deck facts
# --------------------------------------------------------------------------

def exact_facts() -> dict[str, object]:
    assert len(DECK) == 36, "the master deck is 36 cards"
    assert all(a != b for a, b in DECK), "no card pairs a sign with itself -- ties are impossible"

    slots = [(shown, hidden) for a, b in DECK for shown, hidden in ((a, b), (b, a))]
    assert len(slots) == 72, "36 cards x 2 orientations"

    shown_counts = Counter(shown for shown, _ in slots)

    odds: dict[int, float] = {}
    for s in range(1, 10):
        partners = [hidden for shown, hidden in slots if shown == s]
        assert len(partners) == 8, f"sign {s} sits on 8 cards"
        assert sorted(partners) == sorted(set(range(1, 10)) - {s}), (
            f"sign {s}'s partners are every other sign exactly once"
        )
        odds[s] = sum(1 for h in partners if h > s) / 8
        assert abs(odds[s] - (9 - s) / 8) < 1e-12, "enumeration disagrees with (9-S)/8"

    # Accuracy of ignoring the advice and calling the favourite side of the pip.
    # At S = 5 the pip is a true coin flip; score it as half a call.
    favourite_hits = 0.0
    for shown, hidden in slots:
        higher_count, lower_count = 9 - shown, shown - 1
        if higher_count > lower_count:
            favourite_hits += hidden > shown
        elif lower_count > higher_count:
            favourite_hits += hidden < shown
        else:
            favourite_hits += 0.5
    favourite_accuracy = favourite_hits / len(slots)

    # A run resolves at most STREAK_CAP cards: six successes (automatic bank),
    # or five successes and a bust.
    supply = {n: n * STREAK_CAP for n in (3, 4, 5, 6)}

    return {
        "shown_counts": shown_counts,
        "odds": odds,
        "favourite_accuracy": favourite_accuracy,
        "supply": supply,
    }


# --------------------------------------------------------------------------
# 2. Value of a read
# --------------------------------------------------------------------------

def value_of_a_read(trust: float) -> float:
    """Per-card accuracy of a player who knows the Caller tells the truth with
    probability `trust` and plays the Bayesian posterior."""
    hits = 0.0
    for a, b in DECK:
        for shown, hidden in ((a, b), (b, a)):
            prior = (9 - shown) / 8
            truth_is_higher = hidden > shown
            for message_higher in (True, False):
                p_message = trust if message_higher == truth_is_higher else 1 - trust
                p_msg_given_higher = trust if message_higher else 1 - trust
                p_msg_given_lower = 1 - trust if message_higher else trust
                evidence = prior * p_msg_given_higher + (1 - prior) * p_msg_given_lower
                posterior = (prior * p_msg_given_higher / evidence) if evidence else prior
                if abs(posterior - 0.5) < 1e-12:
                    hits += 0.5 * p_message
                else:
                    hits += ((posterior > 0.5) == truth_is_higher) * p_message
    return hits / 72


# --------------------------------------------------------------------------
# 3. Bots
# --------------------------------------------------------------------------

class Player:
    def __init__(self, name: str, call: str, stop: str, target: int = DEFAULT_TARGET) -> None:
        self.name = name
        self.call = call      # 'coin' | 'follow' | 'invert' | 'pip' | 'count'
        self.stop = stop      # 'fixed' | 'chase'
        self.target = target

    @staticmethod
    def live_partners(shown: int, resolved: list[tuple[int, int]]) -> list[int]:
        """Partners of `shown` not yet accounted for. Every pair exists once, so
        a resolved card showing `shown` permanently removes one candidate."""
        gone = {(b if a == shown else a) for a, b in resolved if shown in (a, b)}
        return [p for p in range(1, 10) if p != shown and p not in gone]

    def decide(self, shown: int, message_higher: bool, resolved: list[tuple[int, int]],
               rng: random.Random) -> bool:
        if self.call == "coin":
            return rng.random() < 0.5
        if self.call == "follow":
            return message_higher
        if self.call == "invert":
            return not message_higher
        if self.call == "pip":
            higher, lower = 9 - shown, shown - 1
        elif self.call == "count":
            live = self.live_partners(shown, resolved)
            if not live:
                return rng.random() < 0.5
            higher = sum(1 for p in live if p > shown)
            lower = len(live) - higher
        else:
            raise ValueError(self.call)
        if higher == lower:
            return rng.random() < 0.5
        return higher > lower

    def push(self, streak: int, best_banked: int) -> bool:
        if streak >= STREAK_CAP:
            return False
        if self.stop == "fixed":
            return streak < self.target
        if self.stop == "chase":
            # Push to the EV depth, and further if that would not beat the
            # leader -- matching the leader loses the tie.
            return streak < min(STREAK_CAP, max(self.target, best_banked + 1))
        raise ValueError(self.stop)


# --------------------------------------------------------------------------
# 4. One round
# --------------------------------------------------------------------------

def play_round(players: list[Player], rng: random.Random,
               probe: dict[str, list] | None = None) -> dict[str, object]:
    box = DECK[:]
    rng.shuffle(box)
    resolved: list[tuple[int, int]] = []
    banked: list[int] = []
    best_banked = 0
    busts = 0

    for player in players:
        streak = 0
        while True:
            if not box:                        # the box ran dry mid-run
                break
            if streak and not player.push(streak, best_banked):
                break
            a, b = box.pop()
            shown, hidden = (a, b) if rng.random() < 0.5 else (b, a)

            if probe is not None:
                # How much has the public row narrowed this card, and would the
                # registry change the call the pip alone would make?
                live = Player.live_partners(shown, resolved)
                probe["eliminated"].append(8 - len(live))
                pip_h, pip_l = 9 - shown, shown - 1
                cnt_h = sum(1 for p in live if p > shown)
                cnt_l = len(live) - cnt_h
                pip_call = None if pip_h == pip_l else pip_h > pip_l
                cnt_call = None if cnt_h == cnt_l else cnt_h > cnt_l
                probe["diverged"].append(pip_call is not cnt_call
                                         and not (pip_call is None and cnt_call is None))
                probe["pip_right"].append(0.5 if pip_call is None
                                          else float(pip_call == (hidden > shown)))
                probe["count_right"].append(0.5 if cnt_call is None
                                            else float(cnt_call == (hidden > shown)))

            # The Caller's word: adversarial cheap talk, modelled as noise.
            message_higher = rng.random() < 0.5
            called_higher = player.decide(shown, message_higher, resolved, rng)
            resolved.append((a, b))

            if called_higher == (hidden > shown):
                streak += 1
                if streak >= STREAK_CAP:
                    break
            else:
                streak = 0
                busts += 1
                break
        banked.append(streak)
        best_banked = max(best_banked, streak)

    winner = max(range(len(players)), key=lambda i: (banked[i], -i))  # first bank takes ties
    return {
        "banked": banked,
        "winner": winner,
        "cards_used": len(resolved),
        "box_emptied": not box,
        "busts": busts,
    }


def run(players: list[Player], rounds: int, seed: int, rotate: bool = True,
        probe: dict[str, list] | None = None) -> dict[str, object]:
    """Play `rounds` rounds. With rotate=True the seating is cycled so each bot
    spends equal time in every seat, separating skill from seat order."""
    rng = random.Random(seed)
    n = len(players)
    by_name: Counter[str] = Counter()
    by_seat: Counter[int] = Counter()
    banked_by_name: Counter[str] = Counter()
    cards_max = 0
    emptied = 0
    busts = 0
    for r in range(rounds):
        offset = (r % n) if rotate else 0
        seating = players[offset:] + players[:offset]
        result = play_round(seating, rng, probe)
        by_name[seating[result["winner"]].name] += 1
        by_seat[result["winner"]] += 1
        for seat, value in enumerate(result["banked"]):
            banked_by_name[seating[seat].name] += value
        cards_max = max(cards_max, result["cards_used"])
        emptied += result["box_emptied"]
        busts += result["busts"]
    return {
        "by_name": by_name,
        "by_seat": by_seat,
        "banked_by_name": banked_by_name,
        "cards_max": cards_max,
        "emptied": emptied,
        "busts": busts,
        "rounds": rounds,
    }


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

SIGNS = ["Moon", "Leaf", "Wave", "Flame", "Eye", "Mask", "Key", "Star", "Crown"]
BAR = "=" * 74


def main() -> None:
    facts = exact_facts()
    baseline = facts["favourite_accuracy"]

    print(BAR)
    print("1. EXACT DECK FACTS (enumerated over all 36 cards x 2 orientations)")
    print(BAR)
    counts = facts["shown_counts"]
    print(f"Face-slots per sign: {sorted(set(counts.values()))} -> "
          f"P(shown any given sign) = 8/72 = {8 / 72:.4f} (uniform)")
    print("\nThe printed odds table -- P(hidden face is higher | you see S):")
    print("  " + " | ".join(f"{s:>5}" for s in SIGNS))
    print("  " + " | ".join(f"{facts['odds'][i + 1] * 100:4.1f}%" for i in range(9)))
    print(f"\nIgnore the Caller, call the favourite side of the pip: "
          f"{baseline * 100:.2f}% per card")
    print("  Moon and Crown are free calls; Eye is a true coin flip.")
    print("\nCard supply -- worst-case cards resolved in a round (max 6 per run):")
    for n, total in facts["supply"].items():
        print(f"  {n}P: {total:2d} of 36" + ("   <- exactly the whole deck, zero slack"
                                            if total == 36 else ""))

    print()
    print(BAR)
    print("2. VALUE OF A READ (exact Bayesian ceiling, per card)")
    print(BAR)
    print("If you believe the Caller tells the truth with probability t and play")
    print("the posterior, your per-card accuracy is:\n")
    print("     t   accuracy   vs. ignoring the Caller")
    for t in (0.00, 0.10, 0.25, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.75, 0.90, 1.00):
        acc = value_of_a_read(t)
        note = "   <- no read: the advice is worth nothing" if abs(t - 0.5) < 1e-9 else ""
        print(f"  {t:4.2f}   {acc * 100:6.2f}%   {acc / baseline:5.3f}x{note}")

    print()
    print(BAR)
    print(f"3. FLOOR SIM -- {ROUNDS:,} rounds per configuration, Caller as noise")
    print(BAR)

    print("\n3a. Bank versus push. One bot commits to depth k; three push to 4.")
    print("    Seats rotate, so this is skill only.\n")
    print("     k   avg banked streak   round-win share (fair 25.00%)")
    best_k, best_share = None, -1.0
    for k in range(1, 7):
        hero = Player(f"push-{k}", "pip", "fixed", k)
        foil = [Player(f"foil{i}", "pip", "fixed", 4) for i in range(3)]
        out = run([hero] + foil, ROUNDS, seed=1000 + k)
        avg = out["banked_by_name"][hero.name] / ROUNDS
        share = out["by_name"][hero.name] / ROUNDS
        if share > best_share:
            best_k, best_share = k, share
        print(f"     {k}   {avg:15.3f}   {share * 100:5.2f}%")
    print(f"\n    EV-maximising depth: push to {best_k}. Depths 3-5 sit within a few")
    print("    points of each other, which is what makes bank-or-push a live choice.")

    print("\n3b. Seat fairness -- identical bots (pip, chase the leader).")
    print("    Two opposing biases: 'first to bank takes ties' favours early")
    print("    seats; knowing the benchmark favours late seats.\n")
    for n in (3, 4, 5, 6):
        table = [Player(f"p{i}", "pip", "chase") for i in range(n)]
        out = run(table, ROUNDS, seed=2000 + n, rotate=False)
        shares = [out["by_seat"][i] / ROUNDS * 100 for i in range(n)]
        spread = max(shares) - min(shares)
        print(f"    {n}P  " + "  ".join(f"s{i + 1} {s:5.2f}%" for i, s in enumerate(shares))
              + f"   spread {spread:5.2f}pp (fair {100 / n:.2f}%)")

    print("\n3c. Skill gap -- 4P, seats rotated.\n")
    contests = [
        ("pip + chase", "coin + push-3",
         Player("hero", "pip", "chase"), lambda i: Player(f"f{i}", "coin", "fixed", 3)),
        ("count + chase", "coin + push-3",
         Player("hero", "count", "chase"), lambda i: Player(f"f{i}", "coin", "fixed", 3)),
        ("count + chase", "pip + chase",
         Player("hero", "count", "chase"), lambda i: Player(f"f{i}", "pip", "chase")),
        ("always follow the Caller", "pip + chase",
         Player("hero", "follow", "chase"), lambda i: Player(f"f{i}", "pip", "chase")),
        ("always contradict the Caller", "pip + chase",
         Player("hero", "invert", "chase"), lambda i: Player(f"f{i}", "pip", "chase")),
    ]
    for hero_label, foil_label, hero, make_foil in contests:
        table = [hero] + [make_foil(i) for i in range(3)]
        out = run(table, ROUNDS, seed=3000 + len(hero_label) * 7)
        share = out["by_name"]["hero"] / ROUNDS
        print(f"    {hero_label:28s} vs 3x {foil_label:16s} "
              f"{share * 100:5.2f}%  = {share / 0.25:4.2f}x fair")

    print("\n3d. Is the shrinking pair-registry worth anything?")
    print("    Measured over every card resolved in a 6P round (the deepest case).\n")
    probe: dict[str, list] = {"eliminated": [], "diverged": [],
                              "pip_right": [], "count_right": []}
    table = [Player(f"p{i}", "pip", "chase") for i in range(6)]
    run(table, ROUNDS, seed=5000, rotate=False, probe=probe)
    m = len(probe["eliminated"])
    print(f"    cards observed                       {m:,}")
    print(f"    avg partners already eliminated      {sum(probe['eliminated']) / m:.2f} of 8")
    print(f"    calls where counting differs from pip {sum(probe['diverged']) / m * 100:.2f}%")
    print(f"    accuracy, pip only                   {sum(probe['pip_right']) / m * 100:.2f}%")
    print(f"    accuracy, pip + registry             {sum(probe['count_right']) / m * 100:.2f}%")

    print("\n3e. Termination and supply (pip + chase, all seats).\n")
    for n in (3, 4, 5, 6):
        table = [Player(f"p{i}", "pip", "chase") for i in range(n)]
        out = run(table, ROUNDS, seed=4000 + n, rotate=False)
        print(f"    {n}P  max cards used {out['cards_max']:2d}/36   "
              f"box emptied {out['emptied'] / ROUNDS * 100:.3f}% of rounds   "
              f"busts/round {out['busts'] / ROUNDS:.2f}")

    print("\nSections 1-2 are exact enumerations. Section 3 is a floor simulation")
    print("with the Caller's advice modelled as noise -- it certifies that the")
    print("rules terminate and are non-degenerate, and says nothing about tells.")


if __name__ == "__main__":
    main()
