# Sign → ability mnemonics: a cross-game proposal for TRIGON & TURNCOAT

*Goal: make the two ability tables easy to remember by giving each of the Nine Signs a single, consistent identity that holds across both games, with mnemonics where the sign's picture cues both its requirement and its ability. Re-pairing was authorised and tested; the recommendation below lands on the change that achieves the goal with **zero balance impact**.*

---

## The headline

- **TURNCOAT changes nothing mechanically.** Its nine signs already sit on the "ideal" bundles (Leaf = swap, Mask = flip, Key = extract, Crown = self-extract, …). It was already right.
- **TRIGON needs one relabel: Leaf and Key swap which (requirement + ability) they carry.** Today Trigon's Leaf is the *flip-a-neighbour* sign and Key is the *swap* sign — the **opposite** of Turncoat, where Leaf is swap. Swapping the two labels makes **Leaf = swap** and **Key = flip** in both games.
- Result: **7 of the 9 signs now mean the same thing in both games.** Only Key and Crown stay game-specific, and that is structural, not fixable (see below).
- **No balance cost.** Relabelling reuses Trigon's existing, already-tuned bundles — the simulator runs the identical 9 bundles, so the ~23k-game balance is untouched. I confirmed this against the live sim, and separately tested the more aggressive re-pairing you authorised — it skewed 3-player seats, so I did **not** use it (details in *Balance validation*).

The only edits to apply later are: Trigon's 9-sign table (swap Leaf/Key rows), one worked-example line, and one FAQ line ("Key swap" → "Leaf swap"). Nothing in Turncoat.

---

## The unified system — one idea per sign (the cheat sheet)

Learn these nine once; they carry across both games.

| Sign | One idea | In TRIGON | In TURNCOAT |
|---|---|---|---|
| 🌙 **Moon** | **The underdog** — acts only when you're behind, and strikes at abundance | Behind on captures → take the top card face-down | A rival 2+ ahead → destroy the leader's top banked card |
| 🍃 **Leaf** | **Swap** — trade two cards' places | Swap any two cards | Swap with any agent, then may flip the displaced one |
| 🌊 **Wave** | **Move** — carry a card to open space | Move any card to an empty cell | Move the lone neighbour to an empty post, may flip it |
| 🔥 **Flame** | **Burn** — remove a neighbour from the game | Discard one adjacent card | Remove one adjacent rival |
| 👁 **Eye** | **Peek** — read a hidden neighbour, then maybe flip | Peek an adjacent card; may flip it | Peek an adjacent agent; may flip it |
| 🎭 **Mask** | **Flip** — change a face / an allegiance | Flip any one card | Flip any agent in its row/column |
| ⭐ **Star** | **Draw** — take the next card and play it | Draw-and-play (**and wild** in alignments) | Draw-and-play |
| 🗝 **Key** | **Release one card** *(specialist)* | Turn a neighbour (flip one adjacent) | Free your agent from its line → your pile |
| 👑 **Crown** | **Act from strength** *(specialist)* | Its line is full → command the other two (flip them) | Withdraw itself to its owner's pile |

**Seven are identical** (Moon, Leaf, Wave, Flame, Eye, Mask, Star). **Two are "specialists"** — Key and Crown — because the games score differently: **TRIGON manipulates the board** (you flip and align to capture), while **TURNCOAT banks cards** (you extract to score). Trigon has no "bank a card" action at all, so Key and Crown *cannot* mean the same verb in both — the honest move is to brand them "the expert signs" and learn their two readings. A unifying hook still helps: *Key turns/unlocks one card; Crown acts from a position of strength.*

---

## TRIGON — proposed table

**Only Leaf and Key change** (they swap bundles). Everything else is today's rulebook, with punchier mnemonics.

