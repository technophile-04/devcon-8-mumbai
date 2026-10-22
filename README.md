# BuidlGuidl slide kit for Devcon 8

BuidlGuidl runs one day of community-led sessions at Devcon 8 in Mumbai. Each speaker builds slides with their own tool or agent, so this kit makes every deck come out looking like one family. It holds four background images with the logo already in place, the colours and sizes, a reference deck of every layout, and a pptx template whose layouts carry all of that. We lock the frame, you own the content.

![All eleven layouts](reference/contact-sheet.png)

## Give this to your agent

Paste one line into Claude Code, Codex, Claude chat, or whatever builds your slides:

```
Clone https://github.com/technophile-04/devcon-8-mumbai and follow its SKILL.md to build my slides for <talk title>.
```

`SKILL.md` has the whole system in one file. The agent fills `template/buidlguidl-devcon8.pptx` from its layouts, saves `decks/<talk-slug>.pptx`, and checks its own slides against the rules. You upload that file to Google Drive and open it with Google Slides (File > Save as Google Slides). An agent that can edit Google Slides directly copies the master above instead.

## Or build it by hand

Make a copy of the BuidlGuidl Google Slides master, GOOGLE_SLIDES_MASTER_URL, and build in the copy. It has one layout per slide type with the backgrounds, fonts and sizes already set, plus an example slide of each. Duplicate the example you want, replace the text, delete the rest. Every layout is shown at https://technophile-04.github.io/devcon-8-mumbai/reference/deck.html.

## Hand it in

Devcon wants final slides by Oct 27. Open your Devcon link, the one Devcon emailed you, of the form https://devcon.org/presentation/devcon8/<code>/. Choose File > Import slides, pick your deck, select all slides, tick "Keep original theme", import, then delete Devcon's placeholder slides. Devcon's guidelines say the final deck must live in that link; if you built your slides elsewhere, import them into the link. The guidelines are at https://ef-events.notion.site/Devcon-8-India-Speaker-Guidelines-3e3638cdc41580e2abd8de93aeb659be.

## Fonts

Headings are Space Grotesk Bold, body is Space Grotesk, code is Space Mono. Google Slides has all three built in, so there is nothing to install.

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

For maintainers. `build/build.sh` rebuilds the logo PNGs, the backgrounds, the slide renders, the contact sheet and the pptx. The reference PNGs are rendered from `reference/deck.html`. It needs Google Chrome, Python 3 with Pillow, and `uv` (which fetches python-pptx). The source art in `build/src/` comes from the buidlguidl.com repo. After a rebuild, upload the new pptx to Google Drive and replace the master.
