# AFTERIMAGE — design analysis

*Concept-stage simulation, November 2026. Simulator: [afterimage_sim.py](afterimage_sim.py). Game record: [AFTERIMAGE_concept.md](AFTERIMAGE_concept.md).*

## 1. The questions

1. **Termination.** Does a concentration game in which missed cards stay flipped always reach an end, even with random play?
2. **Does memory matter?** Is the skill gap between good and poor memory wide enough to make it a memory game, and how steep is it?
3. **Where does the game naturally stop**, and can a fixed "stop at N cards" rule end it?
4. **The Sweep end rule.** Does "flip everything; if no two match, the game ends and you score" end the game cleanly, without stalls or long after-play? Should the Sweep be worth 1 or 2?
5. **Fairness.** Seat advantage at 2–4 players; how often the result is a tie.
6. **Skill layers.** Does counting the public sign registry beat memory alone?
7. **Tiebreak.** Which tiebreaker leaves the fewest shared wins without skewing seats? *(added for the v0.1 rulebook)*
8. **Lighter subset.** Does the seven-sign, 21-card deck play cleanly as a first-game variant? *(added for the v0.1 rulebook)*

## 2. Method

- **Ruleset modelled:** all 36 cards with a random face up (the wash-shuffle). A guess flips two cards in turn. A match takes both, scores 1 and guesses again. A miss leaves both flipped and passes the turn. Two endings:
  - **natural** — the run stops at the *true end*, the first moment no sign is pressed under two or more remaining cards. Used for questions 1–3.
  - **sweep** — the real rule. The game ends only by a successful Sweep. A failed Sweep shows every pressed face to everyone and passes the turn. With fewer than 2 cards left, sweeping is the only move.
- **Bots:**
  - `random` — flips any two cards. The mechanics floor.
  - `perfect` — remembers every flipped card.
  - `forget-K` — remembers the last K cards flipped (K = 10, 6, 4).
  - `counter` — perfect memory plus registry counting. It sweeps exactly at the true end, except when trailing by more than the Sweep is worth: then it refuses and makes the safest miss. Mid-game it avoids flips that press a sign already pressed elsewhere.
  - `memory` — perfect memory, no counting. Sweeps once every remaining card is known and pair-free.
  - `gambler` — last-6 memory, no counting. Sweeps at 4 or fewer cards.

  Memory bots use the pair-uniqueness rule for their second flip: a card showing the sign just revealed cannot be hiding it.
- **Volume:** 2,000 games per configuration. Head-to-heads are seat-randomised (2,000 games in each seating, 4,000 per row). There are about 130,000 games in total: 16,000 natural-end, 20,000 memory head-to-head, 60,000 Sweep-rule, 14,000 tiebreak (§3.4) and 20,000 on the seven-sign subset (§3.5).
- **Turn cap:** 2,000 guesses; reaching it counts as a stall.
- **Reproduce:** `python afterimage_sim.py --run` (seeded; default `--games 2000 --seed 0`). This combines and supersedes the two scratch sketches (`flatmem_sim.py`, `flatmem_sweep_sim.py`) used during the concept conversation.

## 3. Results

### 3.1 Natural end

| Config | Ended | Guesses (median / max) | Cards left (mean) | Seat 0 / 1 / … / tie |
|---|---:|---:|---:|---|
| 2P random v random | 100% | 148 / 310 | 5.1 | 47 / 44 / tie 9 |
| 2P perfect v perfect | 100% | 29 / 34 | 4.0 | 44 / 47 / tie 10 |
| 2P forget10 ×2 | 100% | 31 / 38 | 4.1 | 45 / 45 / tie 9 |
| 2P forget6 ×2 | 100% | 34 / 42 | 4.1 | 48 / 43 / tie 10 |
| 2P forget4 ×2 | 100% | 40 / 54 | 4.1 | 49 / 42 / tie 9 |
| 3P perfect ×3 | 100% | 29 / 33 | 4.0 | 27 / 28 / 31 / tie 14 |
| 4P perfect ×4 | 100% | 29 / 33 | 4.0 | 21 / 19 / 21 / 20 / tie 19 |
| 4P forget6 ×4 | 100% | 34 / 44 | 4.1 | 17 / 20 / 23 / 20 / tie 21 |

**Cards left at the true end (2P perfect):** 0: 1.2% · 2: 24.0% · 4: 48.1% · 6: 24.4% · 8: 2.1%.

**A pressed pair is still present when the table first reaches k cards (2P perfect):**

| k | 2 | 4 | 6 | 8 | 10 |
|---|---:|---:|---:|---:|---:|
| pair present | 5% | 40% | 81% | 99% | 100% |

