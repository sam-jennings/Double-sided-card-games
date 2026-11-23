# HINGE

*A pocket duel for 2 players · ~5–10 minutes a round · ages 8+*

> **Known issue:** The two-player game has never been played (only a solo test of the older QUEUE version), and the simulation found that two careful players block each other. Expect stalls; try a house rule and tell the designer.

> **⚠️ Draft v0.1 (November 2026). HINGE is listed as Rough edges.** Written from [HINGE_concept.md](HINGE_concept.md) using its recommended two-player turn order: strict alternation, no bonus move. A floor simulation ([hinge_sim.py](hinge_sim.py)) found that careful players can stall each other under that turn order. See the **Design notes** for the numbers and the decision that needs the designer.

*A hinge is where something folds. Cut the packet anywhere, fold the front over on that hinge, and every card you folded faces the other way. Line up three of a sign and they're yours.*

---

## Components

- The flip deck: **36 double-faced cards, 9 signs, every pair of signs on exactly one card, each sign on exactly 8 cards.** An index pip 1–9 is printed on both faces.
- **Use signs 1–6 only (Moon to Mask).** Remove every card showing Key, Star or Crown. That leaves 15 cards, with each sign on 5 of them.

## Setup

1. Shuffle the 15 cards, turning chunks over as you go so which face is up is random (there is no card back).
2. Make the **packet**: spread the 15 cards in one overlapping row on the table (or any surface: a book, a bag, a knee), so every card's upper face can be read. The left end is the **front**.
3. If the packet already shows three of a sign side by side, shuffle again.
4. Decide who moves first. The other player moves first in the next round.

Everything is public. Both players see every shown face. Anyone may lift a card to check its other face, as long as it goes back exactly as it was.

## Your turn — the hinge

1. **Choose a hinge:** any gap between two cards. The cards in front of it are your **block**: anything from the front card alone up to every card but the last one.
2. **Fold:** slide the block together into a squared stack, **turn the stack over as one**, and spread it back at the front of the row.

Turning a squared stack over does two things at once: the block's order reverses, and every card in it now shows its other face. The rest of the packet doesn't move.

> **Example.** The packet starts Moon · Wave · Leaf · Leaf · Flame · …, and the first two cards hide Leaf (under the Moon) and Eye (under the Wave). Hinge after the first card and fold: Leaf · Wave · Leaf · Leaf · … — no run. Hinge after the *second* card instead: the two-card block turns over, so it reverses *and* shows its other faces. The row now reads **Eye · Leaf · Leaf · Leaf** · Flame · … The three Leaves are a run. Claim them, and the packet closes up to Eye · Flame · …

## Claiming

After your fold, look for a **run**: three or more cards side by side showing the same sign. Take every run into your **pocket** (a face-up pile in front of you) and close the gap. If closing the gap makes a new run, take that too, and keep going until no run remains.

Then the packet passes to your opponent, whether or not you claimed. **There are no bonus moves.**

## End of a round

A round ends when:

- **fewer than three cards** remain in the packet, or
- **8 folds in a row** produce no claim (count them aloud: "one dry… two dry…"). *(Simulation-set default; see the Design notes.)*

The player with more cards in their pocket wins the round. Equal pockets: the round is drawn.

**A match** is three rounds, alternating who folds first. Most round wins takes the match. Still level, most pocketed cards across the match wins. Still level, it's shared.

## Edge cases & FAQ

**Can I fold the whole packet?** No. The last card always stays put. Folding everything would just turn the row around.

**Can I fold one card?** Yes. A one-card hinge simply flips the front card.

**Do I have to fold?** Yes, every turn.

**My fold made two runs.** Take both.

**A run is longer than three.** Take all of it.

**Does the dry count reset after any claim?** Yes, by either player.

## Strategy notes *(read after your first round)*

- **Read the hidden faces first.** Before a fold, check what the block will show after it turns. The packet is open information; lift and look.
- **Don't build for your opponent.** A two-card match with a fold-able third card nearby is a gift to whoever moves next.
- **Count the signs.** Each sign is on exactly five cards, and a card shows only one sign at a time. Once three of a sign's cards are in pockets, that sign can never make another run, because two cards can't make three.

## Designer's variants

- **Solo hinge.** Play alone: clear the packet in as few folds as you can. This is the version the concept's solo test confirmed.
- **Claim and go again.** After a claim, fold again. It's the concept's alternative turn order; see the Design notes for its numbers.

---

## Design notes *(not player-facing)*

### Where these rules come from

