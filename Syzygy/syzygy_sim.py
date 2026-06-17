#!/usr/bin/env python3
"""
SYZYGY — simulator & automated playtest harness.

36 double-faced cards = all C(9,2) pairs of 9 symbols. 3x3 grid.
Place a card (either side up). If its requirement is met it may activate.
Cards that get placed / flipped / moved, or whose requirement newly becomes
true, become eligible ("primed"); each card activates at most once per turn.
Any line (row/col/diag) of 3 identical face-up symbols is captured by the
active player the moment it exists. Deck empty -> game over, most cards wins.

Variant flags allow A/B testing of rule patches between versions.
"""

import argparse
import itertools
import random
import statistics
import sys
import time
from collections import defaultdict

# ---------------------------------------------------------------- constants
SYM = ["Sun", "Moon", "Star", "Comet", "Eclipse", "Aurora", "Meteor", "Nova", "Void"]
SUN, MOON, STAR, COMET, ECLIPSE, AURORA, METEOR, NOVA, VOID = range(9)
CARDS = [tuple(sorted(p)) for p in itertools.combinations(range(9), 2)]  # 36
CORNERS = (0, 2, 6, 8)
EDGES = (1, 3, 5, 7)
CENTER = 4
NEI = {
    0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
    3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8),
    6: (3, 7), 7: (4, 6, 8), 8: (5, 7),
}
ROWS = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
COLS = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
DIAGS = ((0, 4, 8), (2, 4, 6))
ALL_LINES = ROWS + COLS + DIAGS


def other(cid, up):
    a, b = CARDS[cid]
    return b if up == a else a


# ---------------------------------------------------------------- variants
class Var:
    """Rule variant switches (defaults = v1.0)."""
    def __init__(self, eclipse_mode="any", void_mode="deck_point",
                 star_wild=False, diagonals=True, sun_plus=False,
                 meteor_loose=False, tie_to_first=False, tie_mode=None):
        self.eclipse_mode = eclipse_mode      # 'any' | 'self'
        self.void_mode = void_mode            # 'deck_point' | 'catchup' | 'mill'
        self.star_wild = star_wild            # Star faces are wild in lines
        self.diagonals = diagonals            # diagonals count as capture lines
        self.sun_plus = sun_plus              # Sun req: middle row OR column
        self.meteor_loose = meteor_loose      # Meteor req: 1-2 nbrs, pick target
        # tie_mode: 'shared'|'seat'|'first_cap'|'last_cap'
        self.tie_mode = tie_mode or ('seat' if tie_to_first else 'shared')

    def lines(self):
        return ALL_LINES if self.diagonals else ROWS + COLS

    def label(self):
        return (f"eclipse={self.eclipse_mode},void={self.void_mode},"
                f"star_wild={self.star_wild},diag={self.diagonals},"
                f"sun_plus={self.sun_plus},meteor_loose={self.meteor_loose},"
                f"tie={self.tie_mode}")


# ---------------------------------------------------------------- game state
class Game:
    __slots__ = ("grid", "deck", "scores", "removed", "np", "cur", "rng", "var",
                 "first_cap", "last_cap")

    def __init__(self, n_players, rng, var):
        self.np = n_players
        self.rng = rng
        self.var = var
        self.grid = [None] * 9                 # cell -> (cid, up) or None
        self.deck = list(range(36))
        rng.shuffle(self.deck)
        self.scores = [[] for _ in range(n_players)]  # (cid, up) ; up=None for Void deck-grab
        self.removed = []
        self.cur = 0
        self.first_cap = None
        self.last_cap = None

    def clone(self):
        g = object.__new__(Game)
        g.np = self.np
        g.rng = self.rng
        g.var = self.var
        g.grid = list(self.grid)
        g.deck = list(self.deck)
        g.first_cap = self.first_cap
        g.last_cap = self.last_cap
        g.scores = [list(s) for s in self.scores]
        g.removed = list(self.removed)
        g.cur = self.cur
        return g

    def occupied(self):
        return [c for c in range(9) if self.grid[c] is not None]

    def empties(self):
        return [c for c in range(9) if self.grid[c] is None]


