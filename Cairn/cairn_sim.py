"""
CAIRN — compact chain-patience simulator (concept-stage structural check).

Question this sim answers (per design-principles.md rubric #6 and #10):
  1. Is there a healthy skill gap (greedy >> random)? The collection treats
     ~1.5x and up as healthy; a thin gap is the OUROBOROS dull-game warning.
  2. What fraction of deals are *clearable at all* (clairvoyant beam ceiling)?
     This sets the reserve size R and the scoring tiers, the way the
     TWELVE TRIALS exact solver set its flip tiers.

THE GAME (v0 model)
  - Symbols 1..n; deck = all C(n,2) cards, each an unordered pair {a,b}
    (a double-faced card = an edge of K_n). Default subset n=7 (21 cards)
    for a true train-table footprint; n=9 (36) is the long "campaign".
  - K build piles ("cairns") + a reserve of R holding slots. Compact: the
    only live state is the visible TOP of each cairn plus the reserve.
  - Setup: shuffle the deck into a face-up STOCK. Deal one card to each of
    the K cairns; you choose which face shows (the live top symbol).
  - Turn: draw the stock's top card (you may read both its faces). If a face
    matches a cairn's top symbol, place it there showing its OTHER face (the
    join is consumed, the onward sign becomes the new top). If it matches no
    cairn, slide it into the reserve. If the reserve is full and it still
    cannot be placed -> STUCK, the game ends.
  - Whenever a placement changes a top, any reserve card that is now legal may
    be played out onto a cairn.
  - Clear the whole stock (reserve empty) to win.

AGENTS
  - random      : ranks legal moves at random (no skill floor).
  - greedy      : counting only — expose the sign with the most unplaced
                  partner cards.
  - greedy+peek : greedy PLUS the free one-card peek. The stock's top card
                  always shows one face, so before committing the current card
                  you know one face of the next one. This bot prefers exposing
                  that face (guaranteeing the next card a home), tie-broken by
                  count. Models a player who uses the peek but does not plan
                  deeper.
  - beam ceiling: full clairvoyance over the stock order — the achievable
                  upper bound a perfect planner approaches. The gap between
                  greedy+peek and beam is the multi-step-planning skill room.

v0 SIMPLIFYING ASSUMPTIONS (documented; revisit before a rulebook):
  - No *voluntary* reserving: a card goes to reserve only when it cannot be
    placed. Reserve cards are offloaded greedily whenever they become legal.
    (Voluntary reserving would add skill but explodes the search; left for v1.)
  - The heuristic bots look ahead at most one card (the peek). They do NOT do
    multi-step planning; the beam ceiling shows how much that leaves on the
    table.
  - The score is cards-placed-on-cairns (max = total cards). Clear rate is the
    fraction of deals fully placed.

HANDLING NOTE (why this is not OUROBOROS): every symbol the player must read
is a visible cairn TOP or a reserve card in front of them. Nothing is buried
on a hidden/down face. The OUROBOROS failure (the open symbol lived under the
serpent's head as involuntary overhead) cannot occur here by construction.
"""

import argparse
import random
from itertools import combinations


def build_deck(n):
    """All C(n,2) cards as (lo, hi) symbol pairs — the edges of K_n."""
    return [(a, b) for a, b in combinations(range(1, n + 1), 2)]


def incidence_remaining(symbol, to_place_counts):
    """How many still-to-place cards contain `symbol` (public counting info)."""
    return to_place_counts.get(symbol, 0)


def card_incidence_table(cards):
    """Map symbol -> count of cards (in the given iterable) that contain it."""
    counts = {}
    for a, b in cards:
        counts[a] = counts.get(a, 0) + 1
        counts[b] = counts.get(b, 0) + 1
    return counts


# ---------------------------------------------------------------------------
# Policies. A policy scores a candidate (exposed_symbol) given the set of
# cards still to be placed; higher is better. The board chooses the move with
# the best exposed symbol (keeps the chain feedable).
# ---------------------------------------------------------------------------

