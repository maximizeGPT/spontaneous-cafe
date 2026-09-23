# Search and measurement setup

The official domain is `https://spontaneouscafe.com`. The owner confirmed the existing Google Business Profile is already set up. Reuse it; do not create a duplicate.

## Direct GA4 setup

The site uses the Google tag (`gtag.js`) directly. No GTM container, JSON import, or GTM publication is required. The previously prepared `gtm-production.json` is obsolete and must not be used for this setup.

- Google account: `siddh991@gmail.com`.
- Stream: `Spontaneous Cafe Website`, ID `15834223460`.
- Measurement ID: `G-VCT34ZQC92` (already the build default).
- Production origin: `https://spontaneouscafe.com`.
- Demo: `https://spontaneous-cafe.vercel.app/`, never tracked.

Production builds include the measurement ID only when `SITE_URL` uses the exact production hostname. Preview/review builds suppress it. Runtime additionally requires HTTPS and the configured hostname. An explicit empty `GA4_ID` disables tracking; a valid `GA4_ID` overrides the default. `GTM_ID` is no longer used.

The tag loads only after analytics consent. It sends one page view and the explicit events below, with sanitized page paths and referrer origins. Ads consent stays denied and Google Signals/ad personalization are disabled in the configuration. Cookie preferences and withdrawal remain available.

| Event | Additional parameters | GA4 key event? |
|---|---|---|
| `generate_lead` | `lead_service`, `lead_tier` | Yes |
| `phone_click` | None | No |
| `email_click` | None | No |
| `inquiry_error` | `error_category` | No |

All events include sanitized page location, referrer, title and path. Contact details and free-text form fields are never forwarded.

## Before publishing the website

1. In GA4's web stream, turn **Enhanced measurement off**. It was on at the last account inspection. This prevents automatic form/outbound/history events from bypassing the site's explicit event and URL controls.
2. Mark `generate_lead` as a key event. Optional reporting dimensions: `lead_service` and `lead_tier`.
3. Keep user-provided data collection, Google Signals and advertising personalization off; use two-month event retention initially.
4. Deploy the updated site with `SITE_URL=https://spontaneouscafe.com`. The GA4 ID defaults to `G-VCT34ZQC92`; confirm an existing Vercel override does not blank or replace it.
5. Once the custom domain serves this deployment, accept analytics and verify a page view in GA4 Realtime.

The owner retains final Submit/Publish actions. This code change alone does not deploy the site or verify Google account settings. Leave the unused GTM container unpublished and do not add a second Google snippet.

## 3. Domain and indexing

Before calling this launched, verify the official domain actually serves this repository’s deployment. The planning review found the old site there. Connect the domain in the correct Vercel project and update only the necessary DNS records, preserving mail records. `www` redirects to the official apex when both are connected. `/privacy-policy/` redirects to `/privacy/`; `/foraging` normalizes to `/foraging/`.

Preview builds get noindex metadata and an empty sitemap. Vercel aliases receive an `X-Robots-Tag: noindex, follow` header, including the production alias. Confirm this on deployed HTTP responses; the local Python preview server does not apply Vercel rules.

Verify the existing Search Console property or add a Domain property using DNS verification. Submit `https://spontaneouscafe.com/sitemap.xml`. Inspect home and all four service pages. Use the existing Business Profile’s website link for the official domain; no duplicate profile is needed.

## 4. Verification

Run the build with Python and Pillow installed, then:

```
python3 -m unittest discover -s tests
node --test tests/analytics.test.cjs
node tests/browser.cjs
node tests/layout.cjs
```

The browser tests require Playwright and Chrome (or `BROWSER_CHANNEL` for another installed Playwright channel). Their network is intercepted; they never submit real inquiries.

On the real production hostname, verify:

- No Google requests before acceptance or after rejection, including subsequent page visits.
- Acceptance loads one Google tag and sends one page view. No duplicate Google tag installation.
- Cookie preferences remain available; withdrawal removes Analytics cookies, disables collection and reloads. Rejection in another tab stops collection here too. Reloading clears any unsent form entries; no inquiry data is stored just to restore the form.
- `generate_lead` fires once only after Formspree success. Form validation/network failure produces no lead. Owner-notification failure cannot change an accepted inquiry into a failure.
- Network payloads contain no name, email, phone, message, raw query strings or fragments. Confirm sanitized page location/referrer on automatic and custom hits in the live Google tag.
- Analytics continues to work under the deployed CSP. Google Ads and Tag Assistant overlay resources are intentionally not broadly allowed; add narrowly scoped resources only if a chosen feature needs them.
- If using DebugView, enable a temporary Google tag `debug_mode` setting for owner testing only, and remove it before deploying the final site. Verify reports after processing; do not promise a fixed propagation time.
- Coordinate any real test inquiry with Matt and verify receipt in Formspree/the configured inbox. Account creation and a local test do not prove delivery or live GA4 collection.

## Reporting and optional advertising

Track organic clicks/queries in Search Console and landing pages, source/medium, successful inquiries and service interest in GA4. Qualified inquiries and actual bookings need owner follow-up; a submitted form does not prove a sale.

Initial collection intentionally drops query strings and fragments and reduces referrers to their origin. This protects contact information but means UTM/GCLID attribution is not implemented yet. Before launching ads or adding a tagged Business Profile link, add an explicitly validated campaign-attribution design and test that it preserves the chosen campaign identifiers without forwarding other URL values.

Google Ads is a separate optional activation. Confirm a spending cap and service focus first; link GA4, import `generate_lead` as the primary lead conversion with one-count settings, and leave phone/email taps secondary. Do not also count the same inquiry through a native Ads conversion. Recheck consent/CSP and live attribution before any campaign spends. Previous promotional-credit and budget assumptions are not current authorization.

## Performance and remaining owner-dependent work

Production now installs pinned Pillow and fails if it is missing, so responsive image generation cannot silently disappear. CSS/JS are content-hashed; stable image filenames use one-day revalidation instead of a one-year immutable policy. Photos and page layout remain intact.

Vercel runs the build in an isolated `uv` Python 3.12 environment with `requirements.txt`. The inherited `PYTHONPATH` is removed for this command because Vercel’s automatic dependency directory can contain native extensions built for a different Python version. Do not replace this with a system `pip install` or a bare `python3` build on Vercel.

Still to verify with account/domain access: production-domain migration, Search Console ownership/indexing, GA4 settings, real lead delivery and production PageSpeed/Core Web Vitals. There is no field-performance score until it has been measured. The existing labeled sample testimonials remain unchanged and have no review schema.
