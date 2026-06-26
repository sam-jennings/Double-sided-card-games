# Design Document: TRIGON & TURNCOAT Retheme to Nine Signs

> **⚠️ Superseded naming (June 2026).** After this retheme shipped, the Nine Signs' pips 1–2 were renamed for legibility: **Void → Moon, Root → Leaf** (the empty-ring Void and branching Root failed the "suit test"). The change is **skin-only** — every requirement, ability, mechanic, and balance number in the mapping tables below is unchanged; only the pip-1 and pip-2 names and their one-line mnemonics differ. The live `TRIGON_rulebook.md` and `TURNCOAT_rulebook.md` already use Moon/Leaf. Throughout this document, read **Void as Moon** (catch-up: "the new moon waxes from dark") and **Root as Leaf** (connection/flip: "a leaf turns toward what it touches"). See `SYMBOL_SETS.md` §6 (Set F revision note) for the rationale. This document is retained as the design record of the retheme as originally executed.

## Overview

This design specifies the complete sign-to-ability mapping for rethreming TRIGON (formerly SYZYGY) and TURNCOAT onto the Nine Signs primary symbol set. It defines the verb families that give each sign a consistent thematic role across both games, the concrete ability assignments with mnemonic justifications, and a transformation checklist for updating each rulebook section. It also covers the game rename (SYZYGY → TRIGON), the file/folder operations required, and the cross-reference updates across the repository. No mechanics change; only names and flavour text are affected.

**Governing constraints** (from `deck-structure.md` and `product-vision.md`):
- The Nine Signs are the shipping deck identity: Void (1), Root (2), Wave (3), Flame (4), Eye (5), Mask (6), Key (7), Star (8), Crown (9).
- TRIGON and TURNCOAT are tier-1 complete games with ~45k simulated games invested. This retheme touches zero balance numbers.
- The two-layer production rule applies: rulebooks refer to permanent deck-identity names only.
- The game formerly known as SYZYGY is renamed to TRIGON — the celestial framing no longer fits the Nine Signs theme.

## Architecture

The retheme is a pure name-substitution pass over two existing documents plus a game rename, governed by a mapping layer that ensures cross-game consistency. The architecture is:

1. **Verb Family Layer** (shared) — defines what each sign "means" across all games.
2. **Per-Game Mapping Layer** — assigns each sign to one ability per game, constrained by the verb family.
3. **Transformation Layer** — the section-by-section substitution rules that produce the updated rulebooks.
4. **Rename Layer** — handles the SYZYGY → TRIGON name change, including the in-game capture-event term, variant names, and intro rewrite.
5. **File Operations Layer** — creates the new Trigon/ folder, archives the old Syzygy/ folder, and updates TURNCOAT in place.
6. **Cross-Reference Layer** — updates all repository documents that reference SYZYGY.

No mechanical logic changes. The transformation is idempotent: applying it twice yields the same result as applying it once (because the source is always the current rulebook and the mapping is fixed).

---

## Components and Interfaces

The retheme involves two components (rulebook documents) sharing a single interface (the Nine Signs symbol set), plus a set of repository-wide document updates. Each rulebook independently interprets the nine signs through its own ability mapping, but both share the same verb families to ensure cross-game coherence.

- **Shared Interface**: Nine Signs deck-identity names (Void, Root, Wave, Flame, Eye, Mask, Key, Star, Crown) with fixed pips (1–9).
- **Component A**: TRIGON_rulebook.md — assigns signs to 9 alignment-game abilities. (New file in new folder.)
- **Component B**: TURNCOAT_rulebook.md — assigns signs to 9 allegiance-game abilities. (Updated in place.)
- **Component C**: Repository cross-references — all documents that mention SYZYGY or point to the Syzygy/ folder.
- **Contract**: Each sign's verb family constrains which abilities it may carry in either game.

## Data Models

The core data model is the Sign_Mapping: a pair of bijections from the set of Nine Signs to the set of abilities in each game, constrained by verb-family coherence and two locked assignments (Star→TRIGON wild, Void→TRIGON catch-up).

```
SignMapping = {
  trigon: Map<Sign, TrigonAbility>     // bijection, 9 entries
  turncoat: Map<Sign, TurncoatAbility> // bijection, 9 entries
  verbFamilies: Map<Sign, VerbFamily>  // shared across both
  constraints: [Star→TrigonWild, Void→TrigonCatchUp]
}

RenameMapping = {
  gameName: "SYZYGY" → "TRIGON"
  captureEvent: "syzygy" → "trigon"
  introFrame: "alignment of three celestial bodies" → "convergence of three signs"
  variants: {
    "Calm Skies" → "Calm Signs"
    "Deep Space" → "Deep Signs"
  }
  folder: "Syzygy/" → "Trigon/" (new; old archived)
}

CrossReferenceUpdate = {
  documents: [COLLECTION_OVERVIEW, SYMBOL_SETS, NEW_GAME_CONCEPTS,
              DECK_SIZE_DECISION, flip_card_project_goals, steering files]
  rule: replace live-game references "SYZYGY" → "TRIGON",
        replace folder paths "Syzygy/" → "Trigon/",
        historical/analytical references may keep old name with parenthetical
}
```

