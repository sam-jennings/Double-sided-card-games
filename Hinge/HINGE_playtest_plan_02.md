# HINGE — Playtest Plan 02

*Pairs with the forthcoming `HINGE_playtest_02.md`. Written per [playtesting.md](../.kiro/steering/playtesting.md). Numbered 02 because 01 is the solo report [HINGE_playtest_01.md](HINGE_playtest_01.md). Hypotheses come from the Design notes in [HINGE_rulebook.md](HINGE_rulebook.md), the `next_step` on [HINGE_concept.md](HINGE_concept.md), and playtest 01's open rows ("HINGE works as a 2-player game", "Fun, tension, pacing, teachability", and the unrecorded physical form).*

## Open before the session

- **The 2P turn economy is undecided.** The game record's `next_step` asks the designer to choose it. The rulebook draft uses **strict alternation, no bonus move** and lists one alternative already written: the designer's variant **Claim and go again** (after a claim, fold again). This session uses only those two. The sim found that careful players deadlock under strict alternation and that Claim and go again "barely changes anything". The session's job is to find out whether **humans** actually stall, not to fix the stall.
- **No other turn-order rule is written.** The Design notes list three *directions* (reward setting up, force contact, go solo or co-op) but give no wording or numbers. Don't play them as rules. If the table wants to try something in those directions, record it as the table's own house rule, word for word (see "House rules" below).
- **The physical form is set by the draft, not by the solo test.** The rulebook uses a readable row. Playtest 01 couldn't record whether the July solo test used a row, a fan or a held packet. Record what this table does.

## Setup

- **Game:** HINGE
- **Version:** rulebook draft v0.1 (November 2026), as written. Dry cap 8.
- **Players:** 2. This is the first two-player table.
- **Symbol subset:** signs 1–6 (Moon to Mask). Remove every card showing Key, Star or Crown, leaving 15 cards with each sign on 5.
- **Session shape:**
  1. **Match 1 (required):** three rounds, strict alternation, exactly as written. Alternate the first player. Don't read the strategy notes before round 1. Read them aloud between rounds 1 and 2 (see H3).
  2. **Match 2 (optional, if time allows and match 1 stalled):** three rounds of **Claim and go again**, the rulebook's written variant. Everything else is unchanged.
  3. **House-rule round (optional):** if the players propose their own fix, play one round with it and record it. Don't write it into the rulebook.
- **Why this session:** the sim's Skilled v Skilled deadlock comes from a two-ply bot. A one-ply bot is a floor, not a ceiling (design-principles lesson 6b), and the reverse is also true: two humans may not play like either bot. One table session shows whether the deadlock is real before the designer chooses a fix.

## Sim reference (from the Design notes, dry cap 8, strict alternation)

| Table | Folds | Cards claimed (of 15) | Ended by dry cap | Draws | First player wins (decided) |
|---|---:|---:|---:|---:|---:|
| Greedy v Greedy (1-ply) | 14.2 | 7.3 | 92% | 28% | 63% |
| Skilled v Skilled (2-ply) | 8.5 | 1.6 | 100% | 66% | 100% |
| Random v Random | 9.7 | 1.4 | 100% | 70% | 60% |

In Skilled v Skilled play, every claim came on fold 1, 2 or 3. None came later.

## Hypotheses to test

- **H1 — Humans stall like the skilled bot.** The sim's headline. *Prediction (the sim's):* by round 3 of match 1, a round claims **≤ 3 cards**, every claim lands on folds 1–3, and the round ends on the dry cap. *Falsified if* rounds average **≥ 6 cards claimed** (Greedy-like or better) and at least one claim lands after fold 3 in rounds 2–3. That would make the deadlock a bot artefact at this skill level.
- **H2 — Stalling grows as players learn.** The flatness bug: "the better both players get, the less happens". *Prediction:* cards claimed per round falls from round 1 to round 3, and the fall is sharpest after the strategy notes are read. *Falsified if* claims hold steady or rise across rounds.
- **H3 — Denial is found, not taught.** *Prediction:* in round 1 (notes not read) neither player says aloud that they are refusing to leave a setup. After the notes ("Don't build for your opponent") at least one player does so by round 2. *Falsified (worse) if* denial is voiced in round 1 unprompted. Then the stall is the obvious play, not an expert one.
- **H4 — First-player advantage shows.** *Prediction:* in decided rounds the first player wins more often than not. The sim range is 63% (greedy) to 100% (skilled). *Falsified if* the second player wins most decided rounds. Three to six rounds can't settle this; record it so it adds up across sessions.
- **H5 — The dry cap ends rounds cleanly.** *Prediction:* the dry count is kept aloud with no dispute about whether a fold claimed, and every round lasts **5–10 minutes**. *Falsified if* the count is lost or argued over, or a round runs past 12 minutes.
- **H6 — Claim and go again doesn't fix it (match 2 only).** The sim says it barely changes anything (Skilled v Skilled: 1.6 cards, 61% draws). *Prediction:* match 2's cards claimed per round are within about 2 of match 1's. *Falsified if* match 2 claims clearly more and the players say it feels different.

