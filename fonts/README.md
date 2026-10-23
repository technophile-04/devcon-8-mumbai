# Fonts

The kit's two typefaces, with their licenses. Both are under the SIL Open Font License, which allows shipping them here and installing them on any machine. The files are static instances, one per weight, because PowerPoint and Keynote handle variable fonts badly: a variable Space Grotesk can come out Light, or get a faked bold, on the presenting laptop. Space Grotesk is from the 2.0.0 release at https://github.com/floriankarsten/space-grotesk, the same version Google Fonts serves. Space Mono is from the google/fonts repo at commit 00a38a5 (`ofl/spacemono`).

| Folder | Files | Role in the kit |
| --- | --- | --- |
| `space-grotesk/` | Regular, Medium and Bold, and `OFL.txt` | headings, body, labels |
| `space-mono/` | Regular and Bold, and `OFL.txt` | code, tags, handles |

The kit never sets italic, so no italic file ships. Which weights and sizes go where is in `design/tokens.json`.

## Where the files help

- A laptop that presents a pptx or Keynote file needs both fonts installed, or the app substitutes another font. On a Mac, double-click each `.ttf` and press Install, or drag the two folders into Font Book. On Windows, right-click each file and choose Install. Space Grotesk Medium shows up as its own family in some font menus; that is how the file names itself and the kit still finds it.
- An HTML deck shown offline loads them from here through `fonts.css`: replace the Google Fonts link in the deck with `<link rel="stylesheet" href="../fonts/fonts.css">`.
- Google Slides has both fonts built in, so a deck presented there needs nothing.
