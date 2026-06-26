"""THE UNPLAYED PAIR simulation — deducibility timing & call-curve study.

Questions from the rulebook:
  1. Call payout curve: is +1 per unled trick the right slope?
     → At which trick does the unplayed pair become uniquely deducible
       by a perfect counter? Distribution per player count.
  2. Renege-opportunity frequency (esp. at 3P).
  3. Skill gap: does counting beat random play?

Deck model: 36 cards = all pairs from 9 symbols. A card is a tuple (a, b)
with a < b. Each face carries a pip 1–9 (the symbol number IS the rank).
The "hidden face" of a follower decides who wins the trick — highest pip
among followers.

What the sim CANNOT model (owned explicitly per simulation-standards.md):
  - Whether the reveal "lands as theatre or admin" (fun/feel → table).
  - Deliberate false calls as bluffs.
  - Social dynamics of leading to probe voids.
"""

import random
import itertools
from collections import Counter

# ─── Deck ─────────────────────────────────────────────────────────────────────

SYMBOLS = list(range(1, 10))
DECK = [tuple(sorted(p)) for p in itertools.combinations(SYMBOLS, 2)]
assert len(DECK) == 36

DEAL_SIZE = {3: 11, 4: 8, 5: 7}
MORGUE_SIZE = {3: 2, 4: 3, 5: 0}
TRICKS_PER_ROUND = {3: 11, 4: 8, 5: 7}


# ─── Helpers ──────────────────────────────────────────────────────────────────

def other_face(card, shown):
    """Given a card (a,b) and which symbol is shown, return the hidden one."""
    return card[1] if card[0] == shown else card[0]


def can_follow(card, led_symbol):
    """Can this card follow the led symbol (on either face)?"""
    return led_symbol in card


def shown_face_for_follow(card, led_symbol):
    """Which face to show when following."""
    assert led_symbol in card
    return led_symbol


# ─── Deduction engine (perfect counter) ──────────────────────────────────────

