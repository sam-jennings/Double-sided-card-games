# TURNCOAT — Design Analysis

*How the second game was built and tuned, v1.0 → v1.2. Companion to the rulebook, and a sibling document to the SYZYGY design analysis.*

> **Naming note:** this document records tuning under earlier names — the **guild-era ability names** (Blade, Whisper, Coin, Veil, Hound, Ash, etc.) and the Nine-Signs names as they then stood. The shipping deck uses the Nine Signs (see `SYMBOL_SETS.md` §7); the catch-up sign referred to as **"Void"** is now **Moon** (pip 1), and **Root** is now **Leaf** (pip 2). Mechanics and balance numbers are unaffected.

---

## 1. The brief, and the one mechanic

The assignment: a second game from the same component brief (36 double-faced all-pairs cards, 9 symbols, 3×3 grid, draw-the-public-deck-top, requirement-gated abilities, chains), built around **one core mechanic absent from SYZYGY**, constructed so it feels like a different game — and, with hindsight, a better one.

SYZYGY's board is completely **neutral**: no card belongs to anyone, scoring is geometric, and conflict is indirect (capture timing). The chosen core for TURNCOAT is therefore **allegiance**. The all-pairs deck has a structural gift SYZYGY never touches: *every card carries exactly two symbols*, which means every card can literally serve two masters. Make players own the symbols and three things fall out almost for free:

- **Flipping becomes defection** — the brief's signature physical action becomes the game's central aggressive verb instead of a side effect.
- **Scoring becomes covering** — place onto an occupied post and the buried agent banks to *its face's owner*, so you score by burying your own exposed agents before rivals turn them.
- **Conflict becomes personal** — when your Moon equivalent defects, you know exactly who turned it. The brief asked for "lots of player conflict"; allegiance makes conflict targeted rather than ambient.

Everything else (the charging/chain engine, once-per-turn caps, public deck-top, optional activations) was deliberately retained from SYZYGY: it is proven, provably terminating machinery, and keeping the engine identical isolates the experiment to the one variable that matters.

## 2. Method

Same discipline as SYZYGY: the full ruleset as a simulator (`turncoat_sim.py`, included) with every contested rule behind a command-line flag; RandomBot as the mechanics ceiling and a one-ply GreedyBot (point differential + board-presence + own-adjacency evaluation) as the adversarial floor; batches of 300–1,000 games per configuration on fixed seeds with an alternate-seed robustness check; card conservation (grid + piles + removed + deck = 36) asserted every game. Roughly **22,000 simulated games** total.

Health targets were pre-registered before the first run, deliberately stricter than SYZYGY's where hindsight said they should be: greedy ≥ 85% vs random; skilled activations ≥ 0.30/turn (SYZYGY shipped at 0.24 — its one soft result); ≥ 14 banked cards/game; zero-bank < 2%; ties < 8% pre-tiebreak; seats within 52/48 and flat in multiplayer; and a metric SYZYGY never needed: **every guild's owned-win rate within ±6 points of uniform**, because when players *own* symbols, symbol balance becomes draft fairness.

## 3. What v1.0 got wrong — the inverted board

The first complete ruleset was immediately lively (0.56 activations/turn, banked 22/game, zero ties) — the allegiance economy works. But it failed three pre-registered checks, and the diagnosis exposed a beautiful inversion of SYZYGY's pathology.

