# Playtesting Methodology

Table testing is how a game earns a real verdict and moves along the health ladder. It's also how already-good games get better. This document covers the methodology for both.

## Why table testing matters

Simulation certifies the floor (the game ends, isn't broken, defaults are sound). It cannot tell us whether a game is fun, teachable, or physically pleasant. Only humans can. Many games with `physically_playtested: false` (see the classification fields in `product-vision.md`) are waiting on their first table test — but there's no mandate to test them in any order. Test what you're excited to test.

## Every game carries test-focus questions

Each game has a structured `next_step` on its game record and fuller first-table / test-focus questions in `COLLECTION_OVERVIEW.md` and its design analysis or latest report. `NEW_GAME_CONCEPTS.md` is historical context, not a current state source. **A playtest plan must start from that game's current questions.** Preserve and answer them; don't invent generic ones.

## Playtest plan (before a session)

Write a short plan — kept in the game's folder, alongside the report it will pair with — containing:

- **Game, version, player count, symbol subset** being tested.
- **Hypotheses to test** — the game's recorded questions, framed as falsifiable predictions ("a thoughtful first TWELVE TRIALS game lands near 7 flips").
- **What to watch** — the specific handling, pacing, or balance risk this session targets.
- **Observable success/failure signals** — what you'd see if the hypothesis holds vs. fails (these are the tabletop equivalent of acceptance criteria).
- **Teaching plan** — how the game gets taught, and what to watch for during teaching (teachability is itself under test).

## During the session — what to record

- **Handling problems first** — anything awkward with the double-faced cards (buried state, accidental face reveals, fiddly verification, hidden-face memory strain). These are the project's most common and most serious bugs.
- **Comprehension** — what confused players, which rules needed re-explaining, where the rulebook was silent.
- **Pacing & downtime** — turn length, dead time, whether the game overstays.
- **Degenerate play** — dominant strategies, runaway leaders, kingmaking, stalls.
- **Engagement & fun** — where the table leaned in, laughed, agonised, or checked out.
- **Outcome data** — scores, length, who won, seat order, surprises vs. the sim's predictions.

## Playtest report (after a session)

Record a report in the game's folder. Include:

- Setup (version, players, count, subset, date).
- Each hypothesis and whether the session **confirmed, refuted, or left it open**.
- Bugs found, categorised (see the bug list in `design-principles.md`), severity-ranked.
- Concrete rule-change candidates, each tied to an observation.
- A verdict (see below).

## The decision: iterate, park, or cut

Every first test ends with one of three calls, made explicitly:

- **Iterate** — promising, with identified fixes. Apply rule changes, bump the version, re-test (or re-sim if the change is balance-sensitive).
- **Park** — fundamentally sound but not a priority, or blocked on a bigger open decision. Record why and what would unblock it.
- **Cut** — a core flaw that the deck or the concept can't escape. Cut decisively, **keep the folder as a design record**, and write down the lessons (as with OUROBOROS). A clean cut that teaches a lesson is a success, not a failure.

### After every session — set `physically_playtested` and the `state`

Two things change on the game record after a table test.

**Always set `physically_playtested: true`.** It is now permanently true, whatever the session revealed.

**Then set the `state`** (see `product-vision.md`) — the condition you're leaving the game in. An "iterate" verdict is doing too much work if it isn't qualified, so always name the shade:

| Verdict | State to record | Reads as |
|---|---|---|
| Iterate | **Proven** | Played, very happy, only minor polish left — nothing blocking. |
| Iterate | **Ready to test** | Works, with known bugs whose fixes are easy and already queued; put it back on the table. |
| Iterate | **In development** | Didn't really work; needs bigger fixes or a rethink before it's worth another table. |
| Park | **Shelved** | Sound but set aside; folder kept. |
| Cut | **Shelved** | Core flaw the concept can't escape; folder kept as a design record. |

The distinction that matters at the middle two rungs is whether you'd hand the current rules to a table *tonight*. If yes, it stays **Ready to test**; if the next session needs design work first, it drops to **In development** — as JANUS did. A game that was **Proven** and then breaks drops the same way until a re-test. `physically_playtested` stays true throughout, so a dropped game is still visibly one you have actually played.

Record the detailed verdict in the playtest report and the single next action in `next_step`. Do not add a separate status or readiness field to carry the nuance.

## Standards

- A first playtest of an untested game **outranks** further simulation of an already-validated one. Don't over-simulate to avoid the table.
- Be honest in reports. A refuted hypothesis is the point of testing, not a setback.
- Feed lessons back into the binding constraints in `design-principles.md` when a test teaches something general about the deck.
- Tie every proposed rule change to a specific observed problem — no speculative tinkering.
