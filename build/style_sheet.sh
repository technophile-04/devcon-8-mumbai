#!/bin/sh
# Renders design/style-sheet.html to design/style-sheet.png at its full height, 1920 wide, with Google Chrome.
# The page loads the fonts from fonts/, so this step works offline.
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGE="file://$KIT/design/style-sheet.html"
python3 "$KIT/build/style_sheet.py"
DOM=$("$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1920,1080 --virtual-time-budget=10000 --dump-dom "$PAGE" 2>/dev/null)
HEIGHT=$(printf %s "$DOM" | grep -o 'data-height="[0-9]*"' | grep -o '[0-9]*')
echo "fonts that loaded: $(printf %s "$DOM" | grep -o 'data-fonts="[^"]*"')"   # expect Space Grotesk, Space Mono
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1920,"$HEIGHT" \
  --virtual-time-budget=10000 --screenshot="$KIT/design/style-sheet.png" "$PAGE" 2>/dev/null
echo "rendered design/style-sheet.png (1920x$HEIGHT)"
