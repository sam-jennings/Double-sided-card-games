# Game Design Principles

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.

How to design, evaluate, and critique games on this deck. Pairs with `physical-handling.md` (the physical constraint) and `deck-structure.md` (the maths).

## Core principle

**Prefer designs where the deck's unique properties are load-bearing.** A game should feel like it could only exist because of this deck. If an ordinary deck of cards could run it just as well, it does not belong in the collection.

Properties worth building on:

- **Every pair exists exactly once** → deduction, counting, finite/shrinking lie-spaces, public registries.
- **Each symbol on exactly 8 cards** → knowable scarcity, forced-feeding endgames, majority/shortage tension.
- **Smaller subsets are exact all-pairs decks** → tune player count / length per game via declared symbol range.
- **Flipping swaps the active symbol** → reversible commitment, defection, denial, route reorientation, choosing which face to play.
- **A card is an edge between two symbols** → connections, allegiances, routes, promises, lies, reversible commitments, triangle logic.
- **The deck can generate its own board/state** (CROSSROADS city ring, TRIGON grid, TWELVE TRIALS 6×6) — prefer this over external components.

## Evaluation rubric

Score every game idea or change against these. Be critical and concrete.

1. Does it **exploit the all-pairs deck** (not just use generic symbols)?
2. Does it **physically work** with double-faced cards? (Run the `physical-handling.md` checklist.)
3. Is the required information **visible or legally deducible** — not dependent on hidden-face memory?
4. Does **flipping matter** — create real decisions, reversals, threats, or opportunities?
5. Does **pair uniqueness matter**?
6. Does it create a **distinct experience** from the existing games?
7. Does its **player count / time / complexity** fill a useful gap?
8. Can it be **explained cleanly**?
9. Can it be **tested with the current prototype** (the printed Set D deck)?
10. **What is the fastest way to falsify whether it is fun?**

A game that can't answer 1–5 well is probably not for this deck. A game that can't answer 8–10 well is probably not worth prototyping yet.

## What counts as a "bug" (tabletop equivalents)

Treat these as defects to be found and fixed, the way code bugs are:

- Rules ambiguity or unverifiable legality
- Degenerate / dominant strategies
- Physical handling problems (the big one — see `physical-handling.md`)
- Runaway scoring / inability to come back
- Kingmaking (a losing player decides the winner)
- Downtime between turns
- Memory burden, especially hidden-face memory
- Unfun incentives (rules that reward boring play)
- Non-termination (games that can fail to end)

## Lessons already learned — binding constraints

From the OUROBOROS post-mortem and the TRIGON/TURNCOAT simulation work. **Do not repeat these mistakes:**

1. Don't rely on players remembering hidden faces when the physical state makes rechecking annoying.
2. Don't put constantly-needed state on the hidden/down face of a card.
3. Don't assume "face-down" works like a normal card game — it doesn't (no back).
4. Don't design hidden information that collapses because the holder can inspect both sides.
5. Don't accept a rule just because it's mathematically elegant — table handling and fun decide.
6. **A thin skill gap between random and skilled play is a warning sign of a dull game.** Simulation should show skilled play clearly beating random (the collection treats ~1.5× and up as healthy). If it doesn't, suspect the design, not the bot.
7. Open information, public registries, visible state, and exact deduction usually beat hidden-card conventions on this deck.

## Critique stance

When asked for ideas or changes:
- Be critical. Don't preserve an idea just because it was suggested (by anyone, including the owner).
- Challenge rules that are elegant-but-fiddly, clever-but-unfun, or impossible to handle cleanly.
- Prefer fewer rules, cleaner handling, and faster paths to "is this fun?"
- Offer concrete next steps and testable hypotheses, not vague praise.

## Vocabulary mapping (software → tabletop)

- **Implementation** = writing rules, building prototypes, running simulations, conducting playtests.
- **Acceptance criteria** = observable playtest outcomes / measurable sim results.
- **Architecture** = game structure, component flow, information flow, table layout.
- **Bug** = any defect in the list above.
- **Test** = a playtest or a simulation run, depending on what the question needs (see `playtesting.md` and `simulation-standards.md`).
