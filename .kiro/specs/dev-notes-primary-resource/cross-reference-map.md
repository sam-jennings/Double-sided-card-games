# Cross-Reference Map — Pass A (Task 1.1)

> **Working artifact** for the `dev-notes-primary-resource` spec. Produced by Pass A
> (inventory + cross-reference map). Pass B (reference integrity) and Pass E
> (reconciliation) re-walk this map. This file lives in the spec folder, not in
> `.kiro/steering/`. No steering file was edited to produce it.

## 1. Directory inventory

`.kiro/steering/` holds exactly **8 files** — matches the design's inventory table.

| # | File | Role | Auto-load |
|---|---|---|---|
| 1 | `product-vision.md` | Core_Note | always (steering) |
| 2 | `deck-structure.md` | Core_Note | always (steering) |
| 3 | `design-principles.md` | Core_Note | always (steering) |
| 4 | `physical-handling.md` | Core_Note | always (steering) |
| 5 | `playtesting.md` | Core_Note | always (steering) |
| 6 | `repository-structure.md` | Core_Note | always (steering) |
| 7 | `simulation-standards.md` | Referenced_Note | `fileMatch '*sim*.py'` |
| 8 | `rulebook-standards.md` | Referenced_Note | `fileMatch '*rulebook*'` |

**Confirmed:** 6 Core_Notes + `simulation-standards.md` + `rulebook-standards.md`. No missing
file, no extra file. The clarify-phase "six files / no simulation-standards" assumption is
stale, as the design already corrected.

Note on auto-load (relevant to Req 6.4): the 6 Core_Notes are unconditionally steering-loaded,
but the two Referenced_Notes carry `inclusion: fileMatch` front-matter, so they load only when a
matching file (`*sim*.py` / `*rulebook*`) is open. This matters for the primacy mechanism in
Pass D — primacy lands in the 6 always-loaded Core_Notes, which is consistent with Req 5/6.

## 2. Cross-reference records (CrossReference tuples)

Fields: citing note · cited target · `target_in_dir?` (is target a file inside `.kiro/steering/`)
· attributed topic. Kind = **S→S** (steering→steering) or **S→T** (steering→top-level project doc).

### 2a. Steering → steering pointers (in-audit; must resolve in `.kiro/steering/`)

| Citing note | Cited target | target_in_dir? | Attributed topic |
|---|---|---|---|
| `product-vision.md` | `design-principles.md` | yes | evaluation rubric; binding OUROBOROS lessons ("Its lessons are binding … see") |
| `deck-structure.md` | `physical-handling.md` | yes | no-asymmetric-marks rule leaks hidden-face info |
| `deck-structure.md` | `design-principles.md` | yes | "would generic symbols do?" / reconsider test |
| `deck-structure.md` | `simulation-standards.md` | yes | assert combinatorial facts must be verifiable — prefer computing |
| `design-principles.md` | `physical-handling.md` | yes | the physical constraint; the handling checklist; handling-bug flag |
| `design-principles.md` | `deck-structure.md` | yes | the maths |
| `design-principles.md` | `playtesting.md` | yes | "Test = a playtest …" testing stance |
| `design-principles.md` | `simulation-standards.md` | yes | "Test = … a simulation run …" testing stance |
| `physical-handling.md` | `design-principles.md` | yes | flag failing rule as a handling bug (the bug list) |
| `playtesting.md` | `product-vision.md` | yes | tier-2/tier-3 definitions (tiers) |
| `playtesting.md` | `design-principles.md` | yes | the bug list / bug categories; binding constraints feedback |
| `repository-structure.md` | `playtesting.md` | yes | where playtest plans & reports live |
| `simulation-standards.md` | `playtesting.md` | yes | fun/pacing/teachability decided at the table |
| `rulebook-standards.md` | `physical-handling.md` | yes | the no-back deck constraint |

**All 14 steering→steering pointers resolve to existing files in `.kiro/steering/`.**
No dangling steering reference exists. Pass B records this as a confirmation, not a repair.
Topic-fidelity (`topic_satisfied`) is left for Pass B to adjudicate per target.