At 4 cards a pair is still there 40% of the time, and at 6 cards 81%, so **no fixed card count can end the game**: at any threshold, either matches are left or the game ends too late. Some games that reach 4 cards with a pair still present end at 4 anyway: a miss swaps two cards' faces and can break the pair up without anyone taking a card.

**Opening luck:** the first guess of the game is a blind match 11.2% of the time.

### 3.2 Memory head-to-head (natural end, seat-randomised, 4,000 games per row)

| A v B | A wins | B wins | Ties |
|---|---:|---:|---:|
| perfect v random | 100.0% | 0.0% | 0.0% |
| perfect v forget10 | 72.3% | 20.4% | 7.3% |
| perfect v forget6 | 92.5% | 4.7% | 2.9% |
| perfect v forget4 | 98.5% | 0.8% | 0.7% |
| forget6 v random | 100.0% | 0.0% | 0.0% |

### 3.3 Sweep end rule

**Sweep worth 1** (2,000 games per row):

| Config | Stalls | Guesses (median) | Extra guesses after true end (mean / max) | Failed sweeps per game | Refusals per game | Sweep point decided result | Wins |
|---|---:|---:|---:|---:|---:|---:|---|
| 2P counter ×2 | 0 | 28 | 0.34 / 5 | 0.00 | 0.30 | 7.3% | 49 / 45 / tie 7 |
| 2P memory ×2 | 0 | 30 | 1.39 / 6 | 0.00 | 0.00 | 8.8% | 45 / 46 / tie 8 |
| 2P gambler ×2 | 0 | 35 | 0.85 / 10 | 0.37 | 0.00 | 11.1% | 48 / 45 / tie 7 |
| 2P counter(s0) v memory | 0 | 29 | 0.74 / 8 | 0.00 | 0.19 | 9.0% | 66 / 26 / tie 8 |
| 2P memory(s0) v counter | 0 | 29 | 0.75 / 6 | 0.00 | 0.17 | 8.0% | 25 / 67 / tie 8 |
| 2P counter(s0) v gambler | 0 | 30 | 0.22 / 5 | 0.10 | 0.01 | 2.8% | 96 / 3 / tie 1 |
| 2P gambler(s0) v counter | 0 | 30 | 0.20 / 6 | 0.10 | 0.01 | 1.9% | 2 / 97 / tie 1 |
| 3P counter ×3 | 0 | 29 | 0.58 / 4 | 0.00 | 0.53 | 12.8% | 26 / 31 / 31 / tie 11 |
| 4P counter ×4 | 0 | 29 | 0.88 / 7 | 0.00 | 0.82 | 14.2% | 20 / 21 / 22 / 20 / tie 17 |

Seat-randomised (4,000 per row): counter beats memory **64.4% / 27.3%** (ties 8.3%); counter beats gambler **96.6% / 2.3%**; memory beats gambler **92.5% / 5.8%**.

**Sweep worth 2:** still 0 stalls, and the after-play is similar (mean 0.26–1.35 extra guesses). But the Sweep point decides the result far more often: **13.4% (2P counter), 16.9% (2P memory), 22.6% (3P), 28.4% (4P)**. Counter beats memory 69.5% / 24.2%.

"Sweep point decided result" means the sweeper won outright and would not have been strictly ahead without the Sweep point.

### 3.4 Tiebreak rules (Sweep worth 1, 2,000 games per row)

Seat win % after the tiebreak, with the share of games still tied.

| Config | Shared win: ties · seats | Sweeper wins ties: ties · seats | Most recent pair wins ties: ties · seats |
|---|---|---|---|
| 2P counter ×2 | 6.7% · 45 / 48 | **0.0%** · 48 / 52 | 0.0% · 48 / 52 |
| 2P memory ×2 | 9.1% · 47 / 44 | **0.0%** · 52 / 48 | 0.0% · 52 / 48 |
| 2P gambler ×2 | 7.0% · 48 / 45 | **0.0%** · 51 / 49 | 0.0% · 51 / 49 |
| 3P counter ×3 | 11.7% · 27 / 32 / 29 | **0.0%** · 30 / 36 / 33 | 1.4% · 30 / 35 / 33 |
| 3P memory ×3 | 13.6% · 28 / 29 / 29 | **3.0%** · 33 / 32 / 32 | 2.8% · 32 / 32 / 33 |
| 4P counter ×4 | 16.2% · 21 / 22 / 21 / 20 | **0.1%** · 25 / 26 / 25 / 24 | 3.5% · 25 / 25 / 23 / 23 |
| 4P memory ×4 | 20.1% · 18 / 19 / 22 / 20 | **6.3%** · 21 / 24 / 26 / 23 | 5.3% · 22 / 24 / 26 / 23 |

