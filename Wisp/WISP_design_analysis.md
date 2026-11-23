# WISP — design analysis (vetting + floor sim, November 2026)

*State: **In the workshop** · physically unplayed. Rules: [WISP_rulebook.md](WISP_rulebook.md) v0.1a. Sim: [wisp_sim.py](wisp_sim.py). Verdict: **not promoted.** The handling is sound after one fix, but the starting dials don't make a chase, and every balanced setting trades one recorded value against another. Choosing between them is a designer decision.*

## 1. Physical-handling read-through

| Question | Answer | Problem? |
|---|---|---|
| What can each player see? | The atlas (24 cards, both faces), the trail's shown faces, sprint packets' top faces, the Wisp's hand count | — |
| What can each player inspect? | Hunters: any atlas card, both faces. Wisp: own hand; may tip its own top trail card | — |
| What is hidden, and is it? | The Wisp's current place (one pressed face) and sprint intermediates | **Yes, a leak (fixed in v0.1a).** v0.1 called the held fan "genuinely private", but a fan shows its outer faces to the table (DECK_PLAYTEST_FINDINGS F8). The hunters already know the whole hand by complement, so seeing the outer face of the card leaving the fan names the card, and the trail's shown face then names the current place. **Fix:** hold the hand to the chest and choose each road below the table edge, the C2 Blind Cut technique. No new mechanic. |
| Is required state visible? | The trail is a self-recording overlapped row; sprint packets are squared on purpose | Table risk only: the excavation may slip with an 8–9-card overlapped row and squared packets (already the recorded playtest question) |
| Can the table verify legality without memory? | Yes. The reverse excavation checks every link and every Raid answer | — |

No rules ambiguity found. First-move Raids are allowed, sprints are announced, a sprint from 7 cards escapes at 9, and being cornered is checked at the start of the Wisp's turn. The sim models all of these as written.

## 2. Simulation

**Questions:** does it end; who wins with careful play on both sides; does skill matter on each side; which dials make a chase.

**Method:** v0.1a rules exactly. Hunters reason *exactly*: they track every history consistent with the table (each shown face confirms the previous place, a sprint hides one intermediate, a missed Raid rules out that place for that turn) and drop histories in which a careful Wisp would be cornered.
- **SkilledWisp:** never moves into a position with no full escape route (exact lookahead over its hand). Among safe moves it picks the one whose true place is least likely in the hunters' candidate set, and sprints when a step would leave it at ≥ 50%.
- **SkilledHunter:** raids the most likely place at ≥ 50%, or whenever its remaining Raids outnumber the turns left.
- **RandomWisp / RandomHunter:** uniform legal moves; raids half the time at a random place.

2,000 games per row, seed 1 (`python wisp_sim.py --games 2000`). The pilot sweep covered 54 dial combinations at 200 games each (`--sweep`). Every game ends by rule within 12 cards, so there is no turn cap and no stall is possible.

| Dials (hand / raids / escape / sprints) | Skilled Wisp v Skilled hunters: escapes | Skilled Wisp v random hunters | Random Wisp v skilled hunters | Random v random | Mean trail when caught (S v S) |
|---|---:|---:|---:|---:|---:|
| **12 / 4 / 8 / 2 (v0.1)** | **0.2%** | 70.5% | 0.1% | 31.1% | 4.6 |
| 12 / 1 / 8 / 2 | 46.8% | 88.1% | 13.1% | 41.0% | 3.8 |
| 12 / 1 / 7 / 3 | 51.2% | 89.6% | 17.3% | 53.1% | 3.9 |
| 14 / 1 / 8 / 3 | 51.1% | 90.8% | 21.3% | 61.6% | 5.8 |
| 14 / 2 / 7 / 3 | 43.3% | 81.8% | 8.2% | 61.2% | 5.9 |
| 16 / 2 / 8 / 3 | 49.7% | 80.6% | 12.8% | 65.2% | 7.1 |
| 16 / 3 / 7 / 3 | 50.4% | 77.6% | 10.6% | 65.4% | 6.0 |
| 16 / 3 / 8 / 3 | 41.9% | 74.7% | 6.7% | 60.8% | 7.0 |

The skilled Wisp is never cornered (0.0% in every row), and random Wisps are cornered 7–49% of the time.

## 3. Reading

- **The v0.1 dials are a near-certain catch.** Twelve roads spread over nine places leave ~2–3 candidate places after each move, and every miss deletes one. Four Raids are plenty. Even 3 Raids (2.5–3% at an 8-card escape) or 3 Raids with a 7-card escape (6–19%) doesn't fix it (pilot sweep).
- **Skill matters on both sides.** The Wisp's careful line lifts escapes from ~7–21% (random Wisp) to ~42–51% against skilled hunters. The hunters' careful line cuts escapes from ~75–91% (random hunters) to ~42–51%. That's a healthy two-sided gap at every balanced setting.
- **The balance lever is hand size or Raid count, and each costs something recorded:**
  - **Keep the 12-card hand, cut to 1 Raid** (12/1/8/2 or 12/1/7/3, ~47–51%). Comfortable hand, but the hunters' whole game is one shot, usually fired early: the mean catch comes at trail 3.8, so most catches end the chase after three or four cards. That risks *flatness* (no arc).
  - **Grow the hand to 14–16 and keep 2–3 Raids** (14/2/7/3, 16/2/8/3, 16/3/7/3, ~43–50%). A real chase: catches come late (trail 6–7), with several raids to spend. But the house guidance (DECK_CONVENTIONS C8) calls 14 cards overwhelming and 12 heavy, and the Wisp must hold the hand privately, because an open spread would show which road was taken.
  - **Middle:** 14/1/8/3 (51%, catches at 5.8) keeps one Raid but makes it land later.
- **Sprints:** three sprints instead of two usually help the Wisp (in 21 of the 27 pilot pairs, often by 10–25 points; e.g. 14/2/8 rises from 17.5% to 30%; at a 12-card hand it's mixed). It's a cheap lever that touches no handling, but not a reliable fix on its own.

## 4. Decision for the designer (blocking; no dials changed in the rulebook)

Choose the trade: **(a)** 12-card hand with one Raid (comfortable hand, short chase), **(b)** 14–16-card hand with 2–3 Raids (real chase, heavy hand), or **(c)** something that widens the candidate set without a bigger hand: for example, the rulebook's own **Dark** variant (hunters don't know the hand), not yet simulated. Once chosen, re-run `wisp_sim.py` for that row at 2,000+ games and adopt it as v0.2. WISP can then go to **Untested** with the excavation-slippage and hand-leak checks as playtest hypotheses.

Option (c) is now measured: [WISP_dark_variant_sim_note.md](WISP_dark_variant_sim_note.md). In Dark, the v0.1 dials (12/4/8/2) give 46–56% Skilled v Skilled escapes, with the catch at trail 6.3–6.6. Adopting Dark needs a setup fix: the hunters look away while the Wisp deals its own hand.

## 5. Caveats

- The hunters are exact. Humans may miss sprint possibilities or forget a miss, which favours the Wisp, so a 45–50% bot balance may play Wisp-friendly at the table.
- Tells (hesitation, where the Wisp looks) are not modelled.
- 3P (two hunters sharing a budget) is the same game in the sim. Shared deliberation is a table question.