## 1. Verb Family Definitions

Each sign carries a single thematic verb family — a core archetype that both games' abilities must recognisably express. The verb family is the mnemonic bridge: learn what a sign "means" once, and both games reinforce it.

| Sign (pip) | Verb Family | Core Archetype |
|---|---|---|
| **Void** (1) | Emptiness / Catch-up | Absence, isolation, erasure; the outsider who gains when others have more |
| **Root** (2) | Connection / Influence | Adjacency, anchoring, reaching neighbours; being grounded enables local change |
| **Wave** (3) | Movement / Flow | Displacement, carrying, transit; things in motion change along the way |
| **Flame** (4) | Destruction / Removal | Burning, consuming; what's beside the fire is fuel |
| **Eye** (5) | Perception / Revelation | Seeing hidden truth, peeking, choosing to reveal or conceal |
| **Mask** (6) | Identity-change / Flip | Disguise, face-switching; the Mask alters who something appears to be |
| **Key** (7) | Extraction / Access | Unlocking, rearranging, freeing; access enables movement others can't achieve |
| **Star** (8) | Wild / Exception | The anomaly — counts as anything, draws the unexpected into play |
| **Crown** (9) | Authority / Sovereignty | Command, decree, self-determination; the apex that rules or departs on its own terms |

---

## 2. Complete Sign-to-Ability Mapping

### 2.1 TRIGON

Abilities listed in pip order of their assigned sign. The requirement and mechanical effect columns are unchanged from the current rulebook — only the name in the first column is new.

| Sign (pip) | Requirement (unchanged) | Ability (unchanged) | Mnemonic justification |
|---|---|---|---|
| ⚫ **Void** (1) | Has **no** orthogonally adjacent cards | *Only if you have fewer captured cards than someone else:* take the top card of the deck face-down into your score pile (worth 1 card) | The Void fills itself — emptiness draws substance when others have more |
| 🌱 **Root** (2) | On an edge cell (non-corner border) | Flip one card **orthogonally adjacent** to it | Roots grow at the border and turn what they touch |
| 🌊 **Wave** (3) | Shares its row **or** column with at least one empty cell | **Move** any one card on the grid to any empty cell | The Wave carries a card to an open shore |
| 🔥 **Flame** (4) | Has exactly **1 or 2** orthogonally adjacent cards | **Discard** one of those adjacent cards to the removed pile (out of the game) | Flame consumes what's beside it |
| 👁 **Eye** (5) | Has at least one empty orthogonally adjacent cell | **Peek** at the hidden side of any one adjacent card; you may then flip it | The Eye sees what's hidden nearby and may expose it |
| 🎭 **Mask** (6) | In the middle row **or** middle column (the central cross) | Flip **any** one card on the grid | The Mask at the crossroads can change any face in sight |
| 🗝 **Key** (7) | Has **2 or more** orthogonally adjacent cards | **Swap** any two cards on the grid | The Key unlocks positions — well-connected, it rearranges at will |
| ⭐ **Star** (8) | On a corner cell | **Draw the next card** from the deck and play it (full turn rules apply). *Star is also wild in alignments.* | A Star on the corner draws the next card from the sky. Star is wild. |
| 👑 **Crown** (9) | Its row **or** its column is fully occupied | Choose that full line: **flip the other two cards** in it | When the court is full, the Crown decrees — the other two must change face |

### 2.2 TURNCOAT

Abilities listed in pip order of their assigned sign. Requirement and mechanical effect columns are unchanged.

| Sign (pip) | Requirement (unchanged) | Ability (unchanged) | Mnemonic justification |
|---|---|---|---|
| ⚫ **Void** (1) | A rival has **2+ more** banked cards than you | Choose such a rival: their **top banked card** is removed from the game | The Void erases — when you're behind, it devours what the leader hoarded |
| 🌱 **Root** (2) | Adjacent to one of **your** agents | **Swap** Root's card with any other agent; you may then **flip** the displaced agent at Root's old post | Deep roots among allies let you displace and overturn intruders |
| 🌊 **Wave** (3) | **Exactly one** adjacent agent | **Move** that agent to any empty post; you may then **flip** it | The Wave carries one thing away and tumbles it |
| 🔥 **Flame** (4) | Adjacent to a rival agent | **Remove** one adjacent rival agent from the game (its post empties) | Flame consumes a rival beside it |
| 👁 **Eye** (5) | At most **one** adjacent agent | **Peek** at the hidden face of an adjacent agent; you may then **flip** it | The Eye in solitude sees truth, and may reveal it |
| 🎭 **Mask** (6) | Adjacent to a rival agent | **Flip** any one agent in Mask's row or column | The Mask near an enemy turns a face in its line — identity is mutable |
| 🗝 **Key** (7) | Key's row **or** column holds **2+** of your agents | **Extract** one of your agents from Key's row or column straight to your pile (its post empties) | The Key among allies unlocks one of yours from the line |
| ⭐ **Star** (8) | **Two or more** adjacent agents | **Draw the next card** from the deck and play it immediately (full turn rules) | A Star well-connected draws the unexpected into play |
| 👑 **Crown** (9) | Adjacent to one of **your** agents | **Extract Crown's own card** to its guild-owner's pile (its post empties) | The Crown beside its allies withdraws to safety — sovereign departure |

