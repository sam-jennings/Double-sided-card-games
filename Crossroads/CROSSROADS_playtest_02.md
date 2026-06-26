# CROSSROADS — Playtest Report 02

*Pairs with [CROSSROADS_playtest_plan_02.md](CROSSROADS_playtest_plan_02.md). Written per [playtesting.md](../.kiro/steering/playtesting.md). Part of the Lauren & Arran session, June 2026 — raw notes in [Lauren and Arran Playtest.md](../Lauren%20and%20Arran%20Playtest.md).*

## Setup

- **Game / version:** CROSSROADS v1.1 (Signal Fires flip economy in the rules).
- **Players & config:** started **2P with 14 cards each** (Arran & Lauren, Sam observing); then switched to an **off-spec 3P game with 9 cards each**, using a leftover card as the first built road.
- **Symbol subset:** 9 symbols / 36 cards (8 cities, 28 roads).
- **Critical deviations from the plan:** Plan 02's entire purpose was to test the **Signal Fires flip economy** at 2P. In the event, **flips were effectively not exercised** (players found the game already overwhelming and explicitly declined to engage flipping), and the session **moved to a 3-player variant CROSSROADS is not designed for.** So Plan 02's flip hypotheses (H1, H2) were **not tested**; the session instead exposed two more fundamental problems.

## Hypotheses

| | Verdict | Notes |
|---|---|---|
| **H1 — "eight flips ache"** | **Not tested** | Players found the base game overwhelming before flips entered; flipping was declined as "even more confusion." |
| **H2 — "dimming reads at a glance"** | **Not tested** | Signal Fires weren't meaningfully used. |
| **H3 — banked-contract behaviour survives flips** | **Not tested** | No flip pressure applied. |
| **H4 — the end trigger is clean** | **Refuted** | End-of-game remains undefined and unfair (see Bug 2). |

## Bugs found (severity-ranked)

### Bug 1 — Pass-to-win: doing nothing is a dominant strategy *(degenerate strategy — CRITICAL)*
The session's most important finding, and a serious one. In the 3P game everyone made their contracts; **Sam was the only player to "pass" (not spend a card as a road) and won** — the table felt the pass itself gave the advantage. They then **stress-tested it directly: Sam passed every single turn.** Result: by game end **every route was achievable anyway** (Lauren's observation), so Sam **won overwhelmingly without doing anything.**

This is a genuine dominant-strategy bug: if the network the other players build tends to **connect everything**, then **keeping more cards as contracts (= passing / building nothing) strictly wins**, because every kept card becomes a fulfilled contract for free. The "keeping a road deletes it from the world" tension that's supposed to make hoarding costly **doesn't bite** when the remaining roads still connect all pairs. The intended skill (reading which contracts your opponent nurses; denying routes by direction) collapses. 

*Caveats on scope:* this was observed **3P and off-spec, with flips barely used.** Flips (reversing roads to deny routes) are precisely the mechanism meant to make "every route is achievable" false — and they weren't exercised. So the bug may be **partly an artefact of skipping the flip economy and adding a third builder** (more players = more roads built = more connectivity = more free contracts). But it is alarming enough that it must be **reproduced under proper 2P + Signal Fires play before CROSSROADS's collection status is safe.**

### Bug 2 — End-of-game trigger is undefined and unfair *(rules / fairness — HIGH, carried from Playtest 01)*
Still unresolved. The rulebook's "both players pass consecutively" did not give a clean stop. The table improvised "if one player wants to stop, others take one more turn," but that reintroduces the asymmetry flagged in Playtest 01: a player can **stop early after banking two quick contracts**, freezing the board in their favour. Plan 02 predicted Signal Fires (all eight cities dimming = a natural exhaustion point) would fix this — **untested**, because flips weren't used. The end trigger is now a **twice-flagged HIGH bug.**

