# DEADLOCK

*A territory duel for 2 players · a match of two games, about 20 minutes (one game about 10) · ages 10+*

> **v1.0 (23 November 2026), formerly titled VIGIL.** First played on 23 November 2026, in one sitting: very positive from both players, about 10 minutes a game. This version makes the one-sitting game the main format, makes a two-game match with seats swapped the default, and gives two seat rules for a single game. Playing one move at a time on a shelf, over days, is now a variant, and nobody has tried it yet. See [DEADLOCK_playtest_01.md](DEADLOCK_playtest_01.md) and [DEADLOCK_design_analysis.md](DEADLOCK_design_analysis.md). [DEADLOCK_concept.md](DEADLOCK_concept.md) is the game record.

Deal the whole deck out as a square field. Take turns claiming one card at a time by turning it to face you, and fight for the twelve lines across the field. Four cards of a line win it. But three each is a **deadlock**: the line is dead and scores for nobody, and one well-placed claim is all it takes to lock your rival's best line dead.

---

## Components

- **The deck: 36 double-faced cards, 9 signs.** Every pair of two different signs appears on exactly one card, one sign per face, so each sign is on exactly 8 cards. DEADLOCK uses all 36.
- Nothing else. A pencil helps to note the first game's score in a match.
- **Space:** about **60 × 60 cm** of table.

Each card's **top edge** is the one with the index in its corner. Both faces mark the same top edge, so flipping a card never changes which way it points.

---

## Setup

1. **Shuffle**, flipping random chunks as you go so the face showing on each card is random. (The face an open card shows does not matter much: whoever claims it may flip it.)
2. **Deal a 6 × 6 field**, six rows of six. Space the cards about a card's *length* apart in both directions, so any card can be turned a quarter turn without touching its neighbours.
3. **Turn every card sideways**, top edge pointing to the same side of the field — the side nobody sits on. Call it **East**. A sideways card is **open**.
4. **Choose seats.** One player is **North**, the other **South**, on opposite sides of the field. **North moves first.**

Thirty-six cards, two players: each of you makes exactly 18 claims, and the game ends after the 36th.

---

## Your move

1. **Choose any open card.** If you like, **flip it** where it lies so its other sign shows.
2. **Turn it upright, top edge pointing at your seat.** It is now **claimed** by you.

Claimed cards never move, turn or flip again. That is the whole move. Then it is your rival's move.

**Reading the field.** Sideways = open. Upright = claimed. From your seat, your cards read the right way up (index top-left) and your rival's read upside down (index bottom-right).

**Lost track of whose move it is?** Count the open cards. **Even: North's move. Odd: South's move.**

---

## Game end & scoring

When the last card is claimed, score the **twelve lines**: the six rows and the six columns. Every card is in one row and one column.

1. **Who wins a line.** The player who claimed **4 or more** of its 6 cards wins it. A line split **3–3** is **deadlocked** and scores for nobody.
2. **What a won line is worth.** Look at the sign showing on each of its six cards — **all six, whoever claimed them**. The line is worth **the largest number of cards showing the same sign**. Six different signs = 1 point; two Leaves and four others = 2; three Moons = 3; and so on, up to 6.
3. **Add up your lines.** That is your score for the game.

> **Example.** The top row, left to right: South Moon, North Moon, North Leaf, North Moon, South Wave, North Eye. North claimed four of six, so North wins the row. Signs showing: three Moons, one Leaf, one Wave, one Eye. The row is worth **3** to North. If South had flipped the first card to show its other sign instead of Moon, the row would have been worth only 2.

---

## Winning: the match

Moving first is a real advantage: between careful players, North wins about 7 games in 10. So the standard way to play is a **match of two games**.

1. Play a game and note both scores.
2. **Swap seats.** Whoever was South is now North and moves first. Reshuffle and deal a new field.
3. Play the second game. **Add each player's scores from both games. Highest total wins the match.**

**Ties:** whoever's own claimed cards showed more **Crowns**, counted across both games, wins. Still tied: the match is a draw.

Each of you has moved first once, so the match is fair by construction: in 500 simulated matches between careful players, the two players won 45% and 53%, within noise of even.

### Playing a single game

When you only have time for one game, use one of these seat rules. Agree which before you start.

| Rule | How it works | First player wins (careful play) | Notes |
|---|---|---|---|
| **South's point** (closest to even) | South adds **1 point** to their score. Ties go to Crowns (below). | about 38–47% | Close to even for strong players, slightly favours South for others. About a third of games end level on points, so Crowns often decide. |
| **South's ties** (lighter) | No bonus, but **South wins any tie on points.** | about 55–65% | No Crown tiebreak needed. North keeps an edge, which grows with skill. |

For comparison, with no rule at all the first player wins about 69–78% of careful games.

**Ties under South's point:** whoever's own claimed cards show more **Crowns** wins. Still tied: a draw.

---

## Edge cases & FAQ

**Can I flip a card I have already claimed?** No. Claimed cards are locked.

**Can I flip a card and then not claim it?** No. Flipping is part of a claim, and you claim the card you flipped.

**Do my rival's cards count toward the value of a line I won?** Yes. All six cards count. That is why the rival's choice of face matters to your lines and yours matters to theirs.

**Can a line be worth 0?** No. A won line is always worth at least 1. Only a deadlocked (3–3) line scores nothing.

**Does the face an open card shows matter?** Only as a default. You may always flip a card before you claim it.

**In a match, does the second game use the same field?** No. Reshuffle and deal a fresh one.

---

## Strategy notes (read after your first game)

