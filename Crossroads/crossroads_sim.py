"""CROSSROADS simulation — answers the v1.0 open design questions.

Questions from the rulebook:
  1. Pass timing — does the endgame drag?
  2. Does ko suffice against flip-loops?
  3. First-player advantage — is a komi needed?

Model: cities = symbols 1..8 (the 8 symbol-9 cards form the ring and play no
further part). Roads = the 28 cards pairing symbols 1..8. Hands of 14,
perfect information. Turn = build (choose facing) / flip any built road
(ko: not the road the opponent just flipped) / pass. Two consecutive passes
end the game. A kept card is a contract: fulfilled if a directed route
exists between its cities in either direction.
"""

import random
import itertools
from collections import Counter

CITIES = list(range(1, 9))
ROADS = [tuple(sorted(p)) for p in itertools.combinations(CITIES, 2)]
TURN_CAP = 400


def pip_total(hand):
    return sum(a + b for a, b in hand)


def closure(edges):
    """edges: dict road -> pointed city. Returns set of (u,v) reachable pairs."""
    adj = {c: [] for c in CITIES}
    for (a, b), to in edges.items():
        frm = a if to == b else b
        adj[frm].append(to)
    reach = set()
    for s in CITIES:
        seen = {s}
        stack = [s]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        for v in seen:
            if v != s:
                reach.add((s, v))
    return reach


def undirected_components(edges):
    parent = {c: c for c in CITIES}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (a, b) in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return find


def fulfilled(hand, reach):
    return sum(1 for (a, b) in hand if (a, b) in reach or (b, a) in reach)


def potential(hand, reach, find):
    """Heuristic value of a hand of contracts given current network."""
    v = 0.0
    for (a, b) in hand:
        if (a, b) in reach or (b, a) in reach:
            v += 1.0
        elif find(a) == find(b):
            v += 0.45  # connected ignoring direction: one flip-war away
    return v


class State:
    __slots__ = ("hands", "edges", "ko", "passes", "turns",
                 "builds", "flips", "pass_count", "flips_left", "shared")

    def __init__(self, rng, flip_budget=None):
        deck = ROADS[:]
        rng.shuffle(deck)
        self.hands = [deck[:14], deck[14:]]
        self.edges = {}     # road -> pointed city
        self.ko = None      # road the opponent flipped last turn
        self.passes = 0
        self.turns = 0
        self.builds = [0, 0]
        self.flips = [0, 0]
        self.pass_count = [0, 0]
        self.shared = None
        if flip_budget is None:
            self.flips_left = [float("inf")] * 2
        elif isinstance(flip_budget, str) and flip_budget.startswith("shared:"):
            self.shared = int(flip_budget.split(":")[1])
            self.flips_left = [float("inf")] * 2
        elif isinstance(flip_budget, tuple):
            self.flips_left = list(flip_budget)  # indexed by player id
        else:
            self.flips_left = [flip_budget] * 2

    def first_player(self):
        p0, p1 = pip_total(self.hands[0]), pip_total(self.hands[1])
        if p0 == p1:
            return 0
        return 0 if p0 < p1 else 1


def legal_actions(st, me):
    acts = [("pass", None, None)]
    for card in st.hands[me]:
        acts.append(("build", card, card[0]))
        acts.append(("build", card, card[1]))
    can_flip = st.flips_left[me] > 0 and (st.shared is None or st.shared > 0)
    if can_flip:
        for road in st.edges:
            if road != st.ko:
                acts.append(("flip", road, None))
    return acts


def apply(st, me, act):
    kind, x, y = act
    new_ko = None
    if kind == "pass":
        st.passes += 1
        st.pass_count[me] += 1
    elif kind == "build":
        st.hands[me].remove(x)
        st.edges[x] = y
        st.passes = 0
        st.builds[me] += 1
    else:
        road = x
        cur = st.edges[road]
        st.edges[road] = road[0] if cur == road[1] else road[1]
        st.passes = 0
        st.flips[me] += 1
        st.flips_left[me] -= 1
        if st.shared is not None:
            st.shared -= 1
        new_ko = road
    st.ko = new_ko
    st.turns += 1


def evaluate(st, me):
    reach = closure(st.edges)
    find = undirected_components(st.edges)
    return potential(st.hands[me], reach, find) - \
        potential(st.hands[1 - me], reach, find)


