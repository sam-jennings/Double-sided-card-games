Give me some ideas for games that can be played with this deck. Each game should be playable on 6 to 9 symbols (deck size 15 - 36). Really vary the ideas but always making use of the properties of the deck. No additional cards or pieces

I’ll treat the deck as a complete graph: symbols are nodes, cards are edges. I’ll aim for mechanics that still work when the deck shrinks, rather than assuming a 3×3 grid or 36 cards.

Thought for 24s

A useful way to think about the deck: with n symbols, the cards are the edges of a complete graph. Every symbol appears on exactly n−1 cards, and every pair of symbols exists exactly once. Good games should exploit that rather than just treating the symbols as suits.

Here are varied game ideas that scale from 6 symbols / 15 cards up to 9 symbols / 36 cards, with no extra components.

1. Constellation Control

Type: Tactical tableau / area control
Players: 2–4
Core property: Each card connects exactly two symbols.

Deal players hands. On your turn, play a card into a shared layout, showing one of its two symbols. Cards of the same visible symbol form a “constellation.” You can later flip cards to move them into their other constellation.

At the end, each symbol scores for the player with the most cards showing that symbol. Ties cancel. Your score is the number of cards you won influence over.

The interesting bit is that every card is contested between two possible symbol-majorities. A card showing Fire might later flip to Moon, weakening Fire and strengthening Moon.

Why it scales:
With 6 symbols, it is tight and tactical. With 9, it becomes more strategic because there are more possible battlegrounds.

2. The Missing Link

Type: Deduction / memory / set collection
Players: 2–4
Core property: Every pair exists once, so knowing one pair rules it out everywhere else.

Lay several cards face-down in a grid or row. Players take turns looking at one side of one card, then either claiming a pair or passing.

To claim, you name the two symbols on a hidden card. If correct, you take it. If wrong, you must reveal one of your won cards and return it to the centre face-down.

The twist: when a card is partially known, players can infer its other side because each pair exists exactly once. If the Sun–Moon card has already been claimed, then a visible Sun card cannot have Moon on the back.

Why it scales:
At 15 cards it is a fast memory game. At 36 it becomes a stronger deduction game.

3. Chain Reaction Grid

Type: Tactical flipping / combo game
Players: 2–4
Core property: Flipping a card changes one symbol into its unique partner.

Create a shared grid. Size can scale:

6 symbols / 15 cards: 3×3 grid
7 symbols / 21 cards: 3×4 grid
8 symbols / 28 cards: 4×4 grid
9 symbols / 36 cards: 4×4 or 5×5 grid

On your turn, play a card into an empty space or flip an existing card. Whenever a row, column, or diagonal contains exactly two matching visible symbols, the player who caused it may flip one of those matching cards. If a line contains three matching symbols, the player captures one card from that line.

The appeal is that matches are unstable: flipping a card can create a match somewhere else, break an opponent’s setup, or trigger a chain.

Why it scales:
The grid size adjusts. The core interaction remains the same.

4. Forbidden Pairs

Type: Push-your-luck / hand management
Players: 2–5
Core property: Each pair appears exactly once, so danger cards are unique.

Deal each player a hand. A few cards are placed face-up in the centre as “forbidden symbols.” On your turn, play a card face-up to your personal row. You score one point per card in your row, but if your newly visible symbol matches a forbidden symbol, your whole row busts unless you can flip a previous card to remove the conflict.

Players can choose which side of a card to play, so the puzzle is about managing both immediate visible risk and future flip options.

A round ends when the deck runs out or all players pass. Passed players bank their row. Bust players score nothing for the round.

Why it scales:
Smaller decks make it sharper and faster. Larger decks allow longer rows and more push-your-luck.

5. Bridges

Type: Route-building / blocking
Players: 2
Core property: Cards are edges between symbols.

Players build separate paths using cards. A legal path is a sequence where each card must connect to the previous card through a shared symbol. For example:

