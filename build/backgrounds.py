"""Builds the four 1920x1080 backgrounds from the brand art in build/src.

Run build/logos.sh first (it renders the 4x logo, castle and "Devcon 8" tag PNGs this script bakes in).
"""
from pathlib import Path
from PIL import Image, ImageFilter

KIT = Path(__file__).resolve().parent.parent
SRC = KIT / "build" / "src"
TMP = KIT / "build" / "tmp"
OUT = KIT / "backgrounds"
W, H = 1920, 1080

INK = (0x18, 0x22, 0x32)
PAPER = (0xFF, 0xFC, 0xFC)
GROUND = (0xEB, 0xEC, 0xFE)       # content ground, the buidlguidl.com page background
SKY_TOP = (0xD0, 0xE5, 0xEF)      # Figma hero gradient, top
SKY_BOTTOM = (0xEA, 0xF7, 0xD1)   # Figma hero gradient, bottom

# Placement choices (see AGENTS.md "Backgrounds")
HERO_PUSH = 40          # px the hero art is pushed below the canvas bottom
COVER_LOGO_H = 64       # logo height on cover.png and section.png, at the top-left margin
CASTLE_H = 44           # castle mark height on content backgrounds, top-left of the top margin band
TAG_H = 44              # line box of the "Devcon 8" tag (36 px Space Mono), top-right of the same band
MARK_Y = 26             # top of both marks: centred on y 48, the middle of the 96 px band
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
    bg.alpha_composite(logo("buidlguidl-ink", COVER_LOGO_H), (120, 96))
    return bg


def content(ground, colour):
    """Flat ground with the castle mark at x 120 and the "Devcon 8" tag ending at x 1800, both in the top margin band."""
    bg = Image.new("RGBA", (W, H), ground + (255,))
    bg.alpha_composite(logo(f"castle-{colour}", CASTLE_H), (120, MARK_Y))
    tag = logo(f"tag-{colour}", TAG_H)          # rendered right-aligned, so its right edge is the text's right edge
    bg.alpha_composite(tag, (1800 - tag.width, MARK_Y))
    return bg


def section():
    clouds = Image.open(SRC / "background-clouds.png").convert("RGBA")
    cw = round(clouds.width * H / clouds.height)
    clouds = clouds.resize((cw, H), Image.LANCZOS)
    clouds = clouds.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    x = min(CLOUDS_CROP_X, cw - W)
    bg = clouds.crop((x, 0, x + W, H))
    bg.alpha_composite(logo("buidlguidl-ink", COVER_LOGO_H), (120, 96))
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
