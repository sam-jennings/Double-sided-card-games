---
record_type: game
game: "PADDOCK"
state: In development
players: [3, 4, 5, 6]
player_count: "3, 4, 5, 6"
duration: "~15 min"
genre: "Betting race"
complexity: Light
min_players: 3
max_players: 6
min_minutes: 15
max_minutes: 15
physically_playtested: false
public_document: "Paddock/PADDOCK_concept.md"
next_step: "Develop a complete rulebook if this concept is selected."
catalog_order: 28
---
# PADDOCK — nine runners, countable odds

*3–6 players · ~15 min · betting race · full 36 · In development · physically unplayed*

> **Status & scope.** Wildcard batch, second flight (July 2026) — *originality first, rubric waived, unsimmed*. No rulebook, no sim, no rubric self-score; should not jump the [focus-priority.md](../.kiro/steering/focus-priority.md) queue on novelty alone. Portfolio index: [NEW_GAME_CONCEPTS.md](../NEW_GAME_CONCEPTS.md) §25.

**The trick that makes it exist.** The collection has no racing/betting game — the Camel Up seat at the table — and this deck is built for one: a race whose odds are **honestly countable but never certain**. Each sign is a runner; each sign lives on exactly 8 cards, so every runner's fuel tank is printed on the maths; but every spent card *hides* one face, so the public count is a bound, not an answer. Sharp bettors price the interval; everyone else reads the table. No board, no dice, no pool of plastic camels — the race track builds itself out of the cards that run it.

**Setup.** Deal each player a hand of 3 (4 at 3P); the rest is the **race deck**. Nine lanes, empty.

**The race.** Reveal the race deck one card at a time: the shown sign's runner advances — the card is placed into that lane, and the lane's length *is* the position (columns of cards, fully glanceable). The hidden faces that ride into lanes are never seen — the fuel each runner has *left* is public only as a range. First runner to 5 wins the race; if the deck empties first, the longest lane wins (tie: higher pip).

**Betting.** At any moment between reveals, on your turn cycle, place a hand card beside a lane, **pointed at your seat** (the orientation signature again), showing whichever face you choose. Your stake is the card's **hidden pip** — known to you, half-guessable by others (they see one face; pair-uniqueness bounds the other). Payout: stake × (5 − lane length when the bet was placed) — early conviction pays multiples, late certainty pays pennies. Bets on losing runners score zero and reveal anyway (the table learns who believed what).

**The texture.** Watching a rival stake an unseen pip on an empty lane is the game: were they holding a 9, or performing one? The bet row becomes a second bluffing surface laid over an honest arithmetic race.

**Handling audit.** All race state is lane lengths (visible); all bet state is placement + orientation + one shown face; stakes stay hidden in the only place this deck can hide anything — pressed to the table under a public alibi. Dials: hand size, win-post at 5, the multiplier curve.

**Fastest falsification.** One 4P session, three races: if nobody ever bets before a lane reaches 3 (the multiplier fails to buy courage), the odds interval is too readable and the hidden-stake layer isn't doing its job.
