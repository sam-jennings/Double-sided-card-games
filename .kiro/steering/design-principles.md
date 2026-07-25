# Game Design Principles

How to design, evaluate, and critique games on this deck. Pairs with `physical-handling.md` (the physical constraint) and `deck-structure.md` (the maths).

## Core principle

**The deck must earn its place in the game.** A game belongs in the collection if it would be meaningfully worse — or impossible — with a generic deck of cards. That's the bar. It is *not* required that every structural property of K₉ is consciously felt by the player; some games use the structure as visible puzzle, others as invisible infrastructure that makes the maths *work* while players think about something else entirely. Both are valid.

## Deck properties available to build on

These are the toolkit, not a checklist. A good game leans hard on one or two; it does not need to touch all of them.

- **Every pair exists exactly once** → deduction, counting, finite/shrinking lie-spaces, public registries, guaranteed-find searches.
- **Each symbol on exactly 8 cards** → knowable scarcity, forced-feeding endgames, majority/shortage tension.
- **Smaller subsets are exact all-pairs decks** → tune player count / length per game via declared symbol range.
- **Flipping swaps the active symbol** → reversible commitment, defection, denial, route reorientation, choosing which face to play.
- **A card is an edge between two symbols** → connections, allegiances, routes, promises, lies, reversible commitments, triangle logic.
- **The pressed (hidden) face + the public pair-registry** → *deliberate* memory/deduction: track or deduce the down-face over time, bounded and made verifiable by every-pair-once. **Currently under-served** — most games strip memory out, so a well-built memory game is a deliberate target, not a risk (see lesson 1 under Binding Constraints).
- **The deck can generate its own board/state** (CROSSROADS city ring, TRIGON grid, TWELVE TRIALS 6×6) — prefer this over external components.

---

## Evaluation framework

The old rubric was a ten-item scoring checklist. In practice, games that ticked every structural box sometimes played like homework, while games that scored lower on a few dimensions turned out to be the most exciting at the table. The framework below replaces the checklist with a layered diagnostic.

### Layer 1 — Hard floors (non-negotiable)

These are pass/fail. A game that fails either one does not belong, regardless of how clever it is.

1. **Physical viability.** It must work cleanly with double-faced cards. Run the `physical-handling.md` checklist; any unresolved handling bug is a blocker.
2. **Deck necessity.** An ordinary deck of cards (or generic tokens) could *not* deliver the same experience. The deck's structure must be doing real work — but that work can be invisible infrastructure, not just a player-facing puzzle.

### Layer 2 — Structural engagement (spectrum, not checklist)

Among the deck properties listed above, the game should be **load-bearing on at least one** in a way that creates interesting player decisions or emergent situations. It does not need to use all of them. Diagnostic questions:

- What deck property is the engine of this game? (Name it concretely.)
- If you removed that property — swapped in a generic deck — would the game collapse, get worse, or stay the same?
- Is there a *second* property doing meaningful work, or is the game a one-property design? (One is fine. Two is a bonus, not a requirement.)

Games that lean on a single property deeply (CROSSROADS: deck-as-board + orientation) are just as valid as games that weave several lightly (TRIGON: pairs + flipping + triangles).

**What this replaces:** The old items "does flipping matter?", "does pair uniqueness matter?" are no longer individual gates. A game where flipping is rare but dramatic (a single defection moment) is not penalised for low flip-frequency — the question is whether the flip, when it happens, *matters*. A game where pair uniqueness is invisible infrastructure (players never consciously think "this pair is unique") but the scarcity math it creates is the engine — that's using the deck.

### Layer 3 — Table quality (the dimension the old rubric was missing)

These do not override Layer 1, but they are what separates a *correct* game from a *good* one. Score these from observation (playtests, walkthroughs, or honest self-play), not from rules-reading alone.

- **Tension & moments.** Does the game create points where the table leans in — surprise, dread, a hard choice, laughter, a groan? A game with clean structure but no peaks is a solved problem, not a game.
- **Social texture.** Does it generate interaction — negotiation, bluffing, reading opponents, shared crises, schadenfreude? (Solo/puzzle games get a pass here, but multiplayer games without interaction are suspect.)
- **Discovery curve.** Does it get *better* as players learn it? Are there strategies to find, not just procedures to follow? A game whose first play is its best play has no replay life.
- **Pacing & arc.** Does it build toward something? Does it know when to end? Does downtime stay tolerable?
- **Feel.** Is the dominant emotion during play interesting (not just "thinking hard")? Does the theme/framing help or is it wallpaper?