def play_deal(seeds, stockcards, visibles, K, R, scorer, rng):
    """Play one shuffled deal. Returns cards placed on cairns.

    seeds       : the K cards dealt to start the cairns (player picks each face)
    stockcards  : the draw order (cards), one drawn per turn
    visibles    : visibles[i] = the face symbol that stock card i shows while it
                  sits on top of the stock. This is the FREE one-card peek the
                  deck grants: before you commit the current card, the next
                  card already shows you one of its two faces.

    scorer(symbol, remaining_counts, next_visible, rng) -> float
        ranks the desirability of leaving `symbol` exposed on a cairn top.
        `next_visible` is the visible face of the card you'll draw next (or
        None on the final draw), so a look-ahead scorer can prefer exposing a
        sign that GUARANTEES the next card has a legal home.
    """
    remaining_counts = card_incidence_table(stockcards)
    first_next = visibles[0] if visibles else None

    # Deal K seed cards; the scorer picks which face to expose.
    tops = []
    for (a, b) in seeds:
        sa = scorer(a, remaining_counts, first_next, rng)
        sb = scorer(b, remaining_counts, first_next, rng)
        tops.append(a if sa >= sb else b)
    placed = K  # seeds count as placed

    reserve = []

    def try_offload(next_visible):
        nonlocal placed
        moved = True
        while moved:
            moved = False
            best = None  # (score, idx, pile, exposed)
            for idx, (a, b) in enumerate(reserve):
                for pile, t in enumerate(tops):
                    if t == a:
                        s = scorer(b, remaining_counts, next_visible, rng)
                        if best is None or s > best[0]:
                            best = (s, idx, pile, b)
                    if t == b:
                        s = scorer(a, remaining_counts, next_visible, rng)
                        if best is None or s > best[0]:
                            best = (s, idx, pile, a)
            if best is not None:
                _, idx, pile, exposed = best
                tops[pile] = exposed
                reserve.pop(idx)
                placed += 1
                moved = True

    nstock = len(stockcards)
    for i, card in enumerate(stockcards):
        a, b = card
        # this card leaves the to-place pool
        remaining_counts[a] = remaining_counts.get(a, 0) - 1
        remaining_counts[b] = remaining_counts.get(b, 0) - 1
        next_visible = visibles[i + 1] if i + 1 < nstock else None

        moves = []  # (score, pile, exposed)
        for pile, t in enumerate(tops):
            if t == a:
                moves.append((scorer(b, remaining_counts, next_visible, rng), pile, b))
            if t == b:
                moves.append((scorer(a, remaining_counts, next_visible, rng), pile, a))

        if moves:
            moves.sort(key=lambda m: m[0], reverse=True)
            _, pile, exposed = moves[0]
            tops[pile] = exposed
            placed += 1
            try_offload(next_visible)
        else:
            if len(reserve) < R:
                reserve.append(card)
            else:
                return placed  # STUCK
    # stock exhausted; any leftover reserve cards are unplaced
    return placed


def random_scorer(symbol, remaining_counts, next_visible, rng):
    """No skill: rank legal moves at random."""
    return rng.random()


def greedy_scorer(symbol, remaining_counts, next_visible, rng):
    """Counting only: expose the sign with the most unplaced partner cards."""
    return remaining_counts.get(symbol, 0)


def lookahead_scorer(symbol, remaining_counts, next_visible, rng):
    """Counting + the free one-card peek: strongly prefer exposing the sign the
    NEXT card already shows, which guarantees that card a legal landing spot;
    break ties by remaining-partner count."""
    bonus = 1000 if (next_visible is not None and symbol == next_visible) else 0
    return remaining_counts.get(symbol, 0) + bonus


# ---------------------------------------------------------------------------
# HAND VARIANT. Instead of a reserve buffer, the player holds a hand of H
# fully-known cards and each turn CHOOSES which to play (and onto which cairn),
# then refills from the stock. This gives a real decision every turn rather
# than only reacting to the single drawn card. Footprint stays compact (a held
# fan + the cairns). Stuck = no hand card is playable on any cairn.
# ---------------------------------------------------------------------------

