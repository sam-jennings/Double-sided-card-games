# SNARE — design analysis (draft v0.1)

*November 2026 · simulation and exact solve of [SNARE_rulebook.md](SNARE_rulebook.md) v0.1 · simulator: [snare_sim.py](snare_sim.py)*

**Verdict: stays In the workshop.** No stalls and a strong skill gap, but the single game is a **forced second-claimer win**, careful play finds that win with simple rules of thumb, and the concept's pie rule cannot repair it. The designer must choose a seat-balance rule before SNARE goes to a table.

## 1. Questions

From [SNARE_concept.md](SNARE_concept.md) and the simulation standards:

1. Does the game always end? (Structurally yes: one claim per turn, 15 roads.)
2. Does skilled play clearly beat random play (~1.5× or better)? Is the obvious line already the ceiling?
3. Is it seat-fair? Does the concept's pie rule on the opening claim fix any seat edge?
4. Does the Goodman count beat sudden death (*Sim*) as the base win condition?
5. Does the five-sign rung really allow earned draws, and does six signs really force a snare?
6. Can the table *see* every triangle? The draft's staircase layout claims every snare is a house-cornered rectangle.

## 2. Method

- **Ruleset modelled:** the v0.1 draft. Players alternate claiming one open road; the first claimer takes 8 roads and the second 7. **Tally** (base): fewer snares wins; a tie goes against whoever was snared first; 0–0 is a draw (possible only on five signs). **Sudden** (variant): the first player snared loses. Both rules on six signs (15 roads) and on the five-sign Pentagon (10 roads).
- **Physical handling:** perfect information, and the shown face of a road is inert, so face randomisation is irrelevant. Not modelled: misreading a rectangle, a knocked card, table talk.
- **Bots:**
  - *Random*: uniform legal claim (the mechanics floor).
  - *Greedy*: the beginner-obvious line. Never complete your own snare when another road is available.
  - *Skilled*: the rulebook's strategy notes as a one-ply score (avoid your poison, don't take the rival's poison, avoid lighting fuses, prefer dead triangles), plus exact counting once 7 or fewer roads remain.
  - *Perfect*: full minimax (the exact game value).
- **Exact solver:** memoised minimax over every reachable position (55,064 positions for the tally game on six signs, 112,096 for sudden death).
- **Volume:** 2,000 games per self-play and head-to-head row (400 for rows with the Perfect bot), plus 2,000 two-game matches per match row. **87,200 games in total**, seed 1, about 60 seconds. Turn cap 600 (it can never be reached: every game is exactly 15 or 10 claims).
- **Reproduce:** `python snare_sim.py --run --games 2000 --seed 1`.

## 3. Structure checks (computed, not asserted)

| Claim | Result |
|---|---|
| Six signs: roads / triangles | 15 / 20 |
| Every triangle is a rectangle of three roads plus one house on the staircase, and vice versa | **True**; 20 house-cornered rectangles = 20 triangles |
| 8/7 splits of K₆ (as actually played): total snares | min **2**, mean **4.00**, max 7; zero-snare splits: **0** of 6,435 |
| Five signs, 5/5 splits with no snare at all | **12** exist, so a drawn Pentagon is a real result |
| Opening claim | unique up to relabelling the signs (the symmetric group acts transitively on edges), so **any pie rule on the first claim is inert** |
| Six signs minus one road, 7/7 splits | snare-free splits **exist** (12 for a given removed road); the "someone must be snared" guarantee needs all 15 roads |

These confirm the concept's Goodman framing: on six signs the two players always share at least two snares between them.

## 4. Results

### 4.1 Exact game values

| Game | Value under perfect play |
|---|---|
| SNARE, tally (base) | **second claimer wins** |
| SNARE, sudden death (*Sim*) | second claimer wins (matches the known result, which validates the solver) |
| Pentagon, tally | draw |
| Pentagon, sudden death | draw |

### 4.2 Six signs, tally (base game)

Self-play seat spread:

| Bots | First wins | Second wins | Draws | Mean snares (1st–2nd) |
|---|---:|---:|---:|---|
| Random | 22.1% | 77.8% | 0% | 2.50–1.54 |
| Greedy | 26.9% | 73.2% | 0% | 1.98–0.90 |
| Skilled | **0.0%** | **100.0%** | 0% | 2.00–0.00 |
| Perfect | 0.0% | 100.0% | 0% | 2.00–0.00 |

Head-to-head, seats alternated:

| X v Y | X wins | Y wins | Snares X : Y | Snare ratio |
|---|---:|---:|---|---:|
| Greedy v Random | 72.5% | 27.5% | 1.37 : 2.07 | 1.51× |
| **Skilled v Random** | **97.8%** | 2.2% | 0.74 : 2.48 | **3.36×** |
| Skilled v Greedy | 93.3% | 6.7% | 0.69 : 1.88 | 2.71× |
| Perfect v Skilled | 50.0% | 50.0% | 1.00 : 1.00 | 1.00× |

Perfect v Skilled at 50/50 means Skilled already plays perfectly from the second seat: whoever sits second wins.

