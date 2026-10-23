# Recipe: pptx

Fill `template/buidlguidl-devcon8.pptx` with python-pptx. The result opens in PowerPoint, Keynote and Google Slides, and the speaker can still edit it.

## What the template gives you

Eleven layouts, named as in AGENTS.md: `Title`, `Statement`, `Heading + body`, and so on. Each layout carries its background as a true slide background, draws its fixed shapes, the event line, the image panel, the cards and pills and the quote bar, and holds text placeholders already set to the kit's fonts, sizes, colours, line heights, alignment and bullets. Text you type inherits all of it, so you set only words. The template opens with one example slide per layout, the reference deck's content; delete those at the end.

The slide is 10 x 5.625 in, so 1 px on the 1920 canvas is 4762.5 EMU and 0.375 pt: `Emu(round(px * 4762.5))` for a position, `Pt(px * 0.375)` for a size you set by hand. pptx has no weight 500, so "body medium" is Space Grotesk Bold in the placeholders.

## Placeholders

`title` is `slide.shapes.title` and `[n]` is `slide.placeholders[n]`, in the order AGENTS.md lists the slots.

| Layout | Slots |
| --- | --- |
| Title | talk title `title`, speaker name `[1]`, handle `[2]` |
| Statement | statement `[1]`, sub-line `[2]` |
| Heading + body | heading `title`, body `[1]`, one paragraph per bullet |
| Heading + image | heading `title`. `[1]` is a picture placeholder that crops to fill; remove it and add the picture at its own size, centred in the panel |
| Three columns | heading `title`, card titles `[1]` `[3]` `[5]`, card text `[2]` `[4]` `[6]` |
| Section | part number `[1]`, part title `title` |
| Code | heading `title`, label `[1]`, code `[2]`, one paragraph per line |
| Quote | quote `[1]`, author `[2]`, source `[3]` |
| Diagram | heading `title`. Draw the boxes, arrows and captions with `add_box`, `add_arrow` and `add_text` from `build/build_pptx.py`, which draw the example slide |
| Closing | thanks `title`, speaker name `[1]`, handles `[2]`, link `[3]` |
| Up next | talk title `title`, speaker `[1]`, time and room `[2]` |

## Steps

1. Open the template and fetch layouts by name: `prs.slide_layouts.get_by_name("Heading + body")`.
2. Add one slide per layout with `prs.slides.add_slide(layout)` and set the text of its placeholders. On Title, Closing and Up next also set the title's vertical anchor to bottom on the slide itself, as below, so a long title grows upward in every app that opens the file.
3. Highlight a phrase with a run-level `a:highlight`, as below; Google Slides shows it as a text highlight. The shape alternative, a lime rounded rectangle measured to the words and sent behind the text, is `add_highlight` in `build/build_pptx.py`.
4. On a Code slide, split the prompt glyph into its own run and colour it periwinkle light `9FA9FF`.
5. Delete the eleven example slides, then save `decks/<talk-slug>.pptx`.

```python
from pathlib import Path
from pptx import Presentation
from pptx.enum.text import MSO_ANCHOR
from pptx.oxml import parse_xml
from pptx.util import Emu

PX = 4762.5                                # EMU per canvas px
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
s.shapes.title.text = "Your talk title"
s.shapes.title.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM   # long titles grow upward, away from the speaker block
s.placeholders[1].text = "Your Name"
s.placeholders[2].text = "@handle"

s = add("Heading + body")
s.shapes.title.text = "A heading of one or two lines"
lines(s.placeholders[1], "First point, one short line",
      "Second point, one short line")

s = add("Statement")
lines(s.placeholders[1], "One sentence with a highlighted phrase in it.")
p = s.placeholders[1].text_frame.paragraphs[0]       # one lime highlight: split the phrase into its own run
p.runs[0].text = "One sentence with a "
hl = p.add_run(); hl.text = "highlighted phrase"
hl._r.get_or_add_rPr().append(parse_xml(
    '<a:highlight xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:srgbClr val="B5DC3A"/></a:highlight>'))
p.add_run().text = " in it."

s = add("Heading + image")
s.shapes.title.text = "A heading of one line"
ph = s.placeholders[1]; ph._element.getparent().remove(ph._element)   # the picture placeholder would crop
w, h = 889, 648                                                        # the image's own aspect, scaled to fit 1600x648
s.shapes.add_picture("your-screenshot.png", Emu(round((960 - w / 2) * PX)), Emu(round((620 - h / 2) * PX)), Emu(round(w * PX)), Emu(round(h * PX)))

s = add("Closing")
s.shapes.title.text = "Thanks"
s.shapes.title.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM
s.placeholders[1].text = "Your Name"
s.placeholders[2].text = "@handle on X and GitHub"
s.placeholders[3].text = "your-link.com"

for sldId in examples:                     # drop the example slides
    prs.part.drop_rel(sldId.rId)
    prs.slides._sldIdLst.remove(sldId)
Path("decks").mkdir(exist_ok=True)
prs.save("decks/your-talk-slug.pptx")
```

Run it from the kit root: `uv run --with python-pptx python build_deck.py`, or `pip install python-pptx` first and run it with `python`.

## Look at the slides

With LibreOffice installed: `soffice --headless --convert-to pdf --outdir decks decks/<talk-slug>.pptx`, then `pdftoppm -png -r 192 decks/<talk-slug>.pdf decks/<talk-slug>` for one 1920x1080 PNG per slide. LibreOffice substitutes any font it lacks, so install Space Grotesk and Space Mono first, or judge positions rather than glyphs. Without LibreOffice, open the file in Keynote, PowerPoint or Google Slides and page through it at full size.

## Tell the speaker

PowerPoint and Keynote need Space Grotesk and Space Mono installed on the presenting laptop, from fonts.google.com. A speaker who presents from Google Slides continues with [google-slides.md](google-slides.md).
