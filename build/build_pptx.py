"""Builds template/buidlguidl-devcon8.pptx.

Run: uv run --offline --with python-pptx python build/build_pptx.py
Needs backgrounds/ (build/backgrounds.py) and reference/sample/se2-ui.png.

Slide size 13.333 x 7.5 in. Every px value below is on the 1920x1080 canvas
(1 px = 6350 EMU = 0.5 pt). Layouts carry the backgrounds as true slide
backgrounds plus text placeholders in the kit's fonts and sizes. The example
slides use those layouts so people can duplicate them.
"""
import re
from pathlib import Path
from xml.sax.saxutils import escape

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls, qn
from pptx.util import Emu, Pt

KIT = Path(__file__).resolve().parent.parent
BG = KIT / "backgrounds"
OUT = KIT / "template" / "buidlguidl-devcon8.pptx"
SAMPLE_IMAGE = KIT / "reference" / "sample" / "se2-ui.png"

# ---- the one event-line token (also in reference/deck.html and SKILL.md) ----
EVENT_LINE = "Devcon 8 · Builder Enablement & BuidlGuidl"

# ---- fonts (typeface strings as Office resolves them) ----
HEAD_FONT = "Space Grotesk"  # bold; the font Google Slides has, so the demo matches what shows on stage
BODY_FONT = "Space Grotesk"
CODE_FONT = "Space Mono"

INK, PAPER, GREY, LAVENDER, PEACH = "182232", "FFFCFC", "F4F4F4", "D8DCFF", "FFD4B5"
PERIWINKLE, PERIWINKLE_LIGHT, ORANGE, LIME, PALE_LIME = "808CFF", "9FA9FF", "FF6E1D", "B5DC3A", "EAFFA9"

PX = 6350  # EMU per canvas px


def px(v):
    return Emu(round(v * PX))


# type scale: (size px, line-height px, font, bold)
DISPLAY = (120, 126, HEAD_FONT, True)
COVER_TITLE = (96, 101, HEAD_FONT, True)
HEADING = (80, 88, HEAD_FONT, True)
QUOTE = (80, 92, HEAD_FONT, True)
BODY = (48, 62, BODY_FONT, False)
BODY_BOLD = (48, 62, BODY_FONT, True)   # the HTML uses weight 500; Office has no 500, so bold
LABEL = (36, 47, BODY_FONT, False)
CODE = (44, 64, CODE_FONT, False)

NS = nsdecls("p", "a", "r")
_id = [100]


def next_id():
    _id[0] += 1
    return _id[0]


def run_props(style, color=INK, highlight=None):
    size, _, font, bold = style
    hl = f'<a:highlight><a:srgbClr val="{highlight}"/></a:highlight>' if highlight else ""
    return (f'<a:defRPr sz="{size * 50}" b="{1 if bold else 0}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill>{hl}'
            f'<a:latin typeface="{font}"/><a:ea typeface="{font}"/><a:cs typeface="{font}"/></a:defRPr>')


def para_props(style, bullets=False, space_before=0, color=INK):
    _, lh, _, _ = style
    bu = (f'<a:buClr><a:srgbClr val="{PERIWINKLE}"/></a:buClr><a:buSzPct val="80000"/><a:buFont typeface="Arial"/><a:buChar char="●"/>'
          if bullets else "<a:buNone/>")
    mar = 'marL="406400" indent="-406400"' if bullets else 'marL="0" indent="0"'
    return (f'<a:lvl1pPr {mar} algn="l"><a:lnSpc><a:spcPts val="{lh * 50}"/></a:lnSpc><a:spcBef><a:spcPts val="{space_before * 50}"/></a:spcBef>'
            f'{bu}{run_props(style, color)}</a:lvl1pPr>')


def placeholder_xml(name, ph_type, idx, x, y, w, h, style, prompt, color=INK, bullets=False, space_before=0, anchor="t"):
    ph = f'<p:ph type="{ph_type}"/>' if ph_type == "title" else f'<p:ph type="{ph_type}" idx="{idx}"/>'
    body = (f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}"><a:noAutofit/></a:bodyPr>'
            f'<a:lstStyle>{para_props(style, bullets, space_before, color)}</a:lstStyle>'
            f'<a:p><a:r><a:rPr lang="en-US"/><a:t>{escape(prompt)}</a:t></a:r></a:p></p:txBody>') if ph_type != "pic" else ""
    return parse_xml(
        f'<p:sp {NS}><p:nvSpPr><p:cNvPr id="{next_id()}" name="{name}"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
        f'<p:nvPr>{ph}</p:nvPr></p:nvSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{x * PX}" y="{y * PX}"/><a:ext cx="{w * PX}" cy="{h * PX}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>{body}</p:sp>')


