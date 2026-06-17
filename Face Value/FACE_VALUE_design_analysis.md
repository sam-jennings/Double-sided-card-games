# FACE VALUE — Design Analysis

*Why a betting duel, and not the other two ways to bluff · June 2026*

The brief: a **2-player bluffing game** for the flip deck. The collection's bluffing slot (FALSE FACE) starts at 3P, and its only pure 2P game (CROSSROADS) is perfect-information. Three bluffing engines were explored before committing.

## The three candidate engines

### A. Claim & call (liar's-dice / FALSE FACE lineage)

You state something about a hidden face; the opponent calls or lets it stand.

**Why it fails as the 2P core:** FALSE FACE's tension comes from *diffuse* challenge responsibility — five people each hoping someone else pays the cost of being wrong. Heads-up, every claim has exactly one possible challenger, so each turn collapses into the same binary "do you believe me?" with no table-read, no free-rider tension, and a claim-chain that just ping-pongs. A 2P FALSE FACE variant would be a worse FALSE FACE, not a new game.

**Where it survives:** as FACE VALUE's **Cold Read** (call the exact hidden symbol, double-or-nothing — claim-calling distilled to its sharpest form) and the **Tell** variant (mandatory spoken claims with an honesty bonus).

### B. Trap-setting (Skull lineage)

Commit cards whose visible face conceals the real one; the opponent pushes their luck into your arrangement.

**Why it fails at 2P:** Skull is famously weakest at exactly two — with one opponent there's only one stack to read, the bidding war has no third party to outlast, and the push-your-luck odds become flat calculation. The deck also resists it: there is no face-down state, so a "trap" can only be a hidden face, which is what every other engine already uses.

**Where it survives:** stake cards and the escape card are placed *showing a face of your choice* — every card you commit is a small planted signal. Trap-setting through information rather than position.

### C. Betting / value bluff (poker lineage)

Stake material on the strength of a hidden value; raise, call, or fold.

**Why it wins:** heads-up is poker's *strongest* player count — the entire heads-up genre exists because betting pressure works perfectly at two. And the deck contributes three things generic cards can't:

1. **The shown face is the claim.** You don't declare strength; you *choose what to conceal*. Showing a 3 is a sentence ("I'm hiding something big") that costs nothing to say and everything to back.
2. **Ties are impossible.** Pair uniqueness means two duel cards can never match on both faces — hidden pip, then visible pip, always produces a winner. No split-pot rules.
3. **The lie-space shrinks publicly.** Morgue + two open tallies + your own hand eliminate partners of every shown face. FALSE FACE's signature — bluffing against arithmetic — re-emerges in betting form, and powers the Cold Read's late-game transformation from gamble to deduction.

## Key structural decisions

**Fold keeps the duel card unrevealed.** Poker's engine is that successful bluffs are never shown. Without this, every duel leaks a pair and the deduction layer finishes too fast. Cost of folding = stakes + one chosen escape card, so folding always bleeds material (termination) but never information you didn't choose to give.

**Winner's stakes return on a fold.** If your own staked cards entered your tally when the opponent folds, raising huge with the nuts would convert your hand directly into score. Returning them keeps raises as *risk*, only converted to score through a showdown the opponent consented to.

**Loser acts last next duel.** Crude-bot measurement showed near-flat results between symmetric bots, but positional advantage (acting with more information) goes to the player behind — same catch-up philosophy as CROSSROADS' pie rule.

**Hand exhaustion ends it.** Every duel strictly shrinks total hand cards (showdown ≥ 2, fold ≥ 1), so the game provably terminates — the lesson of the CROSSROADS ko-loop sim, applied at design time.

## Pacing sim (June 2026)

Quick Monte Carlo, 4,000 games per matchup, crude threshold bots (`face_value_sim.py` — pacing only, not balance):

| Matchup | Avg duels | Max duels | Skilled winrate |
|---|---:|---:|---:|
| skilled vs skilled | 11.6 | 17 | ~50% |
| skilled vs random | 12.5 | 17 | **94%** |

Always terminates; ~12 duels ≈ 15–20 minutes; the random-vs-skilled gap comfortably passes the OUROBOROS dullness test. Not yet tuned: raise sizing (High Stakes), cold-read fee (2 cards), escape fee (1 card). These are the table-test dials.

## Collection fit

Fills the last empty cell in the bluffing row: TURNOVER-light party, FALSE FACE 3–6P bluffing, **FACE VALUE 2P bluffing**, THE COUNCIL negotiation. Uses pips as ranks (shared with THE UNPLAYED PAIR), the palms-commit protocol (shared with THE COUNCIL), and the public-examinable dead-pair registry (shared with FALSE FACE). No one-sided marks; no face-down state; all tracked state visible — all standing rules observed.