- **Every line is a race to four.** Three cards each deadlocks the line. If your rival has three cards in a line, one more of yours there kills it, and that move is always available. So build majorities quietly and in more places than you need.
- **Each card is in two lines.** The best claims push a row *and* a column you can still win, or deadlock two of the rival's at once.
- **Values are small.** Most won lines are worth 2 or 3; a 4 is rare. A flip that turns your 2 into a 3, or their 3 into a 2, is often worth as much as a line.
- **Every card offers two signs.** Before you claim, look at both faces against *both* of the card's lines.
- **Crowns break ties, and ties are common.** Close games often come down to Crowns. When the face doesn't matter to either line, show the Crown.
- **North has the tempo.** Between careful players the first mover is ahead in most races. South should dispute lines early, not wait.
- **The last ten claims still matter.** About half the lines are usually still open with ten cards left. Count them.

---

## Card manifest

🌙 Moon (1) · 🍃 Leaf (2) · 🌊 Wave (3) · 🔥 Flame (4) · 👁 Eye (5) · 🎭 Mask (6) · 🗝 Key (7) · ⭐ Star (8) · 👑 Crown (9)

All 36 cards are used:

| | | | |
|---|---|---|---|
| 🌙/🍃 · 🌙/🌊 · 🌙/🔥 · 🌙/👁 | 🌙/🎭 · 🌙/🗝 · 🌙/⭐ · 🌙/👑 | 🍃/🌊 · 🍃/🔥 · 🍃/👁 · 🍃/🎭 | 🍃/🗝 · 🍃/⭐ · 🍃/👑 · 🌊/🔥 |
| 🌊/👁 · 🌊/🎭 · 🌊/🗝 · 🌊/⭐ | 🌊/👑 · 🔥/👁 · 🔥/🎭 · 🔥/🗝 | 🔥/⭐ · 🔥/👑 · 👁/🎭 · 👁/🗝 | 👁/⭐ · 👁/👑 · 🎭/🗝 · 🎭/⭐ |
| 🎭/👑 · 🗝/⭐ · 🗝/👑 · ⭐/👑 | | | |

---

## Designer's variants

### The Shelf (untested)

The game's original idea: leave a field on a shelf or windowsill for days, and make one move each time you pass it and it is your move. Nothing needs remembering, because the field shows everything. Use a single-game seat rule (or play the two games of a match one after the other), and a tray or board under the field so it can be lifted to clean.

**Whose move is it?**

- **Quick check:** count the **open** cards. **Even: North's move. Odd: South's move.**
- **Full check, when in doubt:** count North's cards and South's cards. **Equal: North's move. North one ahead: South's move.** Any other result means the field has been disturbed.

You can only move when it is your move. If it is not, walk on by. If you both walk past at once, the field still decides.

**Repairs.** A field left out for days gets bumped. Because nothing on it is hidden, most accidents are easy to see and undo.

- **A card is crooked.** Square it back the way it was nearly pointing: sideways stays open, upright stays with whoever it points at.
- **The turn check fails.** Something was turned. If you both agree what happened, set it right. If not, the player who is *behind* in claimed cards makes the next move.
- **A card left the field.** Put it back in its gap. If you both agree how it lay, restore it. If you don't, restore its orientation from the gap's neighbours and the turn check; for the face, see the optional photo below.
- **The field was scattered.** Unless you have a photo, start a new field.

**Optional insurance:** after each move, take a photo of the field. It is the only record that can settle which face a fallen card showed.

The first table game suggested that DEADLOCK's decisions are quick enough to suit one sitting better than a week on a shelf, so treat this as an experiment.

### Watchtower (more lines)

Also score the two long diagonals (14 lines). In simulation it *widens* North's edge, so use it only in a match or with a seat rule.

---

## Decisions to review

Each one is a designer call. Item 1 was settled for v1.0.

1. **Seat balance — settled (v1.0).** Default: a two-game match, seats swapped. Single-game options: South's point, or South wins ties. A match's Crown tiebreak counts Crowns across both games (a draft choice). Measured in simulation (North / South wins, careful play):
   - No rule: North 69–72% with the one-ply bots, 78% with a two-ply bot.
   - South +1 point: North 37–40% (one-ply), **47% / 48%** (two-ply); a third of games tie on points and go to Crowns.
   - South wins ties (+½): North 55–58% (one-ply), 65% (two-ply).
   - Two-game match, seats swapped: 500 simulated matches split 45 / 53 (±4.4, fair by construction); 24% of matches tie on points.
   - Untested: a pie (swap) rule after North's first claim; South claiming two cards on their first move.
   - The first table game (no rule) ended 13–11 to North.
2. **Crowns decide many games.** The Crown tiebreak settles 22–25% of careful games (about a third with South's point), because scores are small whole numbers. Keep it as a deliberate second axis (it rewards showing Crowns), or change the scoring so ties are rarer.
3. **Line values are narrow.** In careful play 50% of won lines are worth 2, 45% worth 3 and 3% worth 4. Flipping still matters (a bot that may never flip loses 76% to one that may), but most of the score is line count.
4. **What "pointing East" means physically.** Open = sideways, top edge to the unseated side; claimed = upright, top edge at the owner. Cards are spaced a card-length apart, so the field is about 60 × 60 cm.
5. **North vs South at a glance.** The two claimed orientations differ only by a half turn; the rules rely on the index corner (top-left vs bottom-right from your seat).
6. **South's lines include North's cards' faces** (and vice versa). The concept implies it; the rules make it explicit.
7. **The Watchtower diagonals.** The sim says the last ten claims still matter without them (about 5.7 of 12 lines still open, and the leader with ten left wins only 67–70% of careful games), so diagonals stay a variant.
8. **The Shelf variant's repair rules** (the disputed-turn rule, the optional photo) are untested guesses.

---

*Design v1.0 — floor-checked over 18,000 simulated games (seed 1) plus 500 simulated matches. First tabled 23 November 2026 (one sitting). Formerly titled VIGIL.*