---

## 3. Verb Family Coherence Demonstration

For each sign, both game abilities are recognisable expressions of the same archetype:

| Sign | TRIGON expression | TURNCOAT expression | Shared core |
|---|---|---|---|
| **Void** | Draw when isolated (fill emptiness, catch-up) | Erase leader's gain (catch-up through removal) | Both are catch-up mechanisms triggered by deficiency |
| **Root** | Flip adjacent from edge (border influence on neighbour) | Swap self + flip displaced (allied connection enables displacement) | Both require adjacency/connection and influence neighbours |
| **Wave** | Move a card to empty space (carry across the board) | Move adjacent + optional flip (carry away and tumble) | Both displace a card; TURNCOAT adds transformation-in-transit |
| **Flame** | Discard adjacent card (burn beside it) | Remove adjacent rival (burn beside it) | Both destroy one adjacent target — the flame verb is identical |
| **Eye** | Peek + optional flip adjacent (observe and optionally reveal) | Peek + optional flip adjacent (observe and optionally reveal) | Mechanically near-identical — the purest cross-game echo |
| **Mask** | Flip any card from centre (change any face in sight) | Flip any in row/col from rival proximity (turn a face in its line) | Both flip/change identity; differ in reach (any vs. row/col) |
| **Key** | Swap two cards when well-connected (unlock rearrangement) | Extract own from line when allies present (unlock a card from its position) | Both use "access" (connections) to free/rearrange |
| **Star** | Wild in alignment + draw from corner (the exception that pulls new into play) | Draw-and-play when well-connected (the Star yields a new card) | Both draw an extra card into play — Star = bonus draw |
| **Crown** | Flip two in full line (decree when court complete) | Extract self to owner (sovereign self-banking) | Both express supreme agency: commanding others or commanding self |

---

## 4. Mapping Justification: Edge Cases and Conflicts

### 4.1 Crown's dual expression

Crown's TRIGON ability (flip two in a full line) and TURNCOAT ability (extract self) look mechanically different. The verb-family coherence is "authority/sovereignty" — in TRIGON the Crown exercises authority *over others* (a decree to its full court), in TURNCOAT the Crown exercises authority *over itself* (choosing to depart). Both require being in a position of strength (full line / adjacent to allies) and both represent the apex sign acting with supreme agency. This is the mapping's widest thematic stretch, but it remains within the verb family because "authority" encompasses commanding others AND self-determination.

### 4.2 Key's dual expression

Key in TRIGON swaps two cards (positional rearrangement), while in TURNCOAT it extracts an allied card from a line. The unifying idea is "access/unlocking" — the Key gains access through connections (2+ adjacent in TRIGON, 2+ allies in line in TURNCOAT) and uses that access to *free* something (free cards from their positions / free an ally from its row). "Unlock" covers both.

### 4.3 Root's requirement difference

Root in TRIGON requires an *edge cell* (border position), while in TURNCOAT it requires *adjacency to own agent*. Both are fundamentally "connection" requirements — the Root is defined by what it's connected to (the border / allies). The thematic link: roots need ground (edge = border soil; allied agent = allied soil). The ability expressions (flip adjacent / swap+flip displaced) both involve influencing a neighbouring card.

### 4.4 The Void catch-up parallel

Both Void abilities are catch-up mechanisms, but they work differently: TRIGON draws a bonus card when behind; TURNCOAT removes the leader's top card when behind. Both are triggered by deficiency (fewer cards / rival 2+ ahead). Both equalise. The shared archetype is "emptiness seeks balance" — whether by filling itself or by creating absence in the leader's pile.

### 4.5 No sign conflicts

Every sign is used exactly once in each game. No two signs share a verb family. No ability is left unassigned. The two locked mappings (Star→wild/draw in TRIGON, Void→catch-up in TRIGON) are satisfied. Star's TURNCOAT assignment (draw-and-play) reinforces rather than contradicts the "Star draws" mnemonic from TRIGON.

### 4.6 Pip reordering

The old rulebooks listed abilities by their original symbol's pip. Under the new mapping, several abilities change pip position:

