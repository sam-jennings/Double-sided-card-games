"""BLIGHT simulation — the avoidance trick-taker.

Questions:
  1. Skill gap: does ducking/shedding skill beat random? (target ≥1.5x)
  2. Shoot-the-rot frequency: how often does a player capture EVERY trick
     (the shoot-the-moon equivalent)? Is the rule live or dead?
  3. Penalty distribution & seat fairness — does anyone get crushed by seat?
  4. Behaviour across 3/4/6 players.

Engine (shared with GLEAN):
  - 36 cards = all pairs of 9 symbols; pip = symbol number 1..9.
  - Deal evenly: 3P=12, 4P=9, 6P=6.
  - Lead any card/face → led symbol. Follow by showing the led symbol (flip if
    needed) on either face; else slough. Among followers, highest HIDDEN pip
    wins; winner captures all cards, leads next.

BLIGHT scoring: a captured card's penalty = its HIDDEN-face pip (the strength
you couldn't see). Lowest total penalty wins.
SHOOT THE ROT: capture every trick in the round → you score 0 and each
opponent scores the round's total penalty.

Note: total penalty is endogenous — sum(shown)+sum(hidden)=360, so showing
high faces lowers the table's total poison. Players' face choices matter.

What the sim CANNOT model: whether ducking feels agonising or passive; whether
a surprise hidden 9 reads as drama or gotcha; teaching.
"""

import random
import itertools
from collections import Counter

SYMBOLS = list(range(1, 10))
DECK = [tuple(sorted(p)) for p in itertools.combinations(SYMBOLS, 2)]
assert len(DECK) == 36
HAND_SIZE = {3: 12, 4: 9, 6: 6}


def other(card, shown):
    return card[1] if card[0] == shown else card[0]


# ─── Bots ─────────────────────────────────────────────────────────────────────

def random_lead(hand, rng):
    card = rng.choice(hand)
    return card, rng.choice(card)


def random_follow(hand, led, trick, rng):
    followers = [c for c in hand if led in c]
    if followers:
        return rng.choice(followers), led
    card = rng.choice(hand)
    return card, rng.choice(card)


def skilled_lead(hand, rng):
    """Lead so you won't win your own trick: show the HIGH face, hide a LOW pip.
    Pick the card whose lower face is smallest (cheapest hidden)."""
    card = min(hand, key=lambda c: min(c))
    return card, max(card)  # show high → hidden is the low pip


def skilled_follow(hand, led, trick, rng):
    """Avoid winning; shed dangerous (high-hidden) cards when safe."""
    followers = [c for c in hand if led in c]
    if not followers:
        # slough the worst poison: hand the winner the highest hidden pip.
        # show the low face so the hidden face is as high as possible.
        card = max(hand, key=lambda c: max(c))
        return card, min(card)  # show low → hidden is the high pip
    cur = max([h for (_, _, _, h, f) in trick if f], default=0)
    # cards that LOSE right now (hidden below the current best follower)
    losing = [c for c in followers if other(c, led) < cur]
    if losing:
        # safely shed the most dangerous losing card (highest hidden)
        card = max(losing, key=lambda c: other(c, led))
        return card, led
    # can't guarantee a loss — minimise own hidden contribution
    card = min(followers, key=lambda c: other(c, led))
    return card, led


# ─── Game runner ──────────────────────────────────────────────────────────────

def run_round(n, bots, rng):
    deck = DECK[:]
    rng.shuffle(deck)
    h = HAND_SIZE[n]
    hands = [deck[i * h:(i + 1) * h] for i in range(n)]
    assert sum(len(x) for x in hands) == 36
    captured = [[] for _ in range(n)]
    tricks_won = [0] * n
    penalties = [0] * n
    leader = 0
    n_tricks = 36 // n
    for _ in range(n_tricks):
        trick = []
        led = None
        for i in range(n):
            pid = (leader + i) % n
            lead_fn, follow_fn = bots[pid]
            if i == 0:
                card, shown = lead_fn(hands[pid], rng)
                led = shown
            else:
                card, shown = follow_fn(hands[pid], led, trick, rng)
            hands[pid].remove(card)
            hid = other(card, shown)
            trick.append((pid, card, shown, hid, shown == led))
        followers = [(pid, hid) for (pid, _, _, hid, f) in trick if f]
        winner = max(followers, key=lambda x: x[1])[0]
        tricks_won[winner] += 1
        for (_, card, _, hid, _) in trick:
            captured[winner].append(card)
            penalties[winner] += hid
        leader = winner

    # Shoot the rot: someone won every trick
    shooter = next((i for i in range(n) if tricks_won[i] == n_tricks), None)
    total_penalty = sum(penalties)
    if shooter is not None:
        scores = [total_penalty] * n
        scores[shooter] = 0
        return scores, penalties, True, shooter
    return list(penalties), penalties, False, None


