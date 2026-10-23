---
name: buidlguidl-devcon8-slides
description: Build a talk deck in the BuidlGuidl slide kit for the Devcon 8 community-led day (Builder Enablement & BuidlGuidl track). Use when a speaker asks for Devcon slides, a BuidlGuidl deck, or to restyle an existing deck into this kit. The deliverable is an editable Google Slides deck, built from the kit's pptx template, that ends up in the speaker's Devcon link.
---

# BuidlGuidl Devcon 8 slide kit

Several speakers present back to back and every deck must look like one family. The kit does that with one rule:

**We lock the frame, you own the content.**

Locked (same for everyone, never redrawn or recoloured): the four background images, the BuidlGuidl marks baked into them, the fonts, the colours, the type scale, the margins, the title slide, the closing slide and the "up next" slide. Yours: what goes on content slides, which layouts you use, and in which order.

Devcon gives every session its own Google Slides deck, at a link of the form https://devcon.org/presentation/devcon8/<code>/, and its guidelines say the final deck must live in that link. The deliverable is an editable Google Slides deck that the speaker imports into that link. You build it by filling `template/buidlguidl-devcon8.pptx`; the speaker uploads the result to Google Drive, opens it with Google Slides, and imports it into the Devcon deck (steps at the end of Building the deck). The template is 10 x 5.625 in, the same size as Devcon's deck, so the import rescales nothing and no text overflows.

The kit lives at https://github.com/technophile-04/devcon-8-mumbai (clone it; the demo deck is served at https://technophile-04.github.io/devcon-8-mumbai/reference/deck.html). Reference renders of every layout are in `reference/slides/` and `reference/contact-sheet.png`. Build to match them.

## Files

| Path | What it is |
| --- | --- |
| `template/buidlguidl-devcon8.pptx` | 10 x 5.625 in, one named layout per slide type with the backgrounds, fonts and sizes built in, plus one example slide of each. Fill this |
| `backgrounds/cover.png` | title, closing, up next. Sky gradient, the illustrated town, ink wordmark top-left |
| `backgrounds/section.png` | section dividers. Painted clouds, ink wordmark top-left |
| `backgrounds/content.png` | content slides. Periwinkle-white ground, ink castle mark top-left and a "Devcon 8" tag top-right |
| `backgrounds/content-dark.png` | code and terminal slides. Ink ground, the same marks in white |
| `logos/` | the wordmark and the castle mark as SVG and 2x PNG, ink and white. Already baked into the backgrounds; only for a one-off need |
| `reference/deck.html` | every layout as a 1920x1080 slide with sample content. For maintainers: the reference PNGs are rendered from it, `?slide=N` shows the Nth slide in document order |
| `build/` | scripts that regenerate backgrounds, renders and the pptx. `build/build_pptx.py` is the source of the template |

## Canvas and units

Canvas is 1920x1080 px. Every number in this file is px on that canvas.

- The slide is 10 x 5.625 in, Devcon's deck size: pt = px x 0.375, so 48 px body is 18 pt.
- EMU in the pptx: px x 4762.5 (round to an integer).

Margins: 120 left and right, 96 top and bottom. Nothing readable sits outside them. The content area is x 120 to 1800, y 96 to 984; content headings start at y 120 to leave room under the corner marks. The marks live inside the margin bands and are part of the background.

## Colours

| Token | Hex | Use |
| --- | --- | --- |
| ink | #182232 | all text on light grounds, arrows, the dark ground |
| paper | #FFFCFC | text on the dark ground, cards |
| ground | #EBECFE | the content ground, from buidlguidl.com; already in the background |
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
| display, cover title, heading, quote | Space Grotesk Bold (700) | Google Fonts; built into Google Slides |
| body, labels | Space Grotesk, Regular and Medium (Bold in pptx, which has no 500) | Google Fonts; built into Google Slides |
| code, tags | Space Mono Regular | Google Fonts; built into Google Slides |

Google Slides only offers Google Fonts, so the kit uses only Google Fonts. Nothing to install, nothing to substitute. The pptx layouts already carry these typefaces; text typed into a placeholder inherits them.

## Type scale

