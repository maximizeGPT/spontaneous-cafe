# SEO, Analytics and Optional Google Ads Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task. This document is a plan, not authorization to activate tracking or spend on advertising.

**Goal:** Help people find Matt’s services through local search and measure which visits turn into inquiries, with an optional path to Google Ads.

**Architecture:** Keep the current static website. Establish one production domain, strengthen existing service pages, and install GA4 through a single Google Tag Manager container with consent controls. Add paid acquisition only after successful inquiry measurement is verified.

**Tech Stack:** Static HTML/CSS/JavaScript, Python build, Vercel, Formspree, Google Search Console, Google Business Profile, GTM, GA4; Google Ads optional.

**Spec:** User request dated September 21, 2026: “Make a plan to update the site for SEO optimization. I want it to work with Google Analytics / (potentially ads?)”. Assumption: ads means purchasing Google Ads to attract customers, rather than placing display advertising on the website.

**Implementation update:** The user subsequently authorized implementation from main, confirmed `spontaneouscafe.com` and an existing Google Business Profile, and chose to create GA4/GTM accounts and supply the IDs. Site-side changes and automated verification are implemented; activation, domain migration, account configuration and production measurement remain pending. See `docs/analytics-runbook.md` for the current setup instructions. Testimonials and their existing sample disclosure remain unchanged. No advertising campaign is authorized or active.

## Global constraints

- Preserve the current design, approved photography and corrected biographical facts.
- Measure inquiries; a phone tap is not a completed call or booking.
- Keep names, email addresses, phone numbers and free-text inquiry content out of analytics and the data layer.
- No placeholder tracking IDs, duplicate tag installations or advertising spend during planning.
- Keep business accounts under the owner’s control. Account access and DNS access are implementation dependencies.
- Earlier files in `docs/seo-2026-09-19/` and `docs/ads-2026-09-19/` are research inputs, not verified current configuration. This plan supersedes the earlier tracking specification: do not copy its `user_data` payload or enable enhanced conversions by default. Revalidate previous budget, promotion and ad-copy assumptions.

## Review focus

- Public domain and deployment alias must not present conflicting indexable versions.
- Failed or repeated form submissions must not create false leads.
- Declined or withdrawn consent must be respected; the contact form must still work.
- Preview visits and personal information must not enter production analytics.
- Production image optimization and page performance must match local output.

## Findings as of September 21

The source already supplies unique metadata, canonical URLs, social previews, a sitemap, robots.txt, responsive image markup and business/service structured data. This is refinement, not an SEO rebuild.

The public `https://spontaneouscafe.com/` returned the older website during this review, including outdated teaching copy. The new build hardcodes this domain in canonical URLs and its sitemap. The Vercel alias could not be retrieved through the web tool; its current deployment status remains unverified.

No Analytics or GTM installation exists. `vercel.json` currently blocks Google scripts and collection requests. The privacy page explicitly says there is no analytics or cookies. The form submits asynchronously to Formspree, so its confirmed success branch is the correct measurement point.

The earlier technical audit identified missing Pillow in production. The current repository still has no `requirements.txt`, and `build.py` silently falls back when image dimensions cannot be read. A successful local build therefore does not establish that production serves responsive images.

## 1. Establish the production and indexing foundation — first priority

**Files:** `build.py`, `src/layout.html`, `vercel.json`, new `requirements.txt`; DNS/Vercel/Search Console settings.

- [ ] Verify domain ownership, active DNS, current Vercel deployment and existing Google Search Console properties.
- [ ] Connect the updated deployment to the chosen production host, preserving mail-related DNS records. Inventory old URLs and map each to its closest replacement, including `/foraging` and `/privacy-policy`.
- [ ] Centralize the site origin so canonical URLs, social images, structured data and sitemap entries agree. Redirect host variants consistently. Protect preview deployments from indexing; do not rely on a canonical hint alone.
- [ ] Declare and install a tested Pillow version in the production build, and fail clearly if image processing prerequisites are missing.
- [ ] Verify real HTTP status codes, redirect chains, missing-page 404s, image URLs, canonical tags, robots rules and sitemap URLs on production. Confirm responsive picture/srcset output exists there.
- [ ] Verify a Search Console domain property, submit the sitemap and inspect the home page plus four service pages. Record initial indexing and search performance; request indexing where appropriate without promising immediate inclusion.

