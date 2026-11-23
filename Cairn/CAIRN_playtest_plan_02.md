# CAIRN — Playtest Plan 02

*Pairs with the forthcoming `CAIRN_playtest_02.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md). Hypotheses come from the rulebook's "Open playtest questions", the unanswered hypotheses in [CAIRN_playtest_plan_01.md](CAIRN_playtest_plan_01.md), the "Next recorded test" in [CAIRN_playtest_01.md](CAIRN_playtest_01.md), and the sim tables in `NEW_GAME_CONCEPTS.md` §13. Numbered 02 to pair with the second session's report.*

## Open before the session

**No rule changes are outstanding.** Playtest 01 is a retrospective record: the session's notes were lost in the July 2026 migration, so it observed nothing and called for no changes. The six questions in plan 01 are therefore still **unanswered**, not refuted. This session is effectively the first *recorded* test.

Two small points, neither a rules change:

- **Pathfinder had no sim calibration.** The original sweep covered 7 signs / 3 cairns / hand 4 but not hand 3. It was run for this plan (`cairn_sim.py --planning --configs 7/3/3`, seed 20260619; 2,000 floor deals, 120 planner/ceiling deals): random **23.9%** clear, greedy+peek **48.3%**, depth-2 expectimax **75.0%**, PIMC **76.7%**, ceiling **100%**. Use these as the Pathfinder band below.
- **Starting waymarks are chosen before the hand is drawn.** Setup has you choose each starting cairn's face (step 4) before drawing four cards (step 5), so the choice is blind. That is legal and clear as written. Note whether it feels like a wasted decision; don't change it.

## Setup

- **Game:** CAIRN
- **Version:** v0.1 (sim-validated; played once, unrecorded).
- **Players:** 1 (solo).
- **Symbol subset:** standard trail = **7 signs / 21 cards** (remove every card showing Star or Crown). 3 cairns, hand of 4, stock of 14.
- **Session shape:** about an hour, **five standard deals** first, because `next_step` is to repeat the standard trail:
  1. **Deals 1–5: standard trail.** Only the standard counts towards H1–H2.
  2. **Deal 6: Pathfinder** (hand 3), if time allows, to check the ladder's next step.
  - A **First Trail** warm-up (4 cairns) only if the player is new. The sim puts it at greedy 82% clear, "drifting easy", so it isn't evidence about the standard game.
- **Why this session:** `next_step` is "repeat the standard trail and record whether failure feels foreseeable". The outstanding questions are about how *repeated* play feels, which one deal can't show.

## Hypotheses to test

Sim reference (`NEW_GAME_CONCEPTS.md` §13, seed 20260619): standard **7 / K3 / H4** clears **41%** random, **71%** greedy, **74%** greedy+peek, **98%** depth-2 expectimax and PIMC, **100%** ceiling. Depth-2 lookahead matched 60-world PIMC, so planning two moves ahead is enough to play near-optimally. Pathfinder: see above.

- **H1 — A thoughtful player clears most standard deals.** *Prediction:* **≥ 4 of 5** standard deals cleared (0 stones left). Any loss leaves **≤ 2 stones**, and deals 4–5 are cleared. That puts the player between casual (74%) and careful (98%). *Falsified if* **≤ 2 of 5** clear, which is below the casual band: the rulebook isn't conveying the skill, or hand 4 is too tight at the table. Also falsified if all 5 clear with no scare at all (drifting easy, like First Trail's 82%).
- **H2 — Blocking reads as a foreseeable mistake.** Open question 2, the `next_step` question. *Prediction:* every loss can be traced, straight after the block, to a **named earlier turn**, for example "I topped the middle cairn with Key when only one Key card was left". *Falsified if* any loss is put down to "the draws" with no better line visible in hindsight. One such loss in five is plausible (the rulebook says a few deals are unwinnable). Two or more means draw-luck dominates at the table.
- **H3 — Chaining choices feel meaningful, not like arithmetic.** Open question 1. *Prediction:* on **at least a third of turns** the player weighs two or more legal plays and can give a reason (keep a sign alive, set up the free look, keep waymarks different). *Falsified if* most turns have one obvious play, or the player calls it "sorting".
- **H4 — The free look is found and used unprompted.** Open question 4. *Prediction:* by the end of deal 2 the player steers a placement to leave a home for the stock's visible top card, without being told. *Falsified if* the visible stock top is never used across five deals. It would then need to be in the turn steps, not a side paragraph.
- **H5 — Dead-cairn avoidance is discovered.** Strategy note 1. *Prediction:* after the first time a cairn is topped with a spent sign (a dead stack), the player starts counting remaining cards of a sign before exposing it. *Falsified if* dead stacks keep happening through deal 5 without the player noticing why.
- **H6 — Nothing buried matters.** Plan 01 H6, the anti-OUROBOROS claim. *Prediction:* no buried card is lifted or consulted in any deal. *Falsified if* the player wants to check under a top, e.g. to count which signs are already spent. That would mean the counting the game rewards secretly needs the buried cards.
- **H7 — Hand 4 is the right size, and Pathfinder bites.** Open questions 3 and 6. *Prediction:* the standard game has real scares but is cleared (H1). Pathfinder clears **about half to three-quarters** of the time (sim 48–77%), and the player feels it as harder, not merely luckier. *Falsified if* Pathfinder feels the same as standard, or feels like pure draw-luck. Then the ladder's middle rung is wrong.
- **H8 — The footprint is tray-sized.** Open question 5. *Prediction:* the whole game (three stacks, stock, held fan) fits about **30 × 40 cm**, and the hand of four is held, not laid down.

## What to watch

Handling first:

- **Placement orientation.** Every play puts the matched sign into the join and shows the *other* sign. Watch for the slip of placing the card showing the matched sign, which would leave a waymark that doesn't change.
- **Reading tops.** Are all three waymarks readable at a glance from the seat, including squared stacks of 7+ cards?
- **Stock top.** Does the stock's visible face ever get mistaken for a cairn, or a cairn for the stock?
- **Counting load.** Does the player count spent cards per sign in their head, or want a tally? Mental counting is the designed skill; a written tally would be a finding (not prohibited, but record it).

Then:

- **Blind starting waymarks.** Does choosing them before drawing feel like a non-decision?
- **The end squeeze.** Once the stock is empty and the hand shrinks, is that the tensest part, or a formality?
- **Replay pull.** After each deal, does the player want to reshuffle immediately?
- **Time.** The rulebook says ~10 minutes.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | ≥ 4/5 standard clears; losses ≤ 2 stones | ≤ 2/5 clears; or 5/5 with no scares |
| H2 | Every loss traced to a named turn | ≥ 2 losses blamed on the draws |
| H3 | Reasoned choices on ≥ ⅓ of turns | One obvious move; "sorting" |
| H4 | Free look used unprompted by deal 2 | Never used in five deals |
| H5 | Dead stacks stop after the first one | Dead stacks recur unnoticed |
| H6 | No buried card consulted | Wants to check under a top |
| H7 | Pathfinder ~½–¾ and feels harder | Same as standard, or pure luck |
| H8 | Fits ~30 × 40 cm; hand held | Sprawls; hand laid down |

## Teaching plan (retest: what to re-read)

The rulebook is the teacher. For a player who has played before, re-read only:

- **Core idea**: the join; the old waymark is buried and the other sign shows.
- **Winning and losing**: blocked at the start of a turn = the trail dies. Stones left is the score.
- **Don't** re-read the strategy notes or the free-look paragraph before deal 1. H4 and H5 test whether those skills are found unprompted. If the player has already read them, record that, and treat H4/H5 as retention checks, not discovery.

For a new player, use plan 01's cold-read protocol: hand over the rulebook, give no verbal help, and log every hesitation as a rulebook bug.

## Record sheet

| Deal | Mode | Cleared? | Stones left | Loss cause (stranding / bad run / no-win) | Named turn behind the loss | Dead stacks | Free look used? | Buried card consulted? | Time |
|---:|---|---|---:|---|---|---:|---|---|---|
| 1 | Standard | | | | | | | | |
| 2 | Standard | | | | | | | | |
| 3 | Standard | | | | | | | | |
| 4 | Standard | | | | | | | | |
| 5 | Standard | | | | | | | | |
| 6 | Pathfinder | | | | | | | | |

- Standard clear rate: ___ / 5 (sim band 74–98%)
- Turns with a genuine choice (rough share): ____
- Footprint (approx. cm × cm): ____ Hand held or laid down? ____
- Did the blind starting-waymark choice matter? ____
- Wanted to reshuffle after a loss? ____
- Surprises / quotes:

## Out of scope

- The Long Trail (9 signs, hand 5): later, once the standard trail has a recorded result.
- Scoring or "margin of safety" tiers (`NEW_GAME_CONCEPTS.md` §13 flags them as a rulebook-stage tuning task).
- Further simulation beyond the Pathfinder calibration above.
