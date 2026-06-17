# Implementation Plan: TRIGON & TURNCOAT Retheme to Nine Signs

## Overview

Create the TRIGON rulebook from scratch in a new `Trigon/` folder, rewrite the TURNCOAT rulebook in place, archive the old Syzygy/ file with a notice, and update all cross-references across the repository. The sign-to-ability mapping from design.md §2 is the single source of truth for all name substitutions. The game formerly known as SYZYGY is now TRIGON — the celestial framing is retired entirely. All work is document writing — no code tasks.

## Tasks

- [x] 1. Write TRIGON rulebook (new file: `Trigon/TRIGON_rulebook.md`)
  - [x] 1.1 Write TRIGON title, intro paragraph, and components section
    - Create `Trigon/TRIGON_rulebook.md` as a new file (not a copy of the old SYZYGY rulebook)
    - Title: `# TRIGON`
    - Intro paragraph uses the Nine Signs convergence framing: "a three-point convergence of signs" — no celestial language
    - No pronunciation guide (TRIGON needs none)
    - Replace "9 celestial symbols" with "9 signs" in Components
    - No new lore or narrative prose beyond what the original SYZYGY rulebook contained
    - _Requirements: 8.1, 8.2, 8.3, 4.2, 5.1, 5.2, 7.1_

  - [x] 1.2 Write TRIGON setup and turn overview
    - Replace "whoever most recently saw the night sky" with a Nine Signs first-player rule (e.g. "whoever most recently noticed a sign they couldn't explain")
    - Turn overview: confirm no symbol names appear — write unchanged mechanical text
    - No mechanical text changes
    - _Requirements: 3.1, 3.3, 5.1_

  - [x] 1.3 Write TRIGON alignments (capturing) section
    - The capture-event term is "trigon" (lowercase): "that's a *trigon*: you immediately capture all three cards…"
    - No occurrence of "syzygy" anywhere in this section
    - "Star is wild" remains verbatim (Req 1.4)
    - Replace any old icon references with new sign names using the same mechanical examples
    - No changes to alignment rules or capture mechanics
    - _Requirements: 1.4, 8.4, 3.1, 3.2, 5.1_

  - [x] 1.4 Write TRIGON activations intro and the 9 signs table
    - Replace "Every symbol has a requirement…" with "Every sign has a requirement…"
    - Section heading: "The 9 signs"
    - Sort the ability table rows by new pip order: Void(1), Root(2), Wave(3), Flame(4), Eye(5), Mask(6), Key(7), Star(8), Crown(9)
    - Use Nine Signs icons (⚫🌱🌊🔥👁🎭🗝⭐👑)
    - Preserve all requirement and mechanical effect text verbatim from the original SYZYGY rulebook
    - Add one-sentence mnemonic justification per row (from design §2.1)
    - _Requirements: 1.1, 1.5, 3.1, 3.2, 4.3, 5.3, 6.3_

  - [x] 1.5 Write TRIGON chains worked example
    - Write using new sign names for the same mechanical sequence
    - Example chain per design §5.1: Root placed on edge → flip turns a card into Mask → Mask activates (central cross) flipping another card → alignment triggers capture
    - Verify the described chain is mechanically valid under the new pip assignments
    - Preserve the same illustrative structure and formatting as the original
    - _Requirements: 3.1, 3.2, 4.5, 5.1_

  - [x] 1.6 Write TRIGON game end, scoring, edge cases & FAQ
    - "Face-down Void cards count as 1 each" — Void is still the catch-up sign
    - Use new sign names in all edge cases (e.g. "Flame discards an adjacent card, never itself", "Star's extra play…", "Crown's row AND column are both full — choose one line to flip")
    - Preserve all rulings, numeric values, and mechanical text
    - _Requirements: 3.1, 3.2, 3.3, 3.5, 4.5, 5.1_

  - [x] 1.7 Write TRIGON strategy notes
    - Use Nine Signs names throughout (e.g. "Stars are double-edged" — Star is still wild)
    - Preserve sentence structure, tone, and strategic content from original
    - _Requirements: 4.6, 5.1, 5.2_

  - [x] 1.8 Write TRIGON card manifest
    - Use all 9 Nine Signs icons/names
    - Maintain the same 36-pair structure (complete graph K₉)
    - _Requirements: 3.4, 4.4_

  - [x] 1.9 Write TRIGON designer's variants
    - "Calm Skies" → **"Calm Signs"**: Star is not wild. Slower captures, gentler pace.
    - "Deep Space" → **"Deep Signs"**: Key may only swap itself with another card. More positional.
    - No celestial terminology in variant names or descriptions
    - Preserve mechanical text verbatim
    - _Requirements: 8.6, 3.6, 5.1_

  - [x] 1.10 Write TRIGON sibling reference and design version note
    - Sibling reference: "A sibling to TURNCOAT: same deck architecture, opposite soul."
    - Design version note: "Design v1.2 — rules balanced over ~23,000 simulated games."
    - Game name in surrounding text is TRIGON (not SYZYGY)
    - _Requirements: 8.5, 5.4_