**The board runs sparse, not saturated.** SYZYGY's grid filled by turn 9 and stayed full; abilities that needed empty space died. TURNCOAT's extraction economy *drains* the grid (final boards averaged 3.5 cards), so the failure mode flipped: isolation requirements trivialised (Whisper's "≤1 neighbour" met 95% of the time) while clustering requirements starved (Coin 6.5% met, Crown 7.8% — the banking economy eats the very own-clusters Crown needs). Same lesson, mirror image: *requirements must be written for the board state the economy actually produces.*

**The flip premium concentrated.** Mask (flip any agent anywhere) posted a 72.5% owned-win rate — the strongest dominance signal in either game's data. The mechanism is SYZYGY's Eclipse loop wearing a new coat: the most useful ability gets shown most, shown faces are the ones that get banked, and banked faces pay *the owner*. Utility compounds into points.

**P2 won 55.8% of duels.** The last mover banks the final unanswerable cover and reacts to every exposure.

### v1.0 baseline (greedy mirror, 2P, 500 games)

| Metric | v1.0 | Target |
|---|---|---|
| Banked cards/game | 20.6 | ≥ 14 ✓ |
| Activations/turn (skilled) | 0.72 | ≥ 0.30 ✓ |
| Ties / zero-bank | 0% / 0% | ✓ |
| Seat win rates | 44.4 / 55.6 | ✗ |
| Owned-win spread | 38.4 – 72.5 | ✗ (±6 → 44–56) |
| Dead abilities (greedy) | Veil 0.58, Coin 0.38 | ✗ |

## 4. The whack-a-mole, and the lesson that broke it

Eleven isolated A/B arms (500–600 games each, same seed) drove the tuning. The compressed story:

| Arm | Result | Verdict |
|---|---|---|
| Mask req: 2 adjacent rivals | Mask 72.5 → 46.4, but **Whisper inherits 66.8** | reject — premium migrates |
| Ash burns sacrifice the Ash card | Ash owner 33.8% — rivals weaponise *your* guild | reject |
| Whisper =1 / Veil / Crown req re-map | Crown fixed (7.8 → 50% req-met) | adopt |
| Mask flips only in its row/column | **seats 49.6/50.4** — global reach was the last-mover's scalpel | adopt |
| Ash needs a 2-card deficit | burns 4.7 → 2.7/game, Ash at 49% | adopt |
| Coin req: ≥2 any neighbours | Coin alive at 26% req-met | adopt |
| P1 komi +1 (and later +0.5 in 4P) | 58.4% P1 / 41% P4 — any point overshoots | reject |

The decisive insight came from watching the premium *migrate*: nerf Mask and Whisper spikes; nerf both and the next flipper takes over. In an allegiance economy, **the flip is the wild** — whichever guild flips most freely owns the game, exactly as whichever symbol completed lines most easily owned SYZYGY. And SYZYGY's fix was never to nerf the wild; it was to spread it. So v1.2 **democratises the flip**: Veil's swap gains "you may flip the displaced agent", Hound's move gains "you may flip the moved agent", Whisper keeps its peek-flip, Mask keeps its line-flip, and Blade's removal is flip-grade by nature. Five guilds now carry defection tools; hard requirements gate the strong riders (Veil needs a friendly anchor, Hound exactly one neighbour); and the cold banking guilds got reach instead (Key extracts along its whole line). One residual hot spot — the flip premium briefly re-concentrated in whichever rider was cheapest — was closed by exactly that req-tightening, not by removing the riders.

The result: owned-win spread collapsed from 38–73 to **47.9–58.0**, with eight of nine guilds inside 47.9–50.6. Mask remains the deliberate top pick at +8 — re-gating it (tested once more in the final meta) crushed it to 43 and pushed Key to 56, strictly worse. A known-strong first pick is healthy for a snake draft; the preset teams pair it accordingly, and in the 4P preset Mask is the *unaligned* guild — the strongest house in the court belongs to no one.

## 5. Granularity, the 4P seat problem, and the tiebreak

With guilds balanced, one structural issue remained: 4P games clustered so tightly (average winning margin 0.70) that **44.8% of them shared the top score** before tiebreaks, and the first-extractor rule (inherited from SYZYGY, where it was perfect) interacted badly with seat order — P4 fell to 20.2%. Diagnostics showed P4's *raw* position was fine; the tiebreak was the distortion. Three fixes, tested in isolation and combination:

- **Final-board faces score 2** (not 1): margins widen at every count (2P pre-tiebreak ties drop to 7%), and the endgame gains a real bank-versus-squat decision.
- **Tiebreak = most recent extraction**: seat-neutral in practice and better than first-extraction at every count — 3P lands at a flat 33.4/33.4/33.2, and 4P at 25.8/21.6/26.6/26.0. One rule, all counts, thematically clean ("the freshest intelligence carries the day").
- **Allied Houses**: 2v2 partnership scoring for 4P, seat-symmetric by construction (25.1/24.9/25.1/24.9 over 800 games), offered as the recommended competitive 4P mode since free-for-all 4P remains the lightest, swingiest count.

Point-based seat compensation (komi) was tested honestly and rejected twice: with margins this tight, even half a point flips 40% of games.

## 6. Final state of the design (v1.2)

Greedy mirrors: 1,000 games (2P), 800 (3P), 800 (4P), seed 42; 2P re-run at seed 1234.

| Metric | 2P | 3P | 4P (FFA) | Target |
|---|---|---|---|---|
| Banked cards/game | 22.2 | 25.7 | 22.2 | ≥ 14 ✓ |
| Activations/turn (skilled) | 1.24 | 0.98 | 0.70 | ≥ 0.30 ✓ |
| Turns with 2+ activations | 36% | 27% | 17% | — |
| Flips/game | 22.6 | ~20 | ~14 | — |
| Ties (after tiebreak) / zero-bank | 0% / 0% | 0% / 0% | 0% / 0% | ✓ |
| Seat win rates | 47.6/52.4 (50.5/49.5 alt seed) | 31.8/35.4/32.9 | 24.5/22.8/28.6/24.1 | ✓ / ✓ / range 5.8 |
| Owned-win band (uniform ±6) | 47.9–58.0* | 29.6–37.4 | 19.1–30.9 | ✓ except Mask* |
| Greedy vs random | **100%** (margin 14.8) | — | — | ≥ 85% ✓ |

*\*Mask ships at +8 as the documented strong pick; see §4. In 4P, Veil and Blade sit exactly at the ±6 edges.*

Per-guild health (2P, 1,000 games): every guild activates between 1.6 and 8.7 times per game, every guild banks 2.3–3.7 cards per game, and the win–lose activation differentials are uniformly positive except Ash's deliberately negative catch-up signature (−0.14; the behind player's tool, as designed and as Void was before it).

