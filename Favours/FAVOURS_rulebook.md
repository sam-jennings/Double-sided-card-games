---
record_type: game
game: FAVOURS
state: Ready to test
players:
  - 5
  - 6
  - 7
  - 8
  - 9
player_count: "5–9"
duration: ~10 min
genre: Party / simultaneous gift-giving
complexity: Light
min_players: 5
max_players: 9
min_minutes: 8
max_minutes: 12
physically_playtested: false
public_document: Favours/FAVOURS_rulebook.md
next_step: "Table it at 7P and check whether the giving is lobbied aloud or computed in silence."
catalog_order: 34
---
# FAVOURS

*A simultaneous gift-giving party game for 5–9 players · ~10 minutes · ages 8+*

Everyone at the table **is** one of the signs. Play with only the cards those signs make, and every card in the game names **exactly two people sitting at the table** — and every pair of people appears on **exactly one card**.

Each round you give one card to one of the two people printed on it. A favour that arrives on its own is welcomed and kept. Two favours arriving at once overwhelm their recipient, and every one of them is refused.

The whole game is one sentence long, the table state is always public, and you can hold an entirely unrelated conversation while playing it. That is the design target — see *Design intent*, below.

---

## Components

The **36-card** master deck: 9 signs, every possible pair of signs appearing on exactly one double-faced card.

FAVOURS uses only the **sub-deck your table generates**. With *p* players you use signs **1 up to *p*** and every card pairing two of them — `p × (p−1) ÷ 2` cards.

| Players | Signs in play | Cards | Remove | In play | Cards each | Rounds |
|---:|---|---:|---|---:|---:|---:|
| 5 | Moon–Eye | 10 | — | 10 | 2 | 2 |
| 6 | Moon–Mask | 15 | 3 (below) | 12 | 2 | 2 |
| 7 | Moon–Key | 21 | — | 21 | 3 | 3 |
| 8 | Moon–Star | 28 | 4 (below) | 24 | 3 | 3 |
| 9 | all nine | 36 | — | 36 | 4 | 4 |

