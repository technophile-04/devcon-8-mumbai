#!/bin/sh
# Exports a deck for Devcon's Google Slides: PNG per slide, a pptx of pictures with speaker notes, a PDF.
# Usage: build/export.sh decks/<talk-slug>.html [outdir]   or   build/export.sh <folder-of-images> [outdir]
# Needs Google Chrome and uv (which fetches python-pptx and Pillow). Details in build/export.py.
set -e
KIT="$(cd "$(dirname "$0")/.." && pwd)"
exec uv run --with python-pptx python "$KIT/build/export.py" "$@"
