---
record_type: game
game: "AFTERIMAGE"
state: Untested
players: [2, 3, 4]
player_count: "2, 3, 4"
duration: "10–15 min"
genre: "Memory / concentration"
complexity: Light
min_players: 2
max_players: 4
min_minutes: 10
max_minutes: 15
physically_playtested: false
public_document: "Afterimage/AFTERIMAGE_rulebook.md"
next_step: "Run the first 2-player table test (AFTERIMAGE_playtest_plan_01.md): does recall beat guessing, and does counting feel fun or like homework?"
catalog_order: 37
---
# AFTERIMAGE

*Concentration on a deck with no backs · 2, 3 or 4 players · 10–15 min · Light · Untested · physically unplayed*

> **Status.** The playable rules are now [AFTERIMAGE_rulebook.md](AFTERIMAGE_rulebook.md) (design v0.1, November 2026), and the first-session plan is [AFTERIMAGE_playtest_plan_01.md](AFTERIMAGE_playtest_plan_01.md). This page remains the game record and the concept's reasoning. The sim is [afterimage_sim.py](afterimage_sim.py); the results are in [AFTERIMAGE_design_analysis.md](AFTERIMAGE_design_analysis.md).

## The idea

*An afterimage is what you still see after the thing itself has gone.* That is the whole game: every card on the table shows a sign, and the moment a card is flipped, the sign it showed vanishes underneath. Whoever still sees it in their mind's eye knows what that card hides now.

It is the family memory game Concentration, rebuilt for a deck that cannot lie face-down. In ordinary Concentration the memory task is "where was that picture?". Here nothing is ever hidden at the start: all 36 cards show a sign to everyone. You are hunting for two cards that **hide** the same sign, and the only way to know what a card hides is to remember what it showed before someone flipped it.

## Current shape

**Setup.** Wash-shuffle the deck: spread it, swirl it, and turn cards over at random so nobody knows which face is up. Lay all 36 cards flat in a grid (6 × 6 fits). Every card shows one sign to everyone.

**A guess.** On your turn, flip one card in place, revealing the sign it was pressing. Then flip a second card.

- **Match** — both newly revealed signs are the same: take both cards, score 1, and guess again.
- **Miss** — the turn passes. Both cards **stay flipped**. Nobody turns them back. Each one now presses the sign it showed a moment ago.

So after a miss the table looks normal again: every card still shows a sign. The information has moved underneath, and only memory holds it.

**Suggested (to test): turn flipped cards sideways.** After a miss, leave each flipped card rotated a quarter-turn. The table can then see at a glance which cards have been seen and which are still untouched, without seeing what they hide. This is orientation as state. It costs nothing to try and may make the game too easy or just clearer; the first table should play one game with it and one without.

**Ending: the Sweep.** The table almost never empties. Matches dry up with 2–8 cards left, each hiding a different sign. So, on your turn, instead of guessing, you may **sweep**: flip every remaining card.

- If no two show the same sign, the game ends and you score **1 point**.
- If any two match, flip them all back and your turn ends. Everyone has now seen every hidden face.
- With fewer than 2 cards left, sweeping is the only move.

The player with the most points wins. **Ties are not yet settled** (see open questions).

## How it uses the double-sided deck

- **The pressed face is the game.** The memory load is the vanished face of a flipped card: everyone saw it, so it is symmetric, and any claim can be checked by flipping. This is the deck-native memory game the steering flags as a gap ([physical-handling.md](../.kiro/steering/physical-handling.md), [design-principles.md](../.kiro/steering/design-principles.md)). An ordinary deck can't play it: with real card backs it collapses into plain Concentration, and the "what did it show?" layer disappears.
- **Every pair exists exactly once**, which gives two deductions:
  - A card showing Wave can't hide Wave, so after flipping a card that revealed Wave, never pick a Wave-showing card as your second flip.
  - Two cards showing the same sign never match each other: they are Wave–x and Wave–y with x ≠ y.
- **Each sign is on exactly 8 cards**, so the number of remaining cards hiding a sign is public: **8 − cards showing it on the table − faces with that sign on taken cards.** When every count is 0 or 1, no match remains, and a counting player knows the Sweep is safe before anyone else does.

The deck's structure is load-bearing twice over: double faces create the memory task, and the all-pairs registry turns memory into deduction late on.

## Physical-handling audit

