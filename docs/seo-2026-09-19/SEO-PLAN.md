# SEO plan, 2026-09-19

Site: The Spontaneous Cafe, Chef Matt Samuelson, Mendocino. Staging https://spontaneous-cafe.vercel.app, final domain https://spontaneouscafe.com (DNS still on the old GoDaddy page). Research reports R1 to R4 sit in this folder. This file is the plan Mohammed reads. Scope note added the same evening: Sidd owns the wording on the site, so the pull request (branch `seo/metadata-2026-09-19`, rebased on Sidd's push before it opens) carries metadata and build changes only, and every body-copy suggestion below lives in COPY-PROPOSALS.md for him instead.

## Summary

The site is technically sound and the copy is good, so the wins are specific: the foraging page never says "mushroom" while every confirmed search phrase does; the live build ships no responsive images because the build silently degrades when Pillow is missing; the staging host is indexable and the /privacy-policy redirect never fires; the structured data declares up to nine disconnected businesses instead of one entity. Off the site, the Google Business Profile carries the wrong hours and a review cluster that needs a different habit from here on, and every free listing that matters is still unclaimed. Most of what decides local rankings lives in the profile, the reviews and the citations, so half of this plan is a checklist for Mohammed and Matt rather than code.

## What the research found

- R1, technical audit of the live site (29 findings). Blocker: no `<picture>`, no `srcset`, no WebP on the live host, 6.5 MB of images served where 1.5 MB would do, because Pillow is absent on Vercel and `image_size()` swallows the ImportError. Major: canonicals and og:image point at a domain serving a different site; /privacy-policy redirect cancelled by `trailingSlash`; vercel.app alias has no noindex; Caveat font preloaded on every page for four words; hero posters are the LCP element on five pages and cannot take a srcset; LocalBusiness has no `@id`, `hasMap`, or Person.
- R2, keywords and SERP. "Mushroom foraging mendocino" and its variants are the demand; "foraging excursions" has none. The foraging SERP is six editorial articles and no real service page (an open lane). "Private chef mendocino" is five marketplaces deep (a twelve-month organic project; Airbnb Experiences and Yelp are the channels that convert now). Bare "catering mendocino" collides with the Mendocino Farms sandwich chain, so the county and wedding variants are the targets. Proposed titles and descriptions per page, seven content-gap candidates ranked, doorway pages and sea urchin pages ruled out.
- R3, local entity. The GBP is live, category Personal chef service, 5.0 from 8 reviews. Hours published 8 AM to 11 PM daily (wrong for a by-appointment business). All eight reviews landed in one week, one from an account connected to the consultant, which is the pattern Google's conflict-of-interest clause names. No Yelp, Bing, Apple, Chamber or Visit Mendocino presence. Esalen's faculty page is the best third-party corroboration of Matt and says "High Vitality Foods" where the resume says "High Integrity Foods". Citations table with verified costs and link behaviour. A full `@graph` proposal.
- R4, what changed in search by 2026. FAQ rich results retired 7 May 2026 (keep the markup, expect nothing from it). Google says no special markup or llms.txt helps AI Overviews. Vercel's production vercel.app alias is indexable; the fix is a host-matched rule in vercel.json. Search Console domain property by DNS TXT, Bing by import. Whitespark 2026 weights: GBP 25 percent, reviews 20, behavioural 18, citations 12, links 11, on-page 10. A blog is the wrong format; one seasonal calendar page is the right one.

## Decisions