| Sign | Requirement (cell condition) | Ability | Mnemonic |
|---|---|---|---|
| 🌙 **Moon** (1) | Has **no** orthogonally adjacent card (stands alone) | *If you have fewer captures than someone:* take the top card **face-down** (worth 1) | A lone moon in an empty sky waxes from nothing — having least, it gains |
| 🍃 **Leaf** (2) | **2 or more** orthogonally adjacent cards *(was: on an edge)* | **Swap** any two cards on the grid *(was: flip one adjacent)* | Crowded leaves on a branch trade places — with two or more neighbours, the Leaf swaps any two |
| 🌊 **Wave** (3) | Shares its row or column with an empty cell | **Move** any one card to any empty cell | The Wave needs open water in its row or column — it carries any card to the empty shore |
| 🔥 **Flame** (4) | Exactly **1 or 2** adjacent cards | **Discard** one adjacent card (out of the game) | Flame needs fuel but not a crowd — one or two neighbours, and it burns one away |
| 👁 **Eye** (5) | Has an empty orthogonally adjacent cell (room to look) | **Peek** the hidden side of an adjacent card; you may then flip it | Given room to look, the Eye reads a hidden face — and may turn it to the light |
| 🎭 **Mask** (6) | In the middle row or middle column (central cross) | **Flip** any one card | From the crossroads it sees every face — the Mask flips any one |
| 🗝 **Key** (7) | On an **edge** cell (a threshold) *(was: 2+ adjacent)* | **Flip** one adjacent card *(was: swap any two)* | A key sits in the door at the edge and **turns** — flipping one neighbour |
| ⭐ **Star** (8) | On a corner | **Draw** the next card and play it. *Star is wild in alignments* | From the sky's corner the Star draws the next card — and counts as any sign |
| 👑 **Crown** (9) | Its row or column is fully occupied | **Flip the other two** cards in that full line | When its court (line) is full, the Crown decrees — the other two must turn |

Why this lands well even though Leaf gives up the pretty "leaf at the branch's edge": the **edge** requirement transfers to **Key**, where it reads *better* — a key sits in a door (a threshold/edge) and **turns**, which is exactly its flip. Leaf's new "clustered → trade places" is a clean image too, and crucially Leaf now means **swap** in both games.

---

## TURNCOAT — proposed table

**No mechanical change** — only refreshed mnemonics, phrased to echo Trigon where the sign matches.

| Sign | Requirement | Ability | Mnemonic |
|---|---|---|---|
| 🌙 **Moon** (1) | A rival has **2+ more** banked cards than you | Remove that leader's **top banked card** from the game | Behind by two, the waning Moon darkens the fullest hoard — one banked card gone |
| 🍃 **Leaf** (2) | Adjacent to one of **your** agents | **Swap** with any agent; you may then **flip** the displaced one | Leaves on one branch (your allies) trade places — the Leaf swaps, then may turn what it displaced |
| 🌊 **Wave** (3) | **Exactly one** adjacent agent | **Move** that agent to any empty post; you may then **flip** it | The Wave takes the lone agent beside it, carries it to an open post — and may tumble it over |
| 🔥 **Flame** (4) | Adjacent to a rival agent | **Remove** one adjacent rival agent (its post empties) | Flame burns the rival standing next to it — off the board |
| 👁 **Eye** (5) | **At most one** adjacent agent | **Peek** the hidden face of an adjacent agent; you may then **flip** it | In near-solitude the Eye reads a hidden face — and may turn it |
| 🎭 **Mask** (6) | Adjacent to a rival agent | **Flip** any one agent in its row or column | Near an enemy, the Mask turns a loyalty somewhere along its line |
| 🗝 **Key** (7) | Its row or column holds **2+** of your agents | **Extract** one of your agents from that line → your pile | Where your allies line up, the Key unlocks one — straight to your pile |
| ⭐ **Star** (8) | **Two or more** adjacent agents | **Draw** the next card and play it | Well-connected, the Star draws the unexpected and plays it at once |
| 👑 **Crown** (9) | Adjacent to one of **your** agents | **Extract Crown's own card** to its owner's pile | Among allies, the Crown withdraws itself to its keep — banked to its owner |