| Style | Size | Line height | Font | Where |
| --- | --- | --- | --- | --- |
| display | 120 | 126 | Space Grotesk Bold | statement, section title |
| cover title | 96 | 101 | Space Grotesk Bold | title, closing, up next (two lines in a 1150 wide box in the sky above the art; a title that needs three lines drops to 80) |
| heading | 80 | 88 | Space Grotesk Bold | every content heading |
| quote | 80 | 92 | Space Grotesk Bold | the quote slide |
| body | 48 | 62 | Space Grotesk | everything the audience must read |
| code | 44 | 64 | Space Mono | code and terminal lines |
| label | 36 | 47 | Space Grotesk Medium | credits, part numbers, captions under diagram boxes. Never for a point you are making |
| tag | 36 | 47 | Space Mono | the corner tags, the event line, handles, time and room on cover slides |

Devcon asks for body text of at least 24 pt, which is 48 px here. Letter-spacing is normal (0) everywhere; Google Slides has no tracking control, so the reference renders use none either.

## The highlight

At most one highlighted phrase per slide: a lime #B5DC3A marker behind ink text, like the lime button on buidlguidl.com. The marker extends 0.08em beyond the words on each side with 0.14em corner radius.

- Google Slides: select the words and set Highlight color to #B5DC3A.
- python-pptx: add a run-level highlight to the words (snippet under Building the deck), or draw a lime rounded rectangle sized to the words and send it behind the text, as the example slides do.

Never highlight a whole line, a heading, or more than one phrase.

## Backgrounds: what is baked and what is clear

- `cover.png`: wordmark at (120, 96), 64 tall. Clear sky from y 160 to about 760 within x 120 to 960. The town's line art starts at y 766 on the far left, y 545 past x 960, y 275 past x 1800. Keep every word inside the clear column.
- `section.png`: wordmark at (120, 96), 64 tall. Title zone x 120 to 1120; the pale lime left side gives ink the best contrast.
- `content.png` and `content-dark.png`: castle mark at (120, 26), 44 tall, and a "Devcon 8" tag in Space Mono 36 ending at x 1800, both centred on y 48 inside the top margin band. The whole content area is free; headings start at y 120.

Never place a second logo, recolour a background, or crop one. Export at exactly 1920x1080.

## Layouts

Positions are (x, y, width, height). A text box anchors at its top-left and wraps inside its width. The pptx layout name is in brackets, and each slot names the placeholder that holds it: `title` is `slide.shapes.title`, `[n]` is `slide.placeholders[n]`. Anything without a placeholder is a fixed shape on the layout.

### 1. Title [Title], cover.png

Two groups on the left: the title in the open sky above the art, then the speaker block below it with a clear gap. The title box is anchored at its bottom, so a long title grows upward and never reaches the speaker block.

- event line: (720, 104, 1080, 47) tag, right-aligned, on the wordmark's line. Fixed text box on the layout, the token `EVENT_LINE` below
- talk title: (120, 188, 1150, 252) cover title, bottom-anchored (text ends at y 440), two lines. About 45 characters fit; every talk on the day does. If a title needs three lines, set it to 80 px with 84 px line spacing (30 pt on 31.5 pt) so it stays in the box and clear of the wordmark. `title`
- speaker name: (120, 496, 840, 62) body medium. `[1]`
- handle: (120, 560, 840, 47) tag, e.g. `@handle`. `[2]`

The title slide is the first frame of the YouTube recording. No extra decoration.

### 2. Statement [Statement], content.png

- statement: (120, 300, 1680, 400) display, up to three lines, one highlight. `[1]`
- sub-line: (120, 760, 1680, 62) body, optional. `[2]`

### 3. Heading + body [Heading + body], content.png

- heading: (120, 120, 1680, 176) heading, one or two lines. `title`
- body: (120, 320, 1680, 664) body. Short lines, at most four. `[1]`, one paragraph per bullet. Bullets are periwinkle dots, 32 px between items, text starts 64 px in; the layout draws them.

### 4. Heading + image [Heading + image], content.png

- heading: (120, 120, 1680, 96) heading, one line. `title`
- panel: (120, 256, 1680, 728) lavender, radius 32. Fixed on the layout
- image: inside the panel with 40 px padding, so within (160, 296, 1600, 648), at its natural aspect, corners radius 24. Never crop a screenshot to fill. `[1]` is a picture placeholder that would crop, so remove it and add the picture at its own size, centred in the panel, as the example slide does.

### 5. Three columns [Three columns], content.png

- heading: (120, 120, 1680, 96). `title`
- cards: x 120, 696, 1272, each (528 wide, y 260, 520 tall), paper, radius 32, padding 48. Fixed on the layout
- pill: (card x + 48, 308, 96, 64), fully round, label text 01 02 03 centred; fills periwinkle, orange, lime. Fixed on the layout
- card title: (card x + 48, 404, 432, 120) body medium. `[1]`, `[3]`, `[5]`
- card text: (card x + 48, 544, 432, 200) body, one or two short lines. `[2]`, `[4]`, `[6]`

