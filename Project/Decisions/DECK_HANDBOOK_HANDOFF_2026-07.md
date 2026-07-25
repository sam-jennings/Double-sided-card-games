# Deck Handbook — Content & Implementation Handoff (July 2026)

*Delivers PUBLISHING_PLAN G1 / CORE_SET_AUDIT K2 / HOUSE_KIT_DECISION HK2. Ground truth: HOUSE_KIT_DECISION_2026-07.md (D1/D2 locked), DECK_CONVENTIONS.md (C1–C10 as settled there), CORE_SET_AUDIT_2026-07.md §5 Handbook spec. Section 1 is player-facing and code-free; everything after it is internal.*

---

## 1 · Deck Handbook v0.1 — final player-facing text

*Ready to paste into `DECK_HANDBOOK.md`. One printed page. This page sits at the front of the rules booklet, before every game.*

---

# The Deck Handbook

*Read this page once. It applies to every game in the box.*

## The deck

The deck is **36 cards**, and it has a secret: **there are no card backs.** Every card shows one of the **Nine Signs** on each side — two different signs per card — and **every pair of two signs exists on exactly one card**. That's the whole deck: 36 cards, every combination once, no duplicates. A card lying on the table is always showing one of its two signs to everyone. Some games use fewer signs; their rules tell you which cards to set aside.

## Signs are strengths

Each sign has **one fixed strength**, printed as the number in the corner: Moon 1, Leaf 2, Wave 3, Flame 4, Eye 5, Mask 6, Key 7, Star 8, Crown 9. Before any game where strength matters, say this aloud:

> **"There are 9 signs. Each sign has one fixed strength — Crown is always 9, Moon is always 1. Every card pairs two different signs, so it always has two different strengths, one per face."**

There is no "low Crown" or "high Moon." If you're used to ordinary cards, this is the one habit to unlearn.

## Handling — the house ways

**Shuffle** by **flipping random chunks** as you go, so which side lands up is random.

**Dealing and drawing.** Because a face always shows, each game names one of these methods — use the one it names:

- **Open deal** — deal flat in front of each player; scoop up. The table glimpses one side of each card; for most games that's fine.
- **Self-deal** — square the deck and pass it; each player takes their own cards straight into hand.
- **Blind cut** — for a single secret card: take the deck below the table edge, cut it, and slide the new top card off without looking. The cut buries the side everyone had seen.
- **Box draw** — the deck sits inside the box base; draw blind from inside. Only when a game asks for it. (No box handy? A mug, envelope, or bag works.)

**Stacks and piles.** A stack you still draw from sits **upright**. A pile that's out of the game lies **rotated sideways**, in its own spot. A pile you're meant to read back lies as an **overlapping row**, never squared up.

**Turning cards sideways** means something only when a game says it does — each game defines its own meaning.

**Counting flips.** Where a game counts flips, take **one counter per flip**; if it must also mark *which* cards flipped, set the counter **on** the card.

**Public cards.** Won, dead, and set-aside cards lie in face-up spreads unless a game says otherwise. House rule: **"anyone may pick up and examine any card here, both sides, at any time — return it as found."**

**Your hand** is yours to examine, both sides, whenever you like — unless a game says otherwise. There's no natural way to sort a two-sided hand, so big hands take real effort: when a game offers a choice, fewer cards in hand plays lighter, and that's the friendlier first game.

**Table space.** Games that lay many cards out say "needs a large table" — believe them.

## In the box

**36 double-faced cards** · **1 rules booklet** (this Handbook + the games) · **1 Nine Signs reference sheet** · **12 counters**. Some games ask you to draw cards blind from the box base. Lost the counters? Any coins or pebbles work.

---

*End of player-facing Handbook text.*

---

## 2 · Box / component text

**For the box back and each rulebook's intro (matches HOUSE_KIT_DECISION §5 player-facing line):**

> Inside the box: **36 double-faced cards** · **1 rules booklet** (Deck Handbook + games) · **1 Nine Signs reference sheet** · **12 counters**. Some games ask you to draw cards blind from the box base. Lost the counters? Any coins or pebbles work.

**One-line pitch form (box front / catalogue):**

> One deck of 36 double-faced cards — no backs, every pair of nine signs exactly once — and a whole shelf of games.

## 3 · Nine Signs sheet — text brief

Text master lives at `Reference/NINE_SIGNS_SHEET.md` (HK5). Prerequisite: the Leaf/Key relabel is adopted — the TRIGON table below is the post-relabel version.