def play_deal_hand(seeds, stockcards, visibles, K, H, scorer, rng):
    """Hand-management variant. Returns cards placed on cairns (max = total)."""
    remaining_counts = card_incidence_table(stockcards)
    first_next = visibles[0] if visibles else None

    tops = []
    for (a, b) in seeds:
        sa = scorer(a, remaining_counts, first_next, rng)
        sb = scorer(b, remaining_counts, first_next, rng)
        tops.append(a if sa >= sb else b)
    placed = K

    n = len(stockcards)
    p = 0
    hand = []
    while len(hand) < H and p < n:
        hand.append(stockcards[p]); p += 1

    while True:
        next_visible = visibles[p] if p < n else None
        cands = []  # (score, hand_idx, pile, exposed)
        for hi, (a, b) in enumerate(hand):
            for pile, t in enumerate(tops):
                if t == a:
                    cands.append((scorer(b, remaining_counts, next_visible, rng), hi, pile, b))
                elif t == b:
                    cands.append((scorer(a, remaining_counts, next_visible, rng), hi, pile, a))
        if not cands:
            return placed  # stuck (hand non-empty but unplayable)
        cands.sort(key=lambda c: c[0], reverse=True)
        _, hi, pile, exposed = cands[0]
        a, b = hand.pop(hi)
        remaining_counts[a] -= 1
        remaining_counts[b] -= 1
        tops[pile] = exposed
        placed += 1
        if p < n:
            hand.append(stockcards[p]); p += 1
        if not hand:
            return placed  # cleared


def beam_ceiling_hand(deck_order, K, H, width, rng):
    """Clairvoyant ceiling for the hand variant (knows the full stock order)."""
    n_total = len(deck_order)
    seeds, stockcards = deck_order[:K], deck_order[K:]
    n = len(stockcards)
    base_counts = card_incidence_table(stockcards)

    def seed_variants():
        variants = set()
        g = tuple((a if base_counts.get(a, 0) >= base_counts.get(b, 0) else b)
                  for (a, b) in seeds)
        variants.add(g)
        for _ in range(7):
            variants.add(tuple(rng.choice(c) for c in seeds))
        return [list(v) for v in variants]

    init_p = min(H, n)
    init_hand = tuple(sorted(stockcards[:init_p]))
    beam = {}
    for v in seed_variants():
        beam[(tuple(v), init_hand, init_p)] = (tuple(v), init_hand, init_p, K)
    beam = list(beam.values())

    best_overall = K
    for _ in range(n_total + 1):
        nxt = {}
        for tops, hand, p, placed in beam:
            best_overall = max(best_overall, placed)
            for hi, (a, b) in enumerate(hand):
                for pile, t in enumerate(tops):
                    exposed = b if t == a else (a if t == b else None)
                    if exposed is None:
                        continue
                    nt = list(tops); nt[pile] = exposed
                    nh = list(hand); nh.pop(hi)
                    np_ = p
                    if p < n:
                        nh.append(stockcards[p]); np_ = p + 1
                    nhs = tuple(sorted(nh))
                    key = (tuple(nt), nhs, np_)
                    val = (tuple(nt), nhs, np_, placed + 1)
                    if key not in nxt or val[3] > nxt[key][3]:
                        nxt[key] = val
        if not nxt:
            break
        cand = list(nxt.values())
        cand.sort(key=lambda s: s[3], reverse=True)
        beam = cand[:width]
    return best_overall


# ---------------------------------------------------------------------------
# PLANNING AGENTS — realistic information (hidden stock order). These are the
# "skilled human" proxies. They know the cairn tops, their full hand, the set
# of cards still unseen (counting), and the one-face peek of the next card —
# but NOT the stock order. Two designs:
#   * PIMC  (Option B): sample plausible full stock orders consistent with the
#     peek, solve each greedily, average, pick the best-averaging move.
#   * Expectimax (Option A): bounded-depth search alternating move-choice nodes
#     and uncertain-draw (chance) nodes, with a position heuristic at the horizon.
# A harness drives the TRUE deal and reveals the next card only on draw.
# ---------------------------------------------------------------------------

def legal_moves(tops, hand):
    moves = []  # (hand_idx, pile, exposed)
    for hi, (a, b) in enumerate(hand):
        for pile, t in enumerate(tops):
            if t == a:
                moves.append((hi, pile, b))
            elif t == b:
                moves.append((hi, pile, a))
    return moves