### 6. Section [Section], section.png

- part number: (120, 392, 1000, 47) label, e.g. `Part 2`. `[1]`
- part title: (120, 456, 1000, 380) display, up to three lines. `title`

### 7. Code [Code], content-dark.png

- heading: (120, 120, 1680, 96) heading, paper. `title`
- label: (120, 256, 1680, 47) label, periwinkle light, e.g. `terminal`. `[1]`
- code: (120, 320, 1680, 640) code, paper, up to ten lines. `[2]`, one paragraph per line. Prompt glyphs (`$`, `?`) in periwinkle light: split the first character into its own run and colour it. No syntax colouring beyond that.

### 8. Quote [Quote], content.png

- quote: (120, 240, 1560, 330) quote style, up to three lines, in quotation marks (type the curly quotes). `[1]`
- bar: (120, 600, 60, 6) periwinkle. Fixed on the layout
- author: (120, 640, 1200, 62) body medium. `[2]`
- source: (120, 704, 1200, 47) label. `[3]`

A post screenshot replaces the quote text: put it at natural aspect inside (120, 240, 1560, 330) with radius 24, keep the bar and author.

### 9. Diagram [Diagram], content.png

- heading: (120, 120, 1680, 96). `title`
- boxes: 520x260, radius 32, flat fills in order lavender, peach, pale lime, paper; text body medium, left-aligned, vertically centred, 40 px padding
- three in a row: x 120, 700, 1280 at y 400. Arrows in the 60 px gaps: ink, 4 px line, triangle head, at y 530
- caption under each box: (box x, 692, 520, 100) label; code identifiers in Space Mono 36

The layout has only the heading. Draw the boxes, arrows and captions as shapes: `add_box`, `add_arrow` and `add_text` in `build/build_pptx.py` do exactly this for the example slide, copy them. More than four boxes, or two rows, means two slides. No shadows, no outlines, no diagonal arrows.

### 10. Closing [Closing], cover.png

Same positions as the title slide: Thanks on the title line, the speaker block below it, then the link.

- event line: same fixed box as the title slide, token `EVENT_LINE`
- thanks: (120, 188, 1150, 252) cover title, bottom-anchored (text ends at y 440). `title`
- speaker name: (120, 496, 840, 62) body medium. `[1]`
- handles: (120, 560, 840, 47) tag, e.g. `@handle on X and GitHub`. `[2]`
- link: (120, 656, 840, 62) body, this slide's one highlight. `[3]`

No QR code (Devcon rule below).

### 11. Up next [Up next], cover.png

For the host between talks. The title slide's layout with `Up next` in the corner and the time and room where the handle goes.

- corner tag: (720, 104, 1080, 47) tag, right-aligned, fixed text `Up next` on the layout
- talk title: (120, 188, 1150, 252) cover title, bottom-anchored. `title`
- speaker: (120, 496, 840, 62) body medium, e.g. `Shiv Bhonde`. `[1]`
- time and room: (120, 560, 840, 47) tag, e.g. `13:15 · Workshop 1`. `[2]`

## The event line token

```
EVENT_LINE = "Devcon 8 · Builder Enablement & BuidlGuidl"
```

It is a fixed, right-aligned Space Mono text box named `EVENT_LINE` on the Title and Closing layouts of the pptx (edit it in the slide master once and every cover slide follows) and a constant at the bottom of `reference/deck.html`. Change it only if the track name changes.

## Building the deck

**With python-pptx (Claude Code, Codex, any agent).** The main path. Fill `template/buidlguidl-devcon8.pptx`, save `decks/<talk-slug>.pptx` inside the kit, and hand that file to the speaker. Steps:

1. Open the template and get layouts by name: `prs.slide_layouts.get_by_name("Heading + body")`. The names are the ones in brackets above.
2. Add one slide per layout with `prs.slides.add_slide(layout)` and fill the placeholders listed for that layout. Set only text; fonts, sizes, colours, line heights, alignment and bullets come from the layout. One paragraph per bullet or code line. On the Title, Closing and Up next slides also set the title's vertical anchor to bottom on the slide itself (snippet below), so the deck does not depend on Google Slides reading it from the layout.
3. Delete the eleven example slides that came with the template (they are slides 1 to 11; python-pptx has no delete call, see the snippet).
4. Save as `decks/<talk-slug>.pptx` and run the self-check.

