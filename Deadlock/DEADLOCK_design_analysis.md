# DEADLOCK — design analysis (draft v0.1)

*November 2026 · simulation of [DEADLOCK_rulebook.md](DEADLOCK_rulebook.md) v0.1 · simulator: [deadlock_sim.py](deadlock_sim.py)*

**Verdict: stays In development.** No stalls and a strong skill gap, but the rules as the concept wrote them give the first mover (**North**) about 70% of careful games, rising to 78% with a deeper bot. A South bonus of 1 point balances the deeper bot but over-corrects for the shallower ones, and leaves a third of games decided by the Crown tiebreak. The designer must choose a seat-balance rule before DEADLOCK goes to a table.

## 1. Questions

From [DEADLOCK_concept.md](DEADLOCK_concept.md) and the simulation standards:

1. Does the game always end? (Structurally yes: 36 claims.)
2. Does skilled play clearly beat random (~1.5× or better)? Is the obvious line already the ceiling?
3. Is it seat-fair between North (first) and South (second, and last)?
4. Does flipping matter, or is DEADLOCK just a majority game an ordinary deck could run?
5. The concept's falsification worry: are the last ten claims forced because every line is already decided? Do the diagonals help?
6. Is the concept's "a won line scores 2–6" true in play?

The shelf format itself (days between moves, knocked cards, whose-move questions) cannot be simulated; §7 lists it for the table.

## 2. Method

