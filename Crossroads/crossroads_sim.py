"""CROSSROADS simulation.

v1.0/v1.1 questions (2P) are answered in CROSSROADS_design_analysis.md. This
file is extended for the **player-count + pass-to-win** investigation
(CROSSROADS_tasks.md, Phase 1):

  - N-player support (2 / 3 / 4). 28 roads deal 14 / 9(+1 seed) / 7 per hand.
  - A PassBot that builds nothing and keeps every card as a contract, to
    reproduce the CRITICAL pass-to-win bug from playtest 02.
  - Two candidate fixes:
      * TOLL  — a fulfilled contract scores +1 per road *you* built on its
                (shortest) route. Punishes the parasite.
      * SPLIT — deal K fixed contracts + (hand-K) buildable roads; kept roads
                do NOT score, so you cannot convert hoarded roads into free
                contracts. Also pre-sorts the hand (handling fix).

Model: cities = symbols 1..8 (the 8 symbol-9 cards form the ring). Roads = the
28 cards pairing 1..8. Turn = build (choose facing) / flip any built road
(ko: not the road just flipped) / pass. The game ends when all N players pass
in succession, or at the turn cap. A scored contract is fulfilled if a directed
route exists between its two cities in either direction.
"""

import random
import itertools

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


def shortest_route(edges, a, b):
    """Shortest directed path of roads from a to b (BFS). Returns list of road
    tuples, or None. Used for Toll scoring."""
    adj = {c: [] for c in CITIES}
    for road, to in edges.items():
        frm = road[0] if to == road[1] else road[1]
        adj[frm].append((to, road))
    prev = {a: (None, None)}
    q = [a]
    while q:
        nq = []
        for u in q:
            for v, road in adj[u]:
                if v not in prev:
                    prev[v] = (u, road)
                    if v == b:
                        path = []
                        cur = b
                        while prev[cur][1] is not None:
                            u2, road2 = prev[cur]
                            path.append(road2)
                            cur = u2
                        return path[::-1]
                    nq.append(v)
        q = nq
    return None


def fulfilled(contracts, reach):
    return sum(1 for (a, b) in contracts if (a, b) in reach or (b, a) in reach)


def potential(contracts, reach, find):
    """Heuristic value of a set of contracts given the current network."""
    v = 0.0
    for (a, b) in contracts:
        if (a, b) in reach or (b, a) in reach:
            v += 1.0
        elif find(a) == find(b):
            v += 0.45  # connected ignoring direction: one flip-war away
    return v


class State:
    __slots__ = ("n", "hands", "fixed", "edges", "builder", "ko", "passes",
                 "turns", "builds", "flips", "pass_count", "flips_left",
                 "shared", "toll", "draw_pile", "hand_cap")

    def __init__(self, rng, n=2, flip_budget=None, split_k=None, toll=False,
                 hand_size=None, draw=False, hand_cap=None):
        deck = ROADS[:]
        rng.shuffle(deck)
        self.n = n
        self.draw_pile = []
        self.hand_cap = hand_cap
        if draw:
            per = hand_size
            self.hands = [deck[i * per:(i + 1) * per] for i in range(n)]
            self.draw_pile = deck[n * per:]   # face-up stack in reality (caveat)
            self.edges = {}
            self.builder = {}
        elif hand_size is None:
            per = 28 // n
            self.hands = [deck[i * per:(i + 1) * per] for i in range(n)]
            self.edges = {}
            self.builder = {}
            # 3P leftover card seeds the board as a neutral public road.
            for seed in deck[n * per:]:
                self.edges[seed] = seed[rng.randint(0, 1)]
                self.builder[seed] = None
        else:
            per = hand_size
            self.hands = [deck[i * per:(i + 1) * per] for i in range(n)]
            self.edges = {}      # remainder deck[n*per:] is set ASIDE, unused
            self.builder = {}
        # SPLIT: carve K fixed contracts off the front of each hand.
        if split_k is not None:
            self.fixed = [self.hands[p][:split_k] for p in range(n)]
            self.hands = [self.hands[p][split_k:] for p in range(n)]
        else:
            self.fixed = [None] * n   # base: contracts = whatever stays in hand
        self.toll = toll
        self.ko = None
        self.passes = 0
        self.turns = 0
        self.builds = [0] * n
        self.flips = [0] * n
        self.pass_count = [0] * n
        self.shared = None
        if flip_budget is None:
            self.flips_left = [float("inf")] * n
        elif isinstance(flip_budget, str) and flip_budget.startswith("shared:"):
            self.shared = int(flip_budget.split(":")[1])
            self.flips_left = [float("inf")] * n
        else:
            self.flips_left = [flip_budget] * n

    def contracts(self, p):
        """The cards that score for player p."""
        return self.fixed[p] if self.fixed[p] is not None else self.hands[p]

    def first_player(self):
        """Pie rule proxy: highest pip total chooses; sim lets that seat move
        first (the sim forces a seat anyway for fairness, this is unused there)."""
        totals = [pip_total(self.hands[p]) for p in range(self.n)]
        return max(range(self.n), key=lambda p: totals[p])


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
        st.builder[x] = me
        st.passes = 0
        st.builds[me] += 1
        # DRAW model: refill the hand toward the cap from the (face-up) pile.
        if st.draw_pile and (st.hand_cap is None or
                             len(st.hands[me]) < st.hand_cap):
            st.hands[me].append(st.draw_pile.pop())
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