def rollout_known(tops, hand, future_cards, future_vis, rng, scorer):
    """Greedy playout on a FULLY-KNOWN future. Returns additional cards placed."""
    tops = list(tops); hand = list(hand)
    counts = card_incidence_table(hand)
    for c in future_cards:
        counts[c[0]] = counts.get(c[0], 0) + 1
        counts[c[1]] = counts.get(c[1], 0) + 1
    placed = 0
    fp, nf = 0, len(future_cards)
    while hand:
        moves = legal_moves(tops, hand)
        if not moves:
            break
        nextvis = future_vis[fp] if fp < nf else None
        best = None
        for (hi, pile, exposed) in moves:
            s = scorer(exposed, counts, nextvis, rng)
            if best is None or s > best[0]:
                best = (s, hi, pile, exposed)
        _, hi, pile, exposed = best
        a, b = hand.pop(hi)
        counts[a] -= 1; counts[b] -= 1
        tops[pile] = exposed
        placed += 1
        if fp < nf:
            hand.append(future_cards[fp]); fp += 1
    return placed


def sample_world(pool, peek, rng):
    """A plausible stock order: a peek-bearing card first (showing peek), then
    the rest in random order with random visible faces. Respects the peek
    without leaking the true next card's identity."""
    pool = list(pool)
    rng.shuffle(pool)
    world = []
    if peek is not None:
        idx = next((i for i, c in enumerate(pool) if peek in c), None)
        if idx is not None:
            c = pool.pop(idx)
            world.append((c, peek))
    for c in pool:
        world.append((c, rng.choice(c)))
    return world


def make_pimc_agent(samples):
    def agent(tops, hand, remaining, peek, K, H, rng):
        moves = legal_moves(tops, hand)
        if not moves:
            return None
        pool = list(remaining)
        worlds = [sample_world(pool, peek, rng) for _ in range(samples)]
        best = None
        for (hi, pile, exposed) in moves:
            total = 0
            for world in worlds:
                fcards = [c for (c, _) in world]
                fvis = [v for (_, v) in world]
                nt = list(tops); nt[pile] = exposed
                nh = list(hand); nh.pop(hi)
                if fcards:
                    nh.append(fcards[0]); rc, rv = fcards[1:], fvis[1:]
                else:
                    rc, rv = [], []
                total += 1 + rollout_known(nt, nh, rc, rv, rng, lookahead_scorer)
            avg = total / len(worlds)
            if best is None or avg > best[0]:
                best = (avg, hi, pile, exposed)
        return (best[1], best[2], best[3])
    return agent


def position_heuristic(tops, hand, pool):
    """Leaf eval for expectimax: mobility + liveness + diversity of the tops."""
    counts = card_incidence_table(list(hand) + list(pool))
    mobility = len(legal_moves(tops, hand))
    liveness = sum(counts.get(t, 0) for t in tops)
    diversity = len(set(tops))
    return mobility * 1.0 + liveness * 0.3 + diversity * 0.5


def expectimax_value(tops, hand, pool, peek, d, chance_samples, rng):
    if not hand:
        return 0.0
    moves = legal_moves(tops, hand)
    if not moves:
        return 0.0
    if d == 0:
        return position_heuristic(tops, hand, pool)
    best = None
    for (hi, pile, exposed) in moves:
        nt = list(tops); nt[pile] = exposed
        nh = list(hand); nh.pop(hi)
        if peek is None or not pool:
            val = 1.0 + expectimax_value(nt, nh, pool, None, d - 1, chance_samples, rng)
        else:
            cand = [c for c in pool if peek in c]
            if not cand:
                val = 1.0 + expectimax_value(nt, nh, pool, None, d - 1, chance_samples, rng)
            else:
                k = min(chance_samples, len(cand))
                acc = 0.0
                for c in rng.sample(cand, k):
                    npool = list(pool); npool.remove(c)
                    nh2 = nh + [c]
                    if npool:
                        nc = rng.choice(npool); npeek = rng.choice(nc)
                    else:
                        npeek = None
                    acc += expectimax_value(nt, nh2, npool, npeek, d - 1, chance_samples, rng)
                val = 1.0 + acc / k
        if best is None or val > best:
            best = val
    return best


