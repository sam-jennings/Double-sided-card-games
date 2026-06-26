# Collection Audit

*A design-facing health check of the flip-deck collection — scored, gapped, and ranked.*

> **Date:** 2026-06-14
> **Status of this document:** complete. All sections (§0–§6) are filled; §2 scores every live game, §3 covers gaps and overlaps, §4 reaches the OUROBOROS verdict, §5 ranks the roadmap, and §6 logs the Overview sync.

---

## §0 · Introduction & canonical-index note

This is the **Collection Audit**: a single design-facing analysis that takes stock of the whole flip-deck collection in one place. It scores every live game against the project's evaluation rubric, records each game's maturity tier and outstanding first-table questions, surfaces collection-level gaps and overlaps, re-examines the cut game OUROBOROS for possible revival, and ends with a single ranked roadmap of next actions.

**`COLLECTION_OVERVIEW.md` remains the canonical index.** This audit is *not* a replacement for it and *not* a player-facing rulebook. The Overview is the authoritative record of selectors, status tiers, and coverage tables ([`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md)); this document reads from it and writes a small set of surfaced status/priority changes back into it (recorded in §6), but never supersedes it as the index. This division follows the binding repository-structure steering note, which names the Overview as the canonical index and requires keeping it in sync when a game changes tier (`/.kiro/steering/repository-structure.md`).

**Scope.** The audit covers the **ten live games** — TRIGON, TURNCOAT, TWELVE TRIALS, TURNOVER, CROSSROADS, JANUS, FALSE FACE, THE UNPLAYED PAIR, FACE VALUE, THE COUNCIL — **plus the cut game OUROBOROS**, which is re-evaluated for revival in §4. Game names are written in CAPS in prose to match existing docs.

**Cross-reference, don't duplicate.** Wherever this audit would restate status, deck maths, or coverage that already lives elsewhere, it **links** to the authoritative document rather than copying it (per the repository-structure steering note's "cross-reference rather than duplicate" rule):

- Coverage facts (player count, time, complexity, mood) → the coverage tables in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).
- Deck maths (K₉, the subset property, the 12-triangle almanac) → [`deck-structure.md`](.kiro/steering/deck-structure.md) and [`DECK_SIZE_DECISION.md`](DECK_SIZE_DECISION.md).
- Per-game balance numbers → that game's `_design_analysis.md`.
- Tier definitions, the evaluation rubric, and handling rules → the relevant steering file in `.kiro/steering/`.

The audit may quote a single figure to make a point, but it never reproduces a whole table.

---

## §1 · Methodology note

This section defines the scoring instrument used in §2 so every scorecard reads consistently. It does **not** redefine the rubric — the dimensions and anchors are distilled from the steering files, which the audit applies rather than redefines.

### The seven rubric dimensions

Each live game is scored on these seven dimensions, drawn from the evaluation rubric in [`design-principles.md`](.kiro/steering/design-principles.md) (items 1–8) combined with the collection-level criteria in [`product-vision.md`](.kiro/steering/product-vision.md). Rather than restate those rubrics in full, this audit links to them and applies them.

| # | Dimension | The question it answers | Anchored in (steering source) |
|---|---|---|---|
| **D1** | **Deck-necessity** | Would an ordinary deck run this just as well? (High = impossible without the all-pairs K₉ deck; low = generic.) | `design-principles.md` #1; `product-vision.md` "deck necessity" |
| **D2** | **Physical-handling viability** | Does it survive the double-faced-card reality — no card backs, no *involuntary* hidden-face bookkeeping (deliberate memory/deduction as the point of a game is fine)? | `physical-handling.md` checklist; `design-principles.md` #2–#3 |
| **D3** | **Flipping load-bearing** | Does flipping create real decisions, reversals, or threats, or is it incidental? | `design-principles.md` #4 |
| **D4** | **Pair-uniqueness load-bearing** | Does "every pair exactly once" do real work (deduction, shrinking lie-space, denial)? | `design-principles.md` #5; `deck-structure.md` |
| **D5** | **Distinctness** | Does it create an experience the other games don't already cover? | `product-vision.md` "distinctness"; `design-principles.md` #6 |
| **D6** | **Gap-filling** | Does its player count / time / complexity / mood fill a useful hole? | `product-vision.md` "gap-filling"; `design-principles.md` #7 |
| **D7** | **Teachability** | Can it be explained cleanly and slot into a sensible learning order? | `product-vision.md` "teachability"; `design-principles.md` #8 |

### The 1–10 scale anchors

Every dimension uses the same anchored scale, so scores are comparable across games. Scores are integers.

| Band | Label | Meaning |
|---|---|---|
| **9–10** | **Load-bearing / exemplary** | The dimension is a defining strength; removing it would break the game or its place in the collection. |
| **6–8** | **Solid** | Clearly present and positive, with only minor caveats. |
| **4–5** | **Mixed** | Works, but with a real, named weakness or only partial reliance on the property. |
| **1–3** | **Weak** | The dimension is a liability or essentially absent (an ordinary deck would do; flipping is cosmetic). |

A score of 5 or below must name the specific weakness in its justification, never a generic remark.

### Source documents feeding the audit

Scores and findings are evidenced from the existing corpus, not invented:

- **Canonical index & coverage** — [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md): tiers, selectors, coverage tables, recorded first-table questions.
- **Per-game rules & reasoning** — each game's `<GAME>_rulebook.md` and, where it exists, `<GAME>_design_analysis.md` (balance numbers, sim results, handling notes).
- **Concepts & status notes** — [`NEW_GAME_CONCEPTS.md`](NEW_GAME_CONCEPTS.md): "key deck property used" and recorded first-table questions.
- **OUROBOROS post-mortem** — `Ouroboros/OUROBOROS_design_analysis.md`: the recorded cut reasons and design lessons (confronted in §4).
- **Steering notes** — `.kiro/steering/` (`design-principles.md`, `physical-handling.md`, `product-vision.md`, `deck-structure.md`, `repository-structure.md`): the rubric, tier semantics, handling constraints, and OUROBOROS lessons the audit applies but does not redefine.

---

## §2 · Per-game rubric scorecards

One scorecard per live game: seven D1–D7 scores (integers 1–10, anchored per §1) with a justification that cites a specific deck property, handling technique, or coverage fact; any score ≤5 names the specific weakness. Each block records the game's maturity tier and its faithfully reproduced first-table questions. The cross-game summary matrix follows the individual scorecards.

> *Scoring is complete: all ten live games are scored across Tiers 1–3 below, and the cross-game summary matrix at the end of this section gathers every score in one comparison table.*

### Tier 1 · Complete (sim-tuned, rulebook final)

The two benchmark games. Per `product-vision.md`, they represent ~45k simulated games of investment and are **not** to be casually re-tuned or re-skinned; any change needs strong evidence and explicit owner sign-off.

---

### TRIGON  ·  Tier 1 (Complete)
*2–4 players · ~15–25 min · tactical grid (capture engine)* — folder `Trigon/` ([rulebook](Trigon/TRIGON_rulebook.md) · [analysis](Trigon/TRIGON_design_analysis.md))

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 8/10 | Physically impossible on an ordinary deck: the core decision is *which of a card's two faces to expose*, and the 2/3/4-player turn counts (18/12/9) rely on 36 dividing evenly — a property of the 36-card deck only (`deck-structure.md`, "even divisibility 2,3,4,6 → 36 only"). Held back from 10 because it leans on double-faced-ness and 36-divisibility, not on the all-pairs combinatorics itself (see D4). |
| Physical-handling viability (D2) | 9/10 | Exemplary open-state handling: the whole game lives on a 3×3 grid where every card shows exactly one **public** face and the deck-top is declared public, so required state is visible, not buried (`physical-handling.md` "open / perfect information"). ~23,000 sims asserted card conservation (grid+scores+removed+deck = 36) and termination every game. No constantly-needed hidden state. |
| Flipping load-bearing (D3)       | 8/10 | Flipping is the engine's conversion verb: Sun/Moon/Nova/Aurora abilities flip cards, flips re-charge cards and can complete alignments mid-chain, and choosing a placement face is a turn-one decision. Caveat (why not 9): the design analysis (§5, H5) shows skilled play activates only **0.24 abilities/turn** — flipping is decisive-when-used rather than constant. |
| Pair-uniqueness load-bearing (D4)| 3/10 | **Weakness:** the capture engine matches *like symbols* in a line and depends on even divisibility, not on "every pair exactly once." The design analysis (§7) states the deduction layer that uniqueness would enable is "untested" and unmodelled; the Overview's "pair uniqueness as deduction engine" row pointedly omits TRIGON. A deck of repeated symbols would align identically. |
| Distinctness (D5)                | 7/10 | The flagship neutral-board capture puzzle — "closer to a perfect-information abstract with one secret" (TURNCOAT analysis §7). Caveat: it shares the symbol-ability grid engine with TURNCOAT (Overview coverage "Symbol abilities / grid engine: TRIGON, TURNCOAT"); distinct in *feel* (indirect geometric capture) but not in machinery. |
| Gap-filling (D6)                 | 7/10 | Anchors the 2–4P / ~15–25 min / Medium tactical-engine slot and is the deck's teaching benchmark (#2 in the Overview learning order). Caveat: it occupies the same player-count/time/complexity cell as TURNCOAT per the Overview coverage tables, so the slot is doubled. |
| Teachability (D7)                | 6/10 | One clean reference table, a single 3×3 board, and a "Calm Skies" no-wild variant staged for first teaches. Caveat: nine distinct symbol abilities plus the charging-vs-recharging rule is a real load — the analysis (§7) lists "do new players grasp charging vs re-charging within one game" as an open first-table question. |

**First-table questions:** None are recorded in `COLLECTION_OVERVIEW.md` or `NEW_GAME_CONCEPTS.md` (both treat TRIGON as a finished benchmark rather than a game awaiting its first table). The game's own design analysis (§7) does record recommended first live tests, reproduced faithfully: (1) does a capture every ~5 turns feel exciting or exhausting at ~19 cards/game; (2) does anyone use Aurora; (3) is the "active player captures everything" rule legible and dramatic, or does it feel like theft; (4) do new players grasp charging vs. re-charging within one game.
**Recommendation:** Leave alone — benchmark. *Tier 1; no re-tune or re-skin proposed, so no owner sign-off is required. Per `product-vision.md`, any future change would need strong evidence and explicit owner sign-off.*

---

### TURNCOAT  ·  Tier 1 (Complete)
*2–4 players · ~15–25 min · allegiance grid (same engine as TRIGON)* — folder `Turncoat/` ([rulebook](Turncoat/TURNCOAT_rulebook.md) · [analysis](Turncoat/TURNCOAT_design_analysis.md))

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 8/10 | Built on a property unique to this deck: every card carries **two** symbols, so "each card serves two masters" makes allegiance possible, and the snake-draft leans on each sign marking exactly **8 cards** (its degree in K₉, `deck-structure.md`). Turn counts again use 36's even divisibility. Held to 8 for the same reason as TRIGON: it exploits the edge/two-faces property, not all-pairs uniqueness (see D4). |
| Physical-handling viability (D2) | 9/10 | Allegiance lives on the **visible** face, so loyalty is fully public and verifiable at a glance — no hidden-face memory burden (`physical-handling.md` "orientation/visible state"; "claim verifiable on demand"). ~22,000 sims asserted card conservation (grid+piles+removed+deck = 36) and termination. Only the Eye peek touches hidden faces, and it is a one-off reveal, not tracked state. |
| Flipping load-bearing (D3)       | 9/10 | Exemplary: flipping **is** the game's central aggressive verb — "flip an agent and they defect." The analysis (§4) treats "the flip is the wild" as the master balance lever and democratises it across five signs in v1.2; skilled play flips ~22.6 times/game and activates **1.24 abilities/turn**. Removing flipping would remove the game. |
| Pair-uniqueness load-bearing (D4)| 3/10 | **Weakness:** the allegiance economy uses the edge/two-masters property and per-sign scarcity (8 cards each), but does no work with "every pair exactly once" — there is no deduction registry. The Overview's "pair uniqueness as deduction engine" row omits TURNCOAT; the game would run on non-unique sign pairings. |
| Distinctness (D5)                | 7/10 | A genuinely different experience from TRIGON despite the shared engine: directed, personal conflict (~30 named conflict verbs/game vs TRIGON's indirect capture, analysis §7) and the bury-your-own banking loop. Caveat: it shares the grid ability engine with TRIGON (Overview coverage "Symbol abilities / grid engine"). |
| Gap-filling (D6)                 | 6/10 | Fills the **confrontation/allegiance mood** TRIGON leaves open (Overview "Flipping as defection/denial: TURNCOAT, THE COUNCIL"). Caveat: it duplicates TRIGON's exact player-count/time/complexity cell (2–4P, ~15–25 min, Medium) in the Overview coverage tables, so it fills a mood gap rather than a structural one. |
| Teachability (D7)                | 6/10 | Eased by being taught third in the learning order — "same engine, now personal" — so the ability engine transfers, and preset teams skip the draft on a first game. Caveat: it stacks allegiance, covering, banking, and a draft on top of nine sign abilities, and the analysis (§8) flags "does the bury-your-own loop teach itself" as an open question — the heavier teach of the two benchmarks. |

**First-table questions:** None are recorded in `COLLECTION_OVERVIEW.md` or `NEW_GAME_CONCEPTS.md` (both treat TURNCOAT as a finished benchmark). The game's own design analysis (§8) records recommended first live tests, reproduced faithfully: (1) is one activation per turn exciting or exhausting over 18 turns; (2) does the bury-your-own loop teach itself within a game, or does "covering rivals gifts them points" need a harder warning; (3) does Mask feel like a fun strong pick or a must-pick; (4) Allied Houses versus free-for-all at four.
**Recommendation:** Leave alone — benchmark. *Tier 1; no re-tune or re-skin proposed, so no owner sign-off is required. Per `product-vision.md`, any future change would need strong evidence and explicit owner sign-off.*

---

### Tier 2 · Sim/maths-validated — needs first table test

The three games whose numbers are checked but whose tables are not. Per `product-vision.md` and `playtesting.md`, the priority for every game here is its **first table test**, not more simulation — "a first playtest of an untested game outranks further simulation of an already-validated one." Each recommendation below is therefore framed as a first table test built around the game's own recorded questions.

---

### TWELVE TRIALS  ·  Tier 2 (Sim/maths-validated — needs first table test)
*1–2 players (+2–5 co-op) · ~15 min · solo/co-op open-information puzzle* — folder `Twelve Trials/` ([rulebook](Twelve%20Trials/TWELVE_TRIALS_rulebook.md) · [analysis](Twelve%20Trials/TWELVE_TRIALS_design_analysis.md))

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 10/10 | The win condition *is* the deck's own combinatorics: the 36 cards are the edges of K₉, which partition into 12 triangles in exactly **840** ways (Steiner triple systems), and the game is the search for the cheapest such almanac (analysis §2). Triangle partitions exist *only* at 7 and 9 symbols (`deck-structure.md`, "Steiner triple / triangle partition"); no ordinary deck has this structure to find. |
| Physical-handling viability (D2) | 9/10 | Exemplary, and designed explicitly against the OUROBOROS post-mortem: **nothing is hidden** — any card may be examined and returned as found, and the only tracked state is a flip, marked by rotating the card **sideways** (player-added, like tapping; no printed marks, no orientation leak into JANUS/FALSE FACE — analysis §4). All scoring and decisions read off visible faces. The one open risk is verification *flow*, not hidden state (see D7), so it stays a first-table question, not a handling bug. |
| Flipping load-bearing (D3)       | 9/10 | Flipping is literally the cost function: **your score is the number of sideways (flipped) cards**, lower is better, and the "exactly one flip per broken trio — never two" law (analysis §2; clockwise/anticlockwise mismatches sum to 3) is the entire skill surface. Listed under the Overview's "flipping as the core action" row. Held from 10 only because flipping is the *cost* to minimise rather than an interactive weapon. |
| Pair-uniqueness load-bearing (D4)| 8/10 | "Every pair exactly once" guarantees the puzzle's integrity: a claimed trio is valid because its three hidden faces are the same three symbols again — "there are no impostor trios" (rulebook), which holds precisely because each pair sits on exactly one card. Solid rather than load-bearing-maximal because the property does *structural/partition* work (the Overview files it under "algebraic structure", not "pair uniqueness as deduction engine") — there is no lie-space or denial layer. |
| Distinctness (D5)                | 9/10 | The collection's only **solo / quiet** game (Overview "By genre / mood") and the only one that exposes the deck's algebraic structure from the inside — #4 in the learning order, "see the deck's mathematical structure from the inside." Succeeds OUROBOROS in the solo slot without repeating its sins. |
| Gap-filling (D6)                 | 9/10 | The **only 1-player game** in the collection (Overview "By player count" — the lone ✓ in column 1) and the only post-setup-no-randomness open puzzle, plus a co-op mode. Fills the solo/puzzle hole outright. (That it is the *sole* solo game is itself a coverage thinness, examined in §3/§4 — but as a filler of the slot it is unambiguous.) |
| Teachability (D7)                | 7/10 | Helped by a clean pitch ("nothing is hidden"), a ~15-min length, and a **First Trial** tutorial that prints one almanac so beginners learn the trio shape and the one-flip law before facing the search (rulebook; analysis §5). Caveat: the real game's depth — that the skill is *choosing among 840 almanacs*, not cheaply fixing trios — is subtle and admittedly invisible to players (analysis §4), and the trio-verification flow is untested for fiddliness. |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` (echoed in analysis §4): does a thoughtful first game land near 7 flips? Does the trio-verification flow feel fiddly? Does the 840-almanac depth reveal itself or stay invisible?
**Recommendation:** Run the first solo table test, timed against those three recorded questions — watch where a thoughtful first solve lands (near 7 → tiers hold; clustering at 5 → compress them, per analysis §4), whether examine-three-cards verification drags, and whether a player feels the "unpick an early lock" moment. *Tier 2; a first table test takes priority over building a human-level bot or further solver runs (`playtesting.md`).*

---

### TURNOVER  ·  Tier 2 (Sim/maths-validated — needs first table test)
*3–6 players · ~10 min · party shedding race · v1.1 (~60k games)* — folder `Turnover/` ([rulebook](Turnover/TURNOVER_rulebook.md) · [analysis](Turnover/TURNOVER_design_analysis.md))

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 7/10 | The match-and-turn action needs double-faced cards: you match the target, then **turn the card over** so its other symbol becomes the next target — "every card in your hand is an exit door from the current symbol to one specific other" (rulebook FAQ), impossible with one-faced cards. Held to 7 because it leans on double-faced-ness plus per-symbol scarcity (8 cards each) and 36's clean deal sizes, not on the all-pairs combinatorics itself (see D4). |
| Physical-handling viability (D2) | 9/10 | Exemplary, and a deliberate OUROBOROS fix: the original HOT POTATO PAIRS tracked the pile's *buried* faces from memory, "the rule died with OUROBOROS"; v1.1's match-and-turn puts **every constraint on the visible top face**, the well sits face-up, and the pile's turned history is public — "card-counting a skill of attention, never recall" (rulebook footnote). ~60k sims, zero stalls. |
| Flipping load-bearing (D3)       | 9/10 | The turn **is** the deck's signature flip and the core verb — every play changes the target by flipping the just-played card, and chaining two flips in a turn is the central tactical choice ("chaining burns the exact bridges you'll wish you had"). Listed under the Overview's "flipping as the core action" row. |
| Pair-uniqueness load-bearing (D4)| 4/10 | **Weakness:** the race runs on double-faced-ness and per-symbol *scarcity* (eight cards carry each symbol → countable "safe targets"), **not** on "every pair exactly once." There is no deduction registry or shrinking lie-space, and the Overview's "pair uniqueness as deduction engine" row pointedly omits TURNOVER — a double-faced deck with repeated pairings would play almost identically. |
| Distinctness (D5)                | 9/10 | The collection's only **party / fast** game and only shedding race (Overview "By genre / mood"); nothing else delivers a loud ~10-minute filler. |
| Gap-filling (D6)                 | 9/10 | Fills the fast-filler hole cleanly: the **only ~10-min game** (Overview "By play time"), among the lightest weights (Overview "By complexity": Light, ages 8+), and one of the few reaching a 6-player table (Overview "By player count"). |
| Teachability (D7)                | 9/10 | The deck's on-ramp: **#1 in the learning order** — "learn the deck's flipping feel in 10 minutes, no abilities to track" — taught in one sentence (match the symbol, turn it over, empty your hand). The only added rules are the chain limit and the "Turnover!" announce, both light. |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md`: is announce-rule policing fun? Does chaining feel as bridge-burning as the maths says? (Analysis §5 notes the catch-the-forgetter mini-game is "untested by construction" — the sim treated the announce rule as always observed.)
**Recommendation:** Run a party table test at 5–6P targeting exactly those two questions — whether catching a player who forgets to announce "Turnover!" is fun or fussy, and whether spending a chain genuinely *aches* later as the maths predicts. *Tier 2; the balance questions are already closed by ~60k sims (analysis §3–§4), so the next step is the table, not more simulation (`playtesting.md`).*

---

### CROSSROADS  ·  Tier 2 (Sim/maths-validated — needs first table test)
*2 players · ~20 min · perfect-information abstract route duel · v1.1 (sim-tested)* — folder `Crossroads/` ([rulebook](Crossroads/CROSSROADS_rulebook.md) · [analysis](Crossroads/CROSSROADS_design_analysis.md))

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 10/10 | Built straight on pair-uniqueness: each card is **the only road between its two cities**, so keeping a card "removes the only direct road between [those cities] from the world" (rulebook) — surgical denial impossible on any deck where edges repeat. The board itself is the deck: the **eight symbol-9 cards become the cities** (`deck-structure.md`, "special role of symbol 9"), solving the "board with no board" problem from within the deck. |
| Physical-handling viability (D2) | 9/10 | Open / perfect information with self-reading state: a road **points at the city its visible face names** (visible face = destination, "no memory, no ambiguity"), and the eight shared flips are paid by **dimming** a city — rotating a city card 90°, a glanceable, countable orientation marker the deck supplies for free (`physical-handling.md` "orientation as state"). No hidden state. Held from 10 only because "does dimming read at a glance" is itself an open first-table question. |
| Flipping load-bearing (D3)       | 9/10 | Flipping a built road reverses its one-way direction — the heart of the tempo war — and the **eight Signal Fires flips are the whole endgame** ("who will get the last flip?", "the last flip is the largest"). Simulation proved flipping so central that *unlimited* flips never terminate (100% of v1.0 duels looped — analysis §3), which is why the shared pool exists. |
| Pair-uniqueness load-bearing (D4)| 10/10 | Maximal and exact: 28 roads exist, you hold 14, "**your rival's hand is exactly the rest**" — perfect deduction straight from every-pair-once, and every kept card is a unique edge deleted from the map. Listed in the Overview's "pair uniqueness as deduction engine" row; the rulebook calls hidden information nil after the deal. |
| Distinctness (D5)                | 9/10 | The collection's only **head-to-head abstract** — "the collection's chess" (Overview "By genre / mood"), the only perfect-information 2P duel, and the only game that constructs its own board from the symbol-9 cards. A clearly singular experience. |
| Gap-filling (D6)                 | 8/10 | Fills the perfect-information-abstract mood that nothing else occupies. Caveat: the 2-player *count* is shared with FACE VALUE and the 2–4P engine games (Overview "By player count"), so what it uniquely fills is the abstract/duel **mood**, not an empty player-count slot — solid rather than maximal gap-fill. |
| Teachability (D7)                | 6/10 | A ~20-min duel, but a genuinely heavier teach: build-with-facing, flip-with-**ko**, the Signal Fires pool, contracts-as-kept-cards scored by directed reachability either way, and the pie-rule start all interact. Mitigated by the **Caravans** variant, explicitly offered as a direction-blind "good first game", and by self-reading roads — but the ko rule and directed-route scoring are real first-game friction. |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` (echoed in rulebook footnote and analysis §5): does eight flips ache properly? Does dimming read at a glance? (Analysis §5 adds a watch-item: whether Caravans wants the pool at all, since flips don't affect undirected connectivity.)
**Recommendation:** Run the first 2P duel targeting those questions — whether the eight shared flips feel scarce enough to ache (the bot evidence is myopic about hoarding, analysis §5), and whether dimmed cities read at a glance as the remaining-flip counter. *Tier 2; termination and seat-balance are already settled by simulation (the shared pool and pie rule — analysis §3–§4), so the priority is the table, not more sim runs (`playtesting.md`).*

---

### Tier 3 · Rulebook complete — untested at the table

Games with full rules and **zero plays**. Per `product-vision.md` and `playtesting.md`, the priority for every game here is its **first playtest**, framed around the test-focus questions already recorded for it. None of the three below has a `_design_analysis.md` or a simulator — each is scored from its rulebook alone, so **D2 (physical-handling viability) is marked "un-simmed; handling unverified at the table"** rather than given a confident handling score (per the design's missing-evidence rule). This group A covers JANUS, FALSE FACE, and THE UNPLAYED PAIR.

---

### JANUS  ·  Tier 3 (Rulebook complete, untested)
*2–4 players · ~20 min · co-operative half-seen-hand deduction · 7-symbol subset (21 cards)* — folder `Janus/` ([rulebook](Janus/JANUS_rulebook.md) · no design analysis yet)

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 9/10 | Physically impossible on an ordinary deck: the engine is the **fanned hand showing opposite faces to opposite sides of the table** (concepts "key deck property used") — a held card shows *you* one symbol and the table its *different* partner, which needs a double-faced, backless card (a normal card held backward leaks only one bit, not a second symbol). The lock-check (two pillars sharing the same buried X = a triangle) then rides on every-pair-once. Held from 10 only because it runs on the 7-symbol K₇ subset rather than needing all 36. |
| Physical-handling viability (D2) | 5/10 | **Un-simmed; handling unverified at the table.** **Weakness:** concealment depends on the policed sacred rule "never look at the outward face of a card in your fan" — exactly the fragile anti-pattern `physical-handling.md` singles out ("hidden hands that the holder can't help seeing… JANUS makes this work only with an explicit, policed 'never inspect your own face' rule — the exception that proves the cost"). A single accidental glance permanently and irreversibly leaks a face, and nothing physical enforces the rule. The v1.1 face-down deal/refill protocol and open archive/keystones mitigate, but the core concealment is self-policed and untested — the most handling-fragile game in the collection. |
| Flipping load-bearing (D3)       | 5/10 | **Weakness:** flipping is *not* a live reversal/denial verb here. The two-faced-ness manifests as a **static asymmetry** (your side vs the table's) plus a one-time "my face / your face" commitment when raising a pillar; once placed, a card is never flipped back as a tactic. The lock-check flip is a verification reveal, not a player decision. Compared with TURNOVER/CROSSROADS (flip = the core tempo weapon), flipping in JANUS is a placement choice, not an ongoing dynamic. |
| Pair-uniqueness load-bearing (D4)| 9/10 | Near-maximal and exact: because every pair exists exactly once, a **single omen reading fully identifies a card** (the receiver knows their side; the unique partner is forced), and "the archive, the locked gates, the keystones, and every omen reading all chip away at what each buried face can possibly be." Each symbol lives on exactly 6 cards (K₇) → late-game faces are deducible to certainty. Listed in the Overview's "pair uniqueness as deduction engine" row. Held from 10 because early-game deduction is still probabilistic, not the total determinism of CROSSROADS. |
| Distinctness (D5)                | 9/10 | The collection's **only co-operative game** and its only "co-op, no talking" entry (Overview "By genre / mood": Co-op → JANUS alone). A Hanabi-like hint discipline but with *exact* deduction (one hint fully identifies). Nothing else in the collection delivers the half-seen-hand co-op experience. |
| Gap-filling (D6)                 | 9/10 | Fills the **co-operative mood outright** — the lone ✓ for co-op in the Overview genre/mood table — at 2–4P / ~20 min / Medium. Caveat: the 2–4P / ~20-min cell is shared with the engine games and other ~20-min titles (Overview "By play time"), so what it uniquely fills is the *co-op mood*, not an empty player-count or time band. |
| Teachability (D7)                | 5/10 | **Weakness:** the hardest teach of the group. The legal/illegal **communication grammar** (a whole rulebook section of "may say / may not say" examples, plus reading wince-and-pause tells as illegal) must be policed socially or "the game collapses into one person reading another's cards aloud," and "hint grammar ease of first game" is itself an unanswered recorded question; layered on the sacred no-self-inspection discipline, the omen economy, and setup validation. The Apprentice variant (3 gates, open talk) eases the on-ramp but not the core protocol. |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` ("Test focus: omen economy pacing; hint grammar ease of first game") and `NEW_GAME_CONCEPTS.md` ("Next: table test the omen economy"). The rulebook's own recorded tuning order is reproduced too: starting omens (4), strike count (3), then fan sizes.
**Recommendation:** Run the **first co-op table test** (start at the Apprentice ramp: 3 gates / 4 omens, then 4 gates) targeting those recorded questions — does the omen economy pace well (never deadlocking, never trivial), and can a first table absorb the hint/communication grammar without accidental face-leaks or quarterbacking. *Tier 3 (Rulebook complete, untested); a first playtest of the information protocol takes priority over any further rule tuning or simulation (`playtesting.md`).*

---

### FALSE FACE  ·  Tier 3 (Rulebook complete, untested)
*3–6 players · ~20 min · bluffing / hand-shedding against a public pair-registry · full 36-card deck* — folder `False Face/` ([rulebook](False%20Face/FALSE_FACE_rulebook.md) · no design analysis yet)

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 9/10 | Built on pair-uniqueness: "there is exactly one Moon/Crown in the world," so a claim about a hidden face **forges a specific, unique object** that someone may be holding, and the lie-space provably shrinks (concepts "every lie about a hidden side is eventually falsifiable"). The registry kills 6–12 *named* pairs publicly; each symbol on exactly 8 cards makes lies countable. Held from 10 because the shed-by-bluffing skeleton echoes a normal-deck bluff game (Cheat/BS) — K₉ supplies the *verifiable shrinking* lie-space rather than the whole shell. |
| Physical-handling viability (D2) | 7/10 | **Un-simmed; handling unverified at the table.** Designed to a handling pattern `physical-handling.md` endorses: **claim-and-challenge** (the hidden face is verified on demand by flipping) over a **public oriented ledger** whose row of visible faces *is* the history, so "the only remembered state is the newest claim, repeatable on demand — a deliberate constraint from the OUROBOROS post-mortem"; the registry is openly examinable. Risk is low by design, but pacing/ledger-swing handling is untested, so no confident higher score. |
| Flipping load-bearing (D3)       | 6/10 | Solid: each card shows one symbol and **hides its unique partner — the lie object** — and flipping a hand card to its other face to meet the required symbol is an always-legal, frequent play that sets up what you can claim; the challenge resolves by flipping the played card. Caveat: flipping is face-*selection* for the claim and a reveal mechanic, not a reversal/denial weapon, so it is load-bearing for the bluff but not the tempo engine. |
| Pair-uniqueness load-bearing (D4)| 10/10 | Maximal and exact: the whole "finite lies" engine is arithmetic on every-pair-once — "the registry kills 6–12 pairs at setup… every challenge flips a card and kills its pair… the good lies must thread the few pairs still unaccounted for," and "count the eights" (each symbol on exactly 8 cards) can prove a claim impossible. Listed in the Overview's "pair uniqueness as deduction engine" row; remove uniqueness and the game has no shrinking lie-space. |
| Distinctness (D5)                | 7/10 | A distinct *multiplayer* bluff: 3–6P hand-shedding with a public kill-registry and walk-into-a-challenge tension. Caveat: it shares the **bluffing mood** with FACE VALUE (Overview "By genre / mood": Bluffing → FALSE FACE, FACE VALUE) — distinguished by player count (3–6P vs heads-up) and the shedding/registry structure, but the niche is doubled (adjudicated in §3). |
| Gap-filling (D6)                 | 7/10 | Fills the **social-bluffing slot that scales to 5–6 players** — one of the few games reaching a 6-player table (Overview "By player count") — at Light–Medium weight. Caveat: the ~20-min band is well populated (JANUS, CROSSROADS, and FACE VALUE-adjacent titles share it per Overview "By play time"), so it fills a player-count/mood hole more than a time-band one. |
| Teachability (D7)                | 7/10 | Clean core taught in a sentence — play a card, claim its hidden face (truth or lie), challenge to force a reveal, or decline — at Light–Medium weight (Overview "By complexity"), with an **Apprentice Forgers** first-game variant that shrinks challenge swings to 3 cards. Caveat: the skill ("price a lie", when to challenge) is subtle for first-gamers — the recorded test-focus question "whether first-game players can price a lie." |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` ("Test focus: ledger pacing; whether first-game players can price a lie") and `NEW_GAME_CONCEPTS.md` ("Next: table test ledger pacing"). The rulebook's own recorded first-playtest questions are reproduced too: ledger swing size (whole-row vs Apprentice), decline rate, and whether 3P has enough challenge pressure.
**Recommendation:** Run the **first table test** (consider the Apprentice Forgers swing for a teaching table, then full ledger), watching exactly those recorded questions — does the ledger pace well or swing too hard, can first-game players price a lie, and does 3P generate enough challenge pressure or need the bigger counts. *Tier 3 (Rulebook complete, untested); the first playtest outranks any further rule tuning or simulation (`playtesting.md`).*

---

### THE UNPLAYED PAIR  ·  Tier 3 (Rulebook complete, untested)
*3–5 players · ~25 min · trick-taking whodunit / deduction · full 36-card deck* — folder `The Unplayed Pair/` ([rulebook](The%20Unplayed%20Pair/UNPLAYED_PAIR_rulebook.md) · no design analysis yet)

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 8/10 | Needs *both* deck properties: double-faced-ness drives **follow-by-either-face** ("flipping a card to follow is the game's signature move… mandatory if that's the only way you can follow") and the trick-end hidden-face reveal; pair-uniqueness makes "void in a suit" *provable* and the **one removed card fully identifiable by elimination** (concepts). More deck-properties in play than TURNOVER. Held from higher only because the underlying trick-scoring skeleton is a generic genre a normal deck supports — K₉ supplies the flip-to-follow and the whodunit, not the trick frame itself. |
| Physical-handling viability (D2) | 7/10 | **Un-simmed; handling unverified at the table.** Deliberately built against the OUROBOROS post-mortem: "v1.0 resolves all hidden information through the public **trick-end reveal**, keeps every revealed card open for inspection (morgue, won tricks), and asks players to remember nothing… it asks you to reason." Renege "polices itself" the moment a slough flips. Strongest handling design of the three on paper, but the flip-every-card reveal *flow* (recorded question: "theatre or admin?") and renege detection are untested — so no confident higher score. |
| Flipping load-bearing (D3)       | 8/10 | Flipping is a core, recurring decision: **flip-to-follow** is "the game's signature move," and *which partner you burn vs keep* by flipping is half the craft; the trick-end flip then reveals the rank that decides the trick and feeds deduction. Listed indirectly under the deduction-engine games. Held from 9–10 because flipping is a follow-and-reveal mechanic, not an aggressive reversal/denial weapon aimed at opponents. |
| Pair-uniqueness load-bearing (D4)| 10/10 | Maximal and exact: "**ties are impossible** — every follower hid a different partner of the led symbol, because every pair exists exactly once," and the win condition is identifying the single missing card by elimination ("every card you see strikes exactly one candidate off the list"); each symbol on exactly 8 cards makes voids provable arithmetic. Listed in the Overview's "pair uniqueness as deduction engine" row. Remove uniqueness and both the no-tie rule and the whodunit collapse. |
| Distinctness (D5)                | 9/10 | The collection's **only trick-taking game** (Overview "By genre / mood": Trick-taking → THE UNPLAYED PAIR alone), and a trick-taking *whodunit* — a singular fusion nothing else approaches. |
| Gap-filling (D6)                 | 8/10 | Fills the **trick-taking genre outright** (the only one) and the 3–5P mid-count at ~25 min / Medium. Caveat: the ~25-min band is shared with THE COUNCIL (Overview "By play time"), so the time band is doubled even though the genre slot is uniquely filled. |
| Teachability (D7)                | 6/10 | Builds on a **familiar trick-taking base** and offers a **Quiet Round** first-game variant (no calls, pure trick-taking with reveals) as a clean on-ramp. Caveat: the novel twists stack — follow-by-either-face, the trick-end reveal ritual, call timing/scoring, and renege — and "hidden-face ranking rule simplicity" is a recorded open question (the rank rule was already reworked once from a memory-based version per the OUROBOROS lesson). |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` ("Test focus: hidden-face ranking rule simplicity; 4P balance") and `NEW_GAME_CONCEPTS.md` ("Next: table test at 4P"). The rulebook's own recorded first-playtest questions are reproduced too: call payout curve (is +1/unled trick the right slope?), renege rate at 3P, and whether the reveal moment lands as theatre or admin.
**Recommendation:** Run the **first table test at 4P** (consider opening with the Quiet Round variant to teach the follow-by-either-face rhythm) targeting those recorded questions — is the reworked pip-rank reveal simple enough to read cleanly, does 4P balance well, does the call payout curve (+1 per unled trick) reward good timing, and does the reveal land as theatre rather than admin. *Tier 3 (Rulebook complete, untested); the first playtest at 4P outranks any further rule tuning or simulation (`playtesting.md`).*

---

### FACE VALUE  ·  Tier 3 (Rulebook complete, untested)
*2 players · ~15–20 min · heads-up bluffing / betting duel · full 36-card deck (pacing sim-checked, table-untested)* — folder `Face Value/` ([rulebook](Face%20Value/FACE_VALUE_rulebook.md) · [analysis](Face%20Value/FACE_VALUE_design_analysis.md))

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 8/10 | Built on two deck properties at once: **the shown face *is* the claim** — "you don't declare strength; you choose what to conceal" (analysis), impossible with one-faced cards — and **pair-uniqueness makes ties impossible** ("two duel cards can never match on both faces… there is always a winner", so no split-pot rules), with the lie-space shrinking publicly via the morgue + two open tallies + your hand. Listed in the Overview's "pair uniqueness as deduction engine" row. Held from higher because the raise/call/fold **betting skeleton is poker** (a normal deck runs it); K₉ supplies the verifiable claim and the shrinking count, not the wagering shell itself. |
| Physical-handling viability (D2) | 7/10 | **Un-simmed for handling; unverified at the table** (the pacing sim is pacing-only, "not balance", and touches no handling). Designed to endorsed patterns: **palms-commit** simultaneous reveal (shared with THE COUNCIL — `physical-handling.md` "palms-commit / simultaneous reveal"), a **public examinable dead-pair registry** (the 6-card morgue, both faces inspectable by either player) plus two open tallies, and explicitly "no hidden randomness after the deal… all tracked state visible". The duel card's hidden face stays pressed to the table and, on a fold, returns to hand **unrevealed**, so no hidden-face memory accrues. No confident higher score because the pacing/ledger-swing handling and the commit-reveal flow are untested. |
| Flipping load-bearing (D3)       | 5/10 | **Weakness:** there is no reversible flip verb here — unlike TURNOVER/CROSSROADS where flipping is the tempo weapon, a FACE VALUE card is **never flipped back as a tactic**. The double-faced property is used as a **one-time face-choice at commitment** (which symbol to show vs hide) plus face-choice on staked/escape cards; the only "flip" is the showdown/cold-read **reveal**, which is verification, not a player move. The shown-vs-hidden choice is genuinely the heart of the bluff, but flipping *as an in-play action* is static, not dynamic. |
| Pair-uniqueness load-bearing (D4)| 9/10 | Near-maximal and exact: every shown face has exactly **eight partners**, and "minus every pair in the morgue, minus every pair in either tally, minus every one you're holding" turns the **Cold Read** from "a 1-in-8 gamble" early into "arithmetic" late — the deduction engine is the count of remaining partners, which exists only because every pair sits on exactly one card. The no-tie rule (hidden pip, then visible pip) is also a direct consequence of every-pair-once. Held from 10 because the deduction layer is *optional and late* ("a gamble early, arithmetic late") rather than the total, immediate determinism of CROSSROADS. |
| Distinctness (D5)                | 7/10 | The collection's **only head-to-head bluffing game** (Overview "By genre / mood": Head-to-head bluffing → FACE VALUE alone) and its only 2P bluffing duel — a poker-style betting feel nothing else delivers. Caveat: it shares the **bluffing mood** with FALSE FACE (Overview "Bluffing → FALSE FACE, FACE VALUE"), distinguished by player count (heads-up vs 3–6P) and engine (betting vs shedding/registry) — the niche is doubled and adjudicated in §3. |
| Gap-filling (D6)                 | 7/10 | Fills "**the last empty cell in the bluffing row**" (analysis "collection fit") — 2P betting bluff at Light–Medium weight, the gap between CROSSROADS' perfect-information 2P duel and FALSE FACE's 3–6P bluff. Caveat: the 2-player *count* is already occupied by CROSSROADS and the engine games (Overview "By player count"), and the ~15–20-min band is well populated, so what it uniquely fills is the **2P-bluffing mood**, not an empty count or time slot. |
| Teachability (D7)                | 7/10 | Poker-shaped and light: raise / call / fold / cold read taught in a sentence, "the shown face is the claim" is the whole pitch, at Light–Medium weight (Overview "By complexity"), with a **Quick Draw** 21-card (symbols 1–7) shorter on-ramp. Caveat: the real skill — *pricing a lie*, folding-to-stay-hidden, and counting partners before a cold read — is subtle for first-gamers, which is exactly what the recorded first-table questions target. |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` ("Test focus: fold frequency; cold-read timing; whether acting last reads as the advantage it is"). The rulebook's own recorded first-playtest questions are reproduced too: does fold-to-stay-hidden get used, or do tables call everything; is the cold read attempted at the right frequency (rarely early, decisively late); does acting last feel like the advantage the maths says it is. (FACE VALUE has no separate status note in `NEW_GAME_CONCEPTS.md`'s numbered list.)
**Recommendation:** Run the **first heads-up table test** (consider opening with Quick Draw to teach the count quickly) targeting those recorded questions — whether folding-to-stay-hidden is actually used or tables call everything, whether the cold read fires at the right cadence (rare early, decisive late), and whether acting last reads as the predicted advantage. *Tier 3 (Rulebook complete, untested); pacing already passes ~4k-game sim checks (analysis), so the next step is the table, not more simulation (`playtesting.md`).*

---

### THE COUNCIL  ·  Tier 3 (Rulebook complete, untested)
*3–6 players · ~25 min · simultaneous negotiation / minority game · full 36-card deck* — folder `The Council/` ([rulebook](The%20Council/COUNCIL_rulebook.md) · no design analysis yet)

| Dimension | Score | Justification (cites a specific deck property / handling technique / coverage fact) |
|---|:---:|---|
| Deck-necessity (D1)              | 7/10 | Built on the **edge property** — "every card supports exactly one cause and **can defect to exactly one other**, and everyone can read both options off your card" (concepts "key deck property used": every commitment is reversible, but only to one specific alternative). A card *is* an edge between two symbols, so the threat space is the printed pair; index pips (1–9) supply issue values. Held to 7 because the underlying **lone-supporter minority game + open negotiation** shell is fairly generic and pair-uniqueness does only light work (see D4); it leans on the two-faces/edge property and pip values, not on all-pairs combinatorics. |
| Physical-handling viability (D2) | 7/10 | **Un-simmed; handling unverified at the table** (rulebook only — no `_design_analysis.md`, no simulator). Designed to endorsed patterns: the **palms-commit** simultaneous slap-down "replaces the face-down concealment this deck cannot have" (`physical-handling.md` "palms-commit / simultaneous reveal"), a card's only alternative is **public the moment it is committed** ("the threat was public the moment you slapped it down" — orientation/visible state, no hidden-face memory), and **all spent material stays public** in the discard row ("no memory"); tabled issues are re-examinable by anyone. No confident higher score because the simultaneous-commit + seat-order turncoat flow and stack-tracking are untested at the table. |
| Flipping load-bearing (D3)       | 9/10 | Exemplary: the **turncoat flip is the central verb** — "in seat order… each player may flip their committed card to its other face, defecting to the issue matching the new face." Listed in the Overview's "Flipping as defection/denial: TURNCOAT, THE COUNCIL" row. Flipping creates the whole reversible-promise tension ("promise the Crown and flip to the Moon — but only to the Moon"); late seats defect with better information and the Speaker rotation shares that power. Removing flipping removes the game. Held from 10 only because the flip is once-per-card-per-round and most threats "die unexecuted". |
| Pair-uniqueness load-bearing (D4)| 4/10 | **Weakness:** the minority/negotiation game runs on **pip values and the edge property**, not on "every pair exactly once". There is no deduction registry or shrinking lie-space, and the Overview's "pair uniqueness as deduction engine" row **omits THE COUNCIL**. The only counting it offers is the public discard row plus the 6P "issue deck empties exactly, so you can't count what was never dealt" wrinkle — minor, not load-bearing. A deck with repeated pairings would play almost identically. |
| Distinctness (D5)                | 8/10 | The collection's **only negotiation / betrayal game** (Overview "By genre / mood": Negotiation / betrayal → THE COUNCIL alone) — open table-talk, public promises, and printed-on-the-card treachery, a social experience nothing else delivers. Caveat: it shares the **social / negotiation** axis with FALSE FACE (Overview "Social / negotiation: THE COUNCIL, FALSE FACE"), but FALSE FACE is bluff-and-shed against a registry, not open multiplayer negotiation — distinct in kind (adjudicated in §3). |
| Gap-filling (D6)                 | 8/10 | Fills the **negotiation/social mood at high player counts** — 3–6P, one of the few games reaching a **6-player** table (Overview "By player count"), at ~25 min / Light ("No arithmetic, lots of talking", Overview "By complexity"). Caveat: the ~25-min band is shared with THE UNPLAYED PAIR (Overview "By play time"), so the time slot is doubled even though the negotiation mood and the 6P reach are uniquely filled. |
| Teachability (D7)                | 8/10 | Among the lightest teaches: commit one card to its visible issue, optionally defect to its one printed alternative, lone supporter takes the stack, sum pips after 4 rounds — graded **Light** in the Overview ("No arithmetic, lots of talking") with no per-symbol abilities and trivial scoring. Caveat: the *strategic* subtlety (causing a deadlock to harvest in round 4, abstention-as-threat, counting seats before promising) is deep, but the **rules** explain themselves quickly; gentler/variant ramps (The Whip, Backroom) exist. |

**First-table questions:** Reproduced faithfully from `COLLECTION_OVERVIEW.md` ("Test focus: kingmaking at 5–6P; pot arithmetic staying frictionless") and `NEW_GAME_CONCEPTS.md` ("Next: table test at 4–5P"). The rulebook's own recorded first-playtest questions are reproduced too: does 4 rounds feel one short; do deadlock stacks roll often enough to matter; is the Speaker rotation enough to balance flip order at 5–6P.
**Recommendation:** Run the **first table test at 4–5P** targeting those recorded questions — whether a losing player kingmakes at 5–6P, whether the pot/pip arithmetic stays frictionless, whether 4 rounds feels one short, whether deadlock stacks roll over often enough to matter, and whether the Speaker rotation balances flip order. *Tier 3 (Rulebook complete, untested); with no sim and zero plays, the first playtest outranks any further rule tuning or simulation (`playtesting.md`).*

---

### Cross-game summary matrix

Every score from the scorecards above, gathered into one table covering all ten live games. Values match each game's scorecard exactly. **Read down a column** to rank the games on a single dimension (e.g. which lean hardest on pair-uniqueness, D4); **read across a row** to profile one game's whole shape.

| Game | Tier | D1 | D2 | D3 | D4 | D5 | D6 | D7 |
|------|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| TRIGON | 1 | 8 | 9 | 8 | 3 | 7 | 7 | 6 |
| TURNCOAT | 1 | 8 | 9 | 9 | 3 | 7 | 6 | 6 |
| TWELVE TRIALS | 2 | 10 | 9 | 9 | 8 | 9 | 9 | 7 |
| TURNOVER | 2 | 7 | 9 | 9 | 4 | 9 | 9 | 9 |
| CROSSROADS | 2 | 10 | 9 | 9 | 10 | 9 | 8 | 6 |
| JANUS | 3 | 9 | 5 | 5 | 9 | 9 | 9 | 5 |
| FALSE FACE | 3 | 9 | 7 | 6 | 10 | 7 | 7 | 7 |
| THE UNPLAYED PAIR | 3 | 8 | 7 | 8 | 10 | 9 | 8 | 6 |
| FACE VALUE | 3 | 8 | 7 | 5 | 9 | 7 | 7 | 7 |
| THE COUNCIL | 3 | 7 | 7 | 9 | 4 | 8 | 8 | 8 |

*Dimensions: D1 deck-necessity · D2 physical-handling viability · D3 flipping load-bearing · D4 pair-uniqueness load-bearing · D5 distinctness · D6 gap-filling · D7 teachability (all on the 1–10 scale anchored in §1).*

---

## §3 · Collection gaps & overlaps

This section reads the four coverage tables in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md) as the empirical baseline and asks two questions of them: where is the collection **thin or empty** (the gap analysis below), and where do two or more games **crowd the same niche** (the overlap analysis that follows). It cross-references the Overview tables by name rather than reproducing them, per the "cross-reference, don't duplicate" rule in `repository-structure.md`.

### Gap analysis

Each of the four coverage dimensions is examined against its own Overview table. For every dimension the analysis names the **explicit missing band** (the specific player count, time band, weight, or mood) and cites the table it came from; a dimension found to be well covered is stated as such rather than dropped, so the reader knows it was examined and not merely skipped. All four dimensions are reported.

#### Player count — gap: solo (1 player) is served by a single game

*Source: the **"By player count"** matrix in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

Reading down the columns of the matrix: the **1-player column holds exactly one ✓ — TWELVE TRIALS** (its co-op mode aside). Columns 2 through 6 are all comfortably filled — 2P by six games (TWELVE TRIALS, JANUS, TRIGON, TURNCOAT, CROSSROADS, FACE VALUE), 3P and 4P by seven or eight games each, 5P by four (THE UNPLAYED PAIR, FALSE FACE, THE COUNCIL, TURNOVER), and 6P by three (FALSE FACE, THE COUNCIL, TURNOVER).

- **The named gap is solo play (1P):** the collection's *only* solo game is TWELVE TRIALS. If a player wants a quiet single-player session and TWELVE TRIALS does not suit the mood, there is no alternative. This is the structural thinness flagged in that game's §2 scorecard (D6: "that it is the *sole* solo game is itself a coverage thinness, examined in §3/§4"), and it is the niche OUROBOROS vacated when it was cut — taken up in the §4 re-evaluation.
- **Player counts 2–6 are adequately covered** and need no new game on player-count grounds alone; if anything they are *crowded* at 2–4P, which is the overlap question (§3 overlap analysis), not a gap.

#### Play time — gap: no genuine sub-10-minute filler, and nothing past ~25 minutes

*Source: the **"By play time"** table in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

Bucketing the table into bands shows the mid-range is saturated and both ends are thin:

- **Fast end (≤10 min):** **TURNOVER alone (~10 min)**. There is no game *below* ten minutes — no two-to-five-minute micro-filler for a between-games palate cleanser. The named gap is a **sub-10-minute filler besides TURNOVER**.
- **Middle (~15–25 min):** crowded — TWELVE TRIALS (~15), TRIGON and TURNCOAT (~15–25), JANUS (~20), FACE VALUE (~15–20), FALSE FACE (~20), CROSSROADS (~20). Adequately (over-)covered.
- **Long end (~25 min):** THE UNPLAYED PAIR and THE COUNCIL cap the collection at ~25 min. The named gap at this end is the **absence of any 30-minutes-plus, longer-arc game** — though, like the Heavy-weight gap below, this is plausibly a deliberate consequence of the project's "small, replayable games" vision (`product-vision.md`) rather than a hole to plug.

Both named bands (sub-10 min and 30+ min) are genuine empties in the table; the middle band is well covered.

#### Complexity — gap: no Heavy game (Medium is crowded)

*Source: the **"By complexity"** table in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

The table runs Light → Light–Medium → Medium, and **stops there — there is no Heavy row**:

- **Light:** TURNOVER, THE COUNCIL. **Light–Medium:** FALSE FACE, FACE VALUE. Both bands adequately covered.
- **Medium:** six games (TRIGON, TURNCOAT, JANUS, TWELVE TRIALS, THE UNPLAYED PAIR, CROSSROADS) — the collection's centre of mass, well covered to the point of crowding.
- **The named gap is Heavy:** there is no heavyweight, long-decision-tree game. Per the evaluation rubric's gap-filling criterion (`design-principles.md` #7) this is a real empty band, **but it is most likely a deliberate choice, not an oversight** — the product vision is explicitly to "build a varied collection of *small, replayable* games" (`product-vision.md`), and a 90-minute strategy game would cut against that identity and against the deck's fast-subset-selection strengths. Recorded here as examined: the Heavy band is empty *by design intent*, and filling it should not be a roadmap priority unless the vision changes.

#### Mood / genre — gap: co-operative play rests on a single game

*Source: the **"By genre / mood"** table in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

The mood table is the collection's broadest axis and is mostly well spread — solo/quiet (TWELVE TRIALS), head-to-head abstract (CROSSROADS), tactical engine (TRIGON, TURNCOAT), trick-taking (THE UNPLAYED PAIR), negotiation/betrayal (THE COUNCIL), bluffing (FALSE FACE, FACE VALUE), and party/fast (TURNOVER) are each represented. Two observations:

- **The named gap is co-operative play:** the **"Co-op, no talking" mood holds a single game — JANUS** (TWELVE TRIALS adds a co-op *mode*, but its identity is the solo puzzle). A table that wants a co-operative evening has exactly one true option, and JANUS is itself the most handling-fragile game in the collection (§2, D2 = 5). A second, sturdier co-op — ideally one not resting on the policed "never inspect your own face" rule — is the clearest mood-level gap.
- **A pure-luck / family-roll mood is absent, and that is correctly a non-gap.** Every game in the table rewards deduction, counting, or tactics; none is a pure-luck family game. This is *not* a hole to fill: the deck "rewards deduction and counting" (`physical-handling.md`), and a pure-luck game would fail the deck-necessity criterion (`design-principles.md` #1) — an ordinary deck would run it just as well. Recorded as examined and deliberately empty.
- The remaining moods are **adequately covered**; no other mood is a meaningful gap.

**Gap-analysis summary.** The actionable gaps, in the terms the Overview tables name them: (1) **solo (1P)** has only TWELVE TRIALS; (2) **sub-10-minute filler** has only TURNOVER, with nothing shorter; (3) the **Heavy** complexity band is empty but deliberately so; (4) **co-operative** mood has only JANUS. The 30+ min time band and the pure-luck mood are empty by design intent rather than by oversight. These feed the §4 OUROBOROS re-evaluation (the solo niche) and the §5 roadmap.

### Overlap analysis

An overlap is two or more live games occupying **substantially the same niche**. The detection method is a shared-niche scan across the four coverage axes used for gaps (player count, play time, complexity, mood/genre) **plus the deck-property axis** — the **"Coverage at a glance"** table in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md), which lists which games lean on which deck property. Games sharing a cell or adjacent cells on any axis are clustered, then for each cluster the analysis **names the games and the shared dimension**, **cites the Overview table** that reveals it, and **adjudicates** using the distinctness criterion from `product-vision.md`: a game earns coexistence only if it "create[s] an experience the other games don't already cover (genre, player count, length, mood, deck-property used)." A near-overlap that resolves on inspection is still reported, with its coexist verdict, so the reasoning is visible.

The scan surfaced **one genuine multi-axis overlap** (TRIGON ↔ TURNCOAT), **two single-axis mood overlaps** (FALSE FACE ↔ FACE VALUE; FALSE FACE ↔ THE COUNCIL), and **three near-overlaps that resolve on inspection** (CROSSROADS ↔ FACE VALUE; THE UNPLAYED PAIR ↔ THE COUNCIL; the five-game deduction-engine cluster). Each is adjudicated below.

#### TRIGON ↔ TURNCOAT — shared engine *and* shared count/time/complexity cell · **coexist** (the collection's one genuine multi-axis overlap)

*Sources: the **"Coverage at a glance"** table (row "Symbol abilities / grid engine: TRIGON, TURNCOAT"), plus the **"By player count"**, **"By play time"**, and **"By complexity"** tables in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

This is the collection's deepest overlap — the only pair that crowds on **four axes at once**. Both run the same symbol-ability grid engine (the deck-property table pairs them alone on that row); both sit at **2–4 players** (By player count), both at **~15–25 min** (By play time), and both at **Medium** weight (By complexity). No other pair coincides on more than two axes.

**Adjudication — coexist.** They clear the distinctness criterion on the one axis the coverage tables separate them by: **mood/feel**. TRIGON is an indirect, neutral-board capture puzzle ("closer to a perfect-information abstract with one secret"); TURNCOAT is directed, personal allegiance conflict with a bury-your-own banking loop (§2 TRIGON D5 = 7, TURNCOAT D5 = 7; ~30 named conflict verbs/game vs TRIGON's indirect capture). The "By genre / mood" table files the engine pair under "Tactical engine," but TURNCOAT also uniquely fills the "Flipping as defection/denial" niche (shared only with THE COUNCIL), which TRIGON does not. The shared engine is a **deliberate design** — the learning order teaches TURNCOAT third as "same engine, now personal" (§2 TURNCOAT D7) — not an accident to resolve. Both are **Tier 1 benchmarks** representing ~45k simulated games; per `product-vision.md` they are not to be re-tuned or re-skinned without strong evidence and owner sign-off, so even if one *wanted* to differentiate them further, the tier discipline forbids casual change. **No action** beyond recording that this cell is the collection's most doubled (the related gap-side observation — that 2–4P / Medium / ~15–25 min is crowded — is in the gap analysis above).

#### FALSE FACE ↔ FACE VALUE — shared bluffing mood and shared deduction-engine property · **coexist**

*Sources: the **"By genre / mood"** table (row "Bluffing: FALSE FACE, FACE VALUE") and the **"Coverage at a glance"** table (row "Pair uniqueness as deduction engine") in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

The two bluffing games share both the **bluffing mood** (the only two games on that mood row) and the **pair-uniqueness deduction-engine** deck-property (both score D4 = 10 / 9). This is a real single-axis-family overlap, flagged in both §2 scorecards (FALSE FACE D5 = 7; FACE VALUE D5 = 7, both noting "the niche is doubled").

**Adjudication — coexist.** They separate cleanly on **player count and engine**. FACE VALUE is a **heads-up (2P)** betting duel — raise/call/fold/cold-read poker shape — and uniquely fills the "Head-to-head bluffing" mood row (By genre / mood); FALSE FACE is a **3–6P** hand-shedding game against a public kill-registry, one of the few games reaching a 6-player table (By player count). A table choosing between them is choosing between a two-player betting duel and a party-scale shedding bluff — different experiences by count, structure, and feel. Both clear the distinctness bar; **no action**. (FACE VALUE's own design analysis frames itself as filling "the last empty cell in the bluffing row" — i.e. the 2P slot — rather than competing with FALSE FACE's multiplayer niche.)

#### FALSE FACE ↔ THE COUNCIL — shared social/negotiation axis at 3–6P · **coexist**

*Sources: the **"Coverage at a glance"** table (row "Social / negotiation: THE COUNCIL, FALSE FACE") and the **"By player count"** table in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md).*

The deck-property table pairs these two on the **"Social / negotiation"** row, and both reach the **3–6P** band (By player count), including the rare 6-player table. The shared social axis at overlapping counts is the candidate overlap.

**Adjudication — coexist (distinct in kind).** The shared "social" label covers two genuinely different experiences. FALSE FACE is **bluff-and-shed against a public pair-registry** — the social act is a claim-and-challenge over a shrinking lie-space (§2 FALSE FACE: deduction-engine D4 = 10). THE COUNCIL is **open multiplayer negotiation and printed-on-the-card betrayal** — table-talk, public promises, and the turncoat flip — and uniquely fills the "Negotiation / betrayal" mood row (By genre / mood), doing almost no pair-uniqueness work (§2 THE COUNCIL D4 = 4). One is a deduction-driven bluff; the other is a talk-driven minority/negotiation game. They share an axis label but not a niche; **no action**.

#### Near-overlaps that resolve on inspection

These clusters share a single axis but separate decisively on another; each is reported with its **coexist** verdict so the reasoning is on record.

- **CROSSROADS ↔ FACE VALUE — the only two strictly-2P-only games · coexist.** *Source: the **"By player count"** table.* Both are exclusively 2-player and both run ~15–20 min, so they share the heads-up count cell. But they are opposite in information model and mood: CROSSROADS is the collection's only **perfect-information abstract** ("the collection's chess," D4 = 10, D5 = 9, zero hidden information after the deal); FACE VALUE is a **hidden-information bluffing duel** (By genre / mood: "Head-to-head abstract" vs "Head-to-head bluffing" are separate rows). A player wanting a tense calculation duel and one wanting a poker-style bluff are not served by the same game. Coexist; the 2P count is shared but the experience is not.

- **THE UNPLAYED PAIR ↔ THE COUNCIL — shared ~25-min band and overlapping 3–5P counts · coexist.** *Sources: the **"By play time"** and **"By player count"** tables.* Both cap the collection at **~25 min** and overlap at 3–5 players. But they fill different mood rows outright — THE UNPLAYED PAIR is the only **trick-taking** game, THE COUNCIL the only **negotiation/betrayal** game (By genre / mood) — and lean on different properties (UNPLAYED PAIR D4 = 10 deduction vs COUNCIL D4 = 4 edge/pip play). The shared time band is the doubling already noted in each game's §2 D6 caveat; the genres do not compete. Coexist.

- **The deduction-engine cluster (JANUS · THE UNPLAYED PAIR · FALSE FACE · CROSSROADS · FACE VALUE) — shared deck-property, five distinct niches · coexist.** *Source: the **"Coverage at a glance"** table (row "Pair uniqueness as deduction engine").* Five games lean on the same load-bearing deck property — the largest cluster on any single axis. This is **intended, not an overlap to resolve**: the deck "rewards deduction and counting" (`physical-handling.md`), so a deduction spine is the collection's identity, and the five express it through entirely different moods and counts — co-op half-seen hands (JANUS), a trick-taking whodunit (THE UNPLAYED PAIR), a multiplayer shedding bluff (FALSE FACE), a 2P perfect-information route duel (CROSSROADS), and a heads-up betting bluff (FACE VALUE), each occupying a different genre/mood row. Sharing a deck-property is exactly the coherence the collection wants when the games are otherwise distinct; the distinctness criterion is met on mood, count, and engine. Coexist; **no action**.

**Overlap-analysis summary.** No game is a candidate to differentiate, park, or cut on overlap grounds. The one genuine multi-axis overlap — **TRIGON ↔ TURNCOAT** — is a deliberate, tier-protected "same engine, different feel" pairing that clears the distinctness bar on mood. The two mood-family overlaps (**FALSE FACE ↔ FACE VALUE**, **FALSE FACE ↔ THE COUNCIL**) resolve on player count and engine. The remaining near-overlaps separate cleanly on information model or genre, and the five-game deduction-engine cluster is the collection's intended spine rather than crowding. Every live game clears the distinctness criterion; the actionable findings for the §5 roadmap come from the gap analysis above, not from overlaps.

---

## §4 · OUROBOROS revival re-evaluation

> **⚠️ Superseded (late June 2026).** This section concluded "keep cut," but a later re-examination **revived OUROBOROS to the pipeline (Stage 2)**. The verdict below rested on two points that did not hold up: it took the "thin skill gap" as fatal using **one-ply** bot numbers, when a Monte-Carlo planner later showed the ceiling at ~1.74× (n=9) / ~1.84× (n=7) over random — above the healthy bar; and the handling bug it judged "resolvable but not sufficient" is now fixed in v1.1. See [`OUROBOROS_design_analysis.md`](Ouroboros/OUROBOROS_design_analysis.md) §6 for the current position. The analysis below is retained as the record of the reasoning at audit time.

OUROBOROS is the collection's one **cut** game (Tier 4) — a 1-player serpent-building solitaire, demoted from the main collection after live testing in June 2026. Per `product-vision.md`, it is retained "as a design record only" and must not be revived "without confronting why it was cut." This section does exactly that: it reads the post-mortem in [`OUROBOROS_design_analysis.md`](Ouroboros/OUROBOROS_design_analysis.md) and the cut notes in [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md) (❌ Cut) and [`NEW_GAME_CONCEPTS.md`](NEW_GAME_CONCEPTS.md) (§3), then works through four steps: it **confronts each of the three recorded cut reasons** in its own subsection, **assesses the vacated solo niche** and which mechanics (if any) are worth carrying forward, **applies the handling constraints as a gate** to any candidate revival, and **reaches a single verdict** tied back to the three cut reasons.

Three reasons are recorded for the cut, consistently across all three documents: **(a) luck-driven play**, **(b) the hidden "open symbol" living under the serpent's head**, and **(c) the thin skill gap between random and skilled play**. Each is confronted below; numbers are cited from the post-mortem rather than reproduced wholesale.

### (a) Luck-driven play — most of a session's variance is the shuffle, not the player

The recorded complaint (Overview ❌ Cut note; analysis playtest verdict) is that the short game was "too luck-based." The post-mortem's own diagnosis agrees: "most of a session's variance is the shuffle, not the player" — the puzzle is handed a shuffled deck with only a 3- or 4-card reserve of foresight, so the order in which playable and dead cards arrive dominates the outcome more than any decision does. This is not a tuning miss that a scoring-ladder tweak fixes; it is intrinsic to a **single-pass construction puzzle with limited hand foresight**. A redesign that genuinely widened player control (full-deck visibility, undo, a larger working set) would stop being OUROBOROS and start being a different game — and the open-information version of "arrange the whole deck under a combinatorial constraint" **already exists and is better**: TWELVE TRIALS (Tier 2), which the concepts doc records was "promoted to main-game development after OUROBOROS was cut," explicitly redesigned for "no hidden-face memory, no luck-blame." So the luck reason is **not resolved by any revival that keeps the concept**, and the niche a luck-free version would occupy is already taken.

### (b) The hidden open symbol under the serpent's head — constantly-needed state on a down-face

This is the load-bearing **handling** failure, and the one cut reason that is in principle *fixable*. In OUROBOROS the playable symbol at each end of the serpent — the "open symbol" you must match to place your next card — is the **hidden face of the last card** at that end (analysis playtest verdict: "the head's open symbol is the hidden face of the last card, so the player must repeatedly check under the end of the serpent to know what's playable"). That is a textbook violation of the handling constraint in [`physical-handling.md`](.kiro/steering/physical-handling.md): *"Constantly-needed, low-payoff state on the hidden/down face… (This was part of what sank OUROBOROS: the 'open symbol' lived under the serpent's head.)"* The same note records the lesson for the whole collection (`design-principles.md` lessons 1–2): constantly-needed, **low-payoff** state must be **visible**, never buried on the down-face — though hidden-face memory or deduction is welcome when it is the *point* of a game rather than involuntary overhead.

**Can the open end be made visible?** Yes — and this is the only cut reason with a clean handling answer. The fix is to **orient the end card so its active (open) symbol is the one showing**, turning the join into visible state read off the face rather than memory of the buried face — exactly the "orientation as state / self-reading layout" technique that CROSSROADS uses (roads point at the city their *visible* face names) and that TWELVE TRIALS uses (a flip is marked by rotating the card sideways). So cut reason (b) is **resolvable in isolation**. The trouble is that fixing the handling does nothing for (a) and (c): a perfectly legible serpent whose every join is glanceable is still a shuffle-driven puzzle with a thin skill gap. Handling was a necessary fix, not a sufficient one.

### (c) The thin skill gap — a red-flag predictor that the live table confirmed

This is the decisive reason, and the one the steering treats as a general law: *"A thin skill gap between random and skilled play is a warning sign of a dull game… the collection treats ~1.5× and up as healthy"* (`design-principles.md` lesson 6). OUROBOROS's simulation (n = 9, hand of 4, closing scar included — analysis §3) recorded, in **average scars (lower is better)**:

- **random 7.90** · **greedy 7.00** · **smart 4.74**

The headline the post-mortem itself flags is that **greedy barely beats random — 7.00 vs 7.90, a ~1.13× gap** — and greedy ("maximise remaining copies of the symbol you expose") is "the move every beginner reasons toward." That is well below the collection's ~1.5× healthy bar, and it is the gap a *typical* player actually experiences. A deeper "smart" policy (value each play by how many hand cards stay connected to an open end) does reach 4.74, a **~1.67× gain over random** that clears the bar — but the post-mortem is candid that this skill is **hand stewardship, not the obvious symbol-chasing**, and that the insight is subtle. The n = 7 short game (the version actually tabled) is even flatter at the obvious tier: **random 4.29 · greedy 3.65 (~1.18×) · smart 2.60**. Crucially, the sim's warning and the table agreed — the Overview records the lesson that "thin bot skill-gaps predict dull tables," and live play confirmed it ("boring and too luck-based"). The thin skill gap is **not resolved**; it is the concept's core flaw, and it predicted the live verdict accurately.

### Vacated solo niche and mechanics worth carrying forward

**The niche.** With OUROBOROS cut, **TWELVE TRIALS is the collection's lone 1-player game** — the structural thinness named in the §3 gap analysis (player-count gap: "the 1-player column holds exactly one ✓ — TWELVE TRIALS") and in that game's §2 D6 caveat. So there *is* a genuine solo gap, and a second solo game would have collection value. But the gap is an argument for **a** second solo game, not for *this* one: TWELVE TRIALS already fills the open-information solo-puzzle slot OUROBOROS would compete for, and does so without OUROBOROS's luck-dominance or hidden-face handling. Reviving OUROBOROS to fill the solo gap would re-introduce the exact flaws TWELVE TRIALS was promoted to escape.

**The mechanics.** Two pieces of OUROBOROS are mathematically lovely and worth distinguishing:

- **The Eulerian-loop construction** (the whole K₇/K₉ deck chains into one closed loop because odd symbol counts give all-even degrees — `deck-structure.md`, "Eulerian circuit … odd symbol counts (7, 9)"). As a *live, interactive* mechanic this is the very thing that carries the luck and handling problems, so carrying it forward as the spine of a solo game reproduces (a)–(c).
- **The impossible-single-scar theorem** (a finished serpent can never end with exactly one scar; scars "come in constellations" — analysis §1, confirmed across ~50,000 simulated serpents). This is a **static combinatorial fact**, not a tracked-state mechanic — it requires no hidden faces and no memory to be true, so it is the one fragment that travels cleanly (e.g. as a box-page curiosity, the role the post-mortem already suggests).

### The handling gate

Any proposed revival of an OUROBOROS mechanic must pass the handling gate from `physical-handling.md` / `design-principles.md`: it must use **visible state**, with **no involuntary hidden-face bookkeeping** (deliberate memory/deduction is fine when it *is* the game — but OUROBOROS's buried open symbol was forced overhead, not a chosen challenge) and **no constantly-needed, low-payoff state on a down-face**. Applying the gate:

- **Eulerian-loop construction as a live solo mechanic — FAILS the gate as it stood**, because the open end is the buried face (reason (b)). It can be *made* to pass by orienting each end card so the active symbol shows (visible state, per CROSSROADS), but passing the handling gate does not address reasons (a) or (c) — the game would still be shuffle-dominated with a thin obvious-skill gap. So even the gate-passing version is **rejected on fun/skill grounds**, not handling grounds.
- **The impossible-single-scar theorem — PASSES the gate trivially**, being a static printed fact with no state to track. It carries no hidden-face memory and needs no down-face state. It is admissible as flavour/curiosity, but it is not a game on its own.

### Verdict — **Keep cut**

**OUROBOROS stays cut.** This single verdict is tied to the three cut reasons as follows:

- **(a) Luck-driven play — unresolved, and fatal.** It is intrinsic to a single-pass, limited-foresight construction puzzle; the only way to remove it is to remove the concept, and the luck-free version of the idea already exists as TWELVE TRIALS.
- **(c) Thin skill gap — unresolved, and fatal.** The obvious-play gap (~1.13× greedy-vs-random at n = 9; ~1.18× at n = 7) sits below the collection's ~1.5× healthy bar, the steering treats this as a red-flag predictor of a dull game, and the live table confirmed the prediction. No evidenced redesign widens the *obvious* skill gap without becoming a different game.
- **(b) Hidden open symbol — resolvable, but not sufficient.** Orientation-as-visible-state would fix the handling (per CROSSROADS/TWELVE TRIALS), so this reason alone would not keep the game cut — but fixing it leaves (a) and (c) untouched. A legible serpent is still a dull, luck-driven one.

Because two of the three cut reasons are intrinsic and unresolved, and the vacated solo niche is already served by a stronger game, the verdict is **keep cut** — consistent with the steering's standing position that "a clean cut that teaches a lesson is a success." No OUROBOROS *game* is revived. The only fragment carried forward is the **impossible-single-scar theorem** as a curiosity (it passes the handling gate trivially); the **Eulerian-loop construction is not revived** as a live mechanic, since even its gate-passing (visible-end) form fails on the luck and skill-gap reasons. If a future second solo game is pursued to fill the §3 solo-count gap, it should follow TWELVE TRIALS's model — open information, visible state, a skilled-vs-random gap demonstrably at or above ~1.5× **before** tabling — not OUROBOROS's.

---

## §5 · Ranked priority roadmap

This is the audit's single output list: every actionable finding from §2–§4, harvested and ordered into **one ranked sequence** of concrete next actions, each tagged with the specific finding it traces to. It is the place the whole document points at — do these, in this order, for these reasons.

### Ranking principle

The order is set by the project's stated **centre of gravity**: *"a first playtest of an untested game outranks further simulation of an already-validated one"* (`playtesting.md`), and the collection's current priority is **table testing, not new design** (`product-vision.md`). So the ranking is, in bands:

1. **First table tests of untested games** rank highest — this is the centre of gravity. Within the band, items rise by **collection impact** (how singular the niche the game uniquely fills) weighted by **current risk** (Tier-3 games carry both zero sim *and* zero plays, and several have named handling or degenerate-play risks, so they sit above the Tier-2 games whose floor is already sim-certified).
2. **New gap-filling design** ranks below all table tests (new design sinks beneath table testing per the centre of gravity), ordered by how pressing the gap is.
3. **Documentation-only carries** rank below new design (near-zero effort, no table needed).
4. **Deliberate no-action / hold calls** are ranked last and recorded explicitly so the decision is on the record; they require no work, by design. Tier-1 changes sink to here absent strong evidence and owner sign-off (`product-vision.md`).

Each item names a **concrete action** and a **back-reference** to the finding it answers.

### The ranked list

**— Band 1 · First table tests (the centre of gravity) —**

1. **Run JANUS's first co-operative table test.** Start at the Apprentice ramp (3 gates / 4 omens, then 4 gates); watch whether the omen economy paces well (never deadlocking, never trivial) and whether a first table can absorb the hint/communication grammar without accidental face-leaks or quarterbacking.
   *Back-reference:* §2 JANUS scorecard (the collection's **most handling-fragile** game, D2 = 5, D7 = 5 — concealment self-policed by the "never inspect your own face" rule) **and** §3 mood gap (co-operative play **rests on this single game**). Highest rank because the one niche the collection cannot otherwise cover sits on its riskiest untested game.

2. **Run THE UNPLAYED PAIR's first table test at 4P.** Open with the Quiet Round variant to teach the follow-by-either-face rhythm; watch whether the reworked pip-rank reveal reads cleanly, whether 4P balances, whether the +1-per-unled-trick call payout rewards timing, and whether the reveal lands as theatre rather than admin.
   *Back-reference:* §2 THE UNPLAYED PAIR scorecard (rank rule already reworked once off the OUROBOROS lesson; "theatre or admin?" recorded) **and** §3 mood coverage (the collection's **only trick-taking game** — its whole genre rests on it).

3. **Run THE COUNCIL's first table test at 4–5P.** Watch for kingmaking at 5–6P, whether the pot/pip arithmetic stays frictionless, whether 4 rounds feels one short, whether deadlock stacks roll over often enough to matter, and whether Speaker rotation balances flip order.
   *Back-reference:* §2 THE COUNCIL scorecard (a named **kingmaking** degenerate-play risk at high counts) **and** §3 mood coverage (the **only negotiation/betrayal game**).

4. **Run FACE VALUE's first heads-up table test.** Open with Quick Draw (symbols 1–7) to teach the count quickly; watch whether folding-to-stay-hidden is actually used or tables call everything, whether the cold read fires at the right cadence (rare early, decisive late), and whether acting last reads as the predicted advantage.
   *Back-reference:* §2 FACE VALUE scorecard (the **only head-to-head bluffing** game; flip is static, D3 = 5; pacing sim-checked but handling table-untested).

5. **Run FALSE FACE's first table test at 3–6P.** Consider the Apprentice Forgers swing for a teaching table, then the full ledger; watch whether the ledger paces well or swings too hard, whether first-game players can price a lie, and whether 3P generates enough challenge pressure.
   *Back-reference:* §2 FALSE FACE scorecard (zero plays; ledger pacing untested) — the bluff that **uniquely scales to a 5–6P table**.

6. **Run TWELVE TRIALS's first solo table test,** timed against its three recorded questions: does a thoughtful first solve land near 7 flips (near 7 → tiers hold; clustering at 5 → compress them), does the examine-three-cards trio-verification flow drag, and does the 840-almanac depth reveal itself or stay invisible.
   *Back-reference:* §2 TWELVE TRIALS scorecard **and** §3 player-count gap (the collection's **sole 1-player game** — testing it also informs whether a second solo game is wanted, item 10). Ranked below the Tier-3 tests because its floor is sim-certified and its handling is exemplary (D2 = 9), so it carries less risk.

7. **Run TURNOVER's party table test at 5–6P.** Watch whether catching a player who forgets to announce "Turnover!" is fun or fussy, and whether spending a chain genuinely *aches* later as the maths predicts.
   *Back-reference:* §2 TURNOVER scorecard (announce-policing and chaining "untested by construction") **and** §3 play-time gap (the **only ~10-min filler** and the #1 teaching on-ramp). Balance is already closed by ~60k sims, so the table is the only remaining step.

8. **Run CROSSROADS's first 2P duel.** Watch whether the eight shared Signal-Fire flips feel scarce enough to ache (the bot is myopic about hoarding) and whether dimmed cities read at a glance as the remaining-flip counter.
   *Back-reference:* §2 CROSSROADS scorecard (recorded "does eight flips ache? / does dimming read at a glance?"). Termination and seat-balance are already settled by simulation, so the priority is the table, not more sim runs.

**— Band 2 · New gap-filling design (ranks below all table tests) —**

9. **Scope a second, sturdier co-operative game** that does *not* rest on a policed "never inspect your own face" rule — ideally one built on open registries / visible state. Gate this on item 1: JANUS's test may show the co-op niche is healthy, but the gap stands because that niche currently has a single, fragile occupant.
   *Back-reference:* §3 mood gap (co-op rests on JANUS alone) **and** §2 JANUS D2 = 5 (handling fragility). Most pressing new-design item because its niche's sole occupant is the riskiest game in the collection.

10. **Scope a second solo (1P) game on the TWELVE TRIALS model** — open information, visible state, and a demonstrable **≥1.5× skilled-vs-random** skill gap *before* tabling. Gate on item 6 confirming the solo niche wants a second entry.
    *Back-reference:* §3 player-count gap (solo served by one game) **and** §4 OUROBOROS verdict (the vacated solo niche is real, but any new solo game must follow TWELVE TRIALS, **not** revive OUROBOROS's luck-dominated, hidden-face design).

11. **Consider a sub-10-minute micro-filler** (a 2–5 minute palate-cleanser) sitting below TURNOVER — only if it clears the deck-necessity bar (no generic filler).
    *Back-reference:* §3 play-time gap (no game below ~10 min besides TURNOVER). Lowest of the new-design items: a nice-to-have, not a structural hole.

**— Band 3 · Documentation-only carry (near-zero effort) —**

12. **Add the impossible-single-scar theorem to the box/almanac page** as a printed curiosity (a finished serpent can never end with exactly one scar — confirmed across ~50,000 simulated serpents).
    *Back-reference:* §4 OUROBOROS re-evaluation — the **one fragment that travels cleanly**, since as a static combinatorial fact it passes the handling gate trivially (no hidden faces, no memory).

**— Band 4 · Deliberate no-action / hold calls (recorded explicitly; require no work) —**

13. **Hold TRIGON and TURNCOAT unchanged** — no re-tune and no re-skin absent strong evidence *and* explicit owner sign-off.
    *Back-reference:* §2 Tier-1 leave-alone recommendations (two benchmarks, ~45k simulated games of investment; `product-vision.md` tier discipline).

14. **Take no overlap-driven action — every cluster coexists.** No game is differentiated, parked, or cut on overlap grounds: TRIGON ↔ TURNCOAT is a deliberate, tier-protected "same engine, different feel" pair; FALSE FACE ↔ FACE VALUE and FALSE FACE ↔ THE COUNCIL separate on player count and engine; CROSSROADS ↔ FACE VALUE and THE UNPLAYED PAIR ↔ THE COUNCIL separate on information model and genre; and the five-game deduction-engine cluster is the collection's intended spine.
    *Back-reference:* §3 overlap-analysis summary (all verdicts: coexist).

15. **Keep OUROBOROS cut — revive no game.** Two of its three cut reasons (luck-dominance and the thin obvious-skill gap) are intrinsic and unresolved, and the vacated solo niche is already served by a stronger game. The Eulerian-loop construction is **not** revived even in its gate-passing visible-end form. Only the theorem (item 12) travels.
    *Back-reference:* §4 verdict — keep cut.

16. **Leave the Heavy, 30-minutes-plus, and pure-luck bands deliberately unfilled.** These are non-gaps: a Heavy/long-arc game runs against the "small, replayable games" vision, and a pure-luck family game would fail deck-necessity (an ordinary deck would run it).
    *Back-reference:* §3 gap-analysis summary (recorded as examined and deliberately empty, not oversights).

### One-line read

**Test the untested first — JANUS leads because the co-op niche rests on its most fragile game — then fill the co-op and solo gaps with sturdier designs, carry the scar theorem forward as flavour, and leave the benchmarks, the coexisting overlaps, the deliberate non-gaps, and the cut OUROBOROS exactly where they are.**

---

## §6 · Overview sync log

This log records the write-back from this audit into [`COLLECTION_OVERVIEW.md`](COLLECTION_OVERVIEW.md), the canonical index, so the change is auditable. Per the "cross-reference, don't duplicate" rule (`repository-structure.md`), the Overview was edited as little as possible — it now points at this audit rather than absorbing its scorecards or roadmap.

### What the audit surfaced

- **No tier changes.** All ten live games kept their maturity tiers (§2 scorecards and the cross-game matrix), and OUROBOROS stays cut (§4 verdict). No Overview entry needed relocating between tier sections.
- **No per-game status changes.** Every game's recorded tier, status, and first-table / test-focus questions in the Overview already match the audit's findings (§2 reproduces them faithfully). No genuine per-game delta.
- **One genuine priority delta — a cross-game ranking.** §5 newly orders the outstanding first table tests into a single sequence and places **JANUS first** (the co-operative niche rests on its most handling-fragile game). The Overview previously recorded per-game "needs first table test" priorities but no ordering *across* games — so the ranking is new information.

### Overview entries CHANGED

- **Development Status section — added one priority note** (a single block directly under the `## Development Status` heading). It records the audit's cross-game ranking and names JANUS as the current top first table test, linking to the audit's §5 ranked roadmap. Per Req 9.3 it references the audit rather than duplicating scorecards or the full roadmap.

### Overview entries LEFT UNCHANGED (and why)

- **All ten per-game entries** (TRIGON, TURNCOAT, TWELVE TRIALS, TURNOVER, CROSSROADS, JANUS, FALSE FACE, THE UNPLAYED PAIR, FACE VALUE, THE COUNCIL): tier, status line, and test-focus questions already accurate — the audit surfaced no per-game delta (Req 9.1). In particular the **JANUS entry's own text is unchanged**; its new top-priority standing is captured once in the Development Status note rather than duplicated on the entry.
- **OUROBOROS ❌ Cut entry:** the §4 re-evaluation confirms the cut and revives no game, so the entry is correct as written — no change (Req 9.1).
- **All four coverage tables, the Quick Selector, and the learning order:** the audit's gaps and overlaps (§3) produced no tier/status change and no new game, so the index tables stay untouched. Those gaps feed the audit's roadmap (§5), not the Overview.

The write-back is therefore a single, surgical priority pointer; every other entry was verified accurate and deliberately left as-is.