| Old TRIGON name (old pip) | New sign (new pip) | Pip change |
|---|---|---|
| Sun (1) | Mask (6) | 1 → 6 |
| Moon (2) | Root (2) | unchanged |
| Star (3) | Star (8) | 3 → 8 |
| Comet (4) | Wave (3) | 4 → 3 |
| Eclipse (5) | Key (7) | 5 → 7 |
| Aurora (6) | Eye (5) | 6 → 5 |
| Meteor (7) | Flame (4) | 7 → 4 |
| Nova (8) | Crown (9) | 8 → 9 |
| Void (9) | Void (1) | 9 → 1 |

| Old TURNCOAT name (old pip) | New sign (new pip) | Pip change |
|---|---|---|
| Blade (1) | Flame (4) | 1 → 4 |
| Mask (2) | Mask (6) | 2 → 6 |
| Whisper (3) | Eye (5) | 3 → 5 |
| Coin (4) | Star (8) | 4 → 8 |
| Veil (5) | Root (2) | 5 → 2 |
| Key (6) | Key (7) | 6 → 7 |
| Hound (7) | Wave (3) | 7 → 3 |
| Crown (8) | Crown (9) | 8 → 9 |
| Ash (9) | Void (1) | 9 → 1 |

The ability reference tables in both rulebooks must be re-sorted into the new pip order (1–9 of the assigned sign). This is a presentation change, not a mechanical one.

---

## 5. Transformation Checklist

### 5.1 TRIGON Rulebook Sections

| Section | Transformation required |
|---|---|
| **Title & intro paragraph** | Title becomes "TRIGON". Replace celestial-alignment flavour with Nine Signs convergence flavour: "the alignment of three celestial bodies" → "a three-point convergence of signs." Remove pronunciation guide (TRIGON needs none). Replace "celestial bodies" / "celestial symbols" with "signs." |
| **Components** | Replace "9 celestial symbols" with "9 signs." |
| **Setup** | Replace "whoever most recently saw the night sky" with an equivalent Nine Signs first-player rule (e.g. "whoever most recently noticed a sign they couldn't explain"). No mechanical change. |
| **Turn overview** | No symbol names appear here — no changes needed. |
| **Alignments (capturing)** | Replace the section's narrative term: "that's a *syzygy*" → "that's a *trigon*". "Star is wild" stays verbatim (Req 1.4). Replace icon references if present. The wild rule itself is unchanged. |
| **Activations intro** | Replace "Every symbol has a requirement…" with "Every sign has a requirement…" |
| **The 9 symbols table** | Rename to "The 9 signs." Re-sort rows by new pip order (Void 1, Root 2, Wave 3, Flame 4, Eye 5, Mask 6, Key 7, Star 8, Crown 9). Replace all symbol names and icons. Mechanics text in requirement/ability columns is untouched. |
| **Chains worked example** | Rewrite using new sign names for the same mechanical sequence: Root placed on edge → flip turns a card into a Mask → Mask activates (central cross) flipping another card → alignment triggers capture. Adjust to be mechanically valid with new pip assignments. |
| **Game end & scoring** | Replace "Face-down Void cards" reference — Void is still the catch-up sign so this stays as "Face-down Void cards count as 1 each." No change needed. |
| **Edge cases & FAQ** | Replace symbol names. "Flame discards itself? No — Flame discards an adjacent card, never itself." "Star's extra play…" stays. "Crown's row AND column are both full. Choose one line to flip." etc. |
| **Strategy notes** | Replace all symbol name references. E.g. "Stars are double-edged" stays as-is (Star is still wild). |
| **Card manifest** | Replace all 9 symbol icons/names with Nine Signs equivalents. The 36 pairs are unchanged structurally. |
| **Designer's variants** | "Calm Skies" → **"Calm Signs"**: Star is not wild. "Deep Space" → **"Deep Signs"**: Key may only swap itself with another card (was Eclipse). Mechanics preserved; only names change. |
| **Sibling reference** | End-of-document note reads: "A sibling to TURNCOAT: same deck architecture, opposite soul." |
| **Design version note** | Update to: "Design v1.2 — rules balanced over ~23,000 simulated games." Game name in any surrounding text becomes TRIGON. |

### 5.2 TURNCOAT Rulebook Sections

