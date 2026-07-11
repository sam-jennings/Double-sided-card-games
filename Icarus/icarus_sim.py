"""ICARUS simulator — push-your-luck on the all-pairs flip deck.

Ruleset modelled (v0.1, as shipped in ICARUS_rulebook.md):
- 9 signs (ranks 1..9), 36 cards = every unordered pair once (K9 edges).
- Shuffle randomises which face is up (C1). Deck split into equal personal
  towers: 18/12/9 cards at 2/3/4 players. Tower tops always public.
- Flight: draw own tower top (visible sign X public), reveal hidden sign Y.
  FALL if Y is among the face-up (revealed) signs of the flight row.
  Otherwise the card joins the row, Y face-up. Then rise or land.
- Land: bank the row; score = sum of revealed ranks, DOUBLED if the flight
  has >= SOAR_AT (4) cards. TOLL: burn the new tower top to the public
  Fallen field. Tower emptied mid-flight => auto-land, no toll.
- Fall: whole row to the Fallen field (fully public), no toll.
- Game ends when all towers are empty. Highest banked total wins.

Information model:
- Fully public: Fallen cards, banked cards, cards in any current row.
- Semi-public: every tower's top face.
- Counting bots condition on fully-public cards only (uniform over the
  rest) — a table-realistic counter, not a Bayesian oracle over tower tops.

What the sim cannot model: table feel, downtime, the social layer of
watching opponents count, and human (non-myopic) reach-for-the-soar lines.

Assertions every game: card conservation (36) and termination (turn guard).

Headline results (seeds in __main__, ~50k games total):
- Toll load-bearing: without it, bank-every-card beats a counting player
  80/20 (degenerate); with it, 10/90.
- Soar (x2 at 4+) load-bearing: lifts skilled-vs-random score ratio from
  ~1.25x to ~1.5-1.6x (house health bar) and makes flight lengths bimodal
  (land at 2 / reach for 4).
- Counting layer alone (vs naive odds, matched policy): ~1.07x score,
  55-60% h2h at 2P — myopic-bot floor; deeper human lines untested.
"""

import random
import itertools
from collections import defaultdict

SIGNS = list(range(1, 10))  # rank == sign index (Moon=1 .. Crown=9)
ALL_CARDS = [frozenset(p) for p in itertools.combinations(SIGNS, 2)]
assert len(ALL_CARDS) == 36

SOAR_AT = 4      # flights of this many cards or more bank double
SOAR_MULT = 2


class Card:
    __slots__ = ("pair", "up")

    def __init__(self, pair, up):
        self.pair = pair          # frozenset {a, b}
        self.up = up              # sign currently face-up

    @property
    def down(self):
        (a, b) = tuple(self.pair)
        return b if self.up == a else a


def fresh_towers(n_players, rng):
    deck = [Card(p, rng.choice(tuple(p))) for p in ALL_CARDS]
    rng.shuffle(deck)
    size = 36 // n_players
    return [deck[i * size:(i + 1) * size] for i in range(n_players)]


class State:
    def __init__(self, n_players, rng, toll=True, soar=True):
        self.towers = fresh_towers(n_players, rng)
        self.fallen = []              # fully public cards
        self.banked = [[] for _ in range(n_players)]
        self.scores = [0] * n_players
        self.toll = toll
        self.soar = soar

    def public_pairs(self, extra_rows=()):
        pubs = {c.pair for c in self.fallen}
        for pile in self.banked:
            pubs.update(c.pair for c in pile)
        for row in extra_rows:
            pubs.update(c.pair for c in row)
        return pubs

    def conservation(self):
        n = sum(len(t) for t in self.towers) + len(self.fallen)
        n += sum(len(b) for b in self.banked)
        assert n == 36, f"card conservation broken: {n}"


# ---------------- bots ----------------

class Bot:
    name = "bot"

    def press(self, state, pid, row):
        raise NotImplementedError


class RandomBot(Bot):
    """Mechanics floor: presses 50/50."""
    name = "random"

    def __init__(self, rng):
        self.rng = rng

    def press(self, state, pid, row):
        return self.rng.random() < 0.5


class BankOneBot(Bot):
    """Degeneracy probe: lands after every first card."""
    name = "bank1"

    def press(self, state, pid, row):
        return False


class EVBot(Bot):
    """Myopic one-step EV, soar-aware. counting=True uses the public
    registry to compute the exact candidate set for the hidden face;
    counting=False uses naive odds (all 8 partners possible)."""

    def __init__(self, counting):
        self.counting = counting
        self.name = "counting" if counting else "naive"

    def press(self, state, pid, row):
        tower = state.towers[pid]
        if not tower:
            return False
        x = tower[-1].up
        if self.counting:
            pubs = state.public_pairs(extra_rows=[row])
            cand = [z for z in SIGNS
                    if z != x and frozenset((x, z)) not in pubs]
        else:
            cand = [z for z in SIGNS if z != x]
        if not cand:
            return False
        pset = {c.up for c in row}
        poison = [z for z in cand if z in pset]
        safe = [z for z in cand if z not in pset]
        p = len(poison) / len(cand)
        k, stake = len(row), sum(c.up for c in row)
        gain = (sum(safe) / len(safe)) if safe else 0.0
        if state.soar:
            now = stake * (SOAR_MULT if k >= SOAR_AT else 1)
            nxt = (stake + gain) * (SOAR_MULT if k + 1 >= SOAR_AT else 1)
        else:
            now, nxt = stake, stake + gain
        return (1 - p) * nxt - now > 0


