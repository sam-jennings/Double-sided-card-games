# Card Layout Requirements

*Physical layout specification for the double-faced master deck.*

This document defines what information each card face must carry, where it goes, and why — resolved against the competing demands of hand-fan readability, flat-on-table concealment, and 90° rotation as game state.

---

## The core problem

Every face of every card must carry three pieces of information:

1. **Symbol icon** — primary identity (matched, played, read across the table)
2. **Index pip (1–9)** — authoritative rank, subset selection, rank-sensitive games
3. **Orientation marker** — a top-edge cue that lets CROSSROADS and TWELVE TRIALS read card direction at a glance

The constraint unique to this deck: there is no card back, so both faces must be independently self-sufficient, visually identical in structure, and incapable of leaking information about the other face.

---

## Who needs what

### Games that READ the pip during play

| Game | How | When |
|---|---|---|
| FACE VALUE | Hidden pip decides showdowns; visible pip breaks ties; Cold Read names a symbol | Duel card on table; hand inspection |
| THE UNPLAYED PAIR | Highest revealed pip wins tricks | Trick-end reveal |
| THE COUNCIL | Pip = issue value, sum for final score | Tabled issues, public discard |
| CROSSROADS | Pip total for pie-rule start; tiebreak | Setup; scoring |

### Games that CONCEAL a face

| Game | What's hidden | Physical state |
|---|---|---|
| FACE VALUE | Duel card's underside | Flat on table surface |
| JANUS | Outward face of fan cards | Held in fan, angled away |
| FALSE FACE | Face pressed to table after play | Flat in ledger row |
| THE UNPLAYED PAIR | Hidden face of trick cards (until reveal) | Flat on table |
| TRIGON / TURNCOAT | Hidden face of grid cards | Flat on grid |

### Games that need ORIENTATION

| Game | Why | What "oriented" means |
|---|---|---|
| CROSSROADS | Road points at the city its visible face names; cities dim by 90° rotation | Top edge = pointing direction |
| TWELVE TRIALS | Sideways rotation = "this card was flipped" (score tracker) | Straight vs. 90° |
| THE ORRERY | Flip-tracking via rotation | Straight vs. 90° |

---

## The pip-position question — resolved to a single top-left corner pip

> **Updated June 2026 after the TURNOVER + GLEAN session (finding F2).** Earlier this spec settled on a top-centre pip and declared corners closed. Table play reopened it: players wanted corner numbers for instant fan recognition, and the original anti-corner argument only ever defeated *mirrored* corners, not a single one. The resolution below adopts a **single, non-mirrored top-left corner pip**.

### Arguments for a corner pip (standard playing-card position)

- Readable in a fanned hand without spreading — the decisive point from F2. Players recognise a fanned hand instantly when the number sits in the corner, the way every traditional card game trains them to.
- Flipping a fanned hand while holding the fan shape reveals all reverse-side values at a glance — useful for assessing hand strength (FACE VALUE, THE COUNCIL, GLEAN).
- FACE VALUE, UNPLAYED PAIR, and COUNCIL players inspect hand pips constantly.
- Subset selection ("remove 8s and 9s") stays fast.

### Why a single corner pip beats both top-centre and mirrored corners

- **vs. mirrored corners (top-left + bottom-right):** mirroring works on a normal deck because one whole face is always hidden, so the bottom-right copy is never seen alongside a contradicting "up." On this double-faced deck both faces are live, so a second pip position implies "either end can be up" and contradicts the orientation marker. A **single** top-left pip carries none of that ambiguity — there is exactly one "up," marked by the top-edge marker, and the pip sits in its corner.
- **vs. top-centre:** the original spec rejected mirrored corners and then over-generalised the conclusion to ban *all* corners, defaulting to top-centre. But top-centre is the worst position for fan readability — it's the first thing covered when cards overlap in a fan. F2 found players reaching for the corner. A single top-left pip keeps the unambiguous-orientation benefit of one pip while restoring fan readability.

### Why hidden-face leakage is not a concern either way

When a card lies flat on the table (FACE VALUE duel, FALSE FACE ledger, TRIGON grid), the bottom face is pressed against the surface — **nothing on it is physically visible**, regardless of pip placement. No corner pip, centre pip, or any other element on the underside can "peek out." The concealment is absolute by physics, not layout.

