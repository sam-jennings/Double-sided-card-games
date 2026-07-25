"""
WILDFIRE - decision-density simulation.

Companion to WILDFIRE_excitement_diagnosis.md.

WILDFIRE_design_analysis.py tuned the game's BALANCE and found it healthy
(zero stalls, flat seats, 1.5-1.8x skill edge). The first table test then
reported the game "felt reactive rather than strategic". This script measures
the thing that reconciles those two results: how often a turn contains a
decision at all.

Metrics per turn:
    legal plays      how many cards in hand match a live target
    no play          the player cannot act and simply draws
    exactly 1 play   an action, but no decision
    a real choice    2+ legal plays
    choice mattered  2+ legal plays AND at least one blocks the next player
                     while another does not - i.e. the choice visibly decided
                     something the player can see happen

Section 1 validates the model against the published figures before any of the
above is trusted.

Run:  python3 wildfire_decision_sim.py
"""

import itertools
import math
import random
import statistics
from collections import Counter

DECK = [tuple(c) for c in itertools.combinations(range(1, 10), 2)]
DEAL = {3: 9, 4: 7, 5: 6, 6: 5}
SEED = 8


def other(card, sign):
    """The card's other face."""
    return card[1] if card[0] == sign else card[0]


def legal(hand, targets):
    """(card index, pile index) for every playable card/pile combination."""
    return [(i, k) for i, c in enumerate(hand)
            for k, t in enumerate(targets) if t in c]


def game(n, piles=1, hand=None, chain=2, policy=None, refusal=2,
         cap=800, stats=None, mirror="off", mirror_penalty="skip"):
    """Play one game. Returns (turns, winner).

    policy[p]        'random' | 'cruel' (strangle the next player)
                     | 'mirror' (seek a mirror, else play cruel)
    mirror           'off' | 'on' - a mirror is a visible fact on the table,
                     so it fires for WHOEVER makes it, deliberately or not.
    mirror_penalty   'skip' (next player misses their go) | 'draw' (takes 2)

    A mirror leaves both piles showing the same sign, which would otherwise
    halve everyone's options, so the penalised player flips a pile - clearing
    the jam at the cost of their turn.

    NOTE - a removed mode. An earlier version had mirror='called', intended to
    model "only a mirror the player notices and announces counts". It set the
    deliberate flag inside the mirror policy branch only, so in practice it
    fired the test seat's mirrors and never the opponents' - a privilege for
    one player rather than a rule, which inflated that seat's win rate. There
    is no honest version of it: a mirror is two matching faces lying on the
    table in front of the person who just played, so everyone sees it and it
    always fires. Removed rather than fixed.
    """
    if policy is None:
        policy = ["random"] * n
    d = DECK[:]
    random.shuffle(d)
    h = hand or DEAL[n]
    hands = [[d.pop() for _ in range(h)] for _ in range(n)]

    targets, stacks = [], []
    for _ in range(piles):
        c = d.pop()
        targets.append(c[0] if random.random() < 0.5 else c[1])
        stacks.append([c])
    well = d

    p = turns = 0
    penalised = set()
    while turns < cap:
        if p in penalised:
            penalised.discard(p)
            k = random.randrange(piles)                 # flip a pile: clear the jam
            if stacks[k]:
                targets[k] = other(stacks[k][-1], targets[k])
            if mirror_penalty == "draw":
                for _ in range(refusal):
                    if well:
                        hands[p].append(well.pop())
            p = (p + 1) % n
            continue
        turns += 1
        nxt = (p + 1) % n
        opts = legal(hands[p], targets)

        if stats is not None:
            stats["turns"] += 1
            stats["opts"].append(len(opts))
            if not opts:
                stats["refuse"] += 1
            if len(opts) >= 2:
                stats["choice"] += 1
            reachable = set()
            for i, k in opts:
                nt = list(targets)
                nt[k] = other(hands[p][i], targets[k])
                reachable.add(bool(legal(hands[nxt], nt)))
            if len(reachable) > 1:
                stats["pivotal"] += 1

        if opts:
            for _ in range(chain):
                opts = legal(hands[p], targets)
                if not opts:
                    break

                def answers(o):
                    i, k = o
                    nt = list(targets)
                    nt[k] = other(hands[p][i], targets[k])
                    return len(legal(hands[nxt], nt))

                mirrors = ([o for o in opts
                            if other(hands[p][o[0]], targets[o[1]])
                            == targets[1 - o[1]]] if piles == 2 else [])
                if policy[p] == "mirror" and mirrors:
                    i, k = random.choice(mirrors)
                elif policy[p] in ("cruel", "mirror"):
                    i, k = min(opts, key=answers)
                else:
                    i, k = random.choice(opts)
                card = hands[p].pop(i)
                targets[k] = other(card, targets[k])
                stacks[k].append(card)
                if not hands[p]:
                    return turns, p
        else:
            for _ in range(refusal):
                if not well:
                    big = max(range(piles), key=lambda k: len(stacks[k]))
                    if len(stacks[big]) > 1:
                        top = stacks[big].pop()
                        well.extend(stacks[big])
                        stacks[big] = [top]
                        random.shuffle(well)
                if well:
                    hands[p].append(well.pop())

        if mirror != "off" and piles == 2 and targets[0] == targets[1]:
            penalised.add(nxt)
            if stats is not None:
                stats["fired"] += 1
        p = (p + 1) % n
    return turns, None


