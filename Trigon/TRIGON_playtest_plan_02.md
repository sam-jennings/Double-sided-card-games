# TRIGON — Playtest Plan 02

*Pairs with the forthcoming `TRIGON_playtest_02.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md). Hypotheses come from the "Next session should answer" list and rule-change candidates in [TRIGON_playtest_01.md](TRIGON_playtest_01.md), the `COLLECTION_OVERVIEW.md` outstanding questions, and the table questions in [TRIGON_design_analysis.md](TRIGON_design_analysis.md) §7. Numbered 02 to pair with the second session's report.*

## Open before the session

Playtest 01 called for five changes. Two were made, one is conditional, and the two that this session exists to test were **not** made. The rules stay as they are; the gaps are covered by session conventions below.

- **The grid is still undefined (Bug 1, HIGH — not applied).** Setup step 3 still says only "leave space for a 3×3 grid". The proposed centre-first line is not in the rulebook. **Session convention:** the **first card placed is the centre cell**; the grid is the eight cells around it, one step in each direction. Before the deal, say aloud which cells are corners, edges and the central cross.
- **There is no player aid (Bug 2, HIGH — not applied).** No aid file exists. The planned Nine Signs sheet (`Reference/NINE_SIGNS_SHEET.md`, per `Project/Decisions/HOUSE_KIT_DECISION_2026-07.md`) has not been written, and the rulebook's Components section doesn't mention one. **Session convention:** print the rulebook's nine-sign table (requirement, ability, mnemonic), **one copy per player**. It is a copy of existing text, not new rules. Close the laptop or rulebook once the aid is on the table.
- **The Leaf/Key relabel is adopted but not applied.** `HOUSE_KIT_DECISION_2026-07.md` D4 adopts it (Leaf = swap, Key = flip-adjacent). The rulebook still has **Leaf = flip an adjacent card, Key = swap any two**. Play the rulebook as written, and make sure the printed aid matches it. Don't mix the two.
- **Applied:** the requirement-vs-placement callout (Bug 3) is now the blockquote under Activations. The chaining FAQ (Bug 4: switch freely between chains; once per card per turn, whichever face is up) is in Edge cases. The removed pile is now kept sideways (Bug 6 / F9).
- **Conditional, not applied:** change 5 (start the strategy notes with "declining is usually right") was to be made only if a second game still feels aimless. The notes still start with "Showing a sign feeds it". This session decides it (H5).

## Setup

- **Game:** TRIGON
- **Version:** v1.2 rules, plus the two session conventions above (centre-first grid, printed aid).
- **Players:** 2. This is the first 2P table; playtest 01 was 3P. 18 turns each, full deck.
- **Symbol subset:** all 9 signs / 36 cards.
- **Session shape:** two games, ~20–25 minutes each.
  1. **Game 1:** full v1.2 (Star wild) if both players have played before. Use **Calm Signs** (Star not wild) if either player is new, since playtest 01 skipped it. Centre-first, **no mat**.
  2. **Game 2:** full v1.2, swap the start player. If game 1 had any grid-drift incident, play game 2 on a **drawn 3×3 grid** (paper, outlines only), the C2 control arm in `Project/Playtesting/PROTOTYPE_KIT_2026-07.md`. Otherwise stay centre-first only.
- **Why this session:** `next_step` is "retest at 2 players with a defined grid and a player aid". Playtest 01 left all four of its hypotheses open because the two HIGH handling bugs throttled the table. This session removes those two blockers and then asks whether the engine works.

## Hypotheses to test

Sim reference for v1.2 at 2P ([design analysis](TRIGON_design_analysis.md) §5–§6, greedy mirror, 1,500 games): **19.2 cards captured per game** (about 6 alignment captures, one every 5–6 turns), winning margin 5.6 cards, 9.3 forced full-grid discards. Activations per turn: **0.24** for skilled bots, **0.74** for random bots, **0.49** for a mixed table. Greedy beats random 96.3%.

- **H1 — Centre-first fixes the grid.** Bug 1. *Prediction:* no dispute in either game about whether a cell is a corner, edge or centre, and no card placed outside the 3×3. *Falsified if* any position-based requirement (Moon, Leaf, Mask, Star, Crown) is argued over or misjudged even once with centre-first alone. That points to a printed grid; whether to accept it is the designer's call.
- **H2 — One aid per player ends the reference stall.** Bug 2. *Prediction:* after turn 4 of game 1, the rulebook is opened **at most twice per game**, and game 2 finishes in **≤ 25 minutes**, the top of the banner range. 36 turns in 25 minutes is about 40 seconds a turn. *Falsified if* players still look up both faces' requirements every turn from the aid, or game 2 runs past 30 minutes. Then nine requirement+ability pairs is a load problem, not a lookup problem.
- **H3 — Capture cadence reads as periodic payoff.** Playtest 01 H1, left open. *Prediction:* each full v1.2 game has **≥ 4 alignment captures** (the sim's ~6 is a bot mirror) and **≥ 12 captured cards** in total, with no stretch of 10+ turns without a capture. *Falsified if* there are ≤ 2 captures (the engine isn't converting at the table), or players call it a grind.
- **H4 — "Active player captures everything" lands as drama.** Playtest 01 H3, left open. *Prediction:* at least one capture per game completes a line that the *other* player mostly built, and it gets an audible reaction ("oh no" / "nice"), not "that's not fair". *Falsified if* a stolen line produces a fairness complaint, or no line is ever stolen. The second would suggest 2P players simply never leave pairs.
- **H5 — Declining emerges by game 2 (the aimless-placement check).** Bug 5, binding lesson 6(a). *Prediction:* game 1's activation rate is near the random/mixed band (**≥ 0.5 per turn**). Game 2's is lower (**≤ 0.4 per turn**), and at least one decline is said aloud with a reason. *Falsified if* game 2 still fires nearly everything or a player again reports placing "arbitrarily". Then the skill is hidden behind a near-random obvious line, and change 5 (start the strategy notes with declining) should be made.
- **H6 — Charging is judged unaided by game 2.** Playtest 01 H4, leaning refuted. *Prediction:* in game 2 no one asks "is this card charged?" more than once. *Falsified if* charge-state questions continue at the game 1 rate.

## What to watch

Handling first:

- **Grid drift.** Log every moment a card's position class is unclear, and every placement outside the 3×3 frame. Note whether the centre card's identity is remembered after it is captured and its cell empties. That is the likeliest centre-first failure.
- **Aid use.** Tally glances at the aid against rulebook openings. Note which rows get looked up most. If it's the same two or three signs, the problem is those signs, not the table.
- **Chains.** Does anyone lose track of which cards are charged mid-chain? Are any chains of 3+ activations attempted, and do they stay resolvable without a referee? Playtest 01 flagged that "multi-chaining could become overwhelming".
- **Hidden faces.** Does either player try to remember a placed card's hidden face (Eye, flips)? Is it a chosen effort or a strain?
- **Piles.** Is the sideways removed pile ever mistaken for the deck? (F9 fix.)

Then:

- **Rare signs.** Eye (peek) and Flame (1–2 neighbours) were the sim's quietest abilities: 0.31 and 0.14 activations a game under their celestial-era names (Aurora, Meteor, §5). Note whether either fires at all. One session can't condemn them, but a 2P table that never wants them is worth recording.
- **Moon catch-up.** Does the losing player ever trigger Moon? Does it feel like a comeback or a consolation prize?
- **The deck top.** Is the public top card used to plan?

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Zero position disputes; no off-grid placements | Any disputed corner/edge/cross judgement |
| H2 | ≤ 2 rulebook openings per game after turn 4; game 2 ≤ 25 min | Per-turn look-ups persist; > 30 min |
| H3 | ≥ 4 captures, ≥ 12 cards, no 10-turn drought | ≤ 2 captures; "grind" |
| H4 | A stolen line draws a reaction, not a complaint | "Not fair"; or no line ever stolen |
| H5 | Game 2 ≤ 0.4 activations/turn; a reasoned decline voiced | Still firing everything; "arbitrary" placement |
| H6 | ≤ 1 charge-state question in game 2 | Charge questions unchanged |
| Handling | Chains resolved without a referee | Lost charge state mid-chain |

**Verdict framing:** H1 and H2 decide whether the handling fixes work. If both hold, the conventions are ready to write into the rulebook (a designer decision for the report). H3–H5 are the first real read of the engine. If H1/H2 hold but H5 fails, it's a teaching fix (lesson 6a), not a balance one.

## Teaching plan (retest: what to re-teach)

- Start with the **grid**: place the first card, name it as the centre, and point out the four corners, the four edges and the central cross before the first ability is read.
- Re-teach the **requirement-vs-placement** line word for word ("Requirements never restrict where you place a card").
- Re-teach **charging** with one example of each of the four triggers: placed, flipped, moved, requirement newly met. Then **once per card per turn, whichever face is up**.
- Hand out the aids. Don't re-read the ability table aloud; that's what the aid is being tested for.
- **Don't** read the strategy notes before game 1 (H5 tests whether declining is found unprompted). Read them between games if game 1 felt aimless, and note that you did.

## Record sheet

| | Game 1 | Game 2 |
|---|---|---|
| Variant (Calm Signs / v1.2) | | v1.2 |
| Grid method (centre-first / drawn grid) | | |
| Start player / winner / final cards | | |
| Grid-drift or position disputes (count) | | |
| Rulebook openings after turn 4 | | |
| Aid glances (rough tally) | | |
| Alignment captures (count) / cards captured | | |
| Longest capture drought (turns) | | |
| Stolen lines / reaction | | |
| Activations (count) ÷ 36 turns | | |
| Declines voiced with a reason | | |
| "Is it charged?" questions | | |
| Signs activated (✓ Moon Leaf Wave Flame Eye Mask Key Star Crown) | | |
| Longest chain (activations) | | |
| Removed-pile / deck confusions | | |
| Time | | |

- Did the aid replace the rulebook? Which rows were consulted most? ____
- Did anyone say they were placing "arbitrarily"? When? ____
- Strategy notes read between games? (Y/N) ____
- Surprises / quotes:

## Out of scope

- 3P and 4P. This session isolates the engine at 2P, as playtest 01 asked.
- Deep Signs and Shared Glory variants.
- The Leaf/Key relabel. Applying it is a rulebook decision; don't test both labellings in one session.
- Re-simulation. The sim answered balance; the open questions are handling and feel.
