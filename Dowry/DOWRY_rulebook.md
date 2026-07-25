---
record_type: game
game: DOWRY
state: Proven
players:
  - 2
  - 3
  - 4
player_count: 2, 3, 4
duration: ~20 min
genre: Cut-and-choose bluff
complexity: Medium
min_players: 2
max_players: 4
min_minutes: 20
max_minutes: 20
physically_playtested: true
public_document: Dowry/DOWRY_rulebook.md
next_step: Confirm the strong 2-player result with another match; 3–4-player modes remain untested.
catalog_order: 13
---
# DOWRY

*for 2 players · ~20 minutes · ages 10+*
*(3–4 player variant in Designer's Variants — untested)*

> **State: Proven.** The 2-player base game worked extremely well in its first physical playtest—possibly the collection's strongest game so far. See [`DOWRY_playtest_01.md`](DOWRY_playtest_01.md); simulation results are in [`DOWRY_design_analysis.md`](DOWRY_design_analysis.md).

*The match is agreed and the chests are being packed. Whoever packs them decides what the visitors see — silk laid on top, stones beneath. You will pack chests, and you will pick from chests packed against you. Every card in this deck has two faces; in DOWRY, the face you are shown is a claim, not a promise.*

DOWRY is an **"I cut, you choose"** game: one player splits goods into two lots, the other picks first. On this deck the cut has a second layer — the cutter also chooses **which face of every offered card shows**. The lot that looks poor may be the rich one.

## Components

- The flip deck: **36 double-faced cards, 9 signs, every pair of signs on exactly one card, each sign on exactly 8 cards.** An index pip 1–9 is printed on both faces.
- Nothing else. Score is counted from the card spreads themselves.

> **The Nine Signs (say this aloud before the first game — rank matters):**
> *"There are 9 signs. Each sign has one fixed strength — Crown is always 9, Moon is always 1. Every card pairs two different signs, so it always has two different strengths, one per face."*

| Pip | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Sign | Moon | Leaf | Wave | Flame | Eye | Mask | Key | Star | Crown |

## Setup

1. **Shuffle by flipping random chunks** so that which face lands up is randomised — there is no card back.
2. **Self-deal 9 cards each** (hidden-commitment deal): pass the squared deck; each player takes their own 9 cards one at a time off the top, straight into hand. The face showing on the deck as each card is taken is seen by the whole table — that glimpse is legitimate information. Hold your hand privately; you may inspect both faces of your own cards freely.
3. Place the remaining 18 cards as the **stock**: a live, upright, squared stack. Its top face is public.
4. Each player claims table space for a **spread** — your captured cards, laid face-up in columns grouped by scoring sign, visible to everyone.
5. The player who most recently divided anything fairly cuts first.

## How a turn works

Players alternate taking the **cutter** role; the other player is the **chooser**. A turn is one **offer**:

1. **Cut.** The cutter takes any **3 cards from their hand** and lays them flat on the table in two lots: **one lot of 2 cards, one lot of 1 card**. For each card, the cutter chooses **which face is up**. Lay each card down flat and deliberately — only the chosen face may be shown.
2. **Choose.** The chooser examines the shown faces (no touching, no peeking underneath) and **takes either lot**. The cutter takes the other lot. Lots may not be refused.
3. **Place.** Each player adds their lot's cards to their own spread, one at a time, **openly choosing which face is up for each card**. Flipping here is public — everyone sees both faces of every captured card as it is placed. **The face left up is the card's scoring face, permanently: spread cards are never re-flipped.** File each card under the column of its scoring sign.
4. **Refill.** The cutter draws from the stock back up to 9 cards (while the stock lasts). The top face of the stock is public before each draw — attentive players note what their opponent just picked up.

Roles then swap. The game is exactly **12 offers — 6 cuts each**. The stock runs out after offer 6; offers 7–12 are cut from shrinking hands (9 → 6 → 3 → 0). Every card in the deck ends in a spread.

## Game end & scoring

When both hands are empty (after offer 12), score each sign:

- For each of the 9 signs, whoever has **more cards showing that sign** in their spread wins the sign and scores its **pip value** (Moon 1 … Crown 9).
- A tied sign scores for **no one**.
- Highest total wins (45 points are available if no sign ties).

**Tiebreakers, in order:** (1) most signs won; (2) the winner of the Moon majority; (3) shared victory.

**Match play.** Simulation shows a mild edge (~56/44) for the player who cuts second. For anything competitive, play an even number of games, alternating who cuts first, and sum scores.

## What is actually hidden (read this — it is the whole game)

This deck has no card backs, so DOWRY never pretends a card is unknown. Instead:

- **Your hand** is the only private zone. You know both faces of your 9 cards; your opponent knows only the stock-top faces they saw you draw — and what the registry implies.
- **An offered lot** shows one chosen face per card. The hidden face of each offered card is exactly one sign — and because **every pair exists exactly once**, the set of possible hidden faces shrinks as the game goes on.
- **Spreads are open registries:** anyone may pick up and examine any spread card, both sides, at any time — return it as found. Every capture publicly reveals both faces of the card forever. By the late game most of the deck is accounted for, and a cutter can no longer dress a lie the chooser cannot audit.

The table can always verify legality without memory: offers are always 3 cards in lots of 2 and 1, every placement flip happens in the open, and the spreads re-read the whole capture history on demand.

## Edge cases & FAQ

**Q. May the chooser pick up or tilt offered cards to see the hidden face?**
No. Offered cards are read from the shown faces only. Deduce; don't peek.

**Q. May the cutter split 3/0 or offer more than 3 cards?**
No. Every offer is exactly 3 cards, in lots of exactly 2 and 1.

**Q. May I re-flip a card already in a spread?**
Never. The scoring face is locked at placement. (You may *examine* spread cards freely — return them exactly as found, same face up.)

**Q. I forgot which face my opponent drew from the stock. Can I ask?**
No — that memory is part of the game. Everything else (spreads, offer legality) is verifiable on demand; the stock glimpse is the one thing worth remembering.

**Q. Does the unseen face of a spread card count for anything?**
No. Only scoring faces count for majorities. The hidden face's only job was to be a threat or a disappointment.

**Q. The cutter's last cut (offer 11 or 12) comes from a 3-card hand.**
Yes — the whole hand is offered. By then both faces of nearly everything are deducible; the endgame cut is pure calculation. That is intended.

**Q. What if a sign ends 4–4 (all 8 of its cards showing it)?**
Tied; no one scores it. Note only 8 cards carry each sign — showing a 5th instance of a sign makes that majority mathematically safe.

## Strategy notes *(read after your first game)*

- **Price the dressing.** A cutter who always shows a lot's best faces is telling the truth; one who always hides value teaches you to grab the ugly lot. The registry decides who can still afford to lie.
- **Count to five.** Each sign is on exactly 8 cards, and not all 8 will show it. Five shown instances is an unassailable majority; a 4th instance is often worth more than a bigger pip.
- **Crown is loud.** Everyone fights for pips 7–9. Quietly winning Leaf, Wave and Flame (2+3+4 = 9) matches a Crown for less contest.
- **The refill is a broadcast.** The face you drew on is public. Sometimes the right play is taking a card whose *public* face is the one you wanted — nothing is revealed at all.
- **Dress your keeps, disclose your gifts.** You score the lot the chooser leaves. A lot you want to keep should look worse than it is; a lot you want taken can afford honesty — but a predictable cutter is a poor one.

## Designer's variants

- **Open Dowry** *(first game / lighter)*: the chooser may examine both faces of offered cards before choosing. Removes the bluff, teaches the flow, the placement decision, and majority counting.
- **Trousseau** *(harder / meaner)*: at setup, before dealing, each player receives one secret card by **Blind Cut** (take the deck below the table edge, cut, slide the new top card off unseen). Its two signs score **double their pip** for you. Play with hands of 8 (deal 8 each; stock 19; the 12th offer is short — cut 2 as lots of 1 and 1). Reveal secret cards at scoring; they join no spread. *Untested; deal arithmetic to be confirmed at the table.*
- **Three or four packers** *(3–4P, untested)*: the cutter lays **one lot per player** (3P: 4 cards as 2/1/1 · 4P: 5 cards as 2/1/1/1). Choosers pick in clockwise order from the cutter's left; the cutter takes the last lot. Adjust deal so all 36 cards flow out evenly; majority scoring unchanged. Expect more kingmaking pressure — test before trusting.

## Follow-up playtest questions

1. ~~Does even-splitting dominate?~~ **Answered by sim (floor):** a deceptive cutter beats an honest even-splitter ~83% of games, ~1.6× on score. The table question is now: *can humans execute and read the dressing game* — or does it only exist for perfect-memory players?
2. Is the mid-game deduction load fun or fatiguing at the 9-card hand size?
3. Does the pip ladder (Crown 9 … Moon 1) create enough asymmetric valuation, or is a goal-card mechanism (Trousseau) needed in the base game?
4. Is the stock-glimpse memory rewarding for the players who invest in it?

---

*Design v0.2 — July 2026. Proven in its first physical 2-player playtest; see [`DOWRY_playtest_01.md`](DOWRY_playtest_01.md). Floor certified over ~4,750 simulated games ([`DOWRY_design_analysis.md`](DOWRY_design_analysis.md)): always terminates in exactly 12 offers, 0 stalls; skilled play beats random ~3.6× on score; deceptive cutting beats honest even-splitting ~1.6× (the dressing layer is load-bearing); mild second-cutter seat edge ~56/44 (see Match play).*