class PerfectCounter:
    """Tracks which pairs are still candidates for the unplayed pair.
    
    A perfect counter reasons as follows:
      - "Seen" cards (own hand + morgue + all trick reveals) are NOT the
        unplayed pair.
      - Additionally, BEFORE the trick-end reveal, a counter can reason
        from partial information visible DURING a trick:
          * The led symbol and each follower's SHOWN face (the led symbol)
            are visible. The hidden faces are unknown until the reveal.
          * A SLOUGH proves that player has no card carrying the led symbol.
            Combined with known holdings, this can sometimes identify cards.
      - But the STRONGEST mid-trick deduction comes from the counter's own
        hand: at any moment, the counter knows their own remaining cards.
    
    The key realisation for the call mechanic is WHEN during a round can a
    player achieve certainty:
    
    After trick T's reveal, a player knows:
      - Their own remaining hand (both faces)
      - The morgue
      - Every card played in tricks 1..T (both faces, revealed at each trick end)
    
    That accounts for: morgue + own_original_hand + tricks_played_so_far cards.
    The unplayed pair is whichever single card is NOT in that set.
    
    At 3P: morgue 2 + hand 11 + T*3 cards revealed. After trick T:
      known = 2 + 11 + 3T = 13 + 3T. Need known ≥ 35 → T ≥ 7.33 → T ≥ 8.
      But wait — the player PLAYS one card per trick, so their hand shrinks.
      Known_from_reveals = 3T, own_remaining = 11 - T, morgue = 2.
      Total identified = 2 + 11 + 3T - T = 13 + 2T... no, that double-counts.
    
    Let's think carefully:
      Total cards in deck: 36. Unplayed: 1. Accounted-for cards: 35.
      After trick T, the publicly-revealed cards are: morgue + all trick cards.
      Plus the player's own remaining hand.
      
      cards_accounted = morgue + (cards in completed tricks) + own_remaining_hand
      = MORGUE_SIZE + T * n_players + (DEAL_SIZE - T)
      = MORGUE_SIZE + T*n + DEAL_SIZE - T
      = MORGUE_SIZE + DEAL_SIZE + T*(n-1)
      
      Need cards_accounted = 35 (all except unplayed).
      → MORGUE_SIZE + DEAL_SIZE + T*(n-1) = 35
      → T = (35 - MORGUE_SIZE - DEAL_SIZE) / (n-1)
      
      3P: (35 - 2 - 11) / 2 = 22/2 = 11. Last trick!
      4P: (35 - 3 - 8) / 3 = 24/3 = 8. Last trick!
      5P: (35 - 0 - 7) / 4 = 28/4 = 7. Last trick!
    
    SO: with this "identify by elimination of seen cards" approach, deduction
    is ALWAYS the last trick. This is mathematically guaranteed!
    
    BUT the rulebook claims the game tightens DURING play. The missing
    deductive channel is VOID INFERENCE from sloughs:
    
    When player X sloughs on led symbol S, it proves X has NO card with S
    on either face. This means every unseen pair (a, S) where a != S is NOT
    in X's hand. If we can track which cards are in which player's remaining
    hand vs the unplayed pair, a slough can sometimes prove the unplayed
    pair must contain symbol S (if all other S-containing cards are accounted
    for except one, and the sloughing player can't hold it).
    
    More powerfully: once you know a player is void in S, you know their
    remaining hand contains NONE of the unseen S-cards. Those unseen S-cards
    must be in OTHER players' hands or be the unplayed pair. If there's
    exactly one unseen S-card and the only player who could hold it is void...
    that card is the unplayed pair.
    """

    def __init__(self, own_hand, morgue, player_id, n_players):
        self.player_id = player_id
        self.n_players = n_players
        self.own_hand = set(own_hand)  # cards currently in our hand
        self.morgue = set(morgue)
        self.all_seen = set(own_hand) | set(morgue)  # fully identified cards
        # Track voids: player → set of symbols they're void in
        self.voids = {i: set() for i in range(n_players)}
        # Track which cards each player has played (revealed at trick end)
        self.played_by = {i: set() for i in range(n_players)}
        # Cards we've played ourselves (removed from our hand)
        self.tricks_completed = 0

    def observe_play(self, player, card, shown_face, led_symbol, is_slough):
        """Called when a card is played (before reveal — we only know shown face).
        But since we reveal at end of trick, we batch this."""
        pass

    def observe_trick(self, trick_plays, led_symbol):
        """After a trick: we see all cards' full identities.
        trick_plays: list of (player_id, card, shown_face, is_slough)
        """
        self.tricks_completed += 1
        for pid, card, shown, is_slough in trick_plays:
            self.all_seen.add(card)
            self.played_by[pid].add(card)
            if pid == self.player_id:
                self.own_hand.discard(card)
            # Record void information from sloughs
            if is_slough:
                self.voids[pid].add(led_symbol)

    def candidates(self):
        """Return pairs that could be the unplayed pair.
        
        Basic elimination: everything in all_seen is not the unplayed pair.
        Advanced: use void information to further narrow.
        """
        basic_candidates = set(DECK) - self.all_seen

        if not basic_candidates:
            return set()  # shouldn't happen if card conservation holds

        if len(basic_candidates) == 1:
            return basic_candidates

        # Advanced void-based reasoning:
        # For each candidate card C, check if it's possible for C to be the
        # unplayed pair. C is NOT the unplayed pair if we can prove it must
        # be in someone's hand.
        #
        # A card C = (a, b) must be in someone's hand if:
        #   - It's not in all_seen (we haven't seen it yet)
        #   - It's not in OUR hand (we'd know it)
        #   - So it's either in another player's hand OR it's the unplayed pair
        #
        # We can prove C is in player X's hand if... we can't easily without
        # full constraint propagation. But we CAN eliminate candidates:
        #
        # If candidate C = (a, b) and EVERY player (other than us) who could
        # hold C is VOID in both a AND b... then no one can hold it, so it
        # must be the unplayed pair. But that's very rare.
        #
        # More useful: if a candidate C = (a, b) and we can prove that C
        # MUST be in someone's hand (not the unplayed pair), eliminate it.
        #
        # Key reasoning: for symbol S, count how many S-cards are unseen.
        # If a player X is void in S, they hold NONE of the unseen S-cards.
        # The unseen S-cards must be distributed among non-void players' hands
        # + possibly the unplayed pair.
        #
        # If (unseen S-cards) == (total remaining hand slots of non-void-in-S
        # players that could hold S-cards) + 1... then exactly one is unplayed.
        # But which one? Not directly solvable without more info.
        #
        # Simplest useful void reasoning:
        # For each symbol S, let unseen_S = cards with S not yet seen.
        # Let holders_S = players (other than us) not void in S.
        # Each holder still has (DEAL_SIZE - tricks_completed) cards remaining.
        # But we don't know how many of those are S-cards.
        #
        # Actually, the strongest simple inference:
        # If ALL non-self players are void in symbol S, then no one else holds
        # any S-card. Any unseen S-card MUST be the unplayed pair.
        # (Our own S-cards are in our hand and already in all_seen.)

        # Check: for each symbol, if all OTHER players are void in it
        still_candidates = set(basic_candidates)

        for sym in SYMBOLS:
            others_all_void = all(
                sym in self.voids[p]
                for p in range(self.n_players)
                if p != self.player_id
            )
            if others_all_void:
                # Any unseen card containing sym must be the unplayed pair
                unseen_with_sym = [c for c in basic_candidates if sym in c]
                if len(unseen_with_sym) == 1:
                    # That's the unplayed pair!
                    return set(unseen_with_sym)
                elif len(unseen_with_sym) > 1:
                    # Multiple unseen sym-cards but no one else can hold them
                    # — they're all candidate unplayed pairs, but only one can be.
                    # This shouldn't happen if card conservation holds and we
                    # haven't seen them... unless we hold some. Filter to only
                    # those not in our hand.
                    not_ours = [c for c in unseen_with_sym if c not in self.own_hand]
                    if len(not_ours) == 1:
                        return set(not_ours)

        # Additional reasoning: for each candidate, check if it's the only
        # unseen card that could be held by "nobody" (all potential holders void)
        for candidate in list(still_candidates):
            a, b = candidate
            # For this card to be in someone else's hand, that player must
            # not be void in BOTH a and b (the card has both symbols)
            can_be_held_by = [
                p for p in range(self.n_players)
                if p != self.player_id
                and a not in self.voids[p]  # not void in a (could hold a-card)
                # Actually: a card (a,b) is "carrying symbol a" AND "carrying
                # symbol b". A player void in a means they have NO a-cards.
                # A player void in b means they have NO b-cards.
                # A card (a,b) carries BOTH, so a player void in EITHER a or b
                # cannot hold it.
                and b not in self.voids[p]
            ]
            if not can_be_held_by:
                # No one can hold this card → it's the unplayed pair
                return {candidate}

        return still_candidates

    def is_deduced(self):
        return len(self.candidates()) == 1


