# Design Document — Collection Audit

## Overview

This design describes **how to produce `COLLECTION_AUDIT.md`** — its document structure, the scoring methodology behind it, the information flow from existing source documents, and the analytical methods for each section. It is a methodology design for a written analysis deliverable, not a software architecture. There is no code. The "system" is the audit document; "architecture" here means document structure and information flow (per the vocabulary mapping in `design-principles.md`).

The audit is a **read-mostly** deliverable. It reads from the existing corpus (the canonical index, per-game rulebooks and design analyses, the concepts sheet, the OUROBOROS post-mortem, and the steering rubric) and produces one new top-level document plus *surgical* edits to `COLLECTION_OVERVIEW.md` only where a finding changes a game's status or priority.

Two firm boundaries shape every decision below:

- **The canonical index is authoritative.** `COLLECTION_OVERVIEW.md` stays the index of record. The audit cross-references it rather than restating its tables, and writes back to it only the deltas it surfaces (Requirements 1.3, 1.4, 9.1–9.4).
- **Steering is binding.** The rubric dimensions, tier semantics, physical-handling constraints, and OUROBOROS lessons come from the steering files; the audit applies them, it does not redefine them.

## Architecture

*Architecture here means the structure of the audit document and how information flows into it — not software architecture.*

### Document structure of `COLLECTION_AUDIT.md`

The document is organised top-to-bottom so a reader meets framing first, evidence in the middle, and the single actionable list last. Section order is deliberate: the roadmap (§6) sits at the end because every roadmap item must trace back to a finding stated in §2–§5.

| § | Section | Purpose | Primary requirements |
|---|---|---|---|
| 0 | **Introduction & canonical-index note** | States that `COLLECTION_OVERVIEW.md` remains the canonical index and that this is a design-facing analysis; states scope (10 live games + OUROBOROS), date, and the cross-reference (not duplicate) policy. | 1.2, 1.3, 1.4 |
| 1 | **Methodology note** | Briefly defines the 7 rubric dimensions, the 1–10 scale anchors, and the source docs feeding the audit, so the scorecards read consistently. | 2.2 |
| 2 | **Per-game rubric scorecards** | One scorecard per live game: 7 dimension scores (1–10) with cited justification, plus tier and recorded first-table questions; followed by the cross-game **summary matrix**. | 2.1–2.5, 3.1–3.4, 4.1–4.3 |
| 3 | **Collection gaps & overlaps** | Gap analysis across player count / time / complexity / mood, and overlap (shared-niche) analysis, both referencing the Overview coverage tables. | 5.1–5.4, 6.1–6.4 |
| 4 | **OUROBOROS revival re-evaluation** | Confronts the three cut reasons, assesses the vacated solo niche, applies binding handling constraints, reaches a verdict. | 7.1–7.5 |
| 5 | **Ranked priority roadmap** | Single ranked list of concrete next actions, each tied to a finding above. | 8.1–8.4 |
| 6 | **Overview sync log** | Short record of which `COLLECTION_OVERVIEW.md` entries were changed (and which deliberately were not) as a result of the audit. | 9.1–9.4 |

The config file `.kiro/specs/collection-audit/.config.kiro` accompanies this spec.

### Cross-reference discipline (Requirement 1.4)

Wherever the audit would restate status, deck maths, or coverage already held elsewhere, it **links** instead:

- Coverage facts → link to the relevant table in `COLLECTION_OVERVIEW.md`.
- Deck maths (K₉, subset property, 12-triangle almanac) → link to `deck-structure.md` / `DECK_SIZE_DECISION.md`.
- Per-game balance numbers → link to that game's `_design_analysis.md`.
- Tier definitions, rubric, handling rules → link to the relevant steering file.

The audit may *quote a single figure* to make a point, but never reproduces a whole table.

## Components and Interfaces

*The audit's "components" are its analytical sections; their "interfaces" are the source documents each one reads and the outputs it produces. The detailed method for each is given in the sections that follow this one.*