When a card is held in a JANUS fan, the holder sees their entire inner face and the table sees the entire outer face. Secrecy is enforced by angle, not by element position within a face.

**Conclusion:** pip placement is purely a readability decision, and the readability evidence (F2) points to a single top-left corner pip. The orientation marker stays top-edge-centre and remains the sole "which end is up" cue.

---

## Recommended layout

```
┌─────────────────────────────┐
│  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔  │  ← orientation marker (top-edge bar, centred)
│   ┌───┐                     │
│   │ 5 │                     │  ← index pip, single top-left corner
│   └───┘                     │
│                             │
│                             │
│         ██████████          │
│        ████████████         │
│        ██  ICON  ██         │  ← symbol icon, large, centred
│        ████████████         │
│         ██████████          │
│                             │
│                             │
│                             │
│       [ SIGN NAME ]         │  ← sign name, small, bottom-centre
│                             │
└─────────────────────────────┘
```

Both faces of every card use this identical structure. Only the symbol icon, pip number, sign name, and colour/pattern change between faces.

---

## Element-by-element specification

### Orientation marker — top edge

- **Position:** spanning or centred at the very top edge of each face.
- **Rule:** MUST be identical on both faces of every card (per [physical-handling.md](../.kiro/steering/physical-handling.md) H3 — no mark that differs between faces or correlates with the hidden face).
- **Purpose:** defines "up" for CROSSROADS pointing, TWELVE TRIALS rotation tracking, and general glanceability.
- **Form:** a thin coloured bar, small centred arrow/notch, or gradient. Subtle enough not to compete with the icon. The symbol icon's own directional art (if the shipping set has oriented symbols) provides a secondary cue.
- **When rotated 90°:** the marker moves from top to side, making the rotation immediately legible.

### Index pip — top-left corner, single instance

- **Position:** in the top-left corner, just inside the frame and below the orientation marker's left end. Single instance — **not** mirrored to the opposite corner.
- **Why a single top-left corner (per finding F2):**
  - Readable in a hand fan without spreading — players recognise a fanned hand instantly from the corner number, as every traditional card game trains them to. Top-centre is covered first when cards overlap; the corner stays exposed.
  - Flipping a held fan reveals all reverse-side pips at a glance for hand-strength assessment.
  - A single pip position is unambiguous because the card has a defined top (the orientation marker) — no mirroring needed, so no "either end is up" contradiction.
  - When the card rotates 90° (CROSSROADS dim, TWELVE TRIALS flip-mark), the pip leaves its expected corner, reinforcing the rotation signal.
  - Subset selection stays fast: thumb the top-left corners, read the number.
- **Why NOT mirrored corners:**
  - This deck has a defined orientation; a second pip position implies "either end can be up," which contradicts the orientation marker.
  - On a double-faced card, there is no back to hide a second pip from — every mark exists on a live, potentially-visible face.
- **Why NOT top-centre (superseded):** top-centre was the worst position for fan readability and was chosen only by over-generalising the case against *mirrored* corners. F2 reopened and reversed this.
- **Size:** large enough to read at arm's length; at least 8pt equivalent. Must not be mistaken for the sign name or icon detail.

### Symbol icon — centre, dominant

- **Position:** centred, filling the main body of the card.
- **Purpose:** the primary identity. Matched, counted, read across a table (JANUS fans, TRIGON 3×3 grid, TURNOVER pile).
- **Requirements:**
  - Bold, filled, high-contrast silhouette (per [deck-structure.md](../.kiro/steering/deck-structure.md)).
  - Distinct at arm's length, when rotated 90°/180°, and for colour-blind players — shape carries identity, colour is secondary.
  - Large enough that JANUS fans read across the table and TURNOVER matches verify at party speed.
- **Oriented art is welcome:** a symbol with a natural "up" (Crown points up, Flame rises, an animal faces right) gives a free secondary orientation cue without breaching H3, because the icon is identical wherever that symbol appears — it leaks nothing about the other face.

### Sign name — bottom-centre, small

- **Position:** centred horizontally at the bottom.
- **Purpose:** aids first-game teaching, accessibility (triple-redundancy: icon + pip + name), and verbal-claim games (FALSE FACE: "claim its hidden face aloud").
- **Behaviour in a fan:** partially or fully hidden when cards are tightly fanned. This is acceptable — experienced players read icon + pip; the name is a learning aid, not a primary identifier.
- **Size:** small but legible (8pt minimum per the knowledge base typography rules).