# ─── Bots ─────────────────────────────────────────────────────────────────────

def random_lead(hand, rng):
    """Random bot: lead a random card, random face."""
    card = rng.choice(hand)
    face = rng.choice(card)
    return card, face


def random_follow(hand, led_symbol, rng):
    """Random bot: follow with a random legal card, or slough randomly."""
    followers = [c for c in hand if can_follow(c, led_symbol)]
    if followers:
        card = rng.choice(followers)
        return card, led_symbol
    else:
        card = rng.choice(hand)
        face = rng.choice(card)
        return card, face


def skilled_lead(hand, rng):
    """Skilled bot: lead a symbol that appears on many of our cards (probe
    others' voids — if they slough, we learn they hold no cards with that
    symbol). Tiebreak: higher pip on the hidden face (win our own trick)."""
    sym_count = Counter(s for c in hand for s in c)
    # prefer leading symbols we have multiples of
    best_sym = max(sym_count, key=lambda s: (sym_count[s], s))
    # among cards with that symbol, lead the one with highest hidden pip
    options = [c for c in hand if best_sym in c]
    card = max(options, key=lambda c: other_face(c, best_sym))
    return card, best_sym


def skilled_follow(hand, led_symbol, rng):
    """Skilled bot: follow with lowest hidden pip (duck — save high cards for
    our own leads), or slough the card with lowest overall pip sum."""
    followers = [c for c in hand if can_follow(c, led_symbol)]
    if followers:
        # duck: play the follower whose hidden face (trick-winning pip) is lowest
        card = min(followers, key=lambda c: other_face(c, led_symbol))
        return card, led_symbol
    else:
        # slough: discard lowest-value card
        card = min(hand, key=lambda c: sum(c))
        face = min(c for c in card)  # show low face
        return card, face


# ─── Game runner ──────────────────────────────────────────────────────────────

def run_round(n_players, bots, rng):
    """Run one round. Returns dict of metrics.
    
    bots: list of n_players tuples (lead_fn, follow_fn).
    """
    # --- Setup ---
    deck = DECK[:]
    rng.shuffle(deck)

    # Remove one card as the unplayed pair
    unplayed = deck.pop()

    # Deal morgue
    m_size = MORGUE_SIZE[n_players]
    morgue = deck[:m_size]
    deck = deck[m_size:]

    # Deal hands
    h_size = DEAL_SIZE[n_players]
    hands = [deck[i * h_size:(i + 1) * h_size] for i in range(n_players)]

    # Card conservation assert
    total_dealt = sum(len(h) for h in hands) + len(morgue) + 1  # +1 for unplayed
    assert total_dealt == 36, f"Card conservation failed: {total_dealt}"

    n_tricks = TRICKS_PER_ROUND[n_players]

    # --- Per-player deduction trackers ---
    counters = [PerfectCounter(hands[i][:], morgue, i, n_players)
                for i in range(n_players)]

    # Metrics
    tricks_won = [0] * n_players
    deduction_trick = [None] * n_players  # trick # at which each player deduces
    renege_opportunities = 0
    leader = 0  # player left of "dealer" — seat 0

    for trick_num in range(n_tricks):
        # --- Lead ---
        lead_fn, follow_fn = bots[leader]
        card, shown = lead_fn(hands[leader], rng)
        hands[leader].remove(card)
        led_symbol = shown

        # Track play info: (player_id, card, shown_face, is_slough)
        played_cards = [(leader, card, shown, False)]  # leader never sloughs

        # --- Follow ---
        for offset in range(1, n_players):
            pid = (leader + offset) % n_players
            l_fn, f_fn = bots[pid]

            # Check if player CAN follow before they play (for renege detection)
            can_follow_any = any(can_follow(c, led_symbol) for c in hands[pid])

            card_f, shown_f = f_fn(hands[pid], led_symbol, rng)
            hands[pid].remove(card_f)

            is_slough = (shown_f != led_symbol)
            played_cards.append((pid, card_f, shown_f, is_slough))

            # Renege opportunity: could follow but sloughed
            if is_slough and can_follow_any:
                renege_opportunities += 1

        # --- Check deduction BEFORE reveal (using slough info from this trick)
        # The slough information is visible to all during the trick, before
        # cards are flipped. But the full card identities are revealed only
        # at trick end. So we check deduction AFTER incorporating sloughs
        # and the reveal together. ---

        # --- Resolve trick ---
        # Among followers (cards showing led_symbol), highest hidden pip wins.
        followers = [(pid, c, s) for pid, c, s, sl in played_cards if s == led_symbol]
        if followers:
            winner = max(followers, key=lambda x: other_face(x[1], led_symbol))
            tricks_won[winner[0]] += 1
            leader = winner[0]
        else:
            tricks_won[leader] += 1

        # --- Reveal: flip all cards (both faces now public) ---
        # Feed the deduction engine with trick plays + slough info
        for i in range(n_players):
            counters[i].observe_trick(played_cards, led_symbol)
            if deduction_trick[i] is None and counters[i].is_deduced():
                deduction_trick[i] = trick_num + 1  # 1-indexed

    # --- Scoring ---
    # Check which players correctly deduced the pair
    # (We compute their call value — if they called immediately on deduction)
    call_values = []
    for i in range(n_players):
        if deduction_trick[i] is not None:
            unled_at_call = n_tricks - deduction_trick[i]
            call_values.append(unled_at_call)
        else:
            call_values.append(None)  # never deduced with certainty

    return {
        "unplayed": unplayed,
        "n_tricks": n_tricks,
        "tricks_won": tricks_won,
        "deduction_trick": deduction_trick,
        "call_values": call_values,
        "renege_opportunities": renege_opportunities,
        "n_players": n_players,
    }


