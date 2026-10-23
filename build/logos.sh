#!/bin/sh
# Renders logos/*.svg to PNG with Google Chrome (transparent background), plus the "Devcon 8" corner tag.
# 2x exports ship in logos/; 4x renders go to build/tmp for baking into backgrounds.
# The tag is Space Mono from Google Fonts, so that step needs network (the SVG renders do not).
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
# ink wordmark is 388x78, white wordmark is 396x78, the castle marks are 76x78 (viewBox sizes)
render buidlguidl-ink   776  156 "$KIT/logos/buidlguidl-ink@2x.png"
render buidlguidl-white 792  156 "$KIT/logos/buidlguidl-white@2x.png"
render castle-ink       152  156 "$KIT/logos/castle-ink@2x.png"
render castle-white     152  156 "$KIT/logos/castle-white@2x.png"
render buidlguidl-ink   1552 312 "$KIT/build/tmp/buidlguidl-ink@4x.png"
render buidlguidl-white 1584 312 "$KIT/build/tmp/buidlguidl-white@4x.png"
render castle-ink       304  312 "$KIT/build/tmp/castle-ink@4x.png"
render castle-white     304  312 "$KIT/build/tmp/castle-white@4x.png"

# "Devcon 8" tag at 4x: 36 px Space Mono on a 44 px line, right-aligned, so the text's right edge is the image's right edge.
tag() { # name colour
  html="$KIT/build/tmp/tag-$1.html"
  printf '<html><head><link href="https://fonts.googleapis.com/css2?family=Space+Mono&display=swap" rel="stylesheet"></head><body style="margin:0;background:transparent"><p style="position:absolute;right:0;top:0;margin:0;font:400 144px/176px &quot;Space Mono&quot;,monospace;color:%s;white-space:nowrap">Devcon 8</p></body></html>' "$2" > "$html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --default-background-color=00000000 --virtual-time-budget=10000 \
    --window-size=1200,176 --screenshot="$KIT/build/tmp/tag-$1@4x.png" "file://$html" 2>/dev/null
}
tag ink "#182232"
tag white "#FFFCFC"
echo "logos rendered"
