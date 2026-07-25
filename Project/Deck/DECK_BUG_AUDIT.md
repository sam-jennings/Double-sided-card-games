# Deck-Wide Bug Audit — July 2026

> **Point-in-time audit.** This remains useful evidence, but its game count and task list are historical. Current handling rules live in [Deck Conventions](DECK_CONVENTIONS.md), current cross-game observations in [Deck-wide Playtest Findings](../Playtesting/DECK_PLAYTEST_FINDINGS.md), and current game status in [Collection Overview](../../COLLECTION_OVERVIEW.md).

*A system-level audit of all sixteen games plus the shared deck, run against every rulebook, design analysis, playtest report, and steering doc. Companion outputs: `DECK_CONVENTIONS.md` (the canonical handling conventions this audit proposes) and three new findings appended to `DECK_PLAYTEST_FINDINGS.md` (F10–F12). Edits already applied are marked ✅; everything else is proposed, not done.*

---

## 1 · What the audit did

Every issue found was classified **game-local** (fix it in one file, nothing ripples) or **deck-wide** (touches the physical deck, a shared handling convention, or the symbol/rank/orientation model — so any fix must be checked against every game sharing the mechanic). Deck-wide fixes were cross-checked against all sixteen games before being proposed; the compatibility matrix is in `DECK_CONVENTIONS.md`. Where two games genuinely need contradictory conventions, that is recorded as an open tension (T1–T5), not silently resolved.

## 2 · New deck-wide findings (now F10–F12 in DECK_PLAYTEST_FINDINGS)

**F10 — Secret single-card draws leak.** Any card taken from the top of a stack was already showing one face to the table. This *broke SLEEPER as written* (the loyalty deal could name a player's Master outright — the game's only secret, dead at setup), falsified THE UNPLAYED PAIR's "unseen by anyone" removal, and is the second half of JANUS's blocker. Deck-native fix for one-off draws: the **Blind Cut** (cut below the table edge, take the new top unseen) or a mid-deck slide. ✅ Both rulebooks patched. JANUS's *repeated* draws stay unsolved (T1).

**F11 — "Face-down" language survives despite the no-back rule.** TRIGON (removed pile, and the Moon ability — which needed a real mechanism, not a copyedit: an unmarked Moon-taken card shows a sign and would wrongly count for the tiebreaker), TURNCOAT (removed pile), GLEAN (Closed Harvest), JANUS (the F7 blocker itself). ✅ TRIGON/TURNCOAT/GLEAN patched (Moon-taken cards now go **sideways = anonymous**); JANUS left to the T1 decision, bannered.

**F12 — No canonical flip tally for regrouping games.** F6 killed sideways-marking for TWELVE TRIALS but nothing replaced it, and THE ORRERY's rulebook never had *any* physical method (mental counting = involuntary bookkeeping), while `CARD_LAYOUT.md` still claimed both use rotation. Proposed canon: counters from the already-sanctioned generic kit; counter-on-card where replay modes need per-card state. ✅ CARD_LAYOUT annotated; trial already on the TRIALS task list — add to ORRERY's next session.

## 3 · Edits applied (all local, none change tuned mechanics)

| File | Change |
|---|---|
| `DECK_CONVENTIONS.md` | **New** — canonical conventions C1–C9, compatibility matrix, open tensions T1–T5 |
| `DECK_PLAYTEST_FINDINGS.md` | F10–F12 appended; F6/F7/F9 statuses cross-linked |
| TRIGON rulebook | Moon ability → sideways-anonymous mechanism; removed pile → sideways dead pile (C3); scoring line matched; placement-vs-requirement callout and chain-order FAQ added (both were playtest 01 recommendations already answered by the rules but buried) |
| TURNCOAT rulebook | Removed pile → sideways (C3); extraction keeps its showing sign (was "face-up"); score piles = ordered stacks, newest on top (gives Moon's "top banked card" a physical meaning) |
| WILDFIRE rulebook | Pile is an **overlapping line**, not a squared stack — the rules and strategy notes treat the pile as readable history, which a stack physically isn't; recycle wording adjusted. Also resolves WILDFIRE's F9 instance (well = squared live stack, pile = cascade) |
| BLIGHT rulebook | "Sign *is* rank" callout added (F4 parity with GLEAN); rot-pile wording no longer implies a second flip after the reveal |
| GLEAN rulebook | Closed Harvest variant reworded ("face-down stack" → unexamined squared stack) |
| SLEEPER rulebook | **Loyalty deal → Blind Cut (F10, was game-breaking)**; turn reveal explicitly shows both faces; spent pile sideways (C3); version → v0.1a with changelog note |
| THE UNPLAYED PAIR rulebook | Removal → slide from the **middle** of the deck (F10) |
| JANUS rulebook | Blocker banner (F7/F10/T1); stale "untested at the table" footnote corrected to cite playtest 01 |
| OUROBOROS rulebook | Stock's visible top face made explicit legal information (matches CAIRN's "free look"; it physically cannot be hidden), with a par-honesty note since the sim didn't model it |
| THE COUNCIL rulebook | FAQ: the issue deck's top face is a public half-preview (physical honesty per rulebook-standards); "spare cards never seen" claim corrected |
| CROSSROADS rulebook | **v1.2-pending banner** — deal-9 / Toll-in-base / 2–4P are settled in the design analysis but deliberately unapplied while the end trigger (Phase 3) is open; the banner stops anyone playing the superseded deal-14 rules unaware |
| `Designs/CARD_LAYOUT.md` | Orientation table rows for TWELVE TRIALS / THE ORRERY annotated with F6/F12 reality |

