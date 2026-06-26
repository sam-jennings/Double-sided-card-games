"""GLEAN simulation — the accumulation trick-taker.

Questions:
  1. Does "highest hidden pip wins" DEGENERATE — i.e. is the winner just
     whoever holds high hidden pips (low skill), or is which-trick-to-contest
     a real lever (skill)?  → measured as skilled-vs-random edge.
  2. Skill gap (target ≥1.5x per the OUROBOROS standard).
  3. Score distribution, tie frequency, seat fairness.
  4. Behaviour across 3/4/6 players (clean deals on the 36-card deck).

Engine (shared with BLIGHT):
  - 36 cards = all pairs of 9 symbols; pip = symbol number 1..9.
  - Deal evenly: 3P=12, 4P=9, 6P=6.
  - Lead any card, choosing which face shows → led symbol.
  - Follow: must play a card carrying the led symbol on EITHER face, shown as
    the led symbol (flip to follow). Else slough (any card, any face).
  - Reveal: among followers (cards showing the led symbol — incl. the leader),
    highest HIDDEN pip wins. Ties impossible (each follower hides a distinct
    partner of the led symbol). Winner captures all cards, leads next.

GLEAN scoring: at round end, for each of the 9 symbols, whoever captured the
most cards carrying it (either face) scores that symbol's pip (1..9).
Ties for a symbol's majority: nobody scores it (deadlock).

What the sim CANNOT model: whether 9 simultaneous majorities are trackable at
a real table; whether the captures feel meaningful; teaching.
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


# ─── Scoring ──────────────────────────────────────────────────────────────────

def score_round(captured, n):
    """captured: list per player of captured cards. Returns list of scores."""
    # count cards carrying each symbol, per player
    sym_counts = [Counter() for _ in range(n)]
    for pid in range(n):
        for card in captured[pid]:
            sym_counts[pid][card[0]] += 1
            sym_counts[pid][card[1]] += 1
    scores = [0] * n
    for s in SYMBOLS:
        counts = [sym_counts[p][s] for p in range(n)]
        best = max(counts)
        leaders = [p for p in range(n) if counts[p] == best]
        if len(leaders) == 1 and best > 0:
            scores[leaders[0]] += s
        # tie or nobody → deadlock, no score
    return scores


# ─── Bots ─────────────────────────────────────────────────────────────────────

def random_lead(hand, rng, captured, pid, n):
    card = rng.choice(hand)
    return card, rng.choice(card)


def random_follow(hand, led, trick, rng, captured, pid, n):
    followers = [c for c in hand if led in c]
    if followers:
        return rng.choice(followers), led
    card = rng.choice(hand)
    return card, rng.choice(card)


def _want_weight(s, captured, pid, n):
    """How much I still want symbol s (its pip if the majority is live & winnable
    for me, else 0)."""
    counts = [sum(1 for c in captured[p] if s in c) for p in range(n)]
    mine = counts[pid]
    best_other = max((counts[p] for p in range(n) if p != pid), default=0)
    remaining = 8 - sum(counts)
    if mine - best_other > remaining:
        return 0          # already clinched — no need to fight
    if mine + remaining < best_other:
        return 0          # can't catch the leader
    return s              # contested and winnable → worth its pip


def _trick_value(trick_cards, candidate, led, captured, pid, n):
    """Value to me of winning a trick containing trick_cards + my candidate."""
    cards = list(trick_cards) + [candidate]
    val = 0
    for c in cards:
        val += _want_weight(c[0], captured, pid, n)
        val += _want_weight(c[1], captured, pid, n)
    return val


CONTEST_THRESHOLD = 7  # min trick-value worth spending a winning card on


def skilled_lead(hand, rng, captured, pid, n):
    """Lead the symbol you hold most of (funnel it to your pile) with a strong
    (high-hidden) card so you tend to win your own lead."""
    sym_count = Counter(s for c in hand for s in c)
    # restrict to symbols still worth winning
    weighted = {s: sym_count[s] * (1 + 0.1 * _want_weight(s, captured, pid, n))
                for s in sym_count}
    best_sym = max(weighted, key=lambda s: (weighted[s], s))
    options = [c for c in hand if best_sym in c]
    card = max(options, key=lambda c: other(c, best_sym))
    return card, best_sym


def skilled_follow(hand, led, trick, rng, captured, pid, n):
    """Win tricks worth winning (cheaply); duck the rest to save strong cards."""
    followers = [c for c in hand if led in c]
    if not followers:
        # slough the least useful card (lowest combined want)
        card = min(hand, key=lambda c: _want_weight(c[0], captured, pid, n)
                   + _want_weight(c[1], captured, pid, n) + (c[0] + c[1]) * 0.01)
        return card, min(card)
    cur = max([h for (_, _, _, h, f) in trick if f], default=0)
    trick_cards = [c for (_, c, _, _, _) in trick]
    win_opts = [c for c in followers if other(c, led) > cur]
    if win_opts:
        # value if I win with the cheapest sufficient card
        cheap = min(win_opts, key=lambda c: other(c, led))
        val = _trick_value(trick_cards, cheap, led, captured, pid, n)
        if val >= CONTEST_THRESHOLD:
            return cheap, led
    # duck: lowest hidden follower
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
    leader = 0
    n_tricks = 36 // n
    for _ in range(n_tricks):
        trick = []  # (pid, card, shown, hidden, is_follower)
        led = None
        for i in range(n):
            pid = (leader + i) % n
            lead_fn, follow_fn = bots[pid]
            if i == 0:
                card, shown = lead_fn(hands[pid], rng, captured, pid, n)
                led = shown
            else:
                card, shown = follow_fn(hands[pid], led, trick, rng, captured, pid, n)
            hands[pid].remove(card)
            hid = other(card, shown)
            trick.append((pid, card, shown, hid, shown == led))
        followers = [(pid, hid) for (pid, _, _, hid, f) in trick if f]
        winner = max(followers, key=lambda x: x[1])[0]
        for (_, card, _, _, _) in trick:
            captured[winner].append(card)
        leader = winner
    scores = score_round(captured, n)
    return scores, captured


def pct(x):
    return f"{100*x:.1f}%"


def experiment(n_games=4000, seed=42):
    rng = random.Random(seed)
    print("=" * 78)
    print("GLEAN SIMULATION — accumulation trick-taker")
    print(f"{n_games} rounds per configuration · seed {seed}")
    print("=" * 78)

    for n in (3, 4, 6):
        print(f"\n{'─' * 78}")
        print(f"  {n} PLAYERS · {HAND_SIZE[n]} cards each · {36 // n} tricks")
        print(f"{'─' * 78}")

        # All-skilled: score distribution, seat fairness, ties
        seat_wins = Counter()
        score_spread = []
        ties = 0
        all_scores = []
        for _ in range(n_games):
            bots = [(skilled_lead, skilled_follow)] * n
            scores, _ = run_round(n, bots, rng)
            best = max(scores)
            winners = [i for i in range(n) if scores[i] == best]
            if len(winners) > 1:
                ties += 1
            for w in winners:
                seat_wins[w] += 1 / len(winners)
            score_spread.append(max(scores) - min(scores))
            all_scores.extend(scores)
        print(f"\n  [All-skilled mirror]")
        print(f"  Avg winning score margin (max−min): {sum(score_spread)/len(score_spread):.1f}")
        print(f"  Avg player score: {sum(all_scores)/len(all_scores):.1f} "
              f"(of 45 max possible)")
        print(f"  Tie rate: {pct(ties / n_games)}")
        seats = " ".join(f"seat{i}:{pct(seat_wins[i]/n_games)}" for i in range(n))
        print(f"  Seat win shares: {seats}")

        # Skill gap: 1 skilled vs (n-1) random, seat randomised
        sk_wins = 0
        done = 0
        for _ in range(n_games):
            seat = rng.randrange(n)
            bots = [(random_lead, random_follow)] * n
            bots[seat] = (skilled_lead, skilled_follow)
            scores, _ = run_round(n, bots, rng)
            best = max(scores)
            winners = [i for i in range(n) if scores[i] == best]
            done += 1
            if seat in winners:
                sk_wins += 1 / len(winners)
        base = 1.0 / n
        wr = sk_wins / done
        print(f"\n  [Skill gap: 1 skilled vs {n-1} random, seat randomised]")
        print(f"  Skilled win rate: {pct(wr)} (baseline {pct(base)}, "
              f"edge {wr/base:.2f}x)")

        # Degeneration check: does the player dealt the most high-hidden
        # potential just win? Correlate "hand strength" with score under
        # all-RANDOM play (isolates the engine from bot skill).
        strong_seat_wins = 0
        done2 = 0
        for _ in range(n_games):
            deck = DECK[:]
            rng.shuffle(deck)
            hh = HAND_SIZE[n]
            hands = [deck[i*hh:(i+1)*hh] for i in range(n)]
            # "strength" = sum of the higher pip of each card (best hidden you
            # could expose) — a proxy for raw winning power
            strength = [sum(max(c) for c in hands[i]) for i in range(n)]
            strong = max(range(n), key=lambda i: strength[i])
            # replay these exact hands under all-random
            captured = [[] for _ in range(n)]
            leader = 0
            for _t in range(36 // n):
                trick = []
                led = None
                for i in range(n):
                    pid = (leader + i) % n
                    if i == 0:
                        card, shown = random_lead(hands[pid], rng, captured, pid, n)
                        led = shown
                    else:
                        card, shown = random_follow(hands[pid], led, trick, rng, captured, pid, n)
                    hands[pid].remove(card)
                    hid = other(card, shown)
                    trick.append((pid, card, shown, hid, shown == led))
                followers = [(pid, hid) for (pid, _, _, hid, f) in trick if f]
                winner = max(followers, key=lambda x: x[1])[0]
                for (_, card, _, _, _) in trick:
                    captured[winner].append(card)
                leader = winner
            scores = score_round(captured, n)
            best = max(scores)
            winners = [i for i in range(n) if scores[i] == best]
            done2 += 1
            if strong in winners:
                strong_seat_wins += 1 / len(winners)
        deg = strong_seat_wins / done2
        print(f"\n  [Degeneration check — all RANDOM play]")
        print(f"  'Strongest hand' wins: {pct(deg)} (baseline {pct(base)}). "
              f"High = engine rewards the deal, not decisions.")


if __name__ == "__main__":
    experiment()
