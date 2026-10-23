# Fonts

The kit's two typefaces, with their licenses. Both are under the SIL Open Font License, which allows shipping them here and installing them on any machine. The files are the ones Google Fonts serves, copied from the google/fonts repo at commit 00a38a5 (`ofl/spacegrotesk` and `ofl/spacemono`).

| Folder | Files | Role in the kit |
| --- | --- | --- |
| `space-grotesk/` | `SpaceGrotesk[wght].ttf`, one variable file for weights 300 to 700, and `OFL.txt` | headings, body, labels |
| `space-mono/` | Regular, Bold, Italic and Bold Italic, and `OFL.txt` | code, tags, handles |

Which weights and sizes go where is in `design/tokens.json`.

## Where the files help

- A laptop that presents a pptx or Keynote file needs both fonts installed, or the app substitutes another font. On a Mac, double-click each `.ttf` and press Install, or drag the two folders into Font Book. On Windows, right-click each file and choose Install.
- An HTML deck shown offline loads them from here through `fonts.css`: replace the Google Fonts link in the deck with `<link rel="stylesheet" href="../fonts/fonts.css">`.
- Google Slides has both fonts built in, so a deck presented there needs nothing.
