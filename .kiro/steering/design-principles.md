# Game Design Principles

How to design, evaluate, and critique games on this deck. Pairs with `physical-handling.md` (the physical constraint) and `deck-structure.md` (the maths).

## Core principle

**Prefer designs where the deck's unique properties are load-bearing.** A game should feel like it could only exist because of this deck. If an ordinary deck of cards could run it just as well, it does not belong in the collection.

Properties worth building on:

- **Every pair exists exactly once** → deduction, counting, finite/shrinking lie-spaces, public registries.
- **Each symbol on exactly 8 cards** → knowable scarcity, forced-feeding endgames, majority/shortage tension.
- **Smaller subsets are exact all-pairs decks** → tune player count / length per game via declared symbol range.
- **Flipping swaps the active symbol** → reversible commitment, defection, denial, route reorientation, choosing which face to play.
- **A card is an edge between two symbols** → connections, allegiances, routes, promises, lies, reversible commitments, triangle logic.
- **The pressed (hidden) face + the public pair-registry** → *deliberate* memory/deduction: track or deduce the down-face over time, bounded and made verifiable by every-pair-once. **Currently under-served** — most games strip memory out, so a well-built memory game is a deliberate target, not a risk (see lesson 1, `physical-handling.md`).
- **The deck can generate its own board/state** (CROSSROADS city ring, TRIGON grid, TWELVE TRIALS 6×6) — prefer this over external components.

## Evaluation rubric

Score every game idea or change against these. Be critical and concrete.

1. Does it **exploit the all-pairs deck** (not just use generic symbols)?
2. Does it **physically work** with double-faced cards? (Run the `physical-handling.md` checklist.)
3. Is the required information **visible or legally deducible** — not dependent on *involuntary* hidden-face memory? (Deliberate, verifiable, roughly symmetric hidden-face memory is a legitimate **core** mechanic — see lesson 1. The failure mode is memory as *involuntary overhead*, not memory as the game.)
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

1. Hidden-face **memory and deduction are legitimate, deck-suited mechanics.** A game *built on* tracking or deducing the pressed face is welcome — the caution is narrower: don't impose hidden-face tracking as *involuntary bookkeeping* (mandatory, thin-payoff, and physically awkward to recheck). Make it a chosen challenge, not background overhead. This is currently **under-served**: most games in the collection deliberately strip memory out and advertise "no hidden-face memory" as a virtue. A deliberate, verifiable memory game is an **explicit design target**, not a merely-tolerated option — don't reflexively cite OUROBOROS to avoid it (OUROBOROS was not a memory game; it buried *involuntary* state, which is a different defect).
2. Don't bury **constantly-needed, low-payoff** state on the hidden/down face. (If tracking the hidden face *is* the game, that's fine — see 1. OUROBOROS failed because the open symbol lived under the serpent's head *as overhead*, with a thin skill gap on top.)
3. Don't assume "face-down" works like a normal card game — it doesn't (no back).
4. Don't design hidden information that collapses because the holder can inspect both sides.
5. Don't accept a rule just because it's mathematically elegant — table handling and fun decide.
6. **A thin skill gap between random and skilled play is a warning sign of a dull game** — but read the gap carefully before condemning the design. Simulation should show skilled play clearly beating random (the collection treats ~1.5× and up as healthy). Two cautions the OUROBOROS post-mortem actually teaches, and which were under-weighted in the original cut:
   - **(a) Obvious-strategy gap ≠ ceiling.** OUROBOROS's *greedy* (beginner-obvious) line beat random only ~1.13×, but a counter-intuitive **hand-stewardship** line reached ~1.67×. A game can hide a real skill ceiling behind a near-random *obvious* strategy. That is a **teaching/onboarding problem** (surface the real skill in the rulebook) — possibly fixable, not automatically a dead game.
   - **(b) A one-ply bot is a floor, not a ceiling.** If a shallow bot shows a thin gap, try a deeper/lookahead bot (or watch a thoughtful human) before concluding the design is dull. Suspect the bot's depth as well as the design — the OUROBOROS analysis itself flagged its one-ply bots as underselling humans, yet the cut leaned on those floor numbers.
7. Open information, public registries, visible state, and exact deduction usually beat hidden-card conventions on this deck.

## Critique stance

When asked for ideas or changes:
- Be critical. Don't preserve an idea just because it was suggested (by anyone, including the owner).
- Challenge rules that are elegant-but-fiddly, clever-but-unfun, or impossible to handle cleanly.
- Prefer fewer rules, cleaner handling, and faster paths to "is this fun?"
- Offer concrete next steps and testable hypotheses, not vague praise.

## General board-game craft (external reference)

The deck-specific rules here sit *on top of* general board-game design craft, not instead of it. `Reference/Game Development Notes/Board Game Design Knowledge Base.md` synthesises that craft — player experience, mechanics, interaction, theme, visual design/ergonomics, rules-writing, playtesting, production, business, and pitching. When working on anything it covers, consult it and apply the relevant principles. Where the deck's physical (`physical-handling.md`) or mathematical (`deck-structure.md`) constraints conflict with generic advice, the deck wins.

## Vocabulary mapping (software → tabletop)

- **Implementation** = writing rules, building prototypes, running simulations, conducting playtests.
- **Acceptance criteria** = observable playtest outcomes / measurable sim results.
- **Architecture** = game structure, component flow, information flow, table layout.
- **Bug** = any defect in the list above.
- **Test** = a playtest or a simulation run, depending on what the question needs (see `playtesting.md` and `simulation-standards.md`).