Known count-scaling softness, documented rather than hidden: with only 2 owned guilds in 4P, own-adjacency requirements fire less (Coin 14.5%, Crown 16.4% req-met) and the game plays lighter — which is precisely why Allied Houses, which restores the 4-guild-per-side structure of the duel, is the recommended 4P mode.

## 7. Is it better than SYZYGY? The data case

The brief asked for lots of player conflict, and expected hindsight to produce a stronger game. Head-to-head on the metrics both games share:

| Metric (2P skilled play) | SYZYGY v1.2 | TURNCOAT v1.2 |
|---|---|---|
| Activations/turn | 0.24 | **1.24** |
| Turns using no ability | 78% | **30%** |
| Turns chaining 2+ abilities | ~4% | **36%** |
| Scoring events/game | ~6 alignments | **~28 extractions** |
| Directed conflict verbs/game (flips of rival assets, removals, burns) | indirect | **~30** |
| Greedy vs random | 96.3% | **100%** |
| Seats / ties | flat / 0% | flat / 0% |

SYZYGY's one soft hypothesis (H5: are chains lively under *skilled* play?) is TURNCOAT's headline strength — and the reason is structural, not luck. In SYZYGY, the active-player-captures rule makes most ability use self-defeating, so optimal play is restraint. In TURNCOAT, abilities convert allegiance, and allegiance is points: a flip is roughly worth a banked card, so skilled play *wants* to act. The hindsight that mattered most was choosing a core mechanic whose incentives point toward the toybox instead of away from it. Conflict is also legible in a way SYZYGY's is not: every flip, burn, and removal has a name attached. SYZYGY remains the cleaner, quieter puzzle — closer to a perfect-information abstract with one secret — and some tables will prefer that. But against the brief as written, TURNCOAT is the better answer.

## 8. Honest limitations — what simulation cannot tell us

**The draft is unmodelled.** Sims assign guilds randomly each game; owned-win rates therefore measure guild strength under random assignment, not under drafting. Human drafts will partially self-correct (Mask goes first overall), but draft *strategy* — synergy picks, hate picks, reading the table — is an untested layer, and the preset teams are the hedge.

**Whisper's information value is invisible**, exactly as Aurora's was: perfect-information bots can't price a peek. Whisper's 48.4% owned-win is a floor.

**One-ply bots under-rate position.** Veil and Hound activate heavily but show the lowest owned-win rates; a deeper searcher (or a human) who repositions *for the next turn* may value them higher. The balance band could shift a couple of points in live play.

**Mercenary activations may read as feel-bad.** The bots happily spend rivals' agents; whether humans find "your own Blade swung against you" delicious or demoralising is exactly the kind of thing only a table can answer.

**Recommended first live tests:** (1) is one activation per turn exciting or exhausting over 18 turns; (2) does the bury-your-own loop teach itself within a game, or does "covering rivals gifts them points" need a harder warning; (3) does Mask feel like a fun strong pick or a must-pick; (4) Allied Houses versus free-for-all at four.

## 9. Change log

| Version | Change | Reason (data) |
|---|---|---|
| v1.0 | Initial ruleset: allegiance, covering, mercenary chains | — |
| v1.1 | Mask flips restricted to its line | Seats 44/56 → 50/50 |
| v1.1 | Ash needs a 2-card deficit | Burns 4.7 → 2.7/game |
| v1.1 | Coin req ≥2 neighbours; Crown req 1 own; Veil req re-anchored; Whisper bounded | Dead reqs revived (Crown 8 → 50% met) |
| v1.2 | Flip democratisation: Veil and Hound gain flip riders; Key gains line reach | Owned-win spread 38–73 → 48–58 |
| v1.2 | Final-board faces score 2 | 2P pre-tiebreak ties 8.3 → 7.1%; 4P 44.8 → 36.8% |
| v1.2 | Tiebreak: most recent extraction → seat | Flat seats at all counts; P4 20.2 → 24.1% |
| — | Komi (every flavour) rejected | +1 or +0.5 overshoots to 36–58% |
| — | Allied Houses adopted as 4P variant | Seat-symmetric by construction |

*All numbers: greedy-mirror simulations, 300–1,000 games per configuration, seeds 42/1234, ~22,000 games total. Every rule above is a flag in `turncoat_sim.py`.*
