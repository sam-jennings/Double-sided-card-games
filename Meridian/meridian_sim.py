"""MERIDIAN — structural simulation (concept-stage, NEW_GAME_CONCEPTS.md §14).

Two forks share one skeleton (draft -> build a directed edge -> optional re-aim):

  GOAL  (deck-only): you score by claiming public GOAL cards. A goal (o->d) is
        claimed by the active player the instant a directed route o->d exists.
  NODE  (cube kit): you OWN each edge you build and aim it at one of its two
        signs (a vote). At end, the player with most votes aimed at a sign
        controls it and scores its pip.

Questions (per the concept sheet):
  1. Termination — does the draft clock end the game regardless of flips?
  2. Skill gap — greedy vs random, >= ~1.5x fair?
  3. Pass-to-win — a do-nothing player should score ~0 (dead by construction).
  4. FLIP-RELEVANCE (decides the fork) — compare each fork WITH vs WITHOUT the
     flip action. If removing flips barely changes skill/scoring, flipping is
     inert (rubric #4 fails) and the deck-tie weakens.
  5. Tie/draw rate (a crude kingmaking-adjacency signal at 3-4P).

Player-count scales by SUBSET: 2P=7 signs/21 cards, 3P=8/28, 4P=9/36. Sign pip
= sign index (Moon 1 .. Crown 9). One-ply bots — a floor, not a ceiling.
"""

import random
import itertools

# n players -> (#signs). Subset property: declare fewer signs for fewer players.
SIGNS_FOR = {2: 7, 3: 8, 4: 9}
HAND = 3
MARKET = 3
GOALS_FACEUP = 3
GOAL_POOL = {2: 5, 3: 6, 4: 7}     # total goal cards carved off the deck
FLIP_POOL = {2: 6, 3: 8, 4: 9}     # shared re-aim budget (bounds flip wars)
TURN_CAP = 200


def signs_of(n):
    return list(range(1, SIGNS_FOR[n] + 1))


def all_edges(signs):
    return [tuple(sorted(p)) for p in itertools.combinations(signs, 2)]


def directed_reach(aim, signs):
    """aim: edge -> the sign it points to. Returns set of (s, v): v reachable
    from s along directed edges."""
    adj = {s: [] for s in signs}
    for (a, b), to in aim.items():
        frm = a if to == b else b
        adj[frm].append(to)
    reach = set()
    for s in signs:
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


def same_component(aim, signs):
    """Union-find over present edges (ignoring direction). Returns find()."""
    parent = {s: s for s in signs}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (a, b) in aim:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return find


def node_control(aim, owner, signs, n):
    """NODE fork: for each sign, the player with the most owned edges aimed at
    it controls it (ties -> nobody). Returns score[p] = pip-sum controlled."""
    score = [0] * n
    for s in signs:
        votes = [0] * n
        for e, to in aim.items():
            if to == s:
                votes[owner[e]] += 1
        top = max(votes)
        if top == 0:
            continue
        leaders = [p for p in range(n) if votes[p] == top]
        if len(leaders) == 1:
            score[leaders[0]] += s   # pip == sign index
    return score


