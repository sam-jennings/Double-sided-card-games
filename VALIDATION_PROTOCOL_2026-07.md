# 90-Day Validation Protocol — July–October 2026

*The validation plan that turns the Flip-Deck Collection from "internally coherent" into "ready for external blind testing and publisher scrutiny." Ground truth: CORE_SET_AUDIT_2026-07.md (Core Set locked), HOUSE_KIT_DECISION_2026-07.md (kit locked), DECK_HANDBOOK_HANDOFF_2026-07.md (Handbook locked), DECK_CONVENTIONS.md, DECK_PLAYTEST_FINDINGS.md (F1–F12), DECK_BUG_AUDIT.md, PUBLISHING_PLAN.md. Every scheduled test answers a decision question; there are no "get feedback" sessions. Budget: 5–10 hrs/week, 13 weeks, limited local testers (household group: Lauren, Arran, parents).*

*Sessions are named (BL-2 = BLIGHT session 2, etc.) and referenced from the calendar (§2), the gates (§3), and the scripts (§4). Kiro/Opus implement the desk work (§6); Sam runs the tables.*

---

## 1 · Executive 90-day verdict

**What the 90 days are trying to prove:** that the declared Core Set — BLIGHT (flagship), GLEAN (conditional), WILDFIRE (opener), FACE VALUE (2P), CAIRN (solo), TRIGON (conditional) — survives contact with (a) its own untested configurations, (b) the settled house kit and Handbook, and (c) at least one group of players Sam is not sitting with. Secondary: that the C5 counter method is validated so TWELVE TRIALS / THE ORRERY have a live pipeline path, and that CROSSROADS' one reclaim clause is discharged either way.

**Success at day 90 looks like:**

- BLIGHT confirmed flagship: comfortable at 9-card hands, luck complaint washed out by the match structure, and **one blind group has played a full round from the Handbook + rulebook with Sam out of the room**. This is PUBLISHING_PLAN goal G4's Stage-7 entry condition and the single most important outcome of the quarter.
- GLEAN's majority scoring proven at the table with the F4 teach script, or cleanly demoted to PNP extra per D4 — either is a success; limbo is the failure.
- Every conditional/provisional Core Set slot resolved by evidence: TRIGON promoted or demoted (Core Set = 6 or 5), FACE VALUE tabled and holding the 2P slot, CROSSROADS' reclaim clause spent, CAIRN confirmed and packaged for the BGG Solitaire PNP contest.
- The counter method (C5) table-validated, including the counter-on-card restore or its recorded fallback (T3).
- The Handbook + house kit validated as instruments: the known F1/F4/F9 failure modes do not recur in front of testers who were given the Handbook.
- The external-testing machinery exists: feedback form in use, Screentop build started, first BGG WIP thread live, one contest entry queued.

**Failure at day 90 looks like:** any Core Set slot still "provisional" without a scheduled test that resolves it; a blind test postponed because something was being polished; CROSSROADS having consumed more than its one session; table time spent on parked games; or gate decisions deferred because the result was disliked. A demotion made on evidence is a pass; an unresolved slot is the only fail.

**The one thing this quarter does not do:** reopen the Core Set, the house kit, or the Handbook wording. Tests can *invalidate* those decisions (§3 says exactly how); nothing else can.

---

## 2 · Validation calendar — 13 weeks

*Rhythm: one table block + one desk block per week. Table sessions have scripts in §4. Multiplayer evenings need Lauren/Arran and/or parents booked ahead — recruit dates for weeks 2, 4, 7, 8, 10 in week 1. Solo sessions are schedule-proof and can swap weeks freely; multiplayer evenings are the fixed skeleton. Hours are estimates; every week fits 5–10.*

| Week | Table work | Desk work | Hrs |
|---|---|---|---|
| **1** (Jul 6–12) | **TT-1** — TWELVE TRIALS counter trial: one full solve with counters + counter-on-card Duel restore (solo, §4.1) | **VP1** Kiro sweep: confirm HK1–HK8 + DH1–DH6 landed; print the session kit (Handbook, Nine Signs sheet text master, F4 script card, 12 counters); book testers for wks 2/4/7/8/10; Kiro drafts playtest plan files from §4 scripts | 6 |
| **2** | **Evening A** — **WF-2** WILDFIRE second test as 15-min warm-up (§4.3), then **BL-2** BLIGHT full match at 4P, 3P full-match fallback (§4.2) | Write reports (Templates/Playtest Report); update DECK_PLAYTEST_FINDINGS if deck-general findings emerge | 6 |
| **3** | **CA-1** — CAIRN first table test, 6–8 deals per existing plan (solo, §4.5) | **VP2** — CROSSROADS eighth-dim end-trigger sim (Phase 3, crossroads_sim.py); this is the CR-3 prerequisite | 7 |
| **4** | **Evening B** — **GL-2** GLEAN majority scoring at 3–4P with the F4 script + Nine Signs sheet (§4.4) | Reports; log Nine Signs sheet teach-aid observations against G10 | 5 |
| **5** | **FV-1** — FACE VALUE first table test, 2P (§4.6). **OR-1** — THE ORRERY 2–3 random 7-sym deals with counters (solo, §4.7, same week) | Reports | 6 |
| **6** | *(none — gate week)* | **GATE WEEK 1 (~day 42):** decide G1 BLIGHT, G2 GLEAN, G3 WILDFIRE, G4 counters, G5 CAIRN, G8 FACE VALUE-provisional (§3). Kiro applies §8 file updates; **VP3** CROSSROADS on-spec crib sheet from VP2 results; **VP4** TRIGON session prep (centre-first setup line + printed sheet) | 6 |
| **7** | **TR-2** — TRIGON gate re-test at 2P: centre-first grid + Nine Signs sheet (§4.8). This is PUBLISHING_PLAN's ~day-45 gate | Report; decide **G6** | 6 |
| **8** | **CR-3** — CROSSROADS reclaim session, 2P, on-spec, one only (§4.9) | Report; decide **G7**; start blind-kit prep | 6 |
| **9** | *(none — gate week)* | **GATE WEEK 2:** file G6/G7 consequences (Kiro: K1 Core Set declaration draft, TRIGON promote/demote edits; CROSSROADS v1.2 rewrite **only if G7 passed**). **VP5** blind kit: print Handbook + BLIGHT rulebook + feedback form (from Templates/Playtest Report, one page); recruit the ring-1 group and a date. If G1+G2 passed: draft the 9-icon commission brief (F1/F4/colourblind/rotation requirements) per PUBLISHING_PLAN month-2 item 12 | 7 |
| **10** | **BL-3** — Ring-1 blind test: BLIGHT + Handbook, **Sam out of the room** (§4.10) | **VP6** — Screentop.gg deck build started | 7 |
| **11** | **CA-2** — CAIRN cold-read hand-off: rulebook-only, Sam absent, any solo tester (§4.11) | **G9** decision; iterate Handbook/BLIGHT rulebook text on blind findings (text fixes only — no rule changes without a named observation) | 6 |
| **12** | *(only if G9 failed:)* second ring-1 blind session with revised text | **VP7** — BGG WIP thread for BLIGHT (PNP files + Handbook); join Break My Game; package CAIRN for the BGG Solitaire PNP contest (entry when the window opens); Screentop build finished | 7 |
| **13** | *(none)* | **DAY-90 REVIEW (G10):** final Core Set declaration in COLLECTION_OVERVIEW (K1 complete), write `VALIDATION_REVIEW_2026-10.md` (gate outcomes, verdicts, evidence links), sync PUBLISHING_PLAN, set the month-4–6 plan (ring-2 remote sessions, publisher shortlist research, second contest) | 6 |