### Bug 3 — 14-card hands are overwhelming; no foothold to plan *(handling / onboarding — HIGH)*
At the designed 2P / 14 cards, Arran and Lauren **didn't enjoy it from the start**: too many cards, each needing both faces checked, too many options, and **no idea how to begin** — they felt they *should* be able to form a plan but couldn't find the entry point. Dropping to **9 cards (the 3P split) felt markedly more manageable.** This echoes TRIGON/BLIGHT: large hands × two-faced cards × no natural sort (DECK_PLAYTEST_FINDINGS F1) is a recurring wall, and CROSSROADS's perfect-information "compute everything" framing makes the analysis-paralysis worse, not better.

### Bug 4 — First-turn paralysis persists *(onboarding — MEDIUM, carried from Playtest 01)*
The "no obvious anchor for the opening move" bug from Playtest 01 recurred and feeds Bug 3.

## Findings (not bugs)

- **The 3P variant felt better than the 2P game** to this group — purely on hand-size manageability (9 vs 14 cards). CROSSROADS is explicitly a 2P duel and 3P breaks its information structure (your rival's hand is no longer exactly "the rest"), so this is **not** a recommendation to make it 3P — but it's a strong signal that **hand size is the dominant comfort lever.**
- **Flipping was perceived as added complexity, not added depth**, by first-time players already at capacity — a teachability warning for v1.1's central mechanic.

## Rule-change candidates (each tied to an observation)

1. **Reproduce Bug 1 properly before redesigning.** Run the **designed 2P game with Signal Fires actually used**, and have one player attempt the pass-to-win line. If flips let the active player **deny the passer's routes** (reverse a critical road so a kept contract fails), the bug is an artefact of the off-spec 3P/no-flip session. If pass-to-win **survives proper play**, it is a structural flaw requiring one of the fixes below. *This is the single most important next test for CROSSROADS.*
2. **If pass-to-win is real, the leading candidate fix already exists: the Toll Roads variant.** It scores +1 per road *you* built on a fulfilled route — directly punishing the parasite who builds nothing and rewards infrastructure. Consider **promoting Toll Roads scoring into the base game.** (Tie to Bug 1.)
3. **Lauren's deal-split idea (Bug 1):** fix some cards as **contracts** and some as **roads** at the deal, so you can't convert every kept card into a free contract. Sam found it "not as neat," but it's a clean structural answer — worth prototyping/simming against the pass line. (Her second idea — pre-declaring contract direction — was rejected by the table as unclear in when/how you'd commit; drop it.)
4. **Define the end trigger (Bug 2).** The cleanest answer is to **lean on Signal Fires as the clock**: the game ends when the **eighth city dims** (all flips spent), making the stop point objective and shared rather than negotiated. Test whether this also resolves the asymmetric-readiness unfairness, as Plan 02 predicted. *Alternative floated by the table:* a player may only declare a stop if **their entire hand is completed contracts** — worth considering as a secondary condition.
5. **Hand-size / onboarding (Bug 3, 4):** consider an explicit **opening-move suggestion** in the rules to break first-turn paralysis, and a **reduced-hand teaching variant** (fewer roads in play) to let new players learn before the full 14-card duel. Do not make 3P official.

## Verdict: **ITERATE — with a flagged structural concern**

This was an **off-spec session** (3P, flips unused) that did not test what Plan 02 set out to test, so v1.1's Signal Fires economy remains **untested at the table for a second time running**. But it surfaced a **CRITICAL pass-to-win line** and re-confirmed the **HIGH end-trigger** and **hand-size/onboarding** bugs. Because CROSSROADS is currently a **promoted collection game**, the pass-to-win finding is the priority: it must be reproduced (or refuted) under the **designed 2P + Signal Fires** rules before the next iteration.

**CROSSROADS remains in the collection for now, but on notice:** if pass-to-win survives a proper 2P flip game, its collection status should be re-examined.

### Next session must answer (this is the rung-1 priority for CROSSROADS)
1. **Under 2P with Signal Fires actually used, does pass-to-win survive?** Have a player attempt it; see whether flips let the opponent deny the passer's routes.
2. Does the **eighth-dim end trigger** resolve the end-of-game unfairness (Bug 2 / H4)?
3. Do the recorded flip hypotheses (**H1 "eight flips ache," H2 "dimming reads at a glance"**) finally get a test?
4. Does a **reduced-hand teaching ramp** cure the 14-card cold-start paralysis (Bug 3, 4)?