def make_expectimax_agent(depth, chance_samples):
    def agent(tops, hand, remaining, peek, K, H, rng):
        moves = legal_moves(tops, hand)
        if not moves:
            return None
        pool = list(remaining)
        best = None
        for (hi, pile, exposed) in moves:
            nt = list(tops); nt[pile] = exposed
            nh = list(hand); nh.pop(hi)
            if peek is None or not pool:
                val = expectimax_value(nt, nh, pool, None, depth - 1, chance_samples, rng)
            else:
                cand = [c for c in pool if peek in c]
                if not cand:
                    val = expectimax_value(nt, nh, pool, None, depth - 1, chance_samples, rng)
                else:
                    k = min(chance_samples, len(cand))
                    acc = 0.0
                    for c in rng.sample(cand, k):
                        npool = list(pool); npool.remove(c)
                        nh2 = nh + [c]
                        if npool:
                            nc = rng.choice(npool); npeek = rng.choice(nc)
                        else:
                            npeek = None
                        acc += expectimax_value(nt, nh2, npool, npeek, depth - 1, chance_samples, rng)
                    val = acc / k
            if best is None or val > best[0]:
                best = (val, hi, pile, exposed)
        return (best[1], best[2], best[3])
    return agent


def play_hand_with_agent(seeds, stockcards, visibles, K, H, agent_fn, rng):
    """Drive the TRUE deal; the agent sees only observable state + the peek."""
    counts = card_incidence_table(stockcards)
    tops = [(a if counts.get(a, 0) >= counts.get(b, 0) else b) for (a, b) in seeds]
    placed = K
    n = len(stockcards)
    p = 0
    hand = []
    while len(hand) < H and p < n:
        hand.append(stockcards[p]); p += 1
    while hand:
        remaining = stockcards[p:]          # the SET is known; order must not be used
        peek = visibles[p] if p < n else None
        move = agent_fn(tops, hand, remaining, peek, K, H, rng)
        if move is None:
            return placed                    # stuck
        hi, pile, exposed = move
        hand.pop(hi)
        tops[pile] = exposed
        placed += 1
        if p < n:
            hand.append(stockcards[p]); p += 1
    return placed


# ---------------------------------------------------------------------------
# Clairvoyant beam search — knows the stock order, estimates the achievable
# ceiling (max cards placeable). Used to set R and the scoring tiers.
# Branches on the drawn card's placement; reserve offload is greedy/auto.
# ---------------------------------------------------------------------------

def beam_ceiling(deck_order, n, K, R, width, rng):
    total = len(deck_order)
    seeds, stock = deck_order[:K], deck_order[K:]

    # A state: (tops tuple, reserve tuple, placed). Start: both seed-face choices.
    start_tops = []
    # enumerate seed face combos is 2^K; K small (3-4) so fine, but keep it light:
    # pick faces greedily by global incidence to seed a single strong start,
    # plus a few random alternatives for diversity.
    base_counts = card_incidence_table(stock)
    seed_choices = []

    def seed_variants():
        variants = set()
        # greedy seed
        g = tuple((a if base_counts.get(a, 0) >= base_counts.get(b, 0) else b)
                  for (a, b) in seeds)
        variants.add(g)
        for _ in range(7):
            variants.add(tuple(rng.choice(c) for c in seeds))
        return [list(v) for v in variants]

    def auto_offload(tops, reserve, placed):
        tops = list(tops)
        reserve = list(reserve)
        moved = True
        while moved:
            moved = False
            for idx, (a, b) in enumerate(reserve):
                done = False
                for pile, t in enumerate(tops):
                    if t == a:
                        tops[pile] = b
                        reserve.pop(idx)
                        placed += 1
                        moved = True
                        done = True
                        break
                    if t == b:
                        tops[pile] = a
                        reserve.pop(idx)
                        placed += 1
                        moved = True
                        done = True
                        break
                if done:
                    break
        return tuple(tops), tuple(sorted(reserve)), placed

    beam = []
    for v in seed_variants():
        t, res, p = auto_offload(tuple(v), (), K)
        beam.append((t, res, p))
    # dedupe
    beam = list({s for s in beam})

    for card in stock:
        a, b = card
        nxt = {}
        for tops, reserve, placed in beam:
            options = []
            for pile, t in enumerate(tops):
                if t == a:
                    options.append((pile, b))
                if t == b:
                    options.append((pile, a))
            if options:
                for pile, exposed in options:
                    nt = list(tops)
                    nt[pile] = exposed
                    s = auto_offload(tuple(nt), reserve, placed + 1)
                    key = s
                    if key not in nxt or s[2] > nxt[key][2]:
                        nxt[key] = s
            else:
                if len(reserve) < R:
                    nr = tuple(sorted(reserve + (card,)))
                    s = (tops, nr, placed)
                    if s not in nxt:
                        nxt[s] = s
                else:
                    # stuck branch: terminal, keep its placed count as candidate
                    s = (tops, reserve, placed)
                    key = ("DEAD", placed, tops, reserve)
                    nxt[key] = s
        # prune to beam width by placed count (then fewer reserve cards)
        cand = list(nxt.values())
        cand.sort(key=lambda s: (s[2], -len(s[1])), reverse=True)
        beam = cand[:width]
        if not beam:
            break

    return max((s[2] for s in beam), default=0)


