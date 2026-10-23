# Recipe: HTML

Build from `reference/deck.html`. It already has the 1920x1080 canvas, the backgrounds, the type scale, every layout's positions as CSS, and the Google Fonts link for Space Grotesk and Space Mono.

## Steps

1. Copy `reference/deck.html` to `decks/<talk-slug>.html`. The background paths (`../backgrounds/*.png`) resolve from there too.
2. Keep the `<style>` block as it is. Each `<section class="slide ...">` is one layout, named in the comment above it and in `data-name`. Copy the sections you need, in your order, and replace their text; delete the sample sections you do not use. Every element sits in one of the section's existing slots, since the slots are the layout's positions.
3. Highlight a phrase by wrapping it in `<mark>`. An image goes in `.panel` as an `<img>` with its own width and height, scaled to fit 1600x648.
4. For a Diagram, copy the `.flow` block: boxes are `.box` with a colour class at left 0, 580 and 1160, captions are `.under` at the same lefts, and the arrows are the inline SVGs at left 520 and 1100.
5. Keep the script at the bottom. `EVENT_LINE` fills the corner of Title and Closing, and `?slide=N` shows one slide alone.

## Presenting

The file shows every slide in a column. To present it, add this before `</body>`: press `p` to enter presenting mode, then put the browser in full screen and step with the arrow keys.

```html
<style>
  html.present { background: #000; overflow: hidden; }
  html.present .slide { display: none; position: fixed; left: 50%; top: 50%; }
  html.present .slide.show { display: block; }
</style>
<script>
  const slides = [...document.querySelectorAll(".slide")];
  const root = document.documentElement;
  let at = 0;
  const show = () => {
    const on = root.classList.contains("present");
    const k = Math.min(innerWidth / 1920, innerHeight / 1080);
    slides.forEach((s, i) => {
      if (on) s.classList.toggle("show", i === at);
      s.style.transform = on ? `translate(-50%, -50%) scale(${k})` : "";
    });
  };
  addEventListener("keydown", e => {
    if (e.key === "p") root.classList.toggle("present");
    if (["ArrowRight", " ", "PageDown"].includes(e.key)) at = Math.min(at + 1, slides.length - 1);
    if (["ArrowLeft", "PageUp"].includes(e.key)) at = Math.max(at - 1, 0);
    show();
  });
  addEventListener("resize", show);
</script>
```

Offline, the fonts come from the presenting laptop instead of Google Fonts: install Space Grotesk and Space Mono from fonts.google.com, and the `font-family` names resolve to the installed copies.

## PDF backup

Add a print stylesheet inside the `<style>` block, then print with Chrome. The PDF has the fonts embedded and one 1920x1080 page per slide; present it full screen if the browser cannot.

```css
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body { background: none; }
  .deck { display: block; padding: 0; }
  .slide { break-after: page; }
}
```

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=10000 --print-to-pdf="decks/<talk-slug>.pdf" "file://$PWD/decks/<talk-slug>.html"
```

## Look at the slides

Open the file in Chrome at 100% zoom; every slide shows at 1920x1080 in a column. For PNGs, render each slide the way `build/render.sh` does: a headless Chrome screenshot of `decks/<talk-slug>.html?slide=N` at window size 1920x1080.