**Standing rules for the calendar:**

- Solo sessions (TT-1, CA-1, OR-1, CA-2) may move to any week without penalty; multiplayer evenings anchor the plan.
- If a multiplayer evening collapses (testers unavailable), pull a solo session forward and re-book — never substitute an off-spec session to save the date. An off-spec session answers nothing (CROSSROADS has proven this twice).
- **SLEEPER opportunistic rider (the only sanctioned parked-game table time):** if an evening assembles 4+ players *and* finishes early, a 20-minute SLEEPER probe may run — it answers the deck-wide F8 concealment-ceiling question ("can one flat pressed card be guarded all game?"), which caps every future hidden-info design. It is never scheduled, never displaces a Core Set test, and its script is §4.12. JANUS gets **zero** table time this quarter — box-draw playable-in-principle does not change its parked status (HOUSE_KIT_DECISION D3).
- No new game concepts, no RELAY rulebook, no TURNCOAT session — the pipeline is rich enough (PUBLISHING_PLAN "deliberately absent" list stands).

---

## 3 · Decision gates

*Each gate is decided in a gate week from written playtest reports, not from memory. "Fail" consequences execute immediately — deferring a demotion is the failure mode this protocol exists to prevent.*

### G1 — BLIGHT flagship confirmation *(evidence: WF-2/BL-2 report; decide week 6)*