### 2b. Steering → top-level project doc pointers (out-of-audit targets; existence confirmed)

| Citing note | Cited target | exists? | Attributed topic |
|---|---|---|---|
| `product-vision.md` | `COLLECTION_OVERVIEW.md` | yes | coverage tables for distinctness check |
| `deck-structure.md` | `DECK_SIZE_DECISION.md` | yes | the 9-symbol decision is settled |
| `deck-structure.md` | `SYMBOL_SETS.md` | yes | symbol-9 identity; full symbol study |
| `playtesting.md` | `COLLECTION_OVERVIEW.md` | yes | recorded test-focus questions |
| `playtesting.md` | `NEW_GAME_CONCEPTS.md` | yes | recorded test-focus questions |
| `repository-structure.md` | `DECK_SIZE_DECISION.md` | yes | example top-level cross-game doc |
| `repository-structure.md` | `COLLECTION_OVERVIEW.md` | yes | canonical index / status |
| `repository-structure.md` | `NEW_GAME_CONCEPTS.md` | yes | new game pitches |
| `simulation-standards.md` | `DECK_SIZE_DECISION.md` | yes | record verification method in an appendix |

All 9 top-level targets exist at the workspace root (`COLLECTION_OVERVIEW.md`,
`DECK_SIZE_DECISION.md`, `SYMBOL_SETS.md`, `NEW_GAME_CONCEPTS.md`). These are legitimate
reference targets (canonical index + decision records), not part of the edit set, and none is
a Parallel_Copy. No Core_Note points the reader at a Parallel_Copy as authority.

### 2c. Non-pointer mentions (catalogued, not cross-references)

These are filename *examples / benchmarks*, not "see X.md" guidance pointers, so they need no
resolution:

- `repository-structure.md`: `<GAME>_rulebook.md`, `<GAME>_design_analysis.md`, `<game>_sim.py`
  (naming-convention templates); `Twelve Trials/`, `Ouroboros/`, `Print and Play/make_pnp.py`
  (layout examples); `flip_card_project_goals.md` (layout-tree entry, exists).
- `simulation-standards.md`: `Wildfire/wildfire_sim.py`, `WILDFIRE_design_analysis.md` (named benchmarks).
- `rulebook-standards.md`: `Syzygy/SYZYGY_rulebook.md` (named benchmark).

## 3. Anomalies / notes for Pass B

1. **`playtesting.md` → `simulation-standards.md` is conceptual, not a literal pointer.**
   The design's Pass-A map lists this edge "(via stance)". Confirmed: `playtesting.md` discusses
   the sim-vs-table division ("further simulation", "over-simulate") but contains **no literal
   `` `simulation-standards.md` `` pointer**. The reciprocal link exists
   (`simulation-standards.md` → `playtesting.md`). Pass B / Pass C may consider whether
   `playtesting.md` should cite `simulation-standards.md` explicitly for the sim-vs-table stance
   (relevant to Req 4.2/4.3 fidelity), but this is **not** a broken reference — nothing dangles.

2. **No dangling steering references.** Every literal `*.md` steering pointer (14 of them)
   resolves to an existing file. Requirement 3.3 is provisionally satisfied pending Pass B's
   topic-fidelity adjudication.

3. **Referenced_Notes are `fileMatch`-gated, not always-loaded.** Recorded above; affects where
   primacy statements are placed in Pass D (Core_Notes only).

## 4. Reusable reference graph (for Pass B / Pass E re-walk)

```
product-vision      → design-principles
deck-structure      → physical-handling, design-principles, simulation-standards
design-principles   → physical-handling, deck-structure, playtesting, simulation-standards
physical-handling   → design-principles
playtesting         → product-vision, design-principles   [+ simulation-standards conceptually]
repository-structure→ playtesting
simulation-standards→ playtesting        (Referenced_Note)
rulebook-standards  → physical-handling  (Referenced_Note)
```

Every directed edge above terminates at a file present in `.kiro/steering/`.