```python
from pptx import Presentation
from pptx.enum.text import MSO_ANCHOR
from pptx.oxml import parse_xml
from pptx.util import Emu

PX = 4762.5                                # EMU per canvas px (10 in across 1920 px)
prs = Presentation("template/buidlguidl-devcon8.pptx")
examples = list(prs.slides._sldIdLst)       # the template's example slides, removed at the end

def add(layout_name):
    return prs.slides.add_slide(prs.slide_layouts.get_by_name(layout_name))

def lines(placeholder, *text):             # one paragraph per line, layout styling kept
    tf = placeholder.text_frame
    tf.text = text[0]
    for t in text[1:]:
        tf.add_paragraph().text = t

s = add("Title")
s.shapes.title.text = "Building on Ethereum with agents"
s.shapes.title.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM   # long titles grow upward, away from the speaker block
s.placeholders[1].text = "Shiv Bhonde"
s.placeholders[2].text = "@shivbhonde"

s = add("Heading + body")
s.shapes.title.text = "What the agent gets for free"
lines(s.placeholders[1], "A contract, a deploy script and a frontend in one repo",
      "Typed hooks for every deployed contract")

s = add("Statement")
lines(s.placeholders[1], "An agent can scaffold a dapp. Shipping it is still your job.")
p = s.placeholders[1].text_frame.paragraphs[0]       # one lime highlight: split the phrase into its own run
p.runs[0].text = "An agent can scaffold a dapp. "
hl = p.add_run(); hl.text = "Shipping it"
hl._r.get_or_add_rPr().append(parse_xml(
    '<a:highlight xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:srgbClr val="B5DC3A"/></a:highlight>'))
p.add_run().text = " is still your job."

s = add("Heading + image")
s.shapes.title.text = "The debug page is the agent's first UI"
ph = s.placeholders[1]; ph._element.getparent().remove(ph._element)   # the picture placeholder would crop
w, h = 889, 648                                                        # the image's own aspect, scaled to fit 1600x648
s.shapes.add_picture("shot.png", Emu(round((960 - w / 2) * PX)), Emu(round((620 - h / 2) * PX)), Emu(round(w * PX)), Emu(round(h * PX)))

for sldId in examples:                     # drop the example slides
    prs.part.drop_rel(sldId.rId)
    prs.slides._sldIdLst.remove(sldId)
prs.save("decks/building-on-ethereum-with-agents.pptx")
```

Sizes in python-pptx: `Emu(round(px * 4762.5))` for positions, `Pt(px * 0.375)` if you ever set a size by hand. The highlight above becomes a text highlight in Google Slides; the shape alternative is `add_highlight` in `build/build_pptx.py`.

**With an agent that can edit Google Slides directly** (for example through a Google Slides connector): copy the BuidlGuidl Google Slides master, GOOGLE_SLIDES_MASTER_URL, and fill its layouts the same way. Do not create a deck from a blank theme. A speaker building by hand copies the same master.

**Handing in.** Tell the speaker these steps, they are the same for every path. Upload `decks/<talk-slug>.pptx` to Google Drive and open it with Google Slides (File > Save as Google Slides); a deck built from the master is already in Google Slides. Then open the Devcon link, choose File > Import slides, pick the deck, select all slides, tick "Keep original theme", import, and delete Devcon's placeholder slides. Devcon's guidelines (https://ef-events.notion.site/Devcon-8-India-Speaker-Guidelines-3e3638cdc41580e2abd8de93aeb659be) say the final deck must live in that link.

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

Look at every slide as an image. From a pptx: `soffice --headless --convert-to pdf decks/<talk-slug>.pptx` if LibreOffice is installed, then one PNG per page. Otherwise open the uploaded deck in Google Slides and page through it at full size.

1. Every word sits inside the margins: x 120 to 1800, y 96 to 984.
2. Nothing overflows its box. Three-line titles stay in their three lines; long words did not break mid-word.
3. No text sits on line art. On cover slides every word is in the clear column, the title ends at its bottom edge, and the speaker block sits below it with a clear gap.
4. Sizes are on the scale: nothing the audience must read is below 48 px, labels and tags 36, code 44.
5. Headings are Space Grotesk Bold, body is Space Grotesk, code and tags are Space Mono, nothing else.
6. At most one lime highlight per slide, ink text on it.
7. Backgrounds untouched: no second logo or castle, no recolour, no crop, no overlay.
8. Title, closing and up-next slides use the cover layouts, with the event line token in the corner tag.
9. Colours come from the table above; no gradients, no shadows, no emoji.
10. No QR code and none of the §11b words.
