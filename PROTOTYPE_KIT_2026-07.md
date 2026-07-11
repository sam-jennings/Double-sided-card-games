# Prototype Playtest Kit — July 2026

*The complete, minimal component set for playing **every game currently in design** — Core Set, pipeline, drafts, parked games, and sparks — at the table. This is the **playtest kit**, not the product: it deliberately includes diagnostic components that the frozen house kit (HOUSE_KIT_DECISION_2026-07.md, C10) excludes. Relationship to the freeze is stated per item; nothing here reopens C10.*

---

## 1 · Purpose and scope

The frozen house kit answers "what ships?". This kit answers a different question: **"what must be on the table so that any game in the repo can be tested as designed?"** Three games are currently blocked or throttled by *physical* problems, not design problems:

- **JANUS** — repeated concealed draws (F7, solved in principle by box-as-container) plus fan-handling leaks (F8, unsolved — the first table abandoned concealment entirely).
- **TRIGON** — grid drift (HIGH bug 1) and per-turn reference stalls (HIGH bug 2).
- **TWELVE TRIALS** — flip-tally method replaced but untested (K10 counter-on-card restore).

The kit's rule: **a diagnostic component is legitimate in playtesting when it isolates the variable you're testing.** If a game is only fun *with* its diagnostic component, that is a finding — either the component must earn collection-level justification under the graduated policy, or the game needs redesign. If it isn't fun *even with* the component, cut with confidence.

## 2 · The kit

### Tier A — the frozen house kit (matches C10; ships as-is)

| # | Item | Spec | Serves |
|---|---|---|---|
| A1 | **36-card master deck** | Print-and-play Set D Glyphs (duplex A4, corner pips 1–9 for subset sorting). Print **two copies**: one to play, one as spares for wear | Every game; subsets by pip: 21/7-sign (JANUS, CAIRN, OUROBOROS short), 15/6-sign (SNARE), 10/5-sign (SNARE campaign rung 1) |
| A2 | **Deck Handbook** | One page (G1 / DECK_HANDBOOK.md spec): signs+ranks, F4 teach script, shuffle, C2 ladder, C3 pile law, C5 counters, C6 sentence, hand-size, space notes | Every session; teach + rules disputes |
| A3 | **12 identical flat counters** | Glass nuggets or coins — must be **flat** (sit on a card without sliding; dice roll off — K10 requirement) | JANUS omens (6) · COUNCIL Speaker (1) · SLEEPER first-player (1) · TRIALS/ORRERY flip tallies |
| A4 | **Nine Signs reference sheet** | Front: 9 signs, fixed ranks, mnemonic verbs (post Leaf/Key relabel). Back: TRIGON + TURNCOAT ability tables | All rank-sensitive games; TRIGON/TURNCOAT abilities |
| A5 | **Opaque draw well** | Stand-in for the two-piece box base: any opaque mug, bowl, or box ≥9 cm deep, wide enough for a one-handed blind draw. Cards lie flat inside; draw by sliding one card up the wall with fingertips, never lifting the stack | JANUS deal + refills (C2 rung 4). Side benefit: deck-in-well is unmistakably the live deck (kills the F9 misdraw at the source) |

### Tier B — prototype-only conveniences (not in the frozen kit; household-class, no policy tension)

