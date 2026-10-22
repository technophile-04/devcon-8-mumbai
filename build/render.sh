#!/bin/sh
# Renders every slide of reference/deck.html to reference/slides/NN-name.png (1920x1080) with Google Chrome,
# then builds reference/contact-sheet.png.
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DECK="file://$KIT/reference/deck.html"
OUT="$KIT/reference/slides"
mkdir -p "$OUT"
i=0
for name in title statement heading-body heading-image three-columns section code quote diagram closing up-next; do
  i=$((i+1)); nn=$(printf "%02d" $i)
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --window-size=1920,1080 --virtual-time-budget=10000 \
    --screenshot="$OUT/$nn-$name.png" "$DECK?slide=$i" 2>/dev/null
  echo "rendered $nn-$name.png"
done
# fonts that actually loaded (expect: Space Grotesk, Space Mono, PP Neue Machina)
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=10000 --dump-dom "$DECK?slide=1" 2>/dev/null | grep -o 'data-fonts="[^"]*"' || echo "WARNING: could not read loaded fonts"
python3 "$KIT/build/contact_sheet.py"