def differential(st, me, hands, edges):
    """me's contract potential minus the mean of the other players'."""
    reach = closure(edges)
    find = undirected_components(edges)

    def contracts_of(p):
        return st.fixed[p] if st.fixed[p] is not None else hands[p]

    mine = potential(contracts_of(me), reach, find)
    others = [potential(contracts_of(p), reach, find)
              for p in range(st.n) if p != me]
    return mine - (sum(others) / len(others) if others else 0.0)


def greedy_bot(st, me, rng):
    """1-ply greedy on the (own - mean others) contract-potential differential.
    Passes when nothing strictly improves it."""
    base = differential(st, me, st.hands, st.edges)
    best, best_v = ("pass", None, None), base + 1e-9
    for act in legal_actions(st, me):
        if act[0] == "pass":
            continue
        edges = dict(st.edges)
        hands = [list(h) for h in st.hands]
        if act[0] == "build":
            hands[me].remove(act[1])
            edges[act[1]] = act[2]
        else:
            road = act[1]
            cur = edges[road]
            edges[road] = road[0] if cur == road[1] else road[1]
        v = differential(st, me, hands, edges) + rng.random() * 1e-4
        if v > best_v:
            best, best_v = act, v
    return best


def own_only(st, me, hands, edges):
    """me's contract potential, ignoring everyone else (no denial)."""
    reach = closure(edges)
    find = undirected_components(edges)
    cs = st.fixed[me] if st.fixed[me] is not None else hands[me]
    return potential(cs, reach, find)


def naive_bot(st, me, rng):
    """Builds only to improve its OWN contracts; never denies others. Models the
    non-adversarial table play that produced the pass-to-win bug in playtest 02
    (everyone builds their own routes, the network connects everything)."""
    base = own_only(st, me, st.hands, st.edges)
    best, best_v = ("pass", None, None), base + 1e-9
    for act in legal_actions(st, me):
        if act[0] == "pass":
            continue
        edges = dict(st.edges)
        hands = [list(h) for h in st.hands]
        if act[0] == "build":
            hands[me].remove(act[1])
            edges[act[1]] = act[2]
        else:
            road = act[1]
            cur = edges[road]
            edges[road] = road[0] if cur == road[1] else road[1]
        v = own_only(st, me, hands, edges) + rng.random() * 1e-4
        if v > best_v:
            best, best_v = act, v
    return best


def random_bot(st, me, rng):
    acts = legal_actions(st, me)
    nonpass = [a for a in acts if a[0] != "pass"]
    if nonpass and rng.random() > 0.05:
        return rng.choice(nonpass)
    return ("pass", None, None)


def pass_bot(st, me, rng):
    """Builds nothing, keeps everything — the pass-to-win line."""
    return ("pass", None, None)


def score_player(st, p, reach):
    """(fulfilled_count, toll_bonus, fulfilled_pip_sum) for player p."""
    cs = st.contracts(p)
    f = 0
    toll = 0
    pip = 0
    for (a, b) in cs:
        ok = (a, b) in reach or (b, a) in reach
        if not ok:
            continue
        f += 1
        pip += a + b
        if st.toll:
            route = shortest_route(st.edges, a, b)
            if route is None:
                route = shortest_route(st.edges, b, a)
            if route:
                toll += sum(1 for r in route if st.builder.get(r) == p)
    return f, toll, pip


