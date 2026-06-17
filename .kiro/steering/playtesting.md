# Playtesting Methodology

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.

The collection's current centre of gravity. Most games are simulation- or rulebook-complete but **untested at the table** — the highest-value work right now is running first playtests and recording what they reveal.

## Why this matters most now

Simulation certifies the floor (the game ends, isn't broken, defaults are sound). It cannot tell us whether a game is fun, teachable, or physically pleasant. Only humans can. Every tier-2 and tier-3 game (see `product-vision.md`) is waiting on its first table test.

## Every game carries test-focus questions

Each game already has recorded first-table / test-focus questions (in `COLLECTION_OVERVIEW.md` and `NEW_GAME_CONCEPTS.md`) — e.g. TURNOVER's "is announce-rule policing fun?", CROSSROADS' "does eight flips ache properly?", THE COUNCIL's "kingmaking at 5–6P?". **A playtest plan must start from that game's specific questions.** Preserve and answer them; don't invent generic ones.

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

## Standards

- A first playtest of an untested game **outranks** further simulation of an already-validated one. Don't over-simulate to avoid the table.
- Be honest in reports. A refuted hypothesis is the point of testing, not a setback.
- Feed lessons back into the binding constraints in `design-principles.md` when a test teaches something general about the deck.
- Tie every proposed rule change to a specific observed problem — no speculative tinkering.