class ThresholdBot(Bot):
    """Press iff bust probability < theta (counting or naive odds)."""

    def __init__(self, theta, counting):
        self.theta = theta
        self.counting = counting
        self.name = f"{'cnt' if counting else 'nai'}-th{theta}"

    def press(self, state, pid, row):
        tower = state.towers[pid]
        if not tower:
            return False
        x = tower[-1].up
        if self.counting:
            pubs = state.public_pairs(extra_rows=[row])
            cand = [z for z in SIGNS
                    if z != x and frozenset((x, z)) not in pubs]
        else:
            cand = [z for z in SIGNS if z != x]
        if not cand:
            return False
        pset = {c.up for c in row}
        p = len([z for z in cand if z in pset]) / len(cand)
        return p < self.theta


# ---------------- game loop ----------------

def play_flight(state, pid, bot, stats):
    tower = state.towers[pid]
    row = []
    while True:
        card = tower.pop()          # top of tower; card.up was public
        card.up = card.down         # flip: reveal hidden face
        if card.up in {c.up for c in row}:
            state.fallen.extend(row)
            state.fallen.append(card)
            stats["busts"] += 1
            stats["flights"] += 1
            stats["flight_len"].append(len(row) + 1)
            return
        row.append(card)
        if not tower:
            break                   # auto-land, no toll
        if not bot.press(state, pid, row):
            if state.toll and tower:
                state.fallen.append(tower.pop())
            break
    v = sum(c.up for c in row)
    if state.soar and len(row) >= SOAR_AT:
        v *= SOAR_MULT
        stats["soars"] += 1
    state.scores[pid] += v
    state.banked[pid].extend(row)
    stats["flights"] += 1
    stats["flight_len"].append(len(row))


def play_game(bots, rng, toll=True, soar=True):
    n = len(bots)
    state = State(n, rng, toll=toll, soar=soar)
    stats = defaultdict(int)
    stats["flight_len"] = []
    guard = 0
    while any(state.towers):
        for pid in range(n):
            if state.towers[pid]:
                play_flight(state, pid, bots[pid], stats)
                state.conservation()
            guard += 1
            assert guard < 600, "termination guard tripped"
    return state.scores, stats


def h2h(bot_a, bot_b, n_players, games, rng, toll=True, soar=True, label=""):
    """bot_a vs (n-1) copies of bot_b; seats rotated each game."""
    wins = [0, 0, 0]
    tot = [0.0, 0.0]
    flen, busts, flights = [], 0, 0
    for g in range(games):
        seats = [bot_a] + [bot_b] * (n_players - 1)
        rot = g % n_players
        seats = seats[-rot:] + seats[:-rot]
        a_seat = seats.index(bot_a)
        scores, st = play_game(seats, rng, toll=toll, soar=soar)
        a = scores[a_seat]
        best_b = max(s for i, s in enumerate(scores) if i != a_seat)
        wins[0 if a > best_b else (1 if a < best_b else 2)] += 1
        tot[0] += a
        tot[1] += sum(s for i, s in enumerate(scores)
                      if i != a_seat) / (n_players - 1)
        flen += st["flight_len"]
        busts += st["busts"]
        flights += st["flights"]
    print(f"{label:36s} {bot_a.name:>9s} vs {bot_b.name:<9s} "
          f"winA {wins[0]/games:5.1%}  tie {wins[2]/games:4.1%}  "
          f"avgA {tot[0]/games:6.1f}  avgB {tot[1]/games:6.1f}  "
          f"ratio {tot[0]/max(tot[1], 1e-9):4.2f}  "
          f"fall {busts/max(flights,1):5.1%}  len {sum(flen)/len(flen):4.2f}")


def mirror(make_bot, n_players, games, rng, toll=True, soar=True, label=""):
    """All seats the same bot: score levels, flight shape, seat spread."""
    seat_tot = [0.0] * n_players
    flen, busts, flights, soars = [], 0, 0, 0
    lens = defaultdict(int)
    for _ in range(games):
        bots = [make_bot() for _ in range(n_players)]
        scores, st = play_game(bots, rng, toll=toll, soar=soar)
        for i, s in enumerate(scores):
            seat_tot[i] += s
        flen += st["flight_len"]
        busts += st["busts"]
        flights += st["flights"]
        soars += st["soars"]
        for L in st["flight_len"]:
            lens[L] += 1
    avg = [t / games for t in seat_tot]
    dist = " ".join(f"{k}:{v/sum(lens.values()):.0%}"
                    for k, v in sorted(lens.items()))
    print(f"{label:36s} seats {['%.1f' % a for a in avg]}  "
          f"fall {busts/flights:5.1%}  soar/g {soars/games:4.2f}  "
          f"len {sum(flen)/len(flen):4.2f}  dist {dist}")


if __name__ == "__main__":
    rng = random.Random(42)
    G = 3000

    print("== degeneracy: bank-every-card vs counting, toll off/on ==")
    for np_ in (2, 3):
        h2h(BankOneBot(), EVBot(True), np_, G, rng, toll=False,
            label=f"toll OFF {np_}P")
        h2h(BankOneBot(), EVBot(True), np_, G, rng, toll=True,
            label=f"toll ON  {np_}P")

    print("\n== headline skill gap (toll+soar, shipped config) ==")
    for np_ in (2, 3, 4):
        h2h(EVBot(True), RandomBot(rng), np_, G, rng, label=f"{np_}P")
    for np_ in (2, 3, 4):
        h2h(EVBot(True), EVBot(False), np_, G, rng,
            label=f"{np_}P counting layer")

    print("\n== soar off (why the rule exists) ==")
    h2h(EVBot(True), RandomBot(rng), 2, G, rng, soar=False,
        label="2P no-soar")

    print("\n== mirror games: levels, curve, seat spread ==")
    for np_ in (2, 3, 4):
        mirror(lambda: EVBot(True), np_, 2000, rng,
               label=f"{np_}P counting mirror")
