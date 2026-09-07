# The Spontaneous Cafe, website

Static site for Chef Matt Samuelson, Mendocino. Plain HTML, CSS and JS. No framework, no dependencies beyond Python 3 for the build.

## Build

```bash
python3 build.py
```

Writes `dist/`. Preview locally:

```bash
python3 -m http.server 8787 -d dist
```

## Layout

- `src/layout.html`: the shell (head, header, nav, footer). Every page is poured into it.
- `src/pages/*.html`: one file per page. A JSON meta block in an HTML comment at the top, then the page body.
- `src/assets/css/site.css`: design tokens and every component.
- `src/assets/js/site.js`: mobile nav, hero video (pauses off screen, off under reduced motion), reveal on scroll, seasonal menu tabs, contact form fallback.
- `src/assets/logo/`: the wordmark traced from the original JPG into SVG (potrace), plus light variant, tagline, credit and favicon.
- `src/assets/img/`, `src/assets/video/`: placeholders until Matt's own photos and the AI-generated loops land. See `docs/SWAP-LIST.md`.
- `docs/directions-board.html`: the six visual directions shown to Mohammed. Direction C won.
- `CONTEXT.md`: every decision and every client fact. Read it before changing anything.

## Deploy

`vercel.json` runs the build and serves `dist/`. From this folder:

```bash
npx vercel
```

Then point `spontaneouscafe.com` at Vercel from GoDaddy DNS (A record to Vercel, CNAME for www). The GoDaddy site stays untouched until the DNS switch.

## Contact form

The form posts to Formspree (form `maeypdpl`) by AJAX with a plain POST as the no-JS fallback. Submissions arrive by email.
