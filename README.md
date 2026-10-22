# BuidlGuidl slide kit for Devcon 8

BuidlGuidl runs one day of community-led sessions at Devcon 8 in Mumbai. Each speaker builds slides with their own tool or agent and presents from Devcon's Google Slides, so this kit makes every deck come out looking like one family. It holds four background images with the logo already in place, the fonts, the colours and sizes, a reference deck of every layout, and a PowerPoint template. We lock the frame, you own the content.

![All eleven layouts](reference/contact-sheet.png)

## Give this to your agent

Paste one line into Claude Code, Codex, Claude chat, or whatever builds your slides:

```
Clone https://github.com/technophile-04/devcon-8-mumbai and follow its SKILL.md to build my slides for <talk title>.
```

`SKILL.md` has the whole system in one file. The agent reads it, uses the backgrounds and the type scale, and checks its own renders. The live demo deck with every layout is at https://technophile-04.github.io/devcon-8-mumbai/reference/deck.html.

## From the kit to the stage

Devcon gives every session its own Google Slides deck, and that deck is what plays on stage. Google Slides cannot show the kit's heading font as live text, so the deck goes in as pictures: every slide identical to the pixel, with the right font, and still playing from Devcon's link.

1. Give your agent the line above.
2. The agent builds your deck in the kit and runs `build/export.sh`. You get a folder of PNGs, `decks/<talk-slug>-google-slides.pptx` and `decks/<talk-slug>.pdf`.
3. Open your Devcon Google Slides deck (the link Devcon emailed you, of the form https://devcon.org/presentation/devcon8/<code>/). Choose File > Import slides > Upload, pick the `-google-slides.pptx`, select all slides, import, then delete Devcon's placeholder slides. Speaker notes come along.
4. To change anything, edit the source, export again and re-import. Text is not editable inside Google Slides, and that is on purpose: it keeps the font.
5. Keep the PDF on your laptop as the backup.

Building by hand: install the font from `fonts/`, open `template/buidlguidl-devcon8.pptx` in Keynote, duplicate the example slides you want and replace the text, export the slides as images at 1920x1080, then run `build/export.sh` on that folder and import the same way. Do not build natively in Google Slides: it loses the heading font.

## Fonts

Headings use PP Neue Machina Inktrap Semibold. It is licensed to BuidlGuidl and is for BuidlGuidl talks. Keynote users install it from `fonts/` (double-click the `.otf`, click Install Font).

Body and code use Space Grotesk and Space Mono. Install both from Google Fonts: https://fonts.google.com/specimen/Space+Grotesk and https://fonts.google.com/specimen/Space+Mono. HTML decks link them from Google Fonts; nothing to install.

## Locked vs yours

Locked: the backgrounds, the logo baked into them, the fonts, the colours, the type scale, the margins, and the title, closing and up-next slides.

Yours: everything on content slides. Pick from statement, heading and body, heading and image, three columns, section divider, code, quote, and diagram. Put them in any order. One highlighted phrase per slide at most.

## Devcon rules that touch slides

- Sessions are recorded and streamed to YouTube, so the title slide is the first frame people see.
- No QR codes or links to crypto products that are not compliant with Indian law.
- Avoid calling digital assets "currency", "securities", "custodian" or "depositories".
- Body text at least 24 pt.

Source: https://devcon.org/Devcon8-Speaker-Guidelines-2026.pdf

## Regenerating the kit

`build/build.sh` rebuilds the logo PNGs, the backgrounds, the slide renders, the contact sheet and the pptx template. `build/export.sh` turns a deck into the Google Slides pictures, pptx and PDF. Both need Google Chrome, Python 3 with Pillow, and `uv` (which fetches python-pptx). The source art in `build/src/` comes from the buidlguidl.com repo.
