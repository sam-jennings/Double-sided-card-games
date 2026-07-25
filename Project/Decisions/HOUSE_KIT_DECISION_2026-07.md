# House-Kit & Deck-Conventions Decision — July 2026

> **Current physical-kit decision; publishing follow-ups deferred.** The handling/component decisions remain useful for prototypes. Any references to a Core Set, product box, or publication schedule belong to [Later/Publishing](../../Later/Publishing/README.md) and are not current priorities.

*Resolves CORE_SET_AUDIT_2026-07.md D1/D2 (and the audit's T1/T2/T3 tensions). Written as an implementation memo for Opus/Kiro. Evidence tags: **[FILE]** directly supported by an inspected file · **[INFER]** reasoned from multiple files · **[GAP]** unresolved.*

---

## 1 · Executive decision

**The Flip-Deck Collection officially adopts a tiny reusable generic kit (D1 option B): the 36-card deck, one shared Deck Handbook, 12 identical generic counters, one shared Nine Signs reference sheet, and the game box itself — whose base is the sanctioned opaque draw container when a game explicitly calls for one.** This is not a retreat from "one deck, many games" — the component inventory already sanctioned a generic counter kit (JANUS's 6 omens, THE COUNCIL's Speaker token) [FILE: COLLECTION_OVERVIEW component policy], so this decision formalises existing practice and closes the deck's three hardest physical problems (repeated concealed draws, ability-reference load, flip tallies) in one stroke, exactly as DECK_BUG_AUDIT framed it ("really one question: what is the house kit?") [FILE]. C2, C3, C5 and C6 are all ratified **Settled**. The Deck Handbook (G1) and component list (G5) are unblocked and frozen per §5. JANUS becomes *playable-in-principle* but stays parked outside the Core Set until a concealed table test passes. Everything below is implementable today except the two scheduled table validations (K10 counter trial, JANUS concealment test), which validate methods already decided — they do not hold the Handbook or the freeze hostage.

## 2 · Decision table

| # | Decision | Call | Confidence | Consequences |
|---|---|---|---|---|
| D1 | House kit | **B — deck + tiny reusable generic kit** (12 counters, 1 sign sheet, box-as-container, Handbook) | High | Component freeze (§5); Handbook unblocked; pitch line becomes "36 cards, a booklet, a sheet, a dozen counters — nothing else" |
| D2-C2 | Deal/draw ladder | **Settled** (rung-4 cell rewritten to name the box) | High | Every "unseen" rule must name its rung; Handbook prints the ladder |
| D2-C3 | Live stacks vs dead piles | **Settled** | High | Retro-legitimises wording already in TRIGON/TURNCOAT/SLEEPER/WILDFIRE |
| D2-C5 | Flip tallies = counters | **Settled** (K10 trial remains as validation, not as a gate on the convention) | Medium-High | TRIALS/ORRERY rulebooks updated now; confirmed-failed sideways method removed |
| D2-C6 | Public registries | **Settled** | High | Registry sentence canonical; declared exceptions stand |
| D3 | JANUS | **Playable-in-principle; parked outside Core Set until a concealed table test passes** | High | Rulebook rewritten around the container; banner softened, not removed |
| D4 | Nine Signs reference sheet | **Official, one shared sheet** (front: signs+ranks+mnemonic verbs; back: TRIGON/TURNCOAT ability tables). Prerequisite: apply the SIGN_MNEMONICS Leaf/Key relabel to TRIGON — adopted here (zero balance cost) | High (sheet) / High (relabel — tested, balance-neutral) | Kills TRIGON's Bug-2 reference stall path; doubles as the F4 teach aid |
| D5 | Component freeze | **Frozen per §5** | Medium-High | Every design between now and pitch inherits it; G5 closed |

## 3 · Evidence-backed reasoning

### The container (C2 rung 4 / T1)

- [FILE] F7: no concealable draw deck exists; the players' own hack in JANUS playtest 01 was covering the deck with a spare card — "the clearest pointer to the real solution: a genuine opaque deck cover, sleeve, or draw-bag."
- [FILE] DECK_CONVENTIONS T1 options: (a) game box — "arguably free — every copy owns a box"; (b) bag — "new component class, currently justified by one game — fails the reuse bar"; (c) no-draw redesign — "changes pacing, needs re-sim."
- [INFER] The box wins on the collection's own graduated policy: it adds **zero marginal components** (option b fails the reuse bar by the policy's own words; option c spends redesign+re-sim effort on a parked, non-Core game — the worst use of 5–10 hrs/week under PUBLISHING_PLAN's "deliberately absent: JANUS/SLEEPER work"). During play JANUS's deck is only 5 cards [FILE: JANUS rulebook deal arithmetic], easily housed in a box base.
- [INFER] Production consequence: a **tuckbox cannot serve as a draw container**; PUBLISHING_PLAN §5d currently says "tuckbox or small two-piece box" — the decision narrows this to **two-piece box** (or the container claim gets a "box permitting" caveat). Flag in the Game Crafter quote (90-day item 6). Prototype substitute (mug/envelope/bag) is already sanctioned in T1's own text [FILE].
- Note the container is *only* load-bearing for JANUS. That is acceptable because it costs nothing: the box ships regardless. It does not weaken the pitch — the component line is unchanged.

### The counters (C5 / F12)

- [FILE] F6: sideways flip-marking is a **confirmed failure** for TWELVE TRIALS; F12: THE ORRERY's rulebook "never had *any* physical method" (its rules say "count 1 flip" with optional paper — involuntary bookkeeping).
- [FILE] The kit already exists in all but name: JANUS needs 6 omen tokens ("any 6 small objects"), THE COUNCIL 1 Speaker token, SLEEPER an optional first-player token — the inventory's own policy text says "a small, generic, reusable shared counter kit is **sanctioned**, not banned."
- [FILE] TWELVE_TRIALS_tasks.md already specs the fix: "Penny/token on flipped cards — survives regrouping, glanceable, supports Duel replay (remove pennies to restore deal). Needs ~10 small tokens."
- [INFER] **Count = 12**, not "~10": covers JANUS's 6 omens, TRIALS' realistic worst case (unoptimised average 9 flips; 10+ is the fail tier anyway [FILE: TRIALS rulebook tiers]), and ORRERY's 9-symbol deals with headroom; household substitutes make overflow a non-event. Five games draw on the pool — comfortably clearing the "reused by more than one game" bar.
- [INFER] Settling C5 *before* the K10 trial is the right risk: the incumbent method is confirmed-failed, the ORRERY has nothing, and there is no competing candidate. What K10 actually tests is the **counter-on-card restore** for TRIALS' Duel/replay modes (T3) — if that fails, the fallback (written note or cut the Duel restore) is game-local and does not touch the convention. [GAP] The trial itself.

### The reference sheet (T2 / D4)

- [FILE] TRIGON playtest 01 Bug 2 (HIGH): "every turn every player was reading the rules… a single shared laptop reference throttled the whole table." The playtest's own options list names "a *generic* nine-sign quick-reference card could serve TRIGON, TURNCOAT, and others."
- [FILE] SIGN_MNEMONICS_proposal: after the Leaf/Key relabel, **7 of 9 signs carry the same one-idea verb in both games**, at zero balance cost ("the simulator runs the identical 9 bundles"), with the unified cheat-sheet table already drafted.
- [INFER] This is a **generic deck aid, not a TRIGON crutch**: the sheet's front (nine signs, fixed ranks, mnemonic verbs) is the printed form of the C7/F4 teach script — it serves every rank-sensitive game (GLEAN, BLIGHT, FACE VALUE, THE COUNCIL, THE UNPLAYED PAIR) and every future ability game; the back carries the TRIGON/TURNCOAT ability tables. One sheet, two sides, whole collection.
- [INFER] Placement: a **separate sheet** in the box (so it sits mid-table per the playtest need), with the same content duplicated as a back page in the TRIGON and TURNCOAT rulebooks. Handbook carries the ranks line only — it must stay one page.
- Prerequisite ordering [FILE: CORE_SET_AUDIT §2 "T2/SIGN_MNEMONICS… decide before commissioning the 9-icon system"]: relabel is adopted **now**, before the icon commission (month-2 item 12) and before the sheet is laid out.

### The ratifications (C2/C3/C6)

- C2 [FILE]: compatibility matrix shows a rung for every game, no contradictions; the only unresolved cell was JANUS's "4 required — unresolved (T1)" — now resolved by the container. F10's law ("never say 'unseen' without naming the rung") already enforced in SLEEPER/UNPLAYED PAIR patches.
- C3 [FILE]: already written into TRIGON, TURNCOAT, SLEEPER, WILDFIRE rulebooks (verified by grep — all use "rotated 90° sideways… so it can't be mistaken for the deck" phrasing); DECK_BUG_AUDIT's caveat ("if C3 is rejected, three lines to re-touch") is retired by ratifying. No game uses sideways piles for anything else [FILE: C3 text].
- C6 [FILE]: the registry sentence is already live in near-identical form in FACE VALUE (morgue+tallies), FORKED TONGUE (registry), GLEAN (harvest), TWELVE TRIALS (spread) — verified by grep. Declared exceptions (BLIGHT rot pile orientation-encoded, TURNCOAT ordered stack, TRIGON Moon-sideways) each earn their deviation and stand. [INFER] The per-game phrasings differ by a few words from the canonical sentence; accept the variants (they are unambiguous) rather than churn four validated rulebooks — the Handbook prints the canonical form.

### D3 — JANUS

- [FILE] Playtest 01: the table **abandoned the fan-asymmetry concealment entirely** and played open-information — so even with the draw problem solved, F8 (fan-handling leak risk, "most severe for JANUS") is an unproven second blocker.
- [INFER] Therefore: box-as-container makes JANUS **playable-in-principle** (the rulebook can finally be written honestly), but promotion-blocking validation is a *concealed table test* — which is a deck-physics test as much as a game test. JANUS stays **outside the Core Set** and outside the 90-day plan (per PUBLISHING_PLAN's "deliberately absent"). No redesign (option c) — don't spend re-sim effort before the cheap test.
- The box is elegant *enough*: draw-blind-from-box-base is one sentence of protocol, and the deal (12 cards into fans without anyone glimpsing) rewrites cleanly as "each player draws their fan one card at a time from the container, sliding each card straight into the fan outward-face away." [INFER] Burden is now normal-game-level; the residual burden is F8 handling, which only a table can judge.

## 4 · Settled wording for DECK_CONVENTIONS.md

Exact edits (Kiro-applicable):

**C2 header:** `## C2 · The information ladder for deals and draws — **Settled (July 2026)**`
**C2 rung-4 row, replace with:**
`| 4 | **Opaque container** — the deck sits inside the **game box base** (the house-kit container, C10; at home any mug, envelope, or bag); draw blind from inside | Nothing, repeatedly | The only method that supports **repeated concealed draws** (currently JANUS only) |`
**C2, replace** "Rungs 1–3 are deck-native and component-free. Rung 4 is the one concealment the deck cannot do by itself." **with:**
"Rungs 1–3 are deck-native and component-free. Rung 4 is the one concealment the deck cannot do by itself — the house kit's box-as-container (C10) is the official method."

**C3 header:** `## C3 · Live stacks vs dead piles — **Settled (July 2026)**` *(body unchanged)*

**C5 header:** `## C5 · Flip tallies in regrouping games — **Settled (July 2026, F12)**`
**C5 body, replace** "use the **sanctioned generic counter kit** (any small objects — the same house kit JANUS's omens and THE COUNCIL's Speaker token already draw on)" **with:**
"use the **house-kit counters** (C10; any small objects substitute — the same pool JANUS's omens and THE COUNCIL's Speaker token draw on)"
**C5, append:** "*Table validation of the counter-on-card restore (TWELVE TRIALS Duel) is scheduled (see T3); a failure there is game-local and does not reopen this convention.*"

**C6 header:** `## C6 · Score piles and public registries — **Settled (July 2026)**`
**C6, append:** "*Existing rulebooks carry near-identical phrasings of this sentence; those variants are compliant — the canonical form above is for the Handbook and all new rulebooks.*"

**C4 declaration list:** remove "TWELVE TRIALS = flipped (being replaced, F12)" once the TRIALS rulebook edit lands (same commit).

**New C10, append after C9:**

> ## C10 · The house kit — **Settled (July 2026, decision memo HOUSE_KIT_DECISION_2026-07.md)**
>
> The Flip-Deck Collection is the 36-card master deck plus a tiny generic kit. Complete contents:
>
> - **The 36 double-faced cards** (DECK_SIZE_DECISION.md — unchanged).
> - **One shared Deck Handbook** (one page; ships inside every rulebook — see DECK_HANDBOOK.md).
> - **12 identical generic counters** — one shared pool serving JANUS's omens (6), THE COUNCIL's Speaker token, SLEEPER's optional first-player token, and the C5 flip tallies (TWELVE TRIALS, THE ORRERY). Any small objects substitute freely; the counters are a convenience, never a proprietary piece.
> - **One shared Nine Signs reference sheet** — front: the nine signs, their fixed ranks, and their one-idea mnemonic verbs (the C7 teach in printed form); back: the TRIGON and TURNCOAT ability tables (post Leaf/Key relabel, SIGN_MNEMONICS_proposal.md). Serves every rank-sensitive and ability game.
> - **The game box** — the published box base is the official opaque draw container (C2 rung 4) when a game explicitly says so (currently JANUS only). Production note: this requires a two-piece box, not a tuckbox. Prototype substitute: any mug, envelope, or bag.
>
> Nothing else ships. New component classes still face the graduated policy bar (COLLECTION_OVERVIEW): small, generic, off-the-shelf, reused by more than one game.

**T1, replace body with:**
"**Resolved (July 2026, D1/D3):** the container is the **game box base** (C10). JANUS's rulebook is rewritten around it and is playable-in-principle; JANUS remains parked outside the Core Set until a **concealed table test** passes — the F8 fan-handling risk is the remaining unknown, and only a table can retire it."

**T2, replace body with:**
"**Resolved (July 2026, D1/D4):** one shared **Nine Signs reference sheet** (C10). The SIGN_MNEMONICS Leaf/Key relabel is adopted (zero balance cost, confirmed against the live sim) and must be applied to the TRIGON rulebook before the sheet or the 9-icon commission is finalised."

**T3, replace body with (narrowed, not closed):**
"**Narrowed (July 2026):** the method is settled — C5 counters, counter-on-card for restore modes. The only open item is the table trial of counter-on-card in TWELVE TRIALS' Duel/replay (task K10). If it fails, the fallback is a written note or cutting the restore modes — a TRIALS-local decision."

## 5 · Frozen blind-test component list

**Player-facing (prints in the Handbook / box back):**
> Inside the box: **36 double-faced cards** · **1 rules booklet** (Deck Handbook + games) · **1 Nine Signs reference sheet** · **12 counters**. Some games ask you to draw cards blind from the box base. Lost the counters? Any coins or pebbles work.

**Designer/internal:**

| Item | Status | Notes |
|---|---|---|
| 36-card master deck | Required, frozen | 9 symbols, subsets per game |
| Rules booklet incl. one-page Deck Handbook | Required, frozen | G1 |
| 12 identical generic counters | Required, frozen | Serves 5 games; substitutes always legal |
| Nine Signs reference sheet (2-sided) | Required, frozen | Blocked only on Leaf/Key relabel + icon commission for final art; text version printable now |
| Two-piece box (base = draw container) | Required, frozen as *requirement class* | [GAP] confirm two-piece format is available/affordable at POD (Game Crafter quote); fallback = container claim carries "or any opaque cup/bag" |
| Household substitutes | Sanctioned | counters → any small objects; container → mug/envelope/bag |
| **Not included** | — | cloth bag, per-player screens/holders, colour-coded cubes, pencils/scorepad (paper stays optional for ORRERY), any bespoke per-game piece |

**Games incompatible with the frozen list:** none on components. JANUS (needs the concealed-play validation, not a component), SLEEPER (F8 ceiling unproven — component-free), RELAY (no rulebook) are blocked on other grounds.

## 6 · Game-by-game impact matrix

| Game | Affected convention(s) | Now compatible? | Required file edits | Still blocked? |
|---|---|---|---|---|
| JANUS | C2 rung 4, C10 counters (omens) | Playable-in-principle | Rewrite deal/refill around box-container; add keystone lift-freely line (BUG_AUDIT #11); soften banner to "awaiting concealed table test" | **Yes** — concealed table test (F8) |
| TRIGON | T2 sheet, C3 (already applied) | Yes | Leaf/Key relabel (table, worked example, FAQ line per SIGN_MNEMONICS); add sheet mention to Components; centre-first grid line is separate (K9) | Only the K9 gate re-test for Core status |
| TURNCOAT | T2 sheet, C3 (applied) | Yes | Add sheet mention to Components | No (table test pending, not kit-related) |
| TWELVE TRIALS | C5, C4 namespace, C10 | Yes (method basis) | Replace sideways-marking with counters + counter-on-card for Duel/replay; Components line → "the house kit's 12 counters"; fix "the collection's reference card" → "the almanac printed in this rulebook" (BUG_AUDIT #12) | K10 trial validates; restore modes at risk (T3) |
| THE ORRERY | C5, C10 | Yes | Add counter tally as the physical method (currently none); Components line update | K10 extension; 9-sym/full-game tests (ORRERY_tasks 2–3) |
| SLEEPER | C2 rung 3, C3 (both applied) | Yes | None | F8 concealment ceiling — first table test |
| WILDFIRE | C3 (applied) | Yes | None | No |
| GLEAN | C6 (applied), C7 | Yes | None (majority-scoring test is D4-audit, not kit) | No |
| BLIGHT | C6 exception (declared), C7 | Yes | None | No |
| FACE VALUE | C6 (applied), C7 | Yes | Add F4 sign-is-rank callout (BUG_AUDIT #9) | No |
| FORKED TONGUE | C2, C6 (applied) | Yes | None | No |
| THE COUNCIL | C10 counters (Speaker), C7 | Yes | Add F4 callout; optionally cite house-kit counter | No |
| THE UNPLAYED PAIR | C2 rung 3 (applied), C6, C7 | Yes | Add F4 callout (parked — low priority) | Parked by design (unchanged) |
| CROSSROADS | C4 (dimming, fine) | Yes | None from this decision (v1.2 banner stands) | Phase 3 end trigger (unchanged) |
| CAIRN / OUROBOROS | — | Yes | None | First table tests (not kit-related) |
| RELAY | C6 (concept) | Yes | Rulebook still to be written | No rulebook |

## 7 · Files to update

| File | Change | Dependency | Kiro now? |
|---|---|---|---|
| `DECK_CONVENTIONS.md` | All §4 edits (headers, C2 rung 4, C5 body, C6 note, C10, T1/T2/T3, C4 list) | None | **Yes** |
| **New: `DECK_HANDBOOK.md`** | One page per CORE_SET_AUDIT §5 spec (9 signs+ranks, F4 script, C1 shuffle, C2 ladder, C3 pile law, C5 counters, C6 sentence, C8 hand-size, C9 space) + the §5 player-facing component line | DECK_CONVENTIONS edits in same commit | **Yes** |
| `COLLECTION_OVERVIEW.md` (component inventory section only) | Add house-kit row; TRIALS/ORRERY rows → "house-kit counters (C5)"; JANUS row → "house kit: 6 counters as omens + box-as-container"; keep graduated policy text verbatim | DECK_CONVENTIONS C10 | **Yes** |
| `Trigon/TRIGON_rulebook.md` | Leaf/Key relabel per SIGN_MNEMONICS (table rows, worked example, FAQ line); Components: add sheet | None | **Yes** |
| `Turncoat/TURNCOAT_rulebook.md` | Components: add sheet (no mechanical change — SIGN_MNEMONICS confirms) | None | **Yes** |
| `Twelve Trials/TWELVE_TRIALS_rulebook.md` | Sideways-marking → counters (+ counter-on-card for Duel/replay) with "method scheduled for table validation" footnote; Components line; "collection's reference card" → "almanac printed in this rulebook" | None (do **not** wait for K10 — the shipped method is confirmed-failed, worse than untested) | **Yes** |
| `The Orrery/ORRERY_rulebook.md` | Add counter-tally as the physical method; Components line | None | **Yes** |
| `Janus/JANUS_rulebook.md` | Deal/refill protocol rewritten around box-container; keystone lift-freely FAQ line; banner → "container decided (C10); concealment awaiting table test"; purge "face-down stack" language | DECK_CONVENTIONS C10 | **Yes** (banner removal itself only after the test passes) |
| `PUBLISHING_PLAN.md` | §5d "tuckbox or small two-piece box" → "small two-piece box (base doubles as the C2 draw container)"; mark 90-day item 5 (T1/T3 settle) done; G5 noted frozen | This memo | **Yes** |
| `Designs/CARD_LAYOUT.md` | Clear F6/F12 annotations; orientation table rows corrected | C5 settled | **Yes** |
| `SIGN_MNEMONICS_proposal.md` | Header note: "Adopted July 2026 (house-kit decision); applied to TRIGON rulebook" | TRIGON edit | **Yes** |
| `DECK_BUG_AUDIT.md` | Tick punch items 1 (model decided — test pending), 6, 7; annotate 11, 12 as applied when they land | Above edits | **Yes** |
| New: `Reference/NINE_SIGNS_SHEET.md` (text master for the sheet) | Front/back content per C10; final art after icon commission | Leaf/Key relabel | **Yes** (text version) |

## 8 · Kiro-ready implementation tasks

**HK1 — Ratify conventions in DECK_CONVENTIONS.md.**
AC: C2/C3/C5/C6 headers read Settled with July 2026 date; C2 rung-4 row names the box; C10 present exactly per §4; T1/T2 resolved, T3 narrowed; C4 declaration list no longer contains TRIALS sideways=flipped.

**HK2 — Create DECK_HANDBOOK.md.**
AC: ≤1 page; contains all 9 items from CORE_SET_AUDIT §5 spec plus the player-facing component list from §5 above; canonical C6 sentence verbatim; no content contradicts any Settled convention.

**HK3 — Update component inventory (COLLECTION_OVERVIEW.md).**
AC: inventory table matches §5 frozen list; JANUS/TRIALS/ORRERY/COUNCIL/SLEEPER rows reference the house kit; graduated policy prose untouched; "verified" note re-dated.

**HK4 — JANUS status update.**
AC: rulebook deal/refill rewritten so every draw/deal names its C2 rung (deal = one-at-a-time blind draws from the container into the fan; refill = blind draw from container); zero remaining "face-down" phrases; keystone lift-freely line added; banner rewritten to "concealment model decided (C10 box-as-container) — parked pending a concealed table test (F8)"; COLLECTION_OVERVIEW JANUS entry mirrors this status.

**HK5 — TRIGON reference plan.**
AC: Leaf/Key rows swapped in the 9-sign table with mnemonics per SIGN_MNEMONICS proposed table; the one worked-example line and one FAQ line updated; Components lists the Nine Signs sheet; Reference/NINE_SIGNS_SHEET.md exists (text master: front = 9 signs, ranks, one-idea verbs; back = both ability tables); TURNCOAT Components lists the sheet; SIGN_MNEMONICS_proposal.md carries the adopted banner.

**HK6 — TRIALS/ORRERY flip-tally language.**
AC: TRIALS rulebook has no sideways-as-flipped rule anywhere (incl. Duel/replay, which now use counter-on-card), carries a one-line "method scheduled for table validation (K10)" footnote, and the almanac-reference-card fix; ORRERY rulebook names counters as the physical tally (paper stays optional for scoring); both Components lines cite the house kit; CARD_LAYOUT.md annotations cleared.

**HK7 — Ordinary-deck language sweep.**
AC: repo-wide grep for `face-down|face down|unseen|discard pile` over `*_rulebook.md` returns only: (a) physically-true flat-card uses (FACE VALUE duel card, SLEEPER loyalty card), (b) explicitly-negated teaching uses (GLEAN Closed Harvest "there is no face-down"), (c) archived files (SYZYGY). Every "unseen" names its C2 rung. JANUS is clean after HK4.

**HK8 — Bookkeeping.**
AC: DECK_BUG_AUDIT punch items 6 and 7 marked done, item 1 marked "decided — test pending"; PUBLISHING_PLAN edits per §7; this memo linked from CORE_SET_AUDIT D1/D2 lines.

*(Not Kiro: K10 counter trial and the JANUS concealed test are table sessions — Sam.)*

## 9 · Things not to change

Everything in CORE_SET_AUDIT §7 stands, in particular: the 36-card master deck; **C1's shuffle phrasing** (ratify-don't-rewrite applies to all convention bodies — this memo edits status lines, one rung cell, and one C5 clause only); the applied C3/F11 patches; the **graduated component policy** (C10 operates within it — the "reused by more than one game" bar is untouched and remains the test for any future kit addition); F2's pip placement; F1's constraint status; sim-tuned mechanics; the CROSSROADS v1.2-pending banner; parked statuses of THE UNPLAYED PAIR and (until its test) JANUS's outside-Core position. Additionally: do **not** rewrite the four rulebooks' existing C6 sentence variants to match the canonical form — they are compliant and validated; and do not reopen SIGN_MNEMONICS' rejected aggressive re-pairing (it skewed 3-player seats [FILE]).

## 10 · Residual open risks

1. **K10 counter trial** — counter tally is low-risk; the real question is counter-on-card restore for TRIALS' Duel/replay (T3 fallback: written note or cut the modes). [GAP]
2. **JANUS concealed table test** — the container solves F7/F10, but F8 (fan handling; the first table abandoned concealment) may still sink JANUS. Parked status protects the plan either way. [GAP]
3. **Two-piece box at POD** — unverified that Game Crafter/offset pricing supports it at target cost; fallback wording already in §5. Check in the pending quote. [GAP]
4. **Sheet legibility** — the reference sheet's final form depends on the 9-icon commission and must pass the symbol_recognisability_test protocol; the text master is not the final aid. [GAP]
5. **12-counter sizing** — ORRERY's worst 9-symbol deals could exceed 12 flips; substitutes make this cosmetic, but confirm during ORRERY tasks 2–3 before print files freeze. [GAP]
6. **SLEEPER's F8 ceiling** — unchanged by this decision; its first table test remains a deck test.
