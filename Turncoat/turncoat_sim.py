#!/usr/bin/env python3
"""TURNCOAT simulator — allegiance, covering, extraction. v1.2 final rules (defaults).

Invariant: grid + piles + removed + deck == 36 at all times.
"""
import argparse
import random
import time
from collections import defaultdict

# ---------------------------------------------------------------- constants
BLADE, MASK, WHISPER, COIN, VEIL, KEY, HOUND, CROWN, ASH = range(9)
NAMES = ["Blade", "Mask", "Whisper", "Coin", "Veil", "Key", "Hound", "Crown", "Ash"]

CARDS = [(a, b) for a in range(9) for b in range(a + 1, 9)]   # 36 pairs
assert len(CARDS) == 36

ROWS = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
COLS = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
NEI = {
    0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
    3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8),
    6: (3, 7), 7: (4, 6, 8), 8: (5, 7),
}
LINE_OF = {c: (ROWS[c // 3], COLS[c % 3]) for c in range(9)}


def face(cid, up):
    return CARDS[cid][up]


def other_face(cid, up):
    return CARDS[cid][1 - up]


# ---------------------------------------------------------------- variants
class Var:
    """Rule variant switches (defaults = v1.0)."""
    def __init__(self, neutral_bank="removed", cover_own_only=False,
                 hound_mode="to_empty", mask_req="rival", ash_mode="burn",
                 tie_mode="first_ext", loyalist=False, coin_req="pair",
                 komi_p1=0, whisper_req="le1", veil_req="own",
                 crown_req="own2", mask_ability="any", ash_gap=1,
                 veil_flip=False, hound_flip=False, hound_req="12",
                 hound_move="any", key_reach="adj", coin_place="any",
                 vis_weight=1, komi4=0):
        self.neutral_bank = neutral_bank      # 'removed' | 'active'
        self.cover_own_only = cover_own_only  # may only cover faces you own (+neutral)
        self.hound_mode = hound_mode          # 'to_empty' | 'adj_swap'
        self.mask_req = mask_req              # 'rival' | 'any'
        self.ash_mode = ash_mode              # 'burn' | 'gain'
        self.tie_mode = tie_mode              # 'first_ext' | 'shared' | 'seat'
        self.loyalist = loyalist              # only activate faces you own
        self.coin_req = coin_req              # 'pair' | 'two_any'
        self.komi_p1 = komi_p1                # 2P: bonus points for P1
        self.whisper_req = whisper_req        # 'le1' | 'eq1'
        self.veil_req = veil_req              # 'own' | 'rival'
        self.crown_req = crown_req            # 'own2' | 'own1'
        self.mask_ability = mask_ability      # 'any' | 'line'
        self.ash_gap = ash_gap                # rival lead needed to burn
        self.veil_flip = veil_flip            # Veil may flip itself after swap
        self.hound_flip = hound_flip          # Hound may flip the moved agent
        self.hound_req = hound_req            # '12' | '1' adjacent agents
        self.hound_move = hound_move          # 'any' | 'line' empty cells
        self.key_reach = key_reach            # 'adj' | 'line'
        self.coin_place = coin_place          # 'any' | 'empty_only'
        self.vis_weight = vis_weight          # points per final visible face
        self.komi4 = komi4                    # 4P: bonus for the last seat

    def label(self):
        return (f"nb={self.neutral_bank},coo={self.cover_own_only},"
                f"hound={self.hound_mode},mask={self.mask_req},"
                f"ash={self.ash_mode},tie={self.tie_mode},loy={self.loyalist},"
                f"coin={self.coin_req},komi={self.komi_p1},"
                f"wh={self.whisper_req},ve={self.veil_req},cr={self.crown_req},"
                f"ma={self.mask_ability},ag={self.ash_gap},"
                f"vf={self.veil_flip},hf={self.hound_flip},"
                f"hr={self.hound_req},hm={self.hound_move},kr={self.key_reach},"
                f"cp={self.coin_place},vw={self.vis_weight},k4={self.komi4}")


# ---------------------------------------------------------------- game state
class Game:
    __slots__ = ("grid", "deck", "piles", "removed", "np", "cur", "rng", "var",
                 "owner", "first_ext", "last_ext")

    def __init__(self, n_players, rng, var, owner=None):
        self.np = n_players
        self.rng = rng
        self.var = var
        self.grid = [None] * 9                 # cell -> (cid, up) or None
        self.deck = list(range(36))
        rng.shuffle(self.deck)
        self.piles = [[] for _ in range(n_players)]   # (cid, sym)
        self.removed = []
        self.cur = 0
        self.first_ext = None
        self.last_ext = None
        if owner is None:
            owner = draft_random(n_players, rng)
        self.owner = owner                     # symbol -> player | -1

    def clone(self):
        g = object.__new__(Game)
        g.np = self.np
        g.rng = self.rng
        g.var = self.var
        g.grid = list(self.grid)
        g.deck = list(self.deck)
        g.piles = [list(p) for p in self.piles]
        g.removed = list(self.removed)
        g.cur = self.cur
        g.first_ext = self.first_ext
        g.last_ext = self.last_ext
        g.owner = self.owner                   # immutable per game
        return g

    def empties(self):
        return [c for c in range(9) if self.grid[c] is None]

    def occupied(self):
        return [c for c in range(9) if self.grid[c] is not None]

    def pts(self, p):
        return len(self.piles[p])

    def vis(self, p):
        return sum(1 for e in self.grid if e is not None
                   and self.owner[face(*e)] == p)

    def total(self, p):
        k = self.var.komi_p1 if (p == 0 and self.np == 2) else 0
        if self.np == 4 and p == 3:
            k += self.var.komi4
        return self.pts(p) + self.var.vis_weight * self.vis(p) + k


def draft_random(n_players, rng):
    syms = list(range(9))
    rng.shuffle(syms)
    owner = [-1] * 9
    per = {2: 4, 3: 3, 4: 2}[n_players]
    i = 0
    for p in range(n_players):
        for _ in range(per):
            owner[syms[i]] = p
            i += 1
    return owner


# ---------------------------------------------------------------- stats
class Stats:
    def __init__(self):
        self.d = defaultdict(float)
        self.anomalies = 0
        self.per_player_acts = None

    def inc(self, k, v=1):
        self.d[k] += v


# ---------------------------------------------------------------- rules core
def _alleg(g, cell):
    """Allegiance (owner index or -1) of the face-up symbol at cell."""
    return g.owner[face(*g.grid[cell])]


def req_met(g, cell, P):
    """Requirement of the card at `cell`, evaluated for active player P."""
    cid, up = g.grid[cell]
    s = face(cid, up)
    nbrs = NEI[cell]
    occn = [n for n in nbrs if g.grid[n] is not None]
    if s == BLADE:
        return any(0 <= _alleg(g, n) != P for n in occn)
    if s == MASK:
        if g.var.mask_req == "any":
            return len(occn) >= 1
        rivals = sum(1 for n in occn if 0 <= _alleg(g, n) != P)
        if g.var.mask_req == "rival2":
            return rivals >= 2
        return rivals >= 1
    if s == WHISPER:
        if g.var.whisper_req == "eq1":
            return len(occn) == 1
        return len(occn) <= 1
    if s == COIN:
        if g.var.coin_req == "one_any":
            return len(occn) >= 1
        if g.var.coin_req == "two_any":
            return len(occn) >= 2
        al = [_alleg(g, n) for n in occn]
        return any(al.count(a) >= 2 for a in set(al))
    if s == VEIL:
        if g.var.veil_req == "rival":
            return any(0 <= _alleg(g, n) != P for n in occn)
        return any(_alleg(g, n) == P for n in occn)
    if s == KEY:
        r, c = LINE_OF[cell]
        for line in (r, c):
            k = sum(1 for x in line if g.grid[x] is not None
                    and _alleg(g, x) == P)
            if k >= 2:
                return True
        return False
    if s == HOUND:
        hi = 1 if g.var.hound_req == "1" else 2
        return 1 <= len(occn) <= hi
    if s == CROWN:
        need = 1 if g.var.crown_req == "own1" else 2
        return sum(1 for n in occn if _alleg(g, n) == P) >= need
    if s == ASH:
        mine = g.pts(P)
        return any(g.pts(q) >= mine + g.var.ash_gap
                   for q in range(g.np) if q != P)
    raise AssertionError


def _snapshot(g, P):
    d = {}
    for c in range(9):
        e = g.grid[c]
        if e is not None:
            d[e[0]] = req_met(g, c, P)
    return d


def _prime_transitions(g, ctx, pre, P):
    for c in range(9):
        e = g.grid[c]
        if e is None:
            continue
        cid = e[0]
        now = req_met(g, c, P)
        if now and not pre.get(cid, False):
            ctx.primed.add(cid)


class Ctx:
    __slots__ = ("primed", "activated")

    def __init__(self):
        self.primed = set()
        self.activated = set()


def extract_to(g, ctx, stats, cid, sym, dest_player, kind):
    """Card (already off-grid) scores for dest_player (or removed if -1)."""
    if dest_player >= 0:
        g.piles[dest_player].append((cid, sym))
        if g.first_ext is None:
            g.first_ext = dest_player
        g.last_ext = dest_player
        stats.inc(("banked_as", sym))
        stats.inc(kind)
    else:
        g.removed.append(cid)
        stats.inc(kind + "_neutral")
    ctx.activated.add(cid)   # off-board cards never act


def place_card(g, ctx, player, cid, cell, up, bots, stats, depth):
    """Step 2: place (cover if occupied), then prime the new card."""
    pre = _snapshot(g, player)
    if g.grid[cell] is not None:
        ocid, oup = g.grid[cell]
        sym = face(ocid, oup)
        ow = g.owner[sym]
        if ow < 0 and g.var.neutral_bank == "active":
            ow = player
        g.grid[cell] = None
        extract_to(g, ctx, stats, ocid, sym, ow, "cover_ext")
        stats.inc("covers")
    g.grid[cell] = (cid, up)
    ctx.primed.add(cid)
    if req_met(g, cell, player):
        stats.inc(("reqmet", face(cid, up)))
    _prime_transitions(g, ctx, pre, player)
    resolve(g, ctx, player, bots, stats, depth)


def legal_placements(g, player):
    out = []
    for cell in range(9):
        e = g.grid[cell]
        if e is None:
            out.append(cell)
        else:
            if g.var.cover_own_only:
                a = _alleg(g, cell)
                if a == player or a == -1:
                    out.append(cell)
            else:
                out.append(cell)
    if not out:
        out = list(range(9))   # cannot legally place: cover anything
    return out


def ability_candidates(g, cell, P):
    cid, up = g.grid[cell]
    s = face(cid, up)
    nbrs = NEI[cell]
    occn = [n for n in nbrs if g.grid[n] is not None]
    if s == BLADE:
        return [("remove", n) for n in occn if 0 <= _alleg(g, n) != P]
    if s == MASK:
        if g.var.mask_ability == "line":
            r, c = LINE_OF[cell]
            zone = set(r) | set(c)
            return [("flip", x) for x in g.occupied() if x in zone and x != cell]
        return [("flip", x) for x in g.occupied()]
    if s == WHISPER:
        return [("flip", n) for n in occn]
    if s == COIN:
        return [("coin",)] if g.deck else []
    if s == VEIL:
        out = [("swap", cell, o) for o in g.occupied() if o != cell]
        if g.var.veil_flip:
            out += [("swapflip", cell, o) for o in g.occupied() if o != cell]
        return out
    if s == KEY:
        if g.var.key_reach == "line":
            r, c = LINE_OF[cell]
            zone = (set(r) | set(c)) - {cell}
            return [("extract", x) for x in zone
                    if g.grid[x] is not None and _alleg(g, x) == P]
        return [("extract", n) for n in occn if _alleg(g, n) == P]
    if s == HOUND:
        if g.var.hound_mode == "adj_swap":
            return [("swap", n, m) for i, n in enumerate(occn)
                    for m in occn[i + 1:]]
        emp = g.empties()
        if g.var.hound_move == "line":
            r, c = LINE_OF[cell]
            zone = set(r) | set(c)
            emp = [e for e in emp if e in zone]
        out = [("move", n, e) for n in occn for e in emp]
        if g.var.hound_flip:
            out += [("moveflip", n, e) for n in occn for e in emp]
        return out
    if s == CROWN:
        return [("self_extract", cell)]
    if s == ASH:
        if g.var.ash_mode == "gain":
            return [("ash_gain",)] if g.deck else []
        mine = g.pts(P)
        return [("burn", q, cid) for q in range(g.np)
                if q != P and g.pts(q) >= mine + g.var.ash_gap
                and g.piles[q]]
    raise AssertionError


def apply_action(g, ctx, player, action, bots, stats, depth):
    kind = action[0]
    pre = _snapshot(g, player)
    if kind == "flip":
        c = action[1]
        cid, up = g.grid[c]
        g.grid[c] = (cid, 1 - up)
        ctx.primed.add(cid)
        stats.inc("flips")
    elif kind == "remove":
        c = action[1]
        cid, up = g.grid[c]
        g.grid[c] = None
        g.removed.append(cid)
        ctx.activated.add(cid)
        stats.inc("blade_removals")
    elif kind == "swap":
        a, b = action[1], action[2]
        g.grid[a], g.grid[b] = g.grid[b], g.grid[a]
        ctx.primed.add(g.grid[a][0])
        ctx.primed.add(g.grid[b][0])
    elif kind == "move":
        src, dst = action[1], action[2]
        g.grid[dst] = g.grid[src]
        g.grid[src] = None
        ctx.primed.add(g.grid[dst][0])
    elif kind == "moveflip":
        src, dst = action[1], action[2]
        cid2, up2 = g.grid[src]
        g.grid[src] = None
        g.grid[dst] = (cid2, 1 - up2)
        ctx.primed.add(cid2)
        stats.inc("flips")
    elif kind == "swapflip":
        a, b = action[1], action[2]
        g.grid[a], g.grid[b] = g.grid[b], g.grid[a]
        cid2, up2 = g.grid[a]          # the displaced card, now at Veil's old post
        g.grid[a] = (cid2, 1 - up2)
        ctx.primed.add(g.grid[b][0])
        ctx.primed.add(cid2)
        stats.inc("flips")
    elif kind == "extract":
        c = action[1]
        cid, up = g.grid[c]
        sym = face(cid, up)
        g.grid[c] = None
        extract_to(g, ctx, stats, cid, sym, g.owner[sym], "key_ext")
    elif kind == "self_extract":
        c = action[1]
        cid, up = g.grid[c]
        sym = face(cid, up)
        g.grid[c] = None
        extract_to(g, ctx, stats, cid, sym, g.owner[sym], "crown_ext")
    elif kind == "burn":
        q = action[1]
        bcid, bsym = g.piles[q].pop()
        g.removed.append(bcid)
        stats.inc("ash_burns")
        if g.var.ash_mode == "sacrifice":
            for c in range(9):
                e = g.grid[c]
                if e is not None and e[0] == action[2]:
                    g.grid[c] = None
                    g.removed.append(e[0])
                    ctx.activated.add(e[0])
                    break
    elif kind == "ash_gain":
        cid = g.deck.pop(0)
        g.piles[player].append((cid, None))
        if g.first_ext is None:
            g.first_ext = player
        g.last_ext = player
        stats.inc("ash_gains")
    elif kind == "coin":
        stats.inc("coin_plays")
        cid = g.deck.pop(0)
        if g.var.coin_place == "empty_only" and g.empties():
            cells = g.empties()
            best, bv = None, -1e18
            for cell in cells:
                for up in (0, 1):
                    g2 = g.clone()
                    g2.grid[cell] = (cid, up)
                    v = bots[player].eval(g2, player) \
                        if hasattr(bots[player], "eval") else 0
                    if v > bv or best is None:
                        best, bv = (cell, up), v
            cell, up = best
        else:
            cell, up = bots[player].choose_placement(g, ctx, player, cid)
        place_card(g, ctx, player, cid, cell, up, bots, stats, depth + 1)
        return
    else:
        raise AssertionError(kind)
    _prime_transitions(g, ctx, pre, player)


def resolve(g, ctx, player, bots, stats, depth):
    if depth > 50:
        stats.anomalies += 1
        return
    guard = 0
    while True:
        guard += 1
        if guard > 200:
            stats.anomalies += 1
            return
        opts = []
        for cell in range(9):
            e = g.grid[cell]
            if e is None:
                continue
            cid = e[0]
            if cid in ctx.primed and cid not in ctx.activated \
                    and req_met(g, cell, player):
                if g.var.loyalist and _alleg(g, cell) != player:
                    continue
                for a in ability_candidates(g, cell, player):
                    opts.append((cell, a))
        if not opts:
            return
        pick = bots[player].choose_action(g, ctx, player, opts)
        if pick is None:
            return
        cell, action = pick
        cid = g.grid[cell][0]
        ctx.activated.add(cid)
        s = face(*g.grid[cell])
        stats.inc(("activ", s))
        if stats.per_player_acts is not None:
            stats.per_player_acts[player][s] += 1
        stats.inc(("turn_acts",))
        apply_action(g, ctx, player, action, bots, stats, depth)


def play_turn(g, bots, stats):
    """Returns False when the game is over."""
    if not g.deck:
        return False
    player = g.cur
    ctx = Ctx()
    cid = g.deck.pop(0)
    stats.d[("turn_acts",)] = 0
    cell, up = bots[player].choose_placement(g, ctx, player, cid)
    stats.inc(("placed", face(cid, up)))
    place_card(g, ctx, player, cid, cell, up, bots, stats, 0)
    acts = stats.d[("turn_acts",)]
    stats.inc(("acts_hist", min(int(acts), 2)))
    stats.inc("turns")
    g.cur = (g.cur + 1) % g.np
    return bool(g.deck)


def team_winners(g):
    ta = g.total(0) + g.total(2)
    tb = g.total(1) + g.total(3)
    if ta != tb:
        return [0, 2] if ta > tb else [1, 3]
    if g.first_ext is not None:
        return [0, 2] if g.first_ext in (0, 2) else [1, 3]
    return [0, 2]


def winners(g):
    if g.var.tie_mode == "team" and g.np == 4:
        return team_winners(g)
    totals = [g.total(p) for p in range(g.np)]
    best = max(totals)
    lead = [p for p in range(g.np) if totals[p] == best]
    if len(lead) == 1:
        return lead
    m = g.var.tie_mode
    if m == "last_ext":
        if g.last_ext in lead:
            return [g.last_ext]
        return [min(lead)]
    if m == "pile":
        bp = max(g.pts(p) for p in lead)
        lead2 = [p for p in lead if g.pts(p) == bp]
        if len(lead2) == 1:
            return lead2
        if g.first_ext in lead2:
            return [g.first_ext]
        return [min(lead2)]
    if m == "first_ext":
        if g.first_ext in lead:
            return [g.first_ext]
        return [min(lead)]
    if m == "seat":
        return [min(lead)]
    return lead


# ---------------------------------------------------------------- bots
class RandomBot:
    def __init__(self, rng):
        self.rng = rng

    def choose_placement(self, g, ctx, player, cid):
        cell = self.rng.choice(legal_placements(g, player))
        return cell, self.rng.randrange(2)

    def choose_action(self, g, ctx, player, opts):
        if self.rng.random() < 0.15:
            return None
        return self.rng.choice(opts)


class GreedyBot:
    """One-ply: evaluate every (cell, face) placement with a greedy ability
    rollout; during real resolution pick the best immediate action or stop."""
    CAP = 12
    THRESH = 0.5

    def __init__(self, rng):
        self.rng = rng

    # ----- evaluation -----
    def eval(self, g, me):
        riv_pts = max((g.pts(q) for q in range(g.np) if q != me), default=0)
        riv_vis = max((g.vis(q) for q in range(g.np) if q != me), default=0)
        v = 1000.0 * (g.pts(me) - riv_pts)
        v += 330.0 * g.vis(me) - 330.0 * riv_vis
        v += 12.0 * len(g.empties())
        pairs = 0
        for a in range(9):
            ea = g.grid[a]
            if ea is None or g.owner[face(*ea)] != me:
                continue
            for b in NEI[a]:
                if b > a:
                    eb = g.grid[b]
                    if eb is not None and g.owner[face(*eb)] == me:
                        pairs += 1
        v += 24.0 * pairs
        v += self.rng.random() * 0.01
        return v

    # ----- helpers -----
    def _rollout(self, g, player, max_steps=6):
        """Greedy ability rollout on a cloned game (no further coin draws)."""
        ctx = Ctx()
        ctx.primed = set(self._roll_primed)
        ctx.activated = set(self._roll_activated)
        # note: caller seeds primed/activated copies before invoking
        steps = 0
        while steps < max_steps:
            steps += 1
            best, bv = None, self.eval(g, player) + self.THRESH
            opts = []
            for cell in range(9):
                e = g.grid[cell]
                if e is None:
                    continue
                cidx = e[0]
                if cidx in ctx.primed and cidx not in ctx.activated \
                        and req_met(g, cell, player):
                    cands = ability_candidates(g, cell, player)
                    if len(cands) > self.CAP:
                        cands = self.rng.sample(cands, self.CAP)
                    opts.extend((cell, a) for a in cands)
            for cell, a in opts:
                if a[0] == "coin":
                    continue
                g2 = g.clone()
                c2 = Ctx()
                c2.primed = set(ctx.primed)
                c2.activated = set(ctx.activated)
                st = Stats()
                cid2 = g2.grid[cell][0]
                c2.activated.add(cid2)
                apply_action(g2, c2, player, a, None, st, 0)
                v = self.eval(g2, player)
                if v > bv:
                    best, bv = (cell, a, g2, c2), v
            if best is None:
                return g
            _, _, g, ctx = best
        return g

    # ----- decisions -----
    def choose_placement(self, g, ctx, player, cid):
        best, bv = None, -1e18
        cells = legal_placements(g, player)
        for cell in cells:
            for up in (0, 1):
                g2 = g.clone()
                c2 = Ctx()
                c2.primed = set(ctx.primed)
                c2.activated = set(ctx.activated)
                st = Stats()
                # placement without recursive resolve (bots=None blocks coin)
                pre = _snapshot(g2, player)
                if g2.grid[cell] is not None:
                    ocid, oup = g2.grid[cell]
                    sym = face(ocid, oup)
                    ow = g2.owner[sym]
                    if ow < 0 and g2.var.neutral_bank == "active":
                        ow = player
                    g2.grid[cell] = None
                    extract_to(g2, c2, st, ocid, sym, ow, "x")
                g2.grid[cell] = (cid, up)
                c2.primed.add(cid)
                _prime_transitions(g2, c2, pre, player)
                self._roll_primed = c2.primed
                self._roll_activated = c2.activated
                g3 = self._rollout(g2.clone(), player)
                v = self.eval(g3, player)
                if v > bv:
                    best, bv = (cell, up), v
        return best

    def choose_action(self, g, ctx, player, opts):
        base = self.eval(g, player)
        best, bv = None, base + self.THRESH
        if len(opts) > 2 * self.CAP:
            opts = self.rng.sample(opts, 2 * self.CAP)
        for cell, a in opts:
            if a[0] == "coin":
                # value an extra play optimistically as half a banked card
                v = base + 450.0
                if v > bv:
                    best, bv = (cell, a), v
                continue
            g2 = g.clone()
            c2 = Ctx()
            c2.primed = set(ctx.primed)
            c2.activated = set(ctx.activated)
            st = Stats()
            cid2 = g2.grid[cell][0]
            c2.activated.add(cid2)
            apply_action(g2, c2, player, a, None, st, 0)
            v = self.eval(g2, player)
            if v > bv:
                best, bv = (cell, a), v
        return best


BOTS = {"random": RandomBot, "greedy": GreedyBot}


# ---------------------------------------------------------------- experiments
def run_games(n_players, kinds, n_games, seed, var):
    agg = {
        "games": 0, "turns": 0.0, "banked": 0.0, "covers": 0.0,
        "key_ext": 0.0, "crown_ext": 0.0, "blade_removals": 0.0,
        "ash_burns": 0.0, "ash_gains": 0.0, "coin_plays": 0.0,
        "flips": 0.0, "neutral_buried": 0.0,
        "zero_bank": 0, "ties": 0, "margin": 0.0,
        "seat_wins": [0.0] * n_players,
        "kind_wins": defaultdict(float),
        "acts0": 0.0, "acts1": 0.0, "acts2": 0.0,
        "sym": {s: defaultdict(float) for s in range(9)},
        "own_win": defaultdict(float), "own_n": defaultdict(int),
        "final_vis": 0.0, "anomalies": 0,
        "pre_ties": 0, "fe_seat": [0] * n_players,
    }
    rng = random.Random(seed)
    for i in range(n_games):
        owner = draft_random(n_players, rng)
        g = Game(n_players, random.Random(seed * 100003 + i), var, owner)
        bots = [BOTS[k](random.Random(seed * 7 + i * 13 + j))
                for j, k in enumerate(kinds)]
        st = Stats()
        st.per_player_acts = [defaultdict(int) for _ in range(n_players)]
        while play_turn(g, bots, st):
            pass
        # conservation
        tot = (len(g.occupied()) + sum(len(p) for p in g.piles)
               + len(g.removed) + len(g.deck))
        assert tot == 36, (tot, i)
        agg["anomalies"] += st.anomalies
        agg["games"] += 1
        agg["turns"] += st.d["turns"]
        banked = sum(len(p) for p in g.piles)
        agg["banked"] += banked
        for k in ("covers", "key_ext", "crown_ext", "blade_removals",
                  "ash_burns", "ash_gains", "coin_plays", "flips"):
            agg[k] += st.d[k]
        agg["neutral_buried"] += st.d["cover_ext_neutral"]
        if banked == 0:
            agg["zero_bank"] += 1
        w = winners(g)
        totals0 = [g.total(p) for p in range(n_players)]
        b0 = max(totals0)
        if sum(1 for x in totals0 if x == b0) > 1:
            agg["pre_ties"] += 1
        if g.first_ext is not None:
            agg["fe_seat"][g.first_ext] += 1
        if len(w) > 1:
            agg["ties"] += 1
        share = 1.0 / len(w)
        for p in w:
            agg["seat_wins"][p] += share
            agg["kind_wins"][kinds[p]] += share
        for s in range(9):
            ow = owner[s]
            if ow >= 0:
                agg["own_n"][s] += 1
                if ow in w:
                    agg["own_win"][s] += share
        totals = sorted((g.total(p) for p in range(n_players)), reverse=True)
        agg["margin"] += totals[0] - totals[1]
        agg["final_vis"] += len(g.occupied())
        agg["acts0"] += st.d[("acts_hist", 0)]
        agg["acts1"] += st.d[("acts_hist", 1)]
        agg["acts2"] += st.d[("acts_hist", 2)]
        for s in range(9):
            agg["sym"][s]["placed"] += st.d[("placed", s)]
            agg["sym"][s]["activ"] += st.d[("activ", s)]
            agg["sym"][s]["banked"] += st.d[("banked_as", s)]
            agg["sym"][s]["reqmet"] += st.d[("reqmet", s)]
        # req-met-at-placement probe: cheap proxy collected during play would
        # require instrumentation in place_card; approximate post-hoc is skipped.
        wset = set(w)
        for p in range(n_players):
            for s in range(9):
                key = ("wl", s)
                d = st.per_player_acts[p][s]
                agg["sym"][s]["wl"] += d if p in wset else -d / max(1, n_players - 1)
    return agg


def report(agg, title, n_players):
    n = agg["games"]
    t = agg["turns"]
    print(f"\n=== {title} ({n} games) ===")
    print(f"avg turns/game: {agg['turns']/n:.1f}")
    print(f"avg banked cards/game: {agg['banked']/n:.1f}  "
          f"(covers: {agg['covers']/n:.1f}, key: {agg['key_ext']/n:.2f}, "
          f"crown: {agg['crown_ext']/n:.2f})")
    print(f"blade removals/game: {agg['blade_removals']/n:.2f}   "
          f"ash burns/game: {agg['ash_burns']/n:.2f}   "
          f"flips/game: {agg['flips']/n:.2f}   "
          f"coin plays/game: {agg['coin_plays']/n:.2f}")
    print(f"neutral cards buried/game: {agg['neutral_buried']/n:.2f}   "
          f"final grid cards: {agg['final_vis']/n:.1f}")
    print(f"zero-bank games: {100*agg['zero_bank']/n:.1f}%   "
          f"ties: {100*agg['ties']/n:.1f}%   "
          f"avg margin: {agg['margin']/n:.2f}")
    seats = "  ".join(f"P{p+1}:{100*agg['seat_wins'][p]/n:.1f}%"
                      for p in range(n_players))
    print(f"seat win rates: {seats}")
    fes = "  ".join(f"P{p+1}:{100*agg['fe_seat'][p]/n:.0f}%"
                    for p in range(n_players))
    print(f"pre-tiebreak shared-top: {100*agg['pre_ties']/n:.1f}%   "
          f"first-extractor by seat: {fes}")
    for k, v in sorted(agg["kind_wins"].items()):
        if len(set(agg["kind_wins"])) > 1:
            print(f"  bot '{k}': per-seat win share {100*v/n:.1f}%")
    a0, a1, a2 = agg["acts0"], agg["acts1"], agg["acts2"]
    tot_acts = sum(agg["sym"][s]["activ"] for s in range(9))
    print(f"activations/turn: avg {tot_acts/t:.2f} | "
          f"0 acts {100*a0/t:.1f}% | 1 act {100*a1/t:.1f}% | "
          f"2+ acts {100*a2/t:.1f}%")
    print(f"\n{'guild':<9}{'placed%':>9}{'req-met%':>10}{'activ/game':>12}"
          f"{'banked-as/game':>16}{'owned-win%':>12}{'win-lose act':>14}")
    tp = sum(agg["sym"][s]["placed"] for s in range(9))
    for s in range(9):
        d = agg["sym"][s]
        ow = (100 * agg["own_win"][s] / agg["own_n"][s]
              if agg["own_n"][s] else 0.0)
        rm = 100 * d['reqmet'] / d['placed'] if d['placed'] else 0.0
        print(f"{NAMES[s]:<9}{100*d['placed']/tp:>8.1f}%{rm:>9.1f}%"
              f"{d['activ']/n:>12.2f}{d['banked']/n:>16.2f}"
              f"{ow:>11.1f}%{d['wl']/n:>+14.2f}")
    if agg["anomalies"]:
        print(f"!! anomalies: {agg['anomalies']}")


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
        tot = (len(g.occupied()) + sum(len(p) for p in g.piles)
               + len(g.removed) + len(g.deck))
        assert tot == 36, (tot, i)
        assert not g.deck
        assert st.anomalies == 0
    print("smoke OK: card conservation, termination, no anomalies (20 games)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("suites", nargs="*", default=["sanity"])
    ap.add_argument("--games", type=int, default=400)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--neutral-bank", default="removed",
                    choices=["removed", "active"])
    ap.add_argument("--cover-own-only", action="store_true")
    ap.add_argument("--hound", default="to_empty",
                    choices=["to_empty", "adj_swap"])
    ap.add_argument("--mask-req", default="rival", choices=["rival", "any", "rival2"])
    ap.add_argument("--ash", default="burn", choices=["burn", "gain", "sacrifice"])
    ap.add_argument("--tie-mode", default="last_ext",
                    choices=["first_ext", "shared", "seat", "pile", "last_ext", "team"])
    ap.add_argument("--loyalist", action="store_true")
    ap.add_argument("--coin-req", default="two_any", choices=["pair", "two_any", "one_any"])
    ap.add_argument("--komi", type=int, default=0)
    ap.add_argument("--whisper-req", default="le1", choices=["le1", "eq1"])
    ap.add_argument("--veil-req", default="own", choices=["own", "rival"])
    ap.add_argument("--crown-req", default="own1", choices=["own2", "own1"])
    ap.add_argument("--mask-ability", default="line", choices=["any", "line"])
    ap.add_argument("--ash-gap", type=int, default=2)
    ap.add_argument("--veil-flip", action="store_true", default=True)
    ap.add_argument("--hound-flip", action="store_true", default=True)
    ap.add_argument("--hound-req", default="1", choices=["12", "1"])
    ap.add_argument("--hound-move", default="any", choices=["any", "line"])
    ap.add_argument("--key-reach", default="line", choices=["adj", "line"])
    ap.add_argument("--coin-place", default="any", choices=["any", "empty_only"])
    ap.add_argument("--vis-weight", type=int, default=2)
    ap.add_argument("--komi4", type=float, default=0)
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    if args.smoke:
        smoke()
        return
    var = Var(neutral_bank=args.neutral_bank,
              cover_own_only=args.cover_own_only, hound_mode=args.hound,
              mask_req=args.mask_req, ash_mode=args.ash,
              tie_mode=args.tie_mode, loyalist=args.loyalist,
              coin_req=args.coin_req, komi_p1=args.komi,
              whisper_req=args.whisper_req, veil_req=args.veil_req,
              crown_req=args.crown_req, mask_ability=args.mask_ability,
              ash_gap=args.ash_gap, veil_flip=args.veil_flip,
              hound_flip=args.hound_flip, hound_req=args.hound_req,
              hound_move=args.hound_move, key_reach=args.key_reach,
              coin_place=args.coin_place, vis_weight=args.vis_weight,
              komi4=args.komi4)
    for s in args.suites:
        suite(s, var, args.games, args.seed)


if __name__ == "__main__":
    main()