def textbox_xml(name, x, y, w, h, style, text, color=INK):
    return parse_xml(
        f'<p:sp {NS}><p:nvSpPr><p:cNvPr id="{next_id()}" name="{name}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{x * PX}" y="{y * PX}"/><a:ext cx="{w * PX}" cy="{h * PX}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>'
        f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="t"><a:noAutofit/></a:bodyPr>'
        f'<a:lstStyle>{para_props(style, color=color)}</a:lstStyle>'
        f'<a:p><a:r><a:rPr lang="en-US"/><a:t>{escape(text)}</a:t></a:r></a:p></p:txBody></p:sp>')


def rect_xml(name, x, y, w, h, fill, radius_px=0):
    if radius_px:
        adj = round(radius_px / min(w, h) * 50000)
        geom = f'<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val {adj}"/></a:avLst></a:prstGeom>'
    else:
        geom = '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
    return parse_xml(
        f'<p:sp {NS}><p:nvSpPr><p:cNvPr id="{next_id()}" name="{name}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{x * PX}" y="{y * PX}"/><a:ext cx="{w * PX}" cy="{h * PX}"/></a:xfrm>{geom}'
        f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
        f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody></p:sp>')


def set_layout_background(layout, image_path):
    _, rId = layout.part.get_or_add_image_part(str(image_path))
    bg = parse_xml(f'<p:bg {NS}><p:bgPr><a:blipFill dpi="0" rotWithShape="1"><a:blip r:embed="{rId}"/><a:srcRect/>'
                   f'<a:stretch><a:fillRect/></a:stretch></a:blipFill><a:effectLst/></p:bgPr></p:bg>')
    cSld = layout._element.cSld
    old = cSld.find(qn("p:bg"))
    if old is not None:
        cSld.remove(old)
    cSld.insert(0, bg)


def reset_layout(layout, name, background):
    layout.name = name
    spTree = layout.shapes._spTree
    for el in list(spTree):
        if el.tag not in (qn("p:nvGrpSpPr"), qn("p:grpSpPr")):
            spTree.remove(el)
    set_layout_background(layout, BG / background)
    return spTree


# ---------------------------------------------------------------- layouts
def build_layouts(prs):
    L = {}
    layouts = list(prs.slide_layouts)

    t = reset_layout(layouts[0], "Title", "cover.png")
    t.append(textbox_xml("EVENT_LINE", 120, 200, 1000, 47, LABEL, EVENT_LINE))
    t.append(placeholder_xml("Talk title", "title", 0, 120, 280, 840, 310, COVER_TITLE, "Talk title"))
    t.append(placeholder_xml("Speaker name", "body", 1, 120, 624, 900, 62, BODY_BOLD, "Speaker name"))
    t.append(placeholder_xml("Role or handle", "body", 2, 120, 688, 900, 47, LABEL, "Role · @handle"))
    L["title"] = layouts[0]

    t = reset_layout(layouts[1], "Statement", "content.png")
    t.append(placeholder_xml("Statement", "body", 1, 120, 300, 1680, 400, DISPLAY, "One big line, one highlighted phrase"))
    t.append(placeholder_xml("Sub-line", "body", 2, 120, 760, 1680, 62, BODY, "Optional sub-line"))
    L["statement"] = layouts[1]

    t = reset_layout(layouts[2], "Heading + body", "content.png")
    t.append(placeholder_xml("Heading", "title", 0, 120, 96, 1680, 176, HEADING, "Heading"))
    t.append(placeholder_xml("Body", "body", 1, 120, 320, 1680, 664, BODY, "Short lines, at most four", bullets=True, space_before=32))
    L["heading-body"] = layouts[2]

    t = reset_layout(layouts[3], "Heading + image", "content.png")
    t.append(placeholder_xml("Heading", "title", 0, 120, 96, 1680, 96, HEADING, "Heading"))
    t.append(rect_xml("Image panel", 120, 232, 1680, 752, LAVENDER, 32))
    t.append(placeholder_xml("Image", "pic", 1, 160, 272, 1600, 672, BODY, ""))
    L["heading-image"] = layouts[3]

    t = reset_layout(layouts[4], "Three columns", "content.png")
    t.append(placeholder_xml("Heading", "title", 0, 120, 96, 1680, 96, HEADING, "Heading"))
    for i, (x, fill) in enumerate(((120, PERIWINKLE), (696, ORANGE), (1272, LIME))):
        t.append(rect_xml(f"Card {i + 1}", x, 260, 528, 520, GREY, 32))
        t.append(rect_xml(f"Pill {i + 1}", x + 48, 308, 96, 64, fill, 32))
        t.append(textbox_xml(f"Pill number {i + 1}", x + 48, 322, 96, 40, LABEL, f"0{i + 1}"))
        t[-1].txBody.find(qn("a:lstStyle")).find(qn("a:lvl1pPr")).set("algn", "ctr")
        t.append(placeholder_xml(f"Column {i + 1} title", "body", 1 + i * 2, x + 48, 404, 432, 120, BODY_BOLD, "Column title"))
        t.append(placeholder_xml(f"Column {i + 1} text", "body", 2 + i * 2, x + 48, 544, 432, 200, BODY, "One or two short lines"))
    L["three-columns"] = layouts[4]

    t = reset_layout(layouts[5], "Section", "section.png")
    t.append(placeholder_xml("Part number", "body", 1, 120, 392, 1000, 47, LABEL, "Part 1"))
    t.append(placeholder_xml("Part title", "title", 0, 120, 456, 1000, 380, DISPLAY, "Part title"))
    L["section"] = layouts[5]

    t = reset_layout(layouts[6], "Code", "content-dark.png")
    t.append(placeholder_xml("Heading", "title", 0, 120, 96, 1680, 96, HEADING, "Heading", color=PAPER))
    t.append(placeholder_xml("Code label", "body", 1, 120, 256, 1680, 47, LABEL, "terminal", color=PERIWINKLE_LIGHT))
    t.append(placeholder_xml("Code", "body", 2, 120, 320, 1680, 640, CODE, "$ command", color=PAPER))
    L["code"] = layouts[6]

    t = reset_layout(layouts[7], "Quote", "content.png")
    t.append(placeholder_xml("Quote", "body", 1, 120, 240, 1560, 330, QUOTE, "“The quote, up to three lines.”"))
    t.append(rect_xml("Bar", 120, 600, 60, 6, PERIWINKLE))
    t.append(placeholder_xml("Author", "body", 2, 120, 640, 1200, 62, BODY_BOLD, "Author"))
    t.append(placeholder_xml("Source", "body", 3, 120, 704, 1200, 47, LABEL, "Where it was said"))
    L["quote"] = layouts[7]

    t = reset_layout(layouts[8], "Diagram", "content.png")
    t.append(placeholder_xml("Heading", "title", 0, 120, 96, 1680, 96, HEADING, "Heading"))
    L["diagram"] = layouts[8]

    t = reset_layout(layouts[9], "Closing", "cover.png")
    t.append(textbox_xml("EVENT_LINE", 120, 200, 1000, 47, LABEL, EVENT_LINE))
    t.append(placeholder_xml("Thanks", "title", 0, 120, 280, 840, 110, COVER_TITLE, "Thanks"))
    t.append(placeholder_xml("Speaker name", "body", 1, 120, 440, 880, 62, BODY_BOLD, "Speaker name"))
    t.append(placeholder_xml("Handles", "body", 2, 120, 504, 880, 62, BODY, "@handle on X and GitHub"))
    t.append(placeholder_xml("Link", "body", 3, 120, 584, 880, 62, BODY, "one-link.com"))
    L["closing"] = layouts[9]

    t = reset_layout(layouts[10], "Up next", "cover.png")
    t.append(textbox_xml("Up next", 120, 200, 1000, 47, LABEL, "Up next"))
    t.append(placeholder_xml("Talk title", "title", 0, 120, 280, 840, 310, COVER_TITLE, "Talk title"))
    t.append(placeholder_xml("Speaker", "body", 1, 120, 624, 900, 62, BODY_BOLD, "Speaker, affiliation"))
    t.append(placeholder_xml("Time and room", "body", 2, 120, 688, 900, 62, BODY, "13:15 · Room"))
    L["up-next"] = layouts[10]
    return L


# ---------------------------------------------------------------- slide helpers
def fill(slide, idx, text):
    ph = slide.shapes.title if idx == 0 else slide.placeholders[idx]
    tf = ph.text_frame
    lines = text.split("\n")
    tf.text = lines[0]
    for line in lines[1:]:
        tf.add_paragraph().text = line
    return ph


def add_highlight(slide, x, y, w, h, radius):
    """Lime marker behind a phrase. Boxes are measured from the HTML render of the same text
    (reference/deck.html), so they line up with Space Grotesk, which Google Slides has built in.
    A run-level a:highlight would follow the text, but it cannot have rounded corners or the 0.08em overhang."""
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px(x), px(y), px(w), px(h))
    shp.name = "Highlight"
    shp.adjustments[0] = radius / min(w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = RGBColor.from_string(LIME)
    shp.line.fill.background()
    shp.shadow.inherit = False
    el = shp._element
    tree = el.getparent()
    tree.remove(el)
    tree.insert(2, el)  # behind every placeholder (after nvGrpSpPr and grpSpPr)
    return shp


def style_runs(shape, style, color=INK, align=None):
    size, lh, font, bold = style
    for p in shape.text_frame.paragraphs:
        p.line_spacing = Pt(lh / 2)
        if align:
            p.alignment = align
        for r in p.runs:
            r.font.size = Pt(size / 2)
            r.font.name = font
            r.font.bold = bold
            r.font.color.rgb = RGBColor.from_string(color)
            rPr = r._r.get_or_add_rPr()
            for tag in ("a:ea", "a:cs"):
                el = rPr.find(qn(tag))
                if el is None:
                    el = etree.SubElement(rPr, qn(tag))
                el.set("typeface", font)


def add_box(slide, x, y, w, h, fill_hex, radius=32, text=None, style=BODY_BOLD, pad=40):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px(x), px(y), px(w), px(h))
    shp.adjustments[0] = radius / min(w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = RGBColor.from_string(fill_hex)
    shp.line.fill.background()
    shp.shadow.inherit = False
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = px(pad)
    tf.margin_top = tf.margin_bottom = px(pad)
    tf.word_wrap = True
    if text is not None:
        tf.text = text
        style_runs(shp, style)
        from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for p in tf.paragraphs:
            p.alignment = PP_ALIGN.LEFT
    return shp


def add_text(slide, x, y, w, h, text, style=BODY, color=INK):
    tb = slide.shapes.add_textbox(px(x), px(y), px(w), px(h))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True
    tf.text = text
    style_runs(tb, style, color)
    return tb


def add_arrow(slide, x1, y, x2):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, px(x1), px(y), px(x2), px(y))
    c.line.color.rgb = RGBColor.from_string(INK)
    c.line.width = px(4)
    ln = c.line._get_or_add_ln()
    ln.append(parse_xml(f'<a:tailEnd {nsdecls("a")} type="triangle" w="lg" len="lg"/>'))
    return c