Everything above is in [HINGE_concept.md](HINGE_concept.md) except four points the concept left open, which this draft settles as defaults:

1. **The packet is a readable row**, not a squared packet in one hand. In a squared packet only the front and back faces show, so nobody could scan for runs. The concept's "no surface" premise survives as a fan or a row on any surface. *Designer check: is the fan or row how the solo test was actually played?*
2. **Cascading claims.** The concept says "claim all of them" without saying what happens when closing the gap makes a new run. This draft keeps claiming. The pilot showed cascading on vs off makes no measurable difference.
3. **The dry cap is 8.** The concept's "a set number of chordless moves" had no number (see below).
4. **A dealt run means reshuffle**, so the first player can't start with a free claim.

### Floor simulation (November 2026)

[hinge_sim.py](hinge_sim.py), `python -u hinge_sim.py --games 1000 --seed 1`: 1,000 rounds per row, hard cap 300 folds. Bots: **Random** (any hinge), **Greedy** (1-ply: most cards claimed now), **Skilled** (2-ply: claim minus the opponent's best reply). The focus seat rotates independently of the first player. Strict alternation (the concept's recommendation):

| Dry cap | Table | Folds | Cards claimed (of 15) | Ended by dry cap | Draws | First player wins (decided rounds) | Focus seat wins |
|---:|---|---:|---:|---:|---:|---:|---:|
| 6 | Skilled v Skilled | 6.5 | 1.6 | 100% | 64% | **100%** | — |
| 8 | Random v Random | 9.7 | 1.4 | 100% | 70% | 60% | — |
| 8 | Greedy v Greedy | 14.2 | 7.3 | 92% | 28% | 63% | — |
| 8 | Skilled v Skilled | 8.5 | 1.6 | 100% | 66% | **100%** | — |
| 8 | Greedy v Random | 13.8 | 5.7 | 95% | 26% | 53% | 92% |
| 8 | Skilled v Random | 12.8 | 4.6 | 97% | 30% | 52% | 97% |
| 8 | Skilled v Greedy | 12.3 | 5.0 | 97% | 33% | 68% | 83% |
| 10 | Skilled v Skilled | 10.5 | 1.7 | 100% | 65% | **100%** | — |
| none | Random v Random | 257 | 12.2 | — | 24% | 52% | — (78% hit the 300-fold cap) |
| none | Greedy v Greedy | 235 | 12.3 | — | 28% | 60% | — (76% hit the cap) |

**Claim-and-go-again** (the concept's alternative) barely changes anything. At a dry cap of 8, Skilled v Skilled claims 1.6 cards with 61% draws and 100% first-player wins; Greedy v Greedy claims 7.3 cards.

### What the numbers say

- **A dry cap is required.** Without one, even random play hits the 300-fold limit in ~78% of rounds: the last few cards can't form a run, and nothing else ends the round. With any cap there are no stalls, by construction.
- **Skill beats random by a wide margin:** 92–97% at every cap.
- **Careful play deadlocks.** When both players look one reply ahead, almost nothing is ever claimed: 1.6 of 15 cards, with 13.4 still in the packet when the dry cap ends the round. Two-thirds of rounds are drawn, and **every decided round goes to the first player**. Traced over 300 extra Skilled v Skilled rounds (seed 3), every claim happened on fold 1 (134 rounds), fold 2 (19) or fold 3 (4), and none ever came later. The first player takes whatever the opening position offers, then mutual denial freezes the packet. That's the *flatness* and *degenerate strategy* bug: the better both players get, the less happens.
- **A bonus move doesn't fix it,** because the denial lies in never leaving the opponent a one-fold claim, and that is unchanged.

The solo test's finding ("matches form reliably within a handful of moves") is consistent with this: solo, nobody is denying you. The two-player turn economy is the open problem, exactly as the concept warned.

### Decision for the designer (blocking; no rule changed here)

The fix is a design choice, not a tuning number. Directions the evidence points to, none adopted:

- **Reward setting up, not just finishing.** For example, score a pair you leave that the opponent fails to complete, or let a run claimed off your opponent's setup score less.
- **Force contact.** A fold must change at least one card that touches an existing pair, or the hinge must sit within a fixed distance of the front.
- **Make HINGE a solo or co-operative puzzle**, which the solo test supports, and drop the duel.

Re-run `hinge_sim.py` after any change. Targets: Skilled v Skilled claims most of the packet, draws under ~20%, and first-player wins near 50–60%.

*Design v0.1, draft. Floor-simulated (2P, 42,000 rounds); not yet played with two players.*
