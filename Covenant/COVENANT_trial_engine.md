# COVENANT — The Turning (trial engine, version B)

*Design draft, July 2026. Supersedes the Model 3 (memory) recommendation in [COVENANT_design_analysis.md](COVENANT_design_analysis.md). That analysis proved the blind permutation match has no skill in it (1.00x, closed form) and reached for memory as the rescue. This draft rejects that rescue and rebuilds the chapter on a different pillar: **open information, with the sign verbs as the tactical engine**. Not memory, not luck — play.*

## The base (fixed)

- Played in chapters; each chapter introduces one new sign.
- The adversary is the new sign's cards pairing it with already-won signs.
- The player defeats the adversary using the rest of the sub-deck.
- **The sign abilities are the key to completing a chapter** — the skill lives in verb use, not recall or guessing.

## The pivot

The old designs hid the attackers' partner faces and made concealment the game; the sim showed there is nothing behind that curtain. So open the curtain. Lay the enemies **partner-face up**: the new sign *S* has not hidden among your allies — it has *stolen their faces*. Every enemy is an impostor wearing a won sign's face, and everything on the table is public. The game is no longer "what is this card?" but **"in what order, and with which verbs, do I take these impostors down?"** — a tactical gauntlet with a fully readable attack script, which is exactly what solo play wants.

The deck's gift to this design is no longer the uniform row; it is that **every card in your hand is two verbs**. Playing a card means choosing which face — and therefore which power — to commit, and every choice of face is also the loss of the other. That tension was sitting unused in every earlier model.

## The battlefield

Chapter that courts sign *S*, with won set W (|W| = k−1):

- **The gauntlet.** The k−1 cards pairing S with W, laid in a row **partner-face up**. Each impostor's **strength = its visible pip**. The leftmost impostor is the **vanguard**.
- **Your covenant.** The C(k−1, 2) cards pairing signs within W — shuffled, this is your deck, your health, and your toolkit at once. Draw a hand of 4.
- **Piles.** *Spent* (face-up, recoverable) and *Ash* (face-down, gone for the chapter).

## The turn

1. **Draw 1.** If you cannot, the trial is lost.
2. **One action:**
   - **Strike** an impostor: commit cards from hand whose *chosen-face* pips total ≥ its strength, **including at least one card bearing its sign** — only the true friend can unmask the impostor. Committed cards go to Spent. Striking anything behind the vanguard costs +1 pip (reach).
   - **Invoke** a verb: play one card by a chosen face; resolve that sign's power (table below); card to Spent.
   - **Rest:** draw 2.
3. **The vanguard acts**: its visible face's corrupted verb resolves against you (table below). Persistent effects (locks, hostages) belong to the impostor and end when it falls.

An unmasked impostor is **turned**: flip it to its S-face — the sign's true face, acknowledged at last — and set it in your bank. Turn all of them and the chapter is won: the banked cards shuffle into your deck. Winning and writing the save are still one gesture.

## The nine verbs — yours when invoked, corrupted when worn

| Pip | Sign | Your invocation | The impostor's corrupted verb (as vanguard) |
|--:|---|---|---|
| 1 | Moon | Recover any card from Spent to hand | *Wane:* ash the top card of your deck |
| 2 | Leaf | Draw 2, keep 1 in hand, 1 to Spent | *Entangle:* discard your lowest-pip hand card to Spent |
| 3 | Wave | Move any impostor anywhere in the row | *Carry:* takes your deck's top card **hostage** under itself (returned when turned) |
| 4 | Flame | Ash any impostor unturned — instant, but it joins as a **grudge** | *Burn:* ash your highest-pip hand card |
| 5 | Eye | Next strike this chapter needs no matching sign (you see its true name) | *Gaze:* **locks** your highest-pip hand card until it is turned |
| 6 | Mask | Copy the verb of any turned card in your bank | *Masquerade:* swaps itself with the rearmost impostor |
| 7 | Key | Turn a strength-≤3 impostor outright (unlock, no strike) | *Lock:* seals your Spent pile until it is turned |
| 8 | Star | Wild: invoke any won sign's verb | *Anomaly:* flip your deck's top card — suffer its higher face's corrupted verb |
| 9 | Crown | Take a second action this turn | *Decree:* the next impostor in the row also acts |

