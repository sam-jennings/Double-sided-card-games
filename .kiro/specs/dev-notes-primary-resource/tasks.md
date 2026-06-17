# Implementation Plan: Steering Notes as Primary Reference

## Overview

This is an **edit-in-place Markdown deliverable** for a tabletop game design project — not software. There is no build, test runner, or code. "Implementation" means writing and fixing the steering notes; every task's acceptance is **observable by reading the resulting notes**. All work stays inside `.kiro/steering/` (the single source of truth); Parallel_Copies under `flip-card-game-kiro/` (e.g. `docs/design-principles.md`, `AGENTS.md`) are never edited or treated as authoritative.

The plan follows the design's five-pass pipeline:
- **Pass A** — Inventory & cross-reference map
- **Pass B** — Reference integrity (Req 3, 4)
- **Pass C** — Completeness & consistency audit (Req 2)
- **Pass D** — Primacy embedding (Req 5, 6)
- **Pass E** — Reconciliation sweep (Req 7)

`simulation-standards.md` and `rulebook-standards.md` already exist (8 files total in `.kiro/steering/`). Requirement 4 work is therefore a **verify/repair-in-place** check, never a recreation.

## Tasks

- [x] 1. Pass A — Inventory and cross-reference map
  - [x] 1.1 Inventory the steering directory and build the cross-reference map
    - Read all 8 files in `.kiro/steering/` and confirm the file set matches the design's inventory table (6 Core_Notes + `simulation-standards.md` + `rulebook-standards.md`).
    - For every "see `X.md`" pointer in the Core_Notes and Referenced_Notes, record a CrossReference tuple: citing note, cited target, target-in-dir?, attributed topic.
    - Capture the map as a working note (in the spec folder or inline working text) so Pass B and Pass E can re-walk it. Distinguish steering→steering pointers from steering→top-level-doc pointers.
    - Operate only within `.kiro/steering/`; do not edit any file in this task.
    - _Requirements: 3.1_

- [x] 2. Pass B — Cross-reference integrity and Referenced_Note fidelity
  - [x] 2.1 Verify and repair every steering cross-reference resolves
    - For each steering-target CrossReference from Pass A, confirm the target file exists in `.kiro/steering/`; if any is missing, resolve it so the pointer leads to a real target in the directory.
    - Confirm topic fidelity: each named target actually covers the topic the citing note attributes to it; repair a resolves-to-wrong-content reference in place.
    - Confirm no Core_Note points the reader at a Parallel_Copy as authority; redirect any such pointer to the Steering_Directory note (or a legitimate top-level project doc).
    - Verifiable by reading: every pointer in the notes leads to an existing, on-topic steering target.
    - _Requirements: 3.2, 3.3, 3.4, 1.3_

  - [x] 2.2 Verify and repair simulation-standards.md against its citers
    - Confirm `simulation-standards.md` is present (it is) and covers the sim/analysis topics and the skill-gap standard that `design-principles.md` and `playtesting.md` attribute to it.
    - Confirm its guidance agrees with the binding constraints in `design-principles.md` (the ~1.5× thin-skill-gap warning, the OUROBOROS lesson) and the sim-versus-table stance in `playtesting.md`.
    - Confirm the references to it in `design-principles.md` and `playtesting.md` resolve to this file. Repair the file in place only where a gap is found — never recreate it.
    - _Requirements: 4.1, 4.2, 4.3, 4.4_

  - [x] 2.3 Verify and repair rulebook-standards.md against its citer
    - Confirm `rulebook-standards.md` is present and faithfully covers the no-back deck constraint that `physical-handling.md` relies on.
    - Repair in place only if the fidelity check finds a gap; do not recreate the file.
    - _Requirements: 3.3, 3.4_

- [x] 3. Checkpoint — reference integrity confirmed
  - Confirm every cross-reference resolves and both Referenced_Notes are topic-faithful before starting the content audit. Ask the user if questions arise.