- **Ruleset modelled:** the v0.1 draft *without* South's provisional +1. A random 6 × 6 deal of all 36 cards; North and South alternate; a move claims any open card with either face showing; claimed cards are locked. Twelve lines (rows and columns); 4+ of 6 wins a line; a won line scores the largest count of one shown sign among all six cards; most points wins; ties go to Crowns on your own cards, then a draw. **Watchtower** variant: the two long diagonals as well (14 lines). Seat compensation (South +½ to +2½) is evaluated **post hoc** from the same games. That is valid because no bot knows the komi: they maximise the margin, which a komi does not change.
- **Physical handling:** perfect information, and an open card's shown face is inert (the claimer may flip), so face randomisation only sets defaults. Not modelled: knocked or mis-squared cards, misreading North vs South, the days between moves, table talk.
- **Bots:**
  - *Random*: uniform over (open card, face). Mechanics floor.
  - *Greedy*: the strategy notes as a one-ply score. Each line is valued at (P win − P loss) × likely value, with the open cards treated as a fair coin race to four and each open card counting ½ toward a sign's concentration. It flips to concentrate in its lines and dilute the rival's, and poisons lines it cannot win. A small bonus for showing a Crown.
  - *Skilled*: Greedy plus an exact search of the last 6 claims.
  - *Lookahead*: two-ply (top 12 one-ply moves, each against the rival's best one-ply reply) plus the same endgame search. The depth check, because a one-ply bot is a floor, not a ceiling.
  - *NoFlip*: Skilled forbidden to flip. The deck-necessity probe.
- **Volume:** 1,000 games per row (2,000 for Random self-play), **18,000 games** in total, seed 1, about 13 minutes. A second seed for the Skilled self-play row. Turn cap 600 (it can never be reached). The two-field match is built from consecutive Skilled self-play games (500 matches).
- **Exact solve:** not feasible. One deal has about **2.1 × 10²⁴** reachable positions (Σₖ C(36,k)·C(k,⌈k/2⌉)·2ᵏ: which cards are claimed, by whom, showing which face), and every deal is a different game. SNARE's exact seat solve has no counterpart here; seat fairness rests on seeded self-play at three bot depths.
- **Reproduce:** `python deadlock_sim.py --run --games 1000 --seed 1`.

## 3. Structure checks (computed, not asserted)

| Claim | Result |
|---|---|
| Deck fills the field | 36 cards, every sign on 8; the 6 × 6 field uses all 36 |
| Lines | 12; every card is in exactly 2 (one row, one column) |
| Lowest value a random line can be held to (20,000 sampled lines, all 2⁶ face choices) | **1** in 98.2%, 2 in 1.8%. The concept's "2–6" is really **1–6** |
| Highest value a random line can reach | 2: 23.3% · **3: 63.6%** · 4: 12.3% · 5: 0.8% · 6: 0.0% |
| Turn check (North on equal counts, South when North is one ahead) | holds after every move of every game (asserted in the sim) |

The concentration ceiling is low: even with every face in its favour, two lines in three cannot exceed 3.

## 4. Results (base game, 12 lines)

### 4.1 Seat spread, self-play

| Bots | North wins | South wins | Draws | Points N–S | Lines won N–S | Crown tiebreak |
|---|---:|---:|---:|---|---|---:|
| Random (2,000) | 46.9% | 49.9% | 3.2% | 8.0–8.1 | 3.95–3.97 | 12.3% |
| Greedy | 71.1% | 26.4% | 2.5% | 12.2–11.5 | 4.87–4.54 | 24.1% |
| Skilled | **71.9%** | 25.1% | 3.0% | 12.1–11.4 | 4.85–4.54 | 25.1% |
| Skilled, second seed | 69.1% | 27.7% | 3.2% | 12.1–11.4 | 4.84–4.54 | 25.5% |
| Lookahead | **78.0%** | 18.2% | 3.8% | 12.5–11.6 | 5.19–4.85 | 22.2% |

95% intervals are about ±2.8 points. The edge is absent in random play and **grows with depth**: it comes from tempo in line races (careful North wins about 0.3 more lines a game), not from a bot artefact.

### 4.2 Seat-fix candidates (post hoc on the same games)

North wins / South wins:

| South bonus | Greedy | Skilled | Skilled, seed 2 | Lookahead | Tied on points (Crowns decide) |
|---|---|---|---|---|---:|
| none (concept) | 71.1 / 26.4 | 71.9 / 25.1 | 69.1 / 27.7 | 78.0 / 18.2 | 22–25% |
| +½ (South wins ties) | 57.2 / 42.8 | 57.9 / 42.1 | 55.2 / 44.8 | 64.6 / 35.4 | 0% |
| **+1, ties to Crowns** (draft) | 39.6 / 56.5 | 40.3 / 56.7 | 37.5 / 59.3 | **47.2 / 48.3** | **31–34%** |
| +1, ties drawn | 24.8 / 42.8 | 24.0 / 42.1 | 24.3 / 44.8 | 31.1 / 35.4 | 31–34% drawn |
| +1½ | 24.8 / 75.2 | 24.0 / 76.0 | 24.3 / 75.7 | 31.1 / 68.9 | 0% |

**Two-field match, seats swapped (Skilled, 500 matches):** A 45.0% · B 52.6% · drawn 2.4% (±4.4%; fair by construction, so the gap is noise). 24.4% of matches tie on points and go to Crowns.

The right bonus grows with skill (mean North margin +0.70 Greedy, +0.73 Skilled, +0.95 Lookahead), and because scores are small whole numbers, the result jumps in big steps: half a point moves North from 58% to 40%. No single-field bonus lands inside 55/45 for every bot depth.

### 4.3 Skill gap and deck necessity

| X v Y (seats alternated) | X wins | Y wins | Draws | Points X : Y | Ratio |
|---|---:|---:|---:|---|---:|
| Greedy v Random | 100.0% | 0.0% | 0.0% | 17.0 : 6.7 | 2.53× |
| **Skilled v Random** | **100.0%** | 0.0% | 0.0% | 16.7 : 6.8 | **2.47×** |
| Skilled v Greedy | 50.7% | 46.3% | 3.0% | 11.8 : 11.7 | 1.01× |
| Lookahead v Skilled | 62.4% | 34.8% | 2.8% | 12.3 : 11.8 | 1.05× |
| **Skilled v NoFlip** | **76.0%** | 21.9% | 2.1% | 11.3 : 10.0 | 1.14× |

- The obvious line already beats random 100% of the time. The exact six-card endgame adds nothing over it (50.7%), but **two-ply lookahead beats it 62%**, so there is more to find with depth.
- **Flipping is load-bearing.** A player who may not flip loses three games in four to one who may, at equal territory skill. Value-setting is a smaller share of the score than territory (1.14×), but it decides games.

### 4.4 The last ten claims

| | Random | Greedy | Skilled | Skilled, seed 2 | Lookahead |
|---|---:|---:|---:|---:|---:|
| Lines still undecided with 10 cards left (of 12) | 8.9 | 5.7 | 5.7 | 5.7 | 5.3 |
| Leader (by the bot's evaluation) with 10 left goes on to win | 72.8% | 69.7% | 66.8% | 69.3% | 75.9% |

The concept's fear is **not borne out** in simulation: roughly half the lines are still live with ten cards left, and the side that is ahead then loses about a third of careful games.

### 4.5 Line values in play

Won-line values, careful self-play: 1: 1% · **2: 50–51%** · **3: 45–46%** · 4: 3% · 5–6: 0%. Random play: 2 in 71%. A won line is worth 2 or 3, so totals cluster tightly (about 12 each), which is why ties on points are so common.

### 4.6 Watchtower variant (14 lines)

| | Random | Greedy | Skilled |
|---|---|---|---|
| North / South | 45.6 / 51.8 | 78.2 / 19.4 | **77.7 / 19.1** |
| North margin | −0.19 | +1.08 | +1.09 |
| Live lines with 10 left (of 14) | 10.4 | 6.3 | 6.3 |
| Leader with 10 left wins | 74.0% | 73.2% | 76.0% |

Skilled v Random 100% (3.01×); Skilled v Greedy 52.0%. The diagonals **widen** North's edge and do not make the endgame more open in proportion. They are not a fix for anything the sim can see.

## 5. Health checks

| Check | Result | Status |
|---|---|---|
| Stalls | 0 in 18,000 games; termination is structural (36 claims) | Pass |
| Skill gap | Skilled v Random 100% wins, 2.47× points; Lookahead beats Skilled 62% | Pass |
| Seat spread (concept rules) | North 69–72% one-ply, 78% two-ply | **Fail** |
| Seat spread (draft South +1) | North 37.5–40.3% one-ply, 47.2% two-ply | Borderline: over-corrects for beginners |
| Seat spread (two-field match) | fair by construction | Pass, at double length |
| Deck necessity | no-flip player loses 76%; all-pairs deck sets which signs can share a line | Pass |
| Tie frequency | Crowns decide 22–25% of careful games (31–34% with South +1) | **Risk** |
| Real-time length | 36 claims; one sitting about 20–30 min (estimate), or days on a shelf | Estimate only |

## 6. Changes adopted in the draft

- **South's watch (+1 point)** is added as a **provisional** seat rule, because it is the single-field option closest to even at the deepest bot depth. It is not in the concept.
- The concept's turn rule (count claimed cards, even = North) is kept, with the **open-card count** as the same check from the other side and the **North-vs-South count** as a disturbance check.
- A **one-sitting** mode is stated explicitly, and recommended for the first game.
- **Repairs** and an **optional photo** are added for the shelf mode. Neither is in the concept.
- Line value is stated as 1–6, not 2–6 (§3).
- Watchtower (diagonals) is a variant, not a fix.

The full list of open choices is in the rulebook's **Decisions to review**.

## 7. The decision the designer must make

**Pick a seat-balance rule.** Measured options:

- **South +1, ties to Crowns** (draft). Closest to even for strong play (47/48), but South wins 57–59% between one-ply players, and a third of games go to Crowns.
- **South wins ties (+½).** No Crown deciders at all, but North still wins 55–58% (one-ply) and 65% (two-ply).
- **Two-field match, seats swapped.** Fair by construction, no new scoring rule; a quarter of matches tie on points; twice as long, which for a shelf game means weeks.
- Untested ideas: a pie rule after North's first claim (South may take North's seat), or South claiming two cards on their first move. Both change the self-computing turn check, and would need a sim run.

The tie problem (§4.5) is connected: with won lines worth only 2 or 3, any scoring change that widens the spread would also make a points bonus less jumpy.

## 8. Caveats for the first table test (once the seat rule is chosen)

- **The format is the experiment.** The sim says nothing about whether one move per passing is pleasant, whether players forget the game exists, or whether "whose move?" ever has to be asked. The concept's own falsification test stands.
- **Handling over days:** knocked and swept cards, whether a half turn (North vs South) reads at a glance, the 60 × 60 cm footprint, the turn-count chore late in the game, and whether anyone wants a record. The rulebook's *Multi-day handling risks* list is the checklist.
- **Human depth.** Players will sit somewhere between Greedy and Lookahead at first; the right South bonus depends on where.
- **Scoring feel.** Does counting twelve lines at the end feel like a payoff or like bookkeeping, and do Crown tiebreaks feel earned or arbitrary?
- The sim cannot judge fun, table talk across days, or the pull of "kitchen diplomacy".