def run_game(bots, rng, n=2, force_first=0, flip_budget=None,
             split_k=None, toll=False, hand_size=None, draw=False,
             hand_cap=None):
    """bots: list indexed by seat. Returns (winner_seat, scores, state)."""
    st = State(rng, n=n, flip_budget=flip_budget, split_k=split_k, toll=toll,
               hand_size=hand_size, draw=draw, hand_cap=hand_cap)
    me = force_first
    while st.passes < n and st.turns < TURN_CAP:
        act = bots[me](st, me, rng)
        apply(st, me, act)
        me = (me + 1) % n
    reach = closure(st.edges)
    scores = [score_player(st, p, reach) for p in range(n)]
    # winner: max (fulfilled + toll), tiebreak fulfilled-pip-sum.
    def key(p):
        f, toll_b, pip = scores[p]
        return (f + toll_b, pip)
    best = max(key(p) for p in range(n))
    leaders = [p for p in range(n) if key(p) == best]
    winner = leaders[0] if len(leaders) == 1 else None
    return winner, scores, st


def pct(x):
    return f"{100*x:.1f}%"


# --------------------------------------------------------------------------
# Experiments
# --------------------------------------------------------------------------

def regression_2p(n_games, rng):
    """Confirm the original 2P findings still hold after the rewrite."""
    print("\n[REGRESSION] 2P greedy mirror (base, no toll/split)")
    for label, budget in (("unlimited", None), ("shared:8", "shared:8")):
        ng = 40 if budget is None else n_games
        caps = turns = fw = dec = 0
        for _ in range(ng):
            w, scores, st = run_game([greedy_bot, greedy_bot], rng, n=2,
                                     force_first=0, flip_budget=budget)
            if st.turns >= TURN_CAP:
                caps += 1
            turns += st.turns
            if w is not None:
                dec += 1
                if w == 0:
                    fw += 1
        print(f"   {label:>10}: caps {pct(caps/ng)} | len {turns/ng:.1f} | "
              f"P1(first) wins {pct(fw/max(dec,1))} of decisive")


def passbot_test(n_games, rng, n, flip_budget, split_k=None, toll=False,
                 builder=greedy_bot, hand_size=None, draw=False,
                 hand_cap=None, label=""):
    """One seat is the PassBot, the rest are `builder` bots. Rotate the pass
    seat. Report the passer's win rate vs the fair share 1/n."""
    passer_wins = 0
    passer_f = 0.0
    greedy_f = 0.0
    caps = 0
    games = 0
    for g in range(n_games):
        pass_seat = g % n
        bots = [builder] * n
        bots[pass_seat] = pass_bot
        w, scores, st = run_game(bots, rng, n=n, force_first=0,
                                 flip_budget=flip_budget, split_k=split_k,
                                 toll=toll, hand_size=hand_size, draw=draw,
                                 hand_cap=hand_cap)
        games += 1
        if st.turns >= TURN_CAP:
            caps += 1
        if w == pass_seat:
            passer_wins += 1
        pf = scores[pass_seat][0]
        passer_f += pf
        greedy_f += sum(scores[p][0] for p in range(n) if p != pass_seat) / (n - 1)
    fair = 1.0 / n
    flag = "  <-- PASS-TO-WIN" if passer_wins / games > fair * 1.4 else ""
    print(f"   {label:<26} passer wins {pct(passer_wins/games)} "
          f"(fair {pct(fair)}) | passer fulfilled {passer_f/games:.2f} vs "
          f"others {greedy_f/games:.2f} | caps {pct(caps/games)}{flag}")
    return passer_wins / games


def skill_gap(n_games, rng, n, flip_budget, split_k=None, toll=False,
              hand_size=None, draw=False, hand_cap=None, label=""):
    """One greedy vs (n-1) random, rotate the greedy seat. Healthy if the lone
    greedy beats its fair share comfortably."""
    gw = games = 0
    for g in range(n_games):
        gseat = g % n
        bots = [random_bot] * n
        bots[gseat] = greedy_bot
        w, scores, st = run_game(bots, rng, n=n, force_first=0,
                                 flip_budget=flip_budget, split_k=split_k,
                                 toll=toll, hand_size=hand_size, draw=draw,
                                 hand_cap=hand_cap)
        games += 1
        if w == gseat:
            gw += 1
    fair = 1.0 / n
    ratio = (gw / games) / fair
    print(f"   {label:<26} greedy wins {pct(gw/games)} (fair {pct(fair)}) "
          f"= {ratio:.2f}x fair")
    return ratio


