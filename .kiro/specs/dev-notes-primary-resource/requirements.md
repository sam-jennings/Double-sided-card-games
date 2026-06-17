# Requirements Document

## Introduction

This feature makes the **Game Development Notes** — the steering files in `.kiro/steering/` — both correct and durably authoritative for all design work on the flip-deck collection. It has two halves:

1. **Audit and repair.** Review the notes for completeness, internal consistency, and broken cross-references, then fix what is off. This includes ensuring the `simulation-standards.md` document referenced by `design-principles.md` and `playtesting.md` exists and matches how those notes describe and use it, and resolving any other dangling cross-references.
2. **Lock in primacy.** Add a short, explicit primacy statement into the steering files themselves stating that the notes are binding and that design work must defer to and cite them. Because steering files are auto-loaded into every session, embedding the statement in the notes (rather than a separate top-level guide or an automated hook) is what makes them the standing primary reference.

This is a **tabletop game design project, not a software product**. Per the vocabulary mapping in `design-principles.md`: *implementation* here means writing and fixing Markdown notes; *acceptance criteria* are observable, readable content in those notes; a *bug* is an inconsistency, gap, or broken cross-reference. Every acceptance criterion below is written so that a reviewer can open the steering files and verify it by reading.

**Scope clarification.** "Game Development Notes" in this spec means the steering files under `.kiro/steering/`, **not** the top-level `Game Development Notes/` lesson folder. The six core notes named in scope are `product-vision.md`, `deck-structure.md`, `design-principles.md`, `physical-handling.md`, `playtesting.md`, and `repository-structure.md`. `.kiro/steering/` is the single source of truth; parallel copies elsewhere in the workspace (for example under `flip-card-game-kiro/`, such as `docs/design-principles.md` or `AGENTS.md`) are explicitly out of scope and are not to be edited or treated as authoritative.

## Glossary

- **Steering_Directory**: The folder `.kiro/steering/`, the single source of truth for the project's design notes.
- **Core_Notes**: The six steering files in scope — `product-vision.md`, `deck-structure.md`, `design-principles.md`, `physical-handling.md`, `playtesting.md`, `repository-structure.md`.
- **Referenced_Note**: Any steering file that a Core_Note cross-references and that must exist in the Steering_Directory for the reference to resolve — including `simulation-standards.md` and `rulebook-standards.md`.
- **Steering_Notes**: The Core_Notes together with their Referenced_Notes inside the Steering_Directory.
- **Cross_Reference**: A mention in one steering file that points the reader to another steering file (for example "see `simulation-standards.md`").
- **Primacy_Statement**: A short, explicit passage embedded in a steering file declaring that the Steering_Notes are binding and that design work must defer to and cite them.
- **Parallel_Copy**: A document outside the Steering_Directory that duplicates or resembles a steering note (for example files under `flip-card-game-kiro/` like `docs/design-principles.md` or `AGENTS.md`).
- **Author**: The designer or agent performing the audit and edits.
- **Reviewer**: A person who reads the resulting Steering_Notes to verify the criteria are met.

## Requirements

### Requirement 1: Single source of truth confined to the steering directory

**User Story:** As the collection owner, I want all authoritative design notes confined to `.kiro/steering/`, so that there is exactly one place to read and trust the project's guidance.

#### Acceptance Criteria

1. THE Author SHALL make all audit and repair edits within the Steering_Directory.
2. THE Author SHALL leave every Parallel_Copy unchanged.
3. WHERE a Core_Note refers to project guidance, THE Core_Note SHALL point the Reviewer to documents within the Steering_Directory rather than to any Parallel_Copy.

### Requirement 2: Completeness and consistency audit recorded

**User Story:** As a designer, I want the notes audited for gaps and contradictions, so that I can rely on them without hitting silent holes or conflicting guidance.

#### Acceptance Criteria