Sun–Moon → Moon–Tree → Tree–Blade

Since each physical card only shows one side at a time, you orient each card so the connecting symbol is visible on the joined edge.

On your turn, either extend your path, start a branch, or play a card to block the opponent by placing it in a shared discard as a “collapsed bridge.” Once a pair is gone, nobody can use that connection.

Score for longest path, number of different symbols used, and closed loops.

Why it scales:
Complete graph structure gives lots of route options even with 6 symbols, but 8–9 symbols create richer path planning.

6. Triangle Hunt

Type: Fast set-making / tactical drafting
Players: 2–4
Core property: Any three symbols imply exactly three possible pair-cards.

Players draft cards trying to complete triangles: three cards connecting three symbols, e.g.

Sun–Moon
Moon–Tree
Sun–Tree

A completed triangle scores immediately. Bigger bonus if all three cards are currently showing different symbols; smaller bonus if two or more show the same symbol.

On your turn, take one face-up card from the market or blind draw. Then you may play completed triangles from your hand. After scoring a triangle, keep one card from it as a “foundation” and discard the others. Foundations can be reused in future triangles.

Why it scales:
With 6 symbols there are 20 possible triangles. With 9 symbols there are 84. The game naturally gets deeper with more symbols without changing rules.

7. One Symbol Too Many

Type: Shedding / tactical hand management
Players: 2–5
Core property: Every card belongs to exactly two possible symbol groups.

Deal out all cards. Start a central pile with one card visible. On your turn, play a card showing the same symbol as the pile, or flip a card from your hand and play it if the other side matches.

After playing, the symbol now showing becomes the new required symbol.

But there is a catch: you may not play a card if its hidden side matches the hidden side of the previous card. This creates a memory element if players have seen flips.

First player out wins. If stuck, draw/take from a penalty row or pass depending on desired harshness.

Why it scales:
Works as a light filler with 15 cards or a more chaotic shedding game with 36.

8. The Council Vote

Type: Negotiation / semi-political card play
Players: 3–5
Core property: Symbols act as factions, and every card links two factions.

Each round, reveal three symbols as “issues” by flipping three random cards and using their visible sides. Players then secretly choose one card from hand and reveal simultaneously.

A played card supports whichever of its two symbols is visible. After reveal, players may flip their own card, changing allegiance, but only in turn order. The symbol with most support wins the issue. Players who backed it keep their cards as points; others discard theirs.

The nasty bit: because every card is a two-faction card, every commitment is reversible, but only to one specific alternative.

Why it scales:
With fewer symbols, alliances are more predictable. With more symbols, table-talk and betrayal become stronger.

9. Collapse

Type: Abstract strategy / spatial elimination
Players: 2
Core property: Removing one card removes the only connection between two symbols.

Lay cards in a shared pattern, all face-up. Players alternate flipping cards. If a symbol appears too many times in the layout after your flip, that symbol “collapses”: remove all visible cards of that symbol from the game.

The threshold scales with symbol count:

6 symbols: collapse at 3
7 symbols: collapse at 3
8 symbols: collapse at 4
9 symbols: collapse at 4

You score removed cards showing your opponent’s last-flipped symbol, so you are trying to bait them into creating collapses that benefit you.

Why it scales:
The collapse threshold handles different deck sizes. The unique-pair structure prevents duplicate card effects.

10. Echoes

Type: Memory / tactical flipping
Players: 2–4
Core property: A visible symbol always hides one specific partner.

Lay all cards face-down in a loose grid. On your turn, flip one card. If its visible symbol matches any visible symbol already in the grid, you may flip one of those matching cards. If the new symbol revealed creates another match, continue.

You capture cards only when you create a chain of at least three flips. Otherwise, the cards stay visible.

This creates a shifting memory board where players need to remember not just “where symbols are,” but which symbols are on the reverse sides of visible cards.

Why it scales:
15 cards gives a quick memory puzzle. 36 cards gives a more chaotic chain-reaction game.

