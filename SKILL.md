---
name: buidlguidl-devcon8-slides
description: Build a talk deck in the BuidlGuidl slide kit for the Devcon 8 community-led day (Builder Enablement & BuidlGuidl track). Use when a speaker asks for Devcon slides, a BuidlGuidl deck, or to restyle an existing deck into this kit. The deck is built as HTML in the kit and exported as pictures into the speaker's Devcon Google Slides deck.
---

# BuidlGuidl Devcon 8 slide kit

Several speakers present back to back and every deck must look like one family. The kit does that with one rule:

**We lock the frame, you own the content.**

Locked (same for everyone, never redrawn or recoloured): the four background images, the logo baked into them, the fonts, the colours, the type scale, the margins, the title slide, the closing slide and the "up next" slide. Yours: what goes on content slides, which layouts you use, and in which order.

Devcon gives every session its own Google Slides deck, and that deck plays on stage. Google Slides cannot show the heading font as live text, so the deliverable is pictures: you build the deck as HTML in the kit, `build/export.sh` renders one PNG per slide and wraps them in a pptx with speaker notes, and the speaker imports that pptx into their Devcon deck. Every slide arrives pixel-identical, font included.

The kit lives at https://github.com/technophile-04/devcon-8-mumbai (clone it; the demo deck is served at https://technophile-04.github.io/devcon-8-mumbai/reference/deck.html). Reference renders of every layout are in `reference/slides/` and `reference/contact-sheet.png`. Build to match them.

## Files

| Path | What it is |
| --- | --- |
| `backgrounds/cover.png` | title, closing, up next. Sky gradient, the illustrated town, ink logo top-left |
| `backgrounds/section.png` | section dividers. Painted clouds, ink logo top-left |
| `backgrounds/content.png` | content slides. Paper ground, small ink logo bottom-left |
| `backgrounds/content-dark.png` | code and terminal slides. Ink ground, small white logo bottom-left |
| `fonts/` | PP Neue Machina Inktrap Semibold (otf, woff2), licensed to BuidlGuidl |
| `logos/` | the logo as SVG and 2x PNG, ink and white. Already baked into the backgrounds; only for a one-off need |
| `reference/deck.html` | every layout as a 1920x1080 slide with sample content. Copy it to `decks/<talk-slug>.html` and build there |
| `template/buidlguidl-devcon8.pptx` | 13.333x7.5 in, one layout per slide type, example slides. The hand-build option, in Keynote |
| `build/export.sh` | turns a deck into the PNGs, the `-google-slides.pptx` and the PDF. Always the last step |
| `build/` | scripts that regenerate backgrounds, renders and the pptx template |

## Canvas and units

Canvas is 1920x1080 px. Every number in this file is px on that canvas.

- PowerPoint and Keynote widescreen (13.333x7.5 in): pt = px / 2.
- Google Slides default (10x5.625 in): pt = px x 0.375.
- EMU in the pptx: px x 6350.

Margins: 120 left and right, 96 top and bottom. Nothing readable sits outside them. The content area is x 120 to 1800, y 96 to 984. The logo lives inside the margin band and is part of the background.

## Colours

| Token | Hex | Use |
| --- | --- | --- |
| ink | #182232 | all text on light grounds, arrows, the dark ground |
| paper | #FFFCFC | text on the dark ground, content ground |
| grey | #F4F4F4 | neutral cards |
| lavender | #D8DCFF | panels, diagram boxes |
| peach | #FFD4B5 | panels, diagram boxes |
| pale lime | #EAFFA9 | panels, diagram boxes |
| periwinkle | #808CFF | bullets, the quote bar, number pills |
| periwinkle light | #9FA9FF | prompt glyphs and labels on the dark ground |
| orange | #FF6E1D | number pills, with ink text |
| lime | #B5DC3A | the highlight marker, always with ink text |

Lime and periwinkle are fills, never text colours. Text is ink, or paper on the dark ground. No gradients except the art in the backgrounds. No shadows.

## Fonts

| Role | Font | Where it comes from |
| --- | --- | --- |
| display, cover title, heading, quote | PP Neue Machina Inktrap Semibold | `fonts/`, `@font-face` in HTML, installed on the machine for Keynote and PowerPoint |
| body, labels | Space Grotesk, Regular and Medium (Bold in pptx, Office has no 500) | Google Fonts |
| code | Space Mono Regular | Google Fonts |

There is no fallback in what the audience sees. Slides reach Google Slides as pictures, and `build/export.sh` refuses to export a deck whose render did not load Machina, Space Grotesk and Space Mono.

