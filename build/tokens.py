"""Reads design/tokens.json, the kit's single source of truth, and writes design/tokens.css from it.

    python3 build/tokens.py               writes design/tokens.css
    python3 build/tokens.py get <path>    prints one value: color.ink -> #182232, type.tag.fontSize -> 36,
                                          font.family.mono -> Space Mono, mark.castle-height -> 44

The other build scripts import it: `from tokens import Tokens; T = Tokens()`.
The file follows the W3C Design Tokens Community Group format (designtokens.org, 2025.10):
$type, $value, $description, {alias} references and a kit-specific $extensions key.
"""
import json
import re
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
TOKENS = KIT / "design" / "tokens.json"
CSS = KIT / "design" / "tokens.css"
EXT = "com.buidlguidl.slide-kit"
ALIAS = re.compile(r"^\{([^{}]+)\}$")


class Tokens:
    def __init__(self, path=TOKENS):
        self.raw = json.loads(path.read_text())

    # ---- lookup
    def node(self, path):
        n = self.raw
        for part in path.split("."):
            n = n[part]
        return n

    def resolve(self, v):
        """Follows {group.token} aliases, inside composite values too."""
        if isinstance(v, str) and (m := ALIAS.match(v)):
            return self.value(m.group(1))
        if isinstance(v, dict):
            return {k: self.resolve(x) for k, x in v.items()}
        if isinstance(v, list):
            return [self.resolve(x) for x in v]
        return v

    def value(self, path):
        return self.resolve(self.node(path)["$value"])

    def description(self, path):
        return self.node(path).get("$description", "")

    def ext(self, path):
        return self.node(path).get("$extensions", {}).get(EXT, {})

    def tokens(self, group):
        """(name, node) for every token directly in a group, in file order."""
        return [(k, v) for k, v in self.node(group).items() if not k.startswith("$")]

    # ---- typed helpers
    def hex(self, name):
        return self.value(f"color.{name}")["hex"].upper()

    def rgb(self, name):
        h = self.hex(name)
        return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))

    def px(self, path):
        return self.value(path)["value"]

    def family(self, name):
        return self.value(f"font.family.{name}")[0]

    def stack(self, name):
        return ", ".join(f'"{f}"' if " " in f else f for f in self.value(f"font.family.{name}"))

    def style(self, role):
        """One type style, flattened: size and line height in px, family name, weight, and bold for pptx."""
        v = self.value(f"type.{role}")
        size = v["fontSize"]["value"]
        return {
            "size": size,
            "line": v["lineHeight"],
            "line_px": round(size * v["lineHeight"]),
            "family": v["fontFamily"][0],
            "stack": ", ".join(f'"{f}"' if " " in f else f for f in v["fontFamily"]),
            "weight": v["fontWeight"],
            "letter": v["letterSpacing"]["value"],
            "bold": self.ext(f"type.{role}").get("pptxBold", v["fontWeight"] >= 700),
        }


# ---- outputs
def css_value(T, path, node):
    t = node.get("$type") or T.node(path.rsplit(".", 1)[0]).get("$type")
    v = T.resolve(node["$value"])
    if t == "color":
        return v["hex"].upper()
    if t == "dimension":
        return f'{v["value"]}{v["unit"]}'
    if t == "fontFamily":
        return ", ".join(f'"{f}"' if " " in f else f for f in v)
    if t == "number":
        unit = T.node(path.rsplit(".", 1)[0]).get("$extensions", {}).get(EXT, {}).get("unit", "")
        return f"{v}{unit}"
    return str(v)


def write_css(T, out=CSS):
    lines = ["/* Generated from design/tokens.json by build/tokens.py. Edit the JSON, then run build/build.sh. */", ":root {"]

    def var(path):
        return "--" + path.replace(".", "-")

    def group(path):
        for name, node in T.tokens(path):
            p = f"{path}.{name}"
            desc = node.get("$description", "")
            lines.append(f"  {var(p)}: {css_value(T, p, node)};" + (f"  /* {desc} */" if desc else ""))

    lines.append("  /* colours */")
    group("color")
    lines.append("  /* fonts */")
    group("font.family")
    group("font.weight")
    lines.append("  /* type styles: a font shorthand per role, then its parts */")
    for role, node in T.tokens("type"):
        s = T.style(role)
        fam = "var(--font-family-mono)" if s["family"] == T.family("mono") else "var(--font-family-sans)"
        desc = node.get("$description", "")
        lines.append(f"  --type-{role}: {s['weight']} {s['size']}px/{s['line']} {fam};" + (f"  /* {desc} */" if desc else ""))
        lines.append(f"  --type-{role}-size: {s['size']}px; --type-{role}-line: {s['line']}; --type-{role}-weight: {s['weight']}; --type-{role}-family: {fam};")
    lines.append("  /* radius, canvas, margins, marks, highlight */")
    for g in ("radius", "canvas", "space", "mark", "highlight"):
        group(g)
    lines.append("}")
    out.write_text("\n".join(lines) + "\n")
    print("wrote", out)


def get(T, path):
    """A plain value for shell scripts: a hex, a number, a family name or a description."""
    parts = path.split(".")
    for i in range(len(parts), 0, -1):
        try:
            node = T.node(".".join(parts[:i]))
        except KeyError:
            continue
        if isinstance(node, dict) and "$value" in node:
            v = T.resolve(node["$value"])
            for sub in parts[i:]:
                v = v[sub]
            if isinstance(v, dict) and "hex" in v:
                return v["hex"].upper()
            if isinstance(v, dict) and "unit" in v:
                return v["value"]
            if isinstance(v, list):
                return v[0]
            return v
    raise KeyError(path)


if __name__ == "__main__":
    T = Tokens()
    if len(sys.argv) == 3 and sys.argv[1] == "get":
        print(get(T, sys.argv[2]))
    else:
        write_css(T)