def run(n, K, R, trials, beam_trials, width, seed):
    rng = random.Random(seed)
    deck = build_deck(n)
    total = len(deck)

    rnd_scores, grd_scores, look_scores = [], [], []
    rnd_clear = grd_clear = look_clear = 0
    for _ in range(trials):
        order = deck[:]
        rng.shuffle(order)
        seeds, stockcards = order[:K], order[K:]
        # which face each stock card shows on top of the stock (the free peek)
        visibles = [rng.choice(card) for card in stockcards]
        rs = play_deal(seeds, stockcards, visibles, K, R, random_scorer, rng)
        gs = play_deal(seeds, stockcards, visibles, K, R, greedy_scorer, rng)
        ls = play_deal(seeds, stockcards, visibles, K, R, lookahead_scorer, rng)
        rnd_scores.append(rs); grd_scores.append(gs); look_scores.append(ls)
        rnd_clear += (rs == total)
        grd_clear += (gs == total)
        look_clear += (ls == total)

    beam_scores = []
    beam_clear = 0
    for _ in range(beam_trials):
        order = deck[:]
        rng.shuffle(order)
        bs = beam_ceiling(order, n, K, R, width, rng)
        beam_scores.append(bs)
        beam_clear += (bs == total)

    def mean(xs):
        return sum(xs) / len(xs) if xs else 0.0

    rm, gm, lm, bm = (mean(rnd_scores), mean(grd_scores),
                      mean(look_scores), mean(beam_scores))
    # skill gap measured on cards LEFT UNPLACED (the thing skill reduces),
    # which is more sensitive than raw placed when clear rates are high.
    rnd_left, grd_left, look_left = total - rm, total - gm, total - lm
    gap_grd = (rnd_left / grd_left) if grd_left > 0 else float('inf')
    gap_look = (rnd_left / look_left) if look_left > 0 else float('inf')
    peek_value = (grd_left / look_left) if look_left > 0 else float('inf')

    print(f"n={n} symbols ({total} cards)  K={K} cairns  R={R} reserve")
    print(f"  random        : placed {rm:5.2f}/{total}  clear {100*rnd_clear/trials:5.1f}%  (left {rnd_left:.2f})")
    print(f"  greedy        : placed {gm:5.2f}/{total}  clear {100*grd_clear/trials:5.1f}%  (left {grd_left:.2f})")
    print(f"  greedy+peek   : placed {lm:5.2f}/{total}  clear {100*look_clear/trials:5.1f}%  (left {look_left:.2f})")
    print(f"  beam ceiling  : placed {bm:5.2f}/{total}  clear {100*beam_clear/beam_trials:5.1f}%  (width {width}, {beam_trials} deals)")
    print(f"  skill gap (left): greedy/random {gap_grd:.2f}x | peek/random {gap_look:.2f}x | value of peek {peek_value:.2f}x")
    print()
    return dict(n=n, K=K, R=R, rm=rm, gm=gm, lm=lm, bm=bm,
                rnd_clear=rnd_clear/trials, grd_clear=grd_clear/trials,
                look_clear=look_clear/trials, beam_clear=beam_clear/beam_trials,
                gap_grd=gap_grd, gap_look=gap_look, peek_value=peek_value)