def measure(n, piles=1, hand=None, chain=2, games=2500, policy=None, **kw):
    st = {"turns": 0, "opts": [], "refuse": 0, "choice": 0, "pivotal": 0,
          "fired": 0}
    lengths, stalls, wins = [], 0, Counter()
    for _ in range(games):
        t, w = game(n, piles, hand, chain, policy=policy, stats=st, **kw)
        lengths.append(t)
        if w is None:
            stalls += 1
        else:
            wins[w] += 1
    tot = sum(wins.values())
    return dict(
        tpp=statistics.mean(lengths) / n,
        stalls=stalls / games,
        opts=statistics.mean(st["opts"]),
        refuse=st["refuse"] / st["turns"],
        choice=st["choice"] / st["turns"],
        pivotal=st["pivotal"] / st["turns"],
        fired=st["fired"] / st["turns"],
        p0=(wins[0] / tot if tot else 0),
        wins=wins,
    )


def main():
    random.seed(SEED)

    print("=" * 78)
    print("1. MODEL VALIDATION against WILDFIRE_design_analysis.md section 3")
    print("=" * 78)
    print(f"\n{'config':>14} {'turns/player':>13} {'stalls':>8}   published")
    for n, ch, exp in [(3, 2, "11.1 t/p, 0%"), (4, 2, "9.4 t/p, 0%"),
                       (5, 2, "7.9 t/p, 0%"), (6, 2, "6.8 t/p, 0%"),
                       (3, 1, "81 t/p, 24%")]:
        r = measure(n, chain=ch, games=2000)
        print(f"{f'{n}P chain{ch}':>14} {r['tpp']:13.1f} {r['stalls']*100:7.0f}%"
              f"   {exp}")
    print("\nClose on every chain-2 config and it reproduces the chain-1 result")
    print("(a chainless game barely terminates). The model is faithful.")

    print("\n" + "=" * 78)
    print("2. DIAGNOSIS - how often does a turn contain a decision?")
    print("=" * 78)
    print(f"\n{'P':>3} {'deal':>5} {'legal plays':>12} {'no play':>9} "
          f"{'exactly 1':>10} {'a choice':>9} {'mattered':>9}")
    for n in [3, 4, 5, 6]:
        r = measure(n)
        one = 1 - r["refuse"] - r["choice"]
        print(f"{n:>3} {DEAL[n]:>5} {r['opts']:12.2f} {r['refuse']*100:8.0f}% "
              f"{one*100:9.0f}% {r['choice']*100:8.0f}% {r['pivotal']*100:8.0f}%")
    print("\n~70% of turns hold no decision at all. A card carries 2 of 9 signs,")
    print("so it matches the target with probability 2/9 - the hand rarely offers")
    print("more than one answer. This is decision density, not balance.")

    print("\n" + "=" * 78)
    print("3. FIX - two piles, i.e. two live targets. Nothing else changes.")
    print("=" * 78)
    print(f"\n{'P':>3} {'deal':>5} {'legal plays':>12} {'no play':>9} "
          f"{'a choice':>9} {'mattered':>9} {'t/player':>9} {'stalls':>7}")
    for n in [3, 4, 5, 6]:
        r = measure(n, piles=2, games=2000)
        print(f"{n:>3} {DEAL[n]:>5} {r['opts']:12.2f} {r['refuse']*100:8.0f}% "
              f"{r['choice']*100:8.0f}% {r['pivotal']*100:8.0f}% "
              f"{r['tpp']:9.1f} {r['stalls']*100:6.0f}%")
    print("\nDead turns nearly halve, turns offering a choice double, termination")
    print("is untouched. But 'mattered' barely moves: more options does NOT make")
    print("blocking easier, so the consequence stays delayed and diffuse.")

    print("\n" + "=" * 78)
    print("4. DROPPING CHAINING - viable only once two piles exist")
    print("=" * 78)
    print("\nAt one pile, chaining was the exhaust valve: removing it stalled 24%")
    print("of games. Two piles cuts refusals from 34% to 17%, switching off the")
    print("pump - and restores the length that two piles alone destroyed.\n")
    print(f"{'config':>28} {'stalls':>8} {'turns/player (3P)':>18}")
    for lbl, pi, ch in [("1 pile, chain 2 (shipped)", 1, 2),
                        ("1 pile, chain 1", 1, 1),
                        ("2 piles, chain 2", 2, 2),
                        ("2 piles, chain 1", 2, 1)]:
        r = measure(3, piles=pi, chain=ch, games=1500)
        print(f"{lbl:>28} {r['stalls']*100:7.0f}% {r['tpp']:18.1f}")

    print("\n" + "=" * 78)
    print("5. DOES SKILL PAY? one target-choosing player vs random opponents")
    print("=" * 78)
    print(f"\n{'config':>28} {'P':>3} {'fair share':>11} {'wins':>8} {'lift':>7}")
    for label, pi, ch in [("shipped (1 pile, chain 2)", 1, 2),
                          ("two piles, chain 2", 2, 2),
                          ("two piles, NO chaining", 2, 1)]:
        for n in [3, 4, 6]:
            pol = ["cruel"] + ["random"] * (n - 1)
            r = measure(n, piles=pi, chain=ch, games=3000, policy=pol)
            print(f"{label:>28} {n:>3} {100/n:10.1f}% {r['p0']*100:7.1f}% "
                  f"{r['p0']*n:6.2f}x")
        print()

    print("=" * 78)
    print("6. THE MIRROR RULE (same sign on both piles) - REJECTED")
    print("=" * 78)
    print("\nTwo questions have to be separated, or the rule and the strategy get")
    print("confused with each other:")
    print("  A vs B  does the RULE dilute skill?      (same bot, rule off vs on)")
    print("  B vs C  is MIRRORING a skill worth having? (rule on, both bots)")
    print("\nDifferences are a few points, so 15,000 games/arm with Wilson 95% CIs.\n")
    arms = 15000
    for n in [3, 4, 6]:
        print(f"--- {n}P (fair share {100/n:.1f}%) ---")
        configs = [
            ("A  rule OFF, cruel play", "cruel", {}),
            ("B  rule ON, cruel play (ignores mirrors)", "cruel",
             dict(mirror="on", mirror_penalty="draw")),
            ("C  rule ON, actively seeking mirrors", "mirror",
             dict(mirror="on", mirror_penalty="draw")),
            ("D  rule ON as proposed (miss a turn), seeking", "mirror",
             dict(mirror="on", mirror_penalty="skip")),
        ]
        for label, pol, kw in configs:
            r = measure(n, piles=2, chain=1, games=arms,
                        policy=[pol] + ["random"] * (n - 1), **kw)
            p, t = r["p0"], sum(r["wins"].values())
            z = 1.96
            d = 1 + z * z / t
            c = (p + z * z / (2 * t)) / d
            hw = z * math.sqrt(p * (1 - p) / t + z * z / (4 * t * t)) / d
            print(f"  {label:>46}: {p*100:5.1f}% "
                  f"[{(c-hw)*100:4.1f},{(c+hw)*100:4.1f}]  lift {p*n:.2f}x")
        print()
    print("A vs B: the rule measurably DILUTES skill at every count. Two piles")
    print("land on the same sign by chance about 1 turn in 9, so the penalty is")
    print("mostly an accident tax landing on whoever happens to be next.")
    print("B vs C: seeking mirrors is worth ~nothing, and is negative at 6P. The")
    print("key card is in hand only ~7-11% of turns, and playing it forfeits the")
    print("strangle play. Recommendation: two piles + no chaining, no mirror rule.")


if __name__ == "__main__":
    main()
