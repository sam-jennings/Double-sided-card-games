# Product Vision & Collection Goals

> This is a **tabletop game design project**, not a software product. Code exists only in service of game design (simulation, solving, print-and-play). The primary deliverables are **games, rulebooks, playtest plans, playtest reports, design analyses, and collection-level decisions**.

## The one-line vision

Design the best possible paired-symbol flip deck, then build a varied collection of small, replayable games that make that deck worth owning — games that feel like they *could only exist* because of this deck.

## What the project is

A collection of games built around a single unusual deck:

- **9 symbols, 36 double-faced cards.** Each card shows one symbol per face. Every pair of two different symbols appears on exactly one card — the deck is the complete graph **K₉** rendered as cards.
- Games may use smaller symbol subsets (6/15, 7/21, 8/28), but always as a **declared subset of the one master deck** — never a separate deck.
- The long-term goal is a *coherent system*, not a pile of one-offs: each game should explore the deck from a genuinely different angle.

## Collection identity (deferred product question)

The product shape is **not yet decided**. Candidate forms:

- One boxed collection (all games, one deck, one rulebook booklet)
- A print-and-play anthology
- A flagship game (TRIGON) plus variants/expansions
- Something else

The product shape is intentionally **not a current priority**. Earlier Core Set,
publisher, packaging, and launch work lives in `Later/Publishing/` and must not
set ordinary design or playtesting priorities. Revisit the product question only
when the owner explicitly returns to publication planning.

## The collection and how games are classified

Every game is part of the collection and is classified by **two fields, and only
two**. The YAML properties on each game's single game record are the structured source;
`COLLECTION_OVERVIEW.md` is the complete human-readable catalogue.

### Field 1 — `state`: what a player can expect

Exactly one of five values. The deck and website go to friends as playtesters, so the states are worded for them: each says what happens if you sit down and play. There is no obligation to advance games in any order — work on whatever is useful or exciting right now.

| State | What it means (player-facing) | What exists / what it needs next |
|---|---|---|
| **Proven** | Played and works. Just play it. | Rulebook + playtest report, no known blocking problem. Needs final polish or a confirming test, if anything. |
| **Rough edges** | Has been played; works in general but has known bugs or open questions. Your feedback helps — you may even find the fix. | Rulebook + playtest report + a one-line **known issue** shown on `games.html` and at the top of the rules. Needs the queued fix tested, or the open question answered, at a table. |
| **Untested** | Complete rules, never played. You're the first table; expect surprises. | A complete rulebook (sim-validated where possible). Needs its first table. While the designer has not reviewed an AI-written rulebook, `games.html` says "Rules not yet reviewed by the designer". |
| **In the workshop** | Not playable yet: an idea only, or rules with a known problem to solve first. | Anything from a one-line concept sheet to a draft rulebook waiting on a design decision. Needs rules written, completed, or redesigned. |
| **Shelved** | Set aside, kept as a design record. | Whatever exists. Needs nothing unless revived. |

State is descriptive, not prescriptive, and **moves in both directions**. A game can sit In the workshop forever if you're not ready to push it; a Proven game that a later session breaks drops to Rough edges (if a table can still play it) or In the workshop (if it can't) until the fix is designed.

### Field 2 — `physically_playtested`: have humans ever played it?

A boolean, independent of `state`, that becomes `true` after the first table test and **never reverts**. Playtest history is permanent; design readiness oscillates, so the two must not share a field.

The two fields line up as follows:

- `Proven` and `Rough edges` — always played.
- `Untested` — never played.
- `In the workshop` — usually never played, but a played game goes back here if it needs design work before another table.
- `Shelved` — either.

Detailed verdicts live in the playtest reports; the single next action lives in `next_step`. Do not reintroduce a `status`, `table_tested`, or `playtest_ready` field — "can I play it tonight?" is `state` in Proven / Rough edges / Untested, and "have I tested it?" is `physically_playtested`.

**Badges, not states.** Simulation, solving, and versioning are *evidence*, not state — record them as badges alongside it (`sim-validated`, `solver-checked`, `v1.1`, `testable at 2P now`). A sim badge is often what earns a game its way to Untested. The one wrinkle is a concept simmed *before* its rules are written (e.g. a structural sim with no rulebook yet): it stays **In the workshop** — you can't read rules that don't exist — and the badge carries the work done.

### No promotion or shipping axis

The retired “promoted / in-collection” flag and the deferred “Core Set” are not
game states. Do not recreate them in the catalogue. Games set aside or removed are
both **Shelved**; their folders stay as design records.

### Collection-quality questions

When deciding whether a game strengthens the body of work, ask:

- **Distinctness** — does it create an experience the other games don't already cover (genre, player count, length, mood, deck-property used)? Check against the coverage tables in `COLLECTION_OVERVIEW.md`.
- **Gap-filling** — does it fill a useful hole in player count / time / complexity / mood?
- **Deck necessity** — would it play just as well with an ordinary deck? If yes, it does not belong.
- **Teachability** — can it be explained cleanly and slot into a sensible learning order?

Be willing to park or cut. A clever game that overlaps an existing one, or that an ordinary deck could run, can still weaken the collection even when nothing is being prepared for publication.

### Shelved / archived

Shelved games are retained as **design records**. OUROBOROS, the only game ever dropped outright, was **revived in June 2026** (now Rough edges) after its reasons were re-examined (a fixable handling bug plus a skill gap that proved to be a one-ply artefact) — a worked example of confronting *and revisiting* that decision. Shelving is a strong signal, not necessarily permanent: revive only by confronting, with evidence, why it was shelved. The lessons remain binding on live designs — see `design-principles.md`.

## Collaboration stance

Act as a board game development partner: practical, critical, and playtest-minded. Prefer concrete next steps, testable hypotheses, and clear trade-offs. Challenge ideas — including the owner's — that are elegant but fiddly, mathematically clever but unfun, or impossible to handle cleanly at the table. Do not preserve an idea just because it was suggested.
