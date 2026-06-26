"""WILDFIRE simulation — answers the v1.0 open design questions.

Questions from the rulebook:
  1. Chain limit: 2 (current) vs 3?
  2. Refusal cost: 2 (current) vs 3 (Hot Well)?
  3. Does 6P need Hot Well by default?

Also measured: game length, seat advantage, skill gap (skilled vs random),
refusal frequency, stall risk.

Deck model: 36 cards = all pairs from 9 symbols. A card is a frozenset-like
tuple (a, b). The pile is a stack of (shown_then_turned) cards whose BOTH
faces are public history. The well is face-up (top card public; we let bots
see only the top, per the rulebook).
"""

import random
import itertools
from collections import Counter

SYMBOLS = list(range(1, 10))
DECK = [tuple(sorted(p)) for p in itertools.combinations(SYMBOLS, 2)]
HAND_SIZE = {3: 9, 4: 7, 5: 6, 6: 5}
TURN_CAP = 600  # individual turns before declaring a stall


class GameState:
    __slots__ = ("hands", "well", "pile", "target", "n", "turns", "plays",
                 "refusals", "chains_used")

    def __init__(self, n, rng):
        deck = DECK[:]
        rng.shuffle(deck)
        h = HAND_SIZE[n]
        self.n = n
        self.hands = [deck[i * h:(i + 1) * h] for i in range(n)]
        rest = deck[n * h:]
        first = rest[0]
        self.target = rng.choice(first)  # flip one card to the middle
        self.pile = [first]
        self.well = rest[1:]
        self.turns = 0
        self.plays = 0
        self.refusals = 0
        self.chains_used = 0

    def playable(self, pid):
        t = self.target
        return [c for c in self.hands[pid] if t in c]

    def play(self, pid, card):
        self.hands[pid].remove(card)
        self.pile.append(card)
        self.target = card[0] if card[1] == self.target else card[1]
        self.plays += 1

    def refuse(self, pid, cost):
        self.refusals += 1
        for _ in range(cost):
            if self.well:
                self.hands[pid].append(self.well.pop())
            elif len(self.pile) > 1:
                # take from beneath the pile's top card; target unchanged
                self.hands[pid].append(self.pile.pop(0))
            # else: nothing to take (degenerate, extremely rare)


def exit_symbol(card, target):
    return card[0] if card[1] == target else card[1]


def random_choose(state, pid, chain_limit, rng, chain_p=0.5):
    """Random bot: random playable card; chains with prob chain_p."""
    seq = []
    for i in range(chain_limit):
        opts = state.playable(pid)
        if not opts:
            break
        if i > 0 and rng.random() > chain_p:
            break
        card = rng.choice(opts)
        seq.append(card)
        # simulate forward locally
        state.play(pid, card)
    return len(seq)


def skilled_choose(state, pid, chain_limit, rng):
    """Skilled bot: leaves exit symbols the table is poor in, protects pairs,
    chains when it doesn't strand the hand."""
    played = 0
    for i in range(chain_limit):
        opts = state.playable(pid)
        if not opts:
            break
        hand = state.hands[pid]
        if i > 0:
            # chain only if it doesn't leave a fragmented hand (no shared
            # symbols among remaining cards) while hand is still big
            if len(hand) > 3:
                def frag_after(card):
                    rem = [c for c in hand if c is not card]
                    syms = Counter(s for c in rem for s in c)
                    return not any(v >= 2 for v in syms.values())
                opts2 = [c for c in opts if not frag_after(c)]
                if not opts2:
                    break
                opts = opts2
        # public accounting of each exit symbol: pile history (both faces
        # public) + own hand + well top
        acct = Counter()
        for c in state.pile:
            acct[c[0]] += 1
            acct[c[1]] += 1
        for c in hand:
            acct[c[0]] += 1
            acct[c[1]] += 1
        if state.well:
            top = state.well[-1]
            acct[top[0]] += 1
            acct[top[1]] += 1

        def score(card):
            e = exit_symbol(card, state.target)
            s = acct[e]  # more accounted-for = harder for others = better
            # protect doubles: penalise spending one half of my only pair
            rem = [c for c in hand if c is not card]
            syms = Counter(x for c in rem for x in c)
            pair_bonus = 0.5 if any(v >= 2 for v in syms.values()) else 0.0
            return s + pair_bonus + rng.random() * 0.01

        card = max(opts, key=score)
        state.play(pid, card)
        played += 1
    return played