def remove_shape(shape):
    el = shape._element
    el.getparent().remove(el)


# ---------------------------------------------------------------- example slides
def build_slides(prs, L):
    s = prs.slides.add_slide(L["title"])
    fill(s, 0, "Building on Ethereum with agents")
    fill(s, 1, "Shiv Bhonde")
    fill(s, 2, "BuidlGuidl · @shivbhonde")

    s = prs.slides.add_slide(L["statement"])
    fill(s, 1, "An agent can scaffold a dapp. Shipping it is still your job.")
    add_highlight(s, 471, 410, 670, 157, 17)
    fill(s, 2, "What that looks like with Scaffold-ETH 2, step by step.")

    s = prs.slides.add_slide(L["heading-body"])
    fill(s, 0, "What the agent gets for free")
    fill(s, 1, "A contract, a deploy script and a frontend in one repo\nTyped hooks for every deployed contract\n"
               "A local chain, a burner wallet and a faucet\nA debug page that lists every function it can call")

    s = prs.slides.add_slide(L["heading-image"])
    fill(s, 0, "The debug page is the agent's first UI")
    remove_shape(s.placeholders[1])  # the sample image is placed at its natural aspect instead of cropped to the placeholder
    pic = s.shapes.add_picture(str(SAMPLE_IMAGE), px(447), px(234), px(1026), px(748))
    pic._element.spPr.prstGeom.set("prst", "roundRect")
    av = pic._element.spPr.prstGeom.find(qn("a:avLst"))
    av.append(parse_xml(f'<a:gd {nsdecls("a")} name="adj" fmla="val {round(24 / 748 * 50000)}"/>'))

    s = prs.slides.add_slide(L["three-columns"])
    fill(s, 0, "Three places to start")
    for i, (title, text) in enumerate((("SpeedRun Ethereum", "Seven challenges, from a simple NFT to a DEX."),
                                       ("Scaffold-ETH 2", "The toolkit for a real dapp, one command away."),
                                       ("BuidlGuidl batches", "Build with a cohort and ship a project together."))):
        fill(s, 1 + i * 2, title)
        fill(s, 2 + i * 2, text)

    s = prs.slides.add_slide(L["section"])
    fill(s, 1, "Part 2")
    fill(s, 0, "Give the agent a contract")

    s = prs.slides.add_slide(L["code"])
    fill(s, 0, "One command, one repo")
    fill(s, 1, "terminal")
    ph = fill(s, 2, "$ npx create-eth@latest\n? Your project name: my-dapp\n? Solidity framework: hardhat\n? Install packages: yes\n"
                    "\n$ cd my-dapp\n$ yarn chain\n$ yarn deploy\n$ yarn start")
    for p in ph.text_frame.paragraphs:  # prompt glyph in periwinkle light, like the HTML
        if p.runs and p.runs[0].text[:1] in "$?":
            txt = p.runs[0].text
            p.runs[0].text = txt[0]
            p.runs[0].font.color.rgb = RGBColor.from_string(PERIWINKLE_LIGHT)
            p.add_run().text = txt[1:]

    s = prs.slides.add_slide(L["quote"])
    fill(s, 1, "“Everything you need to build on Ethereum.”")
    fill(s, 2, "Scaffold-ETH 2")
    fill(s, 3, "scaffoldeth.io")

    s = prs.slides.add_slide(L["diagram"])
    fill(s, 0, "From contract to UI in Scaffold-ETH 2")
    boxes = (("Write the contract", LAVENDER, "Solidity, with Hardhat or Foundry", BODY_FONT),
             ("Deploy it", PEACH, "yarn deploy writes deployedContracts.ts", CODE_FONT),
             ("Read and write from React", PALE_LIME, "useScaffoldReadContract", CODE_FONT))
    for i, (label, fill_hex, under, under_font) in enumerate(boxes):
        x = 120 + i * 580
        add_box(s, x, 400, 520, 260, fill_hex, text=label)
        add_text(s, x, 692, 520, 100, under, style=(36, 47, under_font, False))
        if i < 2:
            add_arrow(s, x + 524, 530, x + 574)

    s = prs.slides.add_slide(L["closing"])
    fill(s, 0, "Thanks")
    fill(s, 1, "Shiv Bhonde")
    fill(s, 2, "@shivbhonde on X and GitHub")
    fill(s, 3, "buidlguidl.com")
    add_highlight(s, 116, 583, 356, 63, 7)

    s = prs.slides.add_slide(L["up-next"])
    fill(s, 0, "Building on Ethereum with agents")
    fill(s, 1, "Shiv Bhonde, BuidlGuidl")
    fill(s, 2, "13:15 · Workshop 1")


