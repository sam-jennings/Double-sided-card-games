# Core Set Audit — July 2026

> **Deferred historical curation.** The project is not currently selecting a publishable Core Set. This point-in-time audit does not control game status or design priorities.

*Independent audit of the full Flip-Deck collection to decide the first public Core Set. Every claim tagged: **[FILE]** = directly supported by an inspected file · **[INFER]** = reasoned from multiple files · **[GAP]** = missing information / unresolved decision. Optimised for blind-test survival, publisher scrutiny, and onboarding — not mathematical interest.*

*Files inspected: COLLECTION_OVERVIEW.md, COLLECTION_AUDIT.md, DECK_CONVENTIONS.md, DECK_PLAYTEST_FINDINGS.md (F1–F12), DECK_BUG_AUDIT.md, DECK_SIZE_DECISION.md, PUBLISHING_PLAN.md, product-vision.md, and the rulebook / design-analysis / playtest / task files of all 17 game folders.*

---

## 1 · Executive verdict

**The currently promoted collection (TWELVE TRIALS, CROSSROADS, THE ORRERY) is not the pitchable Core Set — all three carry unresolved handling or structural defects that a blind tester hits in the first session.** The internal promotion gate ("first table verdict = iterate") measures design survival, not product readiness; the two must be decoupled.

**Recommended Core Set (6 games):**

| Slot | Game | Status |
|---|---|---|
| Flagship / trick-taking | **BLIGHT** | Confirmed — strongest table evidence in the repo |
| Companion trick-taker | **GLEAN** | Confirmed, one condition: majority scoring must pass a table test |
| Opener / party | **WILDFIRE** | Confirmed — teaches the deck in 10 min, table-tested |
| 2P duel | **FACE VALUE** | Provisional — takes the slot from CROSSROADS by default; CROSSROADS gets one verdict session to reclaim it |
| Solo | **CAIRN** | Provisional — needs its first table test (cheap: solo, any week) |
| Depth / tactical | **TRIGON** | Conditional — must pass the grid-fix + player-aid re-test at 2P, or the Core Set ships with 5 games |

**Flagship: BLIGHT.** Backup flagship: **TRIGON**, strictly conditional on its re-test; if TRIGON fails the gate, the fallback flagship story is "BLIGHT + GLEAN — one deck, two trick-takers" with FACE VALUE as the second pitch once it has two clean sessions.

