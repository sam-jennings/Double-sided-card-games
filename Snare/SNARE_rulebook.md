# SNARE

*A duel of forbidden triangles for 2 players · ~10–15 minutes for a two-game match · ages 10+*

> **Draft v0.1 (November 2026) — not yet cleared for the table.** This is a reviewable draft written from [SNARE_concept.md](SNARE_concept.md), which stays the game record. Simulation found that the single game, as the concept wrote it, is a **forced win for the second claimer**, and that the concept's pie rule cannot fix it. The seat rule below is provisional. See [Decisions to review](#decisions-to-review) and [SNARE_design_analysis.md](SNARE_design_analysis.md).

Six houses, fifteen roads, and every pair of houses joined by exactly one road. You and your rival take turns claiming roads. Own all three roads around any three houses and you are **snared**. On six houses that can't be avoided — somebody is always snared, usually more than once. The skill is making sure it's mostly them.

---

## Components

- **The deck: 36 double-faced cards, 9 signs.** Every pair of two different signs appears on exactly one card, one sign per face, so each sign is on exactly 8 cards.
- SNARE uses **signs 1–6 only** (Moon, Leaf, Wave, Flame, Eye, Mask), plus six Key cards as house markers. Nothing else is needed.

| Role | Cards | How many |
|---|---|---:|
| **Roads** | every card whose two faces are both from 1–6 | 15 |
| **Houses** | the six Key cards that pair Key with 1–6 (🗝/🌙, 🗝/🍃, 🗝/🌊, 🗝/🔥, 🗝/👁, 🗝/🎭), Key face down | 6 |
| Out of the game | every card showing Star or Crown | 15 |

---

## Setup

1. **Sort the deck.** Take out the six house cards (Key paired with 1–6). Then take out the 15 roads (both faces 1–6). Put everything else back in the box.
2. **Lay the houses on a diagonal**, a hand-width apart, Key face down so the house's sign shows: Moon top-left, then Leaf, Wave, Flame, Eye, and Mask bottom-right. This diagonal is the edge of a staircase.
3. **Lay every road in its slot.** A road joining signs *low* and *high* (by pip) goes in **the low sign's row and the high sign's column**: to the right of its lower house and directly above its higher house. Either face may show; it makes no difference. Lay each road **at a slant** (about 45°) so it is clearly crooked. A slanted road is **open**.

```
          Moon   Leaf   Wave   Flame  Eye    Mask
 Moon    [HOUSE]  1-2    1-3    1-4    1-5    1-6
 Leaf           [HOUSE]  2-3    2-4    2-5    2-6
 Wave                  [HOUSE]  3-4    3-5    3-6
 Flame                        [HOUSE]  4-5    4-6
 Eye                                 [HOUSE]  5-6
 Mask                                       [HOUSE]
```

