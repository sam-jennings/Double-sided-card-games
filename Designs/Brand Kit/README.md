# Double-Sided — Brand Kit

A small, dependency-free kit for any **digital artifact** built from this
project: a landing page, a web rules sheet, a print-and-play companion, slides,
or a throwaway mockup. No build step, no framework, no JavaScript.

It is the simplified successor to the auto-generated "Design System" — the same
tokens and visual language, distilled into three files you can actually use.

## Files

| File | What it is |
|---|---|
| `double-sided.css` | The whole kit in one file: webfonts, design tokens, and plain CSS component classes. **Link this and you're done.** |
| `glyphs.svg` | An SVG sprite of the nine sign glyphs (geometric placeholders). Recolour with `currentColor`. |
| `starter.html` | A live gallery of everything, doubling as copy-paste source. **Open this in a browser to see the kit.** |

## Quick start

```html
<link rel="stylesheet" href="double-sided.css">
<body class="ds">            <!-- `ds` turns on the base styles -->
  <button class="ds-btn">Play</button>
</body>
```

Open `starter.html` in any browser to see every token and component rendered.
Copy the markup you want straight out of it.

## The two-layer rule (from `deck-structure.md`)

1. **Permanent deck identity** — pip 1–9, sign icon + name, colour, a both-faces-
   identical orientation marker. The kit encodes this: nine hues, nine glyphs,
   the `.ds-playing-card` anatomy (centred identity cluster — value · symbol ·
   name · colour — plus a top-edge orientation chevron, nothing else).
2. **Per-game interpretation** lives in each rulebook, never in the kit.

The card is deliberately minimal: only the elements defined in `CARD_LAYOUT.md`.
Identity is clustered in the **centre** so a hand can cover it whole; the
orientation marker is a small top-edge chevron (not a bar). No sign-coloured
frame (that is an open question in `CARD_LAYOUT.md`), no notch, no inner keyline.

## Signs

Pip order is fixed: **1 Moon · 2 Leaf · 3 Wave · 4 Flame · 5 Eye · 6 Mask ·
7 Key · 8 Star · 9 Crown.** Each has a hue (`--crown`), a soft tint
(`--crown-tint`), and a glyph (`#sign-crown`). Add a `sign-<name>` class to any
element to set its `--sign` / `--sign-tint`:

```html
<span class="ds-pip sign-crown">9</span>
<div class="ds-sign sign-flame"><svg><use href="glyphs.svg#sign-flame"></use></svg></div>
```

Role signs: **Star (8)** is the wild/exception, **Crown (9)** the apex,
**Moon (1)** the outsider.

## Components (CSS classes)

`.ds-btn` (`--gold` `--secondary` `--ghost` `--danger`, `--sm` `--lg`) ·
`.ds-badge` · `.ds-tag` · `.ds-pip` (`--filled`) · `.ds-card` (`--frame`
`--interactive`) · `.ds-input` · `.ds-switch` · `.ds-overlay` + `.ds-dialog` ·
`.ds-sign` (`--ring` `--framed`) · `.ds-playing-card` (`--selected` `--dim`).

Editorial helpers: `.ds-display`, `.ds-overline`, `.ds-mono`, `.ds-game`
(uppercase game titles).

## Voice (for any copy you write)

Precise, structural, a touch mathematical — confident, never hype, no emoji.
Game titles UPPERCASE (TRIGON, THE COUNCIL); sign names Title Case (Moon, Crown).
Lean on meaningful numbers and tight tables. North star: a game that *could only
exist because of this deck*.

## Notes & next steps

- **Glyphs are placeholders** in the spirit of the project's "Set D Glyphs"
  accessibility benchmark. When illustrated card art exists, either drop it into
  an `assets/` folder and point `.ds-playing-card .glyph` at it, or replace the
  paths inside `glyphs.svg`.
- **Fonts** load from Google Fonts; swap to local woff2 for production/offline.
- **`<use href="glyphs.svg#…">`** works on served pages. For `file://` previews,
  inline the sprite (see the top of `starter.html`).
- If a real React/Vue app ever happens, the tokens map over directly — the old
  React components were removed as broken (missing assets) and over-built for
  current needs.
