# Recipe: HTML

Build from `reference/deck.html`. It already has the 1920x1080 canvas, the backgrounds, the type scale, every layout's positions as CSS, and the Google Fonts link for Space Grotesk and Space Mono.

## Steps

1. Create `decks/` and copy `reference/deck.html` to `decks/<talk-slug>.html`. Set its `<title>` to the talk title. The deck loads `../backgrounds/*.png`, so it runs from inside the kit folder: present from the whole kit folder, and put your own images in `decks/img/`.
2. Keep the kit's `<style>` block as it is; your additions, like the presenting and print rules below, go in a second `<style>` block before `</body>`. Each `<section class="slide ...">` is one layout, named in the comment above it and in `data-name`. Copy the sections you need, in your order, and replace their text; delete the sample sections you do not use. Every element sits in one of the section's existing slots, since the slots are the layout's positions.
3. Highlight a phrase by wrapping it in `<mark>`. An image goes in `.panel` as an `<img>` with its own width and height, scaled to fit 1600x648.
4. For a Diagram, copy the `.flow` block: boxes are `.box` with a colour class at left 0, 580 and 1160, captions are `.under` at the same lefts, and the arrows are the inline SVGs at left 520 and 1100.
5. Keep the script at the bottom. `EVENT_LINE` fills the corner of Title and Closing, and `?slide=N` shows one slide alone.

## Presenting

The file shows every slide in a column. To present from the browser, add this before `</body>`: press `p` to enter presenting mode, then put the browser in full screen and step with the arrow keys.

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
    if (e.metaKey || e.ctrlKey || e.altKey) return;   // leave Cmd+P and other shortcuts alone
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

Add these print rules to your second `<style>` block, then print with Chrome. The PDF has the fonts embedded and one 1920x1080 page per slide; present it full screen if the browser cannot.

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

Render every slide to a PNG and look at each one. This needs network for Google Fonts; the last line prints the fonts that loaded, and it must say `Space Grotesk, Space Mono`, or every check is against a fallback font.

```sh
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DECK="file://$PWD/decks/<talk-slug>.html"
mkdir -p decks/png
n=$(grep -c '<section class="slide' decks/<talk-slug>.html)
for i in $(seq 1 $n); do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1920,1080 \
    --virtual-time-budget=10000 --screenshot="decks/png/$(printf %02d $i).png" "$DECK?slide=$i" 2>/dev/null
done
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=10000 --dump-dom "$DECK?slide=1" 2>/dev/null | grep -o 'data-fonts="[^"]*"'
```
