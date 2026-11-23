# SLEEPER — design analysis

*State: **In the workshop** · physically unplayed. The v0.1a rulebook was vetted and floor-simulated in November 2026 (see Simulation results). Two design-level problems need the designer before it is worth tabling.*

## Design intent

SLEEPER fills the collection's clearest genre hole: there is no **hidden-loyalty / social-deduction** game. THE COUNCIL is open negotiation (no persistent secret, cards go public on commit); FORKED TONGUE and FACE VALUE are claim-and-challenge bluffing about a *card's* hidden face. None of them asks the table's defining social-deduction question — *who is secretly on whose side?* — and sustains it across a whole game.

The game it exploits the deck for:

- **The loyalty card is one guarded double-faced card.** Your cover face shows; your Master face is pressed to the table. This is the *only* persistent secret a backless deck can hold cleanly — a single flat card hides exactly its down face, and nothing else (it is the lesson JANUS learned the hard way: you cannot conceal a hidden hand on this deck, but you can conceal one pressed card).
- **A card is an edge; a flip is an exact, public, one-alternative swing.** Turning a coat moves a decree from the sign it shows to the *single* sign printed on its back — your treachery's destination is public the instant the card lands. This is the deck's reversible-commitment property (shared with THE COUNCIL's "defect to one specific alternative," used here for board control rather than personal scoring).
- **The Court row is a self-recording public registry.** Every push and betrayal stays legible, so the deduction ("who keeps steering toward Crown?") runs on visible history, not memory.
- **Emergent teams via shared secret master.** Because most signs sit on 8 cards, several players can secretly serve the same sign and win together — the table's real alliances are invisible until the reckoning.

## Key constraints

- **Concealment must survive a backless deck.** Each player holds exactly **one** secret card, laid flat, Master-face down. No hidden hands anywhere (everything else — the Court row, the spent pile, the deck's revealed top — is public). This is deliberately the narrowest possible concealment surface.
- **Guaranteed termination.** Every turn spends exactly one Court-deck card (placed as a Decree or discarded to pay for a flip), so the game always ends in `36 − P − 3` turns. There is no flip-war non-termination risk — turning a coat *costs* a drawn card.
- **No moderator, no night phase.** Self-administered; the only secret action is the private master-choice at setup.
- **No new components.** Deck only (plus an optional generic first-player token, already sanctioned by THE COUNCIL).

## Simulation / solver results

### Setup (November 2026)

[sleeper_sim.py](sleeper_sim.py), `python sleeper_sim.py --games 2000 --seed 1`: 2,000 games per row, 4/5/6P × random / skilled / mixed tables = 18,000 games. The game ends when the Court deck empties, so it can't stall (structural, confirmed). Talk and Unmasking are **not** modelled. **RandomBot:** random Master, random action and face. **SkilledBot:** picks the Master that is stronger in the opening row (higher pip breaks ties), then each turn takes the decree or coat-turn that best makes its Master rule *now*. It ignores everyone else's loyalty, so it's a floor. In the mixed table, one skilled seat rotates independently of the first player.

The sim also measures what the **public registry** reveals. Every Court card is shown on both faces when revealed, so by the reckoning the only cards nobody has seen are the loyalty cards. A player's Master must be a sign *X* such that the card {cover, *X*} hasn't been seen.

### Findings

| P | Table | No winner | Shared win | Focus (skilled) seat wins | Crown or Star rules | Public Master candidates at 25 / 50 / 75 / 100% of the deck | Masters pinned to one sign at the end | Win rate by seat from the first player |
|---:|---|---:|---:|---:|---:|---|---:|---|
| 4 | random | 70.8% | 3.2% | — | 33.3% | 5.81 / 4.40 / 3.02 / 1.41 | 63% | 9 · 7 · 9 · 8% |
| 4 | skilled | 5.7% | 40.2% | — | 50.0% | 5.98 / 4.54 / 3.09 / 1.42 | 62% | **60** · 20 · 28 · 32% |
| 4 | mixed | 29.2% | 13.3% | 62.2% | 38.5% | 5.86 / 4.44 / 3.02 / 1.40 | 64% | 25 · 19 · 20 · 21% |
| 5 | random | 64.8% | 5.1% | — | 34.9% | 5.79 / 4.40 / 3.00 / 1.60 | 50% | 7 · 8 · 8 · 9 · 8% |
| 5 | skilled | 6.0% | 48.4% | — | 53.3% | 5.98 / 4.53 / 3.07 / 1.61 | 49% | 26 · 32 · **56** · 19 · 22% |
| 5 | mixed | 32.8% | 16.8% | 53.5% | 39.1% | 5.85 / 4.43 / 3.03 / 1.62 | 49% | 18 · 18 · 19 · 16 · 15% |
| 6 | random | 57.4% | 7.3% | — | 34.7% | 6.02 / 4.60 / 3.20 / 1.80 | 39% | 9 · 8 · 8 · 9 · 8 · 10% |
| 6 | skilled | 5.0% | 56.5% | — | 51.6% | 6.19 / 4.76 / 3.30 / 1.84 | 37% | 25 · 30 · **55** · 18 · 18 · 20% |
| 6 | mixed | 35.5% | 18.1% | 43.2% | 37.6% | 6.01 / 4.62 / 3.21 / 1.80 | 39% | 15 · 16 · 17 · 11 · 12 · 14% |

1. **Termination:** structural, 0 stalls.
2. **Skill gap: healthy.** One skilled seat wins 62 / 54 / 43% at 4 / 5 / 6P against random seats' ~8–9% base rate, and that's before any talk.
3. **The last mover decides the game (design-level).** In skilled tables the bold seat wins 55–60%, against ~18–32% for everyone else. That seat is always the one taking **the final turn**: 29 Court cards at 4P end on seat 1; 28 at 5P and 27 at 6P end on seat 3. With no reply possible, the final decree or coat-turn sets the ruling sign. This confirms, with numbers, the analysis's recorded *kingmaking at the reckoning* worry. The Steward rotation doesn't help, because the deck length fixes who moves last.
4. **The registry largely solves the secret (design-level).** The public candidate set for a Master shrinks from ~6 signs at the first quarter to **1.4–1.8 at the reckoning**, and **37–64% of Masters are pinned to exactly one sign by arithmetic alone** (more at 4P, where fewer loyalty cards remain unseen). The rulebook never mentions this. It may be the deduction payoff the design wants (the *strengthening lever* this analysis proposed), or it may turn the endgame into open information and the social read into counting. Either way, players will find it, so the rules and strategy notes must take a position.
5. **High signs pull.** Crown or Star rules in 50–53% of skilled games (33–35% random), because the pip tiebreak attracts Masters. Combined with shared victories in 40–57% of skilled games, it supports the recorded *obvious-sign collusion* worry, but without talk the sim can't show whether a table converges on it.

### Vetting notes (physical-handling checklist)

- **Concealment:** one flat card, Master pressed down, dealt by Blind Cut. Sound by construction; whether it leaks at a table stays a table hypothesis.
- **Visible state:** the Court row and the sideways spent pile record everything. Every decree's alternative is public because every reveal shows both faces.
- **Ambiguity:** *"The game ends when the Court deck is empty. Finish the go-around in progress"* can't be followed, because every turn begins by revealing a Court card and none are left. The sim ends on the last card. Any fix for finding 3 should replace this sentence anyway.

### Verdict

**Not promoted; stays In the workshop.** Two design-level decisions are needed first:
1. **The last-turn decision.** The analysis already lists candidates: a simultaneous final round, or a hidden-commit final turn. Another option is a deck length that ends each game on a rotating seat. Every candidate is a new mechanic.
2. **What the registry should reveal.** Embrace it (teach counting in the strategy notes, perhaps make it the Wager's engine), or blunt it (for example, set a few Court cards aside unseen at setup so the unseen pool is larger than the loyalty cards). Blunting changes the deck count and the clock, and needs a re-sim.

Re-run `sleeper_sim.py` after either change. Targets: last-seat edge within ~10 points of the others, and the pinned share at whatever level the designer intends.

The candidates are now simulated, but none is chosen yet: [SLEEPER_fix_options_sim_note.md](SLEEPER_fix_options_sim_note.md) (`sleeper_sim.py --fixes`). Of the candidates, only the simultaneous final round meets the last-seat target, and setting k cards aside lowers the pinned share from 62/49/37% to 22/16/12% at k = 4.

## Rubric evaluation

1. **Exploits all-pairs deck?** **Moderate–high.** The flip's "one specific alternative" swing exists because a card is a unique edge {A,B}. The deduction surface (who steers what) leans more on visible behaviour than on pair-uniqueness itself — an honest caveat, and the main thing to validate. *Strengthening lever if it falls short: lean harder on the registry — e.g. track which {A,B} edges remain unseen to bound who can still swing a given sign.*
2. **Physically works with double-faced cards?** **Yes, by construction.** One guarded flat card per player; all other state public and re-examinable. No hidden hand, no face-down stack, no buried state.
3. **Information visible or deducible?** **Yes.** The Court row and spent pile are a complete public history; the only hidden datum is each player's locked master, which is the legitimate thing to deduce.
4. **Flipping matters?** **Yes — it is the core verb.** Choosing a decree's face, and turning a coat to swing it, is the whole tactical layer; Unmasking is a one-shot flip of your own loyalty as a social weapon.
5. **Pair uniqueness matters?** **Partial.** It fixes each decree's single defection target (load-bearing for the flip) and guarantees the spent/row history is unambiguous. It does *not* yet drive the core deduction the way it does in FORKED TONGUE — flagged as the design's softest rubric answer.
6. **Distinct experience?** **Yes.** vs THE COUNCIL: persistent locked secret + emergent hidden teams + a single end reckoning, not per-round public issue-majorities for personal pips. vs FORKED TONGUE / FACE VALUE: the secret is your *allegiance*, resolved by steering and reading, with no claim/challenge pot.
7. **Fills a gap?** **Yes — the headline one.** First hidden-loyalty / social-deduction game; 4–6P, ~25 min, talky, low-arithmetic — sits beside THE COUNCIL on the negotiation/betrayal shelf without duplicating it.
8. **Explainable cleanly?** **Yes.** "You secretly serve one sign. Each turn, push a sign or flip one to its back. When the deck runs out, the most-shown sign rules and everyone sworn to it wins." Three actions, one secret.
9. **Testable with the current prototype?** **Yes** — the Set D print-and-play deck plays it today, no extra parts.
10. **Fastest way to falsify fun?** One 5-player table, base game, watching two things: (a) does anyone's loyalty leak from handling a single flat card; (b) at the reckoning, did players form *reads* on each other ("I think Sam's on Crown") that turned out better than chance? If reads are pure noise, the deduction isn't real and the game is just a tug-of-war — that is the kill test.

## Open questions

- **Concealment integrity (highest risk).** Can a single flat loyalty card be guarded all game without leaks — peeking, accidental flashes, table-edge angles? JANUS's concealment collapsed in play; this needs a clean handling convention (press flat, never lift past vertical) confirmed at a table.
- **Is the deduction real?** The load-bearing question. Do decree-and-flip patterns actually betray masters, or does a busy public row drown the signal? If weak, pull in the pair-registry (rubric Q1/Q5 lever above) or add **The Wager** to the base game to reward reads directly.
- **Kingmaking at the reckoning.** The last flips can decide the ruling sign, and a player who can't win may hand it to a friend. Candidate fixes to test: simultaneous final-round actions, or a hidden-commit final turn.
- **The obvious-sign collusion.** Does everyone serving the highest-pip / safest sign collapse into a shared blowout win? THE COUNCIL hit the analogous "everyone takes one issue" line and broke it with unequal pip values + rollover; a sim *could* check whether the strength-count-plus-pip-tiebreak resolution is collusion-proof, or whether degrees-of-winning scoring is needed.
- **Player-count feel.** Team emergence at 4P (likely 1–2 share a master) vs 6P (likely 2–3) — where is the deduction sharpest? Range may tighten after testing.
