# Fable Prompt: 20 Table-Ready Games for the Flip Deck

*September 2026 · a breadth batch: many varied games, played at the table to find the hits. Paste everything under **Prompt** into a new conversation.*

## How to use

- **Run it in a plain chat with no project files attached.** The concept docs and project memory pull a model toward existing designs, and would make a model comparison unfair.
- **To compare models,** paste the same prompt into Opus 5 in a separate chat. Put all 40 games in one file without model names, shuffle them, and choose what to table before checking which model wrote which.
- **The output runs to about 10,000 words.** If a reply stops early, say "continue from game N".
- **Overlap with existing titles is allowed on purpose.** A new game may beat and replace an old one. Only names must stay distinct.

---

## Prompt

You are designing card games for a custom deck. I want **20 new games I can play at a table this week**, each written as about one page of complete rules. I will test them myself and keep the hits. Don't give me simulations, rubric scores or marketing copy. Give me playable rules, with enough variety that a few of them turn out to be special.

### The deck

- **36 double-faced cards and 9 signs.** Each sign has a fixed rank, printed as a pip on both faces of every card: Moon 1 · Leaf 2 · Wave 3 · Flame 4 · Eye 5 · Mask 6 · Key 7 · Star 8 · Crown 9.
- **Every card carries two different signs, one per face.** Every pair of signs appears on exactly one card. The deck is the complete graph K₉: signs are vertices, cards are edges. Each sign appears on exactly 8 cards.
- **The sign is the rank.** Crown is always 9 and Moon is always 1. There are no suits separate from ranks, and a card's two faces always have two different values.
- **Smaller decks are exact subsets.** Remove every card showing an 8 or 9 and the remaining 21 cards are the complete 7-sign deck. The 6-sign deck has 15 cards and the 8-sign deck 28. Trim from the top pips.
- **Nothing is printed except sign, name, colour, pip, and an orientation mark that is identical on both faces.** Signs have no printed abilities. A game may give them meaning (for example, "in this game Star is wild").
- **Useful structure, if you want it:**
  - 36 divides evenly by 2, 3, 4, 6 and 9.
  - The 36 cards can be split into 12 sign-triangles (such as Moon–Leaf–Wave) in 840 different ways.
  - The whole deck can be laid as one closed loop in which neighbouring cards share a sign.

### Physical facts that break normal card-game habits

1. **There is no card back.** A card on the table always shows one sign to everyone. "Face-down" does not exist; you can only choose which face shows.
2. **A player holding a card can see both faces.** Concealment that depends on players not looking at their own cards fails at the table.
3. **Taking a card off a squared stack shows its top face to everyone.** If a rule needs a card taken unseen, it must name one of these methods:
   - (a) **open deal**: the table glimpses one face of each dealt card, which is fine when that matters little;
   - (b) **self-deal**: each player takes their own cards off the stack straight into hand;
   - (c) **blind cut** below the table edge, for a single secret card;
   - (d) **blind draw** from inside the box base, the only method for repeated concealed draws.
4. **Shuffle by flipping random chunks**, so which face lands up is random.
5. **Hands can't be sorted.** Players re-scan both faces of every card each turn. A hand of 9 is comfortable, 12 is heavy and 14 is overwhelming. Keep starting hands at 9 or fewer unless the game truly needs more.
6. **These work well:**
   - open information;
   - public spreads anyone can pick up and inspect, both faces, returned as found;
   - cards laid in an overlapping row so the row records history;
   - simultaneous reveal from cupped palms;
   - claim-and-challenge, where a hidden face is checked by flipping;
   - rotation as state, for cards that are placed and left alone;
   - deliberate memory of hidden faces, when remembering is the point of the game.

**Components:** the deck, plus at most 12 identical counters and the box base as a blind-draw container. No paper, pencils, screens, boards, dice or per-game reference cards. Deck-only is best.

### What a hit looked like

Two games are proven at the table. Learn from why they work, but don't copy them.

**DOWRY (2 players): "I cut, you choose" with a second layer.**
- The cutter lays 3 cards from hand as a lot of 2 and a lot of 1, choosing which face of each card shows.
- The chooser takes either lot, and the cutter gets the other.
- Captured cards go into a public spread, and their owner picks each card's permanent scoring face.
- At the end, whoever shows more of a sign scores its pip; tied signs score nothing.

Everyone who played it asked to play again. A player who is hard to please borrowed the deck to play it with other people. What seems to matter:
- one player builds the other's dilemma;
- both players are deciding on every offer;
- there is almost nothing to look up;
- the path from decision to reveal is short;
- the two faces are what make the bluff possible.

