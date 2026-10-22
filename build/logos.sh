#!/bin/sh
# Renders logos/*.svg to PNG with Google Chrome (transparent background).
# 2x exports ship in logos/; 4x renders go to build/tmp for baking into backgrounds.
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p "$KIT/build/tmp"
render() { # name width height out
  html="$KIT/build/tmp/$1-$2.html"
  printf '<html><body style="margin:0;background:transparent"><img src="file://%s/logos/%s.svg" style="width:%spx;height:%spx;display:block"></body></html>' "$KIT" "$1" "$2" "$3" > "$html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --default-background-color=00000000 \
    --window-size="$2,$3" --screenshot="$4" "file://$html" 2>/dev/null
}
# ink logo is 388x78, white logo is 396x78 (viewBox sizes)
render buidlguidl-ink   776  156 "$KIT/logos/buidlguidl-ink@2x.png"
render buidlguidl-white 792  156 "$KIT/logos/buidlguidl-white@2x.png"
render buidlguidl-ink   1552 312 "$KIT/build/tmp/buidlguidl-ink@4x.png"
render buidlguidl-white 1584 312 "$KIT/build/tmp/buidlguidl-white@4x.png"
echo "logos rendered"
