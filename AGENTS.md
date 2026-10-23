# BuidlGuidl Devcon 8 slide kit

Several speakers present back to back on BuidlGuidl's community day at Devcon 8, and every deck must look like one family. The kit does that with one rule:

**The frame is locked. The content is yours.**

The frame is the four backgrounds with the BuidlGuidl marks baked in, the fonts, the colours, the type scale, the margins, and the title and closing slides. The content is what goes on the slides in between, which layouts you use, and in which order.

The kit lives at https://github.com/technophile-04/devcon-8-mumbai. The reference deck `reference/deck.html`, served at https://technophile-04.github.io/devcon-8-mumbai/reference/deck.html, shows every layout with sample content, and `reference/slides/*.png` plus `reference/contact-sheet.png` are its renders. They are the visual truth: in any format, build to match them. Every colour, font, type style, radius and margin is a token in `design/tokens.json`; take values from there, never from memory.

## Steps

### 1. Choose the format

The speaker's stated format wins. Otherwise pick the one that fits how they will present, and open its recipe:

| Format | Pick it when | Recipe |
| --- | --- | --- |
| pptx | the default. It opens in PowerPoint, Keynote and Google Slides, and the speaker can still edit it | [recipes/pptx.md](recipes/pptx.md) |
| Google Slides | the speaker works in Google Slides or presents from Devcon's Slides link | [recipes/google-slides.md](recipes/google-slides.md) |
| HTML | the speaker presents from a browser on their own laptop, or wants live embeds | [recipes/html.md](recipes/html.md) |

Any other format, such as Keynote native, Reveal, Slidev or Figma, uses the same tokens, backgrounds and positions from the reference below, with `reference/slides/*.png` as the visual truth.

Fonts in every format are Space Grotesk and Space Mono, shipped in `fonts/` with their licenses. Google Slides has them built in. PowerPoint and Keynote need them installed on the presenting laptop. HTML loads them from Google Fonts, or from `fonts/fonts.css` when the deck is shown offline. `fonts/README.md` has the steps.

Done when you have named the format and read its recipe.

### 2. Build

1. Plan the slides: Title first, Closing last, content slides in between from the layouts below, in any order. Up next is the host's slide between talks; add it only when asked.
2. Write the words under Content rules and Devcon rules before placing them.
3. Build with the recipe and save under `decks/<talk-slug>.<ext>` inside the kit. Every element sits in a slot of its layout at the position given below; the recipe says how to place it in that format.

Done when the file opens, Title is the first slide, Closing is the last, and every slide uses one of the eleven layouts.

### 3. Self-check

Look at every slide as a 1920x1080 image; the recipe says how. On each slide confirm:

1. Every word sits inside the margins, x 120 to 1800, y 96 to 984. The highlight marker and an opening quotation mark may hang a few px into the margin.
2. Nothing overflows its box. Three-line titles stay in three lines, and no word broke mid-word.
3. No text sits on line art. On cover slides every word is in the open sky, the title ends at y 440, and the speaker block sits below it with a clear gap.
4. Every text is one of the type tokens at its size: body or larger for anything the audience must read, label and tag only for credits, part numbers, captions, handles and corner tags, code for code.
5. The fonts on the slide are the token families, Space Grotesk and Space Mono, with no fallback font standing in.
6. At most one lime highlight, with ink text on it.
7. The frame is untouched: one set of marks, no recolour, no crop, no overlay.
8. Title and Closing use the cover layouts with the event line in the corner.
9. Every colour is a colour token, as a flat fill. No gradients, no shadows, no emoji.
10. No QR code and none of the words listed under Devcon rules.

Done when every slide has passed all ten checks and the speaker has the file path.

## Reference

### Files

| Path | What it is |
| --- | --- |
| `backgrounds/cover.png` | title, closing, up next. Sky gradient, the illustrated town, ink wordmark top-left |
| `backgrounds/section.png` | section dividers. Painted clouds, ink wordmark top-left |
| `backgrounds/content.png` | content slides. Periwinkle-white ground, ink castle mark top-left and a "Devcon 8" tag top-right |
| `backgrounds/content-dark.png` | code and terminal slides. Ink ground, the same marks in white |
| `logos/` | the wordmark and the castle mark as SVG and 2x PNG, ink and white. Already baked into the backgrounds; only for a one-off need |
| `design/tokens.json` | every colour, font, type style, radius, margin and mark size, with its use. The single source of truth, in the W3C Design Tokens format |
| `design/tokens.css` | the same tokens as CSS custom properties, generated. `reference/deck.html` loads it |
| `design/style-sheet.html` | every token rendered on one page, generated; `design/style-sheet.png` is its render and https://technophile-04.github.io/devcon-8-mumbai/design/style-sheet.html serves it |
| `fonts/` | Space Grotesk and Space Mono with their licenses, `fonts.css` to load them offline, and a readme on installing them |
| `reference/deck.html` | every layout as a 1920x1080 slide with sample content; `?slide=N` shows the Nth slide alone |
| `template/buidlguidl-devcon8.pptx` | the layouts as a pptx template, see recipes/pptx.md |
| `recipes/` | one file per format: pptx, Google Slides, HTML |
| `build/` | maintainer scripts that regenerate everything from the tokens: CSS, backgrounds, renders, style sheet and the pptx |