- [x] 4. Pass C — Completeness and consistency audit
  - [x] 4.1 Per-note completeness audit and gap-fill
    - Walk each of the 6 Core_Notes; confirm each fully covers its stated remit with no silent hole another note assumes it fills.
    - Fill any identified gap with content consistent with the rest of the Steering_Notes; preserve each note's established meaning and binding constraints (change only what the audit flags).
    - _Requirements: 2.1, 2.3, 2.4_

  - [x] 4.2 Cross-note contradiction scan and resolution
    - Check the overlap seams from the design's contradiction table: maturity tiers (product-vision ↔ playtesting), the bug list (design-principles ↔ physical-handling ↔ playtesting), deck properties (deck-structure ↔ design-principles), the skill-gap standard (design-principles ↔ simulation-standards), and the sim-vs-table division (playtesting ↔ simulation-standards).
    - Resolve any contradiction so the affected notes state consistent guidance, preserving binding constraints.
    - _Requirements: 2.2, 2.4_

  - [x] 4.3 Terminology normalisation across notes
    - Normalise shared-concept terms (tiers, bugs, the deck's properties, the software→tabletop vocabulary mapping) to one consistent term per concept, preferring the owning note's term, without changing meaning.
    - _Requirements: 2.5_

- [x] 5. Pass D — Primacy statement embedding
  - [x] 5.1 Embed the uniform Primacy_Statement in each of the six Core_Notes
    - Add the design's Primacy_Statement blockquote immediately after the H1 title of each Core_Note (`product-vision.md`, `deck-structure.md`, `design-principles.md`, `physical-handling.md`, `playtesting.md`, `repository-structure.md`).
    - The statement must state the notes are binding, instruct the reader to defer to them as the primary reference, and instruct the reader to cite the relevant steering note. Use identical claim and wording intent and identical placement in all six.
    - Verifiable by reading: each Core_Note opens with the same prominent primacy blockquote.
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

  - [x] 5.2 Confirm the mechanism is embedded-only
    - Confirm the primacy mechanism is realised solely as blockquotes inside the six existing auto-loaded Core_Notes: no new top-level guide document is created and no automated hook is introduced.
    - _Requirements: 6.1, 6.2, 6.3, 6.4_

- [x] 6. Pass E — Reconciliation sweep
  - [x] 6.1 Propagate edits to dependent notes
    - For every edit made in Passes B–D, re-read the notes that depend on the changed guidance (using the contradiction-seam table as the dependency map) and update them so both sides agree.
    - _Requirements: 7.1, 7.2_

  - [x] 6.2 Final integrity and primacy-uniformity confirmation
    - Re-walk the cross-reference map and contradiction seams; confirm no identified contradiction and no broken steering reference remains.
    - Compare the six embedded Primacy_Statements; confirm identical claim, wording intent, and placement.
    - _Requirements: 7.1, 7.3_

- [x] 6.3 Reviewer verification against the correctness properties
    - Confirm Property 1 (edits confined to `.kiro/steering/`, no Parallel_Copy changed, no inward-pointing reference broken).
    - Confirm Property 2 (every cross-reference resolves and is topic-faithful) and Property 3 (`simulation-standards.md` present and faithful).
    - Confirm Property 4 (shared concepts consistent, binding constraints preserved), Property 5 and Property 6 (primacy statements present, complete, uniform, prominent), Property 7 (mechanism embedded-only), and Property 8 (final note set internally coherent).
    - _Requirements: 1.1, 1.2, 2.1, 2.2, 2.3, 2.4, 2.5, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3_

- [x] 7. Final checkpoint — steering set correct and authoritative
  - Confirm the audit and repairs are complete, all cross-references resolve, both Referenced_Notes are faithful, and all six Core_Notes carry the uniform primacy statement. Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional review sweeps and can be skipped for a faster pass.
- This is a documentation deliverable: every acceptance criterion is verified by **reading** the resulting steering notes, not by running code.
- Property-based testing is **not applicable** — there is no function with generated inputs — so there are no PBT tasks.
- All edits stay within `.kiro/steering/`; Parallel_Copies under `flip-card-game-kiro/` are never edited.
- `simulation-standards.md` and `rulebook-standards.md` already exist; Requirement 4 is a verify/repair-in-place check, never a recreation.
- Checkpoints ensure integrity is settled before content edits, and content before primacy text.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1", "2.2", "2.3"] },
    { "id": 2, "tasks": ["4.1", "4.2", "4.3"] },
    { "id": 3, "tasks": ["5.1", "5.2"] },
    { "id": 4, "tasks": ["6.1", "6.2"] },
    { "id": 5, "tasks": ["6.3"] }
  ]
}
```
