#!/usr/bin/env python3
"""FORKED TONGUE v1.1 floor simulator.

Models the v1.1 rulebook: hands 8/7/6/5 at 3/4/5/6 players, the rest as the
public registry; a self-recording ledger (each card shows the previous claim);
play-and-claim (show the owed symbol, claim any other symbol as hidden);
decline (take the newest ledger card, the requirement rewinds one link);
"False face!" challenges with closest-to-the-claimant's-left priority, loser
takes the whole ledger, the player after the claimant opens fresh; and the
final-card win (survive the challenge window).

Bots
  RandomBot   plays a random legal card 85% of the time when it can (else
              declines), claims the truth half the time, challenges 15% of
              claims and 50% of final-card claims.
  SkilledBot  plays the strategy notes: shed whenever it can, claim the
              scarcest symbol (fewest cards it cannot account for) to steer
              the next player into a decline, lie only early ("lie early,
              truth late") and only with a pair it cannot see dead, never lie
              on its last card; challenges a claim it can prove false from
              the registry or from cards whose location it knows ("count the
              eights"), and challenges every final-card claim it cannot
              believe.  `honest=True` makes it never lie.

Not modelled: table talk, reading tells, bluff confidence, memory errors.
The skilled bot's knowledge is exact but shallow (it only counts certain
locations), so the skill gap here is a floor.

Usage:  python forked_tongue_sim.py --games 2000 --seed 1
"""

from __future__ import annotations

import argparse
import random
import statistics
from collections import Counter
from itertools import combinations

SYMS = range(1, 10)
DECK = [frozenset(p) for p in combinations(SYMS, 2)]
HAND = {3: 8, 4: 7, 5: 6, 6: 5}
TURN_CAP = 600


def other(card, s):
    (o,) = card - {s}
    return o


class Game:
    def __init__(self, n, bots, rng):
        self.n, self.bots, self.rng = n, bots, rng
        deck = DECK[:]
        rng.shuffle(deck)
        h = HAND[n]
        self.hands = [set(deck[i * h:(i + 1) * h]) for i in range(n)]
        self.registry = set(deck[n * h:])
        self.ledger = []  # entries: (card, shown, claim, claimant)
        self.stats = Counter()
        for p, b in enumerate(bots):
            b.setup(self, p)

    def owed(self):
        return self.ledger[-1][2] if self.ledger else None

    def broadcast(self, event, **kw):
        for p, b in enumerate(self.bots):
            b.observe(self, p, event, **kw)

    def play(self, first=0):
        p, turns = first, 0
        while turns < TURN_CAP:
            turns += 1
            bot = self.bots[p]
            act = bot.act(self, p)
            if act is None:  # decline
                card, shown, claim, claimant = self.ledger.pop()
                self.hands[p].add(card)
                self.stats["decline"] += 1
                self.broadcast("decline", taker=p, card=card)
                p = (p + 1) % self.n
                continue
            card, shown, claim = act
            assert card in self.hands[p] and shown in card and claim != shown
            assert self.owed() is None or shown == self.owed()
            self.hands[p].remove(card)
            self.ledger.append((card, shown, claim, p))
            self.stats["play"] += 1
            lie = claim not in card
            self.stats["lie"] += lie
            self.broadcast("play", claimant=p, shown=shown, claim=claim)
            final = not self.hands[p]
            # challenge window: closest to the claimant's left first
            challenger = None
            for k in range(1, self.n):
                q = (p + k) % self.n
                if self.bots[q].challenge(self, q, p, shown, claim, final):
                    challenger = q
                    break
            if challenger is not None:
                self.stats["challenge"] += 1
                loser = p if lie else challenger
                self.stats["caught" if lie else "wrong_challenge"] += 1
                taken = [e[0] for e in self.ledger]
                self.hands[loser].update(taken)
                self.ledger = []
                self.broadcast("challenge", claimant=p, card=card, loser=loser, taken=taken)
                if final and not lie:
                    return p, turns
                p = (p + 1) % self.n
                continue
            if final:
                return p, turns
            p = (p + 1) % self.n
        return None, turns