4. **Choose colours.** One player is **Upright**, the other is **Across**. Upright owns roads whose long edge runs up and down the columns; Across owns roads whose long edge runs along the rows. Sit across the staircase or side by side; the board reads the same from anywhere.
5. **Choose who claims first** for game one. The match is two games, and the other player claims first in game two (see [The match](#the-match)).

Fifteen roads, two players: the first claimer takes 8 roads and the second takes 7. The game always ends after exactly 15 claims.

---

## Your turn

1. **Claim one open road.** Turn it square in your direction: upright if you are Upright, across if you are Across. It is yours for the rest of the game. Claimed roads never move, turn, or flip again.
2. **Check for snares.** If the road you just claimed is the third side of a triangle you now own, you have been **snared**. Say so aloud; your rival should note which of you was snared first, because it breaks ties.

You must claim on every turn. There is no passing, even if every open road would snare you.

---

## Snares: how to see them

A **snare** is three houses whose three connecting roads all belong to the same player.

On the staircase, every triangle has the same shape: **three roads at three corners of a rectangle, with a house at the fourth corner.** Check by eye: if three of your roads plus one house make a rectangle, that is a snare. Every such rectangle on the board is a triangle, and every triangle is such a rectangle (there are exactly 20).

> **Example.** Moon–Wave–Eye. The three roads are 1-3 (Moon row, Wave column), 1-5 (Moon row, Eye column) and 3-5 (Wave row, Eye column). With the Wave house at the bottom-left, the four make a rectangle. If Across owns 1-3 and 1-5, then 3-5 is **poison** for Across: claiming it would snare them. Upright can claim it safely, which takes the danger away. So Upright usually leaves it alone and lets the board force Across onto it later.

---

## Game end & scoring

After the 15th road is claimed, each player counts their snares. Every triangle of three roads in your colour is one snare. A single road can complete more than one snare at once; each counts.

- **Fewer snares wins the game.**
- **Tie:** whoever was snared **first** loses.

On six houses at least two snares always appear between the two players, and neither of you can finish clean together, so a game cannot be drawn.

### The match

Play two games, swapping who claims first. **Fewer total snares across both games wins the match.**

- **Tie on total snares:** compare how long each of you lasted, when you were the first claimer, before your first snare. Count turns from the start of the game. The player who lasted longer wins. A player never snared in that game counts as lasting the whole game.
- **Still tied:** the match is drawn.

> *Provisional.* This match rule removes the seat advantage by construction, but in simulation two strong players draw every match. See Decisions to review, item 1.

---

## Edge cases & FAQ

**Every open road would snare me.** Claim one anyway. Pick the road that snares you least, or the one that leaves your rival the worst next turn.

**I claimed a road that snares me twice.** Two snares. Count each triangle.

**Can I claim a road that snares my rival?** No such road exists. A road can only snare whoever claims it. Claiming a road your rival would be snared by simply removes that danger from them.

**Does the face a road shows ever matter?** No. A road is the link between its two houses, whichever face is up. SNARE never flips a card.

**A road was knocked out of square.** Set it back. Slanted means open; square means owned, and which way it is squared says by whom.

**How do I double-check a snare?** Name the three houses, find the three roads (row of the lower sign, column of the higher), and check they all run the same way.

---

## Strategy notes (read after your first game)

- **Poison roads.** An open road is *your poison* when you already own the other two roads of one of its triangles. Count your poison roads and your rival's. Neither of you wants your own poison.
- **Don't take their poison.** Claiming your rival's poison road saves them a snare. Leave it; the board will force it on them later.
- **Fuses.** Claiming a road next to one of your own, with the third road still open, lights a fuse: that third road becomes your poison. Every fuse you light shrinks the set of roads you can safely take.
- **Dead triangles are safe.** A road whose triangles already contain one of each colour costs nothing. Spend early turns on them.
- **The endgame is counting.** When the safe roads run out, players eat poison in turn. With seven or eight roads left, count who runs out of safe claims first.
- **Seat matters.** The first claimer must take 8 roads to the second's 7, and in our testing that extra road is decisive between careful players. The match is how it evens out.

---

## Card manifest

🌙 Moon (1) · 🍃 Leaf (2) · 🌊 Wave (3) · 🔥 Flame (4) · 👁 Eye (5) · 🎭 Mask (6) · 🗝 Key (7)

**Roads (15):** 🌙/🍃 · 🌙/🌊 · 🌙/🔥 · 🌙/👁 · 🌙/🎭 · 🍃/🌊 · 🍃/🔥 · 🍃/👁 · 🍃/🎭 · 🌊/🔥 · 🌊/👁 · 🌊/🎭 · 🔥/👁 · 🔥/🎭 · 👁/🎭

**Houses (6):** 🗝/🌙 · 🗝/🍃 · 🗝/🌊 · 🗝/🔥 · 🗝/👁 · 🗝/🎭

---

## Designer's variants

- **The Pentagon (first game, and the ladder's first rung).** Play on signs 1–5: ten roads, five houses (leave out every card showing Mask, including the Mask house). Here a clean finish **is** possible: if neither of you is snared, the game is a draw, and a draw is a good result. Play a Pentagon, then a full game of SNARE, and feel the moment a sixth house makes escape impossible.
- **Sudden Snare (sharper).** The first player snared loses at once. This is the classic pencil game *Sim*, and it is a known win for the second player with perfect play, so play it only as a seat-swapped match.

---

## Decisions to review

The concept left these open, or the draft had to choose them. Each one is a designer call.

1. **Seat balance — blocking.** The single game is a forced win for the second claimer (exact solve), and a careful second claimer wins 100% of simulated skilled games, finishing 0 snares to 2. The concept's **pie rule on the opening claim is inert**: every first road is the same as every other once the signs are relabelled, so the pie choice cannot change anything. The draft uses a seat-swapped two-game match. That fixes beginner-level seat bias (the obvious-play bots split matches 42/42 with 16% drawn), but strong play draws every match. The alternative with evidence is **setting one road aside before play** (7 roads each): skilled seats then split about 50/50 (48.7–51.4% across two seeds) with real snares on both sides, but escape becomes possible, which removes the "someone must be snared" hook. Choose one, or a different repair.
2. **Win condition.** The concept offered sudden death (*Sim*) and the Goodman count, and leaned toward the count. The draft makes the count the base game and sudden death a variant.
3. **Tie rule.** Not in the concept. The draft breaks a tied count against whoever was snared first, which means a single game can never be drawn on six houses.
4. **Layout.** The concept said "lay the six symbols as a hex", but a hex of houses cannot show all 15 roads without cards crossing (the three long diagonals meet at the centre). The draft uses the **staircase**: houses on a diagonal, each road at its row and column, so every snare is a house-cornered rectangle. It needs about 60 × 60 cm. Needs a table check.
5. **Ownership marker.** The concept said "orient it toward your side". The draft uses **upright vs across** (no printed marker needed) and **slanted = open**. Alternative: keep open roads in a loose supply and place them on claiming, so an empty slot means open.
6. **House markers.** Not in the concept. The draft uses the six Key cards paired with signs 1–6, Key face down, so the game stays deck-only.
7. **The ladder.** The concept's best-of series starting at five signs. The draft keeps it as a first-session variant rather than the base match, because five-sign games between careful players are always drawn.
8. **The nine-sign pentagon game** (avoid a five-cycle using all 36 cards) is left out of this draft, as the concept recommends, until six signs prove fun.

---

*Design v0.1 draft — floor-checked over ~87,000 simulated games plus an exact solve of every variant. Not yet tabled.*
