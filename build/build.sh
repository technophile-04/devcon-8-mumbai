#!/bin/sh
# Regenerates the whole kit from design/tokens.json: tokens.css, logo PNGs, backgrounds, slide renders,
# contact sheet, style sheet, pptx. Needs: Google Chrome, python3 with Pillow, uv (python-pptx is fetched by uv).
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$KIT/build/tokens.py"
"$KIT/build/logos.sh"
python3 "$KIT/build/backgrounds.py"
"$KIT/build/render.sh"
"$KIT/build/style_sheet.sh"
uv run --offline --with python-pptx python "$KIT/build/build_pptx.py"