def greedy_bot(st, me, rng):
    """1-ply greedy with potential heuristic. Passes when nothing improves."""
    base = evaluate(st, me)
    best, best_v = ("pass", None, None), base + 1e-9
    for act in legal_actions(st, me):
        if act[0] == "pass":
            continue
        # try action on a cheap copy
        edges = dict(st.edges)
        hands = [list(st.hands[0]), list(st.hands[1])]
        if act[0] == "build":
            hands[me].remove(act[1])
            edges[act[1]] = act[2]
        else:
            road = act[1]
            cur = edges[road]
            edges[road] = road[0] if cur == road[1] else road[1]
        reach = closure(edges)
        find = undirected_components(edges)
        v = potential(hands[me], reach, find) - \
            potential(hands[1 - me], reach, find) + rng.random() * 1e-4
        if v > best_v:
            best, best_v = act, v
    return best


def random_bot(st, me, rng):
    acts = legal_actions(st, me)
    nonpass = [a for a in acts if a[0] != "pass"]
    if nonpass and rng.random() > 0.05:
        return rng.choice(nonpass)
    return ("pass", None, None)


def run_game(bot0, bot1, rng, force_first=None, flip_budget=None):
    st = State(rng, flip_budget)
    first = st.first_player() if force_first is None else force_first
    bots = {first: bot0, 1 - first: bot1} if force_first is not None else \
        {0: bot0, 1: bot1}
    me = first
    while st.passes < 2 and st.turns < TURN_CAP:
        act = bots[me](st, me, rng)
        apply(st, me, act)
        me = 1 - me
    reach = closure(st.edges)
    f0 = fulfilled(st.hands[0], reach)
    f1 = fulfilled(st.hands[1], reach)
    if f0 != f1:
        winner = 0 if f0 > f1 else 1
    else:
        p0 = sum(a + b for (a, b) in st.hands[0]
                 if (a, b) in reach or (b, a) in reach)
        p1 = sum(a + b for (a, b) in st.hands[1]
                 if (a, b) in reach or (b, a) in reach)
        winner = 0 if p0 > p1 else (1 if p1 > p0 else None)
    return winner, first, f0, f1, st


def pct(x):
    return f"{100*x:.1f}%"


def mirror_stats(n_games, rng, flip_budget, label):
    fw = sw = draws = caps = dec = 0
    turns, f_sum, builds, flips, kept = [], [], [], [], []
    for _ in range(n_games):
        w, first, f0, f1, st = run_game(greedy_bot, greedy_bot, rng,
                                        force_first=0,
                                        flip_budget=flip_budget)
        if st.turns >= TURN_CAP:
            caps += 1
        if w is None:
            draws += 1
        else:
            dec += 1
            if w == first:
                fw += 1
            else:
                sw += 1
        turns.append(st.turns)
        f_sum.append(f0 + f1)
        builds.append(sum(st.builds))
        flips.append(sum(st.flips))
        kept.append(len(st.hands[0]) + len(st.hands[1]))
    n = n_games
    print(f"\n  flip budget = {label}")
    print(f"    caps {caps} ({pct(caps/n)}) | len {sum(turns)/n:.1f} turns "
          f"(p90 {sorted(turns)[int(0.9*n)]}) | "
          f"builds {sum(builds)/n:.1f} flips {sum(flips)/n:.1f}")
    print(f"    P1 wins {pct(fw/max(dec,1))} of decisive | draws {pct(draws/n)} | "
          f"kept {sum(kept)/n:.1f}/28 | fulfilled {sum(f_sum)/n:.1f}")


def experiment(n_games=400, seed=42, budgets=(None, 8, 6, 4)):
    rng = random.Random(seed)
    print("=" * 74)
    print(f"CROSSROADS SIMULATION · seed {seed}")
    print("=" * 74)

    print("\nGREEDY MIRROR ACROSS FLIP BUDGETS (forced first move)")
    for b in budgets:
        ng = 40 if b is None else n_games  # unlimited games are 400 turns long
        label = "unlimited" if b is None else b
        if isinstance(b, tuple):
            label = f"P1:{b[0]} P2:{b[1]}"
        mirror_stats(ng, rng, b, label)

    # ---- skill gap at the recommended budget ----
    for b in (6,):
        gw = dec = 0
        for i in range(n_games):
            if i % 2 == 0:
                w, first, *_ = run_game(greedy_bot, random_bot, rng,
                                        force_first=0, flip_budget=b)
                gwin = (w == first)
            else:
                w, first, *_ = run_game(random_bot, greedy_bot, rng,
                                        force_first=0, flip_budget=b)
                gwin = (w == 1 - first)
            if w is not None:
                dec += 1
                if gwin:
                    gw += 1
        print(f"\nSKILL GAP (budget {b}): greedy beats random in "
              f"{pct(gw/max(dec,1))} of decisive games")


if __name__ == "__main__":
    experiment()
