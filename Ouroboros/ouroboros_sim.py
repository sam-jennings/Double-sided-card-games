"""OUROBOROS solitaire simulator — ruleset v1.0 + revival skill-ceiling probe.

Rules simulated:
- Deck = all C(n,2) symbol-pair cards (n=9 full game, n=7 short game), shuffled.
- Hand of up to H cards (both sides known to the player), refilled after each play.
- A line of cards is built; reading head-ward, each card's hidden face must equal
  the next card's visible face (the line is a walk on the symbol graph).
  * Extend the head with card {a,b}: visible face = head's open symbol, the other
    symbol becomes the new open symbol. The tail end works symmetrically.
- If NO hand card can extend either end, you must tie a SCAR: place any hand card
  sideways at the head, either face up; its visible symbol is the new open symbol.
- Game always finishes (every card gets placed). When the last card is down, join
  head to tail: if the final symbols don't match, that join is one more scar.
- Score = total scars. 0 = perfect ouroboros.
  (Theorem: exactly 1 scar is impossible — scar joins form an even-degree graph.)

Policies:
- random : uniform random legal choice.
- greedy : maximise remaining copies of the new open symbol (one-ply, deck-counting).
- smart  : maximise hand health — number of remaining hand cards that can still
           reach either open end (x10) plus deck count of the new open symbol.
- mc     : Monte-Carlo planner. For each legal choice, reshuffle the *remaining*
           deck (the player knows which cards remain, not their order) and roll the
           game out under `smart` several times; pick the choice with the fewest
           expected scars. This is the "deeper bot" the revival re-evaluation calls
           for — it estimates the skill *ceiling* the one-ply bots could only floor.

Usage: python3 ouroboros_sim.py [games=2000] [seed=42] [mc_games=150] [mc_rolls=4]
"""
import random, sys
from itertools import combinations

LEFT, RIGHT = 'L', 'R'  # tail open = left, head open = right


def gen_moves(hand, left, right, placed):
    mv = []
    for i, (a, b) in enumerate(hand):
        if placed == 0:
            mv += [(i, b, a, RIGHT), (i, a, b, RIGHT)]
            continue
        if a == right: mv.append((i, b, None, RIGHT))
        if b == right: mv.append((i, a, None, RIGHT))
        if a == left:  mv.append((i, b, None, LEFT))
        if b == left:  mv.append((i, a, None, LEFT))
    return mv


def apply_move(hand, left, right, placed, m):
    i, new, shown, side = m
    hand = hand[:i] + hand[i + 1:]
    if placed == 0:
        left, right = shown, new
    elif side == RIGHT:
        right = new
    else:
        left = new
    return hand, left, right, placed + 1


def smart_val(m, hand, left, right, placed, deck):
    i, new, shown, side = m
    if placed == 0:
        L, R = shown, new
    elif side == RIGHT:
        L, R = left, new
    else:
        L, R = new, right
    hh = sum(1 for j, c in enumerate(hand) if j != i and (L in c or R in c))
    return hh * 10 + sum(1 for c in deck if new in c)


def greedy_val(m, hand, left, right, placed, deck):
    i, new, shown, side = m
    return sum(1 for c in deck if new in c) + sum(1 for j, c in enumerate(hand) if j != i and new in c)


def run(hand, left, right, placed, scars, deck, H, policy, rng, mc_rolls=0):
    """Play to completion from an arbitrary state; return final total scars."""
    hand = list(hand)
    deck = list(deck)
    while True:
        while deck and len(hand) < H:
            hand.append(deck.pop())
        if not hand:
            break
        mv = gen_moves(hand, left, right, placed)
        if not mv:                                  # forced scar
            scars += 1
            opts = [(i, s) for i, (a, b) in enumerate(hand) for s in (a, b)]
            if policy == 'mc':
                best, bv = None, 1e18
                for (i, s) in opts:
                    nh = hand[:i] + hand[i + 1:]
                    v = sum(run(nh, left, s, placed + 1, scars, _shuffled(deck, rng), H, 'smart', rng)
                            for _ in range(mc_rolls))
                    if v < bv:
                        bv, best = v, (i, s)
                i, s = best
            elif policy == 'random':
                i, s = rng.choice(opts)
            else:
                key = (lambda io: _scar_val(io, hand, deck, policy))
                bv = max(key(io) for io in opts)
                i, s = rng.choice([io for io in opts if key(io) == bv])
            hand.pop(i)
            right = s
            placed += 1
            continue
        if policy == 'mc':
            best, bv = None, 1e18
            for m in mv:
                nh, nl, nr, npl = apply_move(hand, left, right, placed, m)
                v = sum(run(nh, nl, nr, npl, scars, _shuffled(deck, rng), H, 'smart', rng)
                        for _ in range(mc_rolls))
                if v < bv:
                    bv, best = v, m
            m = best
        elif policy == 'random':
            m = rng.choice(mv)
        else:
            val = smart_val if policy == 'smart' else greedy_val
            bv = max(val(m, hand, left, right, placed, deck) for m in mv)
            m = rng.choice([m for m in mv if val(m, hand, left, right, placed, deck) == bv])
        hand, left, right, placed = apply_move(hand, left, right, placed, m)
    if left != right:
        scars += 1                                  # the closing scar
    return scars


def _shuffled(deck, rng):
    d = deck[:]
    rng.shuffle(d)
    return d


def _scar_val(io, hand, deck, policy):
    i, s = io
    hh = sum(1 for j, c in enumerate(hand) if j != i and s in c)
    dv = sum(1 for c in deck if s in c)
    return hh * 10 + dv if policy == 'smart' else hh + dv


def play(n, H, policy, rng, mc_rolls=0):
    deck = [tuple(c) for c in combinations(range(n), 2)]
    rng.shuffle(deck)
    return run([], None, None, 0, 0, deck, H, policy, rng, mc_rolls)


def batch(n, H, policy, games, seed, mc_rolls=0):
    rng = random.Random(seed)
    return [play(n, H, policy, rng, mc_rolls) for _ in range(games)]


def _report(n, H, pol, ks, games):
    pc = lambda t: 100 * sum(1 for k in ks if k <= t) / games
    print(f"{n:>2} {H:>2} {pol:>7} {sum(ks)/games:>9.2f} {pc(0):>5.1f}% {pc(2):>5.1f}% {pc(4):>5.1f}% {pc(6):>5.1f}%")


if __name__ == '__main__':
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    mc_games = int(sys.argv[3]) if len(sys.argv) > 3 else 150
    mc_rolls = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    print(f"games={games} seed={seed} mc_games={mc_games} mc_rolls={mc_rolls}")
    print(f"{'n':>2} {'H':>2} {'policy':>7} {'avg scars':>9} {'0%':>6} {'<=2%':>6} {'<=4%':>6} {'<=6%':>6}")
    for n, H in ((9, 4), (7, 3)):
        for pol in ('random', 'greedy', 'smart'):
            _report(n, H, pol, batch(n, H, pol, games, seed), games)
        _report(n, H, 'mc', batch(n, H, 'mc', mc_games, seed, mc_rolls), mc_games)