class State:
    def __init__(self, rng, n, mode, flips_enabled):
        self.n = n
        self.mode = mode
        self.flips_enabled = flips_enabled
        self.signs = signs_of(n)
        deck = all_edges(self.signs)
        rng.shuffle(deck)
        # carve goals (GOAL fork) — destination = a random end of each goal card
        gpool = GOAL_POOL[n]
        goal_cards = deck[:gpool] if mode == "goal" else []
        rest = deck[gpool:] if mode == "goal" else deck
        self.goal_stock = [(c[rng.randint(0, 1)], c) for c in goal_cards]
        self.goals = []  # face-up: list of (dest, other, card)
        for _ in range(min(GOALS_FACEUP, len(self.goal_stock))):
            self._reveal_goal()
        self.hands = [rest[i * HAND:(i + 1) * HAND] for i in range(n)]
        self.stock = rest[n * HAND:]
        self.market = [self.stock.pop() for _ in range(min(MARKET, len(self.stock)))]
        self.aim = {}        # edge -> sign pointed to
        self.owner = {}      # edge -> player (NODE fork)
        self.claimed = [[] for _ in range(n)]   # GOAL fork: pips claimed
        self.flip_pool = FLIP_POOL[n]            # shared re-aim budget
        self.turns = 0
        self.builds = [0] * n
        self.flips = [0] * n
        self.idle_rounds = 0
        # flip-relevance telemetry
        self.flip_claims = 0
        self.build_claims = 0

    def _reveal_goal(self):
        if self.goal_stock:
            dest, card = self.goal_stock.pop()
            other = card[0] if dest == card[1] else card[1]
            self.goals.append((dest, other, card))

    def deck_empty(self):
        return not self.stock and not self.market

    def draft(self, p, rng, pick_best):
        if not self.market:
            return
        if pick_best:
            idx = max(range(len(self.market)),
                      key=lambda i: self._draft_score(p, self.market[i]))
        else:
            idx = rng.randrange(len(self.market))
        self.hands[p].append(self.market.pop(idx))
        if self.stock:
            self.market.append(self.stock.pop())

    def _draft_score(self, p, card):
        if self.mode == "goal":
            ends = set()
            for (d, o, _c) in self.goals:
                ends.add(d)
                ends.add(o)
            return sum(1 for s in card if s in ends)
        return card[0] + card[1]   # NODE: prefer high-pip signs

    def legal_builds(self, p):
        acts = []
        for card in self.hands[p]:
            acts.append(("build", card, card[0]))
            acts.append(("build", card, card[1]))
        return acts

    def legal_flips(self):
        if not self.flips_enabled or self.flip_pool <= 0:
            return []
        return [("flip", e, None) for e in self.aim]

    def apply(self, p, act):
        kind, x, y = act
        if kind == "pass":
            self.idle_rounds += 1
            self.turns += 1
            return
        self.idle_rounds = 0
        if kind == "build":
            self.hands[p].remove(x)
            self.aim[x] = y
            self.owner[x] = p
            self.builds[p] += 1
        else:  # flip
            e = x
            a, b = e
            self.aim[e] = a if self.aim[e] == b else b
            self.flips[p] += 1
            self.flip_pool -= 1
        self._resolve_claims(p, kind)
        self.turns += 1

    def _resolve_claims(self, p, kind):
        if self.mode != "goal" or not self.goals:
            return
        reach = directed_reach(self.aim, self.signs)
        still = []
        claimed_any = False
        for (d, o, card) in self.goals:
            if (o, d) in reach:
                self.claimed[p].append(d if False else (card[0] + card[1]))
                claimed_any = True
                if kind == "flip":
                    self.flip_claims += 1
                else:
                    self.build_claims += 1
            else:
                still.append((d, o, card))
        self.goals = still
        while len(self.goals) < GOALS_FACEUP and self.goal_stock:
            self._reveal_goal()

    def scores(self):
        if self.mode == "goal":
            return [sum(c) for c in self.claimed]
        return node_control(self.aim, self.owner, self.signs, self.n)


def state_value(st, p):
    """1-ply heuristic of the position for player p."""
    if st.mode == "goal":
        v = sum(st.claimed[p]) * 1.0
        find = same_component(st.aim, st.signs)
        for (d, o, card) in st.goals:
            pip = card[0] + card[1]
            if find(o) == find(d):
                v += 0.3 * pip       # connected (undirected) — close to claimable
        return v
    sc = node_control(st.aim, st.owner, st.signs, st.n)
    others = [sc[q] for q in range(st.n) if q != p]
    return sc[p] - (sum(others) / len(others) if others else 0)


def greedy_action(st, p, rng):
    acts = st.legal_builds(p) + st.legal_flips()
    if not acts:
        return ("pass", None, None)
    base = state_value(st, p)
    best, best_v = ("pass", None, None), base + 1e-9
    for act in acts:
        snap = _snapshot(st)
        st.apply(p, act)
        v = state_value(st, p) + rng.random() * 1e-4
        _restore(st, snap)
        if v > best_v:
            best, best_v = act, v
    return best


def random_action(st, p, rng):
    acts = st.legal_builds(p) + st.legal_flips()
    if acts and rng.random() > 0.05:
        return rng.choice(acts)
    return ("pass", None, None)


def pass_action(st, p, rng):
    return ("pass", None, None)


def _snapshot(st):
    return (dict(st.aim), dict(st.owner), [list(c) for c in st.claimed],
            list(st.goals), list(st.goal_stock),
            [list(h) for h in st.hands], st.flip_claims, st.build_claims,
            list(st.builds), list(st.flips), st.turns, st.idle_rounds,
            st.flip_pool)


def _restore(st, snap):
    (aim, owner, claimed, goals, goal_stock, hands, fc, bc, builds, flips,
     turns, idle, pool) = snap
    st.aim = dict(aim)
    st.owner = dict(owner)
    st.claimed = [list(c) for c in claimed]
    st.goals = list(goals)
    st.goal_stock = list(goal_stock)
    st.hands = [list(h) for h in hands]
    st.flip_claims = fc
    st.build_claims = bc
    st.builds = list(builds)
    st.flips = list(flips)
    st.turns = turns
    st.idle_rounds = idle
    st.flip_pool = pool


def run_game(n, mode, bots, rng, flips_enabled=True, greedy_draft=None):
    st = State(rng, n, mode, flips_enabled)
    if greedy_draft is None:
        greedy_draft = [b is greedy_action for b in bots]
    p = 0
    while st.turns < TURN_CAP:
        st.draft(p, rng, pick_best=greedy_draft[p])
        act = bots[p](st, p, rng)
        st.apply(p, act)
        if st.deck_empty() and st.idle_rounds >= n:
            break
        p = (p + 1) % n
    return st


