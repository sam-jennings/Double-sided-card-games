# Flip Card Game Project Goals

## Project Purpose

The goal of this project is to design a flexible deck of double-sided cards that can support a collection of different games.

The project starts with the **deck structure** rather than with a single fixed game. Each card has one symbol on each side, and every possible pair of symbols appears exactly once in the deck. If the deck has `n` symbols, the total number of cards is:

```text
n choose 2 = n(n - 1) / 2
```

For example:

| Number of symbols | Deck size |
|---:|---:|
| 6 | 15 cards |
| 7 | 21 cards |
| 8 | 28 cards |
| 9 | 36 cards |

The exact number of symbols is not fixed yet. Choosing that number is one of the central design decisions of the project.

## Core Deck Concept

The deck is built around a simple but powerful mathematical structure:

- Every card connects exactly two symbols.
- Every pair of symbols appears once and only once.
- A card can always show either of its two symbols.
- There is no hidden face-down state: if a card is visible, one of its two symbols is visible.
- Flipping a card changes which of its two symbols is active.

This creates a deck where the relationships between symbols matter as much as the symbols themselves.

## Design Direction

The main design challenge is to discover what kinds of games work especially well with this deck structure.

The project should explore games that make meaningful use of properties such as:

- Symbol pairings
- Flipping between two possible states
- Complete pair coverage
- Grid placement
- Symbol adjacency
- Symbol majorities or shortages
- Player control over which side of a card is active
- Tension between immediate use and future flexibility

The aim is not just to make games that happen to use the deck, but to make games that feel as though they could only exist because of this deck.

## Symbol Count Decision

A major project goal is to determine the best number of symbols for the final deck.

This choice affects several important factors:

- Total deck size
- Rules complexity
- Player memory load
- Game length
- Tactical depth
- Number of possible game designs
- Suitability for microgames, fillers, and larger games
- Whether each symbol can reasonably have its own rule, action, role, or identity

The current likely range is **6 to 9 symbols**, giving deck sizes from **15 to 36 cards**.

The final symbol count should not be chosen abstractly. It should be chosen based on which size creates the best overall design space and supports the strongest collection of games.

> **✅ RESOLVED (June 2026): 9 symbols / 36 cards**, used as a **master deck**. Any 6/7/8-symbol subset of the 36-card deck is an exact smaller all-pairs deck, so games declare their symbol range instead of the project fixing a smaller size. Full analysis in [DECK_SIZE_DECISION.md](DECK_SIZE_DECISION.md).

## Game Collection Goal

The intended endpoint is not a single game, but a **collection of playable games** using the same deck.

Each game should explore the deck from a different angle. Some may be tactical grid games, some may be deduction games, some may be conflict-heavy competitive games, and others may be short microgames or abstract puzzles.

The collection should prove that the deck is a strong reusable system rather than a one-off component.

A successful game collection should include:

- Several distinct game designs
- Clear rules for each game
- Games that work at the chosen symbol count
- A range of player counts, ideally including 2-player and multiplayer options
- Different styles of play, not just minor variations of the same mechanism
- Games that make flipping, pairing, and symbol distribution feel central

## Evaluation Criteria

Game ideas should be judged by how well they answer the following questions:

1. **Does the game need this deck?**  
   The best games should rely on the paired-symbol structure, not treat the cards as generic symbols.

2. **Is flipping meaningful?**  
   Flipping should create interesting decisions, reversals, threats, or opportunities.

3. **Is the symbol count manageable?**  
   The game should not require players to remember too many unrelated effects or exceptions.

4. **Does the deck size fit the game length?**  
   A 15-card, 21-card, 28-card, or 36-card deck will create very different pacing.

5. **Does the game create interaction?**  
   Especially for competitive designs, players should be able to disrupt, block, race, trap, or outmaneuver each other.

6. **Does the game reveal new value in the deck?**  
   Each strong design should teach something about what the deck can do.

## Current Working Assumption

The symbol count is **fixed at 9** (36 cards) as of June 2026 — see [DECK_SIZE_DECISION.md](DECK_SIZE_DECISION.md). Games that play best smaller use a declared symbol subset (e.g. "symbols 1–7").

The project is now in the collection-building phase: developing, simulating, and playtesting games against the fixed deck. Current collection: TRIGON and TURNCOAT (complete, sim-tuned), eight further concepts in [NEW_GAME_CONCEPTS.md](NEW_GAME_CONCEPTS.md), of which JANUS, FALSE FACE, and OUROBOROS are being developed to full rulebooks.

## Final Project Endpoint

The project should eventually reach a point where:

1. The number of symbols is fixed.
2. The final deck size is fixed.
3. The symbol set has a clear identity.
4. A collection of games has been designed around the deck.
5. Each game has clear rules and has been checked against the chosen deck size.
6. The deck feels like a coherent game system rather than a prototype for one isolated idea.

In short:

> Design the best possible paired-symbol flip deck, then build a varied collection of games that make that deck worth owning.
