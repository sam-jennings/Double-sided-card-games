# Requirements Document

## Introduction

Retheme SYZYGY and TURNCOAT to use the Nine Signs primary symbol set (Void, Root, Wave, Flame, Eye, Mask, Key, Star, Crown). SYZYGY is renamed to TRIGON as part of this retheme — the old celestial name no longer fits the new sign-convergence theme. TURNCOAT keeps its name (defection/betrayal is theme-independent). This is a flavour-only rewrite: all mechanics, balance numbers, ability requirements, and game structures remain unchanged. Each of the Nine Signs is assigned to the ability whose flavour best matches the sign's core archetype, and each sign carries a consistent thematic role ("verb family") across both games. The old Syzygy/ folder is retired as an archive (not deleted). The deliverables are: a new Trigon/ folder with TRIGON_rulebook.md, an updated TURNCOAT_rulebook.md, and updated cross-references in all top-level documents.

## Glossary

- **Retheme_Engine**: The process and rules governing how Nine Signs names replace the current celestial (SYZYGY/TRIGON) and guild (TURNCOAT) names throughout both rulebooks.
- **Nine_Signs**: The primary symbol set for the shipping deck — Void (1), Root (2), Wave (3), Flame (4), Eye (5), Mask (6), Key (7), Star (8), Crown (9).
- **Sign_Mapping**: The assignment of each Nine Signs name to a specific ability in each game, based on archetype-first matching.
- **Verb_Family**: The consistent thematic role a sign carries across both TRIGON and TURNCOAT (e.g. Eye always means perception, Flame always means destruction).
- **Rulebook**: The complete player-facing rules document for a game (TRIGON_rulebook.md or TURNCOAT_rulebook.md).
- **Ability**: A symbol's mechanical effect, defined by a requirement (grid condition) and a power (what happens when activated). Abilities are identified by their mechanic, not their name.
- **Card_Manifest**: The section of a rulebook listing all 36 cards and their face pairs.
- **Mnemonic_Justification**: A brief note explaining why a sign maps to a given ability, kept to one sentence in the same functional tone as the current rulebooks.
- **TRIGON**: The new name for the game previously called SYZYGY. Refers to the three-point convergence of signs (three matching symbols aligning).
- **Archive_Folder**: The existing Syzygy/ folder, retained as a read-only design record after the rename.
- **Cross_Reference**: Any mention of SYZYGY or its folder path in a document outside the game's own folder (e.g. COLLECTION_OVERVIEW.md, SYMBOL_SETS.md, NEW_GAME_CONCEPTS.md, steering files).

## Requirements

### Requirement 1: Archetype-First Sign Assignment

**User Story:** As a game designer, I want each of the Nine Signs assigned to the ability whose flavour best matches the sign's core meaning, so that sign names serve as mnemonics for their abilities.

#### Acceptance Criteria

1. THE Sign_Mapping SHALL assign exactly one distinct Nine Signs name to each of the 9 abilities in TRIGON and exactly one distinct Nine Signs name to each of the 9 abilities in TURNCOAT.
2. WHEN assigning Star (8) in TRIGON, THE Sign_Mapping SHALL map Star to the ability currently named "Star" (wild in alignments + draw-and-play on corner).
3. WHEN assigning Void (1) in TRIGON, THE Sign_Mapping SHALL map Void to the ability currently named "Void" (catch-up draw when isolated).
4. THE Sign_Mapping SHALL preserve the phrase "Star is wild" verbatim in the TRIGON rulebook.
5. THE Sign_Mapping SHALL use all nine sign names exactly once per game — no sign is unused, no sign is duplicated within a single game.

### Requirement 2: Cross-Game Verb Family Coherence

**User Story:** As a player learning both games, I want each sign to carry a consistent thematic role across TRIGON and TURNCOAT, so that learning one game reinforces the other.

#### Acceptance Criteria

1. THE Sign_Mapping SHALL assign each sign a verb family that applies in both TRIGON and TURNCOAT (e.g. Eye = perception, Flame = destruction/removal, Wave = movement, Mask = identity-swap/flip, Key = extraction/access, Root = connection/adjacency, Crown = apex/self-banking, Void = emptiness/catch-up, Star = wild/exception).
2. THE Sign_Mapping SHALL ensure that a sign's ability in TRIGON and its ability in TURNCOAT both fall within that sign's declared verb family.
3. IF a sign's TRIGON ability and TURNCOAT ability differ in specifics, THEN THE Sign_Mapping SHALL ensure both abilities are recognisable expressions of the same thematic archetype.

