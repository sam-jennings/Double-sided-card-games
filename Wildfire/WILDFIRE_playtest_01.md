# WILDFIRE — Playtest Report 01

**Game:** WILDFIRE v1.1  
**Players:** 3 (designer + 2 parents, non-gamers but experienced with traditional trick-taking)  
**Symbol subset:** Full 9-symbol / 36-card deck  
**Variant:** Standard (chain 2, refusal 2) + house rule (see below)  
**Date:** June 2026

---

## Setup

First ever table test of WILDFIRE. Played as the opening game to introduce the deck before moving to GLEAN. Prototype cards use letters A–I with corresponding numbers 1–9.

---

## Hypotheses tested

### 1. "The match-and-turn action is instantly legible."
**Confirmed.** No rule clarifications were needed at any point. The core action taught itself.

### 2. "Announce-rule policing is fun, not annoying."
**Not tested / not observed.** No data recorded on the announce rule specifically.

### 3. "Chaining feels like a real decision."
**Refuted.** Chaining was not experienced as a choice — everyone chained whenever possible. The bridge-burning tension predicted by the sim did not surface. Players never held back a chain for strategic reasons.

### 4. "A 3P game finishes in under 10 minutes."
**Confirmed (implicitly).** No length complaints; the game served its purpose as a quick intro.

### 5. "Refusal cost 2 hurts enough to drive play."
**Not specifically tested.** No data on refusal frequency or emotional impact.

---

## Bugs found

### B1: Hand management — no natural ordering (Severity: medium, deck-wide)
With 12 cards in hand (9 cards dealt + potential well draws), players wanted to sort their hand but couldn't find a meaningful order. In most card games, ordering by suit/rank is the first step after dealing. Double-faced cards resist this because each card belongs to two "suits" simultaneously. This is a **deck-wide ergonomics issue**, not WILDFIRE-specific.

**Player suggestion:** corner pips (numbers visible in a fan) would allow instant recognition. Flipping the entire fanned hand would also show all values on the reverse side quickly. The benefit outweighs the theoretical covering concern — it's easy to cover an entire card with one hand regardless of pip position.

*Note: the current CARD_LAYOUT.md specifies top-centre pips. The playtest feedback suggests corner pips may be worth revisiting for fan-readability, or at minimum that the top-centre pip must be large enough to read in a tight fan.*

### B2: Well-exhaustion rule is unintuitive (Severity: low)
When the well runs out, the rulebook says "take the 2 cards beneath the pile's top card." Players found it more natural to **move the top (target) card off the pile, flip the remaining pile to form a new well**, then draw from that. Same mechanical outcome (target unchanged, cards become available), but the physical action is cleaner.

### B3: Chaining is not a decision (Severity: medium, design)
Everyone always chained when possible. The sim showed a 1.5–1.8× skill edge partly from selective chaining (not chaining when it fragments your hand), but at the table — at least with new players — there was no perceived reason to hold back. This may emerge with experience, or it may be that the cost of chaining is too invisible to new players.

---

## House rule tested

**"Draw two, play one" (no chain):** When forced to draw 2 cards, the player may immediately play one of them (showing the target symbol), but without chaining. This felt like a small consolation prize for being stuck, reducing the sting of refusal without breaking tempo.

---

## Observations

- **Teaching:** flawless. The game needed zero rule clarifications — the best possible result for a gateway game.
- **Skill perception:** players did not feel there was much skill involved. The game felt reactive ("play whatever matches") rather than strategic. This is acceptable for its role as a deck introduction, but it means WILDFIRE won't hold attention on its own for repeat sessions.
- **Deck introduction value:** confirmed. After WILDFIRE, both parents understood flipping, the concept of two symbols per card, and how matching works. The game did its job.
- **Inferno (chain 3) not tested.**

---

## Verdict: **Iterate**

WILDFIRE works as a gateway game. The core loop is instantly legible and serves its purpose. The chaining-as-decision hypothesis failed, but that may be a skill-ceiling issue that emerges with experience rather than a structural flaw. The deck-wide hand-management finding (B1) is the most important output of this session.

---

## Concrete changes to consider

1. **Well-exhaustion rule:** rewrite to the "move target, flip pile to new well" phrasing. Clearer physical action, same game state. **[ADOPTED — rulebook updated.]**
2. **"Draw two, play one" variant:** document as a softener. Needs sim verification (does it change game length / skill gap meaningfully?). **[ADOPTED as the *Salvage* variant after sim check — see `WILDFIRE_design_analysis.md` §6. It holds length, keeps stalls at zero, and slightly raises the skill edge (3P 1.46×→1.56×). Recommended 3–4P, not made default on one session.]**
3. **Chaining as a decision:** possibly a non-problem — the skill gap exists in sim because the bot *sometimes* doesn't chain. New players always chaining is expected; whether experienced players learn restraint is a later question. **Do not remove chaining** — it's load-bearing for termination. **[NO ACTION — confirmed correct to leave; see analysis §6.]**
4. **Card layout (deck-wide):** the hand-ordering problem and the corner-pip request feed into `CARD_LAYOUT.md`. See session-level findings below. **[LOGGED in `DECK_PLAYTEST_FINDINGS.md` F1–F2.]**

---

## Session-level finding: card readability in hand

This applies to the entire deck, not just WILDFIRE:

- Players want to **fan** the hand and see pips (rank/identity) at a glance — standard card-game behaviour.
- The current top-centre pip position is workable but corner pips would be faster in a tight fan.
- Flipping a fanned hand to see the other side's values was desired and natural.
- The prototype's letter+number system (A=1, B=2, ..., I=9) was readable but the permanent association (same letter always = same number) was not obvious to all players. One player did not realise this until after the session ended, which materially affected their GLEAN play.

This finding should be recorded in `CARD_LAYOUT.md` and considered for the next prototype revision.
