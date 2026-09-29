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

### Review markup and `REVIEW=1`

Pages can carry two kinds of internal, not-for-visitors markup: a `<span class="tag-confirm">confirm with Matt</span>`
chip flagging a fact that needs sign-off, and a `ph` class on any placeholder image or figure. A plain `python3 build.py`
(what Vercel runs in production) strips both from every page, so visitors never see a chip or a "placeholder" badge.
To keep them for an internal review pass, set `REVIEW=1`:

```bash
REVIEW=1 python3 build.py
```

The build prints which mode it ran in (`review` or `production`).

## Layout

- `src/layout.html`: the shell (head, header, nav, footer). Every page is poured into it.
- `src/pages/*.html`: one file per page. A JSON meta block in an HTML comment at the top, then the page body.
- `src/assets/css/fonts.css`: `@font-face` rules for the self-hosted latin subsets in `src/assets/fonts/`
  (Lora upright and italic, Source Sans 3 upright and italic, all variable woff2 pulled from the
  Google Fonts API). The site makes no request to fonts.googleapis.com or fonts.gstatic.com.
- `src/assets/css/site.css`: design tokens and every component.
- `src/assets/js/site.js`: mobile nav, hero video (pauses off screen, off under reduced motion), reveal on scroll, seasonal menu tabs, contact form fallback.
- `src/assets/logo/`: the wordmark traced from the original JPG into SVG (potrace), plus light variant, tagline, credit and favicon.
- `src/assets/img/`, `src/assets/video/`: placeholders until Matt's own photos and the AI-generated loops land. See `docs/SWAP-LIST.md`.
- `docs/directions-board.html`: the six visual directions shown to Mohammed. Direction C won.
- `CONTEXT.md`: every decision and every client fact. Read it before changing anything.

## Cache busting

`build.py` copies `site.css`, `fonts.css` and `site.js` into `dist/assets/` under a content hash
(`site.3d56f943.css`) and rewrites the layout's references. That is what makes the one-year
`immutable` cache header in `vercel.json` safe: a changed file gets a new name, so nothing goes stale.
The woff2 files are not hashed, they never change.

## Security headers

Set in `vercel.json` for every path: HSTS, `X-Content-Type-Options`, `Referrer-Policy`,
`Permissions-Policy`, `X-Frame-Options` and a Content-Security-Policy. The only cross-origin
destination the policy allows is `https://formspree.io`, for the contact form.

The CSP carries `style-src 'self' 'unsafe-inline'` only because a handful of pages still have inline
`style` attributes. Once those are gone from `src/pages/`, drop `'unsafe-inline'` from the
`Content-Security-Policy` value and rebuild. Check first with:

```bash
grep -rc 'style="' dist --include='*.html'
```

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

## Instant text on each inquiry

`api/notify.js` is a Vercel function the contact form calls after a successful Formspree post. It texts Matt through Twilio and, or instead, pushes to Telegram. Configure in Vercel > Settings > Environment Variables:

| Variable | Purpose |
|---|---|
| `TWILIO_SID`, `TWILIO_TOKEN`, `TWILIO_FROM` | Twilio account and sending number (E.164). Needs the one-time Sole Proprietor A2P 10DLC registration, about $4.50 and under a week. |
| `OWNER_PHONE` | Matt's mobile, E.164. |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` | Free alternative: create a bot with @BotFather, message it once, read the chat id. |
| `CONFIRM_INQUIRER=1` | Also text the inquirer a confirmation when they leave a phone number. |

With no variables set the function returns "skipped" and the form still works through Formspree.

## Responsive images

`tools/images.py` writes 480, 800 and 1200 px JPEG and WebP variants next to every photo in `src/assets/img/`. The build wraps any `<img src="/assets/img/x.jpg">` that has variants in a `<picture>` with WebP and JPEG `srcset`. Add `data-sizes="..."` on an `<img>` to override the default `sizes`. Run the tool after adding photos.

## Launch

`docs/LAUNCH-CHECKLIST.md` is the DNS cutover, verification and rollback procedure. `docs/to-questionnaire-matt.md` is the list of client facts still to confirm.

`docs/seo-2026-09-19/SEO-PLAN.md` is the SEO round's plan, and `docs/seo-2026-09-19/OFFSITE-CHECKLIST.md` is the off-site checklist that goes with it.
