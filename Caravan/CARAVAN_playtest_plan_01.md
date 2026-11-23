# CARAVAN — Playtest Plan 01

*Pairs with the forthcoming `CARAVAN_playtest_01.md`. Written per `.kiro/steering/playtesting.md`. Hypotheses come from the rulebook's five follow-up playtest questions and [CARAVAN_design_analysis.md](CARAVAN_design_analysis.md) §7 and §9.*

## Open before the session

No rule gap blocks a 2-player session. **The session scope is the blocker:**

- **The game's headline question can't be answered at 2P.** `next_step` is "table it at 3P and settle whether packing for one *named* neighbour changes what you pack." At 2P the road runs "across, every round". You always pack for the same person, and that person always packs for you. The road never turns, nobody chooses a customer, and you can retaliate directly. Questions 1 (named neighbour, in full), 3 (no retaliation), 4 (reading four offers) and 5 (three rounds at 4P) all need 3–4 players.
- **Decision for the designer:** if a third player can be found, run this plan at 3P instead (4 rounds, road left · right · left · right). Otherwise this 2P session is a **flow-and-feel test**. It can certify the handling, the dressing/placement loop and a weak form of Q1, but **`next_step` stays open after it**.
- Minor, not blocking: the rules don't say who draws first in the self-deal or the refill. Alternate one card at a time, non-dealer first, so stock-top glimpses are shared evenly.

## Setup

- **Game:** CARAVAN
- **Version:** v0.1 (floor certified over ~4,200 simulated games; never tabled).
- **Players:** 2 — the road runs across every round. 6 rounds, 12 offers, stock empties after round 4, hands 6 → 3 → 0.
- **Symbol subset:** all 9 signs / 36 cards. Deal 6 each, stock 24.
- **Session shape:** one **Open Caravan** teaching deal (takers may examine both faces of their offer), then **one or two base deals**.
- **Why this session:** CARAVAN is the collection's simultaneous SILK CUT sibling. It is testable with the deck alone, and its 2P mode has never been handled. Settling flow and dressing feel at 2P makes the later 3P session spend its time on the road.

## Hypotheses to test

The rulebook's playtest questions, adapted to what 2P can show, as falsifiable predictions with the sim's 2P numbers:

- **H1 — The receiver's spread changes what you pack (2P precursor of Q1).** At 2P the only recipient is your only rival, so this is the easiest possible case for the premise. *Prediction:* in at least half the rounds, the packer can name something in the opponent's spread that changed which cards they offered or how they dressed them. *Falsified if* packers consistently pack "my three worst cards" regardless of the opponent's spread. The sim's ring-aware vs ring-blind ablation is **0.90× at 2P** — flat — so the bots predict failure. If even 2P fails, expect 3P to fail too and plan to try *The trailing road* there. If 2P passes, that **does not settle** Q1, because a named neighbour at 3P is a different decision.
- **H2 — Simultaneous play feels social, not solitaire (Q2).** *Prediction:* players watch each other's offers and spreads and react aloud to takes. *Falsified if* each player works their own offer in silence and the round feels like two parallel puzzles.
- **H3 — The take is a real decision.** Sim at 2P: **40.4% of takes live**, 32.7% dominant, and the bigger lot taken **60.7%** of the time. *Prediction:* the taker hesitates on a fair share of offers, and the 1-card lot is taken at least a third of the time. *Falsified if* "take the pair" becomes automatic.
- **H4 — Dressing reads as a bluff.** The dressing ablation is flat (**1.12× at 2P**), and the analysis suggests the bluff may matter more to people than to perfect-memory bots. *Prediction:* at least once per deal a taker says they were misled, or chose to distrust a shown face. *Falsified if* dressing is always honest or ignored.
- **H5 — Placement is a second decision.** *Prediction:* players sometimes place a captured card on its lower-pip face to win a majority. *Falsified if* every card is placed on its higher pip.
- **H6 — Seat parity.** Construction is symmetric; sim 2P thoughtful mirror **92 / 107** (consistent with symmetry, no SILK CUT-style second-cutter edge). *Prediction:* no structural seat effect noticed. One or two deals can only flag something gross.

