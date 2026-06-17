# Requirements Document

## Introduction

The **Collection Audit** is a new top-level deliverable, `COLLECTION_AUDIT.md`, that takes stock of the whole flip-deck collection in one place. It scores every live game against the project's evaluation rubric, records each game's maturity tier and outstanding first-table questions, surfaces collection-level gaps and overlaps, re-examines the cut game OUROBOROS for possible revival, and ends with a single ranked roadmap of next actions. It is a design-facing analysis document, not a player-facing rulebook and not a replacement for the canonical index.

`COLLECTION_OVERVIEW.md` remains the authoritative index. The audit reads from it (coverage tables, tiers, recorded questions) and syncs status/priority changes back into it only where the audit surfaces such a change, cross-referencing rather than duplicating its content.

Because this is a tabletop game design project, "acceptance criteria" below are **observable outcomes in the content of the produced document(s)** — a reviewer can read `COLLECTION_AUDIT.md` (and the synced `COLLECTION_OVERVIEW.md`) and verify each criterion is met.

## Glossary

- **Collection_Audit**: The deliverable document `COLLECTION_AUDIT.md`, created at the top level of the repository. The "system" most requirements below act on.
- **Collection_Overview**: The existing canonical index document `COLLECTION_OVERVIEW.md`.
- **Live_Game**: One of the ten non-cut games — SYZYGY, TURNCOAT, TWELVE TRIALS, TURNOVER, CROSSROADS, JANUS, FALSE FACE, THE UNPLAYED PAIR, FACE VALUE, THE COUNCIL.
- **Cut_Game**: OUROBOROS, the archived solo serpent-building puzzle.
- **Rubric**: The evaluation dimensions the audit scores each game on — deck-necessity, physical-handling viability, flipping load-bearing, pair-uniqueness load-bearing, distinctness, gap-filling, teachability — each scored on the 1–10 scale derived from the evaluation rubric in `design-principles.md`, combined with the collection-level criteria in `product-vision.md`.
- **Maturity_Tier**: The four-level status from `product-vision.md` — Tier 1 Complete (SYZYGY, TURNCOAT); Tier 2 Sim/maths-validated, needs first table test (TWELVE TRIALS, TURNOVER, CROSSROADS); Tier 3 Rulebook complete, untested (JANUS, FALSE FACE, THE UNPLAYED PAIR, FACE VALUE, THE COUNCIL); Tier 4 Cut (OUROBOROS).
- **First_Table_Question**: A game's already-recorded first-table / test-focus question(s) as held in `COLLECTION_OVERVIEW.md` and `NEW_GAME_CONCEPTS.md`.
- **Collection_Gap**: A useful unfilled hole in player count, play time, complexity, or mood/genre across the collection.
- **Collection_Overlap**: Two or more Live_Games occupying substantially the same niche (genre, player count, length, mood, or deck-property used).
- **Priority_Roadmap**: A single ranked list at the end of the Collection_Audit of next actions across the collection, each item tied to a specific finding in the document.
- **Author**: The designer or agent producing the audit.

## Requirements

### Requirement 1: Standalone audit document at the top level

**User Story:** As the collection owner, I want a single standalone audit document at the top level, so that the collection's overall health lives in one referenceable place without disturbing the canonical index.

#### Acceptance Criteria

1. THE Author SHALL create the Collection_Audit as a file named `COLLECTION_AUDIT.md` at the top level of the repository.
2. THE Collection_Audit SHALL contain a dedicated section for each of the four audit outputs: per-game rubric scoring, collection-level gaps and overlaps, the OUROBOROS revival re-evaluation, and the Priority_Roadmap.
3. THE Collection_Audit SHALL state, in an introduction, that Collection_Overview remains the canonical index and that the audit is a design-facing analysis.
4. WHERE the Collection_Audit restates status, maths, or coverage already held in another document, THE Collection_Audit SHALL link or cross-reference the authoritative document rather than duplicate its content.

### Requirement 2: Full-rubric scoring of every live game

**User Story:** As a designer, I want every live game scored on the full rubric, so that I can compare games on consistent, explicit dimensions.

#### Acceptance Criteria

1. THE Collection_Audit SHALL score each of the ten Live_Games on every Rubric dimension: deck-necessity, physical-handling viability, flipping load-bearing, pair-uniqueness load-bearing, distinctness, gap-filling, and teachability.
2. THE Collection_Audit SHALL express each Rubric dimension score on the 1–10 scale derived from `design-principles.md`.
3. THE Collection_Audit SHALL accompany each Live_Game's set of scores with a written justification that cites the specific deck property, handling technique, or coverage fact behind the score.
4. WHERE a Live_Game scores low on a Rubric dimension, THE Collection_Audit SHALL state the specific weakness rather than a generic remark.
5. THE Collection_Audit SHALL present the per-game scores in a form that allows direct cross-game comparison on each Rubric dimension.

### Requirement 3: Maturity tier and first-table questions recorded

**User Story:** As the collection owner, I want each game's maturity tier and outstanding first-table questions recorded in the audit, so that the audit respects where each game actually is and what it still needs.

#### Acceptance Criteria