---

## What does NOT appear on a card face

| Excluded element | Why |
|---|---|
| Ability text | Per `deck-structure.md` two-layer rule: abilities live in per-game reference cards, not the permanent deck. |
| Pair-specific decoration | Would violate H3 (no mark correlating with the hidden face). |
| Mirrored/rotated pip | Contradicts the single defined orientation. |
| Any mark differing between the two faces | H3, the deck's most critical physical constraint. |
| Back-side art or pattern | There is no back. |

---

## How this serves each game's handling

| Game | Key handling moment | Layout support |
|---|---|---|
| CROSSROADS | Point road at destination; dim city by rotating 90° | Orientation marker + pip both "break" visually when rotated; icon's directional art shows pointing |
| TWELVE TRIALS | Sideways = flipped (score marker) | Rotation is immediately obvious from displaced marker and pip |
| FACE VALUE | Read pip in hand; conceal underside flat | Top-left corner pip reads in fan; underside is physically invisible |
| THE UNPLAYED PAIR | Fan hand to choose follows; flip at trick-end to reveal rank | Pip at fan corner for selection; icon centred for post-flip readability on table |
| THE COUNCIL | Assess pip values before secret commit | Pip at fan corner; clear at a glance |
| JANUS | Table reads outward face across the table; holder reads inner face | Large centred icon dominates at distance; pip confirms identity up close |
| FALSE FACE | Slap card to ledger showing previous claim; hidden face down | Icon verifies the match; pip irrelevant mid-play; name aids verbal claims |
| TURNOVER | Match target at party speed | Large icon is primary; no fine-print needed for the match |
| TRIGON / TURNCOAT | Read grid of 9 cards; identify symbols and check requirements | Large centred icons read across a shared grid; pip rarely consulted mid-play |

---

## Future-proofing

| Possible future need | Survives this layout? |
|---|---|
| New game needing rank in hand | ✓ Pip always at fan corner |
| New game using flat concealment | ✓ Underside physically invisible regardless of layout |
| New game using 90° rotation as state | ✓ Both marker and pip signal rotation |
| New game reading cards across the table | ✓ Large centred icon |
| Switching symbol sets (Signs → Menagerie → other) | ✓ Icon slot is a generic rectangle; layout is symbol-agnostic |
| Adding colour/pattern background per symbol | ✓ Background fills card; icon and pip sit over it |
| Accessibility: colour-blind, low-vision | ✓ Triple redundancy (icon shape + pip number + name text) |
| Smaller card format (mini/travel) | ✓ No wasted space on mirrored corners; scales cleanly |
| Per-game overlay cards or sleeves | ✓ Consistent structure means overlays align predictably |

---

## Open questions (for prototype testing)

1. **Pip position confirmation (F2).** The single top-left corner pip is now the spec. The remaining test is confirmatory: print a corner-pip run and verify it reads faster in a fan than the old top-centre pip without harming rotated-state legibility (CROSSROADS, TWELVE TRIALS). Watch that the corner pip doesn't collide with the orientation marker's left end.
2. **Pip size vs. icon dominance.** The pip must be large enough to read in a fan but not so large it competes with the icon. Test at print-and-play scale.
3. **Orientation marker form.** Bar vs. arrow vs. gradient — which reads fastest when rotated 90°? Test with CROSSROADS.
4. **Sign name necessity.** If the icon set is sufficiently distinct and the pip carries rank, can the name be dropped for a cleaner card? Or does FALSE FACE's verbal-claim mechanic make it load-bearing?
5. **Colour field extent.** Full-bleed colour per symbol, or a coloured border/band? Affects legibility when cards overlap in CROSSROADS road-building and FALSE FACE's ledger.

---

*This layout is designed against the full eleven-game collection as of June 2026. It defers to [deck-structure.md](../.kiro/steering/deck-structure.md) (the two-layer production rule), [physical-handling.md](../.kiro/steering/physical-handling.md) (H3: no asymmetric marks), and [design-principles.md](../.kiro/steering/design-principles.md) (handling and legibility decide). Any proposed change should be checked against the handling table above and the future-proofing checklist.*