---

## Why these assignments (the reasoning)

1. **Match each ability to the sign's archetype.** The canonical Nine Signs already carry verbs (`SYMBOL_SET.md`): Flame = burn, Eye = peek, Wave = move/carry, Star = draw-the-unexpected, Moon = wane/catch-up, Mask = flip-identity, Key = unlock/extract, Crown = rule/self-determine, Leaf = connect/turn/trade. Both games' "obvious" abilities fall straight onto these — **five signs were already consistent** (Moon, Wave, Flame, Eye, Star) and Mask (flip) was too.
2. **Fix the one real clash: swap.** Turncoat puts swap on **Leaf** ("leaves trade places"); Trigon put swap on **Key** and flip on **Leaf** — the reverse. That single mismatch made *two* signs read oppositely across the games. Relabelling Trigon's Leaf/Key fixes both at once.
3. **Accept the Key/Crown limit honestly.** Trigon flips/aligns to score; Turncoat extracts to bank. There is no extraction in Trigon, so Key (=extract) and Crown (=self-extract) can't carry the same verb there. Forcing it would mangle one game. Branding them "the two expert signs" is the cleaner teaching.

---

## Balance validation (simulator)

All runs use the rulebook-faithful v1.2 flags. The Trigon health bar (from its design analysis): captures ≥ 8/game, zero-capture < 5%, ties < 8%, seat win rates within 52/48, skilled-beats-random > 70%, no dead signs.

**The recommended relabel is balance-neutral by construction** — it reuses Trigon's existing nine bundles, so the simulator runs identical mechanics. The current numbers therefore *are* the proposal's numbers:

| Trigon (greedy mirror) | Seats | Captures/game | Zero-cap | Ties | Skilled-vs-random |
|---|---|---|---|---|---|
| 2P (1,500 games) | 48.1 / 51.9 | 19.2 | 0.0% | 0.0% | 96.8% |
| 3P (1,400 games) | 33.9 / 33.4 / 32.6 | 19.3 | — | — | — |
| 4P (700 games) | 23.4 / 27.3 / 26.4 / 22.9 | 19.7 | — | — | — |

Turncoat is untouched; its v1.2 balance stands (Mask the deliberate top pick ~57% owned-win, every other sign ~45–54%, every sign active and banking, catch-up Moon's win-correlation slightly negative by design).

**I also tested the aggressive re-pairing you authorised** — giving Leaf its natural *edge* requirement by moving the **swap** power onto "edge" and flip onto "2+ adjacent" (so each sign's requirement would fit even better). The simulator's verdict, same flags:

| Trigon 2P / 3P | Seats 2P | Captures | Seats 3P (1,400 games) |
|---|---|---|---|
| Baseline (= relabel) | 48.1 / 51.9 | 19.2 | 33.9 / 33.4 / 32.6 |
| Aggressive re-pair | 49.2 / 50.8 *(tighter)* | 16.5 | **32.3 / 37.2 / 30.5** *(P2 skew)* |

It tightened 2-player seats and flattened the per-sign spread, but **skewed the 3-player seats** (middle seat +4%) — a regression of the tuned 3P balance, in exchange for only a marginally nicer Leaf requirement. **Not worth it.** The balance-neutral relabel reaches the same cross-game consistency and gives Key a *better* mnemonic anyway, so that's the recommendation.

---

## What applying this would touch (for when you approve)

- **TRIGON_rulebook.md:** swap the Leaf and Key rows in the 9-sign table; the worked-chain example ("activate Leaf: flip the card above it" → that bundle is now **Key**); one FAQ line ("Can **Key** swap two cards…" → "Can **Leaf** swap…"). Card manifest, scoring, and all other rules are unaffected.
- **TURNCOAT_rulebook.md:** optional — drop in the refreshed mnemonics; no rules touched.
- No simulator, balance number, geometry, or card change anywhere.

Say the word and I'll apply it to the rulebooks.
