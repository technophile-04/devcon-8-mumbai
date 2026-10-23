"""Builds the four 1920x1080 backgrounds from the brand art in build/src.

Run build/logos.sh first (it renders the 4x logo, castle and "Devcon 8" tag PNGs this script bakes in).
Colours, canvas, margins and mark sizes come from design/tokens.json; the art placement choices are below.
"""
from pathlib import Path
from PIL import Image, ImageFilter

from tokens import Tokens

KIT = Path(__file__).resolve().parent.parent
SRC = KIT / "build" / "src"
TMP = KIT / "build" / "tmp"
OUT = KIT / "backgrounds"

T = Tokens()
W, H = T.px("canvas.width"), T.px("canvas.height")
MARGIN_X, MARGIN_Y = T.px("space.margin-x"), T.px("space.margin-y")
INK, GROUND = T.rgb("ink"), T.rgb("ground")
SKY_TOP, SKY_BOTTOM = T.rgb("sky-top"), T.rgb("sky-bottom")
COVER_LOGO_H = T.px("mark.wordmark-height")   # wordmark on cover.png and section.png, at the top-left margin corner
CASTLE_H = T.px("mark.castle-height")         # castle mark on content backgrounds, top-left of the top margin band
TAG_H = CASTLE_H                              # line box of the "Devcon 8" tag, top-right of the same band
MARK_Y = T.px("mark.band-top")                # top of both marks: centred on the middle of the top margin band

# Art placement choices
HERO_PUSH = 40          # px the hero art is pushed below the canvas bottom
CLOUDS_CROP_X = 240     # left edge of the 1920 window taken from the upscaled clouds


def logo(name, height):
    im = Image.open(TMP / f"{name}@4x.png").convert("RGBA")
    w = round(im.width * height / im.height)
    return im.resize((w, height), Image.LANCZOS)


def gradient(top, bottom):
    im = Image.new("RGB", (1, H))
    for y in range(H):
        t = y / (H - 1)
        im.putpixel((0, y), tuple(round(a + (b - a) * t) for a, b in zip(top, bottom)))
    return im.resize((W, H), Image.NEAREST).convert("RGBA")


def cover():
    bg = gradient(SKY_TOP, SKY_BOTTOM)
    hero = Image.open(SRC / "hero-new.png").convert("RGBA")
    hw = W
    hh = round(hero.height * hw / hero.width)
    hero = hero.resize((hw, hh), Image.LANCZOS)
    bg.alpha_composite(hero, (0, H - hh + HERO_PUSH))
    bg.alpha_composite(logo("buidlguidl-ink", COVER_LOGO_H), (MARGIN_X, MARGIN_Y))
    return bg


def content(ground, colour):
    """Flat ground with the castle mark at the left margin and the "Devcon 8" tag ending at the right margin, both in the top margin band."""
    bg = Image.new("RGBA", (W, H), ground + (255,))
    bg.alpha_composite(logo(f"castle-{colour}", CASTLE_H), (MARGIN_X, MARK_Y))
    tag = logo(f"tag-{colour}", TAG_H)          # rendered right-aligned, so its right edge is the text's right edge
    bg.alpha_composite(tag, (W - MARGIN_X - tag.width, MARK_Y))
    return bg


def section():
    clouds = Image.open(SRC / "background-clouds.png").convert("RGBA")
    cw = round(clouds.width * H / clouds.height)
    clouds = clouds.resize((cw, H), Image.LANCZOS)
    clouds = clouds.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    x = min(CLOUDS_CROP_X, cw - W)
    bg = clouds.crop((x, 0, x + W, H))
    bg.alpha_composite(logo("buidlguidl-ink", COVER_LOGO_H), (MARGIN_X, MARGIN_Y))
    return bg


def save(im, name):
    im.convert("RGB").save(OUT / name, optimize=True)
    print("wrote", OUT / name, im.size)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    save(cover(), "cover.png")
    save(section(), "section.png")
    save(content(GROUND, "ink"), "content.png")
    save(content(INK, "white"), "content-dark.png")