1. THE Collection_Audit SHALL record the Maturity_Tier of each Live_Game.
2. THE Collection_Audit SHALL record, for each Live_Game that has recorded First_Table_Questions, that game's specific First_Table_Questions.
3. THE Collection_Audit SHALL reproduce or reference each recorded First_Table_Question without altering its meaning.
4. THE Collection_Audit SHALL NOT invent generic test questions in place of a game's recorded First_Table_Questions.

### Requirement 4: Tier-respecting recommendations

**User Story:** As a designer, I want the audit to honour maturity tiers when recommending work, so that proven games are not casually disturbed and untested games are pushed toward the table.

#### Acceptance Criteria

1. IF the Collection_Audit proposes re-tuning or re-skinning a Tier 1 game (SYZYGY or TURNCOAT), THEN THE Collection_Audit SHALL accompany the proposal with explicit supporting evidence and a note that owner sign-off is required.
2. WHERE the Collection_Audit recommends next work for a Tier 2 or Tier 3 game, THE Collection_Audit SHALL prioritise a first table test over additional simulation or new design.
3. THE Collection_Audit SHALL state each game's Maturity_Tier alongside any recommendation it makes for that game.

### Requirement 5: Collection-level gap identification

**User Story:** As the collection owner, I want collection-level gaps identified, so that I can see which player-count, time, complexity, and mood holes remain unfilled.

#### Acceptance Criteria

1. THE Collection_Audit SHALL identify Collection_Gaps across at least the dimensions of player count, play time, complexity, and mood/genre.
2. THE Collection_Audit SHALL reference the coverage tables in Collection_Overview when identifying each Collection_Gap.
3. THE Collection_Audit SHALL describe each identified Collection_Gap in terms specific enough to act on (the missing player count, time band, weight, or mood named explicitly).
4. IF the audit finds a dimension to have no meaningful gap, THEN THE Collection_Audit SHALL state that the dimension is adequately covered rather than omit it.

### Requirement 6: Collection-level overlap identification

**User Story:** As a designer, I want collection-level overlaps identified, so that I can judge whether two games are competing for the same niche.

#### Acceptance Criteria

1. THE Collection_Audit SHALL identify each Collection_Overlap where two or more Live_Games occupy substantially the same niche.
2. THE Collection_Audit SHALL reference the coverage tables in Collection_Overview when identifying each Collection_Overlap.
3. WHEN the Collection_Audit reports a Collection_Overlap, THE Collection_Audit SHALL name the games involved and the shared niche dimension.
4. WHERE a reported Collection_Overlap warrants action, THE Collection_Audit SHALL state whether the games are distinct enough to coexist or whether one is a candidate to differentiate, park, or cut.

### Requirement 7: OUROBOROS revival re-evaluation

**User Story:** As the collection owner, I want OUROBOROS re-evaluated for revival, so that a decisive, evidence-based call is made rather than leaving the cut game in limbo.

#### Acceptance Criteria

1. THE Collection_Audit SHALL include a re-evaluation of the Cut_Game OUROBOROS for possible revival.
2. THE Collection_Audit SHALL explicitly confront each recorded reason OUROBOROS was cut: luck-driven play, the hidden open symbol under the serpent's head, and the thin skill gap between random and skilled play.
3. THE Collection_Audit SHALL assess whether the solo niche vacated by OUROBOROS, or any of its mechanics, is worth reviving.
4. THE Collection_Audit SHALL state a clear verdict for OUROBOROS — revive, keep cut, or revive only under stated conditions — with each verdict tied to the cut reasons it addresses.
5. IF the audit recommends reviving any OUROBOROS mechanic, THEN THE Collection_Audit SHALL show how the revival avoids hidden-face memory and keeps constantly-needed state visible, per the binding constraints in `design-principles.md`.

### Requirement 8: Ranked priority roadmap

**User Story:** As the collection owner, I want a single ranked roadmap of next actions, so that I know what to do next and why.

#### Acceptance Criteria

1. THE Collection_Audit SHALL end with a single Priority_Roadmap of next actions across the collection.
2. THE Collection_Audit SHALL present the Priority_Roadmap as a ranked ordering.
3. THE Collection_Audit SHALL tie each Priority_Roadmap item to a specific finding stated earlier in the document.
4. THE Collection_Audit SHALL describe each Priority_Roadmap item as a concrete action rather than a vague aspiration.

### Requirement 9: Canonical index sync on surfaced changes

**User Story:** As the collection owner, I want the canonical index kept in sync only where the audit surfaces a change, so that the overview stays accurate without being needlessly rewritten.

#### Acceptance Criteria

1. WHEN the Collection_Audit surfaces a status or priority change for a game, THE Author SHALL update the corresponding entry in Collection_Overview to reflect that change.
2. WHERE the Collection_Audit surfaces no status or priority change for a game, THE Author SHALL leave that game's Collection_Overview entry unchanged.
3. THE Author SHALL keep Collection_Overview as the canonical index, recording in it only status/priority changes and not the audit's full per-game scoring or analysis.
4. IF a game's Maturity_Tier changes as a result of the audit, THEN THE Author SHALL move that game to the correct tier section within Collection_Overview.