*Caveat:* the sideways-dead-pile wording in TRIGON/TURNCOAT/SLEEPER applies the **proposed** C3 convention — those three lines were broken either way ("face-down" piles) and had to say something. If C3 is rejected, three lines to re-touch.

## 4 · Verified clean (close reading, no action)

FACE VALUE (palms-commit, flat concealment, fold-unrevealed: all physically sound — the post-lessons designs hold up), FORKED TONGUE (ledger cascade and registry are exemplary; deal exposure covered by C2), CAIRN (the model citizen — codifies the free look OUROBOROS omitted), RELAY concept (face-up market/goals turn F7 into a feature), THE ORRERY v0.2 rules text (split-cycle fixes already applied). Deal arithmetic checked for every game: all correct (JANUS fans/deck, FORKED TONGUE registry sizes, COUNCIL issue-deck sizes, GLEAN/BLIGHT/WILDFIRE deals, CAIRN stocks, FACE VALUE 15+15+6).

## 5 · Punch list

### Blocking — a game cannot be played correctly as written

1. **JANUS concealment model (F7 + F10, tension T1).** The core design decision of the audit: box-as-container / bag / no-draw redesign. Until decided, only the open-information Apprentice variant is playable. Everything else about JANUS waits behind this.
2. **CROSSROADS end trigger + rulebook sync (Phases 3 + 6).** Pass-to-win and hand-size are *solved on paper* (Toll, deal-9) but live only in the design analysis; the end trigger is the last open piece (sim the eighth-dim clock), then the v1.2 rewrite. Twice-flagged, and the game is in the collection **on notice**.
3. **TRIGON grid definition.** Five of nine abilities are position-defined and the grid physically isn't. Centre-first (first card = centre cell) is the agreed candidate — one session to confirm, then one setup line in the rulebook.
4. **TWELVE TRIALS flip tracking (F6/F12).** The shipped method is confirmed-failed and still in the rulebook. Trial the counter tally (and counter-on-card for Duel restore) next solo session — already task #1 in its file.
5. **SLEEPER loyalty concealment.** The deal leak is patched (v0.1a Blind Cut), but the game's whole premise still rests on guarding one flat card all game — JANUS's lesson says confirm at the first table before trusting it.

### Quality-of-life

6. **Ratify the conventions.** C2 (deal/draw ladder), C3 (live vs dead piles), C5 (flip counters), C6 (registry sentence) are proposed and contradiction-checked; a yes/no on each turns them from proposal into house rules.
7. **TRIGON reference overhead (T2).** Decide the reference model (staged teach / shared back-page sheet / one generic Nine Signs card shared with TURNCOAT). Related one-word decision: the SIGN_MNEMONICS Leaf/Key relabel — balance-neutral, still unapplied.
8. **F2 confirmatory print test** of the top-left corner pip (fan readability vs rotated states) — the last open item on an otherwise settled decision.
9. **Sign-is-rank callout** for the remaining rank games (FACE VALUE, THE UNPLAYED PAIR, THE COUNCIL) — GLEAN and BLIGHT now carry it.
10. **Memory-dependent tiebreakers**: TURNCOAT "banked most recently" and THE COUNCIL "carried most recently" quietly assume the table remembers global order. Ordered score piles (now written into TURNCOAT) mostly cover it; consider memory-free tiebreaks in the next revision.
11. **JANUS keystone down-face re-checking** (playtest Bug 3): pairs are public knowledge — add a "lift keystones freely / say the pair on request" line once the T1 rewrite happens.
12. **Doc drift**: COLLECTION_OVERVIEW's CROSSROADS tags (perfect-info, 2P-only) await Phase 6; COLLECTION_AUDIT §0's "ten live games" scope is dated (its §4 already carries a supersession banner — a matching one-line note at §0 would prevent misreads); TWELVE TRIALS' "the collection's reference card" mention vs the deck-only component inventory should say "the almanac printed in this rulebook."

### Open design tensions — no single right answer yet

- **T1/T2/C5 together are really one question: what is the house kit?** The deck's three hardest problems (concealed repeated draws, ability-reference load, flip tallies) all reach for a small component; the collection's identity says deck-only. One deliberate decision — e.g. *"the kit is: the box itself, ~10 generic counters, one shared sign sheet"* — would close three fronts at once; a principled refusal instead means redesigning JANUS (no-draw) and accepting slower TRIGON teaches. Don't let each game answer this separately — that's exactly the per-game patching this audit exists to stop.
- **Open registries vs memory-as-skill (T4).** GLEAN's playtesters *missed* remembering; the steering wants a deliberate memory game. Keep the C6 open-registry default, route the appetite into declared variants (Closed Harvest) and the future memory game — not into per-game erosion of the default.
- **F1 is a constraint, not a bug.** No sort order exists; the levers are hand size, subsets, and the shipping deck's visual identity. New designs should declare their worst-case hand against the C8 comfort line (≤9 to teach).
- **F8 caps hidden-hand ambition.** Fan concealment is fragile even before JANUS's draws; SLEEPER's single-pressed-card model is probably the deck's honest concealment ceiling. Its first table test is therefore a *deck* test, not just a game test.
- **T3 TRIALS replay modes** depend on whichever tracking method wins — if counter-on-card fails, Duel/restore may need a written note or a cut.

---

*The through-line: the deck's physics (no back, top card always showing, sign = rank, rotation as the only free marker) are not bugs — but every game that borrowed an ordinary-deck convention ("face-down," "unseen," "sorted hand," "hidden draw") imported one. The conventions doc exists so the next game borrows from the house, not from ordinary decks.*
