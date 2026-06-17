# Implementation Plan: Collection Audit

## Overview

This plan builds the `COLLECTION_AUDIT.md` deliverable section by section, following the §0–§6 document structure in the design. Each task is a concrete analysis/writing step: read the relevant source documents, score or analyse, and write the corresponding audit section. Tasks build on one another — scorecards feed the summary matrix; scorecards, gaps, overlaps, and the OUROBOROS verdict all feed the roadmap; surfaced changes feed the Overview sync. The final task is a review sweep against the design's correctness-property checklist.

This is a documentation deliverable for a tabletop game design project. "Acceptance" is observable document content a reviewer can read and confirm — not test execution. There are no code-build or test-run tasks.

Sources read throughout: `COLLECTION_OVERVIEW.md` (canonical index, coverage tables, tiers, recorded questions), per-game `<GAME>_rulebook.md` and `<GAME>_design_analysis.md`, `NEW_GAME_CONCEPTS.md`, the OUROBOROS post-mortem, and the steering files (`design-principles.md`, `physical-handling.md`, `product-vision.md`, `deck-structure.md`).

## Tasks

- [x] 1. Scaffold `COLLECTION_AUDIT.md` (§0 introduction + §1 methodology note)
  - Create `COLLECTION_AUDIT.md` at the repository top level with the §0–§6 section skeleton from the design's document-structure table.
  - Write §0 Introduction & canonical-index note: state that `COLLECTION_OVERVIEW.md` remains the canonical index, that this is a design-facing analysis (not a rulebook), the scope (10 live games + OUROBOROS), the date, and the cross-reference-not-duplicate policy.
  - Write §1 Methodology note: define the seven rubric dimensions (D1 deck-necessity, D2 physical-handling viability, D3 flipping load-bearing, D4 pair-uniqueness load-bearing, D5 distinctness, D6 gap-filling, D7 teachability) and reproduce the 1–10 scale anchors (9–10 load-bearing, 6–8 solid, 4–5 mixed, 1–3 weak); name the source docs feeding the audit and link out to the steering rubric rather than restating it.
  - _Requirements: 1.1, 1.3, 1.4, 2.2_

- [x] 2. Write per-game rubric scorecards (§2)
  - [x] 2.1 Score the Tier 1 games — SYZYGY, TURNCOAT
    - For each game, read its `_rulebook.md` and `_design_analysis.md`; produce a scorecard block (per the design template) with integer 1–10 scores on all seven dimensions, each justification citing a specific deck property, handling technique, or coverage fact; any score ≤5 names the specific weakness.
    - Record tier in the header, reproduce first-table questions faithfully from Overview/concepts (or "none recorded"), and write the recommendation as "leave alone — benchmark"; if any re-tune/re-skin is proposed, attach explicit evidence and a "requires owner sign-off" note.
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.3_

  - [x] 2.2 Score the Tier 2 games — TWELVE TRIALS, TURNOVER, CROSSROADS
    - Produce a full seven-dimension scorecard for each, scored from the rulebook and `_design_analysis.md`, with cited justifications and specific weaknesses for any score ≤5.
    - Record tier and faithfully reproduced first-table questions; frame each recommendation as a first table test (prioritised over further simulation/new design) built around the game's own recorded questions, with tier stated.
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.2, 4.3_

  - [x] 2.3 Score the Tier 3 games (group A) — JANUS, FALSE FACE, THE UNPLAYED PAIR
    - Produce a full seven-dimension scorecard for each, scored from the rulebook (and `_design_analysis.md` where one exists); for games with only a rulebook, mark D2 explicitly "un-simmed; handling unverified at the table" rather than guessing.
    - Record tier and faithfully reproduced first-table questions; frame each recommendation as a first table test around the game's recorded questions, with tier stated.
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.2, 4.3_

  - [x] 2.4 Score the Tier 3 games (group B) — FACE VALUE, THE COUNCIL
    - Produce a full seven-dimension scorecard for each, scored from the rulebook (and `_design_analysis.md` where one exists), with cited justifications and specific weaknesses for any score ≤5; mark D2 "un-simmed" where evidence is thin.
    - Record tier and faithfully reproduced first-table questions; frame each recommendation as a first table test around the game's recorded questions, with tier stated.
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.2, 4.3_

  - [x] 2.5 Build the cross-game summary matrix
    - After the individual scorecards, add the single matrix (Game · Tier · D1–D7) covering all ten live games, with values matching each scorecard so reading down a column ranks games on one dimension and across a row profiles one game.
    - _Requirements: 2.5_

- [x] 3. Checkpoint — review §2 before collection-level analysis
  - Confirm all ten live games have a complete seven-dimension scorecard, integer 1–10 scores, cited justifications, faithfully reproduced (never fabricated) first-table questions, and tier-respecting recommendations, and that the summary matrix agrees with the scorecards. Ask the owner if questions arise.