### Canvas and units

The canvas is 1920x1080 px (the `canvas` tokens), and every number in this file is px on it. Tools that measure in pt use pt = px x 0.375, so the slide is 10 x 5.625 in.

Margins are 120 left and right, 96 top and bottom (the `space` tokens). Nothing readable sits outside them. The content area is x 120 to 1800, y 96 to 984; content headings start at y 120 to leave room under the corner marks. The marks sit inside the margin bands and are part of the background.

### Tokens

`design/tokens.json` is where every value lives: the colours with their use, the two font families and three weights, a type token per role (size, line height, weight, where it goes), the radii, the margins, the canvas, the mark sizes and the highlight marker. Read it before you place anything. The names below, like `lime`, `body medium` or `panel radius`, are its token names. `design/style-sheet.png` shows them all rendered.

Rules the tokens do not carry:

- Lime and periwinkle are fills; text is ink, or paper on the dark ground. Fills are flat. The only gradients are the art in the backgrounds.
- Body is the floor: nothing the audience must read goes smaller. Label and tag are for credits, part numbers, captions, handles and corner tags, never for a point you are making.
- A cover title that needs three lines drops to `cover-title-long` so it stays in its box and clear of the wordmark.

### The highlight

At most one highlighted phrase per slide: a lime marker behind ink text, like the lime button on buidlguidl.com. The `highlight` tokens give how far it extends past the words and its corner radius, in em of the text. It marks a phrase, so a whole line or a heading stays plain. Put it mid-line where you can: a marker at the start of a line hangs into the left margin. Each recipe says how to draw it in its format.

### Backgrounds: what is baked and what is clear

- `cover.png`: wordmark at the margin corner (120, 96). The open sky narrows as the town rises: clear across the full width from y 160 to 300, to x 1450 down to y 430, to x 1000 from y 440 to 760. The title box (to x 1270, ending at y 440) and the speaker block (to x 960, below y 440) sit inside it. Keep every word in the open sky.
- `section.png`: wordmark at the margin corner (120, 96). Title zone x 120 to 1120, where the pale lime left side gives ink the best contrast.
- `content.png` and `content-dark.png`: the castle mark at the left margin and a "Devcon 8" tag ending at the right margin, both inside the top margin band (sizes in the `mark` tokens). The whole content area is free; headings start at y 120.

Use the backgrounds as they are, at exactly 1920x1080, with no second logo on top.

### Layouts

Positions are (x, y, width, height). A text box anchors at its top-left and wraps inside its width. The names are the layout names in every format.

#### 1. Title, on cover.png

Two groups on the left: the title in the open sky above the art, then the speaker block below it with a clear gap. The title box is anchored at its bottom, so a long title grows upward and never reaches the speaker block.

- event line: (720, 104, 1080, 47) tag, right-aligned, on the wordmark's line; the text is `EVENT_LINE` below
- talk title: (120, 188, 1150, 252) cover title, bottom-anchored so the text ends at y 440, two lines. About 45 characters fit, which covers every talk on the day. A title that needs three lines drops to cover-title-long so it stays in the box and clear of the wordmark
- speaker name: (120, 496, 840, 62) body medium
- handle: (120, 560, 840, 47) tag, e.g. `@handle`

The title slide is the first frame of the YouTube recording, so it carries nothing else.

#### 2. Statement, on content.png

- statement: (120, 300, 1680, 400) display, up to three lines, one highlight
- sub-line: (120, 760, 1680, 62) body, optional

#### 3. Heading + body, on content.png

- heading: (120, 120, 1680, 176) heading, one or two lines
- body: (120, 320, 1680, 664) body, short lines, at most four. Bullets are periwinkle dots 18 px wide; text starts 64 px in, with 32 px between items

#### 4. Heading + image, on content.png

- heading: (120, 120, 1680, 96) heading, one line
- panel: (120, 256, 1680, 728) lavender, panel radius
- image: inside the panel with 40 px padding, so within (160, 296, 1600, 648), at its natural aspect, centred, image radius on the corners. A screenshot keeps its aspect, with the lavender panel showing around it