- **Decision:** is BLIGHT still the flagship after the 4P / 9-card / full-match test?
- **Evidence needed:** hand-handling observations at 9 cards vs the recorded 12-card pain (F1); per-player luck complaints tracked across a full match; whether a shoot-the-rot attempt or threat surfaced.
- **Pass:** 9-card hands draw no per-trick stall complaints; the "bad hand, no recovery" objection does not survive the rotating-lead match (or the complainer's view visibly shifts once slough-as-weapon is seen/taught); no new rules disputes.
- **Fail:** hand-handling at 9 still dominates the session, **or** the luck complaint persists across a full match from more than one player.
- **Consequence:** pass → flagship confirmed, BL-3 blind test proceeds as scheduled. Fail on handling → one 6P (6-card) config test replaces a week-9 desk block before any demotion talk; fail on luck → trial The Passing (pass 3) as default in that same extra session. Two fails → flagship story falls back to "BLIGHT + GLEAN, one deck, two trick-takers" with FACE VALUE as second pitch (CORE_SET_AUDIT §1), and the day-90 review re-plans. BLIGHT is not demoted from the Core Set by this gate — only its *flagship* label is at stake.

### G2 — GLEAN Core condition (D4) *(evidence: GL-2 report; decide week 6)*

- **Decision:** does GLEAN ship in the Core Set, or become a variant/PNP extra?
- **Evidence needed:** whether counting nine simultaneous sign-majorities at round end is frictionless; whether any rank-structure confusion survives the delivered F4 script + Nine Signs sheet; whether 9-dominance flattens under majorities (GLEAN playtest 01 B4).
- **Pass:** majority count completes in under ~2 minutes without disputes; zero rank-structure errors after the script; players contest majorities during play (captures feel motivated).
- **Fail:** the count is a table-stopper, or a player again plays a full session on a wrong rank model despite the script.
- **Consequence:** pass → GLEAN Core-confirmed; rulebook scoring text confirmed as-is. Fail on counting → one desk pass on a counting procedure (e.g. sort-by-sign sweep) then a re-test *only if* the fix is procedural, not a rules change; fail on comprehension or second fail → **D4 executes: GLEAN demoted to PNP extra, BLIGHT ships alone, Core Set loses the companion slot** and the "two trick-takers" pitch line is retired from PUBLISHING_PLAN.

### G3 — WILDFIRE framing *(evidence: WF-2 report; decide week 6)*

- **Decision:** is WILDFIRE a filler with a real decision, or purely "teach the deck" — and which framing do its rulebook/pitch materials use?
- **Evidence needed:** whether Inferno (chain 3) produces at least one visible don't-chain decision; whether the announce rule is fun or dead weight.
- **Pass (either way is a pass — this gate picks a framing, not a survival verdict):** a visible hold-back-the-chain moment occurs → keep "light filler, sharper with Inferno" framing and recommend Inferno for experienced tables. No such moment → adopt "teach the deck in 10 minutes" framing officially; stop testing for depth.
- **Fail:** n/a — WILDFIRE's opener slot is not at stake (zero-clarification teach is already proven).
- **Consequence:** framing recorded in the rulebook's intro line and PUBLISHING_PLAN §3; WILDFIRE testing **stops** for the quarter either way (stop condition §7).

### G4 — Counter method (C5/T3, K10) *(evidence: TT-1 + OR-1 reports; decide week 6)*

- **Decision:** does the settled counter method survive the table, and does counter-on-card restore work for TWELVE TRIALS' Duel/replay?
- **Evidence needed:** one full TRIALS solve with counters (does state survive regrouping? overhead acceptable?); one Duel-restore attempt (remove counters → deal restored correctly?); ORRERY random deals using the counter tally; whether 12 counters sufficed (G10 input).
- **Pass:** tally survives a full solve with no lost state; restore reproduces the deal; counters never run out.
- **Fail (tally):** counters get lost/knocked/forgotten during regrouping — this would be a *convention-level* surprise; escalate to a T3-style review, but per HOUSE_KIT_DECISION the convention stands unless the failure is fundamental, since the incumbent is confirmed-failed and there is no third candidate.
- **Fail (restore only):** T3 fallback executes as a TRIALS-local decision — written note, or cut the Duel/replay restore modes. Does not touch C5.
- **Consequence:** pass → TRIALS/ORRERY pipeline path is live; record the D6 recommendation (TRIALS holds the eventual seventh-slot claim) — but **neither promotes to Core this quarter** regardless of result, per the locked decision, unless the day-90 review judges the evidence "unexpectedly strong" *and* a slot opened (e.g. TRIGON demoted). ORRERY additionally logs whether sky debt reads as fair benchmark or tedious arithmetic (its own iterate loop, outside this protocol's gates).

### G5 — CAIRN solo slot + contest readiness *(evidence: CA-1 report; decide week 6)*

- **Decision:** is CAIRN Core-confirmed for the solo slot, and strong enough to submit to the BGG Solitaire PNP contest?
- **Evidence needed:** loss-cause tally per deal (foreseeable stranding / unlucky run / no-win deal); clear-rate vs the sim's ~74–98% band; tray-footprint check; free-look discovery.
- **Pass:** most losses trace to a nameable earlier misplay; standard clear rate lands in or near the band; footprint fits a tray; player wants to redeal after a loss.
- **Fail:** losses read as shuffle blame ("the draws killed me") across multiple deals, or the footprint creeps beyond a tray.
- **Consequence:** pass → Core-confirmed; CA-2 cold-read scheduled (contest requires the rulebook to teach unaided); contest packaging in week 12. Fail on feel → one iteration (hand size / First Trail ladder) then one re-test; contest entry off until it passes. Fail twice → solo slot ships with CAIRN as "provisional" flagged in the day-90 review, and the review decides whether OUROBOROS's first test is the month-4 replacement candidate.

### G6 — TRIGON depth-slot gate *(evidence: TR-2 report; decide week 7 — the ~day-45 gate)*

- **Decision:** promote TRIGON to Core-confirmed depth slot, or demote to expansion tier and ship the Core Set with 5 games.
- **Evidence needed:** at 2P with centre-first grid + Nine Signs sheet mid-table: are reference stalls gone (turns flow without rulebook consults)? Is grid drift eliminated? Does the engine finally breathe (capture cadence readable)?
- **Pass:** no laptop/rulebook consults needed after the first two turns; grid positions never disputed; at least a preliminary read on capture drama.
- **Fail:** the sheet does not stop per-turn look-ups, or the grid drifts again despite centre-first.
- **Consequence:** pass → Core-confirmed; centre-first line and sheet reference land in the rulebook (already drafted, VP4). Fail → **demote to expansion tier in COLLECTION_OVERVIEW + PUBLISHING_PLAN, Core Set = 5, no further TRIGON work before month 4** (CORE_SET_AUDIT K9 — sunk sim cost does not vote). A fail here also strengthens the case for FACE VALUE's Cold Read as the second depth story — note it in the day-90 review.

### G7 — CROSSROADS reclaim clause *(evidence: CR-3 report; decide week 8)*

- **Decision:** does CROSSROADS re-enter the 2P Core discussion, or stay pipeline with FACE VALUE's slot confirmed?
- **Evidence needed:** one session, on-spec **as locked**: 2P, deal-9, Toll scoring in base, Signal Fires actually used, pass-to-win deliberately attempted, eighth-dim end trigger (per VP2 sim) in force.
- **Pass:** the session runs on-spec to completion; pass-to-win loses at the table; the end trigger resolves the twice-flagged unfairness; Toll's route-trace scoring is not a handling burden.
- **Fail:** pass-to-win still competitive, or the end trigger still feels unfair, **or the session drifts off-spec in any way** — off-spec = automatic fail of the reclaim clause, not a reschedule.
- **Consequence:** pass → CROSSROADS may re-enter Core discussion at the day-90 review (it challenges for the 2P slot only if FACE VALUE failed G8; otherwise it queues as pipeline-strong) and the v1.2 rulebook rewrite is authorised (Kiro, §6). Fail → **stays pipeline, banner stands, FACE VALUE's 2P slot is permanent, and no CROSSROADS table time for the rest of the quarter.** The clause is spent either way — there is no second reclaim session.

### G8 — FACE VALUE 2P slot *(evidence: FV-1 report; decide week 6, provisional)*

- **Decision:** does FACE VALUE hold the default 2P slot it took from CROSSROADS?
- **Evidence needed:** per FACE_VALUE_playtest_plan_01's H1–H4: at least one information-protecting fold; cold reads clustering late off a real count; acting-last respected; the shown face read as a claim. Plus pacing (~12 duels ≈ 15–20 min) and deck-necessity (morgue/tally counting actually happens).
- **Pass:** H1 + H4 hold and pacing holds (H2/H3 may stay open on one session).
- **Fail:** every duel goes to showdown and the shown face is ignored — the bluffing layer is dead with humans.
- **Consequence:** pass → provisionally confirmed; full confirmation needs one clean session with non-household players (ring 2+, month 4). Fail → the 2P slot question reopens *only within* the locked options: CR-3's result decides whether CROSSROADS inherits it or the Core Set ships without a dedicated 2P game this quarter — logged for the day-90 review; no new 2P design work.

### G9 — Handbook / house-kit validation *(evidence: BL-3 blind report + accumulated kit observations; decide week 11)*

- **Decision:** is the Deck Handbook v0.1 doing its job — does it prevent the known F1/F4/F9/F10/F12 confusion classes in front of players Sam isn't coaching?
- **Evidence needed:** blind group's first-read confusions from the feedback form, mapped against the findings they'd exhibit without the Handbook (hand-sort frustration F1, rank-structure error F4, pile confusion F9, "unseen" disputes F10, tally problems F12); plus the quarter's accumulated observations: did 12 counters suffice everywhere (TT-1, OR-1)? Did the Nine Signs sheet visibly cut teach/reference time (GL-2, TR-2)?
- **Pass:** the blind group completes a full BLIGHT round unaided; no F4 rank error occurs; piles are never confused; the sheet was used mid-game rather than the rulebook.
- **Fail:** a known-class confusion recurs that the Handbook text was written to prevent.
- **Consequence:** pass → Handbook v1.0 declared (text frozen harder; only blind-test evidence edits it from here). Fail → targeted text iteration (the failing item only — DH4 discipline: fix the Handbook, never a settled convention) and one re-run in week 12. Counter-count or sheet failures → house-kit *contents* are not reopened (locked); record as a production note (e.g. counter count revisited at print-file freeze per HOUSE_KIT_DECISION risk 5).

### G10 — Day-90 verdict *(evidence: everything above; decide week 13)*

- **Decision:** the final Core Set declaration (K1), the flagship story, and the month-4–6 external plan.
- **Pass condition for the quarter itself:** every slot above is resolved (confirmed or demoted, none provisional-without-a-plan), the reclaim clause is spent, and at least one blind session has produced a written report.
- **Consequence:** COLLECTION_OVERVIEW restructured around the declared set; `VALIDATION_REVIEW_2026-10.md` written; PUBLISHING_PLAN month-4–6 section updated (ring-2/3 escalation, publisher shortlist research via Cardboard Edison, second contest cycle, indicative offset quote).

---

## 4 · Playtest scripts

*Kiro turns each script into a `*_playtest_plan_NN.md` in the game's folder (per playtesting.md) before the session; Sam writes the paired report after. Common to every session: the printed Handbook is on the table from session 1 onward (it is itself under test); the observer notes any house-kit friction (counters, sheet, box) for G9; any deck-general observation goes to DECK_PLAYTEST_FINDINGS as a new F-number. "What not to test" is binding — scope creep is how CROSSROADS lost two sessions.*

### 4.1 TT-1 — TWELVE TRIALS counter trial *(week 1, solo)*

- **Game / version:** TWELVE TRIALS, current rulebook with HK6 applied (counters replace sideways-marking; sideways rule gone).
- **Players:** 1. **Setup:** full 36-card deal, random; 12 house-kit counters at hand; workspace zones per task #3 (pool centre / staging / locked seasons at the edge).
- **What to test:** (1) counter-per-flip tally through a full solve — does state survive constant regrouping? (2) at solve end, attempt the **Duel restore**: counters sit on flipped cards; remove them one by one to restore the original deal — is it exact? (3) record the final flip count (task #2 / H1: does a thoughtful solve land near 7? solver 5.3, unoptimised 9). (4) do 12 counters suffice?
- **What not to test:** completion-mode scoring variants, co-op, 7-symbol subsets, any tier re-tuning.
- **Observer checklist (self-observe):** counters knocked/displaced during regrouping? counter-on-card vs counter-in-pool ever confused? tally checked mid-solve without breaking flow? workspace zones actually used or abandoned?
- **Post-game questions:** was the tally overhead noticeable next to the puzzle itself? Would you trust the restore in a competitive Duel?
- **Pass/fail:** pass = no lost state, exact restore, counters sufficient. Restore-only fail → G4's T3 fallback. Record flips vs the 7-flip hypothesis separately (it informs tiers, not the gate).
- **Files afterward:** append to TWELVE_TRIALS_playtest_01.md (or write 02); tick TRIALS tasks #1–3; DECK_BUG_AUDIT punch #4 closed if pass; DECK_CONVENTIONS T3 narrowed→closed or fallback recorded.

### 4.2 BL-2 — BLIGHT full match at 4P *(week 2, Evening A)*

- **Game / version:** BLIGHT v1.0, rulebook as-is (sim-tuned trick engine untouchable).
- **Players:** 4 (Sam + 3 — book Lauren, Arran + one parent/other). **Fallback if only 3:** full 3-round match at 3P — this still answers luck-washout; the 9-card handling question then moves to the week-9 contingency slot. Do not run a single round; the match structure is itself under test.
- **Setup:** full 9-sign deck; 9 cards each at 4P; **full match, one round per player, rotating lead**; C7/F4 teach script delivered aloud before the deal; Nine Signs sheet mid-table; Handbook available.
- **What to test:** (1) hand handling at 9 cards vs the recorded 12-card pain — time the per-trick follow decisions loosely; (2) whether the luck complaint survives a full match with rotating lead; (3) whether shoot-the-rot is ever attempted or visibly feared; (4) teach the slough-as-weapon line up front this time ("showing a low face lands the hidden face in the winner's pile") — does pre-teaching it change Lauren's read?
- **What not to test:** The Passing variant (it is the *contingency* lever, not this session), 6P config, any scoring change.
- **Observer checklist:** per-trick re-scan stalls (count them, roughly); rot-pile self-totalling working; any rules dispute (there were zero at test 1 — a regression matters); who notices shoot potential; sheet consulted instead of rulebook?
- **Post-game questions:** to the week-1 complainer specifically: did the match structure change the "bad hand" feeling? To all: at 9 cards, did your hand feel manageable? Was there a moment you considered taking every trick?
- **Pass/fail:** per G1.
- **Files afterward:** BLIGHT_playtest_02.md; DECK_PLAYTEST_FINDINGS F1 update (9-card data point — C8 comfort line evidence); COLLECTION_OVERVIEW BLIGHT entry.

### 4.3 WF-2 — WILDFIRE Inferno probe *(week 2, warm-up before BL-2, ~15 min)*

- **Game / version:** WILDFIRE v1.1 rulebook + **Inferno variant (chain 3)** from the start; announce rule enforced.
- **Players:** same table as BL-2 (3–4). **Setup:** standard deal; one game of Inferno; if it finishes fast, one standard game for contrast.
- **What to test:** (1) does chain-3 surface a visible don't-chain decision (someone holds back a legal chain and can say why)? (2) is announce-rule policing fun, dead, or annoying? (3) does Inferno feel faster/sharper as the sim claims?
- **What not to test:** Salvage variant, chain/refusal retuning (sim-settled, protected), skill-depth claims — one warm-up cannot prove depth, only whether a decision *exists*.
- **Observer checklist:** any refused chain; any table-talk pricing a chain ("if I chain now I lose my Flame"); announce slip-ups and reactions.
- **Post-game questions:** did you ever choose not to chain? Did the game feel like it had choices, or just speed?
- **Pass/fail:** per G3 — either outcome locks a framing; there is no fail.
- **Files afterward:** WILDFIRE_playtest_02.md; rulebook intro framing line per G3; COLLECTION_OVERVIEW entry un-staled (cites both playtests).

### 4.4 GL-2 — GLEAN majority scoring *(week 4, Evening B)*

- **Game / version:** GLEAN, current rulebook: **full majority scoring** (nine sign-majorities, claimed sign = pip value), open harvests per C6. Proto-majority Plunder is available as a 5-minute on-ramp only if the table wants one.
- **Players:** 3 or 4 (whoever is bookable; 3P/12 cards is fine — the question is scoring, not hand size).
- **Setup:** full deck; **F4 teach script delivered verbatim aloud before dealing** (this is itself under test); Nine Signs sheet mid-table; match with rotating lead if time allows.
- **What to test:** (1) is the nine-majority count at round end frictionless — time it; (2) does any rank-structure confusion survive the script + sheet (the F4 re-test); (3) do majorities motivate play mid-round (contested signs, deliberate ducks); (4) does 9-dominance flatten under majorities (playtest 01 B4); (5) does the open harvest feel purposeful now that the registry matters (T4 data point — observe only).
- **What not to test:** Closed Harvest variant (T4 stays open; don't resolve it this session), Plunder retuning, hand-size questions.
- **Observer checklist:** count duration + any dispute; players checking harvests mid-round (registry earning its keep); any "wait, which sign is 7?" moment (sheet failure); captures chosen for majority reasons vs reflex.
- **Post-game questions:** could you say who was winning Crown before the count? Did knowing every sign's fixed strength change your play from last time (returning players)? Was the count satisfying or a chore?
- **Pass/fail:** per G2.
- **Files afterward:** GLEAN_playtest_02.md; on pass, rulebook scoring text confirmed (note in file header); on fail, D4 demotion edits (§8); COLLECTION_OVERVIEW entry un-staled; F4 status update in DECK_PLAYTEST_FINDINGS.

### 4.5 CA-1 — CAIRN first table test *(week 3, solo)*

Runs **exactly per the existing `Cairn/CAIRN_playtest_plan_01.md`** (session shape: 1 First Trail → 3–4 standard → 1 Pathfinder → 1 Long Trail; H1–H6; loss-cause tally; cold-read of the rulebook as the teacher). That plan is already this protocol's standard — no changes. Additional G10 observation: does the whole game + Handbook + sheet fit the tray footprint claim?
- **Pass/fail:** per G5 (H2 — blocked-feels-foreseeable — is the gate question; H1/H3–H6 inform iteration).
- **Files afterward:** CAIRN_playtest_01.md (report); COLLECTION_OVERVIEW entry Stage 2→3; on pass, contest earmark noted in PUBLISHING_PLAN.

### 4.6 FV-1 — FACE VALUE first table test *(week 5, 2P)*

Runs **exactly per the existing `Face Value/FACE_VALUE_playtest_plan_01.md`** (H1–H4, Quick Draw teaching duel first, morgue/tally counting watch, ~12-duel pacing check). One addition per HOUSE_KIT/DH punch list: confirm the **sign-is-rank callout** (newly added to the rulebook) is present and lands during the teach.
- **What not to test:** Tell/High Stakes/Best of Three variants; fee retuning (design-analysis dials — observe, don't tune).
- **Pass/fail:** per G8.
- **Files afterward:** FACE_VALUE_playtest_01.md; COLLECTION_OVERVIEW entry Stage→3; 2P-slot status note pending G7.

### 4.7 OR-1 — THE ORRERY random deals with counters *(week 5, solo)*

- **Game / version:** ORRERY v0.2 (split-cycle terminology fixed) + HK6 counter tally.
- **Players:** 1. **Setup:** 7-symbol sub-deck, **2–3 random deals** (no pre-balancing), full scoring: count sky debt at setup, counter-per-flip tally, per ORRERY tasks #2.
- **What to test:** (1) counter tally in ORRERY's move-heavy solve (the G4 extension); (2) does sky debt read as a fair benchmark or tedious arithmetic; (3) do split-cycle solutions feel valid under the new wording; (4) counter headroom (worst deal vs 12 counters — HOUSE_KIT risk 5).
- **What not to test:** the 9-symbol full game (task #3 — month 4, after the method is proven), Clockmaker's fate (task #4), any TRIALS comparison judgment.
- **Observer checklist:** tally drift; sky-debt count duration; any urge to reach for paper (the involuntary-bookkeeping tell).
- **Post-game questions (self):** did flips feel like the interesting cost or bookkeeping? Would a stranger tolerate the sky-debt count?
- **Pass/fail:** counter portion per G4; sky-debt/feel answers feed ORRERY's own iterate loop, not a gate.
- **Files afterward:** ORRERY_playtest_02.md; ORRERY tasks #2 ticked; counter-headroom note against HOUSE_KIT risk 5.

### 4.8 TR-2 — TRIGON gate re-test *(week 7, 2P)*

- **Game / version:** TRIGON rulebook with the Leaf/Key relabel (HK5, already applied) + the **centre-first grid setup line** (VP4 draft: "the first card placed is the centre cell; the 3×3 extends one cell in each direction from it").
- **Players:** 2 (Sam + one returning player from test 1, ideally — drift recurrence is best judged by someone who drifted).
- **Setup:** full deck; **printed Nine Signs sheet mid-table, rulebook physically closed** after the teach (the point is to force reference load onto the sheet); no laptop.
- **What to test:** (1) grid drift — do positions stay fixed all game? (2) reference stalls — count rulebook opens after turn 2 (target: zero); (3) with handling fixed, first read on capture cadence (H1) and the "active player captures everything" swing (H3); (4) does a second game lift play out of aimless placement (Bug 5)?
- **What not to test:** balance, ability retuning (sim-tuned, protected), 3–4P, Calm Signs staging (only if the full game stalls badly — then note it as evidence, not as a rescue).
- **Observer checklist:** any centre/edge/corner dispute; sheet flips vs rulebook opens (tally both); requirement-vs-ability confusion recurrence (the new front-loaded line's test); turn length trend across the game.
- **Post-game questions:** could you plan a capture two turns out? Did any ability feel unusable without the book? Would you play again tonight?
- **Pass/fail:** per G6 — this is a hard gate with a named demotion consequence.
- **Files afterward:** TRIGON_playtest_02.md; pass → centre-first line confirmed in rulebook, COLLECTION_OVERVIEW Core-confirms the depth slot; fail → §8 demotion set (overview, publishing plan, "no TRIGON before month 4" note).

### 4.9 CR-3 — CROSSROADS reclaim session *(week 8, 2P, one only)*

- **Game / version:** the settled design, **not** the v1.1 rulebook — played from the VP3 crib sheet: deal 9 roads each (rest aside), **Toll scoring in the base game**, Signal Fires pool live, **eighth-dim end trigger** as parameterised by the VP2 sim. The v1.1 book stays bannered and untouched.
- **Players:** 2 — the locked spec. If a second player can't be booked, the session moves weeks; it is never played 3P.
- **Setup:** 9 signs (7-sym is cut); pie rule start; both players briefed that **someone must deliberately attempt pass-to-win** for a sustained stretch (assign it — Sam takes the passer seat, since the strategy is his to disprove).
- **What to test:** (1) does pass-to-win lose at the table as the sim predicts (0–8% vs aware play)? (2) does the eighth-dim trigger kill the asymmetric-readiness unfairness? (3) the twice-dodged flip-economy questions: does spending eight shared flips ache properly? does dimming read at a glance? (4) does Toll's route-trace scoring handle cleanly? (5) does 2P at H=9 feel satisfying or thin (fallback dial: H=10)?
- **What not to test:** 3P/4P, layout candidates beyond whatever VP3 names (pick one, note friction), draft variants, anything not on the crib sheet. **Any drift off-spec ends the reclaim attempt as a fail** — stop the session rather than improvise.
- **Observer checklist:** flips actually spent (count them — "barely used" = off-spec); passer's score trajectory; end-trigger moment: did either player feel trapped? Toll trace duration at game end.
- **Post-game questions:** to the non-passer: did you feel you had the tools to punish the passing? Did the ending arrive fairly? Was 9 cards enough to feel like a hand of options?
- **Pass/fail:** per G7. The clause is spent when the session ends, whatever the result.
- **Files afterward:** CROSSROADS_playtest_03.md with verdict per count; pass → v1.2 rewrite authorised (Kiro, §6) + Phase 3/6 tasks unblocked; fail → pipeline status + banner reaffirmed, COLLECTION_OVERVIEW 2P row = FACE VALUE.

### 4.10 BL-3 — Ring-1 blind test: BLIGHT + Handbook *(week 10, Sam absent)*

- **Game / version:** BLIGHT rulebook (post-G1 text) + Deck Handbook v0.1, both printed; PNP deck; Nine Signs sheet; 12 counters in the kit even though BLIGHT doesn't use them (the kit ships whole — its presence is part of the test).
- **Players:** 3–4 locals (Lauren/Arran group or colleagues) — **people who have not been taught BLIGHT by Sam this quarter if possible; at minimum, Sam leaves before setup and stays out.**
- **Setup:** hand over the box contents and the one-page feedback form (VP5). No verbal teach, no questions answered — a phone note of anything they'd have asked.
- **What to test:** (1) can the group set up, teach themselves, and complete a full round unaided (PUBLISHING_PLAN goal G4 — the Stage-7 flagship entry test)? (2) does the Handbook prevent the known confusion classes — F1 (hand-sort frustration handled by the C8 guidance), F4 (rank structure — does anyone play on a wrong model?), F9 (pile confusion), F10 ("unseen" disputes), F12 (n/a for BLIGHT — but note if they invent tracking needs)? (3) first-read confusions in the rulebook, verbatim.
- **What not to test:** full match (a round is the bar), variants, any other game — resist "while you're here, try…".
- **Observer checklist (via form + debrief, since Sam is absent):** minutes from box-open to first trick; rules re-read moments (which section); what the Handbook page was used for, if anything; the three questions they most wanted to ask.
- **Post-game questions (form):** what confused you first? What did you get wrong that the rules had actually covered? Would you play again — and which game in the box description sounds most appealing? (The last is early pitch data.)
- **Pass/fail:** per G9 + G1's blind condition: full round completed unaided = pass.
- **Files afterward:** BLIGHT_playtest_03_blind.md; Handbook/rulebook text iterations (week 11, text-only); PUBLISHING_PLAN §5a ring-1 marked done; feedback form template refined for ring 2.

### 4.11 CA-2 — CAIRN cold-read hand-off *(week 11, Sam absent, solo tester)*

- **Setup:** CAIRN rulebook + 21-card sub-deck to one person, alone, with the form. The rulebook is the teacher — this is the Solitaire-PNP-contest condition (contest players get exactly this experience).
- **What to test:** setup correct from text alone? First deal played legally? Loss condition understood before it happens?
- **What not to test:** difficulty ladder, scoring tiers.
- **Pass/fail:** legal unaided play = contest packaging proceeds (week 12). Fail → rulebook text iteration, one re-run with a different reader.
- **Files afterward:** append to CAIRN_playtest_01.md or write 02; contest checklist in PUBLISHING_PLAN.

### 4.12 SL-0 — SLEEPER concealment rider *(unscheduled; only if 4+ players and spare time)*

- **Justification:** the single sanctioned parked-game test — it answers the deck-wide F8 question (is one flat pressed loyalty card the deck's workable concealment ceiling?), which constrains every future hidden-info design. It is *not* a SLEEPER development session.
- **Setup:** SLEEPER v0.1a (Blind Cut loyalty deal per F10 patch), 4P, one short game or even a half-game.
- **What to test:** only this: does the loyalty deal execute leak-free, and does anyone's pressed card flash during normal play? Stop observing anything else.
- **What not to test:** deduction quality, kingmaking, win-condition feel — all future-quarter questions.
- **Pass/fail:** no gate. Leak-free = F8 ceiling provisionally confirmed, recorded in DECK_PLAYTEST_FINDINGS F8; leaks = F8 tightened ("even one pressed card leaks"), which future designs must inherit.
- **Files afterward:** F8 status update; one-paragraph note in Sleeper/ folder. No status change for SLEEPER either way this quarter.

---

## 5 · Blind-test escalation path

*Four rings, cheapest first (PUBLISHING_PLAN §5a). Each ring has an entry condition — a game moves outward only when the inner ring stops producing new findings. Never skip a ring to feel like progress.*

| Ring | What it is | Becomes appropriate when | This quarter |
|---|---|---|---|
| **0 — Local, Sam-present** | Sam at the table, teaching and observing | Default for every first test and every gate re-test | Weeks 1–8 (all §4 sessions except BL-3/CA-2) |
| **1 — Local, Sam-absent** | PNP deck + printed rulebook + Handbook handed over; Sam leaves; feedback form captures what he'd have seen | A game has passed its gate **and** its rulebook has no known open text issues — blind testers are too scarce to spend on known failures (CORE_SET_AUDIT §2.9's warning) | BL-3 (week 10) for BLIGHT; CA-2 (week 11) for CAIRN's rulebook-as-teacher |
| **2 — Remote / digital** | Screentop.gg build + Break My Game Discord / remote friends; unlocks strangers without postage | Ring 1 passed for that game; Screentop build exists; the feedback form is proven | Build starts week 10, finishes week 12; first *sessions* are month 4 — do not rush strangers onto a build that hasn't been smoke-tested |
| **3 — Public: BGG WIP / contests** | BGG Work-In-Progress threads with PNP files; BGG Solitaire PNP contest (CAIRN); 2-Player PNP contest (FACE VALUE, later); Button Shy 15-card route (later) | The game survives ring 1–2 without rules disputes; PNP files regenerate cleanly; Sam accepts the public dated record (it's also the prior-art stake) | Week 12: BLIGHT WIP thread; CAIRN contest package queued for the next contest window. FACE VALUE holds until it has a second clean session |

**Escalation rules:** a finding at an outer ring that reveals a rules-text failure pulls the game **back in** one ring after the fix — never patch text and stay outward-facing untested. Publisher-facing exposure (ring 4 in spirit) is out of scope until the month-6 fork per PUBLISHING_PLAN §4.

---

## 6 · Kiro-ready implementation tasks

*Ordered; desk implementation (Kiro/Opus) strictly separated from table tests (Sam). Table sessions are listed only as dependencies. AC = acceptance criteria.*

**VP1 — Verify the locked handoffs landed** *(week 1; no dependencies)*
AC: every HK1–HK8 and DH1–DH6 acceptance criterion from HOUSE_KIT_DECISION §8 and DECK_HANDBOOK_HANDOFF §5 checked and either confirmed done or implemented now; discrepancies listed in a short note rather than silently fixed if they touch settled wording.

**VP1b — Playtest plan files from §4** *(week 1; after VP1)*
AC: `BLIGHT_playtest_plan_02.md`, `WILDFIRE_playtest_plan_02.md`, `GLEAN_playtest_plan_02.md`, `TRIGON_playtest_plan_02.md`, `CROSSROADS_playtest_plan_03.md`, `ORRERY_playtest_plan_02.md`, and a TRIALS counter-trial plan exist in their game folders, each following Templates/Playtest Plan and containing its §4 script's hypotheses, watch-list, signals, and teaching plan verbatim-or-tighter. CAIRN and FACE VALUE already have plan files — do not duplicate; add a one-line pointer to this protocol.

**VP1c — Feedback form** *(week 1)*
AC: a one-page `Templates/Blind Test Feedback Form.md` derived from Templates/Playtest Report: first-read confusions, minutes-to-first-play, rules re-reads by section, would-play-again, which-game-sounds-best. Printable; no internal codes.

**VP2 — CROSSROADS eighth-dim end-trigger sim** *(week 3; desk)*
AC: crossroads_sim.py extended per Phase 3 tasks: eighth-dim trigger tested at 2/3/4P; crisp termination confirmed; asymmetric-readiness metric reported; if inadequate, the hand-of-completed-contracts secondary condition tested; chosen trigger + parameters written into `CROSSROADS_design_analysis.md` §(next) and the CROSSROADS task list Phase 3 boxes ticked.

**VP3 — CROSSROADS on-spec crib sheet** *(week 6; depends VP2)*
AC: one page: deal-9, Toll-in-base, Signal Fires, pie rule, the VP2 end trigger, one named layout candidate from Phase 5's table, and the pass-to-win assignment note. Explicitly headed "session spec — the v1.1 rulebook remains bannered and is not to be consulted."

**VP4 — TRIGON session prep** *(week 6)*
AC: centre-first setup line drafted into the rulebook behind a "pending TR-2 confirmation" comment; Nine Signs sheet text master print-ready (verify DH6 output prints legibly at one page); requirement-vs-ability front-load line and chaining FAQ (playtest 01 candidates 3–4) confirmed present.

**VP5 — Blind kit** *(week 9; depends G1 pass)*
AC: printed pack: Handbook v0.1, BLIGHT rulebook (post-G1 text), feedback form, Nine Signs sheet; PNP deck verified complete; a half-page "for the group" cover note that tells testers what to do without teaching any rules.

**VP6 — Screentop.gg build** *(weeks 10–12)*
AC: 36-card deck with both faces, flip action, hand + table zones sufficient for BLIGHT and FACE VALUE; smoke-tested by Sam solo; link recorded in PUBLISHING_PLAN.

**VP7 — Public packaging** *(week 12; depends G9, G5)*
AC: BGG WIP thread text for BLIGHT drafted (hook line, PNP + Handbook links, the specific questions Sam wants strangers to answer); CAIRN contest package per contest rules (rulebook standalone-checked via CA-2, PNP file, entry text) staged for the next Solitaire PNP window.

**VP8 — Gate bookkeeping (recurring, weeks 6/9/13)**
AC: after each gate week, every §8 file update for decided gates is applied in one commit per gate; no file update ships before its gate is decided; the day-90 commit includes K1 (Core Set declaration in COLLECTION_OVERVIEW), `VALIDATION_REVIEW_2026-10.md`, and the PUBLISHING_PLAN month-4–6 rewrite.

**Table tests (Sam, not Kiro):** TT-1, WF-2, BL-2, CA-1, GL-2, FV-1, OR-1, TR-2, CR-3, BL-3, CA-2, (SL-0 rider). Kiro never marks these done; Sam's report file is the completion artifact.

---

## 7 · Stop conditions

**Per game — stop testing this quarter when:**

- **BLIGHT:** blind round completed unaided (G9 pass) — further testing is ring-2+ next quarter. Hard stop after BL-3 + at most one re-run.
- **GLEAN:** G2 decided, either way. A demoted GLEAN gets zero further sessions this quarter.
- **WILDFIRE:** after WF-2, full stop — the framing gate is deliberately terminal. Ten minutes of warm-up per evening is play, not testing.
- **FACE VALUE:** after FV-1 this quarter; second confirming session belongs to ring 2 (month 4).
- **CAIRN:** after CA-1 + CA-2 (+ one iteration re-test if G5 failed once). Two G5 fails = stop, flag at day-90 review.
- **TRIGON:** after TR-2, unconditionally. Pass or fail, no third session before month 4.
- **CROSSROADS:** after CR-3, unconditionally — the reclaim clause is single-use. A failed CR-3 also stops all CROSSROADS desk work except filing the report.
- **TWELVE TRIALS / THE ORRERY:** after TT-1/OR-1. The counter method decided is the quarter's whole ambition; deeper solves, 9-sym ORRERY, Clockmaker, completion mode all wait.
- **JANUS:** never started. **SLEEPER:** SL-0 rider only, once.

**Demote to pipeline when:** a Core Set game fails its gate and its named contingency (G1's extra config session, G2's procedural fix, G5's one iteration) also fails. Demotion is a file change, not a mourning period — Kiro applies §8 the same week.

**Cut or park a line of work when:**

- The counter-on-card restore fails → cut TRIALS' Duel/replay restore or replace with a written note (T3, game-local); do not iterate a third tracking method this quarter.
- Blind testing produces a *deck-level* failure the Handbook can't text-fix (e.g. F1 makes 9-card hands unteachable to strangers) → stop scheduling blind sessions, write it up as a new F-finding, and bring it to the day-90 review as a product-shape question — do not quietly redesign anything.
- Any session's findings demand changing a sim-tuned mechanic → park the change as a proposal in the game's task file with the observation attached; re-sim before any rules edit (simulation-standards).
- Tester availability collapses for 3+ consecutive multiplayer weeks → re-plan around solo + ring-1/2 work rather than forcing off-spec tables; the calendar's solo items and desk items can fill five weeks without waste.

---

## 8 · Files to update after each gate

*One commit per gate decision (VP8). "Always" rows apply to every session regardless of gates.*

| Trigger | Files |
|---|---|
| **Every session** | The game's `*_playtest_NN.md` report; game task list tick-boxes; DECK_PLAYTEST_FINDINGS (only if a deck-general finding emerged — new F-number, never edit old findings' conclusions) |
| **G1 (BLIGHT)** | COLLECTION_OVERVIEW (BLIGHT Core-confirmed flagship / contingency note); DECK_PLAYTEST_FINDINGS F1 (9-card data point); PUBLISHING_PLAN §3 flagship line |
| **G2 (GLEAN)** | Pass: GLEAN_rulebook scoring text confirmed; COLLECTION_OVERVIEW un-staled. Fail: overview moves GLEAN to PNP-extra tier; PUBLISHING_PLAN retires "two trick-takers" pitch; DECK_HANDBOOK untouched (it never names GLEAN specifics) |
| **G3 (WILDFIRE)** | WILDFIRE_rulebook intro framing line; COLLECTION_OVERVIEW entry un-staled (cites playtests 01–02); PUBLISHING_PLAN §3 opener row |
| **G4 (counters)** | TWELVE_TRIALS_rulebook (footnote "method scheduled for validation" removed on pass; restore fallback applied on T3 fail); ORRERY_rulebook same; DECK_CONVENTIONS T3 closed; DECK_BUG_AUDIT punch #4; Designs/CARD_LAYOUT annotations confirmed cleared |
| **G5 (CAIRN)** | COLLECTION_OVERVIEW (Stage 3, Core-confirmed solo slot); PUBLISHING_PLAN contest earmark; CAIRN_rulebook only for text fixes CA-1/CA-2 surface |
| **G6 (TRIGON)** | Pass: TRIGON_rulebook centre-first line confirmed; COLLECTION_OVERVIEW depth slot confirmed. Fail: overview + PUBLISHING_PLAN demote to expansion tier, Core Set = 5, "no TRIGON work before month 4" note; the Nine Signs sheet stays in the kit either way (it serves rank games too — locked) |
| **G7 (CROSSROADS)** | Pass: v1.2 rulebook rewrite authorised (deal-9/Toll/end trigger/2–4P callout, banner removed, Phase 6 executed; COLLECTION_OVERVIEW player-count + coverage rows). Fail: banner + pipeline status reaffirmed; overview 2P row = FACE VALUE permanent; CROSSROADS task list gains "reclaim clause spent — pipeline cadence" header |
| **G8 (FACE VALUE)** | COLLECTION_OVERVIEW (Stage 3, 2P slot provisional→held); PUBLISHING_PLAN §3 2P row |
| **G9 (Handbook)** | DECK_HANDBOOK.md text iterations (Handbook only — never a settled convention, per DH4); version → v1.0 on pass; feedback-form template refinements; PUBLISHING_PLAN §5a ring-1 status |
| **G10 (day 90)** | COLLECTION_OVERVIEW full K1 restructure (Core Set section, pipeline moves, play order rewrite); index.html catalogue sync; new `VALIDATION_REVIEW_2026-10.md`; PUBLISHING_PLAN month-4–6 rewrite; COLLECTION_AUDIT banner verified (K3); memory/decision notes as Sam directs |

---

## 9 · Things not to change

*Everything in CORE_SET_AUDIT §7, HOUSE_KIT_DECISION §9, and DECK_HANDBOOK_HANDOFF §6 stands. This quarter's specific restatements:*

- **The Core Set declaration** (BLIGHT flagship, GLEAN conditional, WILDFIRE opener, FACE VALUE 2P default, CAIRN solo, TRIGON conditional; CROSSROADS one-session clause; JANUS/SLEEPER parked; TRIALS/ORRERY pipeline) — only a gate result listed in §3 changes any slot. No mid-quarter re-litigation, however a session *feels*.
- **The house kit** (36 cards, Handbook, 12 counters, Nine Signs sheet, box base as container; C2/C3/C5/C6 Settled; C10) — kit contents and convention wording are frozen. Test failures produce game-local fallbacks (T3) or production notes, never kit edits.
- **Handbook wording** — DH1's text is verbatim-protected; only blind-test evidence (G9) edits it, and only the failing item, fixed in the Handbook rather than in any convention. The C7 teach script and C6 registry sentence stay verbatim everywhere.
- **Sim-tuned mechanics** — WILDFIRE chain-2/refusal-2, the BLIGHT/GLEAN trick engine, TRIGON's ability set, CROSSROADS' deal-9/Toll/Signal-Fires trio (applied whole with the VP2 trigger, never piecemeal). The only session allowed to touch a tuned system is one whose script explicitly targets it (CR-3's trigger parameters via VP2's sim; nothing else this quarter).
- **The 36-card / 9-symbol master deck and subset rule; F2's top-left pip placement** (confirmatory print check rides along with POD copies, not a design reopen); **F1's status as a constraint** — no per-game sort rules ever; the levers remain hand size, subsets, visual identity.
- **CROSSROADS' v1.1 banner** — untouched until G7 passes; CR-3 plays from the crib sheet precisely so the rulebook needn't be half-updated.
- **Parked statuses** — JANUS (playable-in-principle changes nothing), SLEEPER (SL-0 rider only), THE UNPLAYED PAIR, and the PUBLISHING_PLAN "deliberately absent" list (no icons before the gates say so, no box design, no Kickstarter prep, no new concepts, no RELAY rulebook this quarter).
- **The validation-before-polish ordering itself** — if a week's hours are short, the table session survives and the polish item dies, never the reverse.

---

*Companion decision memos: CORE_SET_AUDIT_2026-07.md · HOUSE_KIT_DECISION_2026-07.md · DECK_HANDBOOK_HANDOFF_2026-07.md. Day-90 output: VALIDATION_REVIEW_2026-10.md.*