def pct(x):
    return f"{100*x:.1f}%"


def experiment(n_games=4000, seed=42):
    rng = random.Random(seed)
    print("=" * 78)
    print("BLIGHT SIMULATION — avoidance trick-taker")
    print(f"{n_games} rounds per configuration · seed {seed}")
    print("=" * 78)

    for n in (3, 4, 6):
        print(f"\n{'─' * 78}")
        print(f"  {n} PLAYERS · {HAND_SIZE[n]} cards each · {36 // n} tricks")
        print(f"{'─' * 78}")

        # All-skilled mirror: penalty distribution, seat fairness, shoots
        seat_wins = Counter()
        pen_all = []
        shoots = 0
        spreads = []
        for _ in range(n_games):
            bots = [(skilled_lead, skilled_follow)] * n
            scores, penalties, shot, shooter = run_round(n, bots, rng)
            if shot:
                shoots += 1
            best = min(scores)  # lowest penalty wins
            winners = [i for i in range(n) if scores[i] == best]
            for w in winners:
                seat_wins[w] += 1 / len(winners)
            pen_all.extend(penalties)
            spreads.append(max(penalties) - min(penalties))
        print(f"\n  [All-skilled mirror]")
        print(f"  Avg penalty per player: {sum(pen_all)/len(pen_all):.1f}")
        print(f"  Avg penalty spread (max−min): {sum(spreads)/len(spreads):.1f}")
        print(f"  Shoot-the-rot rate: {pct(shoots / n_games)}")
        seats = " ".join(f"s{i}:{pct(seat_wins[i]/n_games)}" for i in range(n))
        print(f"  Seat win shares (lowest penalty): {seats}")

        # Skill gap: 1 skilled vs (n-1) random
        sk_wins = 0
        done = 0
        for _ in range(n_games):
            seat = rng.randrange(n)
            bots = [(random_lead, random_follow)] * n
            bots[seat] = (skilled_lead, skilled_follow)
            scores, penalties, shot, shooter = run_round(n, bots, rng)
            best = min(scores)
            winners = [i for i in range(n) if scores[i] == best]
            done += 1
            if seat in winners:
                sk_wins += 1 / len(winners)
        base = 1.0 / n
        wr = sk_wins / done
        print(f"\n  [Skill gap: 1 skilled vs {n-1} random, seat randomised]")
        print(f"  Skilled win rate: {pct(wr)} (baseline {pct(base)}, "
              f"edge {wr/base:.2f}x)")

        # Shoot attempt: can a deliberately greedy bot ever shoot vs random?
        # (skilled bot ducks; this measures whether shooting is even feasible)
        greedy_shoots = 0
        for _ in range(n_games):
            seat = rng.randrange(n)
            # greedy = always try to WIN every trick (highest hidden)
            def greedy_lead(hand, rng):
                card = max(hand, key=lambda c: max(c))
                return card, min(card)  # show low, hide high → win

            def greedy_follow(hand, led, trick, rng):
                fols = [c for c in hand if led in c]
                if fols:
                    return max(fols, key=lambda c: other(c, led)), led
                # void: discard lowest card, any face
                card = min(hand, key=lambda c: max(c))
                return card, min(card)
            bots = [(random_lead, random_follow)] * n
            bots[seat] = (greedy_lead, greedy_follow)
            scores, penalties, shot, shooter = run_round(n, bots, rng)
            if shot and shooter == seat:
                greedy_shoots += 1
        print(f"\n  [Shoot feasibility: 1 greedy 'win-everything' bot vs random]")
        print(f"  Successful shoots: {pct(greedy_shoots / n_games)} of games")


if __name__ == "__main__":
    experiment()