def map_connectivity(edges):
    """Fraction of the 28 unordered city-pairs connected (either direction)."""
    reach = closure(edges)
    c = sum(1 for (a, b) in ROADS if (a, b) in reach or (b, a) in reach)
    return c / 28.0


def unified_mirror(n_games, rng, n, hand_size, toll=True, label=""):
    """All-greedy mirror at a fixed hand size. Reports density + satisfaction
    so we can spot 'too sparse' vs 'everything connects (contracts free)'."""
    builds = kept = fulfilled_pp = conn = caps = 0.0
    for _ in range(n_games):
        bots = [greedy_bot] * n
        w, scores, st = run_game(bots, rng, n=n, force_first=0,
                                 flip_budget="shared:8", toll=toll,
                                 hand_size=hand_size)
        if st.turns >= TURN_CAP:
            caps += 1
        builds += sum(st.builds) / n
        kept += sum(len(st.contracts(p)) for p in range(n)) / n
        fulfilled_pp += sum(s[0] for s in scores) / n
        conn += map_connectivity(st.edges)
    g = n_games
    in_play = n * hand_size
    print(f"   {label:<14} H={hand_size} in-play={in_play:>2} | "
          f"builds/p {builds/g:4.1f} | kept/p {kept/g:4.1f} | "
          f"fulfilled/p {fulfilled_pp/g:4.1f} | map-conn {pct(conn/g)} | "
          f"caps {pct(caps/g)}")


def unified_study(n_games=300, seed=42):
    rng = random.Random(seed)
    print("=" * 78)
    print(f"UNIFIED FIXED-HAND-SIZE STUDY · seed {seed} · Toll on, Signal Fires")
    print("  (deal H each, set the rest ASIDE; partial info at every count)")
    print("=" * 78)

    print("\n[DENSITY / SATISFACTION] all-greedy mirror")
    for H in (14, 12, 11, 10, 9, 8):
        unified_mirror(n_games, rng, 2, H, label="2P")
    print()
    for H in (9, 8, 7, 6):
        unified_mirror(n_games, rng, 3, H, label="3P")

    print("\n[SKILL GAP] lone greedy vs random")
    for H in (14, 11, 10, 9, 8):
        skill_gap(n_games, rng, 2, "shared:8", toll=True, hand_size=H,
                  label=f"2P H={H}")
    for H in (9, 8, 7):
        skill_gap(n_games, rng, 3, "shared:8", toll=True, hand_size=H,
                  label=f"3P H={H}")

    print("\n[PASS-TO-WIN vs NAIVE] (Toll on) — confirm the fix survives smaller hands")
    for H in (14, 10, 9):
        passbot_test(n_games, rng, 2, "shared:8", toll=True, builder=naive_bot,
                     hand_size=H, label=f"2P H={H}")
    for H in (9, 8, 7):
        passbot_test(n_games, rng, 3, "shared:8", toll=True, builder=naive_bot,
                     hand_size=H, label=f"3P H={H}")


def experiment(n_games=300, seed=42):
    rng = random.Random(seed)
    print("=" * 74)
    print(f"CROSSROADS SIMULATION · seed {seed} · Phase 1: player count + pass-to-win")
    print("=" * 74)

    regression_2p(n_games, rng)

    print("\n[PASS-TO-WIN] base game, Signal Fires (shared:8), flips live")
    for n in (2, 3, 4):
        passbot_test(n_games, rng, n, "shared:8", label=f"{n}P base vs greedy")

    print("\n[PASS-TO-WIN vs NAIVE builders] (non-adversarial — models the"
          " playtest table)")
    for n in (2, 3, 4):
        passbot_test(n_games, rng, n, "shared:8", builder=naive_bot,
                     label=f"{n}P base vs naive")

    print("\n[FIX 1: TOLL] +1 per own-built road on a fulfilled route")
    for n in (2, 3, 4):
        passbot_test(n_games, rng, n, "shared:8", toll=True,
                     builder=greedy_bot, label=f"{n}P toll vs greedy")
    for n in (2, 3, 4):
        passbot_test(n_games, rng, n, "shared:8", toll=True,
                     builder=naive_bot, label=f"{n}P toll vs NAIVE")

    print("\n[FIX 2: SPLIT] K fixed contracts + (hand-K) buildable roads")
    split_map = {2: (4, 6, 8), 3: (3, 4, 5), 4: (2, 3, 4)}
    for n in (2, 3, 4):
        for k in split_map[n]:
            passbot_test(n_games, rng, n, "shared:8", split_k=k,
                         builder=naive_bot, label=f"{n}P split K={k} vs NAIVE")

    print("\n[SKILL GAP] lone greedy vs random (base / toll / best split)")
    for n in (2, 3, 4):
        skill_gap(n_games, rng, n, "shared:8", label=f"{n}P base")
        skill_gap(n_games, rng, n, "shared:8", toll=True, label=f"{n}P toll")
        k = split_map[n][1]
        skill_gap(n_games, rng, n, "shared:8", split_k=k,
                  label=f"{n}P split K={k}")


