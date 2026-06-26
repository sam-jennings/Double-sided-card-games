# Product Vision & Collection Goals

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

## The pipeline and the collection

Games exist in two worlds: **the pipeline** (a workshop where anything goes) and **the collection** (the curated set of games that have earned their place through table play).

### Pipeline stages

Every game starts in the pipeline and moves through stages as work is done. There is no obligation to advance games in any order — work on whatever is useful or exciting right now.

| Stage | Name | What it means | What exists |
|---|---|---|---|
| 0 | **Spark** | A one-liner or concept sketch. May never go further. | A line in `NEW_GAME_CONCEPTS.md` |
| 1 | **Draft** | Rules written — possibly rough, possibly unread. You could sit down and *read* it. | A rulebook (possibly rough) |
| 2 | **Validated** | Stress-tested via simulation, solver, mathematical analysis, or deep manual walkthrough. You believe it *works*. | Rulebook + design analysis and/or sim results |
| 3 | **Table-tested** | Humans have played it at least once. You have data. | Rulebook + at least one playtest report |

Stages are descriptive, not prescriptive. A game can jump from Spark to Validated if you sit down and sim it before writing full rules. A game can stay at Draft forever if you're not ready to push it.

### The collection gate

A game is **promoted to the collection** only after reaching Stage 3, and only if:

1. The first playtest verdict was **"iterate"** (not "park" or "cut").
2. It passes the evaluation rubric in `design-principles.md`.
3. It satisfies the collection criteria below.

Until promotion, a game is a **pipeline game** — a work in progress with no status anxiety attached.

### Criteria for belonging in the collection

A game earns its place only if it clears the evaluation rubric in `design-principles.md`. At the collection level, also ask:

- **Distinctness** — does it create an experience the other games don't already cover (genre, player count, length, mood, deck-property used)? Check against the coverage tables in `COLLECTION_OVERVIEW.md`.
- **Gap-filling** — does it fill a useful hole in player count / time / complexity / mood?
- **Deck necessity** — would it play just as well with an ordinary deck? If yes, it does not belong.
- **Teachability** — can it be explained cleanly and slot into a sensible learning order?

Be willing to cut. A clever game that overlaps an existing one, or that an ordinary deck could run, weakens the collection.

### Cut / archived

Games that are explicitly cut are retained as **design records**. OUROBOROS, the only game cut so far, was **revived to the pipeline in June 2026** after its cut reasons were re-examined (a fixable handling bug plus a skill gap that proved to be a one-ply artefact) — a worked example of confronting *and revisiting* a cut. A cut is a strong signal, not necessarily permanent: revive only by confronting, with evidence, why it was cut. Lessons from cuts remain binding on live designs — see `design-principles.md`.

## Collaboration stance

Act as a board game development partner: practical, critical, and playtest-minded. Prefer concrete next steps, testable hypotheses, and clear trade-offs. Challenge ideas — including the owner's — that are elegant but fiddly, mathematically clever but unfun, or impossible to handle cleanly at the table. Do not preserve an idea just because it was suggested.