def run_hand(n, K, H, trials, beam_trials, width, seed):
    rng = random.Random(seed)
    deck = build_deck(n)
    total = len(deck)

    rnd_scores, grd_scores, look_scores = [], [], []
    rnd_clear = grd_clear = look_clear = 0
    for _ in range(trials):
        order = deck[:]
        rng.shuffle(order)
        seeds, stockcards = order[:K], order[K:]
        visibles = [rng.choice(card) for card in stockcards]
        rs = play_deal_hand(seeds, stockcards, visibles, K, H, random_scorer, rng)
        gs = play_deal_hand(seeds, stockcards, visibles, K, H, greedy_scorer, rng)
        ls = play_deal_hand(seeds, stockcards, visibles, K, H, lookahead_scorer, rng)
        rnd_scores.append(rs); grd_scores.append(gs); look_scores.append(ls)
        rnd_clear += (rs == total)
        grd_clear += (gs == total)
        look_clear += (ls == total)

    beam_scores = []
    beam_clear = 0
    for _ in range(beam_trials):
        order = deck[:]
        rng.shuffle(order)
        bs = beam_ceiling_hand(order, K, H, width, rng)
        beam_scores.append(bs)
        beam_clear += (bs == total)

    def mean(xs):
        return sum(xs) / len(xs) if xs else 0.0

    rm, gm, lm, bm = (mean(rnd_scores), mean(grd_scores),
                      mean(look_scores), mean(beam_scores))
    rnd_left, grd_left, look_left = total - rm, total - gm, total - lm
    gap_grd = (rnd_left / grd_left) if grd_left > 0 else float('inf')
    gap_look = (rnd_left / look_left) if look_left > 0 else float('inf')

    print(f"n={n} symbols ({total} cards)  K={K} cairns  HAND={H}")
    print(f"  random        : placed {rm:5.2f}/{total}  clear {100*rnd_clear/trials:5.1f}%  (left {rnd_left:.2f})")
    print(f"  greedy        : placed {gm:5.2f}/{total}  clear {100*grd_clear/trials:5.1f}%  (left {grd_left:.2f})")
    print(f"  greedy+peek   : placed {lm:5.2f}/{total}  clear {100*look_clear/trials:5.1f}%  (left {look_left:.2f})")
    print(f"  beam ceiling  : placed {bm:5.2f}/{total}  clear {100*beam_clear/beam_trials:5.1f}%  (width {width}, {beam_trials} deals)")
    print(f"  skill gap (left): greedy/random {gap_grd:.2f}x | peek/random {gap_look:.2f}x")
    print()


def run_planning(n, K, H, fast_trials, heavy_trials, beam_trials, width,
                 pimc_samples, emax_depth, emax_chance, seed):
    """Compare floor agents, both planning agents, and the ceiling on identical
    deals (heavy agents use fewer deals for runtime)."""
    deck = build_deck(n)
    total = len(deck)

    # Fast floor agents (many deals).
    rngf = random.Random(seed)
    rnd_s, grd_s, pk_s = [], [], []
    for _ in range(fast_trials):
        order = deck[:]; rngf.shuffle(order)
        seeds, stock = order[:K], order[K:]
        vis = [rngf.choice(c) for c in stock]
        rnd_s.append(play_deal_hand(seeds, stock, vis, K, H, random_scorer, rngf))
        grd_s.append(play_deal_hand(seeds, stock, vis, K, H, greedy_scorer, rngf))
        pk_s.append(play_deal_hand(seeds, stock, vis, K, H, lookahead_scorer, rngf))

    # Heavy planning agents + beam, on a shared set of deals.
    rngh = random.Random(seed + 1)
    pimc = make_pimc_agent(pimc_samples)
    emax = make_expectimax_agent(emax_depth, emax_chance)
    pimc_s, emax_s, beam_s = [], [], []
    for _ in range(heavy_trials):
        order = deck[:]; rngh.shuffle(order)
        seeds, stock = order[:K], order[K:]
        vis = [rngh.choice(c) for c in stock]
        pimc_s.append(play_hand_with_agent(seeds, stock, vis, K, H, pimc, rngh))
        emax_s.append(play_hand_with_agent(seeds, stock, vis, K, H, emax, rngh))
        if len(beam_s) < beam_trials:
            beam_s.append(beam_ceiling_hand(order, K, H, width, rngh))

    def stat(xs):
        m = sum(xs) / len(xs)
        clr = 100 * sum(1 for x in xs if x == total) / len(xs)
        return m, clr, total - m

    rm, rc, rl = stat(rnd_s)
    gm, gc, gl = stat(grd_s)
    pkm, pkc, pkl = stat(pk_s)
    pim, pic, pil = stat(pimc_s)
    em, ec, el = stat(emax_s)
    bm, bc, bl = stat(beam_s)

    print(f"n={n} ({total} cards)  K={K} cairns  HAND={H}   "
          f"[floor {fast_trials} deals | planning/ceiling {heavy_trials}/{beam_trials} deals]")
    print(f"  random            : placed {rm:5.2f}  clear {rc:5.1f}%  (left {rl:.2f})")
    print(f"  greedy            : placed {gm:5.2f}  clear {gc:5.1f}%  (left {gl:.2f})")
    print(f"  greedy+peek       : placed {pkm:5.2f}  clear {pkc:5.1f}%  (left {pkl:.2f})")
    print(f"  expectimax(d={emax_depth})     : placed {em:5.2f}  clear {ec:5.1f}%  (left {el:.2f})")
    print(f"  PIMC({pimc_samples} worlds)    : placed {pim:5.2f}  clear {pic:5.1f}%  (left {pil:.2f})")
    print(f"  beam ceiling      : placed {bm:5.2f}  clear {bc:5.1f}%  (left {bl:.2f})")

    def gap(x):
        return (rl / x) if x > 0 else float('inf')
    print(f"  skill gap vs random (cards-left): peek {gap(pkl):.2f}x | "
          f"emax {gap(el):.2f}x | PIMC {gap(pil):.2f}x | ceiling {gap(bl):.2f}x")
    # how much of the floor->ceiling room each planner recovers
    room = pkl - bl
    if room > 0:
        print(f"  planner recovery of peek->ceiling room: "
              f"emax {100*(pkl-el)/room:4.0f}%  |  PIMC {100*(pkl-pil)/room:4.0f}%")
    print()