An ad-hoc check with the Skilled bot's exact endgame turned **off** (pure one-ply strategy notes, 1,000 games): self-play still went 0% / 100%, with snares 2.00–0.00. **The second claimer's win needs no deep counting.** The rules of thumb in the rulebook are enough to find it.

### 4.3 Sudden death and the Pentagon (summary)

| Configuration | Skilled self-play | Skilled v Random | Greedy v Random |
|---|---|---|---|
| Six signs, sudden death | 100% second claimer | 99.9% wins | 88.5% wins |
| Pentagon, tally | 100% drawn (0–0) | 96.2% wins, 3.8% drawn | 69.8% wins |
| Pentagon, sudden death | 100% drawn | 96.4% wins | 69.0% wins |

The Pentagon behaves as the concept hoped: careful players always escape and the draw is the expert result. Random players are snared there about once a game (0.83 snares each).

### 4.4 Seat-fix candidates (six signs, tally)

| Candidate | Exact value | Skilled self-play | Greedy self-play | Skilled v Random | Cost |
|---|---|---|---|---|---|
| **A. Pie on the opening claim** (concept) | unchanged | unchanged | unchanged | — | Inert, proved by symmetry |
| **B. Two-game match, seats swapped** (draft) | match drawn | **100% drawn matches** | 42.0 / 41.9 / 16.1% drawn | 100% match wins | Fair by construction, but strong players always draw |
| **C. Leave the last road unclaimed** (7/7) | draw | 100% drawn, 0–0 | 54.1 / 33.8 / 12.1% drawn | 99.9% wins | Snares become avoidable; experts never get snared |
| **D. Set one road aside before play** (7/7) | first claimer wins | **50.0 / 50.0%**, snares 0.70–0.76 | 50.0 / 47.9% | 99.7% wins | Snares avoidable in principle; the perfect-play edge is hidden but exists |

Under the match (B), random-v-random matches split 46.3 / 47.4% with 6.3% drawn; 73–75% of non-skilled matches are decided on total snares, the rest by the survival tiebreak. An extra ad-hoc seed (seed 5, 2,000 games) put D's skilled self-play at 48.7 / 51.4%.

## 5. Health checks

| Check | Result | Status |
|---|---|---|
| Stalls | 0 in 87,200 games; termination is structural | Pass |
| Skill gap | Skilled v Random 97.8% wins, 3.36× fewer snares; the obvious Greedy line already reaches 1.51×, and Skilled beats Greedy 93% | Pass |
| Seat spread (single game) | Second claimer wins 74–78% between beginners and **100%** between careful players; forced win under perfect play | **Fail** |
| Seat spread (match, draft rule B) | Even by construction; 42/42 between beginners | Pass, but see flatness |
| Flatness at the top | Careful play produces the same 2–0 result every game; matches between careful players are all drawn | **Risk** |
| Real-time length | 15 claims per game, about 5–8 minutes; a match fits the 10–15 minute banner | Estimate only |

The skill gap is real but **the seat is decisive**, and the strategy that exploits it is easy. Humans will be far from the Skilled bot at first, but even naive play (Greedy) gives the second claimer 73%.

## 6. Changes adopted in the draft

- The concept's pie rule is **dropped** because it provably does nothing. A seat-swapped two-game match stands in as a provisional rule.
- The concept's hex layout is replaced by the **staircase** (houses on a diagonal), because a hex cannot show the three long diagonals without crossing cards, and because the staircase makes every snare the same visible shape.
- The Goodman count is the base game, sudden death a variant, and the Pentagon a first-game variant. The concept's own leanings decided all three.

The full list of open choices is in the rulebook's **Decisions to review**.

## 7. The decision the designer must make

**Pick a seat-balance rule.** The evidence points two ways:

- **Keep the full 15 roads and the inevitability hook** (B, or something new). Then accept that experts draw, or find a different asymmetry. One untested idea is a handicap for the 8-road player. Its size must be at least the 2–0 gap careful play produces.
- **Set one road aside (D).** Careful players split about 50/50 with real snares on both sides, and the strategy notes stop finding a forced line. The price is the headline: on 14 roads a snare-free finish exists, so "somebody must be snared" becomes "somebody almost always is".

## 8. Caveats for the first table test (once the seat rule is chosen)

- **Legibility is the make-or-break.** The concept's own risk is that humans cannot see triangle threats, so a loss feels arbitrary. The staircase-rectangle rule is the bet. Watch whether players spot poison roads unprompted.
- **Footprint and handling.** About 60 × 60 cm of cards. Does the slanted-equals-open convention survive elbows and reaching across?
- **The 5→6 moment.** Does the Pentagon-then-SNARE ladder make players *feel* the threshold, or is it just a longer second game?
- **Mood versus CROSSROADS.** Both are two-player, perfect-information abstracts. The table has to confirm that avoidance feels different.
- The sim cannot judge fun, the human gap from the Skilled bot, or whether the end-of-game count feels satisfying or like bookkeeping.
