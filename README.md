# BuidlGuidl slide kit for Devcon 8

BuidlGuidl runs one day of community-led sessions at Devcon 8 in Mumbai. Each speaker builds slides with their own tool or agent, so this kit makes every deck come out looking like one family. It holds four background images with the logo already in place, the fonts, the colours and sizes, a reference deck of every layout, and a PowerPoint template. We lock the frame, you own the content.

![All eleven layouts](reference/contact-sheet.png)

## Give this to your agent

Paste one line into Claude Code, Codex, Claude chat, or whatever builds your slides:

```
Clone https://github.com/technophile-04/devcon-8-mumbai and follow its SKILL.md to build my slides for <talk title>.
```

`SKILL.md` has the whole system in one file. The agent reads it, uses the backgrounds and the type scale, and checks its own renders. The live demo deck with every layout is at https://technophile-04.github.io/devcon-8-mumbai/reference/deck.html.

## Three ways to use it

1. **An agent builds the deck.** Give it the line above. It produces an HTML deck from `reference/deck.html` or a pptx from the template, renders every slide, and self-checks against `SKILL.md`.
2. **Google Slides.** If you build in Google Slides, import `template/buidlguidl-devcon8.pptx` with "keep original theme", then write your content into the layouts. Google Slides has Space Grotesk and Space Mono but not the heading font, so headings fall back to Space Grotesk Bold.
3. **Keynote or PowerPoint.** Install the fonts (next section), open `template/buidlguidl-devcon8.pptx`, duplicate the example slide you want, replace the text. Keynote opens the file directly.

## Fonts

Headings use PP Neue Machina Inktrap Semibold. It is licensed to BuidlGuidl and is for BuidlGuidl talks. Keynote and PowerPoint users install it from `fonts/` (double-click the `.otf`, click Install Font).

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

`build/build.sh` rebuilds the logo PNGs, the backgrounds, the slide renders, the contact sheet and the pptx. It needs Google Chrome, Python 3 with Pillow, and `uv` (which fetches python-pptx). The source art in `build/src/` comes from the buidlguidl.com repo.
