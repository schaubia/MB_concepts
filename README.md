# Molecular Mechanisms — Interactive Explainers (single-file version)

Everything — the shared styling, every animation's SVG/CSS/JS, the
registry, and the Streamlit UI — lives in `app.py`. No other files needed
besides `requirements.txt`.

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How it's structured (inside app.py)

1. `COMMON_STYLE` — shared CSS variables/classes (colors, text styles) used
   by every diagram. Change once, everything updates.
2. One string constant per mechanism/level, e.g. `GPCR_GENERAL`,
   `DNA_REPLICATION_TECHNICAL` — each is a self-contained SVG + `<style>` +
   `<script>` block with its own `step` counter and `render()` function.
3. `REGISTRY` — a dict mapping mechanism name → level → which constant to
   show, its iframe height, and a one-line description.
4. Sidebar + rendering logic at the bottom.

## To modify an existing animation

Find its string constant (e.g. `MITOSIS_GENERAL`) and edit the SVG shapes,
the `labels` array, or the `render()` JS directly inside the string. Since
your editor won't syntax-highlight HTML/JS inside a Python string, work
carefully — a stray unescaped `'''` would break the file (none of the
current diagrams use one).

## To add a new mechanism

1. Add a new constant near the others:
   ```python
   TRANSLATION_GENERAL = '''
   <svg ...>...</svg>
   <script>...</script>
   '''
   ```
2. Add one entry to `REGISTRY`:
   ```python
   "Translation": {
       "General": {
           "fragment": TRANSLATION_GENERAL,
           "height": 500,
           "blurb": "One sentence describing the animation.",
       },
   },
   ```

No existing constants or registry entries need to change.

## Deploy / share

Push to a GitHub repo and deploy on Streamlit Community Cloud
(https://streamlit.io/cloud) — point it at `app.py`.
