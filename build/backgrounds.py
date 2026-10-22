"""Builds the four 1920x1080 backgrounds from the brand art in build/src.

Run build/logos.sh first (it renders the 4x logo PNGs this script bakes in).
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
SKY_TOP = (0xD0, 0xE5, 0xEF)      # Figma hero gradient, top
SKY_BOTTOM = (0xEA, 0xF7, 0xD1)   # Figma hero gradient, bottom

# Placement choices (see SKILL.md "Backgrounds")
HERO_PUSH = 40          # px the hero art is pushed below the canvas bottom
COVER_LOGO_H = 64       # logo height on cover.png, at the top-left margin
CONTENT_LOGO_H = 36     # logo height on content backgrounds, in the bottom margin band
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


def content(ground, logo_name):
    bg = Image.new("RGBA", (W, H), ground + (255,))
    lg = logo(logo_name, CONTENT_LOGO_H)
    y = H - 96 + (96 - CONTENT_LOGO_H) // 2
    bg.alpha_composite(lg, (120, y))
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
    save(content(PAPER, "buidlguidl-ink"), "content.png")
    save(content(INK, "buidlguidl-white"), "content-dark.png")
