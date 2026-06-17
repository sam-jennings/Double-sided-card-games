# Product Vision & Collection Goals

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.

> This is a **tabletop game design project**, not a software product. Code exists only in service of game design (simulation, solving, print-and-play). The primary deliverables are **games, rulebooks, playtest plans, playtest reports, design analyses, and collection-level decisions**.

## The one-line vision

Design the best possible paired-symbol flip deck, then build a varied collection of small, replayable games that make that deck worth owning — games that feel like they *could only exist* because of this deck.

## What the project is

A collection of games built around a single unusual deck:

- **9 symbols, 36 double-faced cards.** Each card shows one symbol per face. Every pair of two different symbols appears on exactly one card — the deck is the complete graph **K₉** rendered as cards.
- Games may use smaller symbol subsets (6/15, 7/21, 8/28), but always as a **declared subset of the one master deck** — never a separate deck.
- The long-term goal is a *coherent system*, not a pile of one-offs: each game should explore the deck from a genuinely different angle.

## Collection identity (open decision)

The product shape is **not yet decided**. Candidate forms:

- One boxed collection (all games, one deck, one rulebook booklet)
- A print-and-play anthology
- A flagship game (TRIGON) plus variants/expansions
- Something else

Treat "what shape is this product?" as a live design question. Don't assume a form; when a decision touches packaging, scope, or which games ship, surface the trade-offs.

## Criteria for belonging in the collection

A game earns its place only if it clears the evaluation rubric in `design-principles.md`. At the collection level, also ask:

- **Distinctness** — does it create an experience the other games don't already cover (genre, player count, length, mood, deck-property used)? Check against the coverage tables in `COLLECTION_OVERVIEW.md`.
- **Gap-filling** — does it fill a useful hole in player count / time / complexity / mood?
- **Deck necessity** — would it play just as well with an ordinary deck? If yes, it does not belong.
- **Teachability** — can it be explained cleanly and slot into a sensible learning order?

Be willing to cut. A clever game that overlaps an existing one, or that an ordinary deck could run, weakens the collection.

## Game maturity tiers — and how to treat each

Every game sits in one of four tiers. Respect the tier when proposing work.

1. **Table-tested (sim-tuned + at least one physical playtest)** — TWELVE TRIALS, CROSSROADS, THE ORRERY.
   - These have been both simulation-validated and physically played at the table. Priority is iterating on findings, running further playtests, or finalising rules based on table experience.
2. **Simulation/mathematically validated — needs first table test** — TRIGON, TURNCOAT, TURNOVER.
   - Numbers are checked; humans haven't played. TRIGON and TURNCOAT represent ~45k simulated games of investment but remain untested at the table. **Priority is the first table test**, not more simulation. Each carries explicit first-table questions — preserve and answer them.
3. **Rulebook complete — untested at the table** — JANUS, FALSE FACE, THE UNPLAYED PAIR, FACE VALUE, THE COUNCIL.
   - Full rules exist, zero plays. Priority is a first playtest and the test-focus questions already recorded for each.
4. **Cut / archived** — OUROBOROS.
   - Retained as a **design record only**. Cut after live testing (too luck-driven, hidden-face tracking awkward, thin skill gap). Its lessons are binding on all live designs — see `design-principles.md`.

When you propose work, state which tier the game is in and respect the priority that tier implies. The collection's current centre of gravity is **table testing**, not new design.

## Collaboration stance

Act as a board game development partner: practical, critical, and playtest-minded. Prefer concrete next steps, testable hypotheses, and clear trade-offs. Challenge ideas — including the owner's — that are elegant but fiddly, mathematically clever but unfun, or impossible to handle cleanly at the table. Do not preserve an idea just because it was suggested.
