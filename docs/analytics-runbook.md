# Search and measurement setup

The official domain is `https://spontaneouscafe.com`. The owner confirmed the existing Google Business Profile is already set up. Reuse it; do not create a duplicate.

## Activation status

The site integration is implemented, but tracking is off until **both** `GTM_ID` and `GA4_ID` are configured in the Vercel Production environment and the GTM container below is published. IDs are public identifiers, not passwords. The owner is creating the accounts and will provide the IDs.

Do not copy `docs/ads-2026-09-19/tracking-spec.md`: it predates this implementation. No contact details or user-provided-data features should be added to the data layer.

## 1. Owner account setup

1. Create an owner-controlled Google Analytics account/property for The Spontaneous Cafe. Use Los Angeles reporting time and USD. Create a Web data stream for `https://spontaneouscafe.com`; record its Measurement ID (`G-…`).
2. In the stream, turn **Enhanced measurement off** for the initial setup. The Google tag supplies the standard page view; our code supplies the explicit inquiry and contact events. This prevents generic form-submit events, automatic outbound URLs and history changes from bypassing our event/URL controls.
3. Turn off user-provided data collection, Google Signals and advertising personalization. Use two-month event-data retention initially. Do not enable enhanced conversions or remarketing.
4. Create an owner-controlled Google Tag Manager account and Web container; record its Container ID (`GTM-…`). Do not also paste a Google tag snippet into the HTML.

## 2. GTM configuration — required before enabling the IDs

Create Version 2 Data Layer Variables with the following names/keys:

| GTM variable name | Data layer variable name |
|---|---|
| DLV – page location | `analytics_page_location` |
| DLV – page referrer | `analytics_page_referrer` |
| DLV – page title | `analytics_page_title` |
| DLV – service | `lead_service` |
| DLV – tier | `lead_tier` |
| DLV – page path | `page_path` |
| DLV – error | `error_category` |

Create one **Google tag**, Tag ID equal to the GA4 Measurement ID. Trigger: Custom Event named `analytics_ready`, not All Pages. Set these configuration parameters:

| Parameter | Value |
|---|---|
| `page_location` | `{{DLV – page location}}` |
| `page_referrer` | `{{DLV – page referrer}}` |
| `page_title` | `{{DLV – page title}}` |
| `allow_google_signals` | `false` (boolean) |
| `allow_ad_personalization_signals` | `false` (boolean) |
| `send_page_view` | `true` (boolean) |

Require additional consent `analytics_storage` for all Analytics tags. The site provides default-denied consent and grants only analytics after acceptance. Never add another consent initializer that overrides this choice.

Create a **GA4 Event tag** for each row below using the same Measurement ID and a Custom Event trigger with the exact event name. Add `page_location`, `page_referrer` and `page_title` to each event tag from the same DLVs as the Google tag. This makes the sanitized values explicit on every event.

| Event/tag/trigger name | Additional event parameters | GA4 key event? |
|---|---|---|
| `generate_lead` | `lead_service` = service DLV, `lead_tier` = tier DLV, `page_path` = path DLV | Yes |
| `phone_click` | `page_path` = path DLV | No |
| `email_click` | `page_path` = path DLV | No |
| `inquiry_error` | `error_category` = error DLV, `page_path` = path DLV | No |

Register event-scoped custom dimensions `lead_service` and `lead_tier` in GA4 if needed for reports. Do not use raw DOM/form values or Custom HTML/Custom JavaScript tags. Do not add automatic form triggers.

Publish the container, then set Vercel Production variables:

```
SITE_URL=https://spontaneouscafe.com
GTM_ID=<actual container ID>
GA4_ID=<actual measurement ID>
```

Redeploy: these are build-time settings. Leave IDs unset on Preview. Setting only one ID does not activate analytics. The code also requires HTTPS and the exact configured hostname; local and Vercel alias visits never send measurement.

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
- Acceptance loads one GTM container and sends one page view. No duplicate Google tag installation.
- Cookie preferences remain available; withdrawal removes Analytics cookies, disables collection and reloads. Rejection in another tab stops collection here too. Reloading clears any unsent form entries; no inquiry data is stored just to restore the form.
- `generate_lead` fires once only after Formspree success. Form validation/network failure produces no lead. Owner-notification failure cannot change an accepted inquiry into a failure.
- Network payloads contain no name, email, phone, message, raw query strings or fragments. Confirm sanitized page location/referrer on automatic and custom hits in the actual published container.
- Analytics continues to work under the deployed CSP. Google Ads and GTM preview overlay resources are intentionally not broadly allowed; add narrowly scoped resources only if a chosen feature needs them.
- If using DebugView, enable a temporary GTM `debug_mode` setting for owner testing only, and remove it before publishing the final container. Verify reports after processing; do not promise a fixed propagation time.
- Coordinate any real test inquiry with Matt and verify receipt in Formspree/the configured inbox. Account creation and a local test do not prove delivery or live GA4 collection.

## Reporting and optional advertising

Track organic clicks/queries in Search Console and landing pages, source/medium, successful inquiries and service interest in GA4. Qualified inquiries and actual bookings need owner follow-up; a submitted form does not prove a sale.

Initial collection intentionally drops query strings and fragments and reduces referrers to their origin. This protects contact information but means UTM/GCLID attribution is not implemented yet. Before launching ads or adding a tagged Business Profile link, add an explicitly validated campaign-attribution design and test that it preserves the chosen campaign identifiers without forwarding other URL values.

Google Ads is a separate optional activation. Confirm a spending cap and service focus first; link GA4, import `generate_lead` as the primary lead conversion with one-count settings, and leave phone/email taps secondary. Do not also count the same inquiry through a native Ads conversion. Recheck consent/CSP and live attribution before any campaign spends. Previous promotional-credit and budget assumptions are not current authorization.

## Performance and remaining owner-dependent work

Production now installs pinned Pillow and fails if it is missing, so responsive image generation cannot silently disappear. CSS/JS are content-hashed; stable image filenames use one-day revalidation instead of a one-year immutable policy. Photos and page layout remain intact.

Still to verify with account/domain access: production-domain migration, Search Console ownership/indexing, published GA4/GTM settings, real lead delivery and production PageSpeed/Core Web Vitals. There is no field-performance score until it has been measured. The existing labeled sample testimonials remain unchanged and have no review schema.