| Component (section) | Reads from (input interface) | Produces (output interface) |
|---|---|---|
| **Scoring engine** (§2 scorecards) | rulebooks, design analyses, steering rubric, concepts | 7 scored dimensions + justification per game; summary matrix |
| **Gap analysis** (§3) | Overview coverage tables | named, table-referenced gaps across 4 dimensions |
| **Overlap analysis** (§3) | Overview coverage + "deck-property used" table | named, adjudicated shared-niche overlaps |
| **OUROBOROS re-evaluation** (§4) | OUROBOROS post-mortem, concepts cut note, handling steering | a gated verdict tied to the three cut reasons |
| **Roadmap builder** (§5) | every finding from §2–§4 | a single ranked, traceable action list |
| **Sync writer** (§6) | the audit's own surfaced changes | minimal edits to `COLLECTION_OVERVIEW.md` + a sync log |

The components run in order: scoring feeds gaps/overlaps (which read the same coverage axes), all of §2–§4 feed the roadmap, and surfaced changes feed the sync writer. The information-flow diagram below is the full interface map.

### Information flow: which sources feed which section

```
COLLECTION_OVERVIEW.md ─┬─► §0 canonical-index note (declare authority)
 (selectors, tiers,     ├─► §2 tier + first-table questions per game
  coverage tables,      ├─► §3 gap & overlap analysis (coverage tables are the baseline)
  recorded questions)   └─► §6 sync targets (write-back)

per-game _rulebook.md ──────► §2 deck-necessity, flipping, pair-uniqueness, teachability evidence
per-game _design_analysis.md ► §2 handling viability + balance evidence (e.g. skill-gap, stalls)
NEW_GAME_CONCEPTS.md ──┬─► §2 "key deck property used" + recorded first-table questions
                       └─► §4 OUROBOROS cut record + vacated solo niche
OUROBOROS_design_analysis.md ─► §4 the three cut reasons + binding lessons (verbatim confrontation)

steering/design-principles.md ─► §1 rubric dimensions + 1–10 anchors; §4 binding constraints
steering/physical-handling.md ─► D2 scoring rubric; §4 handling test
steering/product-vision.md ────► tier semantics; collection-level criteria (D5, D6, D7)
steering/deck-structure.md ────► deck-property citations for D1/D3/D4 justifications
```

Sourcing rules:

- **First-table questions** are lifted from `COLLECTION_OVERVIEW.md` and `NEW_GAME_CONCEPTS.md` and reproduced faithfully; the audit must not invent substitutes (Requirements 3.2–3.4). Games without recorded questions are marked "none recorded" rather than back-filled.
- **Balance/handling claims** in justifications cite the game's `_design_analysis.md` where one exists (SYZYGY, TURNCOAT, TWELVE TRIALS, WILDFIRE, CROSSROADS, FACE VALUE, FORKED TONGUE… per the folder inventory); Tier-3 games with only a rulebook are scored from the rulebook and flagged as un-simmed where D2 evidence is thin.

## Data Models

*The audit's "data models" are the structured scoring artefacts every scorecard instantiates: the dimension set (D1–D7), the shared 1–10 scale, the per-game scorecard block, and the cross-game summary matrix. Defining them once here keeps every game's entry consistent and comparable.*

### The seven rubric dimensions

The dimensions are drawn from the evaluation rubric in `design-principles.md` (items 1–8) combined with the collection-level criteria in `product-vision.md`, distilled to the seven the requirements name:

| # | Dimension | Question it answers | Anchored in |
|---|---|---|---|
| D1 | **Deck-necessity** | Would an ordinary deck run this just as well? (10 = impossible without K₉; 1 = generic) | design-principles #1; product-vision "deck necessity" |
| D2 | **Physical-handling viability** | Does it survive the double-faced-card reality with no hidden-face memory burden? | physical-handling.md checklist; design-principles #2,#3 |
| D3 | **Flipping load-bearing** | Does flipping create real decisions/reversals, or is it incidental? | design-principles #4 |
| D4 | **Pair-uniqueness load-bearing** | Does "every pair exactly once" do real work (deduction, shrinking lie-space, denial)? | design-principles #5; deck-structure |
| D5 | **Distinctness** | Does it create an experience the other games don't? | product-vision "distinctness"; design-principles #6 |
| D6 | **Gap-filling** | Does its player count / time / complexity / mood fill a useful hole? | product-vision "gap-filling"; design-principles #7 |
| D7 | **Teachability** | Can it be explained cleanly and slot into a learning order? | product-vision "teachability"; design-principles #8 |