def pct(x):
    return f"{100*x:.1f}%"


def winner(scores):
    top = max(scores)
    leaders = [i for i, s in enumerate(scores) if s == top]
    return leaders[0] if len(leaders) == 1 else None


# ---------------------------------------------------------------- experiments

def skill_gap(mode, n, flips_enabled, games, rng):
    gw = dec = 0
    for g in range(games):
        seat = g % n
        bots = [random_action] * n
        bots[seat] = greedy_action
        gd = [b is greedy_action for b in bots]
        st = run_game(n, mode, bots, rng, flips_enabled, gd)
        w = winner(st.scores())
        if w is not None:
            dec += 1
            if w == seat:
                gw += 1
    fair = 1.0 / n
    rate = gw / max(dec, 1)
    return rate, rate / fair


def mirror(mode, n, flips_enabled, games, rng):
    turns = caps = draws = 0
    score_sum = flips_sum = builds_sum = 0
    claims = fclaims = bclaims = 0
    for _ in range(games):
        bots = [greedy_action] * n
        st = run_game(n, mode, bots, rng, flips_enabled)
        if st.turns >= TURN_CAP:
            caps += 1
        turns += st.turns
        sc = st.scores()
        if winner(sc) is None:
            draws += 1
        score_sum += sum(sc) / n
        flips_sum += sum(st.flips)
        builds_sum += sum(st.builds)
        if mode == "goal":
            fclaims += st.flip_claims
            bclaims += st.build_claims
            claims += st.flip_claims + st.build_claims
    g = games
    out = {
        "turns": turns / g, "caps": caps / g, "draws": draws / g,
        "score": score_sum / g, "flips": flips_sum / g, "builds": builds_sum / g,
    }
    if mode == "goal":
        out["claims"] = claims / g
        out["flip_claim_frac"] = fclaims / max(claims, 1)
    return out


def passbot_test(mode, n, games, rng):
    pw = 0
    pscore = oscore = 0.0
    for gi in range(games):
        pseat = gi % n
        bots = [greedy_action] * n
        bots[pseat] = pass_action
        gd = [b is greedy_action for b in bots]
        st = run_game(n, mode, bots, rng, True, gd)
        sc = st.scores()
        if winner(sc) == pseat:
            pw += 1
        pscore += sc[pseat]
        oscore += sum(sc[q] for q in range(n) if q != pseat) / (n - 1)
    g = games
    return pw / g, pscore / g, oscore / g


def main(games=250, seed=42):
    rng = random.Random(seed)
    print("=" * 80)
    print(f"MERIDIAN structural sim · seed {seed} · {games} games/cell · 1-ply bots")
    print("=" * 80)

    for mode in ("goal", "node"):
        title = "GOAL-RACE (deck-only)" if mode == "goal" else "NODE-MAJORITY (cubes)"
        print(f"\n############  {title}  ############")

        print("\n[TERMINATION + SKILL GAP]  (flips ON)")
        for n in (2, 3, 4):
            m = mirror(mode, n, True, games, rng)
            rate, x = skill_gap(mode, n, True, games, rng)
            extra = (f" | claims/game {m['claims']:.1f} "
                     f"(flip-claims {pct(m['flip_claim_frac'])})"
                     if mode == "goal" else
                     f" | flips/game {m['flips']:.1f}")
            print(f"  {n}P: len {m['turns']:4.1f} caps {pct(m['caps'])} "
                  f"draws {pct(m['draws'])} | greedy {pct(rate)} = {x:.2f}x fair"
                  f"{extra}")

        print("\n[PASS-TO-WIN]  (do-nothing player vs greedy)")
        for n in (2, 3, 4):
            pw, ps, os_ = passbot_test(mode, n, games, rng)
            print(f"  {n}P: passer wins {pct(pw)} (fair {pct(1/n)}) | "
                  f"passer score {ps:.1f} vs others {os_:.1f}")

        print("\n[FLIP-RELEVANCE]  greedy skill gap & dynamics WITH vs WITHOUT flips")
        for n in (2, 3, 4):
            _, x_on = skill_gap(mode, n, True, games, rng)
            _, x_off = skill_gap(mode, n, False, games, rng)
            m_on = mirror(mode, n, True, games, rng)
            m_off = mirror(mode, n, False, games, rng)
            if mode == "goal":
                dyn = (f"flip-claims {pct(m_on['flip_claim_frac'])} | "
                       f"claims/game {m_on['claims']:.1f}->{m_off['claims']:.1f} "
                       f"(no-flip)")
            else:
                dyn = (f"flips/game {m_on['flips']:.1f} | "
                       f"avg score {m_on['score']:.1f}->{m_off['score']:.1f}")
            print(f"  {n}P: skill {x_on:.2f}x (flips) vs {x_off:.2f}x (no flips) "
                  f"| {dyn}")


if __name__ == "__main__":
    main()