| Section | Transformation required |
|---|---|
| **Title & intro paragraph** | Replace guild/court/intrigue flavour with Nine Signs flavour. Keep the double-allegiance / defection theme but frame agents as "bearing signs" rather than "serving guilds." |
| **Components** | Replace "9 guild symbols" with "9 signs." |
| **Setup — Claim your guilds** | Rename to "Claim your signs." Replace "guild symbols" with "signs." Replace "unclaimed guild is unaligned" with "unclaimed sign is unaligned." |
| **Your turn** | Replace "guild" with "sign" in extraction/banking references. |
| **Agents, allegiance, and flipping** | Replace "guild on its showing face" with "sign on its showing face." "Its allegiance is the sign on its showing face: yours, a rival's, or unaligned." |
| **Activations intro** | Replace "Every guild has a requirement…" with "Every sign has a requirement…" |
| **The 9 guilds table** | Rename to "The 9 signs." Re-sort by new pip order (Void 1, Root 2, Wave 3, Flame 4, Eye 5, Mask 6, Key 7, Star 8, Crown 9). Replace all names/icons. Mechanics unchanged. |
| **Chains worked example** | Rewrite using new sign names for the same mechanical sequence: Eye sits beside a lone rival Mask → activate Eye, peek + flip → reveals a Key of yours → Key's column already has another ally → activate Key, extract → post empties next to Wave → Wave drags and flips. |
| **Game end & scoring** | No symbol names appear in scoring rules (points per card, points per sign on grid). No change needed except ensuring "your signs" replaces "your guilds." |
| **Edge cases & FAQ** | Replace all guild names. "Star's extra card — full rules?" "Who can activate Crown?" "Void with the scores level?" etc. |
| **Strategy notes** | Replace guild names. "Watch the Void gap" (was "Ash gap"). |
| **First-game preset teams** | Replace icons/names. E.g. "🔥🗝🌱🌊 vs 🎭👁👑⚫" with the appropriate sign groupings. Keep balance-validated groupings unchanged (same sets of pip numbers, just new names). |
| **Card manifest** | Replace all 9 icons/names. Same 36-pair structure. |
| **Designer's variants** | "Loyalists: you may only activate agents of *your own* signs." "Bounty: covering an unaligned agent banks it to you." No sign-specific names needed here. |
| **Sibling reference** | End-of-document note reads: "A sibling to TRIGON: same deck architecture, opposite soul." (Was "A sibling to SYZYGY".) |

### 5.3 Cross-Cutting Concerns

| Concern | Resolution |
|---|---|
| **"Star is wild" preserved verbatim** | ✓ Star (8) maps to the wild ability in TRIGON. The phrase "Star is wild" appears unchanged. |
| **Ability table ordering** | Both tables re-sorted by new pip: Void(1), Root(2), Wave(3), Flame(4), Eye(5), Mask(6), Key(7), Star(8), Crown(9). |
| **Icon consistency** | Use the same Nine Signs icons in both rulebooks. Suggested: ⚫ Void · 🌱 Root · 🌊 Wave · 🔥 Flame · 👁 Eye · 🎭 Mask · 🗝 Key · ⭐ Star · 👑 Crown. (Final icons are an art decision; these are placeholders that read clearly in Markdown.) |
| **No new lore** | Mnemonic justifications are kept to one-sentence or parenthetical. No added fiction. |
| **Version note** | Preserved: "Design v1.2 — rules balanced over ~23,000 simulated games" (TRIGON) and "~22,000 simulated games" (TURNCOAT). |
| **Two-layer rule compliance** | No game-local aliases. Rulebooks use the permanent deck-identity names exclusively. |
| **Capture-event term** | The in-game term for three-in-a-row changes from "syzygy" to "trigon" (lowercase in running text, matching the game name). |

---

## 6. Game Rename: SYZYGY → TRIGON

### 6.1 Rationale

The name "SYZYGY" (the alignment of three celestial bodies) no longer fits: the Nine Signs are not celestial bodies. The replacement name **TRIGON** (from Greek *trigōnon*, "three-cornered") captures the core mechanic — a three-point convergence of matching signs — without binding the game to any specific thematic family. It is short, memorable, and needs no pronunciation guide.

### 6.2 In-Game Capture Event Term

The current rulebook uses "syzygy" (lowercase) as the name for the three-in-a-row capture event:

> "…that's a *syzygy*: you immediately capture all three cards…"

This becomes:

> "…that's a *trigon*: you immediately capture all three cards…"

The term "trigon" (lowercase) names the event — three matching signs aligning. It echoes the game title naturally.

### 6.3 Intro Paragraph Rewrite Direction

**Current (celestial):**
> **Syzygy** (SIZ-uh-jee): the alignment of three celestial bodies. Place cards, trigger their powers, and chain reactions across the sky — but the moment three matching symbols align, whoever caused it claims them. Capture the most of the sky to win.

**New (Nine Signs convergence):**
> **Trigon**: a three-point convergence of signs. Place cards, trigger their powers, and chain reactions across the grid — but the moment three matching signs converge, whoever caused it claims them. Capture the most signs to win.

Key changes:
- No pronunciation guide (TRIGON is phonetically obvious).
- "alignment of three celestial bodies" → "three-point convergence of signs."
- "across the sky" → "across the grid."
- "three matching symbols align" → "three matching signs converge."
- "Capture the most of the sky" → "Capture the most signs."

### 6.4 Designer's Variant Renames

Both variant names reference the celestial/space theme and must be updated. Mechanics are preserved verbatim.

| Current Name | New Name | Mechanic (unchanged) |
|---|---|---|
| **Calm Skies** | **Calm Signs** | Star is *not* wild. Slower captures, gentler pace. |
| **Deep Space** | **Deep Signs** | Key may only swap *itself* with another card. Slightly fewer captures, more positional. |

The naming pattern "Calm/Deep Signs" keeps the adjective structure, stays Nine Signs–themed, and requires no further explanation. "Calm Signs" suggests a quieter game (fewer wild triggers); "Deep Signs" suggests a more considered, positional game.