Both breakers remove almost every tie, and neither skews seats: the largest gap between seats is 5.6 points (3P counter, sweeper rule), against 4.6 with shared wins. They differ by under 4 points of residual ties anywhere. The sweeper rule is adopted (§5) because it rewards the counting skill and needs no record of who took which pair last.

### 3.5 First-game subset: signs 1–7 (21 cards)

| Config | Result |
|---|---|
| 2P perfect ×2, natural end | 100% ended · median 16 guesses (max 20) · 3.2 cards left · first guess a blind match 13.3% |
| 2P forget4 ×2, natural end | 100% ended · median 20 guesses (max 30) |
| perfect v forget4 (seat-randomised, 4,000) | 83.6% / 10.3% / ties 6.1% *(full deck: 98.5% / 0.8%)* |
| perfect v forget2 (seat-randomised, 4,000) | 95.9% / 1.9% / ties 2.2% |
| 2P counter ×2, Sweep 1, sweeper wins ties | 0 stalls · median 16 guesses · seats 49 / 51 |
| 2P counter v memory, both seatings | counter wins 71% |
| 2P gambler ×2 | 0 stalls · median 19 guesses · seats 51 / 49 |

The subset is about half as long and the memory gradient is gentler: a last-4 memory wins 10% against perfect recall instead of under 1%. Counting still beats memory alone by more than 2:1, so the skill layer survives. It plays cleanly and is adopted as the first-game variant.

## 4. Health checks

- **Stalls:** none. All 16,000 natural-end games reach the true end, including random play. There were 0 stalls in the 36,000 Sweep-rule games in the tables, and the 24,000 Sweep-rule head-to-head games also all ended (the head-to-head report would fail on a stalled game).
- **After-play:** under the Sweep rule a game runs on average 0.2–1.4 guesses past the true end, and at most 10. The ending is crisp.
- **Seat fairness:** acceptable, with one thing to watch. In the 2P mirrored configurations the gap between seats runs from −3 to +7 points: perfect ×2 44 / 47, counter ×2 (Sweep) 49 / 45, forget6 ×2 48 / 43, forget4 ×2 49 / 42. With 2,000 games the standard error per seat is about 1.1 points, so the forgetful-bot gaps are probably real. That suggests a small first-player edge when memory is poor, since the first player gets the first blind shots. At 4P each seat wins 19–22%.
- **Skill gap:** very wide. Perfect memory beats random 100%. Within skilled play, counting beats memory alone by more than 2:1. This is the opposite of the thin-gap warning sign. The risk instead is **steepness**: a small difference in recall (6 → 4 cards) moves a bot from winning 5% to under 1% against perfect memory.
- **Ties:** 7% (2P) to 17% (4P) with Sweep worth 1. A tiebreaker is needed.
- **Estimated real-time length:** bots take a median of 29 guesses (perfect) to 34–40 (last-6 to last-4 memory). At ~10–15 s per guess plus 2–3 min of layout, that is about 10–15 minutes.

## 5. Changes adopted

- **End rule: the Sweep, worth 1 point.** It is the only rule tested that ends cleanly without a fixed threshold. Worth 2 lets the Sweep decide 13–28% of results, which is too swingy for a reward that comes from counting at the very end.
- **No fixed card-count end** (ruled out by §3.1).
- **Tiebreaker: the successful sweeper wins a tie they are in; otherwise the tie is shared** (§3.4). Residual shared wins: 0% at 2P, 0–3% at 3P, 0–6% at 4P. Reversible; "most recent pair wins ties" is the near-identical alternative.
- **First-game variant: signs 1–7, 21 cards** (§3.5).

These became **design v0.1**, the first rulebook: [AFTERIMAGE_rulebook.md](AFTERIMAGE_rulebook.md).

## 6. Caveats for the first table test

- **Memory model.** Bots forget as "the last N cards flipped". Humans forget by salience, by grid position and by sign. They also misremember with confidence, which bots never do. The forget-K bots bracket a plausible range; they do not model it.
- **Counting at the table.** The `counter` bot does the registry sum exactly every turn. Humans will do it rarely, late, and sometimes wrongly. Whether that late "I know it's safe" moment feels fun or like homework is the key feel question.
- **Refusing to sweep.** A trailing counter that knows the game is over may keep guessing instead of sweeping (0.2–0.8 times per game in the sim). The leader then sweeps on their turn, so it never stalled. A deliberate miss can also *re-open* the game by pressing two shown faces that create a new hidden pair. Watch whether this reads as clever or as stalling.
- **Sideways marking.** The sim's bots know which cards have been flipped. A quarter-turn marker gives humans the same knowledge. Its effect on difficulty is not simulated.
- **Not modelled:** table talk (the rulebook forbids naming pressed signs aloud), cards being nudged out of the grid, and the time cost of the wash-shuffle and layout.