11. Dominion of Degrees

Type: Graph scoring / tableau building
Players: 2–4
Core property: Symbols have degrees based on how many owned cards touch them.

Players build personal networks. On your turn, draft one card and add it to your network. At the end, each symbol scores based on its degree in your network:

1 card touching symbol: 0 points
2 cards: 1 point
3 cards: 3 points
4+ cards: 6 points, but only if no other player has more of that symbol

You are not just collecting symbols; you are building a graph. A card contributes to two different symbol degrees, so each draft has dual value.

Optional harsher rule: if you collect all cards touching a symbol, it scores zero because it becomes “overloaded.” With 6 symbols, that means 5 cards; with 9, it means 8.

Why it scales:
The scoring depends on symbol degree, not fixed deck size.

12. The Unplayed Pair

Type: Trick-taking / deduction hybrid
Players: 3–4
Core property: Each pair is unique, so the missing card matters.

Deal most of the deck, leaving one card hidden as the “unplayed pair.” Players play tricks. The lead symbol is the visible symbol of the first card. Players must follow that visible symbol if they can, either by playing a card already showing it or flipping one from hand to show it.

Highest-ranking symbol wins, using a rotating rank order based on the previous trick’s winning hidden symbol.

At the end, players guess the hidden unplayed pair. Correct guesses score bonus points. During the round, you infer it from which follow options never appeared.

Why it scales:
With 15 cards it becomes a short deduction trick-taker. With 36 it becomes a fuller card-counting game.

13. Rivals

Type: Direct conflict / capture
Players: 2–4
Core property: Every card has exactly one rival side.

Each player has a row of visible cards. On your turn, play a card from hand to attack another visible card. You may attack if your played visible symbol matches the defender’s hidden symbol. The defender may choose to flip the attacked card; if flipping reveals a symbol matching your attacker’s hidden side, the attack rebounds and they capture your card instead.

This makes attacks partially knowable but risky. A card is never just “Sun”; it is “Sun with a specific possible reversal.”

Captured cards are points.

Why it scales:
The probability of a successful attack changes slightly with symbol count, but the tactical structure holds.

14. Market of Opposites

Type: Drafting / economy without tokens
Players: 2–4
Core property: Each symbol has exactly n−1 partners.

Create a market row of face-up cards. On your turn, take one card, then you must flip one remaining market card that shares its visible symbol or hidden symbol. If no such card exists, you take a penalty card face-down.

Sets score at end:

Pair of cards sharing a symbol: small score
Chain of 3+ cards where each connects to the next: medium score
Complete triangle: high score
Star around one symbol: high score but vulnerable to being blocked

Because every taken card alters what can be flipped in the market, drafting one pair changes the availability of related pairs.

Why it scales:
Market size can scale: use 4 visible cards for 6 symbols, 5 for 7, 6 for 8–9.

15. Final Flip

Type: Microgame / bluffing / prediction
Players: 2–4
Core property: Each card has one known alternative state.

Each player gets a small hand. A central row of cards is built over several turns. On your turn, either add a card to the row or flip one card already in the row.

Before the final round, each player secretly places one card face-down as their prediction. At the end, reveal predictions. You score for each visible symbol in the final row matching either side of your prediction card, but you lose points if both sides appear too often.

So you want to steer the board toward your card’s two symbols without making your intention obvious.

Why it scales:
Use fewer rounds with smaller decks, more rounds with larger decks.

Strongest directions

For your deck specifically, I think the richest design spaces are:

1. Flipping grid games
These best exploit the physical front/back nature of the cards. They make the deck feel unique rather than like a normal multi-suit deck.

2. Graph-building games
Triangles, paths, stars, degrees, and missing edges all naturally come from the “every pair exists once” property.

3. Deduction/memory games
Because every pair is unique, every revealed card gives information about what cannot be elsewhere.