### 6.5 Sibling References

| Document | Current | Updated |
|---|---|---|
| TRIGON_rulebook.md (end) | "A sibling to SYZYGY" (n/a — new doc) | "A sibling to TURNCOAT: same deck architecture, opposite soul." |
| TURNCOAT_rulebook.md (end) | "A sibling to SYZYGY: same deck architecture, opposite soul." | "A sibling to TRIGON: same deck architecture, opposite soul." |

---

## 7. File and Folder Operations

### 7.1 Create Trigon/ Folder

Per `repository-structure.md`: one folder per game, Title Case folder name, rulebook as `<GAME>_rulebook.md` (UPPER_SNAKE prefix).

```
Trigon/
└── TRIGON_rulebook.md
```

The new rulebook is the complete rethemed document — standalone, needing no reference to the old SYZYGY_rulebook.md.

### 7.2 Archive Notice for Syzygy/SYZYGY_rulebook.md

Add the following notice to the **top** of `Syzygy/SYZYGY_rulebook.md`, above the existing `# SYZYGY` heading:

```markdown
> **⚠️ ARCHIVED** — This game has been renamed to **TRIGON** as part of the Nine Signs retheme.
> The live rulebook is at [`Trigon/TRIGON_rulebook.md`](../Trigon/TRIGON_rulebook.md).
> This file is retained as a read-only design record of the pre-rename version.
```

No other changes to `Syzygy/SYZYGY_rulebook.md`. The folder and its contents remain untouched as an archive per `repository-structure.md` ("When a game is cut [or renamed], keep its folder as an archive/design record").

### 7.3 TURNCOAT_rulebook.md — In-Place Update

TURNCOAT is not renamed. Its rulebook is updated in its existing location:

```
Turncoat/TURNCOAT_rulebook.md  (modified in place)
```

Changes:
- All guild names → Nine Signs names.
- Sibling reference → "A sibling to TRIGON."
- All other changes per §5.2.

---

## 8. Cross-Reference Updates

The following documents reference SYZYGY and must be updated to point to TRIGON and the new folder path.

### 8.1 Documents to Update

| Document | Nature of references | Action |
|---|---|---|
| **COLLECTION_OVERVIEW.md** | Game name in all tables (coverage, selectors, genre/mood, play order), folder path, status tier listing | Replace "SYZYGY" → "TRIGON", "Syzygy/" → "Trigon/" throughout. Add a note that Syzygy/ is retained as archive. Update play-order position 2 to show TRIGON. |
| **SYMBOL_SETS.md** | References to SYZYGY as a game (sensitivity tiers, ability tables, skin-fit discussions) | Replace live-game references with "TRIGON". In §5 sensitivity tiers and §6 fit matrices where SYZYGY appears as the game name, update to TRIGON. Historical discussion of the celestial skin (Set A, "SYZYGY's native skin") may retain "SYZYGY" with a parenthetical: "(now TRIGON)". |
| **NEW_GAME_CONCEPTS.md** | Likely references SYZYGY in status/tier discussions | Replace live-game references → TRIGON. |
| **DECK_SIZE_DECISION.md** | May reference SYZYGY as an example of even divisibility | Replace → TRIGON. |
| **flip_card_project_goals.md** | Founding vision may mention SYZYGY as a flagship | Replace → TRIGON (with parenthetical if historical context warrants). |
| **COLLECTION_AUDIT.md** | If present, any audit references | Replace → TRIGON. |

### 8.2 Steering Files

| File | Action |
|---|---|
| `.kiro/steering/product-vision.md` | References "SYZYGY" in tier-1 list and collection identity. Replace with "TRIGON". |
| `.kiro/steering/deck-structure.md` | References "SYZYGY" in structural properties table and role symbols section. Replace with "TRIGON". |
| `.kiro/steering/design-principles.md` | References "SYZYGY" in lessons-learned section. Replace with "TRIGON". |
| `.kiro/steering/repository-structure.md` | References "SYZYGY" in naming convention example. Replace with "TRIGON". |
| `.kiro/steering/playtesting.md` | May reference SYZYGY in test-focus discussions. Replace if present. |

### 8.3 Handling Historical References

Where a document discusses the *old name in analytical or historical context* (e.g. "SYZYGY's native celestial skin" in SYMBOL_SETS.md), the reference may remain with a parenthetical noting the rename:

> "SYZYGY (now TRIGON)" or "the game formerly called SYZYGY"

This preserves the design record's readability while making the rename clear.

---

## 9. Potential Conflicts and Mitigations

### 9.1 "Crown" name collision in TURNCOAT

TURNCOAT's current Crown ability (extract self) maps to the Nine Signs Crown (9). The name is unchanged — this is a free inheritance rather than a collision. No mitigation needed.

### 9.2 "Mask" name collision in TURNCOAT