class RandomBot:
    name = "random"

    def __init__(self, rng):
        self.rng = rng

    def setup(self, g, p):
        pass

    def observe(self, g, p, event, **kw):
        pass

    def claim(self, card, shown):
        if self.rng.random() < 0.5:
            return other(card, shown)
        return self.rng.choice([s for s in SYMS if s != shown])

    def act(self, g, p):
        r, owed, hand = self.rng, g.owed(), sorted(g.hands[p], key=sorted)
        if owed is None:
            card = r.choice(hand)
            shown = r.choice(sorted(card))
            return card, shown, self.claim(card, shown)
        legal = [c for c in hand if owed in c]
        if legal and r.random() < 0.85:
            card = r.choice(legal)
            return card, owed, self.claim(card, owed)
        return None

    def challenge(self, g, q, p, shown, claim, final):
        return self.rng.random() < (0.5 if final else 0.15)


class SkilledBot:
    name = "skilled"

    def __init__(self, rng, honest=False, lie_rate=0.5):
        self.rng, self.honest, self.lie_rate = rng, honest, lie_rate

    # --- knowledge -----------------------------------------------------
    def setup(self, g, p):
        # where I know a card to be: "reg", or a player index (in that hand)
        self.loc = {c: "reg" for c in g.registry}
        for c in g.hands[p]:
            self.loc[c] = p
        self.ledger_known = []  # parallel to g.ledger: card if I know it, else None

    def observe(self, g, p, event, **kw):
        if event == "play":
            q, shown = kw["claimant"], kw["shown"]
            mine = None
            if q == p:
                mine = g.ledger[-1][0]
                self.loc.pop(mine, None)
            else:
                # any card I placed in q's hand showing this symbol may be the one played
                for c, w in list(self.loc.items()):
                    if w == q and shown in c:
                        del self.loc[c]
            self.ledger_known.append(mine)
        elif event == "decline":
            known = self.ledger_known.pop()
            if kw["taker"] == p:
                self.loc[kw["card"]] = p
            elif known is not None:
                self.loc[known] = kw["taker"]
        elif event == "challenge":
            loser = kw["loser"]
            for c in ([kw["card"]] + [k for k in self.ledger_known if k is not None]):
                self.loc[c] = loser
            if loser == p:
                for c in kw["taken"]:
                    self.loc[c] = p
            self.ledger_known = []

    def unaccounted(self, s, p):
        """Cards showing symbol s whose location I don't know (could be anywhere)."""
        return sum(1 for c in DECK if s in c and c not in self.loc)

    def certainly_false(self, claimant, shown, claim):
        c = frozenset((shown, claim))
        w = self.loc.get(c)
        return w is not None and w != claimant

    # --- decisions -----------------------------------------------------
    def best_claim(self, g, p, card, shown, may_lie):
        truth = other(card, shown)
        best = (self.unaccounted(truth, p), truth)
        if may_lie:
            for x in SYMS:
                if x in (shown, truth):
                    continue
                pair = frozenset((shown, x))
                # a forged pair I hold myself can't be disproved by anyone else;
                # one that is dead or known elsewhere is a lie I'd be caught in
                if self.loc.get(pair, p) != p:
                    continue
                score = self.unaccounted(x, p) - 0.5  # small premium on steering
                if score < best[0]:
                    best = (score, x)
        return best

    def act(self, g, p):
        owed, hand = g.owed(), sorted(g.hands[p], key=sorted)
        last = len(hand) == 1
        may_lie = (not self.honest and not last and len(hand) >= 4
                   and self.rng.random() < self.lie_rate)
        options = []
        for card in hand:
            faces = sorted(card) if owed is None else ([owed] if owed in card else [])
            for shown in faces:
                score, claim = self.best_claim(g, p, card, shown, may_lie)
                options.append((score, self.rng.random(), card, shown, claim))
        if not options:
            return None
        _, _, card, shown, claim = min(options, key=lambda o: o[:2])
        return card, shown, claim

    def challenge(self, g, q, p, shown, claim, final):
        if self.certainly_false(p, shown, claim):
            return True
        if final:
            return frozenset((shown, claim)) not in g.hands[q]  # can't prove it true
        return False