1. THE Author SHALL review each Core_Note for completeness gaps, internal inconsistencies, and contradictions with the other Core_Notes.
2. WHEN the audit finds a contradiction between two Steering_Notes, THE Author SHALL resolve the contradiction so that the affected notes state consistent guidance.
3. WHEN the audit finds a content gap in a Core_Note, THE Author SHALL fill the gap with content consistent with the rest of the Steering_Notes.
4. THE Author SHALL preserve the established meaning and binding constraints of each Core_Note when repairing it, changing only what the audit identifies as off.
5. THE Steering_Notes SHALL use terminology for shared concepts (tiers, bugs, the deck's properties, vocabulary mapping) consistently across all Core_Notes.

### Requirement 3: Every cross-reference resolves

**User Story:** As a reader of the notes, I want every "see other-file" pointer to lead somewhere real, so that I can always follow guidance to its source.

#### Acceptance Criteria

1. THE Author SHALL identify every Cross_Reference in the Core_Notes.
2. IF a Cross_Reference points to a steering file that is absent from the Steering_Directory, THEN THE Author SHALL resolve the Cross_Reference so that its target exists in the Steering_Directory.
3. THE Steering_Notes SHALL contain no Cross_Reference whose target is missing from the Steering_Directory.
4. WHERE a Cross_Reference names a target document, THE referenced target SHALL cover the topic the citing note attributes to it.

### Requirement 4: Simulation-standards note present and faithful to its references

**User Story:** As a designer, I want the `simulation-standards.md` note to exist and say what the notes that cite it claim, so that the standards `design-principles.md` and `playtesting.md` defer to are actually available.

#### Acceptance Criteria

1. THE Steering_Directory SHALL contain a `simulation-standards.md` document.
2. THE `simulation-standards.md` document SHALL cover the simulation and analysis topics that `design-principles.md` and `playtesting.md` attribute to it, including how tests and simulation runs are conducted and the skill-gap standard those notes rely on.
3. THE `simulation-standards.md` document SHALL state guidance consistent with the binding constraints recorded in `design-principles.md` (including the thin-skill-gap warning) and the simulation-versus-table-test stance in `playtesting.md`.
4. THE Cross_References to `simulation-standards.md` in `design-principles.md` and `playtesting.md` SHALL resolve to the `simulation-standards.md` document in the Steering_Directory.

### Requirement 5: Primacy statement embedded in each core note

**User Story:** As the collection owner, I want each steering note to declare its own authority, so that any session that loads the notes is told to defer to and cite them.

#### Acceptance Criteria

1. THE Author SHALL add a Primacy_Statement to each of the six Core_Notes.
2. THE Primacy_Statement SHALL state that the Steering_Notes are binding on design work.
3. THE Primacy_Statement SHALL instruct the reader to defer to the Steering_Notes as the primary reference for design decisions.
4. THE Primacy_Statement SHALL instruct the reader to cite the relevant Steering_Note when applying its guidance.
5. THE Primacy_Statement SHALL appear in a consistent, prominent position within each Core_Note so that a Reviewer can locate it in every Core_Note.

### Requirement 6: Durable mechanism relies on auto-loaded steering files only

**User Story:** As the collection owner, I want the primacy mechanism built into the auto-loaded notes themselves, so that it persists across sessions without depending on a separate guide or an automated hook.

#### Acceptance Criteria

1. THE primacy mechanism SHALL be implemented as Primacy_Statements embedded within the existing Core_Notes in the Steering_Directory.
2. THE Author SHALL NOT introduce a separate top-level guide document as the primacy mechanism.
3. THE Author SHALL NOT introduce an automated hook as the primacy mechanism.
4. THE Primacy_Statement content SHALL reside in files that are auto-loaded into a session so that the guidance applies without a reader taking an extra action.

### Requirement 7: Repaired notes remain mutually consistent

**User Story:** As a designer, I want the edits from this work to leave the whole note set coherent, so that fixing one note does not create a new conflict in another.

#### Acceptance Criteria

1. WHEN the Author completes all edits, THE Steering_Notes SHALL be free of the contradictions and broken Cross_References the audit identified.
2. IF an edit to one Steering_Note changes guidance that another Steering_Note depends on, THEN THE Author SHALL update the dependent note so that both state consistent guidance.
3. THE added Primacy_Statements SHALL be consistent in claim and wording intent across all six Core_Notes.