- [x] 2. Checkpoint — TRIGON review
  - Ensure all sections are present and complete. Verify no occurrence of "SYZYGY", "syzygy", "celestial", "Calm Skies", "Deep Space", or old celestial names (Sun, Moon, Comet, Eclipse, Aurora, Meteor, Nova) anywhere in the file. Verify the capture-event term is "trigon" (lowercase). Verify ability table is sorted pip 1–9. Ask the user if questions arise.

- [x] 3. Rewrite TURNCOAT rulebook (in place: `Turncoat/TURNCOAT_rulebook.md`)
  - [x] 3.1 Rewrite TURNCOAT title, intro paragraph, and components section
    - Replace guild/court/intrigue flavour with Nine Signs flavour
    - Keep the double-allegiance / defection theme but frame agents as "bearing signs" rather than "serving guilds"
    - Replace "9 guild symbols" with "9 signs" in Components
    - Ensure no new narrative prose beyond what exists
    - _Requirements: 4.2, 5.1, 5.2, 7.1_

  - [x] 3.2 Rewrite TURNCOAT setup — "Claim your signs"
    - Rename heading from "Claim your guilds" to "Claim your signs"
    - Replace "guild symbols" → "signs", "unclaimed guild is unaligned" → "unclaimed sign is unaligned"
    - Replace first-player rule with a Nine Signs equivalent
    - Preserve all mechanical setup rules (snake-draft order, player counts, grid size)
    - _Requirements: 3.1, 3.3, 5.1_

  - [x] 3.3 Rewrite TURNCOAT "Your turn" and "Agents, allegiance, and flipping" sections
    - Replace "guild" → "sign" in extraction/banking references
    - Replace "guild on its showing face" → "sign on its showing face"
    - "Its allegiance is the sign on its showing face: yours, a rival's, or unaligned."
    - Preserve all mechanical text about covering, extraction, and score piles
    - _Requirements: 3.1, 3.2, 5.1, 7.1_

  - [x] 3.4 Rewrite TURNCOAT activations intro and the 9 signs table
    - Replace "Every guild has a requirement…" with "Every sign has a requirement…"
    - Rename section heading from "The 9 guilds" to "The 9 signs"
    - Re-sort the ability table rows by new pip order: Void(1), Root(2), Wave(3), Flame(4), Eye(5), Mask(6), Key(7), Star(8), Crown(9)
    - Replace all old guild names/icons with Nine Signs equivalents
    - Preserve all requirement and mechanical effect text verbatim
    - Add one-sentence mnemonic justification per row (from design §2.2)
    - _Requirements: 1.1, 1.5, 3.1, 3.2, 4.3, 5.3, 6.3_

  - [x] 3.5 Rewrite TURNCOAT chains worked example
    - Rewrite using new sign names for the same mechanical sequence
    - Example chain per design §5.2: Eye beside lone rival Mask → activate Eye, peek + flip → reveals Key of yours → Key's column has another ally → activate Key, extract → post empties next to Wave → Wave drags and flips
    - Verify the described chain is mechanically valid under the new pip assignments
    - _Requirements: 3.1, 3.2, 4.5, 5.1_

  - [x] 3.6 Rewrite TURNCOAT game end, scoring, edge cases & FAQ
    - Replace "your guilds" → "your signs" in scoring rules
    - Replace all old guild names in edge cases ("Star's extra card — full rules?", "Who can activate Crown?", "Void with the scores level?")
    - Preserve all rulings, numeric values, and mechanical text
    - _Requirements: 3.1, 3.2, 3.3, 3.5, 5.1_

  - [x] 3.7 Rewrite TURNCOAT strategy notes
    - Replace guild names (e.g. "Watch the Void gap" — was "Ash gap")
    - Preserve sentence structure, tone, and strategic content
    - _Requirements: 4.6, 5.1, 5.2_

  - [x] 3.8 Rewrite TURNCOAT first-game preset teams
    - Replace old guild icons/names with Nine Signs equivalents
    - Use mapping from design §9.6: 2P teams (🔥⭐🌱🌊 vs 🎭👁👑⚫, unaligned 🗝), 3P, 4P
    - Preserve the same ability groupings (balance unchanged)
    - _Requirements: 3.1, 3.3, 6.2_

  - [x] 3.9 Rewrite TURNCOAT card manifest
    - Replace all 9 old guild icons/names with Nine Signs equivalents
    - Maintain the same 36-pair structure (complete graph K₉)
    - _Requirements: 3.4, 4.4_

  - [x] 3.10 Rewrite TURNCOAT designer's variants and sibling reference
    - "Loyalists: you may only activate agents of your own signs" — update "guilds" → "signs"
    - "Bounty: covering an unaligned agent banks it to you" — check for guild references
    - Sibling reference: "A sibling to TRIGON: same deck architecture, opposite soul." (was "A sibling to SYZYGY")
    - Preserve mechanical text; update design version note
    - _Requirements: 3.6, 5.1, 8.5, 9.6_

