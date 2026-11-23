# COVENANT — playtest plan 01 (first solo sitting)

*Before the session. The report goes in `COVENANT_playtest_01.md` beside this plan.*

## Setup

- **Game / version:** COVENANT v0.1, version A (The Loyalty Duel). Rules: [COVENANT_rulebook.md](COVENANT_rulebook.md).
- **Players:** 1 (solo). If anyone is around, one optional observer acts as an assistant *only for the wash* in chapter three (see H5).
- **Deck:** the printed Set D prototype. Sub-decks of 6, 10 and 15 cards (signs 1–4, 1–5, 1–6). Keep the Crown cards apart as the ledger.
- **Scope:** chapter one twice, then chapters two and three, in one sitting of about 45 minutes. Rules as written: strike-back on, opening hand of one card per stranger, free retries.
- **Bring:** paper for the observation log only. The game itself must need no writing.

## Questions this session answers

These come from the game record and the [design analysis](COVENANT_design_analysis.md) (*Caveats for the first table test*). The concept's own fastest falsification asked whether the 6-card opening is a game. The sim says it is a teaching rite with one decision, so the table now has to confirm that framing and check that the game starts in chapter two.

## Hypotheses (falsifiable)

| # | Hypothesis | Holds if… | Fails if… |
|---|---|---|---|
| H1 | **The wash hides the strangers.** Sliding 3–5 identical cards flat for ~10 s loses track of which is which. | Before your first claim you honestly can't say where any particular stranger is. | You can still follow one or more cards after the wash. *This would be a handling bug.* |
| H2 | **Chapter one plays as a 2-minute lesson with one felt decision.** | Both rites take ≤ 3 minutes. At least once you pause over *which card to risk* after a miss, as in the worked example. | It feels like flipping coins with no choice, or the decision never comes up in two rites. |
| H3 | **The game starts biting in chapter two.** Powers and the reserve create choices that chapter one lacked. | In chapters two and three you deliberately spend a power at least twice, and at least once you hesitate between a power and a claim. | You only ever claim, and use powers only when forced. |
| H4 | **Card stewardship is spotted without the strategy notes.** Don't read them until after chapter three. | By chapter three you are choosing claim cards to keep coverage ("risk the redundant card"). | You pick claim cards at random, or the idea only clicks after reading the notes. |
| H5 | **Rising Ash is tension enough.** The sim predicts ~1.2 / ~3.3 / ~4.2 Ash for chapters one to three, with careful play failing rarely (~16% / 8% / 3%). | You care about the Ash count. A miss stings, and the strike-back draws a groan. | Ash feels like a number you ignore because failure never threatens. That would argue for *Strict hearings* as the default. |
| H6 | **The physical procedure is clean.** | The claim card sits beside the stranger, flips are unambiguous, unmasked strangers stay readable in the row, and the sideways Ash and the Spent pile never get confused. | You ever lose track of which stranger is unmasked, or which pile a card belongs in. |
| H7 | **The save works.** | After chapter three, reshuffling into a 15-card sub-deck and re-sorting from the box takes under a minute, and "highest sign in the sub-deck" tells you where you are. | Any confusion about what goes back into the box, or where. |

## What to watch

1. **Handling first:** the wash (H1); accidental lifts or peeks; whether the Spent and Ash piles stay distinct.
2. **Comprehension:** which rules you had to re-read, especially the strike-back, Mask's two-face claim and Key vs Eye.
3. **Pacing:** time each chapter including setup. The predictions are ~2 minutes for chapter one and 5–8 for chapter three.
4. **Power use:** tally each power used per chapter. The sim predicts Leaf and Eye dominate, with Wave, Moon and Flame almost unused. Note any power you never once wanted.
5. **Feel:** where you leaned in (a forced last stranger, a lucky Mask hit) or checked out.

## Record per chapter

Chapter · hearing number · result (clear / grudge / fail) · Ash count · misses · powers used (by sign) · minutes · one sentence on the best and worst moment.

## Teaching plan

Teach yourself from the rulebook alone, reading only *Components* through *How a chapter ends* before chapter one. Read *Powers* before chapter two. Read *Strategy notes* only **after** chapter three (for H4). Note every point where the rulebook left you guessing, since teachability is under test too.

## Decision after the session

Per [playtesting.md](../.kiro/steering/playtesting.md):

- **Iterate → Rough edges** if H1 and H6 hold and at least two of H3–H5 hold. Queue small fixes such as wording, the default difficulty or a dead power.
- **Iterate → In the workshop** if the wash fails (H1). It needs a new concealment step.
- **Iterate → In the workshop** if chapters two and three play as "claim until done" with no felt decisions (H3 and H4 both fail). The fallback engine is already on file: the open-information Turning ([COVENANT_trial_engine.md](COVENANT_trial_engine.md)).

Either way, set `physically_playtested: true` on the game record.