I would be more cautious with designs where each symbol has its own unique ability. At 6 symbols that is manageable; at 9 it can become too much. The deck’s mathematical structure is already doing a lot of work, so some of the best games may not need symbol-specific powers at all.

A lot of your ideas talk about face-up and face-down cards - this concept doesn't exist, if you can see a card, you can always see one of its faces
Thought for 11s

Good catch. I was mixing in normal-card assumptions. For this deck, the cleaner model is:

Every card always shows exactly one symbol to the table.
The other symbol exists on the reverse side, but there is no “card back” and no true face-down state.

So the useful states are not face-up / face-down, but:

visible symbol
reverse symbol
flipped orientation
known card identity, if players have seen both sides or if it was in their hand
unknown card identity, only if drawn from a shuffled stack without inspecting both sides

That means some of the ideas still work, but need rephrasing. The best design spaces are probably these:

1. Visible/Reverse Tactics

Cards on the table show one symbol, but can be flipped to the other symbol.

This is probably the strongest mechanical identity of the deck.

Example game shape:

Players build a shared grid. On your turn, play a card showing either side, or flip an existing card. Symbols score based on rows, columns, clusters, or adjacency.

The tension is that every card has a fixed alternative. A Sun/Moon card is not just “a Sun that can become anything”; it can only ever become Moon.

This creates good tactical questions:

Do I play this as Sun now, knowing it may later become Moon?
Do I flip my own card to score, even if that gives my opponent a Moon setup?
Do I place a card because of its visible symbol or because of its reverse threat?

This avoids any hidden/back-card issue entirely.

2. Graph Shapes

Since the deck contains every pair exactly once, players can build structures:

Triangles: AB, BC, AC
Paths: AB, BC, CD, DE
Stars: AB, AC, AD, AE
Cycles: AB, BC, CD, DA
Cliques: all pairwise links among a group of symbols

A game could be built around drafting and playing cards into personal/tableau networks.

Example:

On your turn, take a card from a shared display and add it to your network. Score completed structures. The visible side determines temporary control or activation, but the card’s full identity determines graph structure.

This uses the deck’s mathematical property much more directly than symbol abilities.

3. “Only One Pair Exists” Deduction

This can work without face-down cards, but the deduction has to come from unseen cards, not face-down table cards.

For example, players have hands, a market, and maybe a small draw stack. Since each pair exists once, seeing Sun/Moon tells you nobody else can have that connection.

A game could involve guessing which connections remain in opponents’ hands or in the draw stack.

Example:

Players collect cards into visible sets. At the end of each round, players predict one pair still held by another player. Correct predictions score.

This works better if players are allowed to inspect both sides of cards in their own hand, while table cards show only one current orientation.

4. Orientation as Commitment

This is a cleaner alternative to “hidden side” mechanics.

When you play a card, you choose which symbol is active. The inactive symbol still matters, but only for certain effects.

Example:

Each round has a target symbol. Cards showing that symbol contribute power. Cards containing that symbol on the reverse side contribute flexibility, defense, or future scoring.

A Sun/Moon card played as Sun is currently loyal to Sun, but still has Moon potential. That creates commitment without hidden information.

5. Reversible Area Majority

This might be one of the cleanest games.

Each symbol is an area/faction. Played cards show one active faction. Players take turns adding or flipping cards. At scoring, each symbol is won by whoever has contributed most visible cards to it.

But because cards can flip, control is unstable. A card leaving Sun and becoming Moon changes two majorities at once.

This scales well:

6 symbols: tight, simple, aggressive
9 symbols: broader, more strategic, more room for delayed threats
6. Pair Exhaustion

Because each pair exists once, playing a card permanently uses that relationship.

A game could revolve around “closing roads” between symbols.

Example:

There are public objectives like “connect Sun to Crown through a chain.” Players play cards into a shared route network. Once Sun/Moon is used, no other Sun/Moon connection can appear. Players can flip cards to change which endpoint is active, but the underlying connection remains fixed.

