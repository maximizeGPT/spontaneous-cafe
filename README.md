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

## Hero video loops

The five loops are AI-generated from the placeholder photos with fal.ai (MiniMax Hailuo 02, image-to-video, 768p, 6 s, about $0.27 a clip). Ambience only: motion added to an existing photo, never a dish invented. When Matt's own photos land, regenerate from those.

```bash
set -a; . ./.env; set +a; python3 tools/gen-video.py        # all five, or name shots
./tools/place-video.sh                                       # ping-pong loop, 1280 wide, posters cut from frame 0
```

Keys live in `.env` (gitignored): `FAL_KEY`, `MINIMAX_API_KEY`, `VERCEL_TOKEN`.

## Deploy

```bash
set -a; . ./.env; set +a; npx vercel deploy --prod --yes --token "$VERCEL_TOKEN"
```

Production: https://spontaneous-cafe.vercel.app (project `spontaneous-cafe`, team `mohsprojects`).