def main():
    ap = argparse.ArgumentParser(description="CAIRN structural check")
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--beam-trials", type=int, default=600)
    ap.add_argument("--width", type=int, default=80)
    ap.add_argument("--seed", type=int, default=20260619)
    ap.add_argument("--planning", action="store_true",
                    help="run the PIMC vs expectimax planning comparison")
    ap.add_argument("--heavy-trials", type=int, default=250)
    ap.add_argument("--pimc-samples", type=int, default=60)
    ap.add_argument("--emax-depth", type=int, default=2)
    ap.add_argument("--emax-chance", type=int, default=5)
    ap.add_argument("--configs", type=str, default="",
                    help="comma list of n/K/H for --planning, e.g. 9/4/4,9/5/4")
    args = ap.parse_args()

    if args.planning:
        print("=" * 70)
        print("CAIRN — planning agents (realistic info, hidden stock) vs floor & ceiling")
        print("=" * 70)
        print()
        if args.configs:
            cfgs = [tuple(int(x) for x in c.split("/")) for c in args.configs.split(",")]
        else:
            cfgs = [(7, 3, 4), (7, 4, 3), (9, 4, 4)]
        for (n, K, H) in cfgs:
            run_planning(n, K, H, args.trials, args.heavy_trials, args.beam_trials,
                         args.width, args.pimc_samples, args.emax_depth,
                         args.emax_chance, args.seed)
        return

    print("=" * 64)
    print("CAIRN structural check — skill gap & clearability sweep")
    print("=" * 64)
    print()

    print("--- RESERVE variant (draw one; buffer of R slots) ---\n")
    reserve_configs = [
        (7, 3, 1), (7, 3, 2), (7, 3, 3),
        (7, 4, 2),
        (9, 3, 2), (9, 3, 3), (9, 4, 3),
    ]
    for (n, K, R) in reserve_configs:
        run(n, K, R, args.trials, args.beam_trials, args.width, args.seed)

    print("--- HAND variant (hold H cards; choose which to play each turn) ---\n")
    hand_configs = [
        (7, 3, 3), (7, 3, 4),
        (7, 4, 3), (7, 4, 4),
        (9, 4, 3), (9, 4, 4),
    ]
    for (n, K, H) in hand_configs:
        run_hand(n, K, H, args.trials, args.beam_trials, args.width, args.seed)


if __name__ == "__main__":
    main()
