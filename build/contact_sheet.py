"""Builds reference/contact-sheet.png from reference/slides/*.png (4 columns, labelled)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

KIT = Path(__file__).resolve().parent.parent
slides = sorted((KIT / "reference" / "slides").glob("*.png"))
cols, tw, th, gap, pad, label_h = 4, 480, 270, 24, 48, 44
rows = (len(slides) + cols - 1) // cols
sheet = Image.new("RGB", (pad * 2 + cols * tw + (cols - 1) * gap, pad * 2 + rows * (th + label_h) + (rows - 1) * gap), (0xF4, 0xF4, 0xF4))
draw = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
except OSError:
    font = ImageFont.load_default()
for i, p in enumerate(slides):
    r, c = divmod(i, cols)
    x = pad + c * (tw + gap)
    y = pad + r * (th + label_h + gap)
    im = Image.open(p).convert("RGB").resize((tw, th), Image.LANCZOS)
    sheet.paste(im, (x, y))
    draw.rectangle((x, y, x + tw - 1, y + th - 1), outline=(0xC8, 0xCB, 0xD6))
    draw.text((x, y + th + 12), p.stem, fill=(0x18, 0x22, 0x32), font=font)
out = KIT / "reference" / "contact-sheet.png"
sheet.save(out, optimize=True)
print("wrote", out, sheet.size)