**Front (serves every game):**

- Title: *The Nine Signs*.
- Nine rows, in pip order: glyph · name · **strength number (1–9)** · one-idea verb — Moon 1 *the underdog* · Leaf 2 *swap* · Wave 3 *move* · Flame 4 *burn* · Eye 5 *peek* · Mask 6 *flip* · Key 7 *release / unlock* · Star 8 *draw* · Crown 9 *act from strength*.
- Printed across the bottom, verbatim: *"There are 9 signs. Each sign has one fixed strength — Crown is always 9, Moon is always 1. Every card pairs two different signs, so it always has two different strengths, one per face."*
- One footnote line: *"Star is wild in TRIGON only; everywhere else it is simply 8."*

**Back (serves the ability games):**

- Two columns: **TRIGON** and **TURNCOAT** ability tables — per sign: requirement + ability, in pip order, post-relabel (Leaf = swap in both; Key = flip one adjacent in TRIGON, extract in TURNCOAT).
- Column header note: *"Seven signs mean the same in both games; Key and Crown are the two expert signs — learn their two readings."*
- Mnemonic sentences only if space allows at legible size; requirement + ability text takes priority.

No art direction here beyond function: glyph + name + number must be readable mid-table (final form awaits the icon commission and the recognisability test).

## 4 · Rulebook integration plan

Global rule, all rulebooks: add one line under Components — *"Shared handling rules live in the Deck Handbook at the front of this booklet."* Keep each game's shuffle sentence (C1 is deliberately printed in every rulebook — never remove or vary it). Keep every game's own deal/draw method line, but it should **name the method** (open deal / self-deal / blind cut / box draw) rather than re-explain the physics.