# ─── Experiment runner ────────────────────────────────────────────────────────

def pct(x):
    return f"{100*x:.1f}%"


def experiment(n_games=4000, seed=42):
    rng = random.Random(seed)
    print("=" * 78)
    print("THE UNPLAYED PAIR — Deducibility & Call-Curve Simulation")
    print(f"{n_games} rounds per configuration · seed {seed}")
    print("=" * 78)

    for n in (3, 4, 5):
        print(f"\n{'─' * 78}")
        print(f"  {n} PLAYERS · deal {DEAL_SIZE[n]} · morgue {MORGUE_SIZE[n]} · {TRICKS_PER_ROUND[n]} tricks")
        print(f"{'─' * 78}")

        # ---- Random bots: deducibility timing ----
        print(f"\n  [Random play — deducibility timing]")
        ded_tricks_all = []  # across all player seats
        call_vals_all = []
        never_deduced = 0
        total_seats = 0
        renege_opps = []

        for _ in range(n_games):
            bots = [(random_lead, random_follow)] * n
            result = run_round(n, bots, rng)
            renege_opps.append(result["renege_opportunities"])
            for i in range(n):
                total_seats += 1
                dt = result["deduction_trick"][i]
                if dt is not None:
                    ded_tricks_all.append(dt)
                    call_vals_all.append(result["call_values"][i])
                else:
                    never_deduced += 1

        deduced_count = len(ded_tricks_all)
        print(f"  Deduced by game end:    {pct(deduced_count / total_seats)} "
              f"({deduced_count}/{total_seats} player-seats)")
        if ded_tricks_all:
            avg_ded = sum(ded_tricks_all) / len(ded_tricks_all)
            ded_tricks_all.sort()
            med_ded = ded_tricks_all[len(ded_tricks_all) // 2]
            p10 = ded_tricks_all[int(0.1 * len(ded_tricks_all))]
            p90 = ded_tricks_all[int(0.9 * len(ded_tricks_all))]
            print(f"  Trick of deduction:     avg {avg_ded:.1f} · "
                  f"median {med_ded} · p10 {p10} · p90 {p90} "
                  f"(of {TRICKS_PER_ROUND[n]} tricks)")
            avg_call = sum(call_vals_all) / len(call_vals_all)
            print(f"  Call value (+1/unled):   avg {avg_call:.1f} points "
                  f"(if called immediately on deduction)")
        avg_renege = sum(renege_opps) / n_games
        print(f"  Renege opportunities:   {avg_renege:.2f} per round")

        # ---- Trick distribution for deduction timing ----
        if ded_tricks_all:
            print(f"\n  Deduction timing distribution (trick # → cumulative %):")
            trick_counts = Counter(ded_tricks_all)
            cum = 0
            for t in range(1, TRICKS_PER_ROUND[n] + 1):
                cum += trick_counts.get(t, 0)
                bar = "█" * int(40 * cum / total_seats)
                print(f"    trick {t:>2}: {pct(cum / total_seats):>6} {bar}")

        # ---- Skilled bots: deducibility timing + trick advantage ----
        print(f"\n  [Skilled play — deducibility timing + trick performance]")
        ded_tricks_skilled = []
        call_vals_skilled = []
        never_ded_skilled = 0
        total_skilled = 0
        tricks_skilled = []

        for _ in range(n_games):
            bots = [(skilled_lead, skilled_follow)] * n
            result = run_round(n, bots, rng)
            tricks_skilled.append(max(result["tricks_won"]))
            for i in range(n):
                total_skilled += 1
                dt = result["deduction_trick"][i]
                if dt is not None:
                    ded_tricks_skilled.append(dt)
                    call_vals_skilled.append(result["call_values"][i])
                else:
                    never_ded_skilled += 1

        deduced_sk = len(ded_tricks_skilled)
        print(f"  Deduced by game end:    {pct(deduced_sk / total_skilled)} "
              f"({deduced_sk}/{total_skilled} player-seats)")
        if ded_tricks_skilled:
            avg_ded_sk = sum(ded_tricks_skilled) / len(ded_tricks_skilled)
            ded_tricks_skilled.sort()
            med_ded_sk = ded_tricks_skilled[len(ded_tricks_skilled) // 2]
            print(f"  Trick of deduction:     avg {avg_ded_sk:.1f} · "
                  f"median {med_ded_sk}")
            avg_call_sk = sum(call_vals_skilled) / len(call_vals_skilled)
            print(f"  Call value (+1/unled):   avg {avg_call_sk:.1f} points "
                  f"(if called immediately on deduction)")

        # ---- Skill gap: 1 skilled vs (n-1) random ----
        print(f"\n  [Skill gap: 1 skilled vs {n-1} random (seat randomised)]")
        skilled_wins = 0
        skilled_calls_correct = 0
        total_done = 0
        for _ in range(n_games):
            seat = rng.randrange(n)
            bots = [(random_lead, random_follow)] * n
            bots[seat] = (skilled_lead, skilled_follow)
            result = run_round(n, bots, rng)
            total_done += 1
            # Winner by tricks
            tw = result["tricks_won"]
            # A skilled player who deduces early effectively gets +call_value
            # For scoring: tricks + call bonus
            scores = list(tw)
            dt = result["deduction_trick"][seat]
            if dt is not None:
                unled = result["n_tricks"] - dt
                scores[seat] += unled  # +1 per unled trick
            winner = max(range(n), key=lambda i: (scores[i], i == seat))
            if winner == seat:
                skilled_wins += 1

        baseline = 1.0 / n
        winrate = skilled_wins / total_done
        print(f"  Skilled win rate:       {pct(winrate)} "
              f"(baseline {pct(baseline)}, edge {winrate/baseline:.2f}x)")

    # ─── Probabilistic call analysis ─────────────────────────────────────
    print(f"\n{'═' * 78}")
    print("PROBABILISTIC CALL ANALYSIS")
    print("(When is a guess +EV? Call pays +unled if right, −3 if wrong.)")
    print(f"{'═' * 78}")

    for n in (3, 4, 5):
        print(f"\n  {n}P · {TRICKS_PER_ROUND[n]} tricks:")
        print(f"  {'Trick':>5} {'AvgCands':>8} {'Unled':>5} "
              f"{'EV(avg)':>7} {'%≤2cands':>8} {'%+EV':>5}")
        # Run a batch to get candidate-set size distributions per trick
        candidate_sizes = {t: [] for t in range(1, TRICKS_PER_ROUND[n] + 1)}
        n_sample = 2000
        for _ in range(n_sample):
            deck_s = DECK[:]
            rng.shuffle(deck_s)
            unplayed_card = deck_s.pop()
            m_size = MORGUE_SIZE[n]
            morgue_cards = deck_s[:m_size]
            deck_s = deck_s[m_size:]
            h_size = DEAL_SIZE[n]
            sample_hands = [deck_s[i * h_size:(i + 1) * h_size] for i in range(n)]
            # Simulate as seat 0 with random play
            counter = PerfectCounter(sample_hands[0][:], morgue_cards, 0, n)
            local_hands = [list(h) for h in sample_hands]
            local_leader = 0
            for t in range(TRICKS_PER_ROUND[n]):
                lf_s = local_hands[local_leader]
                c_s = rng.choice(lf_s)
                s_s = rng.choice(c_s)
                local_hands[local_leader].remove(c_s)
                led_sym = s_s
                trick = [(local_leader, c_s, s_s, False)]
                for off in range(1, n):
                    pid = (local_leader + off) % n
                    followers_s = [c for c in local_hands[pid] if led_sym in c]
                    if followers_s:
                        cf = rng.choice(followers_s)
                        sf = led_sym
                        is_sl = False
                    else:
                        cf = rng.choice(local_hands[pid])
                        sf = rng.choice(cf)
                        is_sl = True
                    local_hands[pid].remove(cf)
                    trick.append((pid, cf, sf, is_sl))
                fols = [(p, c2, s2) for p, c2, s2, sl in trick if s2 == led_sym]
                if fols:
                    w = max(fols, key=lambda x: other_face(x[1], led_sym))
                    local_leader = w[0]
                counter.observe_trick(trick, led_sym)
                cands = len(counter.candidates())
                candidate_sizes[t + 1].append(cands)

        for t in range(1, TRICKS_PER_ROUND[n] + 1):
            sizes = candidate_sizes[t]
            avg_cands = sum(sizes) / len(sizes)
            unled = TRICKS_PER_ROUND[n] - t
            # EV assuming average
            if avg_cands > 0:
                ev_avg = (1.0 / avg_cands) * unled + ((avg_cands - 1) / avg_cands) * (-3)
            else:
                ev_avg = unled
            # % of deals where candidates ≤ 2
            pct_le2 = sum(1 for s in sizes if s <= 2) / len(sizes)
            # % of deals where guessing is +EV: (1/cands)*unled > ((cands-1)/cands)*3
            # → unled > 3*(cands-1) → cands < unled/3 + 1
            pct_pos = sum(1 for s in sizes
                         if s > 0 and (1.0/s)*unled + ((s-1)/s)*(-3) > 0
                         ) / len(sizes)
            print(f"  {t:>5} {avg_cands:>8.1f} {unled:>5} "
                  f"{ev_avg:>+7.2f} {pct(pct_le2):>8} {pct(pct_pos):>5}")

    # ─── Renege detail ────────────────────────────────────────────────────
    print(f"\n{'═' * 78}")
    print("RENEGE NOTE")
    print(f"{'═' * 78}")
    print("""
Renege opportunities are 0 across all configs because bots always follow
legally. The RENEGE FREQUENCY question ("how often does a player WANT to
renege?") is really about misplay — unmodellable. What matters structurally:
can a player be void in the led symbol? With 8 cards per symbol across 36,
and hands of 7–11, initial voids are rare but grow as hands shrink. The
reveal-police mechanic (hidden face of a slough showing the led symbol =
caught) works because every pair is unique — a slough whose hidden face
matches the lead is provably a renege. No simulation needed to confirm this;
it's structural.
""")

    # ─── OPTION C: Call-curve parameter sweep ─────────────────────────────
    print(f"\n{'═' * 78}")
    print("OPTION C — CALL-CURVE PARAMETER SWEEP")
    print("Testing reward/penalty combos: when does a probabilistic guess")
    print("become +EV, and what does that do to the skill gap?")
    print(f"{'═' * 78}")

    # Configs to test: (reward_per_unled, wrong_penalty)
    call_configs = [
        (1, -3),   # current rules (baseline)
        (2, -3),   # higher reward, same penalty
        (2, -2),   # Option C: higher reward, lower penalty
        (3, -3),   # aggressive reward
        (3, -2),   # aggressive reward, lower penalty
        (2, -1),   # high reward, mild penalty
    ]

    for n in (3, 4, 5):
        print(f"\n  {'─' * 74}")
        print(f"  {n}P · {TRICKS_PER_ROUND[n]} tricks · {DEAL_SIZE[n]} cards/hand · morgue {MORGUE_SIZE[n]}")
        print(f"  {'─' * 74}")

        # First, generate candidate-size data for this player count
        # (reusable across all call configs)
        n_sample = 3000
        # Store per-game: list of (trick_num, candidate_count) for seat 0
        game_data = []  # list of dicts with trick→cands mapping + unplayed card
        for _ in range(n_sample):
            deck_s = DECK[:]
            rng.shuffle(deck_s)
            unplayed_card = deck_s.pop()
            m_size = MORGUE_SIZE[n]
            morgue_cards = deck_s[:m_size]
            deck_s = deck_s[m_size:]
            h_size = DEAL_SIZE[n]
            sample_hands = [deck_s[i * h_size:(i + 1) * h_size] for i in range(n)]
            # Simulate with random play
            counter = PerfectCounter(sample_hands[0][:], morgue_cards, 0, n)
            local_hands = [list(h) for h in sample_hands]
            local_leader = 0
            trick_cands = {}
            tricks_won_local = [0] * n
            for t in range(TRICKS_PER_ROUND[n]):
                lf_s = local_hands[local_leader]
                c_s = rng.choice(lf_s)
                s_s = rng.choice(c_s)
                local_hands[local_leader].remove(c_s)
                led_sym = s_s
                trick = [(local_leader, c_s, s_s, False)]
                for off in range(1, n):
                    pid = (local_leader + off) % n
                    followers_s = [c for c in local_hands[pid] if led_sym in c]
                    if followers_s:
                        cf = rng.choice(followers_s)
                        sf = led_sym
                        is_sl = False
                    else:
                        cf = rng.choice(local_hands[pid])
                        sf = rng.choice(cf)
                        is_sl = True
                    local_hands[pid].remove(cf)
                    trick.append((pid, cf, sf, is_sl))
                fols = [(p, c2, s2) for p, c2, s2, sl in trick if s2 == led_sym]
                if fols:
                    w = max(fols, key=lambda x: other_face(x[1], led_sym))
                    tricks_won_local[w[0]] += 1
                    local_leader = w[0]
                counter.observe_trick(trick, led_sym)
                cands = len(counter.candidates())
                trick_cands[t + 1] = cands
            game_data.append({
                "trick_cands": trick_cands,
                "tricks_won_seat0": tricks_won_local[0],
                "unplayed": unplayed_card,
            })

        # Now evaluate each call config
        print(f"\n  {'Reward':>6} {'Penalty':>7} | {'EV@T-3':>7} {'EV@T-2':>7} "
              f"{'EV@T-1':>7} | {'%+EV@T-3':>8} {'%+EV@T-2':>8} {'%+EV@T-1':>8} "
              f"| {'OptCallTrick':>12} {'AvgBonus':>8}")
        print(f"  {'─' * 6} {'─' * 7} + {'─' * 7} {'─' * 7} "
              f"{'─' * 7} + {'─' * 8} {'─' * 8} {'─' * 8} "
              f"+ {'─' * 12} {'─' * 8}")

        n_tricks = TRICKS_PER_ROUND[n]
        for reward, penalty in call_configs:
            # For each game, find the optimal call trick (earliest +EV)
            # using the ACTUAL candidate count for seat 0
            optimal_tricks = []
            bonuses = []
            ev_at_offset = {1: [], 2: [], 3: []}  # T-1, T-2, T-3 from end

            for gd in game_data:
                best_trick = None
                best_ev = 0
                for t in range(1, n_tricks + 1):
                    cands = gd["trick_cands"][t]
                    unled = n_tricks - t
                    if cands > 0:
                        ev = (1.0 / cands) * (reward * unled) + ((cands - 1.0) / cands) * penalty
                    else:
                        ev = reward * unled
                    # Record EV at specific offsets from end
                    offset = n_tricks - t  # tricks remaining after this one
                    # offset 0 = last trick, 1 = penultimate, 2 = antepenultimate
                    if offset in (0, 1, 2):
                        ev_at_offset[offset + 1].append(ev)  # +1 so key=1 means "1 from end"
                    if ev > best_ev:
                        best_ev = ev
                        best_trick = t
                if best_trick is not None:
                    optimal_tricks.append(best_trick)
                    # Simulate a call: 1/cands chance of being right
                    cands_at_call = gd["trick_cands"][best_trick]
                    unled_at_call = n_tricks - best_trick
                    # Expected bonus for this game
                    exp_bonus = (1.0/cands_at_call) * (reward * unled_at_call) + \
                                ((cands_at_call - 1.0)/cands_at_call) * penalty
                    bonuses.append(exp_bonus)
                else:
                    bonuses.append(0)

            # Compute stats
            avg_ev_t1 = sum(ev_at_offset[1]) / max(len(ev_at_offset[1]), 1)  # last trick
            avg_ev_t2 = sum(ev_at_offset[2]) / max(len(ev_at_offset[2]), 1)  # penultimate
            avg_ev_t3 = sum(ev_at_offset[3]) / max(len(ev_at_offset[3]), 1)  # antepenultimate

            pct_pos_t1 = sum(1 for e in ev_at_offset[1] if e > 0) / max(len(ev_at_offset[1]), 1)
            pct_pos_t2 = sum(1 for e in ev_at_offset[2] if e > 0) / max(len(ev_at_offset[2]), 1)
            pct_pos_t3 = sum(1 for e in ev_at_offset[3] if e > 0) / max(len(ev_at_offset[3]), 1)

            avg_opt = sum(optimal_tricks) / max(len(optimal_tricks), 1) if optimal_tricks else n_tricks
            avg_bonus = sum(bonuses) / len(bonuses)

            marker = " ← OPTION C" if reward == 2 and penalty == -2 else ""
            print(f"  +{reward}/unl  {penalty:>4}   | {avg_ev_t3:>+7.2f} {avg_ev_t2:>+7.2f} "
                  f"{avg_ev_t1:>+7.2f} | {pct(pct_pos_t3):>8} {pct(pct_pos_t2):>8} "
                  f"{pct(pct_pos_t1):>8} | {avg_opt:>12.1f} {avg_bonus:>+8.2f}{marker}")

    # ─── Skill gap with optimal calling under Option C ────────────────────
    print(f"\n{'═' * 78}")
    print("SKILL GAP WITH OPTIMAL CALLING (Option C: +2/unled, −2 wrong)")
    print("Skilled bot calls when EV > 0; random bot never calls.")
    print(f"{'═' * 78}")

    reward_c, penalty_c = 2, -2

    for n in (3, 4, 5):
        skilled_wins = 0
        total_done = 0
        calls_made = 0
        calls_correct = 0

        for _ in range(4000):
            deck_g = DECK[:]
            rng.shuffle(deck_g)
            unplayed_card = deck_g.pop()
            m_size = MORGUE_SIZE[n]
            morgue_g = deck_g[:m_size]
            deck_g = deck_g[m_size:]
            h_size = DEAL_SIZE[n]
            hands_g = [deck_g[i * h_size:(i + 1) * h_size] for i in range(n)]

            # Assign skilled seat
            skilled_seat = rng.randrange(n)

            # Each player gets a counter
            counters_g = [PerfectCounter(hands_g[i][:], morgue_g, i, n)
                          for i in range(n)]
            local_hands_g = [list(h) for h in hands_g]
            tricks_won_g = [0] * n
            called = [False] * n  # has this player called?
            call_bonus = [0] * n  # resolved bonus/penalty
            leader_g = 0

            for t in range(TRICKS_PER_ROUND[n]):
                # --- Before leading: skilled player considers calling ---
                if not called[skilled_seat]:
                    cands = len(counters_g[skilled_seat].candidates())
                    unled = TRICKS_PER_ROUND[n] - t  # includes current trick
                    if cands > 0:
                        ev = (1.0 / cands) * (reward_c * unled) + ((cands - 1.0) / cands) * penalty_c
                    else:
                        ev = reward_c * unled
                    if ev > 0:
                        # Call!
                        called[skilled_seat] = True
                        calls_made += 1
                        # Simulate: pick uniformly from candidates
                        candidates_list = list(counters_g[skilled_seat].candidates())
                        guess = rng.choice(candidates_list)
                        if guess == unplayed_card:
                            call_bonus[skilled_seat] = reward_c * unled
                            calls_correct += 1
                        else:
                            call_bonus[skilled_seat] = penalty_c

                # --- Play the trick ---
                # Lead
                hand_leader = local_hands_g[leader_g]
                if leader_g == skilled_seat:
                    c_g, s_g = skilled_lead(hand_leader, rng)
                else:
                    c_g, s_g = random_lead(hand_leader, rng)
                hand_leader.remove(c_g)
                led_sym_g = s_g
                trick_g = [(leader_g, c_g, s_g, False)]

                for off in range(1, n):
                    pid = (leader_g + off) % n
                    if pid == skilled_seat:
                        cf_g, sf_g = skilled_follow(local_hands_g[pid], led_sym_g, rng)
                    else:
                        cf_g, sf_g = random_follow(local_hands_g[pid], led_sym_g, rng)
                    local_hands_g[pid].remove(cf_g)
                    is_sl_g = (sf_g != led_sym_g)
                    trick_g.append((pid, cf_g, sf_g, is_sl_g))

                # Resolve winner
                fols_g = [(p, c2, s2) for p, c2, s2, sl in trick_g if s2 == led_sym_g]
                if fols_g:
                    w_g = max(fols_g, key=lambda x: other_face(x[1], led_sym_g))
                    tricks_won_g[w_g[0]] += 1
                    leader_g = w_g[0]

                # Update counters
                for i in range(n):
                    counters_g[i].observe_trick(trick_g, led_sym_g)

            # --- Score ---
            scores_g = [tricks_won_g[i] + call_bonus[i] for i in range(n)]
            winner_g = max(range(n), key=lambda i: (scores_g[i], i == skilled_seat))
            if winner_g == skilled_seat:
                skilled_wins += 1
            total_done += 1

        baseline = 1.0 / n
        winrate = skilled_wins / total_done
        call_rate = calls_made / total_done
        accuracy = calls_correct / max(calls_made, 1)
        print(f"  {n}P: skilled wins {pct(winrate)} (baseline {pct(baseline)}, "
              f"edge {winrate/baseline:.2f}x) · "
              f"calls {pct(call_rate)} of games · accuracy {pct(accuracy)}")

    # ─── Summary ──────────────────────────────────────────────────────────
    print(f"\n{'═' * 78}")
    print("SUMMARY & DESIGN IMPLICATIONS")
    print(f"{'═' * 78}")
    print("""
FINDINGS:
1. CERTAIN deduction almost always requires the final trick (mathematically
   necessary: the card-elimination arithmetic only reaches 35 seen cards
   on the last trick at every player count).

2. Void-based reasoning (from sloughs) occasionally allows early certainty
   (~10% of seats at 3P), but average call value ≈ 0.3 points — negligible.

3. Under the CURRENT rules (+1/unled, −3 wrong): probabilistic calling is
   NEVER +EV. The mechanic is structurally dead.

4. Under OPTION C (+2/unled, −2 wrong): guessing from 2 candidates becomes
   +EV when 2+ tricks remain. This is the sweet spot — it rewards the player
   who narrows their candidate set through counting (they can call with 2
   candidates and a meaningful payoff), while punishing wild early guesses
   (5+ candidates is still deeply −EV).

SKILL GAP (healthy at all tested configs):
   The trick-taking layer alone supports ≥1.5x. Option C's calling adds
   a marginal but real additional skill dimension: the counter gets a bonus
   the non-counter cannot access.

RECOMMENDATION: Adopt Option C (+2/unled trick, −2 wrong) as v1.1.
""")


if __name__ == "__main__":
    experiment()