You also need a small pool of **counters** — coins, beads, mints, anything, one bowl in the middle. (This is the collection's standard house kit; see *Variants* for a counter-free version.)

**Needs a table everyone can reach across.** Each player accumulates a face-up spread in front of them and gifts are placed directly in front of their recipient, so at 8–9 players you need a round table within arm's reach — or a nominated passer for the far side.

> Each card shows **one sign per face**. There is no card back: a card on the table always shows exactly one of its two signs. You may freely look at both faces of any card in your hand.

### The even-count removal — do not improvise this

At 6 and 8 players the sub-deck does not divide evenly. **Remove a perfect matching** — a set of cards that covers every sign in play exactly once — so that every player loses exactly one appearance:

- **6 players:** remove **Moon–Mask**, **Leaf–Eye**, **Wave–Flame**.
- **8 players:** remove **Moon–Star**, **Leaf–Key**, **Wave–Mask**, **Flame–Eye**.

Removing any other three or four cards leaves some players named on up to two more cards than others — a silent handicap decided by the shuffle. Simulation: arbitrary removal gives a sign-frequency spread of **2.06** at 6P and **2.31** at 8P; the matching above gives **0**.

---

## Core idea

Every card is a **link between two people**. Because the deck contains every pair exactly once, the map of who-can-give-to-whom is complete and perfectly symmetrical: you can reach every other player, on exactly one card each.

You are trying to place your cards where they will arrive **alone**. Everyone is trying to do the same thing, and nobody can see anyone else's hand — so a favour is a guess about where the rest of the table is *not* looking.

---

## Setup

1. **Sit in a circle and count off in sign order.** Starting anywhere and going clockwise, the first player is **Moon (1)**, the next **Leaf (2)**, then Wave, Flame, Eye, Mask, Key, Star, Crown — up to the number of players. *Your seat is your sign.* Nothing to remember and nothing to look up: to find who a card names, count round the table.
2. **Build the sub-deck** from the table above, and make the even-count removal if there is one. Set every unused card aside in the box.
3. **Shuffle by flipping random chunks** as you go, so which face lands up is randomised.
4. **Deal by passing.** Square the deck and pass it round the circle; each player takes their own cards straight off the top into their hand, without laying them down. (Nobody should see the faces of anyone else's cards.)

Say once, aloud, before the first game: *"Every card in this deck names two of us, and every pair of us is on exactly one card."* That sentence is the whole game.

---

## How to play

Every round, all at once:

1. **Choose one card** from your hand, keeping it hidden.
2. **On a count of three, give it.** Place it face-up in front of one of the **two people printed on it**, turned so that **their sign is the face showing**.
3. **Resolve every gift at once:**
   - A player who receives **exactly one** favour **accepts** it. They keep the card face-up in front of them. **The giver takes one counter from the bowl.**
   - A player who receives **two or more** favours is overwhelmed. **All of them are refused.** The givers take them back and lay them in a shared **refused row** — a face-up overlapping row in the middle of the table, out of the game.
4. Play the next round. The game ends when hands are empty.

**You may never give a favour to yourself.** If a card carries your own sign, it has only one legal recipient — that is a forced play, and it is the game's built-in fallback. There is always a legal move.

**Talk as much as you like.** Lobby, plead, warn people off your target, promise anything. Nothing said is binding.

> **Both piles read themselves.** Every favour in front of you shows *your* sign — after the first round your score pile is also your nameplate. The refused row shows which pairs are spent, and anyone may pick up and examine any card in either place, both sides, at any time — return it as found.

---

## Winning

At the end, your **score is the number of cards in front of you plus the number of counters you hold** — one point for every favour you received, and one for every favour you sent that arrived alone.

Highest score wins. **Ties are broken by the most cards actually received**; if that is still level, the win is shared.

---

## Why it belongs to this deck

Nothing else in the collection turns the deck's completeness into a *social* object. The all-pairs property stops being a fact about the cards and becomes the **seating plan**:

- **Every card names two real people**, so there is no such thing as an abstract play. Choosing a card is choosing which two people you are deciding between, and playing it is choosing one of them over the other, in public.
- **Every pair of people exists exactly once**, so the giving graph is complete and symmetric — no player is easier to reach than any other, and everyone holds precisely one card pointed at each other person. An ordinary deck has no second face and so cannot name a second person.
- **The hidden face is the person you passed over.** When you give someone a card, the face pressed to the table names the player you chose *not* to give it to — and they may turn it over and see. The snub is built into the component.
- **The sub-deck scales with the table.** The deck does not merely accommodate 5 to 9 players; it generates a different, correctly-sized, still-complete game for each count.

It also stays honest about the deck's physics. Nothing is ever placed face-down (there is no back to place it on), concealment lives only in a hand you are holding, and every card that touches the table is public from the moment it lands.

---

## Strategy notes

- **Landing beats denying.** You score as much for a favour that arrives as for one you receive, so crowding somebody else's gift costs you exactly the point it costs them. Spite is affordable, not free — that is the tension.
- **Nobody controls their own receiving.** Half your score arrives from other people. The half you control is where you send.
- **Read the refused row.** Cards there are gone, and because every pair appears once, a spent card is a route between two specific people that no longer exists.
- **Your own-sign cards are your most predictable ones** — they have a single legal recipient, so play them when that person looks quiet, not when they are already being courted.
- **Say who you are giving to.** It is not binding, and it is usually true, which is exactly why saying it works — and why it sometimes doesn't.
- **Being popular is a curse.** If three people announce they are giving to you, you would rather they didn't.

---

## Variants

**Two deals (recommended at 5–6 players).** With two cards each, a game is over in two rounds and roughly half of tables tie. Play two full deals back to back and total the scores.

**Silent FAVOURS.** No talking at all. Sharper, colder, and a genuinely different game — the guessing has nothing to work with but seating and the refused row.

**Snubs (counter-free).** Instead of counters: a refused card is returned to its giver, who keeps it **sideways** in front of them, and each one is **−1** at scoring. This prices spoiling identically and needs no components, but scores go negative — in simulation **37–56%** of players finish below zero, which reads as sour at a party. Use it if you have no counters, not by preference.

**Open hands.** Play with hands face-up on the table. It becomes a pure simultaneous-reasoning puzzle rather than a party game — useful for teaching the resolution once, then put the hands back up.

---

## Design intent, and what is being tested

The brief was an **ambient** game: a one-minute teach, high player counts, and playable while the table talks about something else. That was ranked deliberately above scoring well on the collection's usual depth rubric.

FAVOURS meets it structurally — one decision per round, all state public, no history to reconstruct, and a forced fallback so nobody can be stuck — but two things are known and unresolved:

- **Ties are common.** Under random play, 43% (9P) to 55% (6P) of games end level before the tiebreak. The tiebreak and the two-deal variant are the current answers; if they are not enough, the fix is a larger spread of point values, not more rounds.
- **The obvious heuristic loses.** Giving to whoever has received least is what *everyone* reasons toward, so it collides; in simulation it performs at **0.76–0.84×** random play. That is the correct signature for an anti-coordination game and is acceptable here, but it does mean skill is shallow and reads as luck to some players.

Simulation lives in [favours_sim.py](favours_sim.py) — it checks the spoiling price, the even-count removal, and the score distribution at every count. Design history, including the two bugs repaired before this rulebook was written, is [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §31.

**The falsification test.** One 7-player evening, three rounds. Does the table *lobby* — argue, warn, claim targets aloud — or does everyone silently work out the least-crowded recipient? If it plays in silence, the social premise is wrong and this is an anti-coordination puzzle wearing a party game's clothes.