### The 1–10 scale (Requirement 2.2)

Every dimension uses the same anchored scale so scores are comparable across games:

- **9–10** — Load-bearing / exemplary. The dimension is a defining strength; removing it would break the game or its place in the collection.
- **6–8** — Solid. Clearly present and positive, with minor caveats.
- **4–5** — Mixed. Works but with a real, named weakness or only partial reliance on the property.
- **1–3** — Weak. The dimension is a liability or essentially absent (e.g. an ordinary deck would do; flipping is cosmetic).

Scores are integers. The methodology note (§1) reproduces these anchors so a reader can audit any score against them.

### Scorecard template (Requirements 2.1, 2.3, 2.4, 3.1–3.3, 4.3)

Each live game gets an identical block, so cross-game reading is frictionless:

```markdown
### <GAME NAME>  ·  Tier <n> (<tier label>)
*<players> · <time> · <genre>* — folder `<Folder>/`  (rulebook · analysis links)

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)            | n/10 | … |
| Physical-handling viability (D2)| n/10 | … |
| Flipping load-bearing (D3)     | n/10 | … |
| Pair-uniqueness load-bearing (D4)| n/10 | … |
| Distinctness (D5)              | n/10 | … |
| Gap-filling (D6)               | n/10 | … |
| Teachability (D7)              | n/10 | … |

**First-table questions:** <reproduced verbatim/faithfully from Overview / concepts, or "none recorded">
**Recommendation:** <next action> — *Tier <n>; <table-test-first note for Tier 2/3, or evidence + sign-off note for Tier 1>*
```

Rules the template enforces:

- **Justification must cite something concrete** (Requirement 2.3): a named deck property (e.g. "every pair exactly once → provable voids"), a named handling technique (e.g. "oriented public registry", "palms-commit"), or a named coverage fact ("only 1-player game besides TWELVE TRIALS"). Generic praise is not acceptable.
- **Low scores (≤5) name the specific weakness** (Requirement 2.4): e.g. "D1 = 4: the trick-taking shell would run on a normal deck; only the unplayed-pair deduction needs K₉" — never "could be better".
- **Tier appears in the header and beside the recommendation** (Requirements 3.1, 4.3).

### Cross-game comparison: the summary matrix (Requirement 2.5)

After the individual scorecards, a single matrix lets the reader compare every game on every dimension at a glance:

```markdown
| Game | Tier | D1 | D2 | D3 | D4 | D5 | D6 | D7 |
|------|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| SYZYGY | 1 | … | … | … | … | … | … | … |
| … |
```

Reading **down a column** ranks all games on one dimension (e.g. which games lean hardest on pair-uniqueness); reading **across a row** profiles one game. This table is the comparison instrument Requirement 2.5 calls for.

### Tier-respecting recommendations (Requirement 4)

The recommendation line in each scorecard obeys the tier discipline from `product-vision.md` and `playtesting.md`:

- **Tier 1 (SYZYGY, TURNCOAT):** default recommendation is "leave alone — benchmark". If the audit proposes any re-tune or re-skin, it must attach explicit evidence and the note *"requires owner sign-off"* (Requirement 4.1).
- **Tier 2 (TWELVE TRIALS, WILDFIRE, CROSSROADS) & Tier 3 (JANUS, FORKED TONGUE, THE UNPLAYED PAIR, FACE VALUE, THE COUNCIL):** the recommendation **prioritises a first table test** over more simulation or new design (Requirement 4.2), framed around the game's own recorded first-table questions.

## Methodology: gap analysis (Requirement 5)

The gap analysis treats the four Overview coverage tables as the empirical baseline and asks, per dimension, "what is unfilled?".

