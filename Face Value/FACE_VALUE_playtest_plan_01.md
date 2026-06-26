# FACE VALUE — Playtest Plan 01

*Pairs with the forthcoming `FACE_VALUE_playtest_01.md`. Written per `.kiro/steering/playtesting.md`.*

## Setup

- **Game:** FACE VALUE
- **Version:** v1.0 (pacing sim-checked, 4k games/matchup; never tabled).
- **Players:** 2 (the only count — heads-up duel).
- **Symbol subset:** all 9 signs / 36 cards. Deal 15 each, 6 face-up as the morgue.
- **Why this session:** FACE VALUE fills the 2P bluffing slot (rung 3, testable at 2P per `focus-priority.md`). Pacing and termination are sim-settled; what no simulation can answer is whether the *bluffing* is fun — whether folds, cold reads, and acting-last actually carry the tension the design claims.

## Hypotheses to test

Recorded first-table questions (rulebook footnote), framed as falsifiable predictions:

- **H1 — Fold-to-stay-hidden gets used.** A fold costs a card but reveals nothing; a cheap showdown loss leaks a pair forever. *Prediction:* players fold at least occasionally to protect information, rather than calling everything to showdown. *(If the table calls everything, the deduction layer finishes too fast and the fold mechanic is dead — a core design risk.)*
- **H2 — Cold Read is timed roughly right.** *Prediction:* cold reads are rare early (a 1-in-8 gamble) and attempted decisively late, once the morgue + two tallies + own hand have narrowed a shown face to one or two live partners. Watch for the opposite failure: cold reads thrown early as wild gambles, or never attempted at all because players don't do the count.
- **H3 — Acting last reads as the advantage the maths says.** The duel loser acts last next duel (acting with more information). *Prediction:* players come to *prefer* or at least respect the last-actor seat, rather than experiencing losing as pure punishment.
- **H4 — The shown face is read as a claim.** *Prediction:* players actively interpret a shown low pip as "hiding strength" and bluff against it — the intended mind-game emerges rather than players ignoring the shown face.

## What to watch

- **Does the lie-space counting actually happen?** The deck's signature is bluffing-against-arithmetic. Watch whether players use the morgue and open tallies to eliminate partners, or just play on gut. If the arithmetic never gets used, the deck-necessity (D-rubric #1) is at risk — flag it.
- **Escape-card signalling.** A fold surrenders one chosen escape card, face of your choice — "feed the tally a lie." Watch whether players exploit this as a deliberate disinformation tool or just dump a random card.
- **Stake-row handling.** Cards staked face-of-your-choice in two parallel rows — watch for physical clarity (whose row is whose, level vs unequal stakes) and whether "raise without intent to call" causes confusion.
- **Tie impossibility.** Pair-uniqueness guarantees a winner (hidden pip, then visible pip). Confirm no one ever hits an ambiguous showdown.
- **Pacing.** Sim says ~12 duels ≈ 15–20 min. Time it; note if it overstays.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | At least one fold made to protect a card | Every duel goes to showdown; folding never chosen |
| H2 | Cold reads cluster late, off a real count | Early wild reads, or none ever attempted |
| H3 | Losing seat played as positional advantage | Acting last feels like nothing; losing is pure loss |
| H4 | Shown face actively read/bluffed against | Shown face ignored; play is value-only |
| Deck-necessity | Players eliminate partners via morgue/tallies | No counting; an ordinary deck would play the same |

## Teaching plan

- Teach the **one-sentence hook first**: the face you *show* is your only claim; the face you *hide* is your strength.
- Walk one full duel slowly (commit → bet → showdown) before introducing fold, cold read, and the escape card.
- **Consider opening with the Quick Draw variant** (21-card / symbols 1–7 subset, deal 9, morgue of 3, ~10 min) as the teaching duel — the count tightens twice as fast, so the deduction layer reveals itself within a single short game. Then play the full 36-card game once the engine is understood.
- **Watch during teaching:** whether "showing low = claiming strength" lands as a concept, or has to be demonstrated by a bluff going wrong (direct H4 signal).

## Out of scope

- The Tell / High Stakes / Best of Three variants unless a clean base game finishes with time to spare (the Tell bridges to FORKED TONGUE and is worth a later look).
- Re-tuning the cold-read fee (2 cards), escape fee (1 card), or raise sizing — `FACE_VALUE_design_analysis.md` names these as the table-test dials; collect observations this session, tune later.