## What to watch

Handling first:

- **Laying offers.** Each card must be laid flat with only the chosen face shown. Watch for the hidden face flashing during the lay — and whether players care. A leak here empties the bluff.
- **No-touch offers.** Takers may not lift or tilt offered cards. Watch whether the urge to peek is strong, and whether it causes disputes.
- **Simultaneous take.** "Hands down on three." At 2P this is trivial; note any friction anyway.
- **Placement lock.** Spread cards are never re-flipped, but they may be examined and returned as found. Watch for cards returned the wrong way up — scoring state silently changed.
- **Stock-top glimpses.** The rules make glimpses legitimate memory and forbid asking afterwards. Watch whether players try to remember draws, and whether the no-asking rule feels mean or fine.
- **Spread layout.** Columns by scoring sign. Watch that majorities can be read at a glance across both spreads.

Then:

- **Round length.** Time each round. Pack is the slow step — up to a few hundred legal packs.
- **Endgame.** Rounds 5–6 come from 3-card hands. The rulebook expects them to be "close to pure calculation". Note whether that feels satisfying or dead.
- **Score shape.** Up to 45 points; expect about 30 awarded. Note ties per sign.

## Observable success / failure signals

| | Holds (success) | Fails |
|---|---|---|
| H1 | Packer cites the rival's spread in half the rounds or more | "Three worst cards" every round |
| H2 | Players watch and react to each other's offers | Parallel silence |
| H3 | Visible hesitation; singleton taken ≥ 1/3 | Pair always taken, instantly |
| H4 | A shown face is distrusted or misleads someone | Dressing always honest, or ignored |
| H5 | Some low-face placements to win a sign | Always the higher pip |
| H6 | No gross seat effect | One seat dominates for a structural reason |
| Handling | No flashed hidden faces; no peeks; no mis-returned spread cards | Any of those happen repeatedly |

## Teaching plan

- Say the **Nine Signs rank canon** aloud, verbatim from the rulebook.
- One-sentence core from the analysis: "Pack three cards as a two and a one for the player the road points to; everyone takes at once; you keep what they leave."
- At 2P, say plainly that the road always points across. The turning road is the 3–4P game.
- Play the **Open Caravan** deal first: no bluff, so the flow, placement choice and majority counting land in one deal. Then switch to hidden faces for the base deal.
- Read "What is actually hidden" aloud before the base deal. It is the rulebook's own "whole game" section.
- **Watch during teaching:** whether "you score the lot the taker *leaves*" needs repeating. That reversal is the likeliest comprehension snag.

## Record sheet

Per round (base deal):

| Round | P1 packed: pair / single (shown faces) | Did P2's spread change P1's pack? (Y/N + what) | P2 took | P2 packed: pair / single | Did P1's spread change P2's pack? | P1 took | Round time |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |

| | Player 1 | Player 2 |
|---|---|---|
| Signs won (list) | | |
| Final score | | |
| Signs tied (no score) | | |
| Times misled by dressing | | |
| Low-face placements | | |

- Deal type: Open / Base 1 / Base 2. Teach time: ____ Play time: ____ (target ~15 min)
- Hidden-face flashes / peeks / mis-returned cards: ____
- Surprises / quotes:

## Out of scope

- **The road's real test (Q1 in full), no-retaliation (Q3), four-offer reading load (Q4) and three rounds at 4P (Q5)** — all need 3–4 players. Carry them to a 3P session; `next_step` stays as written.
- **The trailing road** — only after the base road has been played at 3P (analysis §7).
- **Two-deal 4P match play** — later.
- Re-simulation — the floor is certified; the table is the priority.