**Acceptance:** The public domain serves the updated site; canonical targets return the intended content; legacy links resolve; production image output is verified.

## 2. Improve service pages and local credibility

**Files:** `src/pages/index.html`, `about.html`, `foraging.html`, `private-chef.html`, `catering.html`, `cooking-classes.html`, `contact.html`; `build.py` for structured data.

| Page | Initial search intent to validate with Search Console/keyword research |
|---|---|
| Home | The Spontaneous Cafe; Chef Matt Samuelson; Mendocino culinary experiences |
| Foraging | Guided foraging experiences in Mendocino |
| Private chef | Private chef in Mendocino; chef for a vacation rental |
| Catering | Mendocino event and retreat catering |
| Cooking classes | Private cooking classes in Mendocino |
| About | Matt’s actual experience, training and connection to the coast |

- [ ] Refine titles, descriptions, main headings and opening paragraphs around one clear service intent per page. Avoid repetitive town pages and keyword stuffing.
- [ ] Confirm actual service areas, group sizes, costs, inclusions and availability with Matt; use consistent answers throughout the site. Retain resume-backed teaching language.
- [ ] Improve contextual links between relevant services, About and the inquiry form. Keep booking actions prominent on mobile.
- [ ] Validate existing business/service schema against visible facts. Use a stable business identifier and relevant Person/breadcrumb markup only where supported by page content. Do not invent a public storefront address or imply a restaurant if it is a service-area business.
- [ ] Keep useful visible FAQs, but remove automatic FAQPage generation as unnecessary maintenance: Google retired FAQ rich results in May 2026. Do not add fabricated ratings or review markup.
- [ ] Replace the explicitly labeled sample testimonials with permissioned, genuine customer quotes before using that section as public social proof; otherwise omit it from the public launch.
- [ ] Verify and complete the existing Google Business Profile with accurate services, contact details, service area and website link. Use a tagged website URL to distinguish profile referrals. Establish a routine for requesting genuine reviews and adding current photos.

**Acceptance:** Each service has a distinct purpose, accurate metadata and consistent booking details. Structured data describes the real business. Account settings require owner access to verify.

## 3. Install reliable, consent-aware measurement

**Files:** new `src/assets/js/analytics.js`, `src/layout.html`, `src/assets/js/site.js`, `src/assets/css/site.css`, `src/pages/privacy.html`, `build.py`, `vercel.json`; GA4/GTM configuration.

Recommend **GA4 through GTM** because the user may add Ads later. Use this single installation path; do not also embed a separate GA4 tag.

| Event | Trigger | Role |
|---|---|---|
| `page_view` | Consented page visit | Understand landing pages and channels |
| `generate_lead` | Confirmed successful Formspree response | Primary GA4 key event |
| `phone_click` | Click on site phone link | Secondary intent signal |
| `email_click` | Click on site email link | Secondary intent signal |
| `inquiry_error` | Submission failure, with controlled error category | Diagnose lost inquiries |

- [ ] Create or reuse owner-controlled GA4 and GTM accounts and record real public IDs. Configure timezone and production hostname restrictions; keep local and preview traffic out of production reports.
- [ ] Add an accessible consent interface with accept, reject and persistent preference controls. Recommend basic consent mode: no Google measurement requests before opt-in. Configure analytics and advertising consent separately; keep advertising features disabled initially. Determine applicable consent requirements for the business and visitors before launch.
- [ ] Initialize consent before tags. Consent Mode communicates a choice; it is not itself a consent banner. Update the privacy page to match the actual tools, purposes, retention settings and choices.
- [ ] Add a narrowly scoped analytics module and load it through the existing asset build. Use external self-hosted bootstrap code or CSP-compatible hashes; follow Google’s endpoint guidance without removing the existing security policy.
- [ ] Fire `generate_lead` once per successful submission, capturing only controlled service/tier labels before the form resets. Do not count button clicks, validation errors or notification-service failures as new leads. Avoid duplication with enhanced-measurement form events.
- [ ] Keep form values and personal details out of all event parameters, URLs and the data layer. Disable automatic user-provided data collection and enhanced conversions at launch. Do not assign a made-up monetary value to an inquiry.
- [ ] Test success, failure and repeat clicks against mocked form responses first. Verify one event per success, none for failures, no personal information, no duplicate pageviews and no tracking before consent. Check withdrawal, returning visitors and mobile keyboard access.
- [ ] Verify in Tag Assistant/GA4 DebugView and production network tools. Coordinate a clearly labeled live test inquiry with the owner to check delivery end to end. Confirm form use still works with tags blocked.