TURNCOAT's current Mask ability (flip in row/col) maps to the Nine Signs Mask (6). Same situation — name preserved by design. No collision.

### 9.3 "Key" name collision in TURNCOAT

TURNCOAT's current Key ability (extract own from line) maps to Nine Signs Key (7). Free inheritance. No collision.

### 9.4 Star (8) in TURNCOAT — pip 8 vs old Coin pip 4

Star's draw-and-play ability was previously on pip 4 (Coin). Under the new mapping it sits on pip 8. The requirement (2+ adjacent) and effect (draw-and-play) are unchanged. Only the pip-position in the ability table changes. Players reading the card see pip 8 + Star icon; the rulebook tells them "Star: 2+ adjacent → draw-and-play." No ambiguity.

### 9.5 Void (1) in TURNCOAT — pip 1 vs old Ash pip 9

The catch-up/burn ability was the highest pip (9) and is now the lowest (1). There is a mild flavour tension: the *lowest*-rank sign carries a powerful catch-up ability. However, per `deck-structure.md` §4, the pip is authoritative for rank — the ability's power level is orthogonal to its pip number (TRIGON's current Void-9 is already arguably the weakest ability despite highest pip). The Void archetype (emptiness, outsider, catch-up) is more mnemonically important than pip prestige. No mitigation needed.

### 9.6 First-game preset teams in TURNCOAT

The preset teams are balanced by simulation around specific *ability groupings*, not pip numbers. Under the retheme, each old guild maps to a new sign; the teams are listed by new sign names while preserving the same ability combinations.

| Format | Team A | Team B | Unaligned |
|---|---|---|---|
| **2P** | 🔥 Flame · ⭐ Star · 🌱 Root · 🌊 Wave | 🎭 Mask · 👁 Eye · 👑 Crown · ⚫ Void | 🗝 Key |
| **3P** | 🎭 Mask · 🌊 Wave · 🌱 Root | 🔥 Flame · 👑 Crown · 👁 Eye | ⭐ Star · 🗝 Key · ⚫ Void |
| **4P** | 🔥 Flame · 🌱 Root | ⭐ Star · 👁 Eye | 🌊 Wave · 👑 Crown | 🗝 Key · ⚫ Void | 🎭 Mask |

*(3P and 4P derived by mapping old guild→new sign from the original preset table. Mechanical balance is identical.)*

### 9.7 Variant name "Calm Signs" / "Deep Signs" — ambiguity risk

Both new variant names follow the "[Adjective] Signs" pattern. The risk of confusion between them is low because:
- "Calm" clearly signals "gentler, fewer triggers" (Star not wild).
- "Deep" clearly signals "more positional, more considered" (Key restricted).
- The mechanics description immediately follows each name in the variants section.

---

## 10. Summary: The Complete Bijection

### At a glance — old name to new sign

| TRIGON old | → Nine Sign | TURNCOAT old | → Nine Sign |
|---|---|---|---|
| Sun | **Mask** (6) | Blade | **Flame** (4) |
| Moon | **Root** (2) | Mask | **Mask** (6) |
| Star | **Star** (8) | Whisper | **Eye** (5) |
| Comet | **Wave** (3) | Coin | **Star** (8) |
| Eclipse | **Key** (7) | Veil | **Root** (2) |
| Aurora | **Eye** (5) | Key | **Key** (7) |
| Meteor | **Flame** (4) | Hound | **Wave** (3) |
| Nova | **Crown** (9) | Crown | **Crown** (9) |
| Void | **Void** (1) | Ash | **Void** (1) |

---

## Error Handling

Potential failure modes in the retheme process and their mitigations:

