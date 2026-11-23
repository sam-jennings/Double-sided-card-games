#!/usr/bin/env python3
"""WISP v0.1 floor simulator.

Models the v0.1 rulebook: the Wisp holds 12 roads (the hunters know them by
complement with the 24-card atlas); each move lays a road showing the place
left and pressing the place reached; a sprint lays two chained roads as one
packet, hiding the intermediate place; after each Wisp turn the hunters may
spend one of their Raids naming a place; the Wisp escapes on surviving the
turn its trail reaches the escape length; it is cornered if it holds no road
from its current place.

Hunters reason exactly: they track every history consistent with what the
table shows (each shown face confirms the previous position; a sprint hides
one intermediate; a missed Raid rules out that place for that turn).

Bots
  Wisp   RandomWisp  random legal move; sprints 25% of the time when able.
         SkilledWisp never walks into a dead end (exact lookahead: a full
                     escape route must remain from the new place), then picks
                     the move whose true place is least likely in the hunters'
                     candidate set; sprints when a normal move would leave its
                     place at >= 50% likelihood.
  Hunter RandomHunter raids half the time, naming a random place.
         SkilledHunter raids the most likely place when it is >= 50% likely,
                     or when its remaining Raids >= the Wisp turns left before
                     escape (use them or lose them); candidates weighted by
                     consistent histories, excluding histories that corner the
                     Wisp before escape (a careful Wisp avoids them).

Dark variant (--dark): the 24 leftover roads are squared away unseen, so the
hunters do not know the Wisp's hand. Their worlds are then every history
consistent with the trail using ANY unplayed road (all 36 minus those played),
and each world is weighted by how many of the hands the Wisp could hold are
consistent with it AND keep the Wisp alive (the analogue of the open game's
"a careful Wisp is not cornered" pruning). Every world at a given moment has
the same number of played roads k, so the count of hands containing its
played roads, C(36-k, hand-k), is the same for all of them; only the
survival factor differs. Two ways to compute that factor:
  --prune exit1 (default)  exact probability, over every hand consistent with
                           the world, that the Wisp holds at least one onward
                           road from its current place (hypergeometric).
                           Approximation: one-step survival, not the full
                           escape route the open-mode pruning uses.
  --prune mc               Monte Carlo estimate of the full-escape-route
                           probability (--mc-samples hands per world); slow,
                           used to validate exit1 on smaller runs.

Usage:  python wisp_sim.py --games 2000 --seed 1
        python wisp_sim.py --dark --games 2000 --seed 1 --configs 12/4/8/2,12/3/8/2
"""

from __future__ import annotations

import argparse
import random
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb

DECK = [frozenset(p) for p in combinations(range(1, 10), 2)]
ALL = frozenset(DECK)


def path_exists(place, hand, need):
    """Uncached can_escape for sampled hands (keeps the lru_cache small)."""
    if need <= 0:
        return True
    for c in hand:
        if place in c and path_exists(other(c, place), hand - {c}, need - 1):
            return True
    return False


def other(card, s):
    (o,) = card - {s}
    return o


@lru_cache(maxsize=None)
def can_escape(place, hand, need):
    """Can a Wisp at `place` holding frozenset `hand` lay `need` more cards?"""
    if need <= 0:
        return True
    for c in hand:
        if place in c and can_escape(other(c, place), hand - {c}, need - 1):
            return True
    return False