- [x] 4. Write the collection gaps & overlaps analysis (§3)
  - [x] 4.1 Write the gap analysis
    - Analyse all four coverage dimensions — player count, play time, complexity, mood/genre — against the `COLLECTION_OVERVIEW.md` coverage tables; for each, name the explicit missing band (the specific player count, time band, weight, or mood) and reference the source coverage table.
    - For any dimension with no meaningful gap, state explicitly that it is adequately covered rather than omitting it; report all four dimensions.
    - _Requirements: 5.1, 5.2, 5.3, 5.4_

  - [x] 4.2 Write the overlap analysis
    - Run a shared-niche scan across the coverage axes plus the "deck-property used" axis; cluster candidate overlaps (e.g. SYZYGY ↔ TURNCOAT, FALSE FACE ↔ FACE VALUE, FALSE FACE ↔ THE COUNCIL).
    - For each detected overlap, name the games and the shared niche dimension, reference the relevant Overview coverage table, and adjudicate — coexist, or one is a candidate to differentiate/park/cut — applying the distinctness criterion. Report near-overlaps that resolve, with their coexist verdict.
    - _Requirements: 6.1, 6.2, 6.3, 6.4_

- [x] 5. Write the OUROBOROS revival re-evaluation (§4)
  - Read `OUROBOROS_design_analysis.md` and the Overview/concepts cut notes; structure the section as a confrontation in four steps.
  - Confront each recorded cut reason in its own subsection: luck-driven play / thin skill gap (cite the random-vs-skilled numbers and the ~1.5× healthy bar) and the hidden open symbol under the serpent's head (constantly-needed state on a down-face).
  - Assess the vacated solo niche (TWELVE TRIALS is now the lone 1P game) and whether any OUROBOROS mechanic is worth carrying forward; apply the binding handling constraints as a gate (any revived mechanic must use visible state, no hidden-face memory) and reject anything that fails the gate.
  - State exactly one verdict — revive, keep cut, or revive only under stated conditions — tied explicitly back to the three cut reasons it resolves or fails to resolve.
  - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5_

- [x] 6. Build the ranked priority roadmap (§5)
  - Harvest candidate actions from every finding in §2–§4 (each scorecard recommendation, each actionable gap, each overlap verdict warranting action, the OUROBOROS verdict).
  - Present them as a single ranked ordering using the project's centre of gravity (table testing outranks further simulation/new design), weighted by collection impact and tier; write each item as a concrete action and attach a back-reference to the specific finding it traces to (e.g. "see §2 THE UNPLAYED PAIR scorecard / §3 mood gap").
  - _Requirements: 8.1, 8.2, 8.3, 8.4_

- [x] 7. Sync `COLLECTION_OVERVIEW.md` and write the §6 sync log
  - For each game the audit surfaced a status or priority change for, update the matching entry in `COLLECTION_OVERVIEW.md`; if a game's maturity tier changed, relocate its entry to the correct tier section. Leave entries for games with no surfaced change untouched, and record only status/priority lines (not the full scorecards/analysis), linking to the audit instead.
  - Write the §6 sync log in `COLLECTION_AUDIT.md`: record which Overview entries were changed and which were deliberately left unchanged, so the write-back is auditable.
  - _Requirements: 9.1, 9.2, 9.3, 9.4_

- [x] 8. Final review sweep against the correctness-property checklist
  - Walk the design's review checklist over the finished `COLLECTION_AUDIT.md` and synced `COLLECTION_OVERVIEW.md`, fixing any failures in place:
    - Completeness: each of the ten games has a full seven-dimension scorecard, a tier, and faithful first-table questions (Properties 1, 5, 6).
    - Scale & justification: every score is an integer 1–10 with a concrete cited justification; every score ≤5 names a specific weakness (Properties 2, 3, 4).
    - Recommendation: every recommendation states tier and honours tier discipline (Property 7).
    - Gaps & overlaps: each references a coverage table and is specific/adjudicated (Properties 8, 9).
    - OUROBOROS: all three cut reasons confronted; any revived mechanic passes the handling gate (Property 10).
    - Roadmap: every item is ranked, concrete, and traceable to a finding (Property 11).
    - Sync: surfaced changes reflected in the Overview, unchanged games untouched (Property 12).
    - Cross-reference: restated status/maths/coverage links out rather than duplicating (Property 13).
  - _Requirements: 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 5.2, 5.3, 6.2, 6.3, 6.4, 7.2, 7.5, 8.2, 8.3, 8.4, 9.1, 9.2, 9.4_

## Notes

- This is a documentation/analysis deliverable; tasks are reading, scoring, and writing steps, and acceptance is observable document content rather than test execution.
- No property-based or unit-test tasks are included — the design states PBT is not applicable (there is no code with generated inputs); the correctness properties are verified by the review sweep in task 8.
- Each task references the specific requirements it satisfies for traceability.
- Checkpoint (task 3) ensures the per-game scorecards are sound before collection-level analysis builds on them.
- The roadmap (task 6) is built last so every item traces back to a finding written in §2–§4.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1"] },
    { "id": 2, "tasks": ["2.2"] },
    { "id": 3, "tasks": ["2.3"] },
    { "id": 4, "tasks": ["2.4"] },
    { "id": 5, "tasks": ["2.5"] },
    { "id": 6, "tasks": ["4.1"] },
    { "id": 7, "tasks": ["4.2"] },
    { "id": 8, "tasks": ["5"] },
    { "id": 9, "tasks": ["6"] },
    { "id": 10, "tasks": ["7"] },
    { "id": 11, "tasks": ["8"] }
  ]
}
```