class Ctx:
    """Per-turn activation context."""
    __slots__ = ("primed", "activated")

    def __init__(self):
        self.primed = set()      # card ids eligible to activate this turn
        self.activated = set()   # card ids that already activated this turn

    def clone(self):
        c = object.__new__(Ctx)
        c.primed = set(self.primed)
        c.activated = set(self.activated)
        return c


# ---------------------------------------------------------------- stats
class Stats:
    def __init__(self):
        self.d = defaultdict(int)
        self.chain_hist = defaultdict(int)     # activations-per-turn histogram
        self.per_player_acts = None            # set per game
        self.anomalies = 0

    def inc(self, key, n=1):
        self.d[key] += n


class NullStats(Stats):
    def inc(self, key, n=1):
        pass


NULL = NullStats()


# ---------------------------------------------------------------- rules core
def req_met(g, cell):
    cid, up = g.grid[cell]
    if up == SUN:
        if g.var.sun_plus:
            return cell == CENTER or cell in (1, 3, 5, 7)  # middle row/col
        return cell == CENTER
    if up == MOON:
        return cell in EDGES
    if up == STAR:
        return cell in CORNERS
    if up == COMET:
        r, c = divmod(cell, 3)
        for x in range(9):
            if g.grid[x] is None and (x // 3 == r or x % 3 == c):
                return True
        return False
    nbrs = NEI[cell]
    occ = sum(1 for n in nbrs if g.grid[n] is not None)
    if up == ECLIPSE:
        return occ >= 2
    if up == AURORA:
        return occ < len(nbrs)
    if up == METEOR:
        return occ == 1 or (g.var.meteor_loose and occ == 2)
    if up == NOVA:
        r, c = divmod(cell, 3)
        return (all(g.grid[x] is not None for x in ROWS[r])
                or all(g.grid[x] is not None for x in COLS[c]))
    if up == VOID:
        return occ == 0
    raise AssertionError


def _snapshot(g):
    d = {}
    for c in range(9):
        e = g.grid[c]
        if e is not None:
            d[e[0]] = req_met(g, c)
    return d


def _prime_transitions(g, ctx, pre):
    for c in range(9):
        e = g.grid[c]
        if e is None:
            continue
        if e[0] not in ctx.primed and req_met(g, c) and not pre.get(e[0], False):
            ctx.primed.add(e[0])


# --- primitive mutations (all handle priming) ---
def m_place(g, ctx, cid, cell, up):
    pre = _snapshot(g)
    g.grid[cell] = (cid, up)
    _prime_transitions(g, ctx, pre)
    ctx.primed.add(cid)


def m_flip(g, ctx, cell):
    pre = _snapshot(g)
    cid, up = g.grid[cell]
    g.grid[cell] = (cid, other(cid, up))
    _prime_transitions(g, ctx, pre)
    ctx.primed.add(cid)


def m_move(g, ctx, src, dst):
    pre = _snapshot(g)
    g.grid[dst] = g.grid[src]
    g.grid[src] = None
    _prime_transitions(g, ctx, pre)
    ctx.primed.add(g.grid[dst][0])


def m_swap(g, ctx, a, b):
    pre = _snapshot(g)
    g.grid[a], g.grid[b] = g.grid[b], g.grid[a]
    _prime_transitions(g, ctx, pre)
    ctx.primed.add(g.grid[a][0])
    ctx.primed.add(g.grid[b][0])


def m_remove(g, ctx, cell, dest_list, tag):
    pre = _snapshot(g)
    e = g.grid[cell]
    g.grid[cell] = None
    if tag == "removed":
        dest_list.append(e[0])
    else:
        dest_list.append(e)
    _prime_transitions(g, ctx, pre)
    return e


def capture_cells(g):
    """Cells currently part of a 3-identical line (Star wild if variant on)."""
    capt = set()
    for line in g.var.lines():
        e0, e1, e2 = g.grid[line[0]], g.grid[line[1]], g.grid[line[2]]
        if e0 is None or e1 is None or e2 is None:
            continue
        if g.var.star_wild:
            non_star = {e[1] for e in (e0, e1, e2)} - {STAR}
            if len(non_star) <= 1:
                capt.update(line)
        else:
            if e0[1] == e1[1] == e2[1]:
                capt.update(line)
    return capt


def capture_check(g, ctx, player, stats):
    """Capture all aligned lines, repeatedly (removals can't create new lines,
    but keep loop for safety with future variants)."""
    total = 0
    while True:
        cells = capture_cells(g)
        if not cells:
            return total
        pre = _snapshot(g)
        for c in sorted(cells):
            cid, up = g.grid[c]
            g.grid[c] = None
            g.scores[player].append((cid, up))
            ctx.activated.add(cid)          # captured cards never activate
            stats.inc(("captured_as", up))
        total += len(cells)
        if g.first_cap is None:
            g.first_cap = player
        g.last_cap = player
        stats.inc("line_capture_events")
        stats.inc("line_cards", len(cells))
        _prime_transitions(g, ctx, pre)


def ability_candidates(g, cell, player):
    """All legal instantiations of the ability of the face-up card at `cell`."""
    cid, up = g.grid[cell]
    if up == SUN:
        return [("flip", c) for c in g.occupied()]
    if up in (MOON, AURORA):
        return [("flip", n) for n in NEI[cell] if g.grid[n] is not None]
    if up == STAR:
        return [("star",)] if g.deck else []
    if up == COMET:
        emp = g.empties()
        return [("move", s, d) for s in g.occupied() for d in emp]
    if up == ECLIPSE:
        occ = g.occupied()
        if g.var.eclipse_mode == "self":
            return [("swap", cell, o) for o in occ if o != cell]
        return [("swap", a, b) for i, a in enumerate(occ) for b in occ[i + 1:]]
    if up == METEOR:
        ns = [n for n in NEI[cell] if g.grid[n] is not None]
        if g.var.meteor_loose:
            return [("discard", n) for n in ns] if 1 <= len(ns) <= 2 else []
        return [("discard", ns[0])] if len(ns) == 1 else []
    if up == NOVA:
        r, c = divmod(cell, 3)
        out = []
        for line in (ROWS[r], COLS[c]):
            if all(g.grid[x] is not None for x in line):
                out.append(("nova", line, cell))
        return out
    if up == VOID:
        if not g.deck:
            return []
        if g.var.void_mode == "mill":
            return [("void_mill",)]
        if g.var.void_mode == "catchup":
            mine = len(g.scores[player])
            if any(len(g.scores[q]) > mine for q in range(g.np) if q != player):
                return [("void",)]
            return []
        return [("void",)]
    raise AssertionError


def apply_action(g, ctx, player, action, bots, stats, depth):
    kind = action[0]
    if kind == "flip":
        m_flip(g, ctx, action[1])
    elif kind == "move":
        m_move(g, ctx, action[1], action[2])
    elif kind == "swap":
        m_swap(g, ctx, action[1], action[2])
    elif kind == "discard":
        m_remove(g, ctx, action[1], g.removed, "removed")
        stats.inc("meteor_discards")
    elif kind == "nova":
        line, self_cell = action[1], action[2]
        for x in line:
            if x != self_cell and g.grid[x] is not None:
                m_flip(g, ctx, x)
    elif kind == "star":
        if g.deck:
            if not g.empties():
                dcell = bots[player].choose_discard(g)
                m_remove(g, ctx, dcell, g.removed, "removed")
                stats.inc("full_grid_discards")
            cid2 = g.deck.pop(0)
            cell2, up2 = bots[player].choose_placement(g, cid2, ctx, depth + 1)
            stats.inc(("placed_up", up2))
            m_place(g, ctx, cid2, cell2, up2)
            if g.grid[cell2] is not None and g.grid[cell2][0] == cid2 and req_met(g, cell2):
                stats.inc(("req_on_entry", up2))
            stats.inc("star_extra_plays")
    elif kind == "void":
        cid2 = g.deck.pop(0)
        g.scores[player].append((cid2, None))
        stats.inc("void_captures")
    elif kind == "void_mill":
        cid2 = g.deck.pop(0)
        g.removed.append(cid2)
        stats.inc("void_mills")
    else:
        raise AssertionError(kind)


def opportunities(g, ctx, player):
    out = []
    for c in range(9):
        e = g.grid[c]
        if e is None:
            continue
        cid = e[0]
        if cid in ctx.primed and cid not in ctx.activated and req_met(g, c):
            if ability_candidates(g, c, player):
                out.append(c)
    return out


def resolve(g, ctx, player, bots, stats, depth=0):
    """Capture, then let the active player chain activations."""
    capture_check(g, ctx, player, stats)
    n_acts = 0
    guard = 0
    while True:
        opps = opportunities(g, ctx, player)
        if not opps:
            break
        pick = bots[player].choose_activation(g, ctx, player, opps, depth)
        if pick is None:
            break
        cell, action = pick
        cid, up = g.grid[cell]
        ctx.activated.add(cid)
        stats.inc(("activated", up))
        if stats.per_player_acts is not None:
            stats.per_player_acts[player][up] += 1
        apply_action(g, ctx, player, action, bots, stats, depth)
        capture_check(g, ctx, player, stats)
        n_acts += 1
        guard += 1
        if guard > 80:
            stats.anomalies += 1
            break
    return n_acts


def play_turn(g, bots, stats):
    p = g.cur
    if not g.deck:
        return False
    ctx = Ctx()
    if not g.empties():
        dcell = bots[p].choose_discard(g)
        m_remove(g, ctx, dcell, g.removed, "removed")
        stats.inc("full_grid_discards")
    cid = g.deck.pop(0)
    cell, up = bots[p].choose_placement(g, cid, ctx, 0)
    stats.inc(("placed_up", up))
    m_place(g, ctx, cid, cell, up)
    if g.grid[cell] is not None and g.grid[cell][0] == cid and req_met(g, cell):
        stats.inc(("req_on_entry", up))
    n_acts = resolve(g, ctx, p, bots, stats)
    stats.chain_hist[min(n_acts, 6)] += 1
    stats.inc("turns")
    g.cur = (p + 1) % g.np
    return True


def winners(g):
    counts = [len(s) for s in g.scores]
    best = max(counts)
    lead = [p for p in range(g.np) if counts[p] == best]
    if len(lead) == 1:
        return lead
    # tiebreak: most distinct face-up symbols among captures
    def distinct(p):
        return len({up for (_, up) in g.scores[p] if up is not None})
    bd = max(distinct(p) for p in lead)
    lead2 = [p for p in lead if distinct(p) == bd]
    if len(lead2) > 1:
        m = g.var.tie_mode
        if m == "seat":
            return [min(lead2)]
        if m == "first_cap":
            if g.first_cap in lead2:
                return [g.first_cap]
            return [min(lead2)]
        if m == "last_cap" and g.last_cap in lead2:
            return [g.last_cap]
    return lead2


# ---------------------------------------------------------------- bots
class RandomBot:
    def __init__(self, rng):
        self.rng = rng

    def choose_placement(self, g, cid, ctx, depth=0):
        cell = self.rng.choice(g.empties())
        up = self.rng.choice(CARDS[cid])
        return cell, up

    def choose_activation(self, g, ctx, player, opps, depth=0):
        if self.rng.random() < 0.25:
            return None
        cell = self.rng.choice(opps)
        cands = ability_candidates(g, cell, player)
        return cell, self.rng.choice(cands)

    def choose_discard(self, g):
        return self.rng.choice(g.occupied())


class GreedyBot:
    """One-ply greedy with capture/threat heuristic; perfect information."""
    MAX_CANDS = 14

    def __init__(self, rng):
        self.rng = rng

    # ----- evaluation -----
    def eval(self, g, me):
        counts = [len(s) for s in g.scores]
        mine = counts[me]
        opp = max((counts[q] for q in range(g.np) if q != me), default=0)
        v = 1000.0 * (mine - opp)
        threats = 0
        for line in g.var.lines():
            es = [g.grid[x] for x in line]
            occ = [e for e in es if e is not None]
            if len(occ) == 2 and occ[0][1] == occ[1][1]:
                threats += 1
            elif len(occ) == 3:
                ups = [e[1] for e in occ]
                for i in range(3):
                    j, k = (i + 1) % 3, (i + 2) % 3
                    if ups[j] == ups[k] and other(occ[i][0], ups[i]) == ups[j]:
                        threats += 1
                        break
        v -= 70.0 * threats
        v += 1.5 * len({up for (_, up) in g.scores[me] if up is not None})
        return v + self.rng.random() * 0.01

    # ----- helpers -----
    def _capped(self, cands):
        if len(cands) <= self.MAX_CANDS:
            return cands
        return self.rng.sample(cands, self.MAX_CANDS)

    def _try_action(self, g, ctx, player, cell, action, depth):
        g2 = g.clone()
        ctx2 = ctx.clone()
        cid = g2.grid[cell][0]
        ctx2.activated.add(cid)
        apply_action(g2, ctx2, player, action, [self] * g2.np, NULL, depth + 2)
        capture_check(g2, ctx2, player, NULL)
        return self.eval(g2, player), g2, ctx2

    # ----- decisions (choose_placement attached below) -----
    def choose_discard(self, g):
        best_v, best = -1e18, None
        me = g.cur
        for c in g.occupied():
            g2 = g.clone()
            ctx2 = Ctx()
            m_remove(g2, ctx2, c, g2.removed, "removed")
            v = self.eval(g2, me)
            if v > best_v:
                best_v, best = v, c
        return best

    def choose_activation(self, g, ctx, player, opps, depth=0):
        cur_v = self.eval(g, player)
        best_v, best = cur_v + 0.5, None
        for cell in opps:
            for action in self._capped(ability_candidates(g, cell, player)):
                v, _, _ = self._try_action(g, ctx, player, cell, action, depth)
                if v > best_v:
                    best_v, best = v, (cell, action)
        return best


def _greedy_choose_placement(self, g, cid, ctx, depth=0):
    """Place; if the placed card can act, look one action deep; evaluate."""
    me = g.cur
    a, b = CARDS[cid]
    best_v, best = -1e18, None
    for cell in g.empties():
        for up in (a, b):
            g2 = g.clone()
            ctx2 = ctx.clone()
            m_place(g2, ctx2, cid, cell, up)
            capture_check(g2, ctx2, me, NULL)
            v = self.eval(g2, me)
            # if it survived and can activate, consider its best single action
            if depth < 2 and g2.grid[cell] is not None and g2.grid[cell][0] == cid \
                    and req_met(g2, cell):
                cands = self._capped(ability_candidates(g2, cell, me))
                for action in cands:
                    v2, _, _ = self._try_action(g2, ctx2, me, cell, action, depth)
                    if v2 > v:
                        v = v2
            if v > best_v:
                best_v, best = v, (cell, up)
    return best


GreedyBot.choose_placement = _greedy_choose_placement


# ---------------------------------------------------------------- experiments
def run_games(n_players, bot_specs, n_games, seed, var, rotate_seats=True):
    """bot_specs: list of 'greedy'/'random' length n_players (seat order before rotation)."""
    agg = {
        "stats": Stats(),
        "games": 0,
        "seat_wins": [0.0] * n_players,
        "kind_wins": defaultdict(float),
        "kind_games": defaultdict(int),
        "scores_all": [],
        "margins": [],
        "turns": [],
        "zero_cap": 0,
        "ties": 0,
        "winner_acts": defaultdict(list),
        "loser_acts": defaultdict(list),
        "void_pts": [],
        "line_pts": [],
        "deck_leftover": [],
    }
    base_rng = random.Random(seed)
    for gi in range(n_games):
        rng = random.Random(base_rng.random())
        rot = gi % n_players if rotate_seats else 0
        kinds = bot_specs[rot:] + bot_specs[:rot]
        bots = [GreedyBot(rng) if k == "greedy" else RandomBot(rng) for k in kinds]
        g = Game(n_players, rng, var)
        st = agg["stats"]
        st.per_player_acts = [defaultdict(int) for _ in range(n_players)]
        t0 = st.d["turns"]
        while play_turn(g, bots, st):
            pass
        agg["games"] += 1
        agg["turns"].append(st.d["turns"] - t0)
        counts = [len(s) for s in g.scores]
        agg["scores_all"].extend(counts)
        srt = sorted(counts, reverse=True)
        agg["margins"].append(srt[0] - srt[1])
        win = winners(g)
        if len(win) > 1:
            agg["ties"] += 1
        for p in range(n_players):
            share = (1.0 / len(win)) if p in win else 0.0
            agg["seat_wins"][p] += share
            agg["kind_wins"][kinds[p]] += share
            agg["kind_games"][kinds[p]] += 1
            tgt = agg["winner_acts"] if p in win else agg["loser_acts"]
            for s in range(9):
                tgt[s].append(st.per_player_acts[p][s])
        if sum(counts) == 0:
            agg["zero_cap"] += 1
        agg["void_pts"].append(sum(1 for s in g.scores for (_, up) in s if up is None))
        agg["line_pts"].append(sum(1 for s in g.scores for (_, up) in s if up is not None))
        st.per_player_acts = None
    return agg


def fmt_pct(x):
    return f"{100*x:.1f}%"


def report(agg, title, n_players):
    st = agg["stats"]
    G = agg["games"]
    print(f"\n=== {title} ({G} games) ===")
    print(f"avg turns/game: {statistics.mean(agg['turns']):.1f}")
    tot_caps = (sum(agg['line_pts']) + sum(agg['void_pts'])) / G
    print(f"avg captured cards/game: {tot_caps:.1f}  "
          f"(line: {sum(agg['line_pts'])/G:.1f}, void: {sum(agg['void_pts'])/G:.1f})")
    print(f"zero-capture games: {fmt_pct(agg['zero_cap']/G)}   ties: {fmt_pct(agg['ties']/G)}")
    print(f"avg winning margin: {statistics.mean(agg['margins']):.2f} cards")
    print(f"seat win rates: " + "  ".join(
        f"P{p+1}:{fmt_pct(agg['seat_wins'][p]/G)}" for p in range(n_players)))
    if len(agg["kind_games"]) > 1:
        for k in agg["kind_games"]:
            print(f"  bot '{k}': {fmt_pct(agg['kind_wins'][k]/agg['kind_games'][k])} per-seat win rate")
    turns = st.d["turns"]
    chain_total = sum(st.chain_hist.values())
    c0 = st.chain_hist.get(0, 0) / max(chain_total, 1)
    c1 = st.chain_hist.get(1, 0) / max(chain_total, 1)
    c2p = sum(v for k, v in st.chain_hist.items() if k >= 2) / max(chain_total, 1)
    avg_chain = sum(k * v for k, v in st.chain_hist.items()) / max(chain_total, 1)
    print(f"activations/turn: avg {avg_chain:.2f} | 0 acts {fmt_pct(c0)} | 1 act {fmt_pct(c1)} | 2+ acts {fmt_pct(c2p)}")
    print(f"star extra plays/game: {st.d['star_extra_plays']/G:.2f}   "
          f"meteor discards/game: {st.d['meteor_discards']/G:.2f}   "
          f"full-grid discards/game: {st.d['full_grid_discards']/G:.2f}")
    if st.anomalies:
        print(f"!! anomalies (guard hit): {st.anomalies}")
    print(f"\n{'symbol':<9}{'placed%':>9}{'req-met%':>10}{'activ/game':>12}{'captured/game':>15}{'win-lose act diff':>19}")
    total_placed = sum(st.d.get(("placed_up", s), 0) for s in range(9))
    for s in range(9):
        placed = st.d.get(("placed_up", s), 0)
        reqm = st.d.get(("req_on_entry", s), 0)
        act = st.d.get(("activated", s), 0)
        cap = st.d.get(("captured_as", s), 0)
        w = statistics.mean(agg["winner_acts"][s]) if agg["winner_acts"][s] else 0.0
        l = statistics.mean(agg["loser_acts"][s]) if agg["loser_acts"][s] else 0.0
        print(f"{SYM[s]:<9}{fmt_pct(placed/max(total_placed,1)):>9}"
              f"{fmt_pct(reqm/max(placed,1)):>10}{act/G:>12.2f}{cap/G:>15.2f}{w-l:>+19.2f}")


def suite(name, var, n_games, seed):
    t0 = time.time()
    if name == "sanity":
        agg = run_games(2, ["random", "random"], n_games, seed, var)
        report(agg, f"Random vs Random 2P [{var.label()}]", 2)
    elif name == "g2":
        agg = run_games(2, ["greedy", "greedy"], n_games, seed, var)
        report(agg, f"Greedy mirror 2P [{var.label()}]", 2)
    elif name == "g3":
        agg = run_games(3, ["greedy"] * 3, n_games, seed, var)
        report(agg, f"Greedy mirror 3P [{var.label()}]", 3)
    elif name == "g4":
        agg = run_games(4, ["greedy"] * 4, n_games, seed, var)
        report(agg, f"Greedy mirror 4P [{var.label()}]", 4)
    elif name == "gvr":
        agg = run_games(2, ["greedy", "random"], n_games, seed, var)
        report(agg, f"Greedy vs Random 2P [{var.label()}]", 2)
    else:
        raise SystemExit(f"unknown suite {name}")
    print(f"[{name}: {time.time()-t0:.1f}s]")


def smoke():
    var = Var()
    rng = random.Random(7)
    for i in range(20):
        bots = [RandomBot(rng), GreedyBot(rng)]
        g = Game(2, rng, var)
        st = Stats()
        st.per_player_acts = [defaultdict(int) for _ in range(2)]
        while play_turn(g, bots, st):
            pass
        on_grid = len(g.occupied())
        in_scores = sum(len(s) for s in g.scores)
        total = on_grid + in_scores + len(g.removed) + len(g.deck)
        assert total == 36, (total, i)
        assert not g.deck
        assert st.anomalies == 0
    print("smoke OK: card conservation, termination, no anomalies (20 games)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("suites", nargs="*", default=["sanity"])
    ap.add_argument("--games", type=int, default=400)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--eclipse", default="any", choices=["any", "self"])
    ap.add_argument("--void", default="deck_point", choices=["deck_point", "catchup", "mill"])
    ap.add_argument("--star-wild", action="store_true")
    ap.add_argument("--no-diag", action="store_true")
    ap.add_argument("--sun-plus", action="store_true")
    ap.add_argument("--meteor-loose", action="store_true")
    ap.add_argument("--tie-first", action="store_true")
    ap.add_argument("--tie-mode", default=None,
                    choices=["shared", "seat", "first_cap", "last_cap"])
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    if args.smoke:
        smoke()
        return
    var = Var(eclipse_mode=args.eclipse, void_mode=args.void,
              star_wild=args.star_wild, diagonals=not args.no_diag,
              sun_plus=args.sun_plus, meteor_loose=args.meteor_loose,
              tie_to_first=args.tie_first, tie_mode=args.tie_mode)
    for s in args.suites:
        suite(s, var, args.games, args.seed)


if __name__ == "__main__":
    main()