**Acceptance:** Successful inquiries are measurable without false conversions or contact-data leakage. Consent, production-only gating and security headers work together. A completed inquiry is still not a confirmed booking.

## 4. Check mobile performance and publish a useful report

**Files:** `src/layout.html`, `src/assets/css/site.css`, `src/assets/js/site.js`, `build.py`, affected images/video if measurements justify changes; new `docs/analytics-runbook.md`.

- [ ] Baseline the production home, foraging, private-chef and contact pages using mobile PageSpeed/Lighthouse; check available Search Console field data separately. Record results rather than inventing a score.
- [ ] Address measured bottlenecks, especially hero video loading, image selection, above-fold assets, font preloads and layout shifts. Retain the requested photography and design.
- [ ] Compare performance before/after tracking, consent controls and fixes. Avoid loading remarketing or unrelated marketing tools by default.
- [ ] Create a simple GA4 report for traffic source, landing page, service interest and successful inquiries. Pair it with Search Console search queries/clicks and Business Profile performance.
- [ ] Document account ownership, event definitions, tag changes, consent settings and verification steps. Record qualified inquiries and eventual bookings manually at first to evaluate lead quality.

**Acceptance:** Production performance has a documented baseline, no material regression from measurement, and the owner can see which channels/services produce inquiries. Review trends after roughly a month, allowing longer for low traffic; this is not a ranking deadline.

## 5. Optional Google Ads pilot — after measurement works

**Files/settings:** Reassess `docs/ads-2026-09-19/`; refine existing service landing pages only where necessary; Google Ads account settings.

- [ ] Confirm the service to promote, booking capacity, target audience and an explicit spending cap. Validate any promotional credit in the account rather than assuming the earlier offer still applies.
- [ ] Link GA4 and Google Ads. Use the verified `generate_lead` key event as the initial imported primary conversion, with one-count lead settings; keep phone/email taps secondary. Do not also count a separate native Ads conversion for the same inquiry.
- [ ] Start with a focused Search campaign for one or two services. Choose location targeting deliberately: people already on the coast and travelers planning a Mendocino trip are different audiences. Send searches to the matching service page.
- [ ] Recheck keyword demand, search terms, negative keywords, ad claims and landing-page facts. Avoid advertising activities Matt does not offer. Reuse prior draft research only after this review.
- [ ] Leave remarketing, Google Signals and enhanced conversions off initially. Reassess only if there is a concrete need and an appropriate consent/data-handling design.
- [ ] Evaluate cost per qualified inquiry and booked job, not clicks alone. Adjust or pause based on the agreed budget and lead quality. Separate account conversion configuration from live campaign activation.

**Acceptance:** No campaign spends before budget approval, destination checks and conversion verification. SEO and paid acquisition have separate reports; no assumed ranking benefit from buying ads.

## Owner inputs needed at implementation

Access to the production domain/Vercel project; existing GA4, GTM, Search Console and Business Profile accounts (or permission to create them); confirmed service areas and offer details; genuine testimonials if available. Google Ads account access, campaign focus and budget are needed only for the optional pilot. Use account invitations, not passwords pasted into chat.

## Current official references

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) — crawlable, understandable, useful pages.
- [Google Business Profile local ranking guidance](https://support.google.com/business/answer/7091) — profile accuracy and local presence.
- [Local Business structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business) — entity markup and eligibility.
- [Google Search documentation updates](https://developers.google.com/search/updates) — May/June 2026 FAQ rich-result retirement.
- [GA4 recommended events](https://developers.google.com/analytics/devguides/collection/ga4/reference/events) — `generate_lead` semantics.
- [Google consent implementation](https://developers.google.com/tag-platform/security/guides/consent) — consent ordering and signals.
- [GTM Content Security Policy guidance](https://developers.google.com/tag-platform/security/guides/csp) — required policy changes by enabled feature.
- [Create Google Ads conversions from GA4 key events](https://support.google.com/analytics/answer/10632359) — optional paid-measurement integration.
