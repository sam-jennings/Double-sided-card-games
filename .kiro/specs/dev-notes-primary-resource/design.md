# Design Document — Steering Notes as Primary Reference

## Overview

This design describes **how to make the steering files under `.kiro/steering/` correct and durably authoritative** — the audit method, the cross-reference integrity model, the primacy-statement template and placement, and the consistency-reconciliation pass that closes the work. It is a methodology design for a Markdown documentation deliverable, not a software architecture. There is no code, no build, and no test runner. Following the framing of `.kiro/specs/collection-audit/design.md`, the "system" here is the set of steering notes; "architecture" means document structure and information flow (per the vocabulary mapping in `design-principles.md`, where *implementation* = writing/fixing Markdown, *acceptance criteria* = readable content, and a *bug* = an inconsistency, gap, or broken cross-reference).

Unlike collection-audit (which creates a new top-level document), this work is an **edit-in-place** deliverable. It changes the steering files themselves and creates no new documents. Two firm boundaries shape every decision below:

- **`.kiro/steering/` is the single source of truth.** All edits land inside the Steering_Directory. Parallel copies elsewhere in the workspace (for example under `flip-card-game-kiro/`, such as `docs/design-principles.md` or `AGENTS.md`) are out of scope: they are neither edited nor treated as authoritative (Requirements 1.1–1.3).
- **Repair, do not rewrite.** The audit changes only what it identifies as off. The established meaning and binding constraints of each note — the OUROBOROS lessons, the physical facts of the no-back deck, the K₉ maths, the tier semantics, the vocabulary mapping — are preserved (Requirement 2.4).

### Correcting the stale clarify-phase assumption

The clarify phase assumed `simulation-standards.md` did **not** exist and that `.kiro/steering/` held six files. A direct inventory taken for this design shows that assumption is **stale**. The directory currently holds **eight** files:

| # | File | Role |
|---|---|---|
| 1 | `product-vision.md` | Core_Note |
| 2 | `deck-structure.md` | Core_Note |
| 3 | `design-principles.md` | Core_Note |
| 4 | `physical-handling.md` | Core_Note |
| 5 | `playtesting.md` | Core_Note |
| 6 | `repository-structure.md` | Core_Note |
| 7 | `simulation-standards.md` | Referenced_Note (cited by #3, #2) |
| 8 | `rulebook-standards.md` | Referenced_Note (cited by #4 via the no-back rule) |

Consequence for Requirement 4: it is **not** a recreation task. `simulation-standards.md` already exists and is substantial. Requirement 4 is therefore a **consistency/completeness check** of an existing file — verify it is complete and faithful to how `design-principles.md` and `playtesting.md` describe and rely on it, and repair only if the check finds gaps. The same posture applies to `rulebook-standards.md`.

## Architecture

*Architecture here means the structure of the work and how information flows through it — not software architecture.*

The work is a four-pass pipeline over the eight steering files. Each pass reads the current note set and produces edits (or confirms none are needed):

```
.kiro/steering/ (8 files) ─┐
                           ├─► Pass A: Inventory & cross-reference map
                           │     (enumerate files; map every "see X.md" pointer to a target)
                           │
                           ├─► Pass B: Cross-reference integrity check  (Req 3, 4)
                           │     (confirm each steering-target resolves; verify simulation-standards.md
                           │      and rulebook-standards.md are present and topic-faithful)
                           │
                           ├─► Pass C: Completeness & consistency audit  (Req 2)
                           │     (per-note gaps; cross-note contradictions; shared-term consistency)
                           │
                           ├─► Pass D: Primacy-statement embedding  (Req 5, 6)
                           │     (add the uniform Primacy_Statement to each of the six Core_Notes)
                           │
                           └─► Pass E: Reconciliation sweep  (Req 7)
                                 (re-walk dependents of every edit; final integrity confirmation)
```

The passes are ordered so that integrity (B) and content (C) are settled before the primacy text (D) is layered on, and a final reconciliation (E) guarantees no pass introduced a new conflict. The config file `.kiro/specs/dev-notes-primary-resource/.config.kiro` accompanies this spec.

### Scope boundary (Requirement 1)

| In scope (editable) | Out of scope (never edited, never authoritative) |
|---|---|
| The 8 files in `.kiro/steering/` | `flip-card-game-kiro/docs/*.md` and similar Parallel_Copies |
| | `AGENTS.md` and any mirror of a steering note |
| | Top-level project docs (`COLLECTION_OVERVIEW.md`, `NEW_GAME_CONCEPTS.md`, `DECK_SIZE_DECISION.md`, `SYMBOL_SETS.md`) — these are legitimate cross-reference *targets* but are not part of this audit's edit set |

Cross-references from a Core_Note to a legitimate top-level project doc are allowed and expected (they are the canonical index and decision records). What is forbidden is a Core_Note pointing the reader at a Parallel_Copy as the authority (Requirement 1.3).

## Components and Interfaces

*The "components" are the five passes; their "interfaces" are the files each reads and the edits it produces.*

| Pass | Reads (input) | Produces (output) | Requirements |
|---|---|---|---|
| **A — Inventory & map** | all 8 steering files | a cross-reference table: (citing note, cited target, target-exists?, attributed topic) | 3.1 |
| **B — Reference integrity** | the map from A; the target files | confirmation each steering-target resolves; repairs for any dangling pointer; faithful-coverage confirmation for `simulation-standards.md` / `rulebook-standards.md` | 3.2, 3.3, 3.4, 4.1–4.4 |
| **C — Completeness & consistency** | all 6 Core_Notes + 2 Referenced_Notes | resolved contradictions, filled gaps, normalised shared terminology | 2.1–2.5 |
| **D — Primacy embedding** | the 6 Core_Notes | one uniform Primacy_Statement added to each Core_Note | 5.1–5.5, 6.1–6.4 |
| **E — Reconciliation** | the edited note set | dependent-note updates; final no-contradiction / no-broken-reference confirmation | 7.1–7.3 |

### Cross-reference map (output of Pass A)

The inventory produced the following steering→steering reference graph. Every target below is present in the Steering_Directory, so **no dangling steering reference currently exists**; Pass B records this as a confirmation rather than a repair.

| Citing Core_Note | Steering targets it references | Attributed topic |
|---|---|---|
| `product-vision.md` | `design-principles.md` | the evaluation rubric; binding OUROBOROS lessons |
| `deck-structure.md` | `physical-handling.md`, `design-principles.md`, `simulation-standards.md` | no-asymmetric-marks rule; "generic deck" test; verify-by-computing |
| `design-principles.md` | `physical-handling.md`, `deck-structure.md`, `simulation-standards.md`, `playtesting.md` | physical constraint; maths; sim/skill-gap standard; testing stance |
| `physical-handling.md` | `design-principles.md` | the bug list / handling-bug flag |
| `playtesting.md` | `product-vision.md`, `design-principles.md`, `simulation-standards.md` (via stance) | tiers; bug categories; sim-vs-table division |
| `repository-structure.md` | `playtesting.md` | where playtest plans/reports live |
| `rulebook-standards.md` (Ref) | `physical-handling.md` | the no-back deck constraint |

References to top-level project docs (`COLLECTION_OVERVIEW.md`, `NEW_GAME_CONCEPTS.md`, `DECK_SIZE_DECISION.md`, `SYMBOL_SETS.md`) are catalogued but treated as out-of-audit targets whose existence is confirmed, not edited.

## Data Models

*The "data models" are the structured artefacts the passes instantiate: the cross-reference record and the Primacy_Statement template.*

### Cross-reference record

Each pointer found in Pass A is captured as a tuple so Pass B can adjudicate it uniformly:

```
CrossReference {
  citing_note     : steering file containing the pointer
  cited_target    : the file the pointer names (e.g. "simulation-standards.md")
  target_in_dir   : boolean — does cited_target exist in .kiro/steering/ ?
  attributed_topic: the subject the citing note says the target covers
  topic_satisfied : boolean — does the target actually cover attributed_topic ?
}
```

A reference is **healthy** iff `target_in_dir ∧ topic_satisfied` (for steering targets). Pass B repairs any reference where either is false.

### Primacy_Statement template (Requirement 5)

A single, reusable block, embedded as a **blockquote immediately after the H1 title** of each Core_Note — a consistent, prominent, locatable position (Requirement 5.5). The wording is identical across all six notes except where a note may name itself; the claim and intent are uniform (Requirements 5.1–5.4, 7.3):

```markdown
# <Existing Note Title>

> **Primacy.** This note is part of the project's binding steering set in
> `.kiro/steering/`. Treat these notes as the **primary reference** for all
> design decisions and defer to them over any other document. When you apply
> guidance from here, **cite the specific steering note** you are relying on.
```

The template satisfies each sub-requirement:

| Element of the block | Requirement |
|---|---|
| "binding steering set" | 5.2 — states the notes are binding |
| "primary reference ... defer to them over any other document" | 5.3 — instructs deference as primary reference |
| "cite the specific steering note" | 5.4 — instructs citation |
| blockquote directly under the H1, same in every note | 5.5, 7.3 — consistent, prominent, locatable |
| lives inside the existing six Core_Notes | 5.1, 6.1, 6.4 |

### Mechanism constraints (Requirement 6)

The mechanism is **only** the embedded blockquotes:

- **No separate top-level guide** is created to carry primacy (Requirement 6.2). A new "primacy guide" doc would itself need to be loaded and cited, defeating the purpose.
- **No automated hook** is created (Requirement 6.3). A hook is session-fragile and is explicitly excluded.
- The statements live in the **auto-loaded steering files** (Requirement 6.4): because `.kiro/steering/` files are loaded into every session, embedding the statement there makes the guidance apply without the reader taking any extra action. This is precisely why embedding beats a standalone guide.

## Methodology: completeness & consistency audit (Requirement 2)

Pass C walks all eight files and records findings against checkable invariants. It changes only what it flags (Requirement 2.4).

**Per-note completeness (Requirement 2.3).** For each Core_Note, confirm it fully covers its stated remit and has no silent hole that another note assumes it fills. Any gap is filled with content consistent with the rest of the set.

**Cross-note contradiction scan (Requirement 2.2).** Check the seams where notes overlap and must agree:

| Shared concept | Notes that must agree | What to confirm |
|---|---|---|
| Maturity **tiers** (1–4) and which game sits where | `product-vision.md`, `playtesting.md` | same tier labels; same tier→priority mapping (table-testing centre of gravity) |
| The **bug list** (handling, kingmaking, non-termination, thin skill gap, …) | `design-principles.md`, `physical-handling.md`, `playtesting.md` | same categories; `playtesting.md` cites the canonical list in `design-principles.md` |
| **Deck properties** (K₉, every pair once, degree 8, subset property, almanac) | `deck-structure.md`, `design-principles.md` | numbers and claims identical; no divergent restatement |
| **Vocabulary mapping** (software→tabletop) | `design-principles.md` (owner) | other notes use the mapped terms consistently |
| **Skill-gap standard** (~1.5× healthy; thin gap is a red flag) | `design-principles.md`, `simulation-standards.md` | same threshold and same OUROBOROS-derived rationale |
| **Sim-vs-table division** | `playtesting.md`, `simulation-standards.md` | both state sim certifies the floor; the table decides fun |

**Terminology normalisation (Requirement 2.5).** Where the same concept is named differently across notes, normalise to one term (preferring the term the owning note uses) without changing meaning.

**Preservation guard (Requirement 2.4).** The binding constraints — the seven OUROBOROS/SYZYGY lessons, the five hard physical facts, the K₉ tables and almanac, the tier definitions — are treated as fixed. An edit may reword for consistency but must not weaken or alter any of them.

## Methodology: cross-reference integrity (Requirement 3)

Pass B adjudicates every record from the Pass A map:

1. **Existence (Requirement 3.3).** For each steering-target reference, confirm the target file is present in `.kiro/steering/`. The current map shows all steering targets resolve, so this records a confirmation; if any were missing, the resolution would be to create or correct the target so the pointer leads somewhere real (Requirement 3.2).
2. **Topic fidelity (Requirement 3.4).** For each named reference, confirm the target actually covers the topic the citing note attributes to it — e.g. `design-principles.md` sends the reader to `simulation-standards.md` for the skill-gap standard, so `simulation-standards.md` must actually state that standard. A reference that resolves to the wrong-content file is treated as broken and repaired.
3. **No Parallel_Copy targets (Requirement 1.3).** Confirm no Core_Note points the reader at a Parallel_Copy as authority.

## Methodology: simulation-standards verification (Requirement 4)

Because the file already exists, Pass B treats Requirement 4 as a faithfulness check, repairing only on a found gap:

- **4.1 Presence** — confirmed: `simulation-standards.md` is in the directory.
- **4.2 Attributed coverage** — confirm it covers what its citers rely on: how simulations/solvers are built and run (bots, volume, termination guard, parameter sweeps, solver baselines) and the **skill-gap standard** (`design-principles.md` cites it for "verify by computing" and the thin-gap warning; `playtesting.md` leans on the sim-certifies-the-floor stance).
- **4.3 Consistency** — confirm its guidance agrees with the binding constraints in `design-principles.md` (the ~1.5× skill-gap red flag, the OUROBOROS lesson) and the simulation-versus-table stance in `playtesting.md` (a game can be sim-validated and still owe a first table test).
- **4.4 Resolving citations** — confirm the references to it in `design-principles.md` and `playtesting.md` resolve to this file.

If any sub-check fails, the repair edits `simulation-standards.md` to close the gap rather than creating a new file. The same verification is applied to `rulebook-standards.md` against the note that relies on it (`physical-handling.md`'s no-back rule).

## Methodology: reconciliation sweep (Requirement 7)

Pass E is the closing guarantee that the edits leave the whole set coherent:

- **Dependent propagation (Requirement 7.2).** For every edit made in Passes B–D, re-read the notes that depend on the changed guidance (using the contradiction-seam table above as the dependency map) and update them so both sides agree.
- **Final integrity (Requirement 7.1).** Re-walk the cross-reference map and the contradiction seams; confirm no identified contradiction and no broken steering reference remains.
- **Primacy uniformity (Requirement 7.3).** Compare the six embedded Primacy_Statements; confirm identical claim and wording intent and identical placement.

## Error Handling

*With no executing code, "errors" are integrity failures in the deliverable.* The method guards against:

- **Editing the wrong copy** — every edit is path-checked to be under `.kiro/steering/`; a Parallel_Copy edit is reverted (Requirement 1.1, 1.2).
- **Silent recreation** — `simulation-standards.md` is verified and repaired in place, never blindly recreated, so existing content is not lost (Requirement 4).
- **Constraint drift** — a reword that would weaken a binding constraint is rejected; the audit changes wording, not the constraint's substance (Requirement 2.4).
- **Primacy divergence** — any Primacy_Statement that drifts in wording or position from the template is normalised (Requirements 5.5, 7.3).
- **New mechanism creep** — proposals to add a standalone primacy guide or a hook are rejected by the mechanism constraint (Requirements 6.2, 6.3).
- **Cascade conflict** — an edit that fixes one note but breaks a dependent is caught by the reconciliation sweep (Requirement 7.2).

## Testing Strategy

This is a documentation deliverable, so "testing" is **review against checkable content invariants**, not executing code. Property-based testing is **not applicable**: there is no function with generated inputs, so there are no PBT tasks. A Reviewer verifies the edited steering set against the correctness properties below — each is a universal statement over the notes' content that can be confirmed by reading.

Review checklist, mapped to the properties:

- **Scope sweep** — confirm every edit is inside `.kiro/steering/`, no Parallel_Copy changed, and no Core_Note cites a Parallel_Copy as authority (Property 1).
- **Reference sweep** — walk every cross-reference; confirm each steering target exists and covers its attributed topic (Property 2).
- **Simulation-standards sweep** — confirm the file is present, covers the attributed sim/skill-gap topics, and agrees with its citers (Property 3).
- **Consistency sweep** — confirm shared concepts (tiers, bugs, deck maths, vocabulary, skill-gap, sim-vs-table) read consistently and binding constraints are intact (Property 4).
- **Primacy presence sweep** — confirm all six Core_Notes carry a Primacy_Statement asserting bindingness, deference, and citation (Property 5).
- **Primacy uniformity sweep** — confirm the six statements share claim, wording intent, and a consistent prominent position (Property 6).
- **Mechanism sweep** — confirm the mechanism is embedded-only: in auto-loaded steering files, with no new guide and no hook (Property 7).
- **Final-state sweep** — confirm no identified contradiction or broken reference remains after all edits (Property 8).

## Correctness Properties

*A property is a characteristic that should hold true across all valid instances. For this documentation deliverable, properties are universal statements about the content of the edited steering notes that a Reviewer can verify by reading.*

### Property 1: Edits stay confined to the steering directory and point inward

*For every* edit made by this work, the edited file lies within `.kiro/steering/`; *for every* Parallel_Copy, the file is unchanged; and *for every* guidance reference in a Core_Note, the target is a Steering_Directory note or a legitimate top-level project doc, never a Parallel_Copy.

**Validates: Requirements 1.1, 1.2, 1.3**

### Property 2: Every cross-reference resolves and is topic-faithful

*For every* Cross_Reference in the Steering_Notes whose target is a steering file, the target file exists in `.kiro/steering/` and its content covers the topic the citing note attributes to it.

**Validates: Requirements 3.1, 3.2, 3.3, 3.4**

### Property 3: simulation-standards.md is present and faithful to its citers

The Steering_Directory contains `simulation-standards.md`; it covers the simulation/analysis topics and the skill-gap standard that `design-principles.md` and `playtesting.md` attribute to it; its guidance is consistent with the binding constraints in `design-principles.md` and the sim-versus-table stance in `playtesting.md`; and *for every* reference to it in those two notes, the reference resolves to this file.

**Validates: Requirements 4.1, 4.2, 4.3, 4.4**

### Property 4: Shared concepts are consistent and binding constraints are preserved

*For every* concept shared across Core_Notes (maturity tiers, the bug list, deck properties, the vocabulary mapping, the skill-gap standard, the sim-versus-table division), the notes that use it state mutually consistent guidance and consistent terminology; and *for every* binding constraint identified before the audit (the OUROBOROS/SYZYGY lessons, the hard physical facts, the K₉ maths), its substance is preserved after editing.

**Validates: Requirements 2.1, 2.2, 2.3, 2.4, 2.5**

### Property 5: Every core note carries a complete primacy statement

*For every* one of the six Core_Notes, the note contains a Primacy_Statement that states the Steering_Notes are binding, instructs the reader to defer to them as the primary reference, and instructs the reader to cite the relevant note.

**Validates: Requirements 5.1, 5.2, 5.3, 5.4**

### Property 6: Primacy statements are uniform and prominently placed

*For every* pair of the six Primacy_Statements, the two are consistent in claim and wording intent and appear in the same consistent, prominent, locatable position within their note.

**Validates: Requirements 5.5, 7.3**

### Property 7: The primacy mechanism is embedded-only

*For every* part of the primacy mechanism, it is realised as a Primacy_Statement embedded in one of the six existing auto-loaded Core_Notes; no separate top-level guide document and no automated hook is introduced as the mechanism.

**Validates: Requirements 6.1, 6.2, 6.3, 6.4**

### Property 8: The completed note set is internally coherent

*For every* contradiction and broken Cross_Reference the audit identified, the completed Steering_Notes are free of it; and *for every* edit that changes guidance another note depends on, the dependent note is updated so both state consistent guidance.

**Validates: Requirements 7.1, 7.2**