**BLIGHT (3, 4 or 6 players): trick-taking where a captured card's penalty is its hidden pip.**
The harmless-looking card may cost you nine. A player read the rules unaided and called them clear. The standout moment: a player dealt six of the eight Crown cards couldn't follow suit, so he dumped them into tricks other players won. He finished with the lowest penalty and won.

### How games failed

At the table:
- **No decision on most turns.** WILDFIRE is a shedding race played to one pile. A card matched the pile only 2 times in 9, players averaged 1.1 legal plays a turn, and about 70% of turns had nothing to decide. Players said it felt reactive.
- **Looking things up.** TRIGON gave each sign an ability. Every player checked both faces' abilities every turn, and turns crawled.
- **Tedious scoring.** GLEAN summed pips into totals around 110.
- **Concealment nobody followed.** JANUS relied on players never looking at the outward face of cards in their own hand. The table ignored the rule, so the game was never played as designed.
- **Game state hidden under a card.** OUROBOROS kept the playable sign on the underside of the last card, so players kept lifting it to check. It also felt boring and luck-driven.

Caught on paper before the table:
- **Your choices don't change your score.** An early FAVOURS draft scored only the person receiving a gift, so giving badly on purpose cost the giver nothing.
- **Good play ends in a tie.** In an early RENDEZVOUS draft, the best co-operative play gave nearly everyone the same score.

### Variety within the batch

Overlap with existing games is fine. Variety *within these 20* is required.

- **No two of the 20 share the same core structure.** Spread them across structures such as:
  - division and choosing, auctions and bidding, trading, voting, drafting;
  - trick-taking, shedding, set collection and majorities, push-your-luck;
  - route or network building, spatial placement;
  - deduction, memory, bluffing and claims, negotiation, hidden roles;
  - real-time or dexterity, simultaneous action;
  - co-operative play and solo puzzles;
  - games played in one hand or without a table, and games spread over days.

  Invent structures that aren't on this list.
- **Player counts:** at least 4 games playable at 2, at least 4 that are best at 3–4, at least 3 for 5 or more players, and at least 2 playable solo.
- **Lengths:** from under 5 minutes to about 30 minutes.
- **Format:** at least 4 games that change the format itself: where cards are held, how turns work, who can see what, or when the game is played.
- **Use the two faces for different things across the batch:** a claim and its truth, two values, two allegiances, a public and a private side, a direction, a time, or something new.

### Process

1. Privately brainstorm at least 60 seeds across the structures above. Don't show them.
2. Choose 20, for variety and for how likely a table is to ask for a rematch.
3. Write each one in the format below.
4. Check each game against the checks below. If one fails and a single rule change can't fix it, replace it with another seed. Don't report failures or replacements.

### Checks

- **Card flow:** at every listed player count, deals, refills and the end condition work out exactly, and the game always ends.
- Every player's own choices change their own score.
- Most turns contain a real decision, and the right answer usually isn't obvious.
- Nobody waits more than about a minute with nothing to think about.
- Anything meant to be hidden is actually hidden, given physical facts 1–3.
- Nobody needs to look anything up during a turn.
- Scoring takes under two minutes and needs nothing harder than adding small numbers.
- An ordinary deck of playing cards could not run the same game.

### Format for each game (about 450 words)

**TITLE:** one or two words in capitals. It must not share a key word with any existing title: BLIGHT, TWELVE TRIALS, THE ORRERY, TRIGON, WILDFIRE, GLEAN, CROSSROADS, JANUS, OUROBOROS, CAIRN, TURNCOAT, FACE VALUE, DOWRY, ICARUS, CONCORD, BRAVADO, FAVOURS, FORKED TONGUE, THE COUNCIL, SLEEPER, WISP, RELAY, SNARE, STRATA, AUGURY, EDICT, VIGIL, GOLEM, LACUNA, PADDOCK, HINGE, MIRROR, COVENANT, CARAVAN, THE UNPLAYED PAIR, QUEUE, RENDEZVOUS.

- **One line:** what you do, and why it's tense.
- **Players · time · deck:** exact player counts, minutes, and which signs are used.
- **The moment:** what will happen at the table that players will talk about afterwards.
- **Components:** deck only, or which kit items.
- **Setup:** numbered steps, naming the deal method from physical fact 3.
- **Play:** numbered steps for a turn or round, complete enough to play without asking me anything.
- **End and scoring.**
- **Card flow:** the arithmetic at each player count, in one or two lines.
- **Why this deck:** one line on what the two faces or the unique pairs do here.
- **Biggest risk:** the likeliest way it falls flat, and the first thing to watch for at the table.

Start with an index table of all 20 games showing title, players, minutes, core structure and the moment. Then write the 20 games. No introduction and no closing summary.