### Requirement 3: Mechanical Preservation

**User Story:** As a game designer with ~45k simulated games invested in each ruleset, I want all mechanics and balance numbers to remain untouched, so that the retheme does not invalidate existing simulation work.

#### Acceptance Criteria

1. THE Retheme_Engine SHALL preserve every ability's requirement (grid condition) exactly as written in the current rulebook.
2. THE Retheme_Engine SHALL preserve every ability's mechanical effect exactly as written in the current rulebook.
3. THE Retheme_Engine SHALL preserve all numeric values (player counts, grid dimensions, turn counts, scoring rules, tiebreakers, adjacency definitions, activation limits).
4. THE Retheme_Engine SHALL preserve the card manifest structure (36 cards, each showing a pair of two different symbols, complete graph K₉).
5. THE Retheme_Engine SHALL preserve all edge-case rulings and FAQ answers, updating only the symbol names referenced within them.
6. THE Retheme_Engine SHALL preserve all designer's variants, updating only the symbol names referenced within them.

### Requirement 4: Rulebook Completeness

**User Story:** As a player, I want each updated rulebook to be a full standalone document, so that I do not need the old rulebook or any supplementary material to play.

#### Acceptance Criteria

1. THE Rulebook SHALL contain all sections present in the current version: introduction/flavour paragraph, components, setup, turn overview, core mechanism explanation, ability reference table, chains example, game end and scoring, edge cases and FAQ, strategy notes, card manifest, and designer's variants.
2. THE Rulebook SHALL update the intro/flavour paragraph to reference the Nine Signs rather than celestial bodies (TRIGON) or guilds (TURNCOAT).
3. THE Rulebook SHALL update the ability reference table to use Nine Signs names in place of the old symbol names, with all mechanics columns unchanged.
4. THE Rulebook SHALL update the card manifest to use Nine Signs icon/name pairs throughout.
5. THE Rulebook SHALL update all worked examples and chain illustrations to use Nine Signs names while describing the same mechanical sequence.
6. THE Rulebook SHALL update all strategy notes to reference Nine Signs names.

### Requirement 5: Tone and Style Preservation

**User Story:** As a game designer, I want the rewritten rulebooks to maintain the same clean functional voice as the originals, so that the retheme feels like a name-swap rather than a rewrite of authorial intent.

#### Acceptance Criteria

1. THE Rulebook SHALL use the same paragraph structure, sentence length patterns, and formatting conventions (headers, tables, bold, italics, blockquotes) as the current version.
2. THE Rulebook SHALL NOT add new narrative prose, lore paragraphs, or flavour fiction beyond what exists in the current version.
3. WHEN a mnemonic justification is needed to explain a sign-to-ability mapping, THE Rulebook SHALL keep the justification to one parenthetical clause or short sentence in the same functional register.
4. THE Rulebook SHALL preserve the design version note and simulation-count reference at the end of each document.

### Requirement 6: Pip Number Independence

**User Story:** As a game designer, I want the sign-to-ability mapping to prioritise mnemonic fit over pip number, so that the best archetype carries each ability regardless of which pip it sits on.

#### Acceptance Criteria

1. THE Sign_Mapping SHALL assign signs to abilities based on archetype-meaning match, not on preserving the current pip-to-ability correspondence.
2. WHEN a sign's pip number differs from the ability's original pip position, THE Retheme_Engine SHALL update all references in the rulebook to reflect the new sign name without altering any mechanical text.
3. THE Retheme_Engine SHALL ensure the ability reference table lists abilities in pip order (1–9) of their newly assigned sign, matching the physical deck's pip sequence.

### Requirement 7: Two-Layer Production Rule Compliance

**User Story:** As a game designer, I want the retheme to comply with the two-layer production rule (permanent deck identity + per-game interpretation), so that the same physical deck serves both games without ambiguity.

#### Acceptance Criteria

