# ICARUS — Playtest Plan 01

*Pairs with the forthcoming `ICARUS_playtest_01.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from [ICARUS_design_analysis.md](ICARUS_design_analysis.md) §7 and the first-table questions in `COLLECTION_OVERVIEW.md`.*

## Open before the session

No rule gap blocks a first session. One non-blocking gap:

- **Tiebreak 2 is untrackable as written.** "Fewest of your cards in the Fallen field" assumes you can tell whose cards are whose, but the Fallen field is one shared spread, and the rules don't say whether toll cards count. **Workaround for this session:** tally each player's fallen cards (fallen rows and tolls separately) on the record sheet. Don't change the rulebook until a tie actually happens.

## Setup

- **Game:** ICARUS
- **Version:** v0.1 (floor certified over ~50,000 simulated games; never tabled).
- **Players:** 2. The analysis suggested a 3P first table; this plan runs 2P because it is easier to field. The 4P downtime question is deferred.
- **Symbol subset:** all 9 signs / 36 cards. Towers of **18 cards each**.
- **Session shape:** one **Fledgling** teaching game (no toll, exactly 4 flights each), then **two base games** with seats swapped. Kestrel only if both base games run cleanly and time is left.
- **Why this session:** `next_step` is "run the first table test; watch counting load and downtime." The sim certified termination, the toll and a ~1.6× skill gap at 2P. What it cannot say is whether counting feels good to do.

## Hypotheses to test

The analysis's caveats for the first table, framed as falsifiable predictions, with sim numbers for 2P where they exist:

- **H1 — Counting is delicious, not homework.** *Prediction:* by base game 2, at least one player consults the Fallen field or banked clutches before a risky rise, without being prompted, and says they enjoy it. *Falsified if* nobody counts, or counting happens only grudgingly and slows turns. Sim: counting vs naive odds is only **1.06–1.08×** at myopic depth, so the design's bet is that human counting is worth more than bots show.
- **H2 — The k=3 "reach for the soar" moment is tense.** *Prediction:* flight lengths come out bimodal like the sim's (land at 2 cards ~30% of flights, reach 4+ ~40%), and the decision at 3 safe cards draws visible hesitation or table reaction. *Falsified if* flights cluster at 3 or players always (or never) push from 3.
- **H3 — Waiting players stay engaged.** *Prediction:* the non-active player watches flips and reads the Fallen field during the other player's flight. *Falsified if* the waiting player checks out. At 2P downtime is short, so a failure here is a strong warning for 3–4P.
- **H4 — The toll feels fair.** *Prediction:* after one explanation, players accept burning a card on landing as the price of banking, and use it tactically at least once (for example, flying on rather than burning a Crown top). *Falsified if* it reads as an arbitrary penalty that needs reframing.
- **H5 — Table space works.** *Prediction:* 18-card towers, banked clutches, sideways soars and the Fallen field fit at 2P without clutches merging or soars being misread. *Falsified if* players lose track of which clutch is sideways or whose cards are whose.
- **H6 — No meaningful seat edge.** Sim at 2P: **89.8 vs 91.0** (second seat slightly ahead). *Prediction:* across the two base games with swapped seats, no consistent seat edge. Two games can only flag a gross edge, not confirm fairness.

**Expected numbers (sim, 2P counting mirror):** ~90 points per player, fall rate ~27–30%, mean flight ~3 cards. My estimate from those figures (not a sim output): an 18-card tower lasts roughly 4–6 flights per player. Real time: 10–15 minutes.

## What to watch

Handling first:

- **The rise flip.** The tower top is public; the player flips it to reveal the pressed face. Watch that the card is laid in the row **showing the revealed face** every time. The old top face is now underneath, and laying it the wrong way changes the poison set and the score.
- **Poison reading.** Poison is the face-up signs in *your own* row only. Watch for players wrongly treating pressed faces, an opponent's row or banked clutches as poison (all covered in the FAQ — note if it's needed).
- **Examine-and-return.** The Fallen field and clutches may be handled at any time. Watch for cards returned the wrong way up in banked clutches, where the face is the score.
- **Toll execution.** The toll card goes to the Fallen field "as it lies". Watch that it's moved without being flipped, and that the tower-empty and last-card cases (no toll; skip next turn) are handled correctly.
- **Auto-land.** A tower that runs out mid-flight lands with no toll. Check that a 4+ auto-landed flight is still banked sideways as a soar. The rules imply it but don't say so explicitly; note it if it comes up.

Then:

- **Counting aloud vs silently.** Does anyone narrate odds? Does that help or slow the table?
- **Pacing.** Time each game; note any flight where the active player stalls over the count.
- **Fledgling vs base.** Does the toll change behaviour (fewer 1–2 card graze landings) compared with the Fledgling game?

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Unprompted counting before a risky rise; enjoyment | No counting, or counting as visible chore |
| H2 | Landings split between 2 and 4+; hesitation at 3 | Flights mushy at 3; the decision at 3 is automatic |
| H3 | Waiting player reads the field / reacts to flips | Waiting player disengages |
| H4 | Toll accepted and used tactically | Toll resented or forgotten |
| H5 | Clutches, soars and field stay legible | Merged clutches, misread soars |
| H6 | No seat wins both games by a wide margin | Same seat wins both clearly (flag; needs more games) |
| Handling | Rows always show the revealed face | Cards laid with the old top face showing |

## Teaching plan

- Say the **rank canon** aloud first, verbatim from the rulebook.
- Teach the one-breath core: "flip your top card — if the new face matches your row, you fall."
- Play the **Fledgling** game first (no toll, 4 flights each). Introduce the toll and the soar only for base game 1. Ask after Fledgling whether the toll "makes sense" once explained — that's a direct H4 signal.
- Don't teach counting. Mention once that "every card that leaves a tower is public and examinable", then see whether players find counting themselves (H1). Read the Counting the sky paragraph aloud only after base game 1.
- **Watch during teaching:** whether "only your own row's face-up signs are poison" needs repeating.

## Record sheet

Per game:

| | Game: Fledgling / Base 1 / Base 2 | Player 1 | Player 2 |
|---|---|---|---|
| Seat (first / second) | | | |
| Flights flown | | | |
| Falls | | | |
| Soars banked | | | |
| Cards lost in falls / cards burned as toll | | | |
| Final score | | | |

Flight log (one tick per flight, by player):

| Flight length at landing or fall | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|---|
| P1 landed | | | | | | |
| P1 fell | | | | | | |
| P2 landed | | | | | | |
| P2 fell | | | | | | |

- Teach time: ____ Play time per game: ____ / ____ / ____ (target 10–15 min)
- Unprompted counting moments (who, when): ____
- Hesitations at 3 safe cards: ____
- Handling slips (wrong face laid, toll flipped, card returned wrong way): ____
- Surprises / quotes:

## Out of scope

- **3P and 4P downtime** — not testable at 2P; carry forward to a later session.
- **Kestrel (memory)** — only if time is left after two clean base games. It is the collection's flagged memory-game target and deserves its own session.
- **Vulture** — untested, meaner variant; later.
- Re-simulation — the floor is certified; the table is the priority.