| Failure Mode | Detection | Mitigation |
|---|---|---|
| A sign name accidentally used twice in one game | Bijection check (Property 1) | The mapping table in §2 is the single source of truth |
| Old celestial/guild name leaks into rethemed text | Full-text search for old names (Property 6) | Checklist in §5 covers every section; search-and-verify pass |
| Mechanical text accidentally altered during name swap | Diff against original with names reverted (Property 3) | Work from the originals, substituting only the symbol column |
| Ability table sorted by old pip instead of new pip | Pip-order check (Property 7) | Re-sort after all name substitutions are complete |
| Preset teams rebalanced (they shouldn't be) | Compare pip-groupings pre/post | Map old guild → new sign 1:1; keep groupings |
| Game title "SYZYGY" leaks into TRIGON rulebook | Full-text search (Property 9) | The TRIGON rulebook is a new file; no copy-paste from old title |
| Capture-event term "syzygy" leaks into TRIGON rulebook | Full-text search (Property 9) | Replace all instances in the alignments section |
| Cross-reference document still says "SYZYGY" for live game | Full-text search across repository (Property 10) | Checklist in §8 covers every document |
| Syzygy/ folder modified beyond archive notice | Diff check | Only one line (the notice) is prepended; rest is untouched |
| TURNCOAT sibling reference still says "SYZYGY" | Text check (Property 11) | §5.2 checklist explicitly covers the sibling line |

## Testing Strategy

Validation of the retheme is a document review task (not a software test), proceeding in this order:

1. **Mapping verification**: Confirm the bijection tables in §10 assign all 9 signs exactly once per game.
2. **Verb-family audit**: For each sign, verify both game abilities plausibly fall within the declared archetype.
3. **Mechanical diff**: For each ability, compare the requirement and effect text against the original, confirming only the name changed.
4. **Completeness scan**: Verify all rulebook sections exist in the output and no old names remain.
5. **Pip-order check**: Verify the ability table rows are in pip 1–9 order.
6. **Preset team validation**: Verify the preset teams in TURNCOAT map old-guild→new-sign correctly (same ability groupings).
7. **Rename verification**: Confirm the TRIGON rulebook uses "TRIGON" throughout, "trigon" for the capture event, and contains no pronunciation guide.
8. **Variant name check**: Confirm "Calm Signs" and "Deep Signs" replace "Calm Skies" and "Deep Space" with mechanics unchanged.
9. **File structure check**: Confirm Trigon/ folder exists with TRIGON_rulebook.md, Syzygy/ has archive notice, TURNCOAT updated in place.
10. **Cross-reference sweep**: Full-text search across repository for "SYZYGY" — any remaining live-game references are bugs.

---

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system — essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Bijection Invariant

For any valid Sign_Mapping, the assignment of Nine Signs names to abilities in each game is a bijection — every sign appears exactly once per game, and every ability has exactly one sign assigned.

**Validates: Requirements 1.1, 1.5**

### Property 2: Verb Family Coherence

For any sign in the Nine Signs set, the TRIGON ability and the TURNCOAT ability assigned to that sign both fall within the sign's declared verb family as defined in the verb family table.

**Validates: Requirements 2.1, 2.2**

### Property 3: Mechanical Text Preservation

For any ability in either game, the requirement text and effect text in the rethemed rulebook are identical to the original rulebook text after reverting all sign-name substitutions back to original names.

**Validates: Requirements 3.1, 3.2, 3.5, 3.6**

### Property 4: Numeric Preservation

For any numeric value appearing in the original rulebooks (player counts, grid dimensions, turn counts, scoring values, tiebreaker rules, adjacency definitions, activation limits), the same numeric value appears in the corresponding position in the rethemed rulebook.

**Validates: Requirements 3.3**

### Property 5: Section Completeness

For any section heading present in the original rulebook, a corresponding section heading exists in the rethemed rulebook, and no sections are added or removed.

**Validates: Requirements 4.1**

### Property 6: Canonical Name Usage

For any symbol reference in a rethemed rulebook, the name used is exactly one of the nine permanent deck-identity names (Void, Root, Wave, Flame, Eye, Mask, Key, Star, Crown) — no old celestial/guild names appear, and no game-local aliases are introduced.

**Validates: Requirements 4.2, 4.3, 4.4, 7.1**

### Property 7: Pip-Order Table Sorting

For any ability reference table in a rethemed rulebook, the rows are sorted in ascending order by the pip number (1–9) of the sign assigned to each ability.

**Validates: Requirements 6.3**

### Property 8: Card Manifest Structural Preservation

For any card manifest in a rethemed rulebook, it contains exactly 36 entries, each representing an unordered pair of two distinct Nine Signs names, and the set of pairs forms the complete graph K₉ on the nine signs.

**Validates: Requirements 3.4, 4.4**

### Property 9: Game Rename Completeness (TRIGON rulebook)

For any occurrence of a game-title reference in the TRIGON rulebook, the text uses "TRIGON" (uppercase, for the game name) or "trigon" (lowercase, for the capture-event term) — no instance of "SYZYGY" or "syzygy" remains, and no pronunciation guide appears.

**Validates: Requirements 8.1, 8.3, 8.4**

### Property 10: Cross-Reference Consistency

For any live-game reference to the alignment game in the set of repository documents {COLLECTION_OVERVIEW.md, SYMBOL_SETS.md, NEW_GAME_CONCEPTS.md, DECK_SIZE_DECISION.md, flip_card_project_goals.md, all steering files}, the reference uses "TRIGON" (not "SYZYGY") and folder paths use "Trigon/" (not "Syzygy/"), except where the old name appears in clearly marked historical/analytical context with a parenthetical noting the rename.

**Validates: Requirements 10.1, 10.3, 10.5, 10.6**

### Property 11: Sibling Reference Consistency

For any sibling-reference line at the end of either rulebook, the reference names the correct partner game: TRIGON_rulebook.md references TURNCOAT, and TURNCOAT_rulebook.md references TRIGON.

**Validates: Requirements 8.5, 9.6**

### Property 12: Designer's Variant Rename Preservation

For any designer's variant in the TRIGON rulebook, the variant name does not reference the old celestial theme (no "Skies", "Space", or celestial terminology), and the variant's mechanical description is identical to the original.

**Validates: Requirements 8.6, 3.6**