| Game | Remove (now in Handbook) | Keep local | Say "see Deck Handbook" |
|---|---|---|---|
| **WILDFIRE** | Nothing — its pile-as-overlapping-line text is game-specific teaching, not duplication | Pile/well definitions; hand-examine line | Pointer line only |
| **BLIGHT** | Nothing | Sign-is-rank callout (stays — it's the at-the-table reminder; Handbook is the front-of-book teach); pip-rank list in Components; rot-pile orientation rules | Pointer line only |
| **GLEAN** | Nothing | Sign-is-rank callout; pip-rank list; harvest-examine sentence (compliant variant — do not rewrite) | Pointer line only |
| **FACE VALUE** | Generic "no card backs" exposition if any creeps in during edits | Morgue/tally examine sentences (compliant variants); palms-commit protocol; **add** the sign-is-rank callout (pending punch item) | Deal method: name self-deal/open deal per its setup |
| **CAIRN** | The generic "there is no card back" callout **may** be trimmed to the pointer — optional; it costs three lines and helps standalone play, so keeping it is also fine. Decide once, don't churn twice | Sub-deck construction text; free-look rule (game-specific) | Pointer line only |
| **TRIGON** | Nothing from the settled text | Sign/ability table (game content); "top card of the deck is public" (game-relevant); centre-first grid line (K9); Components **adds** the Nine Signs sheet | Pointer line only |
| **TURNCOAT** | Nothing | Ability table; ordered-score-stack rule (declared exception); Components **adds** the sheet | Pointer line only |
| **TWELVE TRIALS** | Old sideways-as-flipped rule (replaced by counters per HK6 — same commit) | Almanac content; workspace zones; "needs a large table"; counter-on-card restore detail | Counter method: one line + pointer |
| **THE ORRERY** | Nothing (it had no method; HK6 adds counters) | Orbit rules; "needs a large table"; optional-paper scoring note | Counter method: one line + pointer |
| **CROSSROADS** | **Nothing — v1.2-pending banner stands; do not touch ahead of the end-trigger decision** | Everything | Pointer line only, if even that |
| **SLEEPER** | Nothing | Loyalty-deal blind-cut protocol (the specific application stays local); spent-pile line | Pointer line only |
| **FORKED TONGUE** | Nothing | Ledger cascade + registry sentences (compliant variants) | Pointer line only |
| **THE COUNCIL** | Nothing | Issue-deck public-top FAQ; **add** sign-is-rank callout (pending punch item) | Pointer line only |
| **JANUS** | (Outside Core Set — handled by HK4, not this plan) | Parked banner until the concealed table test passes | Its rewrite names the box draw and points to the Handbook |

The pattern is deliberate: the Handbook **absorbs generic deck physics and house handling**; rulebooks keep everything **game-specific, declared-exception, or protected**. Almost nothing is deleted — the win is that no *future* rulebook ever needs to re-explain the deck.

## 5 · Kiro-ready implementation tasks

**DH1 — Create `DECK_HANDBOOK.md`** *(repo root)*
AC: file contains §1 above verbatim; ≤1 printed page; covers all 9 spec items (signs+ranks, teach script, shuffle, deal/draw ladder, pile law, counters, registry sentence, hand-size guidance, table-space note) plus the component list; the registry sentence appears verbatim as *"anyone may pick up and examine any card here, both sides, at any time — return it as found."*; the teach script appears verbatim per C7; contains no internal codes (grep `F[0-9]|C[0-9]|T[0-9]|K[0-9]` on the file returns nothing outside this handoff's internal sections — the Handbook itself is clean); no mention of JANUS or any unreleased game.

**DH2 — Add Handbook pointers to rulebooks**
AC: every `*_rulebook.md` except archived SYZYGY and parked UNPLAYED PAIR carries the pointer line under Components; CROSSROADS receives the pointer only, nothing else; no shuffle sentence altered anywhere (`grep -c "flipping random chunks" */[A-Z]*_rulebook.md` unchanged before/after).

**DH3 — Component list sync**
AC: box-back text (§2) recorded in `PUBLISHING_PLAN.md`; COLLECTION_OVERVIEW component inventory matches the frozen house-kit list (this is HK3 — verify done, don't duplicate); TWELVE TRIALS / THE ORRERY Components cite the house-kit counters (HK6); TRIGON / TURNCOAT Components cite the Nine Signs sheet (HK5).

**DH4 — Contradiction check against `DECK_CONVENTIONS.md`**
AC: side-by-side pass confirms the Handbook's four deal/draw methods match the C2 ladder rungs 1–4 exactly (same order, same leak model); pile rules match C3; counter rules match C5; registry sentence matches C6 verbatim; teach script matches C7 verbatim; hand-size and table-space lines are consistent with C8/C9 (guidance, not new rules); the component list matches C10. Any mismatch is fixed in the **Handbook**, never by editing a settled convention.

**DH5 — Ordinary-deck language sweep**
AC: `grep -rn "face-down\|face down" DECK_HANDBOOK.md` returns nothing; repo-wide sweep per HK7's allowlist still passes (only physically-true flat-card uses, explicitly-negated teaching uses, and archived files); `grep -n "unseen" DECK_HANDBOOK.md` returns nothing or only lines that name their method in the same sentence; the Handbook never says "discard pile" (it says dead pile / sideways pile).

**DH6 — Nine Signs sheet text master**
AC: `Reference/NINE_SIGNS_SHEET.md` exists with §3's front/back content; TRIGON table is post-Leaf/Key-relabel (Leaf = swap; Key = flip one adjacent); front carries the teach script verbatim and the Star-is-wild-in-TRIGON-only footnote; depends on HK5's relabel landing first or in the same commit.

## 6 · Things not to change

- **The Handbook does not restate game rules.** If a future edit starts adding per-game examples beyond method names, cut it — one page is a hard ceiling.
- **C1 shuffle sentences in every rulebook** — printed everywhere by design; the Handbook supplements, never replaces.
- **The C7 teach script and C6 registry sentence wording** — verbatim in the Handbook; don't paraphrase in future edits.
- **The four rulebooks' existing registry-sentence variants** (FACE VALUE, FORKED TONGUE, GLEAN, TWELVE TRIALS) — compliant and validated; do not rewrite to the canonical form.
- **Sign-is-rank callouts in GLEAN and BLIGHT** — they stay even though the Handbook teaches it; the callout is the mid-game reminder.
- **The applied sideways-dead-pile patches** in TRIGON, TURNCOAT, SLEEPER, WILDFIRE — settled; the Handbook states the same rule and must never drift from it.
- **CROSSROADS' v1.2-pending banner** — untouched until the end trigger lands.
- **JANUS' parked status** — the Handbook never names it; the box-draw method is described game-neutrally.
- **The 36-card master deck, subset-from-the-top rule, and pip→sign assignment** — the Handbook's numbers (Moon 1 … Crown 9) are the settled assignment; any future sign change goes through the conventions, not the Handbook.
- **The graduated component policy** — the "In the box" list is frozen; additions face the reused-by-more-than-one-game bar.
- **Everything in CORE_SET_AUDIT §7 and HOUSE_KIT_DECISION §9** — this handoff operates inside those protections.