class Game:
    def __init__(self, rng, wisp, hunter, hand=12, raids=4, escape=8, sprints=2,
                 dark=False, prune="exit1", mc_samples=200):
        self.rng, self.wisp, self.hunter = rng, wisp, hunter
        deck = DECK[:]
        rng.shuffle(deck)
        self.hand = frozenset(deck[:hand])          # true hand (public by complement)
        self.full = self.hand
        self.hand_size = hand
        # Dark: hunters only know a road is unplayed, not that the Wisp holds it.
        self.dark, self.prune, self.mc_samples = dark, prune, mc_samples
        self.universe = ALL if dark else self.full
        self._wcache = {}
        # separate stream for MC weights; created only in Dark so the open game's RNG use is unchanged
        self._mcrng = random.Random(rng.random()) if dark and prune == "mc" else None
        self.raids, self.escape, self.sprints = raids, escape, sprints
        self.trail = 0
        self.place = None
        # hunters' consistent worlds: set of (played frozenset, current place)
        self.worlds = None

    # --- possible moves from a world -----------------------------------
    def moves_from(self, played, place, sprint_ok, universe=None):
        rest = (self.full if universe is None else universe) - played
        if place is None:  # first move: any card, either face shown
            for c in rest:
                for s in c:
                    yield ("step", s, c, None, other(c, s))
            return
        for c in rest:
            if place in c:
                mid = other(c, place)
                yield ("step", place, c, None, mid)
                if sprint_ok:
                    for c2 in rest - {c}:
                        if mid in c2:
                            yield ("sprint", place, c, c2, other(c2, mid))

    def update_worlds(self, kind, shown, sprint_ok_before):
        new = set()
        src = self.worlds if self.worlds is not None else {(frozenset(), None)}
        for played, cur in src:
            if cur is not None and cur != shown:
                continue
            start = None if cur is None else cur
            for k, s, c1, c2, end in self.moves_from(played, start, sprint_ok_before, self.universe):
                if k != kind or s != shown:
                    continue
                p2 = played | {c1} | ({c2} if c2 else set())
                new.add((p2, end))
        self.worlds = new

    def dark_weight(self, played, cur, need):
        """Share of the hands consistent with this world that keep the Wisp alive."""
        if need <= 0:
            return 1.0
        key = (played, cur, need)
        if key in self._wcache:
            return self._wcache[key]
        unplayed = ALL - played
        m = self.hand_size - len(played)            # unknown cards still in hand
        if self.prune == "exit1":
            d = sum(1 for c in unplayed if cur in c)
            n = len(unplayed)
            w = 1.0 - comb(n - d, m) / comb(n, m) if m > 0 else 0.0
        else:  # mc: full escape route over sampled consistent hands
            pool = list(unplayed)
            hits = sum(path_exists(cur, frozenset(self._mcrng.sample(pool, m)), need)
                       for _ in range(self.mc_samples))
            w = hits / self.mc_samples
        self._wcache[key] = w
        return w

    def candidates(self, prune=True):
        cnt = Counter()
        need = self.escape - self.trail
        if self.dark:
            for played, cur in self.worlds:
                w = self.dark_weight(played, cur, need) if prune else 1.0
                if w > 0:
                    cnt[cur] += w
            if not cnt:
                for _, cur in self.worlds:
                    cnt[cur] += 1
            return cnt
        for played, cur in self.worlds:
            if prune and need > 0 and not can_escape(cur, self.full - played, need):
                continue
            cnt[cur] += 1
        if not cnt:  # every history corners the Wisp: fall back to all
            for _, cur in self.worlds:
                cnt[cur] += 1
        return cnt

    def play(self):
        while True:
            hand_left = self.hand
            opts = list(self.moves_from(self.full - self.hand, self.place, self.sprints > 0))
            if not opts:
                return "cornered", self.trail
            kind, shown, c1, c2, end = self.wisp.choose(self, opts)
            if kind == "sprint":
                self.sprints -= 1
            sprint_ok_before = self.sprints + (1 if kind == "sprint" else 0) > 0
            self.hand = hand_left - {c1} - ({c2} if c2 else set())
            self.trail += 2 if kind == "sprint" else 1
            self.place = end
            self.update_worlds(kind, shown, sprint_ok_before)
            if self.raids > 0:
                target = self.hunter.raid(self)
                if target is not None:
                    self.raids -= 1
                    if target == self.place:
                        return "caught", self.trail
                    self.worlds = {w for w in self.worlds if w[1] != target}
            if self.trail >= self.escape:
                return "escaped", self.trail


class RandomWisp:
    def __init__(self, rng):
        self.rng = rng

    def choose(self, g, opts):
        sprints = [o for o in opts if o[0] == "sprint"]
        if sprints and self.rng.random() < 0.25:
            return self.rng.choice(sprints)
        steps = [o for o in opts if o[0] == "step"]
        return self.rng.choice(steps or opts)


class SkilledWisp:
    def __init__(self, rng):
        self.rng = rng

    def score(self, g, opt):
        kind, shown, c1, c2, end = opt
        hand = g.hand - {c1} - ({c2} if c2 else set())
        trail = g.trail + (2 if kind == "sprint" else 1)
        safe = can_escape(end, hand, g.escape - trail)
        # simulate the hunters' update to measure how exposed `end` is
        saved = g.worlds, g.trail
        g.trail = trail
        g.update_worlds(kind, shown, g.sprints > 0)
        cnt = g.candidates()
        g.worlds, g.trail = saved
        total = sum(cnt.values()) or 1
        exposure = cnt.get(end, 0) / total
        return safe, exposure

    def choose(self, g, opts):
        scored = [(self.score(g, o), self.rng.random(), o) for o in opts]
        safe = [s for s in scored if s[0][0]] or scored
        steps = [s for s in safe if s[2][0] == "step"]
        best_step = min(steps, key=lambda s: (s[0][1], s[1])) if steps else None
        if best_step is None or best_step[0][1] >= 0.5:
            sprints = [s for s in safe if s[2][0] == "sprint"]
            if sprints:
                best_sprint = min(sprints, key=lambda s: (s[0][1], s[1]))
                if best_step is None or best_sprint[0][1] < best_step[0][1]:
                    return best_sprint[2]
        return (best_step or min(safe, key=lambda s: (s[0][1], s[1])))[2]


class RandomHunter:
    def __init__(self, rng):
        self.rng = rng

    def raid(self, g):
        return self.rng.randint(1, 9) if self.rng.random() < 0.5 else None


class SkilledHunter:
    def __init__(self, rng, threshold=0.5):
        self.rng, self.threshold = rng, threshold

    def raid(self, g):
        cnt = g.candidates()
        total = sum(cnt.values())
        place, n = max(cnt.items(), key=lambda kv: (kv[1], self.rng.random()))
        turns_left = g.escape - g.trail  # Wisp turns still to come (at least this many raids possible)
        if n / total >= self.threshold or g.raids > turns_left:
            return place
        if g.trail >= g.escape:  # last chance
            return place
        return None


