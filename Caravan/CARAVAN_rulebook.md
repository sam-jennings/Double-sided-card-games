---
record_type: game
game: CARAVAN
state: Ready to test
players:
  - 2
  - 3
  - 4
player_count: 2, 3, 4
duration: ~15 min
genre: Simultaneous cut-and-choose
complexity: Medium
min_players: 2
max_players: 4
min_minutes: 12
max_minutes: 20
physically_playtested: false
public_document: Caravan/CARAVAN_rulebook.md
catalog_order: 35
next_step: Table it at 3P and settle the question the simulation cannot — does packing for one *named* neighbour actually change what you pack?
---
# CARAVAN

*for 2, 3 or 4 players · ~15 minutes · ages 10+*
*A sibling of [DOWRY](../Dowry/DOWRY_rulebook.md). Same dressed offer; nobody waits, and nobody chooses their customer.*

> **State: Ready to test.** Never played on a table. Floor-certified over ~4,200 simulated games at 2, 3 and 4 players — see [`CARAVAN_design_analysis.md`](CARAVAN_design_analysis.md). Designed from the sibling brief in [DOWRY_future_directions.md](../Dowry/DOWRY_future_directions.md), and deliberately **not** the market design that brief recommended; the analysis says why.

*The road runs one way this season. You load a chest for the trader ahead of you and take what the trader behind you loads for you — and neither of you can do a thing about the other. Next season the road turns back.*

DOWRY is one bargain at a time between two people. CARAVAN is **every bargain at once**: each round, every player packs a dressed offer for exactly one other player and is packed for by exactly one other. Everyone takes at the same moment. Nobody waits for a turn, and **you cannot choose whom you help** — only how much.

**Strapline:** *You don't choose your customer. Only what they see.*

## Components

- The flip deck: **36 double-faced cards, 9 signs, every pair of signs on exactly one card, each sign on exactly 8 cards.** An index pip 1–9 is printed on both faces.
- Nothing else.

> **The Nine Signs (say this aloud before the first game — rank matters):**
> *"There are 9 signs. Each sign has one fixed strength — Crown is always 9, Moon is always 1. Every card pairs two different signs, so it always has two different strengths, one per face."*

| Pip | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Sign | Moon | Leaf | Wave | Flame | Eye | Mask | Key | Star | Crown |

## Setup

1. **Shuffle by flipping random chunks** so that which face lands up is randomised — there is no card back.
2. **Self-deal 6 cards each** (hidden-commitment deal): pass the squared deck; each player takes their own 6 cards one at a time off the top, straight into hand. The face showing on the deck as each card is taken is seen by the whole table — that glimpse is legitimate information. Hold your hand privately; you may inspect both faces of your own cards freely.
3. Place the rest as the **stock**: a live, upright, squared stack. Its top face is public.
4. Each player claims table space for a **spread** — your captured cards, laid face-up in columns grouped by scoring sign, visible to everyone.
5. No first player, no turn order, no start token. Everything below happens at the same time.

## The road

Each round the road runs in one direction, and that direction tells every player who they are packing for. **You pack for exactly one player; exactly one player packs for you.**

| Players | Deal | Stock | Rounds | The road, round by round | Offers |
|---|---:|---:|---:|---|---:|
| **3** *(recommended)* | 6 each | 18 | 4 | left · right · left · right | 12 |
| **4** | 6 each | 12 | 3 | left · right · opposite | 12 |
| **2** | 6 each | 24 | 6 | across, every round | 12 |

*"Left"* means you pack for the player on your left. *"Opposite"* (4P only) means you pack for the player across the table, so round 3 is two simultaneous private duels.

Because the schedule is the same rotation for everybody, **every seat has an identical game** — there is no first-player advantage to trade away. At 3 players you pack twice for each neighbour; at 4 players you pack exactly once for each of the other three.

## A round

Everything in steps 1, 2 and 3 happens **simultaneously**. Nobody may act on what anyone else does in the same step.

1. **Pack.** Take **3 cards from your hand** and lay them flat in front of the player the road points to, in two lots: **one lot of 2 cards, one lot of 1 card**. For each card, you choose **which face is up**. Lay each card down flat and deliberately — only the chosen face may be shown. Do not touch any offer once every offer is down.
2. **Take.** Read the offer in front of you (no touching, no peeking underneath) and put a hand on the lot you want. When every player has a hand down, everyone takes at once. **The packer takes the lot left behind.** Lots may not be refused.
3. **Place.** Everyone adds their captured cards to their own spread at the same time, **openly choosing which face is up for each card**. Flipping here is public — the whole table sees both faces of every captured card as it is placed. **The face left up is the card's scoring face, permanently: spread cards are never re-flipped.** File each card under the column of its scoring sign.
4. **Refill.** Pass the stock round; each player takes 3 cards off the top, back up to a hand of 6, while the stock lasts. The top face of the stock is public before each draw — every glimpse belongs to everybody.

Then the road turns and the next round begins. The stock runs out after round 4 at two players, round 2 at three, and round 1 at four; from then on hands simply shrink 6 → 3 → 0. **Every game is exactly 12 offers and every card in the deck ends in a spread.**

## Game end & scoring

When all hands are empty, score each sign:

- For each of the 9 signs, whoever has **more cards showing that sign** in their spread wins the sign and scores its **pip value** (Moon 1 … Crown 9).
- A tied lead scores for **no one**.
- Highest total wins (45 points exist if nothing ties; expect roughly 30 of them to be awarded).

**Tiebreakers, in order:** (1) most signs won; (2) the winner of the Moon majority; (3) shared victory.

**Match play.** Seats are symmetric by construction and the simulation finds no seat edge, so a single game is a fair result. At **4 players** the game is only 3 rounds long — play **two deals and sum the scores** if you want a full session rather than a filler.