| Dimension | Source table | Method | Example signal |
|---|---|---|---|
| **Player count** | "By player count" matrix | Tally games per count 1–6; flag thin/empty counts. | 1P has only TWELVE TRIALS; is solo under-served? |
| **Play time** | "By play time" table | Bucket into bands (≤10, ~15, ~20, ~25+ min); flag empty bands. | Is there a sub-10-min filler besides WILDFIRE? |
| **Complexity** | "By complexity" table | Count Light / Light–Medium / Medium / Heavy; flag missing weights. | No genuinely Heavy game — is that a gap or a choice? |
| **Mood / genre** | "By genre / mood" table | List occupied moods; flag absent genres. | Any cooperative game beyond JANUS? Any pure-luck family game? |

Rules:

- Each identified gap **references the specific Overview table** it came from (Requirement 5.2) and **names the explicit missing band** — the player count, time band, weight, or mood — so it is actionable (Requirement 5.3), not "needs more variety".
- A dimension found to be **well covered is stated as such** rather than dropped (Requirement 5.4), so the reader knows it was examined.
- All four dimensions are always reported (Requirement 5.1).

## Methodology: overlap analysis (Requirement 6)

Overlap = two or more live games occupying substantially the same niche. Detection is a **shared-niche scan** across the same coverage axes used for gaps, plus the "deck-property used" axis from the coverage-at-a-glance table:

1. **Cluster** games that share a cell or adjacent cells on an axis (e.g. same player-count band *and* same mood). Candidate clusters from the current index: SYZYGY ↔ TURNCOAT (same engine, same count/length/weight); FORKED TONGUE ↔ FACE VALUE (bluffing family, differing player count); FORKED TONGUE ↔ THE COUNCIL (social/negotiation at 3–6P).
2. For each cluster, **name the games and the shared dimension** (Requirement 6.3) and **cite the Overview table(s)** that reveal the overlap (Requirement 6.2).
3. **Adjudicate** (Requirement 6.4): decide whether the games are distinct enough to coexist (e.g. SYZYGY vs TURNCOAT share an engine but differ in feel — coexist) or whether one is a candidate to differentiate, park, or cut. The verdict applies the distinctness criterion from `product-vision.md`.

Every detected shared niche is reported (Requirement 6.1); a "near-overlap that resolves on inspection" is still reported with its coexist verdict, so the reasoning is visible.

## Methodology: OUROBOROS revival re-evaluation (Requirement 7)

This section is structured as a confrontation, not a summary. It reads `OUROBOROS_design_analysis.md` and the Overview/concepts cut notes, then works through four steps:

1. **Confront each recorded cut reason** (Requirement 7.2), one subsection each:
   - **Luck-driven play** — the thin random-vs-skilled gap (greedy 7.00 vs random 7.90 scars; smart 4.74). Ask whether any redesign widens the skill gap to the collection's ~1.5× healthy bar.
   - **Hidden open symbol under the serpent's head** — the load-bearing handling failure: constantly-needed state lived on a down-face (violates `physical-handling.md`). Ask whether the open end can be made visible.
   - **Thin skill gap** — treated by steering as a red-flag predictor of a dull table; confront whether the concept can clear it.