1. Titles and descriptions change on all seven indexable pages (R2 table, adjusted). Service pages lead with the service and the place; the brand suffix goes only where it fits; every description carries a concrete fact (price, group size or place). H1s stay as approved except foraging, which gains one word: "Mushroom foraging days on the Mendocino coast."
2. The word "mushroom" enters the foraging page's title, h1, description and body, with "mushroom hunting" and "foraging tour" once each as synonyms people type. One sentence states the edge of the practice (mushrooms, greens, berries, salt; meat and fish bought), which is both accurate and an expertise signal.
3. Four pricing FAQs go on the private chef page (cost per day, cost for a dinner party, personal versus private chef, dishes). Every fact is already on the site. A retreat catering section goes on the catering page, built from the resume's retreat menus for 20 to 80 guests. One wedding-cost FAQ answers without a number and carries a CONFIRM for Matt.
4. The canonical host comes from Vercel's `VERCEL_PROJECT_PRODUCTION_URL` (fallback `SITE_URL`, then spontaneouscafe.com). Before cutover the staging host self-canonicalises and carries `X-Robots-Tag: noindex` via a host-matched header rule. At cutover the domain is added to Vercel, a redeploy flips every canonical automatically, and the header rule is swapped for a host-matched 308 to spontaneouscafe.com (exact JSON in R1 and LAUNCH-CHECKLIST).
5. Image dimensions are read by a pure-Python header parser so the build no longer depends on Pillow; if a dimension cannot be read the build fails loudly. `requirements.txt` is added as well.
6. Hero posters move from the `poster` attribute to a real `<img class="hero__poster">` sibling under the video, so the build wraps them in `<picture>` with WebP and a srcset and the head preloads them with `fetchpriority="high"`. The video paints over the still once it plays; behaviour and look are unchanged.
7. One entity graph per page: WebSite, LocalBusiness (`@id` #business, `hasMap` to the GBP, five-decimal geo for Mendocino village, six areaServed places, real photos of Matt as the business image, three price tiers as Offers, an OfferCatalog of the four services), Person (`@id` #matt, dated roles from the resume, Esalen faculty page as sameAs), WebPage, and on service pages the Service node with provider by `@id`. No `openingHoursSpecification` (needs Matt), no `postalCode` (must match the GBP; needs Matt), no Review or AggregateRating (disallowed for self-serving markup), no BreadcrumbList this round (see deferred), no JSON-LD on the 404.
8. Head and layout fixes: robots meta with `max-image-preview:large`; `twitter:image`; per-page `og:image:alt`; drop the Caveat preload and preload Source Sans instead; footer headings become paragraphs; the Google Maps link opens in a new tab; favicon.ico, PNG favicon and apple-touch-icon rendered from the SVG; a PNG wordmark for the schema logo.
9. vercel.json: both `/privacy-policy` forms redirect; cache split so images and video revalidate daily while hashed CSS, JS and fonts stay immutable; `Vary: Accept-Encoding`; robots.txt gains `Disallow: /api/` and keeps every crawler allowed (AI crawlers included, on purpose).
10. Off-site work is a checklist with owners (OFFSITE-CHECKLIST.md): fix GBP hours and service area, add secondary categories and Services, the 742-character description, photos, the review link and a text for Matt; then Bing Places, Apple Business, Yelp, a Facebook Page, the Instagram conversion, the Chamber at $160 a year, an email to Visit Mendocino; marketplaces presented as business decisions with verified fees.

## Code changes this round

| Change | Where | Finding |
|---|---|---|
| Pure-Python image dimensions, loud failure, requirements.txt | build.py, requirements.txt | R1 F1 |
| Canonical host from Vercel env, printed in the build log | build.py | R1 F2, F3 |
| Hero poster preload from the `hero__poster` img | build.py, five pages | R1 F7 |
| Entity `@graph` per page, Person, WebSite, Service by `@id`, no JSON-LD on 404 | build.py | R1 F8, F9, F11; R3 D; R4 1 |
| robots meta, twitter:image, og:url stripped on noindex | build.py | R1 F13, F16, F22 |
| sitemap lastmod omitted when git cannot date the file; robots.txt Disallow /api/ | build.py | R1 F25, F26 |
| Font preload swap, footer h2 to p, Maps link target, icon links | src/layout.html | R1 F6, F15, F17, F23 |
| Icons and PNG wordmark rendered from the SVGs, copied to the dist root | src/assets/logo, build.py | R1 F15; R3 build notes |
| Host-matched noindex header, both privacy-policy redirects, cache split, Vary | vercel.json | R1 F4, F5, F19, F20 |

## Copy changes this round

Metadata on the pages, in the pull request:

| Page | Title | Description |
|---|---|---|
| / | The Spontaneous Cafe \| Private Chef and Foraging, Mendocino | Chef Matt Samuelson forages and cooks on the Mendocino coast. Private chef dinners, mushroom foraging days, catering and cooking classes, from $300. |
| /foraging/ | Mushroom Foraging Days, Mendocino Coast \| From $300 | Mushroom foraging on the Mendocino coast with Chef Matt Samuelson. Beach salt, wild mushrooms, farm stands, then dinner. 3, 6 or 12 hours. |
| /private-chef/ | Private Chef, Mendocino Coast \| Dinners from $300 | A private chef in Mendocino for one to twelve guests. Matt Samuelson cooks in your rental or at his Albion kitchen. 3, 6 or 12 hours, from $300. |
| /catering/ | Mendocino County Catering \| Weddings, Retreats, 20 to 350 | Catering in Mendocino County for weddings, rehearsal dinners, retreats and reunions, 20 to 350 guests. Seated, family style or grazing tables. |
| /cooking-classes/ | Cooking Classes, Mendocino \| Knife Skills, from $300 | Cooking classes in Mendocino with Chef Matt Samuelson, who taught at Living Light in Fort Bragg. Knife skills and cooking with no recipe, from $300. |
| /about/ | Chef Matt Samuelson, Mendocino \| The Spontaneous Cafe | Chef Matt Samuelson cooked at retreats in Peru, Thailand and India, taught at Living Light in Fort Bragg, and has lived in Mendocino for over 25 years. |
| /contact/ | Book Chef Matt Samuelson, Mendocino \| Rates and Contact | Book Chef Matt Samuelson for a foraging day, dinner, catering or a class in greater Mendocino. 3 hours $300, 6 hours $500, 12 hours $1,000. |

Every page also gets a specific `og_alt`. Privacy and 404 are unchanged. Page bodies are byte-identical to main.

Body copy, for Sidd (COPY-PROPOSALS.md, ranked): "mushroom" in the foraging h1, lede and body with "mushroom hunting", "foraging tour", "coastal foraging" and "Mendocino County" once each; a sentence stating the edge of the practice; four pricing FAQs on private chef; a retreat catering section, the "wedding catering" pair and a wedding-cost FAQ on catering; the service-area lines on contact and private chef; the home foraging card wording.

## Off-site work

OFFSITE-CHECKLIST.md in this folder, with an owner on every line. The first five items (GBP hours and service area, categories and Services, the description, the review habit, the free listings) are worth more than everything in the code table above.

## Deferred: needs Matt or a decision

- Mendocino mushroom season calendar page (R2 D1). The best link magnet available; needs Matt's species and months. Questions are in the questionnaire, section 9.
- Foraging rules and permits section (R2 D2). Every line needs Matt (permit held, land used, what guests need).
- Farm stands named in public (R2 D3). Ask first; naming a trust-box stand could ruin it.
- BreadcrumbList markup. Google asks that marked-up breadcrumbs be visible on the page. Adding a visible trail is a design change; Mohammed's call. The markup is a ten-line addition once the trail exists.
- `openingHoursSpecification` and GBP hours: the hours Matt actually answers the phone.
- `postalCode` in the address node: must match the GBP address exactly (Mendocino or Albion).
- `sameAs` for LinkedIn, Facebook and Instagram: only after Matt confirms the accounts are his.
- Marketplaces: Airbnb Experiences (20 percent fee, liability insurance required, strongest audience match), Eventbrite for ticketed classes, a free WeddingPro storefront for wedding catering. Business decisions.
- Caveat font subsetting (74 KB to roughly 10 KB) and 1200 by 630 social crops. Small, later.

## Not doing, and why

- Town-by-town service pages: no demand in autocomplete and the pattern Google's scaled-content guidance targets.
- Sea urchin, mussel or abalone foraging pages: strongest foraging autocomplete in the set, and Matt does not do it.
- A blog: informational posts are the worst-hit format in 2026.
- llms.txt and IndexNow: Google says the first neither helps nor harms and does not use the second.
- More FAQPage markup: the rich result is gone; the FAQ text stays because people and the Maps "Ask" panel read it.
- Review or AggregateRating markup: disallowed for a business marking up its own reviews.
- VideoObject on the hero loops and Course markup on the classes: neither meets Google's definitions.

## Cutover

LAUNCH-CHECKLIST.md carries the sequence: lower the GoDaddy TTL a week ahead; add the domain in Vercel with the apex as primary; redeploy so canonicals flip; swap the vercel.json host rule from noindex to redirect; verify the two privacy-policy redirects and /foraging/; Search Console domain property by DNS TXT; submit the sitemap; request indexing once for eight URLs; Bing Webmaster import; update the GBP and citations.

## Verification gate

A separate agent builds the merged branch and checks: build succeeds with and without Pillow and `<picture>` counts match; every JSON-LD block parses, every `@id` reference resolves on its page or to #business, no Review type, no JSON-LD on 404; titles 60 characters or fewer and descriptions 120 to 155; one h1 per page; every page has robots meta, twitter:image, og:image:alt, canonical; hero pages carry an image preload that matches the poster; vercel.json validates against Vercel's schema; robots.txt and sitemap correct; no em dashes and no banned vocabulary in any changed copy; every new client-facing claim is either in CONTEXT.md or tagged CONFIRM; screenshots of the five hero pages at 1280 and 375 look the same as before.

## Merge and deploy

The repo is public on GitHub (maximizeGPT/spontaneous-cafe) and connected to Vercel, so main deploys to production and every branch gets a preview. Flow: wait for Sidd's push, rebase `seo/metadata-2026-09-19` on it, rebuild and re-run the checks, push the branch, open the pull request. Mohammed merges; nothing deploys on my say.
