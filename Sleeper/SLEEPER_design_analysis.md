# SLEEPER — design analysis

*Status: v0.1, rulebook drafted, untested at the table. Stage 1 (Draft).*

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

### Setup

None yet. SLEEPER is talk-and-read driven (like THE COUNCIL, which also ships unsimmed); its open questions are social, not arithmetic. The two questions a sim *could* settle are listed under Open Questions; everything else needs a table.

### Findings

- n/a (no sim run). Termination is proven structurally rather than by simulation: one Court-deck card is consumed per turn.

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