Machina is wider than Space Grotesk. Size titles for Machina and check line breaks in every render. In the pptx the heading typeface string is `PP Neue Machina Inktrap Smbold` (the font's Office family name). Keynote lists the same font as family "PP Neue Machina", style "Inktrap Semibold"; if Keynote shows a substitute, use Format > Font > Replace Fonts.

HTML head:

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
@font-face { font-family: "PP Neue Machina"; src: url("../fonts/PPNeueMachina-InktrapSemibold.woff2") format("woff2"); font-weight: 600; }
</style>
```

## Type scale

| Style | Size | Line height | Font | Where |
| --- | --- | --- | --- | --- |
| display | 120 | 126 | Machina | statement, section title |
| cover title | 96 | 101 | Machina | title, closing, up next (the clear-sky column is 840 wide; 120 does not fit a normal title there) |
| heading | 80 | 88 | Machina | every content heading |
| quote | 80 | 92 | Machina | the quote slide |
| body | 48 | 62 | Space Grotesk | everything the audience must read |
| code | 44 | 64 | Space Mono | code and terminal lines |
| label | 36 | 47 | Space Grotesk Medium | eyebrows, credits, part numbers, captions under diagram boxes. Never for a point you are making |

Devcon asks for body text of at least 24 pt, which is 48 px here. Letter-spacing on Machina is -0.01em.

## The highlight

At most one highlighted phrase per slide: a lime #B5DC3A marker behind ink text, like the lime button on buidlguidl.com. The marker extends 0.08em beyond the words on each side with 0.14em corner radius.

- HTML: `<mark>` with the CSS from `reference/deck.html`.
- PowerPoint: Text Highlight Color set to #B5DC3A on the words.
- Keynote: it drops imported highlights, so draw a lime rounded rectangle, send it behind the text, and size it to the words. The example slides in the pptx use that shape so they survive every app.

Never highlight a whole line, a heading, or more than one phrase.

## Backgrounds: what is baked and what is clear

- `cover.png`: logo at (120, 96), 64 tall. Clear sky from y 200 to about 740 within x 120 to 960. The town's line art starts at y 745 on the far left, y 545 past x 960, y 275 past x 1800. Keep every word inside the clear column.
- `section.png`: logo at (120, 96), 64 tall. Title zone x 120 to 1120; the pale lime left side gives ink the best contrast.
- `content.png` and `content-dark.png`: logo at (120, 1014), 36 tall, inside the bottom margin. The whole content area is free.

Never place a second logo, recolour a background, or crop one. Export at exactly 1920x1080.

## Layouts

Positions are (x, y, width, height). A text box anchors at its top-left and wraps inside its width. The pptx layout name is in brackets.

### 1. Title [Title], cover.png

- event line: (120, 200, 1000, 47) label. The text is the token `EVENT_LINE` below.
- talk title: (120, 280, 840, 310) cover title, up to three lines
- speaker name: (120, 624, 900, 62) body medium
- role or handle: (120, 688, 900, 47) label, e.g. `BuidlGuidl · @handle`

The title slide is the first frame of the YouTube recording. No extra decoration.

### 2. Statement [Statement], content.png

- statement: (120, 300, 1680, 400) display, up to three lines, one `<mark>`
- sub-line: (120, 760, 1680, 62) body, optional

### 3. Heading + body [Heading + body], content.png

- heading: (120, 96, 1680, 176) heading, one or two lines
- body: (120, 320, 1680, 664) body. Short lines, at most four. Bullets are 18 px periwinkle dots, 32 px between items, text starts 64 px in.

### 4. Heading + image [Heading + image], content.png

- heading: (120, 96, 1680, 96) heading, one line
- panel: (120, 232, 1680, 752) lavender, radius 32
- image: inside the panel with 40 px padding, at its natural aspect, corners radius 24. Never crop a screenshot to fill. In PowerPoint, after inserting into the picture placeholder use Crop > Fit.

### 5. Three columns [Three columns], content.png

- heading: (120, 96, 1680, 96)
- cards: x 120, 696, 1272, each (528 wide, y 260, 520 tall), grey, radius 32, padding 48
- pill: (card x + 48, 308, 96, 64), fully round, label text 01 02 03 centred; fills periwinkle, orange, lime
- card title: (card x + 48, 404, 432, 120) body medium
- card text: (card x + 48, 544, 432, 200) body, one or two short lines

### 6. Section [Section], section.png

- part number: (120, 392, 1000, 47) label, e.g. `Part 2`
- part title: (120, 456, 1000, 380) display, up to three lines

### 7. Code [Code], content-dark.png

- heading: (120, 96, 1680, 96) heading, paper
- label: (120, 256, 1680, 47) label, periwinkle light, e.g. `terminal`
- code: (120, 320, 1680, 640) code, paper, up to ten lines. Prompt glyphs (`$`, `?`) in periwinkle light. No syntax colouring beyond that.

### 8. Quote [Quote], content.png

- quote: (120, 240, 1560, 330) quote style, up to three lines, in quotation marks
- bar: (120, 600, 60, 6) periwinkle
- author: (120, 640, 1200, 62) body medium
- source: (120, 704, 1200, 47) label

A post screenshot replaces the quote text: put it at natural aspect inside (120, 240, 1560, 330) with radius 24, keep the bar and author.

### 9. Diagram [Diagram], content.png

- heading: (120, 96, 1680, 96)
- boxes: 520x260, radius 32, flat fills in order lavender, peach, pale lime, grey; text body medium, left-aligned, vertically centred, 40 px padding
- three in a row: x 120, 700, 1280 at y 400. Arrows in the 60 px gaps: ink, 4 px line, triangle head, at y 530
- caption under each box: (box x, 692, 520, 100) label; code identifiers in Space Mono 36

More than four boxes, or two rows, means two slides. No shadows, no outlines, no diagonal arrows.

### 10. Closing [Closing], cover.png

- event line: same box as the title slide, token `EVENT_LINE`
- thanks: (120, 280, 840, 110) cover title
- speaker name: (120, 440, 880, 62) body medium
- handles: (120, 504, 880, 62) body, e.g. `@handle on X and GitHub`
- link: (120, 584, 880, 62) body, this slide's one highlight

No QR code (Devcon rule below).

### 11. Up next [Up next], cover.png

For the host between talks.

- eyebrow: (120, 200, 1000, 47) label, fixed text `Up next`
- talk title: (120, 280, 840, 310) cover title
- speaker: (120, 624, 900, 62) body medium, e.g. `Shiv Bhonde, BuidlGuidl`
- time and room: (120, 688, 900, 62) body, e.g. `13:15 · Workshop 1`

## The event line token

```
EVENT_LINE = "Devcon 8 · Builder Enablement & BuidlGuidl"
```

It is a constant at the bottom of `reference/deck.html` and a fixed text box named `EVENT_LINE` on the Title and Closing layouts of the pptx (edit it in Slide Master view once and every cover slide follows). Change it only if the track name changes.

## Building the deck

**HTML deck, then export (Claude Code, Codex, any agent).** Copy `reference/deck.html` to `decks/<talk-slug>.html` inside the kit (same depth as `reference/`, so its `../backgrounds/` and `../fonts/` paths keep working), keep its CSS, delete the sample slides you do not need and duplicate the ones you do. Each slide is a `<section class="slide ...">` at 1920x1080 with the background as `background-image`; slide order is document order, and `?slide=N` shows the Nth one. Speaker notes go in an `<aside class="notes">` inside the section: hidden in renders, copied into the pptx speaker notes by the export (slides 1 and 10 of the reference deck show it). The last step is always the export:

```
build/export.sh decks/<talk-slug>.html
```

It renders every slide with Chrome headless the way `build/render.sh` does, refuses if Machina, Space Grotesk or Space Mono did not load (`document.body.dataset.fonts`), and writes next to the deck: `decks/<talk-slug>-slides/NN-name.png`, `decks/<talk-slug>-google-slides.pptx` (one full-bleed picture per slide at 10x5.625 in, Devcon's deck size, with the notes) and `decks/<talk-slug>.pdf` (laptop backup). The speaker imports the pptx into their Devcon Google Slides deck (README, step 3). Hand over all three, and run the self-check on the exported PNGs.

**By hand in Keynote.** Install the font from `fonts/`, open `template/buidlguidl-devcon8.pptx`, duplicate an example slide or add one from its layout (the layouts carry the backgrounds and the type), export the slides as 1920x1080 images, then `build/export.sh <that folder>` makes the same pptx and PDF, without notes. Keep the 13.333x7.5 in size Keynote reports as 960x540 pt.

**Google Slides.** Never build natively in Google Slides: it has no Machina, so the headings lose the font. Import the exported pptx instead.

## Content rules

- One idea per slide. If a slide needs a second heading, it is two slides.
- Short text. A body slide carries at most four lines; a statement is one sentence.
- No walls of bullets. Prefer a statement, a diagram, a screenshot or a code block over a list.
- Code slides show at most ten lines, the ones you will talk about.
- Images and screenshots sit in a rounded panel, at natural aspect, never stretched.
- Numbers you show must be ones you can source in the talk.
- No emoji, no clip art, no stock photos, no drop shadows, no centred paragraphs.

## Devcon rules (speaker guidelines 2026)

- Sessions are recorded and streamed to YouTube. The title slide is the recording's first frame; the closing slide is its last.
- No QR codes or links that let people buy or use crypto products that are not compliant with Indian law (§8). The kit has no QR code slot on purpose.
- Do not call digital assets "currency", "securities", "custodian" or "depositories" (§11b). Say token, asset, wallet, protocol.
- Body text at least 24 pt (48 px here).
- Source: https://devcon.org/Devcon8-Speaker-Guidelines-2026.pdf

## Self-check before handing over

Look at every exported PNG in `decks/<talk-slug>-slides/` (1920x1080) one by one.

1. Every word sits inside the margins: x 120 to 1800, y 96 to 984.
2. Nothing overflows its box. Three-line titles stay in their three lines; long words did not break mid-word.
3. No text sits on line art. On cover slides every word is in the clear column.
4. Sizes are on the scale: nothing the audience must read is below 48 px, labels 36, code 44.
5. Headings are Machina. Body is Space Grotesk, code is Space Mono, nothing else.
6. At most one lime highlight per slide, ink text on it.
7. Backgrounds untouched: no second logo, no recolour, no crop, no overlay.
8. Title, closing and up-next slides use the cover layout and the event line token.
9. Colours come from the table above; no gradients, no shadows, no emoji.
10. No QR code and none of the §11b words.