2. **Assess the vacated solo niche** (Requirement 7.3): with OUROBOROS cut, TWELVE TRIALS is the lone 1P game. Evaluate whether a second solo game is worth having, and whether any OUROBOROS mechanic (the Eulerian-loop construction, the impossible-single-scar theorem) is worth carrying into a new or existing design.
3. **Apply the binding constraints as a gate** (Requirement 7.5): any proposed revival of a mechanic must be shown to use **open information / visible state**, with no hidden-face memory and no constantly-needed state on a down-face. A revival that cannot pass this gate is not recommended.
4. **Reach a verdict** (Requirement 7.4): exactly one of **revive**, **keep cut**, or **revive only under stated conditions**, with the verdict explicitly tied back to the three cut reasons it resolves or fails to resolve. (The steering's standing position is that a clean cut that teaches a lesson is a success — the verdict must earn any departure from "keep cut".)

## Methodology: ranked roadmap construction (Requirement 8)

The roadmap is built **last**, by harvesting findings already stated in §2–§4, so every item is traceable:

1. **Collect candidate actions** — each scorecard recommendation, each actionable gap, each overlap verdict that warrants action, and the OUROBOROS verdict become candidate items.
2. **Rank** them (Requirement 8.2). The ranking heuristic follows the project's stated centre of gravity — *table testing outranks further simulation or new design* (`playtesting.md`) — then weights by collection impact (a gap or overlap affecting the whole collection) and by tier (untested Tier-2/3 first tables rise; Tier-1 changes sink absent strong evidence).
3. **Write each item as a concrete action** (Requirement 8.4): "Run a 4P first table test of THE UNPLAYED PAIR targeting its hidden-face-rank question", not "improve the trick-taker".
4. **Tie each item to its finding** (Requirement 8.3): every item carries a back-reference, e.g. "(see §2 THE UNPLAYED PAIR scorecard / §3 mood gap)".

## Methodology: canonical-index sync (Requirement 9)

The write-back to `COLLECTION_OVERVIEW.md` is deliberately minimal:

- **Change surfaced → update the matching Overview entry** (Requirement 9.1): if the audit concludes a game's status or priority changes (e.g. a park/cut recommendation, a promotion priority), edit that game's entry to reflect it.
- **No change surfaced → leave the entry untouched** (Requirement 9.2): games the audit merely scores without a status/priority delta are not edited.
- **Overview stays the index, not a second audit** (Requirement 9.3): only status/priority lines change; the full scorecards, justifications, and analysis stay in `COLLECTION_AUDIT.md` and are linked, not copied.
- **Tier change → relocate the game** (Requirement 9.4): if a game's maturity tier changes, move its entry into the correct tier section of the Overview (the steering's rule: keep the Overview's tier sections accurate; keep cut games' folders as archives).
- The audit's **§6 sync log** records what was changed and what was intentionally left alone, so the write-back is itself auditable.

## Error Handling

*Since there is no executing code, "errors" are integrity failures in the analysis.* The methodology guards against:

- **Stale source data** — if a source doc conflicts with the Overview, the audit notes the conflict and treats the Overview as canonical for status/tier, flagging the discrepancy as a finding.
- **Missing evidence** — a Tier-3 game with no `_design_analysis.md` is scored from its rulebook with D2 explicitly marked "un-simmed; handling unverified at the table", never silently guessed.
- **Fabricated questions** — first-table questions with no source are not invented; the game is marked "none recorded" (Requirement 3.4).
- **Duplication drift** — any table the audit is tempted to copy from the Overview is replaced by a link (Requirement 1.4).
- **Untraceable roadmap items** — an action with no originating finding is removed or a finding is added to justify it (Requirement 8.3).

## Testing Strategy

This is a documentation deliverable, so "testing" is **review against checkable content invariants** rather than executing code or running property-based tests (PBT is not applicable — there is no function with generated inputs). A reviewer verifies the produced `COLLECTION_AUDIT.md` and the synced `COLLECTION_OVERVIEW.md` against the correctness properties below. Each property is a universal statement over the document's content (every game, every score, every roadmap item, every reference) that can be confirmed by reading.

Review checklist, mapped to the properties:

- **Completeness sweep** — walk the 10 live games; confirm each has a full 7-dimension scorecard, a tier, and faithfully reproduced first-table questions (Properties 1, 5, 6).
- **Scale & justification sweep** — for every score, confirm it is an integer 1–10, carries a concrete cited justification, and (if ≤5) names a specific weakness (Properties 2, 3, 4).
- **Recommendation sweep** — for every recommendation, confirm tier is stated and tier discipline is honoured (Property 7).
- **Gaps & overlaps sweep** — confirm each gap/overlap references a coverage table and is specific/adjudicated (Properties 8, 9).
- **OUROBOROS sweep** — confirm all three cut reasons are confronted and any revived mechanic passes the handling gate (Property 10).
- **Roadmap sweep** — confirm every item is ranked, concrete, and traceable to a finding (Property 11).
- **Sync sweep** — confirm surfaced changes are reflected in the Overview and unchanged games are untouched (Property 12).
- **Cross-reference sweep** — confirm restated content links out rather than duplicating (Property 13).

