# OUROBOROS — Playtest Plan 02

*Pairs with the forthcoming `OUROBOROS_playtest_02.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the three revival gates in [OUROBOROS_design_analysis.md](OUROBOROS_design_analysis.md) §6.4, the "next recorded test" in [OUROBOROS_playtest_01.md](OUROBOROS_playtest_01.md), and the `COLLECTION_OVERVIEW.md` entry. Numbered 02 to pair with the second session's report.*

## Open before the session

No rule gap blocks a session. Two small v1.1 gaps need a session convention:

- **The first card's pressed face is a buried open symbol.** v1.1 lays every card showing its onward symbol, so both ends stay visible. But the **first** card can show only one face, so until something is played on the tail, the tail's open symbol is the first card's pressed face. It is the same buried-state defect v1.1 set out to remove, limited to one card. **Session convention:** the first card's showing face is the **head** open symbol; its pressed face is the **tail** open symbol. Say the tail sign aloud when you place it. Log every time you have to lift that card.
- **Where scars go.** Base rules: scars go "at the head". The *Elder Serpent* variant says "scars may only be tied at the head", which implies the base game allows tail scars. **Session convention:** head only, as the base text says and as the sim modelled (§4). Note any moment a tail scar would have been better.
- **Par and the stock glimpse.** The face-up stock top is legal information, but the sim tuned par without it. Record whether you used it. Per the rulebook, treat par as a floor if you did.

## Setup

- **Game:** OUROBOROS
- **Version:** v1.1 (revived; open symbols shown face-up; ~36,000 simulated games plus a Monte-Carlo planner probe).
- **Players:** 1 (solo).
- **Session shape:** four serpents, ~10–15 minutes each.
  1. **Short Serpent ×1:** 7 signs / 21 cards / hand 3, to relearn the flow.
  2. **Full game ×3:** 9 signs / 36 cards / hand 4. Play game 1 with only the rule text, then **read the strategy notes** and play games 2–3. The note before games 2–3 is the learnability test.
- **Why this session:** `next_step` is "retest the revived v1.1 rules and record the result". §6.4 makes this table test the gate: if v1.1 fails it, the honest call is to re-cut on v1.1 evidence.

## Hypotheses to test

Sim reference (avg scars, lower is better, [design analysis](OUROBOROS_design_analysis.md) §3 and §6.2):

| | random | greedy (obvious line) | smart (hand stewardship) | planner |
|---|---|---|---|---|
| Full (9 signs, hand 4) | 7.88–7.90 | 6.95–7.00 | 4.74–4.78 | 4.52 |
| Short (7 signs, hand 3) | 4.29 | 3.60–3.65 | 2.60–2.63 | 2.33 |

- **H1 — No lifting.** Gate 6.1. *Prediction:* across all four serpents you never lift a placed card to read an open symbol, apart from the first-card tail case above, and that happens at most once per game. *Falsified if* you lift placed cards routinely, or the onward-face convention is mislaid (cards laid showing the matched face).
- **H2 — Hand stewardship is learnable at the table.** Gate 6.2. *Prediction:* full game 1 (rules only) lands near the obvious line, **~6–8 scars**. Games 2–3, after the strategy notes, average **≤ 5.5 scars**, moving towards the smart band (4.7). *Falsified if* games 2–3 stay at 7+ (the skill exists in the sim but isn't findable at the table), or game 1 is already ≤ 4 (the gap is smaller than the sim suggests, or par is too loose).
- **H3 — Variance reads as tension, not luck-blame.** Gate 6.3; the original cut called the short game "boring and too luck-based". *Prediction:* in each game you can point to at least one scar that **your own** choice caused or avoided, and after game 4 you want another. *Falsified if* every scar feels dealt to you, or "boring" comes back.
- **H4 — The one-scar theorem lands as a delight.** §4 open question. *Prediction:* when you're carrying one scar into the endgame, the "you can't finish on one" rule creates tension rather than reading as a gotcha. *Falsified if* it feels like an arbitrary penalty.
- **H5 — Hand of 4 is comfortable.** §4 open question. *Prediction:* four double-faced cards can be held, fanned low and read on both sides without fumbling. *Falsified if* you lay the hand on the table to read it.

## What to watch

Handling first:

- **Onward-face discipline.** Every placement: the matched symbol goes into the seam, the onward symbol shows. Watch for drift back to the old v1.0 habit, especially at the tail.
- **The first card.** Count lifts of the first card (gap above).
- **Scar orientation.** Scars go sideways at the head. Check the sideways card stays distinguishable from the line in a long serpent, and that scars can be counted at the end without lifting anything.
- **The bite.** Head and tail open symbols should both be visible at the end. Confirm the closing check needs no lift.
- **Table length.** A 36-card serpent is long. Note whether it has to bend, and whether bending makes the line hard to read.

Then:

- **Saying it aloud.** "…and Flame flows to Wave." Does it carry the theme, or get dropped by game 2?
- **Tail use.** The strategy notes say "the tail is half your game". Count tail plays per game.
- **Time.** Rulebook says 10–15 minutes.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | No lifts beyond ≤ 1 first-card check per game | Routine lifting; matched face laid up |
| H2 | Games 2–3 average ≤ 5.5 scars | Games 2–3 still 7+ |
| H3 | Own-choice scars named; want to replay | "Luck" / "boring" again |
| H4 | One-scar endgame is tense | Reads as a gotcha |
| H5 | Hand held and read comfortably | Hand put down to read it |

Verdict framing (§6.4): if H1–H3 hold, OUROBOROS has passed its revival gate. If H2 or H3 fail clearly, record the evidence for a re-cut decision; that decision is the designer's.

## Teaching plan (retest — what to re-read)

- Re-read **How the serpent grows** and its **handling note (v1.1)**. The onward-face convention is the one change from the version you played, and the easiest to forget.
- Re-read **Scars** and **The bite**.
- Read the **strategy notes only after full game 1** (H2).

## Record sheet

| | Short | Full 1 (rules only) | Full 2 (after notes) | Full 3 |
|---|---|---|---|---|
| Scars in play | | | | |
| Closing scar? (Y/N) | | | | |
| Total scars / tier | | | | |
| Lifts of placed cards (excluding first card) | | | | |
| Lifts of the first card | | | | |
| Tail plays | | | | |
| Stock glimpse used? (Y/N) | | | | |
| Scars you'd blame on your choice / on the shuffle | | | | |
| Time | | | | |

- Hand of 4 comfortable? ____
- One-scar moment: tension or gotcha? ____
- Want another game after game 4? ____
- Surprises / quotes:

## Out of scope

- Hatchling, Elder Serpent and Two-Player variants.
- **Voluntary scars.** Flagged as untested in §4. Don't introduce them this session.
- Re-tuning par. Only if games 2–3 routinely beat Gold (§4: "tighten the ladder, not the rules").