- [x] 4. Checkpoint — TURNCOAT review
  - Ensure all sections are present and complete. Verify no old guild names remain (search for Blade, Whisper, Coin, Veil, Hound, Ash). Verify no "SYZYGY" references remain. Verify ability table is sorted pip 1–9. Verify sibling line says TRIGON. Ask the user if questions arise.

- [x] 5. Archive operations
  - [x] 5.1 Add archive notice to `Syzygy/SYZYGY_rulebook.md`
    - Prepend the following notice above the existing `# SYZYGY` heading (no other changes to the file):
    ```
    > **⚠️ ARCHIVED** — This game has been renamed to **TRIGON** as part of the Nine Signs retheme.
    > The live rulebook is at [`Trigon/TRIGON_rulebook.md`](../Trigon/TRIGON_rulebook.md).
    > This file is retained as a read-only design record of the pre-rename version.
    ```
    - Do NOT modify any other content in `Syzygy/SYZYGY_rulebook.md`
    - _Requirements: 9.3, 9.4_

- [x] 6. Cross-reference updates
  - [x] 6.1 Update COLLECTION_OVERVIEW.md
    - Replace all "SYZYGY" → "TRIGON" and "Syzygy/" → "Trigon/" throughout
    - Update play-order position 2 to show TRIGON
    - Update all coverage tables, selector tables, genre/mood tables
    - Add a note that Syzygy/ is retained as archive
    - _Requirements: 10.1, 10.2, 10.4, 10.5_

  - [x] 6.2 Update SYMBOL_SETS.md
    - Replace live-game references "SYZYGY" → "TRIGON"
    - In sensitivity tiers and fit matrices, update game name to TRIGON
    - Historical discussion of the celestial skin (Set A) may retain "SYZYGY" with parenthetical: "(now TRIGON)"
    - _Requirements: 10.3_

  - [x] 6.3 Update NEW_GAME_CONCEPTS.md, DECK_SIZE_DECISION.md, flip_card_project_goals.md, COLLECTION_AUDIT.md
    - Replace live-game references "SYZYGY" → "TRIGON" in each file
    - Folder paths "Syzygy/" → "Trigon/" where they appear
    - Historical/analytical references may keep old name with parenthetical "(now TRIGON)"
    - _Requirements: 10.3_

  - [x] 6.4 Update steering files
    - `.kiro/steering/product-vision.md`: Replace "SYZYGY" with "TRIGON" in tier-1 list and collection identity
    - `.kiro/steering/deck-structure.md`: Replace "SYZYGY" in structural properties table and role symbols section
    - `.kiro/steering/design-principles.md`: Replace "SYZYGY" in lessons-learned section
    - `.kiro/steering/repository-structure.md`: Replace "SYZYGY" in naming convention examples
    - `.kiro/steering/playtesting.md`: Replace "SYZYGY" if present in test-focus discussions
    - _Requirements: 10.6_

