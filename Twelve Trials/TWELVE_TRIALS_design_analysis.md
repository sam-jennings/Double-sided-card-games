# TWELVE TRIALS — Design Analysis

*Companion to the rulebook. Successor to OUROBOROS in the solo slot, designed explicitly against that game's post-mortem.*

## 1. Design constraints inherited from the OUROBOROS cut

Live testing killed OUROBOROS for three reasons, which became this game's requirements:

| OUROBOROS failure | TWELVE TRIALS requirement |
|---|---|
| Too luck-based (shuffle dominated outcomes) | Open information: every card examinable at all times; plus a *replay-the-same-deal* mode and a zero-luck duel mode, both enabled by the upside-down flip marker |
| Hidden-face state was awkward (open symbol lived under the serpent's head) | No hidden state is ever *used* — the goal, the score, and all decisions read off visible faces and card orientation |
| Thin skill gap between random and skilled bots | Measured gap: unoptimised play ≈ 9 flips vs exact-optimal ≈ 5.3 — and the human skill (choosing among 840 almanacs) is the entire activity, not a side garnish |

## 2. The mathematical engine

- The 36 cards are the edges of K₉, which partitions into 12 triangles in exactly **840** distinct ways (Steiner triple systems on 9 labeled points; the solver generates and confirms all 840).
- Within any chosen partition, a triple's three dealt faces either already form a 3-symbol cycle or don't. The clockwise and anticlockwise mismatch counts always sum to 3, so a broken triple is **always fixable by flipping exactly one card** — never two. This gives the clean per-trio law in the rulebook and means: any deal completes in ≤ 12 flips, and a deal's true optimum = 12 − (max dealt-perfect triples over all 840 partitions).
- A random triple is dealt-perfect with probability 2/8 = 1/4, so an unoptimised partition costs 12 × 3/4 = 9 flips in expectation — confirmed at 8.97 in simulation.

## 3. Exact tuning numbers

2,000 random deals, every deal solved exactly over all 840 partitions ([twelve_trials_sim.py](twelve_trials_sim.py), seed 42):

| Optimal flips | % of deals | | Random-partition flips | % |
|---|---|---|---|---|
| 1 | 0.1% | | ≤5 | 1.9% |
| 2 | 1.2% | | 6 | 4.0% |
| 3 | 7.0% | | 7 | 10.6% |
| 4 | 20.7% | | 8 | 19.9% |
| 5 | 27.9% | | 9 | 25.0% |
| 6 | 24.9% | | 10 | 22.9% |
| 7 | 12.6% | | 11–12 | 15.7% |
| 8–9 | 5.4% | | | |

Average optimal **5.29**; average unoptimised **8.97**. A zero-flip deal never occurred in 2,000 shuffles, and one-flip deals appeared only twice — so the rulebook deliberately does *not* dangle a "perfect game" tier, unlike OUROBOROS's misleading 0-scar chase.

**Tier placement.** Master ≤ 4 is achievable on 29% of deals *by an exhaustive solver* — a human hitting it occasionally is genuinely strong. Gold at 5 sits at the solver's average (57% of deals admit ≤5). Silver 6–7 is good play; Bronze 8–9 brackets the no-optimisation baseline; 10+ means the player fixed trios instead of choosing almanacs. The known deal-to-deal variance in the optimum (±2 around 5.3) is *disclosed* in the rulebook and answered structurally by the replay mode and the duel, rather than hidden behind a single ladder.

## 4. Honest limitations

- **No human-level bot was built.** The gap measured is solver-vs-baseline; where humans land between 5.3 and 9 is unknown. First table question: does a thoughtful first game land near 7? If most players hit 5 quickly, compress the tiers.
- **Flip tracking (v1.1).** v1.0 marked flips by leaving cards upside-down, which assumed rotationally asymmetric art — and the obvious "fix" of a printed up-marker on one face was rejected on designer review for a serious reason: **a one-sided printed mark leaks hidden-face information in every hidden-information game** (in JANUS or FORKED TONGUE, learning which of Crown's pairs carry the mark Crown-side gradually identifies backs). Orientation-based marking also depends on which axis a player happens to flip over. v1.1 therefore marks flips by **sideways rotation** — state the *player* adds, like tapping: no print requirements on the cards, no information leak anywhere in the collection, fully reversible, and the deal-restore trick still works. This *removes* the art-direction constraint v1.0 had imposed.
- **The 840-almanac depth is invisible to players.** The rulebook hints at it ("840 possible almanacs") but the *experience* of unpicking an early lock needs live validation — it's the moment the game either sings or frustrates.
- **Trio verification flow** (examine three cards, confirm hidden faces) is untested for fiddliness; if it drags, a printed almanac reference card (any one valid 12-trio table) gives beginners a guaranteed-completable target while experts ignore it.

## 5. Change log

| Version | Change | Reason |
|---|---|---|
| concept | Grid + move budget + hidden-face study during setup | — |
| v1.0 | All information open; free rearrangement; flips the only cost | OUROBOROS post-mortem: no hidden-face memory |
| v1.0 | Flip = upside-down card; score self-tracking; perfect deal-restore | Kills bookkeeping; enables replay + zero-luck duel |
| v1.0 | Tiers 4/5/6–7/8–9 from exact solver | Solver avg 5.29, baseline 8.97; no false "perfect" tier |
| v1.1 | Flip marker: upside-down → **sideways rotation** | Designer review: printed/orientation markers leak hidden-face info into other games; sideways needs nothing printed (see §4) |
| v1.1 | Explicit trio set-aside (almanac row), never locked | Review question "what happens when a trio is found?" had no rule; unlocking supports the unpick-early-locks skill |
| v1.1 | Printed 4-season almanac = tutorial mode only | Review question: the AG(2,3) table is *one* of 840 almanacs; forcing it would erase the search (its expected cost ≈ 9.0 = the no-optimisation baseline) |

*All numbers: 2,000 deals solved exactly over all 840 partitions, seed 42, `twelve_trials_sim.py`.*