#### 5. Three columns, on content.png

- heading: (120, 120, 1680, 96)
- cards: x 120, 696, 1272, each (528 wide, y 260, 520 tall), paper, panel radius, padding 48
- pill: (card x + 48, 308, 96, 64), fully round, label text 01 02 03 centred; fills periwinkle, orange, lime
- card title: (card x + 48, 404, 432, 120) body medium
- card text: (card x + 48, 544, 432, 200) body, up to three short lines

#### 6. Section, on section.png

- part number: (120, 392, 1000, 47) label, e.g. `Part 2`
- part title: (120, 456, 1000, 380) display, up to three lines

#### 7. Code, on content-dark.png

- heading: (120, 120, 1680, 96) heading, paper
- label: (120, 256, 1680, 47) label, periwinkle light, e.g. `terminal`
- code: (120, 320, 1680, 640) code, paper, up to ten lines. Prompt glyphs (`$`, `?`) are periwinkle light; everything else stays paper, with no further syntax colouring

#### 8. Quote, on content.png

- quote: (120, 240, 1560, 330) quote style, up to three lines, in curly quotation marks
- bar: (120, 600, 60, 6) periwinkle
- author: (120, 640, 1200, 62) body medium
- source: (120, 704, 1200, 47) label

Attribute only what the speaker attributed. A quote with no known author keeps the bar and leaves author and source empty.

A post screenshot replaces the quote text: put it at natural aspect inside (120, 240, 1560, 330) with the image radius, and keep the bar and author.

#### 9. Diagram, on content.png

- heading: (120, 120, 1680, 96)
- boxes: 520x260, panel radius, flat fills in order lavender, peach, pale lime, paper; text body medium, left-aligned, vertically centred, 40 px padding
- three in a row: x 120, 700, 1280 at y 400. Arrows in the 60 px gaps: ink, 4 px line, triangle head, horizontal at y 530
- caption under each box: (box x, 692, 520, 100) label; code identifiers in the tag style

More than four boxes, or two rows, means two slides. Boxes have flat fills without outlines, and arrows run straight.

#### 10. Closing, on cover.png

Same positions as the title slide: Thanks on the title line, the speaker block below it, then the link.

- event line: (720, 104, 1080, 47) tag, right-aligned, `EVENT_LINE`
- thanks: (120, 188, 1150, 252) cover title, bottom-anchored so the text ends at y 440
- speaker name: (120, 496, 840, 62) body medium
- handles: (120, 560, 840, 47) tag, e.g. `@handle on X and GitHub`
- link: (120, 656, 840, 62) body, this slide's one highlight. The speaker's link, or `buidlguidl.com` when they gave none

The link is typed, with no QR code (Devcon rules below).

#### 11. Up next, on cover.png

For the host between talks: the title slide's positions with `Up next` in the corner and the time and room where the handle goes.

- corner tag: (720, 104, 1080, 47) tag, right-aligned, the text `Up next`
- talk title: (120, 188, 1150, 252) cover title, bottom-anchored
- speaker: (120, 496, 840, 62) body medium, e.g. `Your Name`
- time and room: (120, 560, 840, 47) tag, e.g. `13:15 · Workshop 1`

### The event line

```
EVENT_LINE = "Devcon 8 · Builder Enablement & BuidlGuidl"
```

It fills the corner tag of the Title and Closing slides. Change it only if the track name changes: it is a text box named `EVENT_LINE` on the Title and Closing layouts of the pptx and a constant at the bottom of `reference/deck.html`.

### Content rules

- One idea per slide. A slide that needs a second heading is two slides.
- Short text. A body slide carries at most four lines; a statement is one sentence.
- Prefer a statement, a diagram, a screenshot or a code block over a list.
- Code slides show at most ten lines, the ones you will talk about.
- Images and screenshots sit in a rounded panel at natural aspect.
- Numbers you show are ones you can source in the talk.
- Text is left-aligned. No emoji, no clip art, no stock photos, no drop shadows.

### Devcon rules (speaker guidelines 2026)

- Sessions are recorded and streamed to YouTube. The title slide is the recording's first frame; the closing slide is its last.
- No QR codes or links that let people buy or use crypto products that are not compliant with Indian law (§8). The kit has no QR code slot on purpose.
- Do not call digital assets "currency", "securities", "custodian" or "depositories" (§11b). Say token, asset, wallet, protocol.
- Body text at least 24 pt. The body token clears it, so nothing the audience reads goes smaller than body.
- Source: https://devcon.org/Devcon8-Speaker-Guidelines-2026.pdf
