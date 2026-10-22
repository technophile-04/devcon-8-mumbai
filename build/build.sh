#!/bin/sh
# Regenerates the whole kit: logo PNGs, backgrounds, slide renders, contact sheet, pptx.
# Needs: Google Chrome, python3 with Pillow, uv (python-pptx is fetched by uv).
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
"$KIT/build/logos.sh"
python3 "$KIT/build/backgrounds.py"
"$KIT/build/render.sh"
uv run --offline --with python-pptx python "$KIT/build/build_pptx.py"