def run_game(n, chain_limit, refusal_cost, bots, rng):
    """bots: list of n functions. Returns (winner, state) or (None, state) on stall."""
    state = GameState(n, rng)
    pid = 0
    while state.turns < TURN_CAP:
        state.turns += 1
        played = bots[pid](state, pid, chain_limit, rng)
        if played == 0:
            state.refuse(pid, refusal_cost)
        else:
            if played > 1:
                state.chains_used += 1
            if not state.hands[pid]:
                return pid, state
        pid = (pid + 1) % n
    return None, state


def pct(x):
    return f"{100*x:.1f}%"


def experiment(n_games=4000, seed=42):
    rng = random.Random(seed)
    print("=" * 78)
    print("WILDFIRE SIMULATION")
    print(f"{n_games} games per configuration · seed {seed}")
    print("=" * 78)

    configs = [(cl, rc) for cl in (1, 2, 3) for rc in (2, 3)]

    for n in (3, 4, 5, 6):
        print(f"\n--- {n} PLAYERS (hand {HAND_SIZE[n]}) " + "-" * 40)
        print(f"{'chain':>5} {'refuse':>6} | {'avg turns/p':>11} {'stalls':>7} "
              f"{'refus/game':>10} {'chain%turn':>10} {'seat1 win':>9} "
              f"{'lastseat':>8}")
        for cl, rc in configs:
            wins = Counter()
            turns = []
            stalls = 0
            refus = []
            chains = []
            for _ in range(n_games):
                bots = [skilled_choose] * n
                w, st = run_game(n, cl, rc, bots, rng)
                if w is None:
                    stalls += 1
                else:
                    wins[w] += 1
                    turns.append(st.turns / n)
                    refus.append(st.refusals)
                    chains.append(st.chains_used / max(st.turns, 1))
            done = n_games - stalls
            print(f"{cl:>5} {rc:>6} | {sum(turns)/max(len(turns),1):>11.1f} "
                  f"{stalls:>7} {sum(refus)/max(done,1):>10.1f} "
                  f"{pct(sum(chains)/max(done,1)):>10} "
                  f"{pct(wins[0]/max(done,1)):>9} "
                  f"{pct(wins[n-1]/max(done,1)):>8}")

    # ---- skill gap: 1 skilled vs (n-1) random, skilled seat randomised ----
    print("\n--- SKILL GAP: one skilled bot vs random bots (seat randomised) ---")
    print(f"{'players':>7} {'chain':>5} {'refuse':>6} | {'skilled win':>11} "
          f"{'baseline':>8} {'edge':>6}")
    for n in (3, 4, 5, 6):
        for cl, rc in ((2, 2), (3, 2), (2, 3)):
            sw = 0
            done = 0
            for _ in range(n_games):
                seat = rng.randrange(n)
                bots = [random_choose] * n
                bots[seat] = skilled_choose
                w, st = run_game(n, cl, rc, bots, rng)
                if w is not None:
                    done += 1
                    if w == seat:
                        sw += 1
            base = 1 / n
            print(f"{n:>7} {cl:>5} {rc:>6} | {pct(sw/max(done,1)):>11} "
                  f"{pct(base):>8} {sw/max(done,1)/base:>5.2f}x")

    # ---- game length in minutes (rough: 8 seconds per turn) ----
    print("\n--- ESTIMATED REAL-TIME LENGTH (8s/turn incl. refusals) ---")
    for n in (3, 4, 5, 6):
        for cl, rc in ((2, 2), (2, 3)):
            tl = []
            for _ in range(1000):
                w, st = run_game(n, cl, rc, [skilled_choose] * n, rng)
                if w is not None:
                    tl.append(st.turns * 8 / 60)
            print(f"  {n}P chain {cl} refuse {rc}: "
                  f"{sum(tl)/len(tl):.1f} min avg, "
                  f"p90 {sorted(tl)[int(0.9*len(tl))]:.1f} min")


if __name__ == "__main__":
    experiment()