This creates a strong sense that every card is a unique resource.

7. No-Hand Perfect Information Duel

For a very abstract game, lay all cards in a shared display, each showing one symbol. Players alternate flipping or claiming cards.

Possible rule:

On your turn, choose a visible symbol and flip one card showing it. If the newly visible symbol now appears in a connected cluster of 3+, you claim one card from that cluster.

No hidden info. No hands. Pure tactical state.

This might be especially good for smaller decks: 6 or 7 symbols, 15 or 21 cards.

8. Symbol Abilities, But Orientation-Based

If each symbol has an action, the action should probably trigger from the visible symbol only.

The reverse symbol can create counterplay because opponents know what the card can become.

Example:

On your turn, play a card or flip a card. Then activate the visible symbol:

Swap two adjacent cards
Flip another card
Move a card
Lock a card until your next turn
Copy an adjacent visible symbol
Score a line or cluster

This works because the deck naturally limits how often each symbol can appear: with n symbols, each symbol appears on exactly n−1 cards.

I’d still be careful here. With 9 symbols, 9 unique abilities is a lot unless the abilities are very simple and icon-driven.

9. Public Market Drafting

A shared market of visible cards works nicely because every market card has both an immediate visible value and a reverse value.

Example:

On your turn, take one card from the market. Before taking it, you may flip one market card. Then refill the market.

You score for graph patterns in your collection, but only the orientation of your cards determines which symbols are currently active for bonuses.

This gives players meaningful choices without hidden table states.

10. Flip-Combo Grid

This is probably closest to your original 3×3 idea.

Start with a grid of visible symbols. On your turn, place a card into the grid showing either side. If its visible symbol satisfies a requirement, activate its action.

Actions can cause flips, swaps, pushes, captures, or rotations. Newly revealed symbols can trigger further effects.

The key correction: the reverse side is not “unknown face-down information.” It is simply the card’s other state. The fun is in orientation changes, not reveals.

Revised design principle

Avoid these phrases/rules:

“face-down card”
“hidden card in the grid”
“reveal a card”
“turn a card face-up”
“memory-match hidden cards”

Use these instead:

“visible side”
“reverse side”
“flip the card”
“active symbol”
“inactive symbol”
“card identity”
“orientation”

The strongest games for this deck probably treat each card as a reversible edge: it connects two symbols permanently, but only one endpoint is active at a time. That is more distinctive than using it like a normal deck with unusual backs.

Reduce it to the best five distinct game ideas
Thought for a few seconds

Here are the five strongest and most distinct directions I’d keep developing. I’ve avoided anything that depends on face-down cards or extra components.

1. Flip Grid Duel

Core idea: Tactical shared grid where cards are constantly flipped, moved, and reoriented.

Players build a shared grid using cards that always show one active symbol. On your turn, you either place a card, flip a card, or use a visible symbol’s effect. Rows, columns, clusters, or adjacencies trigger scoring or actions.

This is probably the closest to your original idea.

Why it fits the deck:
Each card is a reversible pair. A card showing Sun can only ever become its specific reverse symbol, not any other symbol. So every placement has both an immediate effect and a known future threat.

Possible win condition:
Score points for completing lines, controlling symbols, or triggering three-of-a-kind formations.

Works best with:
2–4 players.

Scaling:
Use different grid sizes:

6 symbols / 15 cards: 3×3 grid
7 symbols / 21 cards: 3×4 grid
8 symbols / 28 cards: 4×4 grid
9 symbols / 36 cards: 4×4 or 5×5 grid

Why this is worth pursuing:
This is the most “physical” use of the deck. The front/back nature matters constantly.

2. Graph Builders

Core idea: Players collect cards to build mathematical structures: paths, triangles, stars, cycles, and complete networks.

Every card is a link between two symbols. Players draft cards and add them to their personal network. They score for shapes such as:

Path: AB, BC, CD
Triangle: AB, BC, AC
Star: AB, AC, AD, AE
Cycle: AB, BC, CD, DA
Clique: all pairs among a group of symbols

The visible side could matter for temporary bonuses, but the full pair identity determines the structure.

Why it fits the deck:
This uses the strongest mathematical property of the deck: every possible pair exists exactly once.

Possible win condition:
Score completed structures immediately, or score your network at the end.

Works best with:
2–4 players.

Scaling:
This naturally scales. With more symbols, the number of possible structures grows, but the rules do not need to change.

Why this is worth pursuing:
It could become a very elegant game with little rules overhead. This is the cleanest “complete graph as a deck” concept.

3. Reversible Area Control

Core idea: Each symbol is a faction/territory. Players fight for control by playing cards showing that symbol, but cards can later flip to another faction.

Players play cards into a shared area. The visible symbol determines which faction the card currently supports. At scoring moments, each symbol is awarded to the player with the most visible cards supporting it.

But every card has a second allegiance. A Crown/Blade card played as Crown can later flip to Blade, weakening Crown and strengthening Blade.

Why it fits the deck:
Each card shifts influence between exactly two symbols. Flipping a card changes two contests at once.

Possible win condition:
Win majorities across symbols, or score symbols based on how many cards currently support them.

Works best with:
2–4 players, probably best at 3.

Scaling:
With 6 symbols, the fights are tight and direct. With 9, there is more room for strategic diversification.

Why this is worth pursuing:
It gives the deck a strong competitive identity without needing symbol-specific powers. It is interactive, readable, and scalable.

4. Pair Exhaustion Route Game

Core idea: Every card is a unique route between two symbols. Once used, that connection is gone.

Players build routes, chains, or networks in a shared space. A legal play must connect to an existing symbol, extend a route, block a route, or complete an objective.

For example, if the table contains Sun–Moon, another player might extend from Moon using Moon–Tree. But there is only one Sun–Moon card, so that connection is now permanently claimed.

Why it fits the deck:
The uniqueness of each pair becomes the entire tension. You are not just playing a “Sun card”; you are spending the only connection between Sun and Moon.

Possible win condition:
Score for longest route, completed loops, connecting specific symbols, or cutting opponents off.

Works best with:
2 players, possibly 3.

Scaling:
Smaller decks create a tight abstract duel. Larger decks allow more elaborate route-building.

Why this is worth pursuing:
This is one of the most distinct uses of the deck. It would feel unlike a normal card game and more like a compact route-building board game.

5. Combo Market

Core idea: Draft from a shared market where every card has an active visible side and a possible reverse side.

Lay out a row of visible cards. On your turn, take one card. Before or after taking, you may flip one market card, changing what is available to the next player. Cards you collect score based on sets, chains, triangles, or active-symbol bonuses.

Example scoring:

Pair of cards sharing a symbol: small score
Three-card chain: medium score
Triangle: high score
Star around one symbol: high score
Diverse set using many symbols: bonus

Why it fits the deck:
Every card has dual value: its visible symbol affects the current draft, while its pair identity affects long-term scoring.

Possible win condition:
End-game scoring from collected structures.

Works best with:
2–4 players.

Scaling:
Adjust market size:

6 symbols: 4-card market
7 symbols: 5-card market
8–9 symbols: 6-card market

Why this is worth pursuing:
This is probably the most accessible design. It could become a simple, clever drafting game that introduces the deck system without too much board-state complexity.

My ranking

If I were choosing what to prototype first:

Flip Grid Duel — strongest use of physical flipping
Graph Builders — purest use of the mathematical deck structure
Reversible Area Control — best conflict-driven multiplayer idea
Combo Market — most accessible and easiest to teach
Pair Exhaustion Route Game — most abstract, but potentially very elegant

I’d probably avoid starting with heavy symbol-specific abilities. The deck’s reversible-pair structure is already interesting; adding 6–9 unique powers too early may bury the cleanest part of the design.