# ---------------------------------------------------------------- theme + master
def patch_theme(prs):
    from pptx.opc.constants import RELATIONSHIP_TYPE as RT
    theme = prs.slide_master.part.part_related_by(RT.THEME)
    xml = theme.blob.decode("utf-8")
    xml = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*', rf'\g<1>{HEAD_FONT}', xml)
    xml = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*', rf'\g<1>{BODY_FONT}', xml)
    for tag, val in (("dk1", INK), ("lt1", PAPER), ("dk2", INK), ("lt2", GREY), ("accent1", PERIWINKLE), ("accent2", ORANGE),
                     ("accent3", LIME), ("accent4", LAVENDER), ("accent5", PEACH), ("accent6", PERIWINKLE_LIGHT)):
        xml = re.sub(rf'<a:{tag}>.*?</a:{tag}>', f'<a:{tag}><a:srgbClr val="{val}"/></a:{tag}>', xml, flags=re.S)
    theme._blob = xml.encode("utf-8")
    # master ground = paper, so a slide with no layout background still looks right
    master = prs.slide_master._element
    bg = parse_xml(f'<p:bg {NS}><p:bgPr><a:solidFill><a:srgbClr val="{PAPER}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>')
    old = master.cSld.find(qn("p:bg"))
    if old is not None:
        master.cSld.remove(old)
    master.cSld.insert(0, bg)


def main():
    prs = Presentation()
    prs.slide_width = Emu(12192000)   # 13.333 in
    prs.slide_height = Emu(6858000)   # 7.5 in
    patch_theme(prs)
    layouts = build_layouts(prs)
    build_slides(prs, layouts)
    OUT.parent.mkdir(exist_ok=True)
    prs.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