## What is actually hidden (read this — it is the whole game)

This deck has no card backs, so CARAVAN never pretends a card is unknown. Instead:

- **Your hand** is the only private zone. You know both faces of your 6 cards; everyone else knows only the stock-top faces they watched you draw — and what the registry implies.
- **An offered lot** shows one chosen face per card. The hidden face of each offered card is exactly one sign — and because **every pair exists exactly once**, the set of possible hidden faces shrinks as the game goes on.
- **Spreads are open registries:** anyone may pick up and examine any spread card, both sides, at any time — return it as found. Every capture publicly reveals both faces of the card forever.
- **Nothing needs enforcing.** Every player reads a *different* offer, so simultaneous taking cannot collide and no player learns anything useful from watching another's hand go down. If your table prefers, resolve the takes one at a time; nothing material changes. This is why CARAVAN needs no written commitments and no components beyond the deck.

## Edge cases & FAQ

**Q. May I look at the other offers, not just mine?**
Yes, and you should. Every offer is public the moment it is laid. You only *decide* about your own, but what your rivals are being handed is the whole reason to care.

**Q. May the taker pick up or tilt offered cards to see the hidden face?**
No. Offered cards are read from the shown faces only. Deduce; don't peek.

**Q. May I split 3/0, or offer more or fewer than 3 cards?**
No. Every offer is exactly 3 cards, in lots of exactly 2 and 1.

**Q. Two of us put a hand on a lot at different times — does first touch matter?**
No. Hands go down together on a count of three, and everyone takes after all hands are down. Nobody may move a hand once it is placed.

**Q. May I re-flip a card already in a spread?**
Never. The scoring face is locked at placement. (You may *examine* spread cards freely — return them exactly as found, same face up.)

**Q. I forgot which face someone drew from the stock. Can I ask?**
No — that memory is part of the game. Everything else (spreads, offer legality) is verifiable on demand.

**Q. The last round comes from a 3-card hand.**
Yes — the whole hand is offered, and only the split and the dressing are left to decide. By then most of the deck is accounted for and the last offers are close to pure calculation. That is intended.

**Q. What if a sign ends level between two players and a third has fewer?**
Tied at the top scores nobody, whoever else is behind. Only 8 cards carry each sign, so at three players a **4th** shown instance is usually decisive and a **5th** is mathematically safe.

## Strategy notes *(read after your first game)*

- **You are not packing for the table; you are packing for one person.** A Crown you would never hand the Crown leader is nearly free to hand the player who has already lost that sign. The road decides which of those two you are dealing with this round — so plan a round ahead: *next round I pack for the leader, so I must dump my dangerous cards now.*
- **You cannot hit back.** The player squeezing you is not the player you pack for — until the road turns. Retaliation is a *schedule*, not an option.
- **Two cards beat one, until they don't.** Quantity is a real advantage in a majority game, and simulated play takes the pair about three times in five — a lean, not a rule. A pair of cards worth nothing to you is the cheapest thing a packer can hand you, and the fourth instance of a sign you already lead beats two cards of signs you have lost.
- **Count to five.** Each sign is on exactly 8 cards, and not all 8 will show it. A 4th shown instance is often worth more than a bigger pip.
- **Dress your keeps, disclose your gifts.** You score the lot the taker leaves. A lot you want to keep should look worse than it is; a lot you want taken can afford honesty — but a predictable packer is a poor one.
- **Everything is public except six cards per player.** Late in the game the registry closes and lies get expensive. Tell them early.

## Designer's variants

- **Open Caravan** *(first game / lighter)*: takers may examine both faces of the offer in front of them before choosing. Removes the bluff and teaches the flow, the placement choice and majority counting in one deal.
- **The trailing road** *(untested — the fix to try if the road feels flat)*: instead of the fixed schedule, at the start of each round the player with the fewest cards in their spread (ties: fewest signs currently led) names the direction for that round — left or right at 3P, left, right or opposite at 4P. The choice belongs to the weakest player, so it cannot become kingmaking, and it makes *whom you are packing for* a live question every round rather than a timetable. **Try this only if the base game's road reads as bookkeeping**; it is the single most likely repair, and the simulation could not settle whether it is needed.
- **Two deals** *(4 players)*: play two full deals and sum. Three rounds is a filler; six is a game.

## Follow-up playtest questions

1. **Does packing for a *named* neighbour change what you pack?** This is the design's whole premise and the fastest way to falsify it. The simulation says a bot that ignores who receives the lot does just as well (0.90–1.01×). If the table also cannot feel it, the road is decoration and *The trailing road* is the next thing to try. **Log one offer per round: who you packed for, and whether their spread changed your choice.**
2. **Does simultaneous play feel social, or like four solitaires?** Nobody waits, which is the design's main practical gain over a 4-player DOWRY — but the cost may be that nobody watches anybody.
3. **Is not being able to retaliate frustrating or interesting?** The player hurting you is never the player you pack for.
4. **Can four people read four offers without the round slowing to a crawl?** You only *need* to read your own.
5. **Is three rounds at 4P a game or a fragment?**

---

*Design v0.1 — September 2026. Floor-certified over ~4,200 simulated games ([`CARAVAN_design_analysis.md`](CARAVAN_design_analysis.md)): always terminates in exactly 12 offers with all 36 cards placed, 0 flow failures at 2, 3 and 4 players; seats fair at every count (no DOWRY-style second-cutter edge); take-decisions live 36–40% of the time against DOWRY's 32%; a thoughtful line beats a naive-but-sensible one on matched information by 1.22–1.29×. The road ablation is flat and is question 1 above.*
