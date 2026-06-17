"""OUROBOROS solitaire simulator — final ruleset (v1.0).

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
- random: uniform random legal choice.
- greedy: maximise remaining copies of the new open symbol (one-ply, deck-counting).
- smart : maximise hand health — number of remaining hand cards that can still
  reach either open end (x10) plus deck count of the new open symbol.

Usage: python3 ouroboros_sim.py [games=2000] [seed=42]
"""
import random, sys
from itertools import combinations

def play(n, H, policy, rng):
    deck = [tuple(c) for c in combinations(range(n), 2)]
    rng.shuffle(deck)
    hand = []; left = right = None; placed = 0; scars = 0
    def moves():
        mv = []
        for i, (a, b) in enumerate(hand):
            if placed == 0:
                mv += [(i, b, a, 'R'), (i, a, b, 'R')]
                continue
            if a == right: mv.append((i, b, None, 'R'))
            if b == right: mv.append((i, a, None, 'R'))
            if a == left:  mv.append((i, b, None, 'L'))
            if b == left:  mv.append((i, a, None, 'L'))
        return mv
    while True:
        while deck and len(hand) < H:
            hand.append(deck.pop())
        if not hand:
            break
        mv = moves()
        if not mv:                      # forced scar
            scars += 1
            best = None; bv = -1.0
            for i, (a, b) in enumerate(hand):
                for s in (a, b):
                    hh = sum(1 for j, c in enumerate(hand) if j != i and s in c)
                    dv = sum(1 for c in deck if s in c)
                    v = rng.random() if policy == 'random' else (hh * 10 + dv if policy == 'smart' else hh + dv)
                    if v > bv: bv = v; best = (i, s)
            i, s = best
            hand.pop(i); right = s; placed += 1
            continue
        if policy == 'random':
            i, new, shown, side = rng.choice(mv)
        else:
            def val(m):
                i, new, shown, side = m
                if placed == 0: L, R = shown, new
                elif side == 'R': L, R = left, new
                else: L, R = new, right
                if policy == 'smart':
                    hh = sum(1 for j, c in enumerate(hand) if j != i and (L in c or R in c))
                    return hh * 10 + sum(1 for c in deck if new in c)
                return sum(1 for c in deck if new in c) + sum(1 for j, c in enumerate(hand) if j != i and new in c)
            bv = max(val(m) for m in mv)
            i, new, shown, side = rng.choice([m for m in mv if val(m) == bv])
        hand.pop(i)
        if placed == 0: left, right = shown, new
        elif side == 'R': right = new
        else: left = new
        placed += 1
    if left != right:
        scars += 1                      # the closing scar
    return scars

def batch(n, H, policy, games, seed):
    rng = random.Random(seed)
    return [play(n, H, policy, rng) for _ in range(games)]

if __name__ == '__main__':
    games = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    print(f"games={games} seed={seed}")
    print(f"{'n':>2} {'H':>2} {'policy':>7} {'avg scars':>9} {'0%':>6} {'<=2%':>6} {'<=4%':>6} {'<=6%':>6}")
    for n, H in ((9, 4), (7, 3)):
        for pol in ('random', 'greedy', 'smart'):
            ks = batch(n, H, pol, games, seed)
            pc = lambda t: 100 * sum(1 for k in ks if k <= t) / games
            print(f"{n:>2} {H:>2} {pol:>7} {sum(ks)/games:>9.2f} {pc(0):>5.1f}% {pc(2):>5.1f}% {pc(4):>5.1f}% {pc(6):>5.1f}%")
