# BRAVADO — Playtest Plan 01

*Pairs with the forthcoming `BRAVADO_playtest_01.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the ranked table questions in [BRAVADO_design_analysis.md](BRAVADO_design_analysis.md) §7 and the first-table questions in `COLLECTION_OVERVIEW.md`.*

## Open before the session

**One rule gap needs a ruling before play: what happens when everyone busts?** The rules say the longest banked streak wins, a bust counts as zero, and ties go to whoever *banked* first. A bust is not a bank, so a round where every player busts has no winner. This is not a corner case at three players. Under the sim's sensible bots (pip calls, chase the leader), **25.1% of 3P rounds end with everyone bust** (15.5% at 4P, 9.3% at 5P; 40,000 rounds each, measured for this plan). `bravado_sim.py` silently gives those rounds to seat 1 (`max(..., key=(banked, -i))`). That means part of the analysis's 3P seat-1 edge (44.39% against a fair 33.33%, §3b) probably comes from the missing rule, not from play.

- **Session ruling (proposed; agree before the first run):** if every player busts, **nobody wins the round**. Pass the starting player on and play another round. Record each all-bust round on the sheet. The rulebook stays unchanged until the report.

Two smaller things:

- **Draw wording.** Setup says the Caller "is welcome to see what they are drawing", but step 1 says they draw "blind". Use the setup reading: only the active player must not see.
- **3P instead of 4–5P.** `next_step` asks for 4–5 players. This plan runs 3 because 3 is what can be fielded. At 3P the Caller just alternates between the two opponents, the *Crowd* variant has only one pointer, and the sim's seat spread is widest (19.7pp). The 4–5P question carries forward.

## Setup

- **Game:** BRAVADO
- **Version:** v0.1 (odds table and supply bounds exactly enumerated; floor sim 40,000 rounds per configuration; never tabled).
- **Players:** 3.
- **Symbol subset:** all 9 signs / 36 cards. No subset.
- **Components:** the deck, an opaque draw well (box base or a deep mug), about 6 counters for round wins.
- **Session shape:**
  1. **Geometry check** (2 minutes; the rulebook's handling box). Hold one card up and confirm the active seat can't read the far face and both other seats can.
  2. **First game:** to **two** round wins, cap **five**, free table talk once the Caller has spoken.
  3. **Base game:** to **three** round wins, cap **six**, advice from the Caller only. Rotate the starting player every round.
  4. **Accomplice (conditional):** if H2 fails during the base game, switch to *Accomplice* for the rest of that game or for one more short game, and compare.
- **Why this session:** `next_step` is "watch whether the Caller's one word carries any read at all, and whether the room leans in when a strong streak is risked". §7 calls question 1 the one that decides the design.

## Hypotheses to test

§7's ranked questions, as falsifiable predictions:

- **H1 — The room leans in on a risked streak (the gate).** *Prediction:* in every round where someone pushes from 4 or more, the whole table watches the reveal and reacts out loud (groans, cheers, "I told you"). *Falsified if* a push from 4+ draws no reaction from the non-active players. Per §7 that is a **cut** signal, because no rule change repairs it.
- **H2 — The Caller's word carries a read.** The sim models the advice as noise. At equilibrium it is worth **1.01–1.03×** over playing the pip, and blindly following or contradicting the Caller collapses to **0.35×** fair share (§3c, §4). *Prediction:* players visibly try to read the Caller (pause, stare, comment on them), and at least once a player goes against the pip's favourite side because of the Caller. *Falsified if* by the base game everyone just plays the pip and ignores the word. **Then switch to Accomplice.**
- **H3 — Three is a trap, and the table feels it.** Sim (4P): banking at 3 wins **15.65%** of rounds, the worst of any stopping point (bank at 1: 21.21%; push to 5: **32.58%**). *Prediction:* someone banks a 3 in the first game and loses to a later seat. By the base game at least one player says out loud that 3 isn't safe, or pushes past it. *Falsified if* banking at 3 stays the habit with no discussion, or "the first bank wins ties" reads as arbitrary.
- **H4 — The held card holds up physically.** *Prediction:* zero glimpses of the far face by the active player across the session, and the third seat can read the Caller's face every time. *Falsified if* any glimpse (even a suspected one) or a seat that can't see.
- **H5 — Rotation at 3P adds variety.** At 3P the Caller alternates between two people. *Prediction:* players notice and use the switch ("now it's Lauren, she lies"). *Falsified if* it feels like a ping-pong duel, or nobody tracks who is calling.
- **H6 — Seat effects stay small over a match.** Sim 3P seat spread **19.7pp** (seat 1 at 44.39%; partly the all-bust artefact above). Two games can only flag a gross effect. *Prediction:* round wins don't pile up on the starting seat. Record the starting seat of every round winner.

**Expected numbers (sim, 3P pip + chase):** about **2 busts per round**, at most **15 cards** drawn per round, the well never empties. With the all-bust ruling, expect about 1 round in 4 to be replayed.

## What to watch

Handling first:

- **Presentation angle.** Is the card squared and vertical every time? Does a lamp or window show through it? The rulebook requires the card angled away from light.
- **Well leakage.** Does the active player see the card as it comes up the well wall? Is the well tilted away?
- **Announce discipline.** The active player must say sign *and* number. Note mis-announcements and whether they're corrected before the Caller speaks.
- **Record row.** Resolved cards overlap in a public row. Check they stay readable and are returned as found when picked up.

Then:

- **Pacing.** Time each round. Note any dead time while one player runs and the others wait.
- **Table talk.** In the first game (free talk), do the other players help, mislead, or stay quiet? Does that make the base-game restriction feel needed?
- **Rank comprehension.** Do players use the pip as the odds ("only Moon is below Leaf")? The game is meant to teach rank (§6).

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Table reacts to every 4+ push | Silence on a 4+ push (**gate: cut**) |
| H2 | Players try to read the Caller; ≥ 1 call goes against the pip because of them | Everyone plays the pip (**switch to Accomplice**) |
| H3 | A banked 3 loses; players start to push past it | 3 stays the default stop |
| H4 | No glimpses; third seat always sees | Any glimpse or blocked seat |
| H5 | The Caller switch is used | Feels like a fixed duel |
| H6 | Wins spread across starting seats | Starting seat wins most rounds |
| Rules | All-bust ruling applied without fuss | Arguments about all-bust rounds |

Verdict framing (§7): iterate → **Proven** if the room lights up and only polish remains; iterate → **Rough edges** if Accomplice is needed but the game plainly works; iterate → **In the workshop** if higher/lower is too thin for 15–25 minutes; cut → **Shelved** if H1 fails.

## Teaching plan

- Say the **rank canon** aloud, word for word.
- Teach one breath: "The Caller holds up a card. You see one side, we see the other. You say what you see; the Caller tells you higher or lower, true or not; you call it."
- Run one **demonstration card** with the odds table: show a Leaf, say "seven of eight are higher", flip it.
- Teach bank or push, and the **tie rule** ("you must beat the leader; matching loses"). Teach the all-bust ruling here.
- **Don't** teach that three is a trap or that the advice is mathematically weak. H2 and H3 test whether players find those things.
- **Watch during teaching:** whether "the announcement tells the Caller the card" lands first time. If it needs a second explanation, record it.

## Record sheet

Per round:

| Round | Game (First / Base / Accomplice) | Start seat | P1 streak (B = bust) | P2 streak | P3 streak | Winner (or all-bust) | Push from 4+ drew a reaction? (Y/N) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |

Per card (tally; fill in what you can):

| | Followed the Caller | Contradicted the Caller |
|---|---|---|
| Call agreed with the pip's favourite side | | |
| Call went against the pip's favourite side | | |
| …and was correct | | |

- Banked-at-3 outcomes (won / lost to a later seat): ____
- Glimpses of the far face (who, when): ____
- Accomplice switched on? When, and did advice-reading change? ____
- Teach time: ____ Play time per game: ____ / ____ (target 15–25 min)
- Surprises / quotes:

## Out of scope

- 4–6 player counts (the `next_step` target): next session.
- *Stone Faces*, *The Crowd*, *Personal Challenge*. At 3P, The Crowd has one pointer and Personal Challenge is the same as rotation, so neither tests anything here.
- Re-simulation, including fixing the all-bust handling in `bravado_sim.py`: a designer decision once a rule exists.