## What to watch

Handling first:

- **The row.** Can both players read every face from their seats? Note whether anyone reads the row upside down, and whether the row keeps its order when the block is squared, turned and re-spread.
- **Folding.** Does a long block (8+ cards) turn over cleanly as one stack? Count every fold where cards slip, the order is lost, or a card turns over on its own. Each of these is a handling bug: the move must be exact.
- **Checking hidden faces.** The rulebook allows anyone to lift a card to check its other face, then put it back exactly. Count lifts per fold. Note any card that went back on the wrong face, and whether the table noticed. Is reading the hidden faces a chosen skill, or a chore before every fold?
- **Closing gaps and cascades.** After a claim, is closing the gap and checking for a new run clean? Does anyone miss a run or claim a wrong one?
- **Physical form.** Note any move to a held packet or fan, and why.

Then:

- **Thinking time.** Seconds per fold. Long silent turns with no claim are what a stall looks like.
- **Feel at the dry count.** Does "five dry… six dry…" build tension, or read as the game giving up?
- **Moments.** Any fold that produced a reaction: a big cascade, a steal off the opponent's setup, a clever reversal.

## Observable success / failure signals

| | Holds (sim confirmed) | Fails (sim refuted) |
|---|---|---|
| H1 | ≤ 3 cards a round by round 3; claims only on folds 1–3; dry-cap ends | ≥ 6 cards a round; late claims in rounds 2–3 |
| H2 | Claims fall across rounds, most after the notes | Claims steady or rising |
| H3 | Denial voiced only after the notes | Denial voiced in round 1 unprompted |
| H4 | First player wins most decided rounds | Second player wins most |
| H5 | No dry-count disputes; 5–10 min a round | Count lost or argued; > 12 min |
| H6 | Match 2 within ~2 cards of match 1 | Match 2 clearly livelier |
| Handling | Folds exact; lifted cards always returned correctly | Order lost, or a card returned on the wrong face |

**Verdict framing:** if H1 holds, the sim's deadlock is real at the table, and the designer's turn-economy decision is confirmed as blocking. If H1 fails, the duel works at this skill level and the decision can wait for stronger players. H6 tells the designer whether the only other written option is worth keeping. Handling failures are their own result: a fold that can't be done exactly blocks the game whatever the turn order.

## Teaching plan

- Lay out the row, then teach the one move with the rulebook's example: the two-card block turns over, reverses and shows its other faces, making Eye · Leaf · Leaf · Leaf. Do it on the real cards.
- Then claiming, cascades, passing (no bonus move), and the two round ends (fewer than 3 cards, 8 dry folds counted aloud).
- State that everything is public and anyone may lift a card, as long as it goes back exactly.
- **Don't read the strategy notes before round 1.** Read them aloud between rounds 1 and 2, and note that you did (H2, H3).
- **Watch during teaching:** does "the block reverses *and* flips" land from one demonstration? Time from the end of the teach to the first fold.

## House rules

If the table proposes its own fix, play it for one round. Then record:

- the rule, in the players' exact words;
- which problem it was meant to fix;
- cards claimed, folds, and how the round ended;
- whether the players would keep it.

Don't write it into the rulebook. It is evidence for the designer.

## Record sheet

| | R1 | R2 | R3 | (M2) R1 | (M2) R2 | (M2) R3 | House rule |
|---|---|---|---|---|---|---|---|
| Turn order | alt | alt | alt | go again | go again | go again | |
| First player / winner | | | | | | | |
| Pockets (P1–P2) | | | | | | | |
| Folds | | | | | | | |
| Fold numbers that claimed | | | | | | | |
| Ended by (< 3 cards / dry cap) | | | | | | | |
| Denial voiced (Y/N, who) | | | | | | | |
| Dry-count disputes | | | | | | | |
| Fold slips / order lost | | | | | | | |
| Lifts per fold (rough) / wrong-face returns | | | | | | | |
| Time | | | | | | | |

- Strategy notes read before round 2? (Y/N) ____
- Physical form used (row / fan / held packet), and any change: ____
- Did either player say "nothing's happening" or similar? When? ____
- Surprises / quotes:

## Questions for the designer (not answered by this session)

- The Design notes' three directions (reward setting up, force contact, solo or co-op) have no wording or numbers. Which, if any, should be written up and simulated for the next table?
- Design-note check 1: was the July solo test played as a row, a fan or a held packet?

## After the session

Write `HINGE_playtest_02.md`: setup, each hypothesis (confirmed / refuted / open), bugs ranked by severity with handling bugs first, rule-change candidates each tied to an observation, and a verdict (iterate / park / cut). `physically_playtested` is already true. Choose the `state` per the playtesting table, update `next_step` and the known issue in all three catalogue views, and re-run `hinge_sim.py` if any change is adopted.

## Out of scope

- Choosing or writing a new turn economy.
- Changing the dry cap. The rulebook calls 8 a simulation-set default.
- Solo HINGE. Already confirmed solo in playtest 01.
- Re-simulation before the session.