| # | Item | Spec | Serves | Freeze status |
|---|---|---|---|---|
| B1 | **3 extra Nine Signs sheets** (4 total) | Same text master, one per player | TRIGON bug 2 was a *shared*-reference bottleneck — one sheet mid-table may still throttle a 4P game. Per-player sheets isolate "is the game slow?" from "is the reference queue slow?" | Product ships 1 sheet; if testing shows 1 is not enough, that's a production finding (print the tables in the rulebook margins, or duplex the Handbook) — log it, don't silently absorb it |
| B2 | **Almanac card** | The 12-triangle / 4-season table (DECK_SIZE_DECISION.md) printed as one card/sheet | TWELVE TRIALS play; box-copy proof-of-depth | Product prints it inside the TRIALS rulebook (BUG_AUDIT #12) — standalone print is a table convenience |
| B3 | **Pencil + scorepad** | Any | ORRERY scoring (optional per its rules) · match scores for GLEAN/BLIGHT/FACE VALUE/CROSSROADS · playtest notes | Explicitly excluded from the frozen kit; paper stays optional forever |
| B4 | **8 overflow counters, different colour** | Flat, distinct from A3 | ORRERY's worst 9-sign deals may exceed 12 flips (HOUSE_KIT residual risk 5). **Protocol: any session that dips into overflow gets a log line** — this converts the 12-counter sizing gap into free data before print files freeze | Product stays at 12; substitutes cover overflow at home |

### Tier C — diagnostic fix-components (purpose-designed; each targets one blocked game)

| # | Item | Spec | Targets | Decision rule |
|---|---|---|---|---|
| C1 | **Janus racks ×4** | See §3.1 | JANUS F8 (fan-handling leak — the remaining promotion blocker) | Pass + fun → JANUS's concealed test can finally run honestly; then decide whether the *game* demands a rack-class component (collection-level justification needed) or whether trained hands suffice. Fail even with racks → cut JANUS cleanly |
| C2 | **Trigon grid mat** | See §3.2 | TRIGON bug 1 (grid drift) — as the **B arm of the K9 A/B test** against the centre-first rule | Centre-first alone kills drift → mat retired, no component. Drift persists without the mat → either strengthen the convention or accept a printed grid in the rulebook (a diagram, not a component) |

**Deliberately excluded** (unchanged from the freeze): cloth bag, per-player screens, colour-coded cubes, bespoke per-game pieces. Also excluded from Tier C: any concealment aid for FORKED TONGUE / FACE VALUE / THE COUNCIL — their hidden faces are open to the holder, so F8 risk is mild; monitor first, build later only if a table demands it.

## 3 · The fix-component designs

### 3.1 Janus racks — killing the F8 leak

**Problem.** JANUS requires each player to hold a fan where the table sees the outward face and the holder sees only the inward face — and the holder must *never* see the outward face. Playtest 01 showed humans can't sustain this grip: sorting, choosing, and playing all risk flashing a face, so the table gave up and played open. The box-as-container decision solved the *draw* (F7) but explicitly left F8 as the untested second blocker.

**Component.** A per-player upright card rack (Scrabble/Rummikub tile rack, or DIY below) placed between player and table:

- Cards stand **vertically** in the groove, inward faces to the player, outward faces to the table.
- The lip must be **low (~15 mm)** so the table sees the outward faces fully.
- Length ≥30 cm — holds a 12-card deal with overlap.
- **Draw protocol:** blind-draw from the well (A5), keep the card face-away-from-you and edge-on, slot it into the rack outward-face out *without turning it*. One sentence of rules; no finger yoga.
- Playing a card: lift it from the rack **keeping its facing** and place it. The sacred no-self-inspection rule becomes physically passive — peeking now requires a deliberate act (standing up, turning a card), which the table will see.

**DIY builds (pick one):**

1. Two ~30 cm strips of foam board glued into an L-channel, card leaned into the corner.
2. A fat rubber band around a paperback book, cards tucked under the band, spine toward the player.
3. Four large binder clips per player, card bottoms clipped, clips standing on their backs.

**What it isolates.** With racks, the concealed table test measures the *game* (does locking a gate pay off? is the deduction fun?) instead of measuring grip stamina. That is the test JANUS has been waiting for.

### 3.2 Trigon grid mat — the K9 control

**Problem.** Playtest 01: the grid was never physically defined, play drifted into unfixed-grid habits, which breaks position-based ability requirements. The adopted fix is the **centre-first rule** (first card defines the centre cell — zero components), but it is untested (K9).

**Component.** A paper mat with a 3×3 grid of cells at 65×90 mm with 5 mm gutters (fits on A3, or two taped A4 sheets). Cells drawn as faint outlines only — the mat must not carry information, just geometry.

**Protocol.** Run K9 as A/B: first game centre-first *without* the mat, second game *with* it (or alternate by session). Log drift incidents per game. The mat is the control arm proving whether drift is a convention problem or a physics problem.

### 3.3 The draw well — F7 made concrete

Already decided (C2 rung 4, box base); the kit item (A5) just makes it real before a two-piece box exists. Two build notes from the decision memo worth honouring at the table:

- The well holds the **whole live deck** whenever a game says "draw unseen" (currently JANUS only). Everything else keeps the deck as a normal upright stack — don't let the well creep into games that don't name rung 4.
- During JANUS play the deck is only ~5 cards; any mug swallows it. The test that matters is the **deal** — 12 cards drawn blind one at a time into racks without a glimpse. Time it; if the deal drags past ~2 minutes, note it (it's the pitch-facing cost of the container model).

## 4 · Coverage matrix — every game in design

| Game | Status | Deck used | Kit items beyond deck | Component-fixable core problem? |
|---|---|---|---|---|
| TWELVE TRIALS | Collection, Stage 3 | 36 | A3 counters (tallies + counter-on-card), B2 almanac | Yes — K10 restore test is *the* open item; kit carries it |
| CROSSROADS | Collection, Stage 3 | 36 (deal 9 per v1.2 pending) | B3 pad (match scores) | No — pass-to-win & end-trigger are rules problems (Toll Roads, eighth-dim); dimming is orientation, component-free |
| THE ORRERY | Collection, Stage 3 | 21 or 36 | A3 + B4 counters, B3 pad | Yes — counters give it its first physical tally method; overflow logging feeds risk 5 |
| TRIGON | Pipeline, Stage 3 | 36 | A4/B1 sheets, **C2 grid mat** | Yes — both HIGH bugs are handling; sheets + mat/centre-first target them directly |
| TURNCOAT | Pipeline, Stage 2 | 36 | A4/B1 sheets | No core problem; sheet pre-empts the TRIGON reference stall |
| WILDFIRE | Pipeline, Stage 2 | 36 | — | None |
| GLEAN | Pipeline, Stage 2 | 36 | B3 pad | F1 hand-load is a config lever (prefer 4P/6P), not a component |
| BLIGHT | Pipeline, Stage 3 | 36 | B3 pad | Same as GLEAN — test smaller-hand configs before judging |
| OUROBOROS | Pipeline, Stage 2 | 21 or 36 | — | No — v1.1's orientation-as-state fix is deck-native |
| CAIRN | Pipeline, Stage 2 | 21 (36 Long Trail) | box lid as tray | None — built for a tray by design |
| RELAY | Pipeline, Stage 2 | 36 | — | No — blocked on a rulebook, not a component |
| JANUS | Draft, Stage 3* | 21 | A3 (6 omens), **A5 well, C1 racks** | **Yes — the kit's headline case.** Well solves F7; racks target F8 |
| FORKED TONGUE | Draft, Stage 1 | 36 | — | None known pre-test; pot and registry are cards |
| FACE VALUE | Draft, Stage 1 | 36 | B3 pad (match) | None — stakes are cards from hand |
| THE COUNCIL | Draft, Stage 1 | 36 | A3 (Speaker) | None known pre-test |
| SLEEPER | Draft, Stage 1 | 36 | A3 (first-player, optional) | No — loyalty-deal leak already solved component-free (Blind Cut, F10); F8 ceiling is a table question, cards lie flat |
| SNARE | Spark, Stage 0 | 15 (10 for rung 1) | — | No — orientation-as-ownership is deck-native; component-free by design |
| THE UNPLAYED PAIR | Parked | 36 | — | **No — and don't try.** Its problem is structural (deduction certainty arrives on the last trick); no component fixes that. Blind Cut already fixed the removal leak. Stays parked |

*JANUS remains outside the Core Set until the concealed table test passes — the racks exist to make that test runnable, not to pre-empt its verdict.*

**Verification notes:** counter demand never collides (JANUS's 6 omens, COUNCIL's 1, SLEEPER's 1, and TRIALS/ORRERY tallies are different sessions; worst single-session case is ORRERY at 12+, covered by B4). Every subset is a pip-sort of the master deck — no second deck. RELAY is playable the moment its rulebook exists; nothing in it (design analysis: deck-only, open draft) will demand a component.

## 5 · Packing list (one line, table-ready)

> 2 printed decks (1 play + 1 spares) · Deck Handbook · 4 Nine Signs sheets · almanac card · 12 flat counters + 8 overflow (other colour) · 1 opaque mug/box (draw well) · 4 card racks · 1 grid mat (A3) · pencil + pad

Everything except the racks prints or comes from the kitchen. Racks: ~£8 for four wooden tile racks, or ten minutes of foam board.

## 6 · Scheduled tests this kit unblocks

1. **K10** — counter-on-card restore, TWELVE TRIALS Duel (A3).
2. **K9** — centre-first grid A/B, TRIGON (C2 as control arm).
3. **JANUS concealed table test** — the F8 verdict (A5 + C1). Now runnable as designed for the first time.
4. **ORRERY 9-sign sessions** — with overflow logging (B4) feeding the 12-counter sizing risk.
5. **SLEEPER first table test** — F8 ceiling for a single flat card (no new component; kit-complete).

*Written July 2026. Companion to HOUSE_KIT_DECISION_2026-07.md — that memo governs what ships; this one governs what gets tested.*
