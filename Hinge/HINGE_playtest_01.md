# HINGE — Playtest 01 (solo, July 2026)

> **Reconstructed report.** No session log was written at the time. This report is reconstructed, in November 2026, solely from the designer's notes in [HINGE_concept.md](HINGE_concept.md) ("Playtest note — original QUEUE mechanic rejected" and "Why it works") and the retired [QUEUE_concept.md](../Queue/QUEUE_concept.md). Anything those notes do not state is marked **not recorded**; nothing has been filled in from memory or inference.

## Setup

| | |
|---|---|
| Date | 25 July 2026 for the QUEUE test (the date of the playtest note and the rename). The split-and-flip test's date is not recorded separately; it is recorded in the same July 2026 notes. |
| Players | Solo (1 player) — both tests. Tester's name not recorded. |
| Deck / subset | 6-sign sub-deck, 15 cards (the concept's stated deck). Which six signs: not recorded. |
| Versions tested | **(a)** Original QUEUE rules: per move, rotate the front card to the back or flip it in place; score when the front three cards match. **(b)** Replacement HINGE mechanic: cut the packet at any point and flip the front block as one unit (reverses order and every face); claim any run of 3+ adjacent matching signs. The written rulebook (v0.1, November 2026) did not exist yet. |
| Physical form | Not recorded — whether the packet was held squared in one hand, fanned, or laid out as a row. (The rulebook flags this as an open designer check.) |
| Number of rounds / moves | Not recorded. |
| Endgame, scoring totals | Not recorded. |

## Hypotheses

| Hypothesis | Result | Evidence in the notes |
|---|---|---|
| QUEUE's one-card moves (rotate / flip front) can build three matching faces often enough to reach an endgame. | **Refuted** | "Basically impossible to line up three matching faces." The failure was structural: rotating only cycles the same 15-card order past a 3-card window; flipping only changes one face. It "never generated enough matches to reach an endgame." |
| QUEUE's stated risk — parity-solvable, not a real game. | **Refuted as framed** (the real failure was different) | The note says this risk "undersold the actual failure — it wasn't solvable *or* unsolvable." |
| A block flip (cut anywhere, flip the block) forms matching runs reliably. | **Confirmed (solo)** | "Matches now form reliably within a handful of moves"; the block flip is "expressive enough to hunt for and construct runs." Exact move counts: not recorded. |
| The move keeps the no-surface, one-hand premise (a single thumb action). | **Confirmed by the designer's description** | "No surface needed, the packet is still held in one hand, and the move is still a single thumb action (a cut-and-flip)." How runs were scanned in a held packet: not recorded. |
| HINGE works as a 2-player game. | **Open** | "Not yet tested with two players." |
| Fun, tension, pacing, teachability. | **Open** | Not recorded. |

## Bugs found

| Severity | Category | Bug | Status |
|---|---|---|---|
| Blocking | Non-termination / flatness | QUEUE's one-card moves touch too little state; the game never produces enough triples to reach an endgame. | Fixed by replacing the mechanic (QUEUE → HINGE, 25 July 2026). |
| Not assessed | Physical handling | Scanning for runs needs every face in view, but a squared packet shows only the front and back faces. The July notes do not say how the test handled this. | Open. Raised later by the rulebook draft, not by the test. |

No other bugs are recorded for the split-and-flip test.

## Rule-change candidates

| Change | Observation it answers | Status |
|---|---|---|
| Replace rotate/flip-front with cut-and-flip-the-block. | QUEUE never built triples (above). | **Adopted** July 2026; game renamed HINGE. |
| 2P turn economy: strict alternation, no bonus move, as the first hypothesis. | None. The solo test does not observe two-player play; this is the concept's recommendation for the first 2P test. | Taken into rulebook v0.1. The November 2026 sim found careful players deadlock under it ([HINGE_rulebook.md](HINGE_rulebook.md) design notes). |

## Verdict

- **QUEUE mechanic: Cut.** Core flaw the concept could not escape. Its folder is kept as a design record ([QUEUE_concept.md](../Queue/QUEUE_concept.md)).
- **HINGE mechanic: Iterate.** It works solo. The two-player game is untested and its turn economy is undecided. State **In development**; `physically_playtested: true` (set by these solo tests; it never reverts).

**Next step:** the designer chooses the two-player turn economy (see the blocking decision in [HINGE_rulebook.md](HINGE_rulebook.md)), then runs the first two-player table test. Record the physical form used (fan, row, or held packet), since this report could not.