## Correctness Properties

*A property is a characteristic that should hold true across all valid instances. For this documentation deliverable, properties are universal statements about the content of the produced `COLLECTION_AUDIT.md` (and synced `COLLECTION_OVERVIEW.md`) that a reviewer can verify by reading the documents.*

### Property 1: Every live game is fully scored

*For every* one of the ten live games, the audit contains a scorecard with a score for all seven rubric dimensions (D1–D7).

**Validates: Requirements 2.1**

### Property 2: All scores lie on the 1–10 scale

*For every* dimension score appearing in any scorecard or in the summary matrix, the score is an integer between 1 and 10 inclusive.

**Validates: Requirements 2.2**

### Property 3: Every score carries a concrete justification

*For every* dimension score of every live game, there is an accompanying justification that cites a specific deck property, handling technique, or coverage fact (not a generic remark).

**Validates: Requirements 2.3**

### Property 4: Low scores name a specific weakness

*For every* dimension score of 5 or below, the justification states the specific weakness rather than a generic remark.

**Validates: Requirements 2.4**

### Property 5: Every live game has a recorded tier

*For every* one of the ten live games, the audit records its maturity tier, and that tier matches the tier semantics in `product-vision.md`.

**Validates: Requirements 3.1**

### Property 6: First-table questions are reproduced faithfully and never fabricated

*For every* live game that has recorded first-table questions in the source documents, the audit reproduces those specific questions without altering their meaning; *for every* game without recorded questions, the audit invents none.

**Validates: Requirements 3.2, 3.3, 3.4**

### Property 7: Every recommendation states its game's tier and respects tier discipline

*For every* recommendation the audit makes for a game, the game's tier is stated alongside it; *for every* Tier-2 or Tier-3 recommendation, a first table test is prioritised over further simulation or new design; *for every* Tier-1 re-tune/re-skin proposal, explicit evidence and an owner-sign-off note are attached.

**Validates: Requirements 4.1, 4.2, 4.3**

### Property 8: Every identified gap is grounded and specific

*For every* gap the audit identifies, it references the relevant `COLLECTION_OVERVIEW.md` coverage table and names the explicit missing band (player count, time band, weight, or mood).

**Validates: Requirements 5.2, 5.3**

### Property 9: Every overlap is grounded, named, and adjudicated

*For every* overlap the audit reports, it references the relevant Overview coverage table, names the games involved and the shared niche dimension, and — where action is warranted — states whether the games coexist or one is a candidate to differentiate, park, or cut.

**Validates: Requirements 6.2, 6.3, 6.4**

### Property 10: The OUROBOROS re-evaluation confronts every cut reason and gates revivals

The re-evaluation addresses each of the three recorded cut reasons (luck-driven play, hidden open symbol under the serpent's head, thin skill gap); *for every* OUROBOROS mechanic it recommends reviving, it shows the revival avoids hidden-face memory and keeps constantly-needed state visible.

**Validates: Requirements 7.2, 7.5**

### Property 11: Every roadmap item is ranked, concrete, and traceable

*For every* item in the priority roadmap, the item appears in a ranked ordering, describes a concrete action, and references a specific finding stated earlier in the document.

**Validates: Requirements 8.2, 8.3, 8.4**

### Property 12: Overview sync fidelity

*For every* game for which the audit surfaces a status or priority change, the corresponding `COLLECTION_OVERVIEW.md` entry is updated to reflect it (and relocated to the correct tier section if its tier changed); *for every* game for which the audit surfaces no such change, that game's Overview entry is left unchanged.

**Validates: Requirements 9.1, 9.2, 9.4**

### Property 13: Cross-reference, not duplication

*For every* place where the audit refers to status, deck maths, or coverage already held in another document, it links or cross-references the authoritative document rather than reproducing that content.

**Validates: Requirements 1.4**