1. THE Rulebook SHALL refer to signs by their permanent deck-identity names (Void, Root, Wave, Flame, Eye, Mask, Key, Star, Crown) — not by game-local aliases.
2. THE Rulebook SHALL treat the sign icon and pip printed on the card as the authoritative identity reference.
3. THE Rulebook SHALL NOT require any card content beyond what the permanent deck identity provides (pip, sign icon, sign name, colour, orientation marker).

### Requirement 8: Game Rename (SYZYGY → TRIGON)

**User Story:** As a game designer, I want the game formerly called SYZYGY renamed to TRIGON, so that the game name reflects the new Nine Signs theme (three-point convergence) rather than the retired celestial theme (astronomical alignment).

#### Acceptance Criteria

1. THE Rulebook SHALL use the title "TRIGON" in the document heading, all internal references, and the design version note.
2. THE Rulebook SHALL replace the intro flavour paragraph's celestial-alignment framing ("the alignment of three celestial bodies") with a Nine Signs convergence framing (three signs converging / a three-point convergence of signs).
3. THE Rulebook SHALL NOT include a pronunciation guide — TRIGON requires no pronunciation aid.
4. THE Rulebook SHALL replace all occurrences of the word "syzygy" (as a game-mechanic term for the three-in-a-row capture event) with "trigon" or an equivalent term consistent with the new name.
5. THE Rulebook SHALL update the sibling-reference note at the end of the document to read as a sibling to TURNCOAT (not "a sibling to SYZYGY").
6. THE Rulebook SHALL update the designer's-variants section heading and any variant names that reference the old celestial theme (e.g. "Calm Skies" renamed to fit the Nine Signs theme, "Deep Space" renamed similarly) while preserving each variant's mechanics.

### Requirement 9: File and Folder Structure

**User Story:** As a game designer following the repository's per-game folder conventions, I want a new Trigon/ folder with correctly named files, and the old Syzygy/ folder marked as archived, so that the project structure stays clean and navigable.

#### Acceptance Criteria

1. THE Retheme_Engine SHALL create a new folder named `Trigon/` at the same level as other game folders.
2. THE Retheme_Engine SHALL place the new rulebook in `Trigon/TRIGON_rulebook.md` following the UPPER_SNAKE naming convention.
3. THE Retheme_Engine SHALL NOT delete, move, or modify any files in the existing `Syzygy/` folder.
4. THE Retheme_Engine SHALL add an archive notice to the top of `Syzygy/SYZYGY_rulebook.md` stating that the game has been renamed to TRIGON and directing readers to `Trigon/TRIGON_rulebook.md`.
5. WHEN the TURNCOAT rulebook is updated, THE Retheme_Engine SHALL modify `Turncoat/TURNCOAT_rulebook.md` in place (TURNCOAT is not renamed, so its folder stays unchanged).
6. THE Retheme_Engine SHALL update the sibling-reference line at the end of TURNCOAT_rulebook.md to reference TRIGON rather than SYZYGY.

### Requirement 10: Cross-Reference Updates

**User Story:** As a game designer, I want all top-level documents and collection indexes to reference TRIGON (not SYZYGY) and point to the correct folder, so that the project remains internally consistent after the rename.

#### Acceptance Criteria

1. THE Retheme_Engine SHALL update COLLECTION_OVERVIEW.md to replace all references to "SYZYGY" with "TRIGON" and all folder paths from `Syzygy/` to `Trigon/`.
2. THE Retheme_Engine SHALL update COLLECTION_OVERVIEW.md to note that the Syzygy/ folder is retained as an archive of the pre-rename design record.
3. THE Retheme_Engine SHALL update any references to "SYZYGY" in SYMBOL_SETS.md, NEW_GAME_CONCEPTS.md, DECK_SIZE_DECISION.md, and flip_card_project_goals.md to use "TRIGON" where the reference is to the live game (references to the old name in historical/analytical context may remain with a parenthetical noting the rename).
4. THE Retheme_Engine SHALL update the recommended play order in COLLECTION_OVERVIEW.md to list TRIGON in position 2 (replacing SYZYGY) with the same description updated for the new name.
5. THE Retheme_Engine SHALL update all coverage tables, selector tables, and genre/mood tables in COLLECTION_OVERVIEW.md to use TRIGON.
6. IF any steering file in `.kiro/steering/` references SYZYGY by name, THEN THE Retheme_Engine SHALL update that reference to TRIGON (or note both names where historical context requires it).