A game that clears Layers 1–2 but has no life in Layer 3 needs design work, not rejection. Layer 3 problems are often fixable (add a timing pressure, surface a hidden interaction, cut a dead phase). But a game that *cannot* generate table quality — where the structure just doesn't produce interesting moments no matter how you tune it — that's the signal to park or cut.

### Layer 4 — Practicality (tiebreakers and scheduling)

These don't determine whether a game is *good*, but they determine whether it's *worth working on next*:

- Can it be **explained cleanly**?
- Does its **player count / time / complexity** fill a gap in the collection?
- Can it be **tested with the current prototype** (the printed Set D deck)?
- **What is the fastest way to falsify whether it is fun?**

A game that's hard to explain might still be great (complexity isn't a sin if the depth justifies it). A game that overlaps existing coverage might still be better than what it overlaps. These are factors for prioritisation, not gates for inclusion.

---

## What counts as a "bug" (tabletop equivalents)

Treat these as defects to be found and fixed, the way code bugs are:

- Rules ambiguity or unverifiable legality
- Degenerate / dominant strategies
- Physical handling problems (the big one — see `physical-handling.md`)
- Runaway scoring / inability to come back
- Kingmaking (a losing player decides the winner)
- Downtime between turns
- Involuntary memory burden (memory as overhead, not as the game)
- Unfun incentives (rules that reward boring play)
- Non-termination (games that can fail to end)
- **Flatness** — a game that works mechanically but never produces a memorable moment across multiple plays

---

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
7. Open information, public registries, visible state, and exact deduction usually beat hidden-card conventions on this deck — but this is a *default*, not a law. Deliberate opacity is a valid design choice when it creates the game's core tension.

---

## On innovation and the rubric's limits

The structural properties of this deck are finite and known. If every game must consciously foreground them, the collection converges on a narrow band of deduction-and-flip puzzles. The best games often use the deck's properties as **invisible infrastructure** — the maths makes the game *work*, but the player's experience is about something else: route-building, social reading, timing, territory.

**Don't design to the rubric. Design to the table.** The rubric exists to catch games that don't need this deck at all, and to catch handling bugs. It is not a recipe for fun. A game that scores 2/5 on structural engagement but makes people want to play again immediately is worth more than one that scores 5/5 but gets shelved after two plays.

When evaluating a new concept, ask:
- Would I want to play this again after the first game?
- Is there a moment in this game I'd tell someone about?
- Does it make me *feel* something the other games in the collection don't?

If the answers are yes and it clears the hard floors, pursue it — even if it only touches one deck property lightly.

---

## Critique stance

When asked for ideas or changes:
- Be critical. Don't preserve an idea just because it was suggested (by anyone, including the owner).
- Challenge rules that are elegant-but-fiddly, clever-but-unfun, or impossible to handle cleanly.
- Prefer fewer rules, cleaner handling, and faster paths to "is this fun?"
- Offer concrete next steps and testable hypotheses, not vague praise.
- **Don't let structural purity override table evidence.** If a playtest shows a game is exciting but it only lightly uses pair uniqueness, that is not a problem to solve — it's a data point that the game works.

## General board-game craft (external reference)

The deck-specific rules here sit *on top of* general board-game design craft, not instead of it. `Reference/Game Development Notes/Board Game Design Knowledge Base.md` synthesises that craft — player experience, mechanics, interaction, theme, visual design/ergonomics, rules-writing, playtesting, production, business, and pitching. When working on anything it covers, consult it and apply the relevant principles. Where the deck's physical (`physical-handling.md`) or mathematical (`deck-structure.md`) constraints conflict with generic advice, the deck wins.

## Vocabulary mapping (software → tabletop)

- **Implementation** = writing rules, building prototypes, running simulations, conducting playtests.
- **Acceptance criteria** = observable playtest outcomes / measurable sim results.
- **Architecture** = game structure, component flow, information flow, table layout.
- **Bug** = any defect in the list above.
- **Test** = a playtest or a simulation run, depending on what the question needs (see `playtesting.md` and `simulation-standards.md`).
