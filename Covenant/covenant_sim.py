#!/usr/bin/env python3
"""COVENANT v0.1 -- The Loyalty Duel: trial and campaign simulator.

Models the rules in COVENANT_rulebook.md (v0.1). One trial = one chapter:

  * Chapter n (1..6) courts the newcomer sign S = n+3 (Flame, Eye, Mask, Key,
    Star, Crown). The won set W = signs 1..n+2, so k = n+2 strangers.
  * The strangers are the k cards pairing S with each sign in W, laid S-face up.
    Their pressed faces are a hidden permutation of W (every pair exactly once).
  * Your covenant = the C(k,2) cards with both signs in W. Opening hand H
    (chapter one: all 3 cards); the rest is the reserve, reachable only by powers.
  * Claim: play a hand card naming one of its signs at a stranger, flip the
    stranger. Hit -> the stranger is turned (won) and the claim card returns to
    hand. Miss -> the stranger stays flipped (unmasked: its true sign is now
    public), the claim card goes to Ash, and (strike rule) the top reserve card
    is ashed too.
  * Powers (chapter two onward; a won sign's card is spent to use its power):
      Moon  recover one card from Ash to hand
      Leaf  draw 2 from the reserve
      Wave  look at the top 3 of the reserve, take 1, rest to the bottom
      Flame burn a stranger (flip it, set it aside); the newcomer joins as a grudge
      Eye   unmask a stranger (flip it) at no other cost
      Mask  passive: a claim with a Mask-bearing card names BOTH its signs
      Key   turn an unmasked stranger without a matching card
      Star  passive: a Star-bearing card may claim any one sign
      Crown none in the solo campaign (Crown is the last sign to join)
  * The trial is lost when you hold no cards (or cannot act / concede).
  * Grudge toll: opening hand -1 per grudge carried (minimum 3).

Bots:
  RandomBot  -- uniform over every legal action (the mechanics floor).
  GreedyBot  -- the obvious line: claim unmasked strangers it can match; else
                guess a still-possible sign with a random card; powers only when
                stuck.
  SkilledBot -- card stewardship (risks the card whose loss hurts coverage
                least), Leaf for card advantage, Eye before blind guesses on
                long rows, Key/Moon/Wave to fix coverage, Flame only as a last
                resort on the final attempt.

Chapter one is also solved exactly (expectimax) to answer "does it contain any
real decision?".

Usage:
  python covenant_sim.py                 # full report, seed 2026, 2000 runs
  python covenant_sim.py --runs 1000 --seed 7
  python covenant_sim.py --scoping       # July 2026 blind-permutation scoping model
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

MOON, LEAF, WAVE, FLAME, EYE, MASK, KEY, STAR, CROWN = range(1, 10)
NAMES = {1: "Moon", 2: "Leaf", 3: "Wave", 4: "Flame", 5: "Eye",
         6: "Mask", 7: "Key", 8: "Star", 9: "Crown"}
TURN_CAP = 600


# --------------------------------------------------------------------------
# The trial
# --------------------------------------------------------------------------

class Trial:
    def __init__(self, chapter: int, rng: random.Random, hand_size: int = 5,
                 strike: bool = True, toll: int = 0):
        self.chapter = chapter
        self.S = chapter + 3
        self.W = list(range(1, chapter + 3))
        self.k = len(self.W)
        self.powers = set(self.W) if chapter >= 2 else set()
        self.strike = strike
        cov = list(combinations(self.W, 2))
        rng.shuffle(cov)
        base = self.k if hand_size == 0 else hand_size   # 0 = one card per stranger
        if chapter == 1:
            h = len(cov)
        else:
            h = min(len(cov), max(3, base - toll))
        self.hand: list[tuple[int, int]] = cov[:h]
        self.reserve: list[tuple[int, int]] = cov[h:]      # top = end
        perm = self.W[:]
        rng.shuffle(perm)
        self.true = perm                                    # stranger i's pressed sign
        self.status = ["M"] * self.k                        # M masked, U unmasked, T turned, B burned
        self.spent: list = []
        self.ash: list = []
        self.misses = 0
        self.burned = 0
        self.actions = 0

    # ---- views ----
    def masked(self):
        return [i for i, s in enumerate(self.status) if s == "M"]

    def unmasked(self):
        return [i for i, s in enumerate(self.status) if s == "U"]

    def unaccounted(self) -> set[int]:
        """Signs that could be under a masked stranger (burn and miss reveal)."""
        return set(self.W) - {self.true[i] for i, s in enumerate(self.status) if s != "M"}

    def needed(self) -> set[int]:
        return self.unaccounted() | {self.true[i] for i in self.unmasked()}

    def done(self) -> bool:
        return all(s in "TB" for s in self.status)

    def claim_options(self, card) -> list[frozenset]:
        opts = {frozenset([card[0]]), frozenset([card[1]])}
        if MASK in self.powers and MASK in card:
            opts.add(frozenset(card))
        if STAR in self.powers and STAR in card:
            opts |= {frozenset([x]) for x in self.W}
        return list(opts)

    def legal_actions(self):
        acts = []
        live = [i for i, s in enumerate(self.status) if s in "MU"]
        for ci, c in enumerate(self.hand):
            for named in self.claim_options(c):
                for i in live:
                    acts.append(("claim", i, ci, named))
            for p in c:
                if p not in self.powers:
                    continue
                if p == MOON and self.ash:
                    acts += [("moon", ci, ai) for ai in range(len(self.ash))]
                elif p == LEAF and self.reserve:
                    acts.append(("leaf", ci))
                elif p == WAVE and self.reserve:
                    acts.append(("wave", ci))
                elif p == FLAME:
                    acts += [("flame", ci, i) for i in live]
                elif p == EYE:
                    acts += [("eye", ci, i) for i in self.masked()]
                elif p == KEY:
                    acts += [("key", ci, i) for i in self.unmasked()]
        return acts

    def apply(self, act, picker):
        kind = act[0]
        if kind == "claim":
            _, i, ci, named = act
            card = self.hand.pop(ci)
            if self.true[i] in named:
                self.status[i] = "T"
                self.hand.append(card)
            else:
                self.status[i] = "U"
                self.ash.append(card)
                self.misses += 1
                if self.strike and self.reserve:
                    self.ash.append(self.reserve.pop())
            return
        card = self.hand.pop(act[1])
        self.spent.append(card)
        if kind == "moon":
            self.hand.append(self.ash.pop(act[2]))
        elif kind == "leaf":
            for _ in range(2):
                if self.reserve:
                    self.hand.append(self.reserve.pop())
        elif kind == "wave":
            top = [self.reserve.pop() for _ in range(min(3, len(self.reserve)))]
            j = picker(self, top)
            self.hand.append(top.pop(j))
            self.reserve[0:0] = top
        elif kind == "flame":
            self.status[act[2]] = "B"
            self.burned += 1
        elif kind == "eye":
            self.status[act[2]] = "U"
        elif kind == "key":
            self.status[act[2]] = "T"


# --------------------------------------------------------------------------
# Bots
# --------------------------------------------------------------------------

class RandomBot:
    name = "Random"

    def choose(self, tr, rng, last_attempt=True):
        acts = tr.legal_actions()
        return rng.choice(acts) if acts else None

    def pick(self, tr, cards, rng):
        return rng.randrange(len(cards))


def _sure_hit(tr):
    """A claim on an unmasked stranger with a card that can name its sign."""
    for i in tr.unmasked():
        t = tr.true[i]
        for ci, c in enumerate(tr.hand):
            for named in tr.claim_options(c):
                if t in named:
                    return ("claim", i, ci, named)
    return None


def _power_cards(tr, sign):
    return [ci for ci, c in enumerate(tr.hand) if sign in c and sign in tr.powers]


class GreedyBot:
    """The obvious line: use what the misses revealed, otherwise guess."""
    name = "Greedy"

    def choose(self, tr, rng, last_attempt=True):
        if not tr.hand:
            return None
        a = _sure_hit(tr)
        if a:
            return a
        U = tr.unaccounted()
        masked = tr.masked()
        if masked:
            opts = [(ci, named) for ci, c in enumerate(tr.hand)
                    for named in tr.claim_options(c) if len(named) == 1 and named & U]
            if opts:
                ci, named = rng.choice(opts)
                return ("claim", rng.choice(masked), ci, named)
        # stuck: powers in a fixed, unthinking order
        for p in (LEAF, WAVE, MOON, KEY, EYE, FLAME):
            for ci in _power_cards(tr, p):
                if p in (LEAF, WAVE) and tr.reserve:
                    return ("leaf" if p == LEAF else "wave", ci)
                if p == MOON and tr.ash:
                    return ("moon", ci, rng.randrange(len(tr.ash)))
                if p == KEY and tr.unmasked():
                    return ("key", ci, tr.unmasked()[0])
                if p == EYE and masked:
                    return ("eye", ci, masked[0])
                if p == FLAME and last_attempt:
                    live = [i for i, s in enumerate(tr.status) if s in "MU"]
                    return ("flame", ci, live[0])
        return None

    def pick(self, tr, cards, rng):
        N = tr.needed()
        good = [j for j, c in enumerate(cards) if set(c) & N]
        return rng.choice(good) if good else rng.randrange(len(cards))


class SkilledBot:
    """Card stewardship + sensible powers. Public information only."""
    name = "Skilled"

    def __init__(self, eye_u: int = 3):
        self.eye_u = eye_u

    def value(self, tr, card, hand=None):
        hand = tr.hand if hand is None else hand
        N = tr.needed()
        v = 0.0
        for x in card:
            if x in N:
                cover = sum(1 for c in hand if x in c)
                v += 1.0 / max(cover, 1)
        if STAR in tr.powers and STAR in card:
            v += 1.0
        if MASK in tr.powers and MASK in card:
            v += 0.5
        for p in card:
            if p in tr.powers and p in (LEAF, KEY, EYE, MOON, WAVE):
                v += 0.25
        return v

    def cheapest(self, tr, idxs):
        return min(idxs, key=lambda ci: self.value(tr, tr.hand[ci])) if idxs else None

    def choose(self, tr, rng, last_attempt=True):
        if not tr.hand:
            return None
        a = _sure_hit(tr)
        if a:
            return a
        U = tr.unaccounted()
        masked = tr.masked()
        unm = tr.unmasked()

        # Leaf is pure card advantage while the reserve can pay for it.
        leaf = self.cheapest(tr, _power_cards(tr, LEAF))
        if leaf is not None and len(tr.reserve) >= 2 and self.value(tr, tr.hand[leaf]) < 1.0:
            return ("leaf", leaf)

        # An unmasked stranger we cannot match: Key it, or dig for its sign.
        if unm:
            key = self.cheapest(tr, _power_cards(tr, KEY))
            if key is not None:
                return ("key", key, unm[0])
            need = {tr.true[i] for i in unm}
            moon = self.cheapest(tr, _power_cards(tr, MOON))
            if moon is not None:
                for ai, c in enumerate(tr.ash):
                    if set(c) & need:
                        return ("moon", moon, ai)

        # Eye before gambling on a long row.
        if masked and len(masked) >= self.eye_u:
            eye = self.cheapest(tr, _power_cards(tr, EYE))
            if eye is not None and len(tr.hand) >= 3 and self.value(tr, tr.hand[eye]) < 1.0:
                return ("eye", eye, masked[0])

        # Best guess: minimise the expected coverage lost on a miss.
        if masked:
            best = None
            strike_pen = 0.3 if (tr.strike and tr.reserve) else 0.0
            for ci, c in enumerate(tr.hand):
                for named in tr.claim_options(c):
                    hits = len(named & U)
                    if not hits:
                        continue
                    p = hits / len(masked)
                    rest = tr.hand[:ci] + tr.hand[ci + 1:]
                    loss = (1 - p) * (self.value(tr, c, rest + [c]) + strike_pen)
                    key = (loss, -p)
                    if best is None or key < best[0]:
                        best = (key, ci, named)
            if best:
                return ("claim", masked[0], best[1], best[2])

        # Stuck: fix coverage with whatever is left.
        for p in (WAVE, LEAF):
            ci = self.cheapest(tr, _power_cards(tr, p))
            if ci is not None and tr.reserve:
                return ("wave" if p == WAVE else "leaf", ci)
        moon = self.cheapest(tr, _power_cards(tr, MOON))
        if moon is not None and tr.ash:
            N = tr.needed()
            ai = max(range(len(tr.ash)), key=lambda j: len(set(tr.ash[j]) & N))
            return ("moon", moon, ai)
        eye = self.cheapest(tr, _power_cards(tr, EYE))
        if eye is not None and masked:
            return ("eye", eye, masked[0])
        flame = self.cheapest(tr, _power_cards(tr, FLAME))
        if flame is not None and last_attempt:
            live = [i for i, s in enumerate(tr.status) if s in "MU"]
            return ("flame", flame, live[0])
        return None

    def pick(self, tr, cards, rng):
        return max(range(len(cards)), key=lambda j: self.value(tr, cards[j], tr.hand + [cards[j]]))


# --------------------------------------------------------------------------
# Running trials and campaigns
# --------------------------------------------------------------------------

def play(chapter, bot, rng, hand_size, strike, toll=0, last_attempt=True):
    tr = Trial(chapter, rng, hand_size, strike, toll)
    picker = lambda t, cards: bot.pick(t, cards, rng)
    while not tr.done() and tr.actions < TURN_CAP:
        a = bot.choose(tr, rng, last_attempt)
        if a is None:
            break
        tr.apply(a, picker)
        tr.actions += 1
    if tr.actions >= TURN_CAP:
        res = "stall"
    elif tr.done():
        res = "grudge" if tr.burned else "clear"
    else:
        res = "fail"
    return res, tr


def chapter_stats(chapter, bot, runs, seed, hand_size, strike):
    rng = random.Random(seed)
    tally = {"clear": 0, "grudge": 0, "fail": 0, "stall": 0}
    lost = misses = acts = 0
    for _ in range(runs):
        res, tr = play(chapter, bot, rng, hand_size, strike, last_attempt=True)
        tally[res] += 1
        lost += len(tr.ash)
        misses += tr.misses
        acts += tr.actions
    return {"clear": tally["clear"] / runs, "grudge": tally["grudge"] / runs,
            "fail": tally["fail"] / runs, "stall": tally["stall"] / runs,
            "lost": lost / runs, "misses": misses / runs, "actions": acts / runs}


def campaign(bot, rng, hand_size, strike, retries=2):
    grudges = attempts = lost = 0
    for ch in range(1, 7):
        toll = grudges
        for att in range(retries + 1):
            last = att == retries
            res, tr = play(ch, bot, rng, hand_size, strike, toll, last)
            attempts += 1
            lost += len(tr.ash)
            if res == "clear":
                break
            if res == "grudge":
                grudges += 1
                break
        else:
            grudges += 1          # failed every hearing: joins as a grudge
    return grudges, attempts, lost


# --------------------------------------------------------------------------
# Chapter one, solved exactly
# --------------------------------------------------------------------------

def solve_chapter_one():
    """Expectimax over information states of chapter one (k=3, hand = all 3).

    State: (hand, unmasked signs awaiting a claim, unaccounted signs U).
    Masked strangers are interchangeable, so they collapse to |U|.
    Returns optimal / random / worst-sensible win probabilities and a count of
    decision states where a sensible (non-dominated-looking) choice matters.
    """
    W = (1, 2, 3)
    start_hand = tuple(sorted(combinations(W, 2)))

    def actions(hand, unm, U):
        """(label, sensible?, [(prob, next_state, miss)])"""
        out = []
        m = len(U)
        for ci, c in enumerate(hand):
            rest = hand[:ci] + hand[ci + 1:]
            for x in c:
                # claim an unmasked stranger
                for j, t in enumerate(unm):
                    unm2 = unm[:j] + unm[j + 1:]
                    if x == t:
                        out.append(((c, x, "U", t), True, [(1.0, (hand, unm2, U), 0)]))
                    else:
                        out.append(((c, x, "U", t), False, [(1.0, (rest, unm, U), 1)]))
                # claim a masked stranger
                if m:
                    branches = []
                    for y in U:   # true sign uniform over U
                        if y == x:
                            branches.append((1 / m, (hand, unm, U - {y}), 0))
                        else:
                            branches.append((1 / m, (rest, tuple(sorted(unm + (y,))), U - {y}), 1))
                    out.append(((c, x, "M"), x in U, branches))
        return out

    @lru_cache(maxsize=None)
    def V(hand, unm, U, mode):
        if not unm and not U:
            return 1.0
        if not hand:
            return 0.0
        vals = []
        for _, sensible, br in actions(hand, unm, U):
            if mode == "worst" and not sensible:
                continue
            vals.append(sum(p * V(*s, mode) for p, s, _ in br))
        if not vals:
            return 0.0
        if mode == "opt":
            return max(vals)
        if mode == "worst":
            return min(vals)
        return sum(vals) / len(vals)

    @lru_cache(maxsize=None)
    def M(hand, unm, U):
        """Expected misses under the optimal (win-maximising) policy."""
        if (not unm and not U) or not hand:
            return 0.0
        best = None
        for _, _, br in actions(hand, unm, U):
            v = sum(p * V(*s, "opt") for p, s, _ in br)
            e = sum(p * (mi + M(*s)) for p, s, mi in br)
            if best is None or (v, -e) > best:
                best = (v, -e)
        return -best[1]

    # Count decision states reachable under optimal play where a sensible
    # choice changes the win probability.
    seen, critical = set(), []

    def walk(hand, unm, U):
        st = (hand, unm, U)
        if st in seen or (not unm and not U) or not hand:
            return
        seen.add(st)
        acts = actions(hand, unm, U)
        vals = [(sum(p * V(*s, "opt") for p, s, _ in br), sensible, lab, br)
                for lab, sensible, br in acts]
        sens = [v for v in vals if v[1]]
        if sens and max(v[0] for v in sens) - min(v[0] for v in sens) > 1e-9:
            critical.append((st, max(v[0] for v in sens) - min(v[0] for v in sens)))
        bestv = max(v[0] for v in vals)
        for v, _, _, br in vals:
            if abs(v - bestv) < 1e-12:
                for _, s, _ in br:
                    walk(*s)
                break

    U0 = frozenset(W)
    walk(start_hand, (), U0)
    return {
        "opt": V(start_hand, (), U0, "opt"),
        "worst_sensible": V(start_hand, (), U0, "worst"),
        "random": V(start_hand, (), U0, "rand"),
        "opt_misses": M(start_hand, (), U0),
        "decision_states": len(seen),
        "critical_states": len(critical),
        "max_swing": max((c[1] for c in critical), default=0.0),
    }


# --------------------------------------------------------------------------
# July 2026 scoping model (blind permutation, no hand, no reveal) -- kept so
# the numbers in COVENANT_design_analysis.md stay reproducible.
# --------------------------------------------------------------------------

def scoping(trials=200_000):
    def random_legal(perm, rng):
        k = len(perm)
        placed, misses = set(), 0
        for a in range(k):
            tried = set()
            while True:
                g = rng.choice([s for s in range(k) if s not in placed and s not in tried])
                if g == perm[a]:
                    placed.add(g)
                    break
                tried.add(g)
                misses += 1
        return misses

    def deducer(perm, rng):
        """Full constraint propagation; gamble on the most-constrained attacker."""
        k = len(perm)
        cand = [set(range(k)) for _ in range(k)]
        placed = [False] * k
        misses = 0

        def place(a, s):
            placed[a] = True
            cand[a] = {s}
            for o in range(k):
                if o != a:
                    cand[o].discard(s)

        def propagate():
            changed = True
            while changed:
                changed = False
                for a in range(k):
                    if not placed[a] and len(cand[a]) == 1:
                        place(a, next(iter(cand[a])))
                        changed = True
                for s in range(k):
                    homes = [a for a in range(k) if not placed[a] and s in cand[a]]
                    if len(homes) == 1:
                        place(homes[0], s)
                        changed = True

        propagate()
        while not all(placed):
            a = min((x for x in range(k) if not placed[x]), key=lambda x: len(cand[x]))
            g = rng.choice(sorted(cand[a]))
            if g == perm[a]:
                place(a, g)
            else:
                cand[a].discard(g)
                misses += 1
            propagate()
        return misses

    print("COVENANT v.A -- blind permutation-match scoping (July 2026 model)\n")
    for k in range(4, 9):
        rng = random.Random(1000 + k)
        tot = dtot = 0
        for _ in range(trials):
            perm = list(range(k))
            rng.shuffle(perm)
            tot += random_legal(perm, rng)
            dtot += deducer(perm, rng)
        print(f"k={k} perms={factorial(k):>6,} random-legal misses={tot / trials:5.2f} "
              f"deducer misses={dtot / trials:5.2f} (closed form C(k,2)/2 = {comb(k, 2) / 2:.2f})")


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def report(runs, seed, hand_size, strike):
    bots = [RandomBot(), GreedyBot(), SkilledBot()]
    print(f"COVENANT v0.1 -- The Loyalty Duel | runs/config={runs} seed={seed} "
          f"hand={'one per stranger' if hand_size == 0 else hand_size} "
          f"strike={'on' if strike else 'off'}\n")

    print("1. Per chapter (one hearing, Flame allowed as a last resort)")
    print(f"{'ch':>2} {'newcomer':>8} {'k':>2} {'deck':>4} | {'bot':>7} | {'clear':>6} {'grudge':>6} "
          f"{'fail':>6} {'stall':>5} | {'lost':>5} {'miss':>5} {'acts':>5}")
    rows = {}
    for ch in range(1, 7):
        k = ch + 2
        for b in bots:
            s = chapter_stats(ch, b, runs, seed + 97 * ch, hand_size, strike)
            rows[(ch, b.name)] = s
            print(f"{ch:>2} {NAMES[ch + 3]:>8} {k:>2} {comb(k, 2):>4} | {b.name:>7} | "
                  f"{100 * s['clear']:5.1f}% {100 * s['grudge']:5.1f}% {100 * s['fail']:5.1f}% "
                  f"{100 * s['stall']:4.1f}% | {s['lost']:5.2f} {s['misses']:5.2f} {s['actions']:5.1f}")
        print()

    print("2. Skill gap per chapter (cards lost ratio, and clean-clear difference)")
    print(f"{'ch':>2} | {'Random/Skilled':>14} {'Greedy/Skilled':>14} | "
          f"{'clear R':>7} {'clear G':>7} {'clear S':>7}")
    for ch in range(1, 7):
        r, g, s = rows[(ch, "Random")], rows[(ch, "Greedy")], rows[(ch, "Skilled")]
        ratio = lambda a: (a["lost"] / s["lost"]) if s["lost"] > 0 else float("inf")
        print(f"{ch:>2} | {ratio(r):13.2f}x {ratio(g):13.2f}x | "
              f"{100 * r['clear']:6.1f}% {100 * g['clear']:6.1f}% {100 * s['clear']:6.1f}%")
    print()

    print("3. Chapter one solved exactly (no powers, 3 strangers, hand = all 3 cards)")
    c1 = solve_chapter_one()
    print(f"   optimal win {100 * c1['opt']:.1f}% | worst sensible play {100 * c1['worst_sensible']:.1f}% | "
          f"uniform random {100 * c1['random']:.1f}%")
    print(f"   optimal expected misses {c1['opt_misses']:.2f} | decision states on the optimal path "
          f"{c1['decision_states']} | states where a sensible choice changes the odds "
          f"{c1['critical_states']} (max swing {100 * c1['max_swing']:.1f} pts)")
    print()

    print("4. Campaign (6 chapters, up to 2 retries, then the newcomer joins as a grudge)")
    for b in bots:
        rng = random.Random(seed + 5000)
        G = A = L = 0
        dist = {}
        n = max(runs // 2, 1000)
        for _ in range(n):
            g, a, l = campaign(b, rng, hand_size, strike)
            G += g
            A += a
            L += l
            dist[g] = dist.get(g, 0) + 1
        top = ", ".join(f"{g}:{100 * c / n:.0f}%" for g, c in sorted(dist.items()))
        print(f"   {b.name:>7}: grudges {G / n:4.2f} | hearings {A / n:5.2f} (min 6) | "
              f"cards lost {L / n:5.1f} | grudge distribution {top}")
    print()


def sweep(runs, seed):
    print("5. Parameter sweep: Skilled vs Greedy, fail+grudge rate and cards lost, per chapter")
    print(f"{'hand':>4} {'strike':>6} | " + " | ".join(f"ch{c} S/G bad%  lostS/G" for c in range(2, 7)))
    for hs in (0, 4, 5, 6):   # 0 = one card per stranger (k)
        for st in (False, True):
            cells = []
            for ch in range(2, 7):
                s = chapter_stats(ch, SkilledBot(), runs, seed + 11 * ch, hs, st)
                g = chapter_stats(ch, GreedyBot(), runs, seed + 11 * ch, hs, st)
                cells.append(f"{100 * (1 - s['clear']):4.1f}/{100 * (1 - g['clear']):4.1f} "
                             f"{s['lost']:4.2f}/{g['lost']:4.2f}")
            print(f"{'k' if hs == 0 else hs:>4} {'on' if st else 'off':>6} | " + " | ".join(cells))
    print()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--hand", type=int, default=0, help="opening hand; 0 = one card per stranger")
    ap.add_argument("--no-strike", action="store_true")
    ap.add_argument("--scoping", action="store_true")
    ap.add_argument("--no-sweep", action="store_true")
    args = ap.parse_args()
    if args.scoping:
        scoping()
    else:
        report(args.runs, args.seed, args.hand, not args.no_strike)
        if not args.no_sweep:
            sweep(args.runs // 2, args.seed)