**Parked (deck-wide blocker):** JANUS (T1/F7 — no concealed repeated draw exists), SLEEPER (the deck's concealment ceiling — F8 — is unproven; its first table test is a *deck* test).
**Demoted to pipeline/expansion/PNP:** CROSSROADS (on notice, rulebook out of sync), TWELVE TRIALS + THE ORRERY (both hostage to the untested F12 counter method), TURNCOAT (expansion-natural, zero table tests), RELAY (no rulebook), FORKED TONGUE, THE COUNCIL, OUROBOROS.
**Cut/ignore for now:** THE UNPLAYED PAIR (stays parked — call mechanic structurally dead), SNARE (Stage 0 concept).

**The single biggest product risk is not any game — it is that DECK_CONVENTIONS C2/C3/C5/C6 are still "Proposed" and the house-kit question (T1+T2+C5) is open, so the Deck Handbook (PUBLISHING_PLAN G1) cannot be written, and no component list can freeze (G5).** Blind testing anything before the Handbook exists wastes testers on known handling failures (F1/F9).

---

## 2 · Evidence-backed findings

### Status contradictions (documentation says one thing, evidence says another)

**2.1 — Promotion status is inverted relative to product readiness.** [FILE] COLLECTION_OVERVIEW's "Collection (table-tested and promoted)" = TWELVE TRIALS, CROSSROADS, THE ORRERY. But: TWELVE TRIALS ships a flip-tracking method its own playtest confirmed failed (TWELVE_TRIALS_playtest_01.md; DECK_BUG_AUDIT punch #4: "the shipped method is confirmed-failed and still in the rulebook"); CROSSROADS is "in the collection on notice" with a CRITICAL pass-to-win finding and a rulebook that "contradicts the settled decisions" (CROSSROADS_playtest_02.md; DECK_CONVENTIONS T5); THE ORRERY has no physical flip-tally method at all (F12) and its full 9-symbol game and sky-debt layer are untested (ORRERY_tasks.md #2–3). Meanwhile BLIGHT — "the session's standout… rules praised as clear, play clean" (BLIGHT_playtest_01.md) — sits in the pipeline. [INFER] "Promoted" currently means "was tested first," not "is best." The Core Set declaration must not inherit the promotion list.

**2.2 — COLLECTION_OVERVIEW is stale on WILDFIRE and GLEAN.** [FILE] Both are listed at Stage 2 with "*First table questions:*" phrasing as if untested — but WILDFIRE_playtest_01.md and GLEAN_playtest_01.md exist (June 2026), and PUBLISHING_PLAN §0/§3 cites their results ("the overview's Stage 2 listing is stale"). Anyone reading the overview alone mis-stages two Core Set games.

**2.3 — COLLECTION_AUDIT.md is systemically outdated.** [FILE] Its tier structure predates every table test: TRIGON and TURNCOAT sit at "Tier 1 · Complete (sim-tuned, rulebook final)" while TRIGON's playtest verdict is "not yet a candidate for promotion"; WILDFIRE/CROSSROADS/TWELVE TRIALS are tiered "needs first table test" (all now tested); §4's OUROBOROS verdict "Keep cut" is superseded by the revival (banner exists per DECK_BUG_AUDIT #12, but §0's "ten live games" scope note is still unpatched). [INFER] COLLECTION_AUDIT should be treated as a historical document and banner-marked as such, or it will keep leaking stale authority (it is the only place with per-game rubric scores).

**2.4 — The overview's learning order and flagship language contradict the table evidence.** [FILE] "Recommended play order" #2: "TRIGON — the flagship" — but PUBLISHING_PLAN §0: TRIGON "is currently the collection's biggest teach-cost risk, not its proven star," and its playtest shows the engine "never got a fair run." [INFER] Any external reader (publisher, blind tester) following the overview meets the collection's hardest teach second. Rewrite after the Core Set is declared.

**2.5 — GLEAN's shipped scoring has never been played.** [FILE] GLEAN_playtest_01.md: "Played Plunder scoring only — full majority scoring was not tested," and Plunder was refuted (B1: "tedious… needs a simpler scoring method"). The rulebook's real game (nine simultaneous sign-majorities) is table-unproven. [INFER] The "BLIGHT + GLEAN ride together" pitch story (PUBLISHING_PLAN §3) is sound on engine evidence but weaker than it reads: GLEAN's promotion condition is one majority-scoring session, and F4's rank-teaching gap (which materially damaged the first session) must be re-tested with the teach script.

### Weak assumptions

**2.6 — "CROSSROADS or FACE VALUE, the pass-to-win verdict decides" assumes CROSSROADS gets tested on-spec.** [FILE] CROSSROADS has now failed to test its own core (the flip economy) **twice** — playtest 01 (simplified no-flip version) and playtest 02 (off-spec 3P, "flips barely used"). [INFER] The evidence-honest default for the 2P Core slot is FACE VALUE (physically "verified clean" in DECK_BUG_AUDIT §4, pacing sim-checked, familiar poker-lineage pitch), with CROSSROADS allowed one properly-run 2P Signal-Fires session to reclaim it. Do not hold the Core Set declaration open indefinitely for a game that keeps dodging its own test.

**2.7 — The Core Set's proven depth is thin if TRIGON fails its gate.** [FILE] WILDFIRE playtest: "players did not feel there was much skill involved"; BLIGHT is the only tested game with a demonstrated depth line (slough-as-weapon). [INFER] If TRIGON is demoted at the gate, the pitch leans entirely on BLIGHT's depth — acceptable, but it raises the stakes on BLIGHT's full-match test and on getting FACE VALUE tabled (its Cold Read is the next-best depth story). This is a reason to run the TRIGON re-test early (PUBLISHING_PLAN already gates it ~day 45), not to pre-promote it.

**2.8 — "Deck only" component claims will not survive the conventions.** [FILE] Component inventory lists TWELVE TRIALS and THE ORRERY as needing nothing, but C5 (counters for flip tallies) is the proposed fix for their confirmed/latent F6/F12 failures; T1 may add a container; T2 may add a shared sign reference. [INFER] The component inventory is correct today and wrong the moment C5 is ratified — freeze the component list (G5) only after the house-kit decision (Decision D1 below), then update the inventory in the same commit.

**2.9 — Zero external validation exists anywhere.** [FILE] PUBLISHING_PLAN §5a: "Currently zero external sessions; everything so far is Sam-at-the-table." Also all playtests are 1–3 players from the same household group. [INFER] No game — including BLIGHT — can currently be called blind-test-survivable. G4 (flagship at Stage 7) is unmet for every game; every Core Set validation test below therefore ends in a ring-1 blind session, not another Sam-run table.

### Unresolved decisions blocking the product (all [GAP])

- **T1** — JANUS concealment model (box / bag / no-draw redesign). Blocks JANUS entirely; also blocks G5 component freeze.
- **T1+T2+C5 house-kit meta-decision** — DECK_BUG_AUDIT: "really one question: what is the house kit?" One decision closes three fronts (concealed draws, TRIGON references, flip tallies).
- **Ratification of C2/C3/C5/C6** — proposed, contradiction-checked, awaiting yes/no. Blocks the Deck Handbook (G1), which blocks all blind testing.
- **T3** — counter-on-card for TWELVE TRIALS replay modes: proposed, untested. Blocks TRIALS' rulebook repair.
- **CROSSROADS Phase 3 end trigger** (eighth-dim clock) — blocks the v1.2 rulebook rewrite; the rulebook contradicts settled design until then (T5).
- **T2 / SIGN_MNEMONICS Leaf–Key relabel** — balance-neutral, unapplied; decide before commissioning the 9-icon system (PUBLISHING_PLAN month-2 item 12) or the icons bake in the old names.
- **T4** — open registries vs memory-as-skill: keep C6 default, but it's an explicit standing decision, not settled.
- **F2 confirmatory print test** — top-left corner pip: settled on paper, unverified physically; must precede the icon commission brief being finalised.

### Local fixes that could damage the shared deck system (watch-list)

**2.10** [FILE] The C3 sideways-dead-pile wording is already written into TRIGON/TURNCOAT/SLEEPER rulebooks while C3 is still *Proposed* (DECK_BUG_AUDIT §3 caveat: "if C3 is rejected, three lines to re-touch"). Ratify C3 before any further rulebook passes, or the convention gets entrenched by drift instead of decision. **2.11** [FILE] TWELVE TRIALS' broken sideways method is also a C4 namespace squatter ("sideways on a single placed card… TWELVE TRIALS = flipped") — when C5 counters replace it, update the C4 declaration list too, or the namespace table lies. **2.12** [INFER] Any per-game fix to F1 hand-scan pain (e.g. a BLIGHT-specific sort rule) would violate the F1-is-a-constraint ruling — the sanctioned levers are player count, subsets, and the icon system only.

---

## 3 · Candidate scoring

Scale 1–5 (5 best); Risk columns L/M/H (L best). *PS pitch strength · RR rules-readiness · PH physical-handling confidence · DN deck-necessity · DX distinctness · BR blind-test risk · PT production/teaching risk.*

| Game | PS | RR | PH | DN | DX | BR | PT | Evidence base |
|---|---|---|---|---|---|---|---|---|
| **BLIGHT** | 5 | 5 | 4 | 5 | 4 | **L–M** | L | Table-tested clean; rules read unaided [FILE] |
| **GLEAN** | 4 | 4 | 4 | 5 | 4 | **M** | L | Engine table-tested; majority scoring untested [FILE] |
| **WILDFIRE** | 3 | 5 | 5 | 4 | 5 | **L** | L | Table-tested; zero clarifications [FILE] |
| **FACE VALUE** | 4 | 4 | 5 | 4 | 4 | **M** | L | Audit-clean physics; pacing sim; never tabled [FILE] |
| **CAIRN** | 3 | 4 | 5 | 4 | 4 | **M** | L | "Model citizen" physics; sim-validated; never tabled [FILE] |
| **TRIGON** | 4 | 3 | 3 | 4 | 5 | **H** | **H** | 23k sims; table test bottlenecked on handling [FILE] |
| CROSSROADS | 3 | **1** | 3 | 5 | 4 | **H** | M | Rulebook contradicts settled design; core untested twice [FILE] |
| TWELVE TRIALS | 3 | 2 | **2** | 5 | 4 | **H** | M | Shipped tracking method confirmed-failed [FILE] |
| THE ORRERY | 2 | 3 | 2 | 5 | 3 | **H** | M | No flip-tally method; full game untested [FILE] |
| TURNCOAT | 3 | 4 | 4 | 4 | 3 | **H** | M | 22k sims, zero table tests [FILE] |
| OUROBOROS | 2 | 4 | 4 | 4 | 3 | M | L | Revived v1.1, untested at table [FILE] |
| FORKED TONGUE | 3 | 4 | 4 | 5 | 4 | M | L | Exemplary physics per audit; untested [FILE] |
| THE COUNCIL | 3 | 4 | 4 | 4 | 4 | M | M | Untested; kingmaking question open [FILE] |
| RELAY | 3 | **0** | 4 | 5 | 3 | — | — | No rulebook exists [FILE] |
| JANUS | 4 | 2 | **1** | 5 | 5 | **H** | H | Blocked: F7/F10/T1 [FILE] |
| SLEEPER | 4 | 3 | **2** | 4 | 5 | **H** | M | Premise = unproven concealment ceiling (F8) [FILE] |
| UNPLAYED PAIR | 2 | 3 | 3 | 4 | 2 | H | M | Call mechanic structurally dead [FILE] |

**Distinctness check on the recommended six** [INFER]: party shedding / trick-avoidance / trick-accumulation / heads-up bluff / solo patience / tactical grid — six genres, player counts 1–6 covered, no shared cell; GLEAN↔BLIGHT overlap is deliberate (one engine, opposite goals — a pitch asset, and COLLECTION_AUDIT §3 already rules the TRIGON-class overlaps "coexist").

### Next validation test per Core Set game

| Game | Next test (in order) | Pass condition |
|---|---|---|
| BLIGHT | ① 4P (9-card hands) + full match ② ring-1 blind test (Sam absent) with Deck Handbook | Hand-handling comfortable at 9; luck complaint washes out over match; blind group completes a round unaided |
| GLEAN | Majority scoring at 3–4P with the F4 teach script delivered | Nine-majority counting frictionless; no rank-structure confusion post-script |
| WILDFIRE | Second test: Inferno (chain 3) + announce rule, as warm-up | A visible don't-chain decision occurs, or accept "pure opener" framing |
| FACE VALUE | First table test per FACE_VALUE_playtest_plan_01 | Fold/cold-read tension real; ~12-duel pacing holds; then a second session with strangers |
| CAIRN | First solo table test (First Trail → standard) | Blocking reads as foreseeable mistake, not shuffle blame; then BGG Solitaire PNP contest |
| TRIGON | Re-test at 2P with centre-first grid + 9-ability player-aid card | Turns flow without reference stalls; grid drift gone → promote. Fail → demote to expansion tier, Core Set = 5 |

---

## 4 · Decisions required from Sam

- **D1 — The house kit (closes T1 + T2 + C5 in one stroke).** Recommend: *"the kit is the game box (T1 container), ~10 generic counters (C5), one shared Nine Signs reference sheet (T2)."* This is the single decision DECK_BUG_AUDIT identifies as three-fronts-in-one. Until decided: no component freeze, no Handbook, JANUS stays parked.
- **D2 — Ratify C2, C3, C5, C6** (yes/no each; all contradiction-checked already). Unblocks the Deck Handbook and retro-legitimises the C3 wording already in three rulebooks.
- **D3 — Core Set declaration** per §1 above, including accepting FACE VALUE as 2P default with CROSSROADS' one-session reclaim clause, and the TRIGON conditional gate (with a named date — PUBLISHING_PLAN says ~day 45).
- **D4 — GLEAN's condition**: confirm GLEAN ships in the Core Set only if majority scoring passes one session; otherwise BLIGHT ships alone and GLEAN becomes a PNP extra.
- **D5 — SIGN_MNEMONICS Leaf/Key relabel** — decide before the icon commission brief is sent.
- **D6 — TWELVE TRIALS vs THE ORRERY**: neither enters the Core Set now; decide whether the eventual seventh slot (post-F12 validation) is reserved for one of them, and which — recommend TRIALS (stronger playtest engagement, clearer score story) once counters pass.
- **D7 — COLLECTION_AUDIT.md status**: banner it as historical (recommended) or commission a full re-score. Do not leave it half-authoritative.

---

## 5 · File-by-file implementation tasks

| File | Task |
|---|---|
| `COLLECTION_OVERVIEW.md` | Restructure Development Status around the declared Core Set (D3): new "Core Set" section (6 games, per-game status: confirmed/provisional/conditional); move TWELVE TRIALS, CROSSROADS, THE ORRERY out of "promoted" into pipeline-with-banner; fix stale WILDFIRE/GLEAN Stage-2 entries (both are Stage 3, cite playtest files); rewrite "Recommended play order" (WILDFIRE → BLIGHT → GLEAN → FACE VALUE → CAIRN → TRIGON-conditional); update CROSSROADS player-count/coverage rows only when v1.2 lands (Phase 6 dependency) |
| `COLLECTION_AUDIT.md` | Add §0 supersession banner ("tiers predate all June–July 2026 table tests; see CORE_SET_AUDIT_2026-07.md") per D7 |
| `DECK_CONVENTIONS.md` | On D2: flip C2/C3/C5/C6 from Proposed → Settled; on D1: rewrite T1/T2 as resolved, record the house kit as C10; update C4 declaration list when TRIALS drops sideways-marking |
| **New: `DECK_HANDBOOK.md`** | One page (G1): 9 signs + ranks, F4 teach script, C1 shuffle, C2 deal ladder, C3 pile law, C5 counters, C6 registry sentence, C8 hand-size guidance, C9 table-space note. Blocked by D1/D2. Ships inside every Core Set rulebook |
| `PUBLISHING_PLAN.md` | Update §3 slate to match D3 (FACE VALUE default in 2P slot; CAIRN confirmed solo; TRIALS/ORRERY both deferred); mark punch-list items done as they land |
| `Glean/GLEAN_rulebook.md` | After majority-scoring session: either confirm scoring text or apply the chosen Plunder replacement to the teaching variant; ensure F4 callout survives edits |
| `Trigon/TRIGON_rulebook.md` | Add centre-first grid setup line; extract the 9-ability table into a printable player-aid page (T2-dependent format); keep all C3/Moon-sideways patches |
| `Crossroads/CROSSROADS_rulebook.md` | v1.2 rewrite **only after** Phase 3 end-trigger sim: deal-9, Toll-in-base, 2–4P callout, end trigger. Keep the pending banner until then |
| `Twelve Trials/TWELVE_TRIALS_rulebook.md` | After counter trial passes: replace sideways-marking with C5 counters (+ counter-on-card for Duel); component line gains "~10 counters (house kit)"; fix "the collection's reference card" → "the almanac printed in this rulebook" (DECK_BUG_AUDIT #12) |
| `The Orrery/ORRERY_rulebook.md` | Add C5 counter tally as the physical method (currently none) after the same trial |
| `Face Value/FACE_VALUE_rulebook.md`, `The Council/COUNCIL_rulebook.md`, `The Unplayed Pair/UNPLAYED_PAIR_rulebook.md` | Add the F4 sign-is-rank callout (DECK_BUG_AUDIT #9) |
| `Janus/JANUS_rulebook.md` | On D1 (box-as-container): rewrite deal/refill protocol around the container; add the keystone lift-freely line (DECK_BUG_AUDIT #11); remove blocker banner only after a concealed table test passes |
| `Relay/` | Write `RELAY_rulebook.md` (pipeline priority, not Core-blocking) |
| `index.html` | Sync catalogue to Core Set / pipeline split after D3 |
| `Designs/CARD_LAYOUT.md` | Clear F6/F12 annotations once C5 is ratified and the orientation table rows are corrected |

---

## 6 · Kiro-ready task list

Ordered; each has acceptance criteria. K1–K3 are desk work unblocked today.

**K1 — Declare the Core Set in COLLECTION_OVERVIEW.md** *(needs D3)*
- AC: overview has a "Core Set" section listing exactly the 6 games with per-game status labels and reclaim/gate clauses; TRIALS/CROSSROADS/ORRERY moved to pipeline with one-line reasons citing their playtest files; WILDFIRE and GLEAN entries cite their June 2026 playtests; play order rewritten; no remaining "flagship" label on TRIGON.

**K2 — Ratify conventions and write DECK_HANDBOOK.md** *(needs D1, D2)*
- AC: DECK_CONVENTIONS shows C2/C3/C5/C6 as Settled and the house kit recorded; DECK_HANDBOOK.md exists, ≤1 page, covers the 9 items listed in §5; no rulebook contradicts it (grep for "face-down" returns only JANUS-pre-rewrite hits or zero).

**K3 — Banner COLLECTION_AUDIT.md** *(needs D7)*
- AC: §0 carries a dated supersession note pointing here; no other edits.

**K4 — BLIGHT promotion session** *(table)*
- AC: playtest 02 written: 4P (9-card hands) + full match started; records hand-handling comfort at 9 cards, luck-washout read, any shoot attempt. Pass → BLIGHT marked Core-confirmed flagship.

**K5 — GLEAN majority-scoring session** *(table, can share an evening with K4)*
- AC: playtest 02 written: majority scoring, F4 script delivered pre-game; records whether nine-majority counting is frictionless. Pass → GLEAN Core-confirmed; fail → D4 fallback executed.

**K6 — CROSSROADS reclaim session (one only)** *(table)*
- AC: 2P, deal-9, Toll, Signal Fires actually used, pass-to-win deliberately attempted. Playtest 03 answers: pass-to-win dead at the table? eighth-dim trigger fair? Pass → CROSSROADS may re-enter Core discussion; fail/off-spec again → slot is FACE VALUE's, CROSSROADS stays pipeline.

**K7 — FACE VALUE first table test** *(table, per existing plan file)*
- AC: playtest 01 written against FACE_VALUE_playtest_plan_01 hypotheses; verdict recorded; if iterate → provisional-confirmed for Core 2P slot pending K6's outcome.

**K8 — CAIRN first table test** *(solo, any week)*
- AC: playtest 01 written; blocking-reads-as-mistake question answered; if iterate → Core-confirmed and earmarked for BGG Solitaire PNP contest.

**K9 — TRIGON gate re-test** *(desk: player-aid draft; then table at 2P)*
- AC: centre-first grid line drafted; 9-ability player-aid produced; 2P session played; playtest 02 records whether reference stalls are gone and grid drift eliminated. Pass → Core-confirmed depth slot. Fail → TRIGON demoted to expansion tier in overview + publishing plan, Core Set = 5, no further TRIGON work before month 4.

**K10 — F12 counter trial (TWELVE TRIALS, extend to ORRERY)** *(solo)*
- AC: one full TRIALS solve with counters (+ counter-on-card Duel restore attempt); result appended to playtest file; if pass → K11 unblocked and D6 decided; if fail → T3 fallback (written note or Duel cut) proposed.

**K11 — Rulebook sync sweep after K1–K10** *(desk)*
- AC: every §5 file-task whose dependency has landed is applied; F4 callout present in all five rank games; component inventory matches the frozen kit; index.html matches the overview.

**K12 — Ring-1 blind test: BLIGHT + Handbook** *(Sam out of the room)*
- AC: blind group plays a full round unaided; first-read confusions logged on the Templates feedback form; Handbook and rulebook iterated. This is the G4 Stage-7 entry test for the flagship.

---

## 7 · Things NOT to change

- **The 9-symbol / 36-card master deck with subset play** (DECK_SIZE_DECISION.md) — settled, load-bearing for every game.
- **DECK_CONVENTIONS C1–C9 text** — ratify, don't rewrite. In particular C1's shuffle phrasing ("identical in every rulebook — never change per game").
- **The C3/F11 patches already applied** to TRIGON, TURNCOAT, GLEAN, SLEEPER, WILDFIRE, THE UNPLAYED PAIR rulebooks — they fix physically-false rules; reverting reintroduces F10/F11 bugs.
- **Sim-tuned mechanics**: WILDFIRE chain-2/refusal-2 (chaining is load-bearing for termination — playtest 01 explicitly rules "do not remove"), BLIGHT/GLEAN trick engine, TRIGON's tuned ability set, CROSSROADS' decided-but-unapplied trio (deal-9 / Toll / 2–4P) — apply them whole with the end trigger, never piecemeal.
- **CROSSROADS v1.2-pending banner** — do not partially update the rulebook ahead of the Phase 3 end-trigger decision (T5's exact warning).
- **THE UNPLAYED PAIR's parked status and folder** — retained as a design record; the missing-card idea is already preserved in the Parking Lot.
- **OUROBOROS's revival status** — the cut-then-revive lessons in COLLECTION_OVERVIEW are binding as corrected; don't relitigate.
- **The graduated component policy** (COLLECTION_OVERVIEW inventory section) — D1 operates *within* it; don't loosen the "reused by more than one game" bar.
- **F2's top-left corner pip decision** — only the confirmatory print test remains; don't reopen placement.
- **F1's status as a constraint, not a bug** — no per-game sort rules; levers are hand size, subsets, visual identity only.
- **The stage framework and collection gate** (product-vision.md) — the fix in this audit is decoupling *Core Set membership* from *promotion*, not changing the gate.