def run(n, games, table, seed):
    rng = random.Random(seed)
    stalls, turns_l, seat_w, s_w = 0, [], Counter(), 0.0
    tot = Counter()
    stall_shapes = Counter()
    for i in range(games):
        first = i % n
        if table == "random":
            bots = [RandomBot(rng) for _ in range(n)]
        elif table == "skilled":
            bots = [SkilledBot(rng) for _ in range(n)]
        elif table == "honest":
            bots = [SkilledBot(rng, honest=True) for _ in range(n)]
        elif table in ("mixed", "honest-mixed"):
            s = (i // n) % n  # skilled seat rotates independently of first seat
            bots = [RandomBot(rng) for _ in range(n)]
            bots[s] = SkilledBot(rng, honest=(table == "honest-mixed"))
        elif table == "liar-vs-honest":
            s = (i // n) % n
            bots = [SkilledBot(rng, honest=True) for _ in range(n)]
            bots[s] = SkilledBot(rng)
        g = Game(n, bots, rng)
        winner, turns = g.play(first)
        tot += g.stats
        if winner is None:
            stalls += 1
            sizes = sorted(len(h) for h in g.hands)
            stall_shapes[(sizes[0], sizes[-1], len(g.ledger))] += 1
            continue
        turns_l.append(turns)
        seat_w[(winner - first) % n] += 1
        if table in ("mixed", "honest-mixed", "liar-vs-honest") and winner == (i // n) % n:
            s_w += 1
    done = games - stalls
    return {
        "stall": stalls / games,
        "turns": statistics.mean(turns_l) if turns_l else float("nan"),
        "p90": sorted(turns_l)[int(0.9 * len(turns_l))] if turns_l else float("nan"),
        "seat": [seat_w[k] / max(done, 1) for k in range(n)],
        "focus_win": s_w / games,
        "decline": tot["decline"] / max(tot["decline"] + tot["play"], 1),
        "lie": tot["lie"] / max(tot["play"], 1),
        "chal_pg": tot["challenge"] / games,
        "caught": tot["caught"] / max(tot["challenge"], 1),
        "stall_shapes": stall_shapes.most_common(3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    print(f"FORKED TONGUE v1.1 sim · {a.games} games per row · seed {a.seed} · turn cap {TURN_CAP}\n")
    print(f"{'P':>2} {'table':<15}{'stall':>7}{'turns':>7}{'p90':>5}{'focus win':>10}{'x fair':>7}"
          f"{'decl%':>7}{'lie%':>6}{'chal/g':>7}{'caught':>7}  seat wins (from first)")
    for n in (3, 4, 5, 6):
        for table in ("random", "skilled", "honest", "mixed", "honest-mixed", "liar-vs-honest"):
            r = run(n, a.games, table, a.seed)
            fw = r["focus_win"] if "mixed" in table or "vs" in table else float("nan")
            print(f"{n:>2} {table:<15}{r['stall']:>7.1%}{r['turns']:>7.1f}{r['p90']:>5}"
                  f"{fw:>10.1%}{fw * n:>7.2f}{r['decline']:>7.0%}{r['lie']:>6.0%}"
                  f"{r['chal_pg']:>7.1f}{r['caught']:>7.0%}  "
                  + " ".join(f"{s:.0%}" for s in r["seat"])
                  + (f"   stalls (min hand, max hand, ledger): {r['stall_shapes']}" if r["stall_shapes"] else ""))
        print()


if __name__ == "__main__":
    main()
