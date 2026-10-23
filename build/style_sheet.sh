#!/bin/sh
# Renders design/style-sheet.html to design/style-sheet.png at its full height, 1920 wide, and design/overview.html
# to design/overview.png at 1920x1080, with Google Chrome. Both pages load the fonts from fonts/, so this step works offline.
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGE="file://$KIT/design/style-sheet.html"
CARD="file://$KIT/design/overview.html"
python3 "$KIT/build/style_sheet.py"
DOM=$("$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1920,1080 --virtual-time-budget=10000 --dump-dom "$PAGE" 2>/dev/null)
HEIGHT=$(printf %s "$DOM" | grep -o 'data-height="[0-9]*"' | grep -o '[0-9]*')
echo "fonts that loaded: $(printf %s "$DOM" | grep -o 'data-fonts="[^"]*"')"   # expect Space Grotesk, Space Mono
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1920,"$HEIGHT" \
  --virtual-time-budget=10000 --screenshot="$KIT/design/style-sheet.png" "$PAGE" 2>/dev/null
echo "rendered design/style-sheet.png (1920x$HEIGHT)"
DOM=$("$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1920,1080 --virtual-time-budget=10000 --dump-dom "$CARD" 2>/dev/null)
echo "overview overflow: $(printf %s "$DOM" | grep -o 'data-overflow="[^"]*"')"   # expect 0: everything fits the card
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1920,1080 \
  --virtual-time-budget=10000 --screenshot="$KIT/design/overview.png" "$CARD" 2>/dev/null
echo "rendered design/overview.png (1920x1080)"
