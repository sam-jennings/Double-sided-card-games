# TRIGON

*A game of converging signs for 2–4 players · ~15–25 minutes · ages 10+*

**Trigon**: a three-point convergence of signs. Place cards, trigger their powers, and chain reactions across the grid — but the moment three matching signs converge, whoever caused it claims them. Capture the most signs to win.

---

## Components

- **36 double-faced cards.** There are 9 signs. Every possible *pair* of two different signs appears on exactly one card (one sign per face). Each sign therefore appears on exactly 8 cards.
- This rulebook (the sign reference table below is the only thing you'll need mid-game).

A full card manifest is at the end of this document.

---

## Setup

1. Shuffle the deck thoroughly, **flipping random chunks as you shuffle** so each card's face-up side is randomised (riffle one half flipped, or smush-shuffle — anything that randomises faces).
2. Stack the deck face... well, *a* face up — with double-faced cards the top card is always visible. **The top card of the deck is public information.** Its hidden side is not.
3. Leave space for a **3×3 grid** in the middle of the table. It starts empty.
4. Choose a start player (whoever most recently noticed a sign they couldn't explain). Play proceeds clockwise.

With 2/3/4 players everyone gets exactly 18/12/9 turns — the deck divides evenly.

---

## Turn overview

On your turn:

1. **Draw** the top card of the deck. Look at both sides secretly.
2. **Place** it in any **empty** cell of the grid, choosing which side faces up.
   - *If the grid is full:* first discard any one card from the grid to a face-down **removed pile** (out of the game), then place into the empty cell.
3. **Resolve** the consequences (alignments and activations — see below), in any order you choose, until nothing new is triggered.

Then the next player draws. When the deck runs out, the game ends at the end of that turn.

---

## Alignments (capturing)

The instant **three cards in a row, column, or diagonal show the same sign face-up**, that's a *trigon*: **you** (the player whose turn it is) immediately capture all three cards into your score pile, leaving those cells empty.

- **Star is wild.** A face-up Star counts as any sign for alignments. Two Roots and a Star? Captured. Two Stars and a Wave? Captured. Three Stars? Captured.
- Alignments are checked **continuously** — after your placement and after *every* ability resolution. If an ability flips or moves a card into alignment, you capture it, even mid-chain.
- If two lines complete at the same moment, capture all cards involved (overlapping cards are captured once).
- Captured cards keep their face-up sign visible in your score pile (this matters for the tiebreaker). They never activate abilities.
- **The active player always captures**, even if an opponent's earlier placements did most of the work. Be careful what you leave on the board.

---

## Activations (abilities)

Every sign has a **requirement** (about where it sits on the grid) and an **ability**. A card becomes **charged** when:

- it is just **placed**, or
- it is **flipped** or **moved** (by any ability), or
- its requirement **changes from unmet to met** (e.g. a Crown's row just filled up).

At any point during your resolution step, you may **activate any charged card whose requirement is currently met** — or decline it. You choose the order. Each card can activate **at most once per turn**. Cards that were already sitting on the grid with their requirement met are *not* charged — they've already had their moment.

Activations are **always optional**. Skipping one is often the smartest play.

### The 9 signs

| Sign | Requirement (cell condition) | Ability | Mnemonic |
|---|---|---|---|
| ⚫ **Void** (1) | Has **no** orthogonally adjacent cards | *Only if you have fewer captured cards than someone else:* take the top card of the deck **face-down** into your score pile (worth 1 card) | The Void fills itself — emptiness draws substance when others have more |
| 🌱 **Root** (2) | On an edge cell (non-corner border) | Flip one card **orthogonally adjacent** to it | Roots grow at the border and turn what they touch |
| 🌊 **Wave** (3) | Shares its row **or** column with at least one empty cell | **Move** any one card on the grid to any empty cell | The Wave carries a card to an open shore |
| 🔥 **Flame** (4) | Has exactly **1 or 2** orthogonally adjacent cards | **Discard** one of those adjacent cards to the removed pile (out of the game) | Flame consumes what's beside it |
| 👁 **Eye** (5) | Has at least one empty orthogonally adjacent cell | **Peek** at the hidden side of any one adjacent card; you may then flip it | The Eye sees what's hidden nearby and may expose it |
| 🎭 **Mask** (6) | In the middle row **or** middle column (the central cross) | Flip **any** one card on the grid | The Mask at the crossroads can change any face in sight |
| 🗝 **Key** (7) | Has **2 or more** orthogonally adjacent cards | **Swap** any two cards on the grid | The Key unlocks positions — well-connected, it rearranges at will |
| ⭐ **Star** (8) | On a corner cell | **Draw the next card** from the deck and play it (full turn rules apply: place, resolve). *Star is also wild in alignments.* | A Star on the corner draws the next card from the sky. Star is wild. |
| 👑 **Crown** (9) | Its row **or** its column is fully occupied | Choose that full line: **flip the other two cards** in it | When the court is full, the Crown decrees — the other two must change face |

*Orthogonally adjacent = sharing an edge, not just a corner. Flipped/moved/swapped cards become charged and may chain. Discarded and captured cards do not.*

### Chains

Abilities charge other cards, which can activate, which charge others… Long chains are legal, fun, and self-limiting (once-per-turn cap guarantees they end). A worked example:

> The grid has a Crown in the middle-left whose row lacks one card. You place a **Root** on the bottom edge — its requirement (edge) is met. You activate Root: flip the card above it, which turns a Wave face into a **Mask**. The flipped card is now charged — it's in the central cross — so you activate **Mask**: flip the top-centre card from Eye to **Key**. That filled... nothing yet — but the Key now shows in the top row alongside another Key and a **Star**. *Three aligned (Star is wild): you capture all three.* The Crown's row will never fill now — its moment passed.

---

## Game end & scoring

When the deck is empty, finish the current turn, then score:

- **Most captured cards wins.** (Face-down Void cards count as 1 each.)
- **Tiebreaker 1:** most *distinct* face-up signs among your captures.
- **Tiebreaker 2:** whoever made the **first alignment capture** of the game.
- **Tiebreaker 3:** whoever is earliest in turn order.

---

## Edge cases & FAQ

**The deck is empty and a Star or Void activates.** Nothing happens — those abilities need a deck.

**Flame discards itself?** No — Flame discards an *adjacent* card, never itself.

**Can Key swap two cards that aren't adjacent to it?** Yes, any two cards anywhere on the grid.

**A card is captured before I activated it.** Its activation is lost. Capture removes cards instantly.

**An ability empties a cell next to a Void that's been sitting there.** If the Void's requirement goes from unmet to met, it becomes charged and may activate. If it was already met, nothing — no re-charging.

**Does placing a card that completes a line trigger that card's ability first?** No — alignments resolve the *instant* they exist. The captured cards are gone before anything can activate.

**Crown's row AND column are both full.** Choose one line to flip.

**Star's extra play completes a line — who captures?** You, the active player. Always.

**Star chains.** A Star drawn by a Star can activate too (it's a new card). The deck running dry ends the fun.

**Full-grid discard: can I discard a card mid-chain?** No — discarding only happens at the start of placement, when the grid is full.

**Do diagonals count for Mask/Crown requirements?** No. "Middle row or column" and "its row or column" mean ranks and files only. Diagonals matter *only* for alignments.

---

## Strategy notes (read after your first game)

- **Showing a sign feeds it.** Every face you place face-up is a face someone might align. The deck's top card is public — watch what your opponent is about to inherit.
- **Pairs are bait.** Two matching signs in a line is a gift to whoever moves next. Either finish lines on *your* turn or don't start them.
- **Stars are double-edged.** The wild face accelerates everyone's alignments, including yours.
- **Declining is a move.** Roughly three-quarters of skilled activations are *declined* in our testing. The board you leave matters more than the action you take.
- **Memory pays.** Cards in the grid have known hidden sides if you saw them placed. Eye formalises this, but attention is free.

---

## Card manifest (36 cards)

Each card lists its two faces. ⚫ Void · 🌱 Root · 🌊 Wave · 🔥 Flame · 👁 Eye · 🎭 Mask · 🗝 Key · ⭐ Star · 👑 Crown

| | | | |
|---|---|---|---|
| ⚫/🌱 | ⚫/🌊 | ⚫/🔥 | ⚫/👁 |
| ⚫/🎭 | ⚫/🗝 | ⚫/⭐ | ⚫/👑 |
| 🌱/🌊 | 🌱/🔥 | 🌱/👁 | 🌱/🎭 |
| 🌱/🗝 | 🌱/⭐ | 🌱/👑 | 🌊/🔥 |
| 🌊/👁 | 🌊/🎭 | 🌊/🗝 | 🌊/⭐ |
| 🌊/👑 | 🔥/👁 | 🔥/🎭 | 🔥/🗝 |
| 🔥/⭐ | 🔥/👑 | 👁/🎭 | 👁/🗝 |
| 👁/⭐ | 👁/👑 | 🎭/🗝 | 🎭/⭐ |
| 🎭/👑 | 🗝/⭐ | 🗝/👑 | ⭐/👑 |

---

## Designer's variants

- **Calm Signs** (first game / with kids): Star is *not* wild. Slower captures, gentler pace.
- **Deep Signs** (2P, more brutal): Key may only swap *itself* with another card. Slightly fewer captures, more positional.
- **Shared Glory:** skip tiebreakers 2–3; ties are shared wins.

*A sibling to TURNCOAT: same deck architecture, opposite soul.*

*Design v1.2 — rules balanced over ~23,000 simulated games. See the accompanying design analysis for the data.*