def draw_mirror(n_games, rng, n, hand_size, hand_cap, label=""):
    """All-greedy mirror in the DRAW model. Reports density, length, and how
    many of the 28 roads get built (deck churn)."""
    builds = kept = fulfilled_pp = conn = caps = turns = built_total = 0.0
    for _ in range(n_games):
        bots = [greedy_bot] * n
        w, scores, st = run_game(bots, rng, n=n, force_first=0,
                                 flip_budget="shared:8", toll=True,
                                 hand_size=hand_size, draw=True,
                                 hand_cap=hand_cap)
        if st.turns >= TURN_CAP:
            caps += 1
        turns += st.turns
        builds += sum(st.builds) / n
        kept += sum(len(st.contracts(p)) for p in range(n)) / n
        fulfilled_pp += sum(s[0] for s in scores) / n
        conn += map_connectivity(st.edges)
        built_total += len(st.edges)
    g = n_games
    print(f"   {label:<10} H={hand_size} cap={hand_cap} | turns {turns/g:4.1f} | "
          f"roads built {built_total/g:4.1f}/28 | kept/p {kept/g:4.1f} | "
          f"fulfilled/p {fulfilled_pp/g:4.1f} | map-conn {pct(conn/g)} | "
          f"caps {pct(caps/g)}")


def draw_study(n_games=300, seed=42):
    rng = random.Random(seed)
    print("=" * 78)
    print(f"DRAW-MODEL STUDY · seed {seed} · deal H=6, build auto-refills from a"
          " pile")
    print("  (Toll on, Signal Fires; contracts = final hand. NOTE: a real draw")
    print("   pile of double-faced cards has no back — handling caveat, not"
          " simmed.)")
    print("=" * 78)

    print("\n[DENSITY / LENGTH / CHURN] all-greedy mirror — draw vs static")
    for (H, cap) in ((6, 6), (6, 8), (5, 6)):
        draw_mirror(n_games, rng, 2, H, cap, label="2P draw")
    draw_mirror(n_games, rng, 3, 6, 6, label="3P draw")
    print("   --- reference (static, no draw) ---")
    unified_mirror(n_games, rng, 2, 9, label="2P static")
    unified_mirror(n_games, rng, 2, 6, label="2P static")
    unified_mirror(n_games, rng, 3, 9, label="3P static")

    print("\n[SKILL GAP] lone greedy vs random — does churn dilute skill?")
    for (H, cap) in ((6, 6), (6, 8)):
        skill_gap(n_games, rng, 2, "shared:8", toll=True, hand_size=H,
                  draw=True, hand_cap=cap, label=f"2P draw H={H} cap={cap}")
    skill_gap(n_games, rng, 3, "shared:8", toll=True, hand_size=6, draw=True,
              hand_cap=6, label="3P draw H=6 cap=6")
    skill_gap(n_games, rng, 2, "shared:8", toll=True, hand_size=6,
              label="2P static H=6 (ref)")

    print("\n[PASS-TO-WIN vs NAIVE] (Toll on) — does drawing reopen the exploit?")
    for (H, cap) in ((6, 6), (6, 8)):
        passbot_test(n_games, rng, 2, "shared:8", toll=True, builder=naive_bot,
                     hand_size=H, draw=True, hand_cap=cap,
                     label=f"2P draw H={H} cap={cap}")
    passbot_test(n_games, rng, 3, "shared:8", toll=True, builder=naive_bot,
                 hand_size=6, draw=True, hand_cap=6, label="3P draw H=6 cap=6")


if __name__ == "__main__":
    draw_study()