- [x] 7. Final verification pass
  - [x] 7.1 Old name leak check — full repository
    - Search TRIGON_rulebook.md for: "SYZYGY", "syzygy", "celestial", "Sun" (as ability), "Moon" (as ability), "Comet", "Eclipse", "Aurora", "Meteor", "Nova", "Calm Skies", "Deep Space"
    - Search TURNCOAT_rulebook.md for: "SYZYGY", "Blade", "Whisper", "Coin", "Veil", "Hound", "Ash", "guild" (except "unaligned" context if applicable — per Req 7.1 it should not be)
    - Search cross-reference docs for any remaining live-game "SYZYGY" references (historical parenthetical usages are permitted)
    - Fix any leaks found
    - _Requirements: 4.2, 4.3, 7.1, 10.3, 10.6 · Properties 6, 9, 10_

  - [x] 7.2 Mechanical drift check — both rulebooks
    - For each ability in both games, compare requirement text and effect text against the originals
    - Confirm only the symbol-name column changed; all mechanics, numbers, and edge-case rulings are identical
    - Confirm numeric values (player counts, grid dimensions, turn counts, scoring, tiebreakers) are unchanged
    - _Requirements: 3.1, 3.2, 3.3 · Properties 3, 4_

  - [x] 7.3 Structural completeness and pip-order check
    - Verify both rulebooks contain all original sections (intro, components, setup, turn overview, mechanism explanation, ability table, chains example, game end/scoring, edge cases/FAQ, strategy notes, card manifest, designer's variants, sibling reference, design version note)
    - Verify ability tables are sorted ascending by pip 1–9
    - Verify card manifests contain exactly 36 pairs forming K₉
    - Verify TRIGON sibling line references TURNCOAT; TURNCOAT sibling line references TRIGON
    - _Requirements: 4.1, 6.3, 8.5, 9.6 · Properties 5, 7, 8, 11_

  - [x] 7.4 Rename-specific verification
    - Confirm "trigon" (lowercase) is used as the capture-event term in TRIGON_rulebook.md
    - Confirm no pronunciation guide exists in TRIGON_rulebook.md
    - Confirm variant names are "Calm Signs" and "Deep Signs" (not "Calm Skies" / "Deep Space")
    - Confirm Trigon/ folder exists with TRIGON_rulebook.md
    - Confirm Syzygy/SYZYGY_rulebook.md has archive notice and is otherwise unmodified
    - _Requirements: 8.3, 8.4, 8.6, 9.1, 9.2, 9.3, 9.4 · Properties 9, 12_

- [x] 8. Final checkpoint
  - Ensure all verification checks pass. Both rulebooks are complete standalone documents. Cross-references are consistent. Archive is in place. Ask the user if questions arise.

## Notes

- This is a document-writing task, not a code task. Each "implementation" step is a rulebook section write/rewrite.
- The TRIGON rulebook is a **new file** in a new `Trigon/` folder — it is not a copy-edit of the old SYZYGY rulebook. Write it fresh using the original as a structural reference.
- The TURNCOAT rulebook is **modified in place** in the existing `Turncoat/` folder.
- The sign-to-ability mapping in design.md §2 is the single source of truth for all name substitutions.
- The old-to-new lookup tables in design.md §10 provide the quick-reference for each substitution.
- The transformation checklist in design.md §5 was used to derive these tasks.
- Mechanical text (requirements, effects, numbers) must never change — only names and flavour.
- Mnemonic justifications are one sentence max, in the same functional register as the originals.
- "Star is wild" must remain verbatim in TRIGON (Requirement 1.4).
- The capture-event term is "trigon" (lowercase) — not "syzygy."
- Variant renames: "Calm Skies" → "Calm Signs", "Deep Space" → "Deep Signs."
- The intro paragraph removes the pronunciation guide and uses "convergence of signs" framing.
- Checkpoints ensure incremental validation before moving to the next phase.
- Tasks marked with `*` are optional and can be skipped for faster MVP — none present in this plan (all tasks are required for a complete retheme).

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1", "1.2"] },
    { "id": 1, "tasks": ["1.3", "1.4"] },
    { "id": 2, "tasks": ["1.5", "1.6", "1.7"] },
    { "id": 3, "tasks": ["1.8", "1.9", "1.10"] },
    { "id": 4, "tasks": ["3.1", "3.2"] },
    { "id": 5, "tasks": ["3.3", "3.4"] },
    { "id": 6, "tasks": ["3.5", "3.6", "3.7"] },
    { "id": 7, "tasks": ["3.8", "3.9", "3.10"] },
    { "id": 8, "tasks": ["5.1"] },
    { "id": 9, "tasks": ["6.1", "6.2", "6.3", "6.4"] },
    { "id": 10, "tasks": ["7.1", "7.2", "7.3", "7.4"] }
  ]
}
```