Damage verbs hurt; **lock and hostage verbs create target-priority decisions** — the false Key strangles your Moon economy until you cut it down, the false Wave dares you to strike deep for your hostage. That, plus Wave/Mask reordering the readable attack script, is where the tactics live.

## The chapter curse

The sign you are courting fights with its own verb all chapter — the campaign is the nine verbs crossing the table one at a time:

| Trial | Curse while unwon |
|---|---|
| Eye | You play with your hand face-up on the table; Gaze locks the card of *the game's* choosing (highest pip, ties leftward) |
| Mask | At the end of every round, the two frontmost impostors swap |
| Key | Every strike pays a toll: +1 pip |
| Star | Each round, flip your deck's top card; its higher face's corrupted verb triggers |
| Crown | The vanguard acts twice |

Win the trial and the curse becomes your invocation, permanently. (The founders — Moon, Leaf, Wave, Flame — are never trialed; their verbs are yours from the founding rite.)

## The campaign frame

- **Founding.** Chapter one is the founders' rite: the 6-card deck, a 4-impostor gauntlet with no curse — the teach.
- **Choose your court.** After founding, court Eye, Mask, Key, or Star **in any order** — each order is a different campaign, because the verbs you win early are the tools you carry, and the curses you delay grow harsher against longer gauntlets. Crown is always last: the Crown does not treat with a Tenth who lacks the other eight. (Canonical top-trim is a lobby convention; mid-campaign, any won set is a complete all-pairs deck — the ORRERY precedent.)
- **Between chapters** everything returns to the deck; only grudges persist.
- **Grudges.** A Flamed or failed sign still joins, cards rotated 180° (the orientation-lock save): its invocation costs two cards, and impostors wearing its face in later trials strike with doubled effect. The story remembers how you won.
- **Assists (2–4).** Each assistant embodies one won sign and may invoke its verb once per chapter for free, on the solo player's turn.

## What survives, what dies

Survives: the sub-deck as the save file; deck-as-health; the flip as the reward; grudges; the falsification discipline. Dies: the blind permutation (proven skinless) and memory as the spine. Memory is not banned — a future Mask-trial variant could seal the gauntlet faces and run Model 3 as *that one chapter's* texture — but it carries nothing.

## Open questions

- **Economy tuning.** Draw 1 + one action against a vanguard acting every round: is the founders' rite (6-card deck, 10 pips of strength to buy) winnable often enough — and losable at all? First number to check.
- **Vanguard-only vs. auras.** Only the front impostor acts. If gauntlets of 7–8 feel inert behind the front, give rear impostors passive auras — but count the cognitive load first.
- **Reach cost.** +1 pip to strike deep may be too cheap to protect the queue structure, or too dear to ever use.
- **Are invocations real choices?** Flame (instant kill, grudge price) and Rest (tempo loss) must both get picked sometimes; if either is always right or always wrong, retune.
- **Order-of-courtship balance.** Star-early (wild) vs. Eye-early (free strikes) — different, or strictly better?

## Fastest falsification

One solo sitting, printed Set D deck: play the founders' rite twice, then the trial of Key (curse: +1 pip toll, false Key locking Spent). Watch two things — does turn order against the readable script feel like a plan being executed, and does at least one game end in a loss or a tempting Flame-grudge? If every game is a comfortable clear with no order decisions, the engine is not yet a game. Extend [covenant_sim.py](covenant_sim.py) to measure the skill gap (greedy striker vs. verb-sequencing player) before writing the full campaign book.

## Next step

Script the founders' rite turn-by-turn on paper, then sim it. Only then write chapter rules prose.