def run(games, wisp_kind, hunter_kind, seed, **dials):
    rng = random.Random(seed)
    W = {"R": RandomWisp, "S": SkilledWisp}
    H = {"R": RandomHunter, "S": SkilledHunter}
    res, lengths = Counter(), Counter()
    for _ in range(games):
        g = Game(rng, W[wisp_kind](rng), H[hunter_kind](rng), **dials)
        outcome, trail = g.play()
        res[outcome] += 1
        lengths[outcome] += trail
    return {k: res[k] / games for k in ("escaped", "caught", "cornered")}, {
        k: lengths[k] / res[k] for k in res}


def sweep(games, seed):
    print(f"\nDial sweep (Skilled Wisp v Skilled Hunter, plus skill checks) · {games} games per row\n")
    print(f"{'hand/raids/escape/sprints':<28}{'S v S escape':>13}{'S v R':>8}{'R v S':>8}{'R v R':>8}{'S v S cornered':>15}")
    for hand in (12, 14, 16):
        for raids in (1, 2, 3):
            for escape in (6, 7, 8):
                for sprints in (2, 3):
                    d = dict(hand=hand, raids=raids, escape=escape, sprints=sprints)
                    ss = run(games, "S", "S", seed, **d)[0]
                    sr = run(games, "S", "R", seed, **d)[0]
                    rs = run(games, "R", "S", seed, **d)[0]
                    rr = run(games, "R", "R", seed, **d)[0]
                    print(f"{hand}/{raids}/{escape}/{sprints:<20}{ss['escaped']:>13.1%}{sr['escaped']:>8.1%}"
                          f"{rs['escaped']:>8.1%}{rr['escaped']:>8.1%}{ss['cornered']:>15.1%}")


def dark_main(a):
    print(f"WISP Dark variant sim · {a.games} games per row · seed {a.seed} · prune {a.prune}"
          + (f" ({a.mc_samples} sampled hands per world)" if a.prune == "mc" else "") + "\n")
    print(f"{'dials (hand/raids/escape/sprints)':<36}{'Wisp v Hunter':<15}{'escaped':>8}{'caught':>8}{'cornered':>9}  mean trail when caught")
    pairs = [tuple(p.split("v")) for p in a.pairs.split(",")]
    for spec in a.configs.split(","):
        hand, raids, escape, sprints = map(int, spec.split("/"))
        d = dict(hand=hand, raids=raids, escape=escape, sprints=sprints,
                 dark=True, prune=a.prune, mc_samples=a.mc_samples)
        for w, h in pairs:
            r, ln = run(a.games, w, h, a.seed, **d)
            print(f"{spec:<36}{w + ' v ' + h:<15}{r['escaped']:>8.1%}{r['caught']:>8.1%}{r['cornered']:>9.1%}"
                  f"  {ln.get('caught', float('nan')):.1f}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--dark", action="store_true", help="Dark variant: hunters do not know the hand")
    ap.add_argument("--prune", choices=("exit1", "mc"), default="exit1")
    ap.add_argument("--mc-samples", type=int, default=200)
    ap.add_argument("--configs", default="12/4/8/2,12/1/8/2,12/2/8/2,12/3/8/2,12/3/7/3")
    ap.add_argument("--pairs", default="SvS,SvR,RvS,RvR")
    a = ap.parse_args()
    if a.dark:
        dark_main(a)
        return
    if a.sweep:
        sweep(a.games, a.seed)
        return
    print(f"WISP v0.1 sim · {a.games} games per row · seed {a.seed} · games end by rule within 12 cards (no cap needed)\n")
    print(f"{'dials (hand/raids/escape/sprints)':<36}{'Wisp v Hunter':<15}{'escaped':>8}{'caught':>8}{'cornered':>9}  mean trail when caught")
    configs = [dict(hand=12, raids=4, escape=8, sprints=2),   # v0.1 rulebook dials
               dict(hand=12, raids=1, escape=8, sprints=2),   # balanced at hand 12, one Raid
               dict(hand=12, raids=1, escape=7, sprints=3),
               dict(hand=14, raids=2, escape=7, sprints=3),
               dict(hand=14, raids=1, escape=8, sprints=3),
               dict(hand=16, raids=3, escape=8, sprints=3),
               dict(hand=16, raids=3, escape=7, sprints=3),
               dict(hand=16, raids=2, escape=8, sprints=3)]
    for d in configs:
        label = f"{d['hand']}/{d['raids']}/{d['escape']}/{d['sprints']}"
        pairs = (("S", "S"), ("S", "R"), ("R", "S"), ("R", "R"))
        for w, h in pairs:
            r, ln = run(a.games, w, h, a.seed, **d)
            print(f"{label:<36}{w + ' v ' + h:<15}{r['escaped']:>8.1%}{r['caught']:>8.1%}{r['cornered']:>9.1%}"
                  f"  {ln.get('caught', float('nan')):.1f}")


if __name__ == "__main__":
    main()