| Question | Answer |
|---|---|
| **What can each player see?** | Every card's shown face, which is public. Taken cards in front of each player, with both faces inspectable. |
| **What can each player inspect freely?** | Their own taken pairs and the open grid. Nobody may lift a grid card to peek; the only way to see a pressed face is to flip it as part of a guess or sweep. |
| **What is supposed to be hidden, and is it?** | The pressed face of each grid card. It *is* hidden: it lies against the table. But it is not secret, because anyone who watched the flip saw it. That is the design. The memory load is deliberate and the same for everyone. |
| **Is any required state buried?** | No. The pressed faces are the challenge, not bookkeeping: nothing has to be consulted to *play* a turn, and a forgetful player can still legally flip any two cards. The suggested sideways marker shows which cards have been seen. |
| **Can the table verify legality without memory?** | Yes. A match is visible when both cards are face-up, and a sweep is checked by flipping everything. The only thing memory decides is *which* cards to choose, never whether a move was legal. |

No back is assumed anywhere: the grid is "every card shows a sign", not "face-down".

## Comparison with LODGE

[LODGE](../Lodge/LODGE_rulebook.md) is the collection's other hidden-face memory game, and they are different games:

- In **LODGE** the memory is *private and partial*. You know some of your own pressed faces from a peek, rivals know others, and Mask swaps move knowledge around. It is a swap-and-knock score-minimiser with powers and a knock decision.
- **AFTERIMAGE** is *public and symmetric*. Everyone sees every flip, there are no powers and no hands, and the whole game is the recall race plus late-game counting. It is lighter and quicker to teach (one rule plus the Sweep), and it is a family/filler game where LODGE is a small card game.

STRATA (concept) is a third memory design, but its memory serves bluffing. AFTERIMAGE is the only pure memory game.

## Simulation summary

From [AFTERIMAGE_design_analysis.md](AFTERIMAGE_design_analysis.md) (2,000 games per configuration, 96,000 games in total):

- The game always reaches its true end, even random v random (median 148 guesses). Perfect players take a median of 29 guesses. About 4 cards are left at the true end.
- Memory decides the winner. Perfect memory beats random 100% of the time. It beats a player who remembers only the last 10 / 6 / 4 flipped cards 72% / 93% / 99% of the time.
- No fixed card-count end works. Perfect bots finish with 0 / 2 / 4 / 6 / 8 cards left 1 / 24 / 48 / 24 / 2% of the time.
- **Sweep worth 1:** 0 stalls in 18,000 games, under 1.4 extra guesses on average after the true end, and seats close to fair (a small first-seat edge with weak memory). Counting beats memory-only 64% to 27%. The Sweep point changes the winner in 7% (2P) to 14% (4P) of games. Sweep worth 2 is too swingy (13–28%).

## Open questions

1. **Tiebreak.** *Provisionally settled in rulebook v0.1:* the successful sweeper wins a tie they are in; otherwise the tie is shared (0–6% shared wins in the sim). Reversible; "most recent pair wins ties" was near-identical.
2. **Sideways marking.** Does turning seen cards a quarter-turn help, or does it give away so much that the game becomes trivial? Play one game with it and one without.
3. **Does counting feel fun or like homework?** The sim says counting is worth ~2:1 over memory alone. At the table it may feel like the satisfying "I know it's safe" moment, or like arithmetic. That can only be answered at the table.
4. **Memory steepness.** Remembering 4 cards instead of 6 drops a bot from 7% to <1% of wins against perfect memory. If humans sit near "last 4–6", a strong rememberer may win every time. Is that a feature in a memory game, or does it need a handicap variant (e.g. a smaller grid on the 7-sign 21-card subset for younger players)?
5. **Opening luck.** The first guess is a blind match about 11% of the time, and a match lets you guess again. With weak memory the first seat also wins a few points more often (up to 49 v 42 in the sim). Is a lucky start noticeable at the table?
6. **Refusing to sweep.** A trailing player who knows the game is over can keep guessing (a deliberate miss) instead of sweeping. In the sim this happens ~0.3–0.8 times per game and never stalled it, because the leader sweeps next turn. Watch whether it feels like stalling at the table.

## Fastest falsification

One 2-player game with the full 36-card grid. If, after the first dozen guesses, neither player can recall what any flipped card showed (so play is effectively random and drags past ~60 guesses), or if one player reconstructs the whole table and wins without contest, the memory band is wrong for humans. Then try the 7-sign subset (21 cards) before cutting.

## Next step

Run the first 2-player table test with [AFTERIMAGE_playtest_plan_01.md](AFTERIMAGE_playtest_plan_01.md), against open questions 2–6.

### How the duration was estimated

The sim counts guesses, not minutes. Perfect bots take a median of 29 guesses. Bots that remember only the last 4–6 flipped cards (a plausible human range) take 34–40. A guess is two flips and a moment's thought, roughly 10–15 seconds at the table, so 34–40 guesses is about 6–10 minutes. Add 2–3 minutes to wash-shuffle and lay out 36 cards, and the estimate is **10–15 minutes**. Player count barely changes the guess count (29 at 2P, 3P and 4P), but more players means more thinking turns, so 4P likely sits at the top of the range. To be confirmed at the table.
