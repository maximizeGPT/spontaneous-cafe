# R1. Technical SEO audit, Spontaneous Cafe

Date: 2026-09-19. Host audited: `https://spontaneous-cafe.vercel.app/` (production Vercel alias). Repo at commit `864e4ed`.

## Summary

The production build silently ships no responsive images at all: Pillow is absent from Vercel's Python runtime, so `responsive_images()` and the `og:image` dimension tags degrade to no-ops and every page serves full-size JPEGs, 6.54 MB across six pages where 1.46 MB would do.
Every page tells Google its canonical is `spontaneouscafe.com`, a host that today serves the old GoDaddy site, and `spontaneouscafe.com/foraging/` returns HTTP 200 with a different page titled "Foraging", so the canonical points at real, conflicting content.
The `og:image` URLs 404 today, the `/privacy-policy` redirect never fires because `trailingSlash` redirects first, and the `.vercel.app` alias gets no `X-Robots-Tag` from Vercel, so it is fully indexable.
Fonts are 182 KB per page, of which Caveat is 74.6 KB preloaded on all eight pages for at most four words and zero words on `/privacy/`.
Structured data is valid but thin: no BreadcrumbList, no Person for Matt, the Google Maps CID in `sameAs` rather than `hasMap`, and FAQPage, the only extra type on five pages, stopped producing rich results on 7 May 2026.

Two caveats on evidence. The live deployment is two commits behind HEAD (`b7eb62b`, 2026-09-16), so page copy and image alts differ; `build.py`, `vercel.json` and `src/layout.html` are byte-identical between that commit and HEAD, so every finding below holds for both. The PageSpeed Insights API returned HTTP 429 on all four targets across four attempts, detail in "PageSpeed results".

---

## Findings

### Blocker

**F1. Responsive images and `og:image` dimensions are silently disabled in production because Pillow is not installed on Vercel.**

Evidence. Zero `<picture>`, zero `srcset` and zero `type="image/webp"` across all eight live pages:

```
about.html               picture=0 srcset=0 source-webp=0
catering.html            picture=0 srcset=0 source-webp=0
contact.html             picture=0 srcset=0 source-webp=0
cooking-classes.html     picture=0 srcset=0 source-webp=0
foraging.html            picture=0 srcset=0 source-webp=0
home.html                picture=0 srcset=0 source-webp=0
privacy.html             picture=0 srcset=0 source-webp=0
private-chef.html        picture=0 srcset=0 source-webp=0
```

The same source at HEAD built locally gives `home.html picture=10`, `about.html picture=7`, `foraging.html picture=4`. Reproduced by blocking the import and rebuilding:

```
BUILD OK (no Pillow)
picture elements in /foraging/: 0
srcset: 0
og:image:width: 0
--- vs WITH Pillow ---
picture elements in /foraging/: 4
srcset: 8
og:image:width: 1
```

Mechanism. `image_size()` at `build.py:184-190` catches every exception and returns `None`. `pixel_width()` at `build.py:115-125` returns `None`, so `responsive_images()` at `build.py:134-136` hits `if not full_w ... return m.group(0)` and hands back the bare `<img>`. `head_meta()` at `build.py:212-215` skips `og:image:width`/`height` for the same reason. The build exits 0, so nothing flags it. There is no `requirements.txt` in the repo, so Vercel installs nothing.

Cost, measured from real file sizes on disk. "Served now" is the full JPEG the live site sends at every viewport. "800w webp" is what a 375 px phone at DPR 2 would fetch once `<picture>` works, given the existing `sizes` of `(max-width: 600px) 100vw, ...`:

```
PAGE                 served-now    800w-webp    480w-webp   saving@800
home                    2160027       497738       226432      1662289
foraging                1085100       318066       137330       767034
private-chef             492322        79772        37554       412550
catering                 252184        50850        23508       201334
cooking-classes         1004921       194810        96980       810111
about                   1550311       319500       136656      1230811
TOTAL                   6544865      1460736       658460      5084129
```

Every variant file already exists in `src/assets/img/`. The build is throwing them away.

Fix, two parts.

1. Add `/Users/main/MOSI/Spontaneous Cafe/requirements.txt` with one line, so Vercel's Python build installs it:

```
Pillow>=11.0
```

2. Make the failure loud instead of silent. Replace `build.py:184-190`:

```python
def image_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None
```

with:

```python
_PIL_OK = None

def image_size(path):
    global _PIL_OK
    try:
        from PIL import Image
    except ImportError:
        if _PIL_OK is None:
            _PIL_OK = False
            sys.exit('Pillow is not installed. Responsive images and og:image '
                     'dimensions would be dropped silently. Add Pillow to '
                     'requirements.txt.')
        return None
    _PIL_OK = True
    try:
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None
```

The `sys.exit` fails the Vercel build rather than shipping a degraded site. `sys` is already imported at `build.py:18`.

**F2. Canonical, `og:url`, sitemap `<loc>` and the robots `Sitemap:` line all point at `spontaneouscafe.com`, which today serves a different site, and one path collides with real content.**

Evidence. `SITE = 'https://spontaneouscafe.com'` at `build.py:23` feeds `src/layout.html:8` (canonical), `:13` (`og:url`), `:14` (`og:image`), and `build.py:300,305,310` (sitemap and robots). Live on `/foraging/`:

```html
<link rel="canonical" href="https://spontaneouscafe.com/foraging/">
<meta property="og:url" content="https://spontaneouscafe.com/foraging/">
```

What that target serves today:

```
/                    200
/foraging/           200      <title>Foraging</title>
/private-chef/       404
/catering/           404
/cooking-classes/    404
/about/              404
/contact/            404
/privacy/            404
```

The old GoDaddy sitemap at `https://spontaneouscafe.com/sitemap.website.xml` lists exactly three URLs: `/`, `/foraging`, `/privacy-policy`, all with `<lastmod>2023-10-16</lastmod>`.

What this means for indexing now. Google treats `rel=canonical` as a hint, not a directive, and reserves the right to pick a different canonical when the declared target's content does not match ([Google, consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)). Two outcomes are live today. For `/foraging/` the canonical resolves to a genuinely different page, so Google either drops the Vercel URL as "Alternate page with proper canonical tag" and indexes nothing, or ignores the mismatched hint and indexes the Vercel URL under its own address. For the other six pages the canonical resolves to a 404, and Google ignores a canonical pointing at a 404 and falls back to self-canonicalising the Vercel URL. Either way the new content accrues no signal to the domain it is meant to live on, and any Vercel URLs that do get indexed become duplicates that must be redirected at cutover.

What this means at cutover. Once DNS moves, the canonicals become correct in a single step, which is the whole point of hardcoding the final domain. The problem is only the window before that, and the window has no defined end date because DNS is waiting on Matt.

Fix. Make the canonical host build-time configurable, so the staging host self-canonicalises until the domain is real. Replace `build.py:23`:

```python
SITE = 'https://spontaneouscafe.com'
```

with:

```python
SITE = os.environ.get('SITE_URL', 'https://spontaneouscafe.com').rstrip('/')
```

Then set `SITE_URL=https://spontaneous-cafe.vercel.app` as a Vercel project environment variable for Production, and delete that variable at cutover. This also fixes F3 in the same move, because `og:image` then resolves on the host serving the page. Pair it with the host-scoped `X-Robots-Tag` in "vercel.json before and after cutover".

Do not add `X-Robots-Tag: noindex` while the canonical still points at `spontaneouscafe.com`. A `noindex` on a page whose canonical names a different URL can propagate to the canonical target, which here is the live GoDaddy site that currently ranks. Changing the canonical first removes that risk.

### Major

**F3. Every `og:image` URL returns 404 today, so any share of the staging link renders with no image.**

Evidence:

```
status=404 type=text/html;charset=utf-8 size=47737 url=https://spontaneouscafe.com/assets/img/home-poster.jpg
```

All eight pages emit an absolute `og:image` on `spontaneouscafe.com` (`src/layout.html:14`), and `/assets/` does not exist on that host.

Fix. The `SITE_URL` change in F2 resolves this without further edits.

**F4. The `/privacy-policy` redirect never fires. `trailingSlash` redirects first and the slashed form has no rule.**

Evidence, live:

```
=== /privacy-policy ===
HTTP/2 308
location: /privacy-policy/
=== /privacy-policy/ ===
HTTP/2 404
```

`vercel.json:7` declares `{ "source": "/privacy-policy", "destination": "/privacy/", "permanent": true }`. With `"trailingSlash": true` at `vercel.json:5`, Vercel answers the slashless form with its own 308 to `/privacy-policy/` before the custom rule is reached ([Vercel, trailingSlash](https://vercel.com/docs/project-configuration/vercel-json): "When `trailingSlash: true`, visiting a path that does not end with a forward slash will respond with a 308 status code and redirect to the path with a trailing slash"). Nothing then matches `/privacy-policy/`.

This matters because `/privacy-policy` is one of exactly three URLs in the old site's sitemap and returns 200 on the live domain today. The rule exists to catch it and does not.

Fix. `vercel.json:6-8`, add the slashed form:

```json
"redirects": [
  { "source": "/privacy-policy", "destination": "/privacy/", "permanent": true },
  { "source": "/privacy-policy/", "destination": "/privacy/", "permanent": true }
],
```

The old `/foraging` needs no rule: `trailingSlash` sends it to `/foraging/`, which exists on the new site.

**F5. The `.vercel.app` production alias is fully indexable. Vercel adds no `X-Robots-Tag` to it, and no host redirect is configured for after cutover.**

Evidence. Full response headers for `https://spontaneous-cafe.vercel.app/` contain no `x-robots-tag`:

```
HTTP/2 200
cache-control: public, max-age=0, must-revalidate
content-type: text/html; charset=utf-8
server: Vercel
strict-transport-security: max-age=63072000; includeSubDomains
x-vercel-cache: HIT
```

Vercel's own documentation confirms the header is scoped to preview deployments and superseded production deployments, not to the production alias ([Vercel, Are Vercel Preview Deployments indexed by search engines?](https://vercel.com/kb/guide/are-vercel-preview-deployment-indexed-by-search-engines)). Production deployments keep the header off deliberately so they can rank.

Fix. Before cutover, a host-scoped `X-Robots-Tag`. After cutover, a host-scoped 308 to the real domain. Both are conditional on `has` with `type: "host"`, which Vercel's published JSON schema confirms is valid for both `headers` and `redirects` entries, requiring exactly `type` and `value` with `additionalProperties: false` (fetched from `https://openapi.vercel.sh/vercel.json`, paths `/properties/redirects/items/properties/has/items/anyOf/0` and `/properties/headers/items/properties/has/items/anyOf/0`). The `type` field is documented as "Must be either `header`, `cookie`, `host`, or `query`" ([Vercel, vercel.json](https://vercel.com/docs/project-configuration/vercel-json)). Exact JSON in the section below.

**F6. Caveat, 74,572 bytes, is preloaded at top priority on all eight pages for at most four words, and zero words on `/privacy/`.**

Evidence. `src/layout.html:19`:

```html
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/caveat-latin.woff2" crossorigin>
```

Real transfer sizes from the browser on `/foraging/`, plus the count of `.hand` spans per source page:

```
lora-latin.woff2           37792
caveat-latin.woff2         74572
source-sans-3-latin.woff2  28792
lora-italic-latin.woff2    40648
                          ------
fonts total               181804   (45% of the 402 KB page)

index              hand-spans: 4
foraging           hand-spans: 3
private-chef       hand-spans: 4
catering           hand-spans: 4
cooking-classes    hand-spans: 3
about              hand-spans: 4
contact            hand-spans: 1
privacy            hand-spans: 0
```

The `<link rel=preload>` fetches the file unconditionally, so `/privacy/` downloads 74.6 KB for a font it never paints. Caveat carries the full Latin `unicode-range` declared at `src/assets/css/fonts.css:47`, covering roughly 220 codepoints, while the site uses it on about 25 distinct characters.

Fix, two parts, either of which helps on its own.

1. Drop the preload. `src/layout.html:19`, delete the line. Caveat has `font-display: swap` at `fonts.css:45`, so removing the preload costs a swap on two words and saves 74.6 KB of top-priority bandwidth on the critical path. The Lora preload at `:18` should stay, and `source-sans-3-latin.woff2` deserves the preload Caveat currently has, since it is the body face and is discovered only after CSS parse.

2. Subset Caveat to the characters actually used. Run over the built `dist/` to collect the glyph set inside `.hand` spans, then subset with `pyftsubset` (fonttools). Expect roughly 8 to 12 KB from 74.6 KB. Estimate, based on the ratio of 25 used characters to about 220 in the current subset; confirm by running the subsetter.

**F7. The LCP element on all five hero pages is a `<video poster>`, which cannot carry a `srcset`, is not preloaded, and is not prioritised.**

Evidence. `src/pages/index.html:6` and the same line in `foraging.html`, `private-chef.html`, `catering.html`, `cooking-classes.html`:

```html
<video data-hero muted loop playsinline preload="none" poster="/assets/img/home-poster.jpg" aria-hidden="true">
```

The hero measures 1396 px tall in the layout engine and the poster covers it with `object-fit: cover` (`src/assets/css/site.css:225`). Chrome counts a video poster as an LCP candidate: "`<video>` elements (the poster image load time or first frame presentation time for videos is used, whichever is earlier)" ([web.dev, Largest Contentful Paint](https://web.dev/articles/lcp)). With `preload="none"` and playback armed only on window `load` (`src/assets/js/site.js:228-231`), the poster is what paints, so the poster is the LCP.

The `poster` attribute takes a single URL. F1's `<picture>` machinery never touches it, because `IMG_RE` at `build.py:110` matches `<img ...>` only. So the poster is immune to the F1 fix and needs its own change. Sizes served today against the variants already on disk:

```
home             jpg=64376   800.webp=22948   480.webp=12828
foraging         jpg=119112  800.webp=49802   480.webp=26410
private-chef     jpg=69097   800.webp=23620   480.webp=13444
catering         jpg=64910   800.webp=20660   480.webp=11192
cooking-classes  jpg=58356   800.webp=19268   480.webp=10554
```

`/foraging/` sends 119 KB where 49.8 KB covers a DPR 2 phone.

Fix. Move the poster out of the attribute and into a real `<picture>` layered behind the video, which `.hero__media video, .hero__media img` already styles identically at `site.css:225`. In each of the five page files at line 6, replace the `poster="..."` attribute with a sibling image:

```html
<img src="/assets/img/home-poster.jpg" alt="" aria-hidden="true"
     fetchpriority="high" decoding="async"
     data-sizes="100vw" width="1280" height="720">
<video data-hero muted loop playsinline preload="none" aria-hidden="true">
```

`build.py`'s `responsive_images()` then wraps it in `<picture>` with the WebP and JPEG srcsets, honouring the `data-sizes="100vw"` override at `build.py:147-149`. Add a CSS rule so the video paints over the still once it plays:

```css
.hero__media picture, .hero__media img { position: absolute; inset: 0; }
.hero__media video { position: relative; }
```

Also add a matching preload to `src/layout.html`, built per page. In `head_meta()` at `build.py:216`, before the twitter tags:

```python
    poster = meta.get('hero_poster')
    if poster:
        stem = poster.rsplit('.', 1)[0]
        tags.append(
            f'<link rel="preload" as="image" fetchpriority="high" '
            f'href="/assets/img/{stem}.jpg" '
            f'imagesrcset="/assets/img/{stem}-480.webp 480w, '
            f'/assets/img/{stem}-800.webp 800w, '
            f'/assets/img/{stem}-1200.webp 1200w" imagesizes="100vw">')
```

and add `"hero_poster": "home-poster.jpg"` to the meta block at line 2 of each of the five hero pages. Document the key alongside the others at `build.py:13`.

**F8. The LocalBusiness block is missing `hasMap` and `openingHoursSpecification`, puts the Google Maps CID in `sameAs`, has no `@id`, and uses a stock video still as the business image.**

Evidence, the live block on `/` (also on `/about/`, `/contact/`, `/privacy/`), emitted by `build.py:88-105`:

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "The Spontaneous Cafe",
  "alternateName": "Chef Matt Samuelson",
  "url": "https://spontaneouscafe.com/",
  "image": "https://spontaneouscafe.com/assets/img/home-poster.jpg",
  "telephone": "+1-707-972-6647",
  "email": "chefmattsamuelson@gmail.com",
  "founder": { "@type": "Person", "name": "Matthew Samuelson" },
  "foundingDate": "2009",
  "areaServed": { "@type": "Place", "name": "Mendocino County, California" },
  "address": { "@type": "PostalAddress", "addressLocality": "Mendocino", "addressRegion": "CA", "addressCountry": "US" },
  "geo": { "@type": "GeoCoordinates", "latitude": 39.3077, "longitude": -123.7995 },
  "priceRange": "$$$",
  "makesOffer": [ ... ],
  "sameAs": ["https://www.google.com/maps?cid=7343978535458024901"]
}
```

Against Google's LocalBusiness reference, `address` and `name` are the only required properties and both are present. Of the recommended set, `geo`, `priceRange`, `telephone` and `url` are present; `openingHoursSpecification` is absent; `aggregateRating` and `review` are correctly absent, since Google recommends them "only recommended for sites that capture reviews about other local businesses" and self-serving review markup breaks the structured data policies ([Google, LocalBusiness](https://developers.google.com/search/docs/appearance/structured-data/local-business)). Google asks for `geo` "at least 5 decimal places"; the current values carry four.

Four specific problems.

`sameAs` holds a Google Maps CID link. `sameAs` is for a reference page that identifies the entity, such as a Wikipedia article or an official social profile. The Maps URL belongs in `hasMap`, an inherited Place property (confirmed present on [schema.org/LocalBusiness](https://schema.org/LocalBusiness)). Moving it lets Google tie the site to the Business Profile created 2026-09-07 rather than treating a Maps link as a social profile.

`image` points at `home-poster.jpg`, a stock loop still of hands over a pan (see `src/assets/MANIFEST.md`). Google's LocalBusiness image guidance wants photos of the business. `matt-kitchen.jpg` and `matt-square.jpg` are real photos of Matt and belong here.

No `@id`. Each page emits a standalone business node with no shared identifier, and the five service pages each nest a separate `provider` LocalBusiness (`build.py:75-81`), so the site declares up to nine disconnected business entities. A single `@id` of `https://spontaneouscafe.com/#business` referenced from every other node collapses them into one.

No `postalCode` or `streetAddress`. For a service-area business, omitting `streetAddress` is correct, and a `postalCode` strengthens the local signal. Whether that is Mendocino 95460 or Albion 95410 is Matt's call, given CONTEXT.md records his home kitchen in Albion and the Business Profile in Mendocino. Tag it `<!-- CONFIRM -->` rather than guessing, and make it match the Google Business Profile exactly.

On subtype choice, the task asked me to evaluate four alternatives. `Caterer` does not exist in schema.org: `https://schema.org/Caterer` returns 404 and the type is absent from the 33 subtypes listed on `https://schema.org/LocalBusiness`. `FoodEstablishment` exists and is defined as "A food-related business" with subtypes Bakery, BarOrPub, Brewery, CafeOrCoffeeShop, Distillery, FastFoodRestaurant, IceCreamShop, Restaurant and Winery, all of them premises a guest travels to; its added properties are `acceptsReservations`, `hasMenu`, `servesCuisine` and `starRating` ([schema.org/FoodEstablishment](https://schema.org/FoodEstablishment)). Matt cooks in the guest's kitchen, so the type would assert a storefront that does not exist. `TouristAttraction` is a Place subtype describing the attraction itself, not its operator, so it is wrong for the business. `LocalBusiness` stays. Sharpen it with `additionalType` and a `hasOfferCatalog` instead of a subtype change. Exact JSON below.

**F9. No BreadcrumbList on any page.**

Evidence. Parsing every `ld+json` block on all eight pages returns these `@type` sets and nothing else:

```
home             LocalBusiness, Person, Place, PostalAddress, GeoCoordinates, Offer x3, Service x3
foraging         Service, LocalBusiness, Offer x3, Service x3  +  FAQPage
private-chef     same shape                                    +  FAQPage
catering         same shape                                    +  FAQPage
cooking-classes  same shape                                    +  FAQPage
about            LocalBusiness, ...
contact          LocalBusiness, ...                            +  FAQPage
privacy          LocalBusiness, ...
```

Breadcrumbs are a live rich result and change the URL line in mobile results to a named path. `itemListElement` is the only required property on BreadcrumbList; ListItem requires `position`, `name` and `item`, and "If the breadcrumb is the last item in the breadcrumb trail, `item` is not required" ([Google, Breadcrumb](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)).

Fix. Emit one per non-home page from `build.py`. Code in the JSON-LD section below.

**F10. FAQPage is the only extra schema on five pages and it earns nothing in 2026.**

Evidence. `faq_jsonld()` at `build.py:164-181` builds a FAQPage from every `<details>` block: 5 questions on `/foraging/`, 4 each on `/private-chef/`, `/catering/`, `/cooking-classes/`, 3 on `/contact/`.

Google restricted FAQ rich results to "well-known, authoritative government and health websites" in August 2023 ([Google Search Central blog, Changes to HowTo and FAQ rich results](https://developers.google.com/search/blog/2023/08/howto-faq-changes)) and then stopped showing them entirely on 7 May 2026, with the search appearance filter, the rich result report and Rich Results Test support removed in June 2026 ([Search Engine Journal, Google Drops FAQ Rich Results From Search](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/), [Search Engine Land](https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957)).

Fix. Keep the markup. Unused structured data causes no harm, the FAQ content itself is good on-page copy that answers real queries, and other consumers still read FAQPage. What to change is the expectation: stop counting it as a rich result and put the schema effort into BreadcrumbList, Person and a single linked business entity, none of which exist. No code change.

**F11. Service schema is thin, and the nested `provider` creates a separate business entity on every service page.**

Evidence. `build.py:69-86` emits, on all four service pages, an `offers` array whose three members are identical apart from price, each with `itemOffered` named "Culinary experience with Chef Matt" rather than the service the page is about:

```json
"offers": [
  { "@type": "Offer", "name": "Three hours", "price": "300", "priceCurrency": "USD",
    "itemOffered": { "@type": "Service", "name": "Culinary experience with Chef Matt" } },
  ...
]
```

`areaServed` is a bare string, `"Mendocino County, California"` (`build.py:82`), where the home page uses a typed `Place` for the same value. The `provider` at `build.py:75-81` is an inline LocalBusiness with no `@id`, so each service page declares its own copy of the business.

Three concrete defects. `itemOffered` names a generic product instead of the page's service, so the three Offers on `/catering/` and the three on `/foraging/` are indistinguishable. `Offer` has no `availability`, no `priceValidUntil` and no `url`. `Service` has no `image` and no `provider` reference that resolves to one entity.

Fix. Reference the business by `@id`, name the real service in `itemOffered`, and type `areaServed`. Full replacement for `build.py:58-86` in the JSON-LD section.

**F12. The About meta description runs 198 characters and will be truncated.**

Evidence. `src/pages/about.html:2`:

```
"description": "Matt Samuelson cooked at yoga retreats in Peru, in Thailand and India, and privately in Los Angeles. He taught at Living Light in Fort Bragg, settled in Mendocino in 2009 and studied foraging there."
```

198 characters. The other seven land between 130 and 155, which is the right band. Google states "There's no limit on how long a meta description can be, but the snippet is truncated in Google Search results as needed, typically to fit the device width", and uses the tag only "if we think it gives users a more accurate description than would be possible purely from the on-page content" ([Google, control your snippets](https://developers.google.com/search/docs/appearance/snippet)). So the description is a hint that may be ignored entirely, and when it is used, everything past roughly 155 characters is cut on a phone. Write it to survive the cut.

Fix. `src/pages/about.html:2`, cut to roughly 155 characters, for example:

```
"description": "Chef Matt Samuelson cooked at retreats in Peru, Thailand and India, taught at Living Light in Fort Bragg, and has foraged the Mendocino coast since 2009."
```

155 characters. This drops the Los Angeles clause, which the CONTEXT notes cannot name clients anyway.

### Minor

**F13. No robots meta on indexable pages, so no `max-image-preview:large`.**

Evidence. `<meta name="robots">` is absent from all seven indexable pages; `build.py:221-222` emits it only when `noindex` is set, which only `404.html` sets.

Without `max-image-preview:large`, Google may show a thumbnail rather than a large image preview in mobile results and Discover ([Google, robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)). On a business selling a visual experience, the large preview matters.

Fix. `build.py:221`, change:

```python
    if meta.get('noindex'):
        tags.append('<meta name="robots" content="noindex, follow">')
```

to:

```python
    if meta.get('noindex'):
        tags.append('<meta name="robots" content="noindex, follow">')
    else:
        tags.append('<meta name="robots" content="index, follow, '
                    'max-image-preview:large, max-snippet:-1, max-video-preview:-1">')
```

**F14. `og:image:alt` is the same generic string on all eight pages.**

Evidence. Every page carries `<meta property="og:image:alt" content="The Spontaneous Cafe, Mendocino">`. `build.py:210` reads `meta.get("og_alt", DEFAULT_OG_ALT)` and no page in `src/pages/` sets `og_alt`.

Fix. Add `"og_alt": "..."` to each page's meta block describing that page's own image, for example on `src/pages/foraging.html:2`: `"og_alt": "Black trumpet mushrooms on a mossy trunk in the Mendocino coastal forest"`.

**F15. No `apple-touch-icon`, no `favicon.ico`, no PNG fallback.**

Evidence:

```
=== favicon.ico ===          HTTP/2 404
=== apple-touch-icon.png ===  HTTP/2 404
=== favicon.svg ===           HTTP/2 200  content-type: image/svg+xml  content-length: 243
```

`src/layout.html:17` declares only the 243-byte SVG. Safari on iOS and several link-preview crawlers ignore SVG favicons and fall back to `/apple-touch-icon.png` and `/favicon.ico` at the root, both of which 404 today.

Fix. Render `src/assets/logo/favicon.svg` to `dist/apple-touch-icon.png` at 180x180 and to `dist/favicon.ico` at 32x32, and add to `src/layout.html:17`:

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/logo/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

**F16. No `twitter:image`, and the `og:image` files are not 1.91:1.**

Evidence. All pages emit `twitter:card=summary_large_image`, `twitter:title` and `twitter:description` (`build.py:217-219`) and no `twitter:image`. X falls back to `og:image`, so cards render, but the fallback is undeclared. The posters are 1280x720 (16:9) and `matt-kitchen.jpg` is 1448x1086 (4:3); Facebook and LinkedIn crop to 1.91:1, so the 4:3 About image loses roughly a third of its height.

Fix. Add `f'<meta name="twitter:image" content="{SITE}/assets/img/{og_image}">'` to `head_meta()` after `build.py:219`. Separately, generate 1200x630 social crops for the six distinct `og_image` files and point the meta blocks at those.

**F17. The two footer `h2`s land in every page's heading outline.**

Evidence. `src/layout.html:56` and `:66`:

```html
<h2 class="footer-h">Experiences</h2>
<h2 class="footer-h">Chef Matt</h2>
```

Every outline ends the same way. On `/privacy/`, whose own content is five `h2`s, the footer supplies two of the seven.

This is cosmetic rather than harmful. Google reads headings as one signal among many and does not require a valid outline. It does make the outline less useful to any tool reading structure, and "Experiences" and "Chef Matt" read as page sections when they are navigation labels.

Fix. `src/layout.html:56,66`, change both to `<p class="footer-h">`, keeping the class so the CSS is untouched. If the accessible landmark structure matters more, use `<h2 class="footer-h visually-hidden">` inside a `<nav aria-label>` instead. The footer already sits in `<footer>`, which is its own landmark, so the plain paragraph is enough.

**F18. Duplicate `h3` and `h4` text inside the seasonal tab panels.**

Evidence. `/private-chef/` carries `<h3>Six courses for a table of six</h3>` four times, once per season panel (`src/pages/private-chef.html:119,138,...`). `/catering/` carries `<h3>Family style for forty</h3>` four times. Each panel's dish names are `h4`s, so `/private-chef/` has 24 `h4`s.

Fix. Name the season in the heading: `<h3>Six courses for a table of six, spring</h3>`, and so on. This also makes the three panels Googlebot renders as `hidden` distinguishable.

**F19. Images and fonts carry a one-year `immutable` cache without content hashes in their filenames.**

Evidence. `vercel.json:11-15` applies `Cache-Control: public, max-age=31536000, immutable` to `/assets/(.*)`. CSS and JS are content-hashed by `hash_assets()` at `build.py:226-242`; images and fonts are not:

```
/assets/css/site.f4ae1c62.css   cache-control: public, max-age=31536000, immutable
/assets/img/home-poster.jpg     cache-control: public, max-age=31536000, immutable
/assets/fonts/lora-latin.woff2  cache-control: public, max-age=31536000, immutable
```

`immutable` tells the browser never to revalidate. With Matt's photo swaps still in progress (`docs/SWAP-LIST.md`), anyone who has visited keeps the placeholder for a year after the real photo ships.

Fix. Either extend `hash_assets()` to images and rewrite references, or narrow the immutable rule and give images a revalidating policy. The second is a two-line change to `vercel.json:11-15`:

```json
{
  "source": "/assets/(css|js|fonts)/(.*)",
  "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
},
{
  "source": "/assets/(img|video)/(.*)",
  "headers": [{ "key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800" }]
}
```

Fonts keep the immutable rule because their filenames are stable by intent, though a hash there would be safer too.

**F20. No `Vary: Accept-Encoding` on compressed responses.**

Evidence. HTML and CSS come back Brotli-encoded with no `vary` header:

```
content-encoding: br
content-type: text/css; charset=utf-8
(no vary header present)
```

Vercel's CDN keys its own cache on encoding, so the edge is correct. Any intermediate proxy between the edge and the user can cache one encoding and serve it to a client that did not ask for it.

Fix. `vercel.json:16-25`, add to the catch-all headers block:

```json
{ "key": "Vary", "value": "Accept-Encoding" }
```

**F21. `/contact/` is thin and carries no image.**

Evidence. 315 words inside `<main>` (the next-thinnest indexable page is `/privacy/` at 246, which is a legal page and fine). Heading outline: `h1 Send Matt the details.`, `h2 Questions people ask`, then the two footer `h2`s. Images: two logo SVGs and nothing else.

`/contact/` is the page that ranks for "chef mendocino contact" style queries and the conversion target of 14 internal links.

Fix. Add the service-area paragraph, the three tiers as text rather than links out, the phone and email as visible text, and one photo. The page already self-canonicalises correctly across all query-string variants, verified on `/contact/?service=Private%20chef`:

```html
<link rel="canonical" href="https://spontaneouscafe.com/contact/">
<meta property="og:url" content="https://spontaneouscafe.com/contact/">
```

**F22. The 404 page's `og:url` claims to be the homepage.**

Evidence, on `https://spontaneous-cafe.vercel.app/zzz-nothing-here/`:

```html
<title>Page not found | The Spontaneous Cafe</title>
<meta property="og:url" content="https://spontaneouscafe.com/">
<meta name="robots" content="noindex, follow">
```

The canonical is correctly stripped by `build.py:285-286`; `og:url` is not. The status code is a true 404 with `content-type: text/html; charset=utf-8`, which is correct.

Fix. `build.py:285-286`, extend the same stripping to `og:url`:

```python
        if meta.get('noindex'):
            html = re.sub(r'\n<link rel="canonical"[^>]*>', '', html, count=1)
            html = re.sub(r'\n<meta property="og:url"[^>]*>', '', html, count=1)
```

**F23. The Google Maps link carries `rel="noopener"` with no `target`.**

Evidence, `src/layout.html:73`:

```html
<li><a href="https://www.google.com/maps?cid=7343978535458024901" rel="noopener">Find us on Google Maps</a></li>
```

`noopener` only does anything on a link that opens a new browsing context. On a same-tab link it is inert. The link should stay `dofollow`, since it points at the business's own Google Business Profile and is a legitimate entity signal.

Fix. Either drop `rel="noopener"`, or add `target="_blank" rel="noopener"` so a visitor checking the map does not lose the site. The second is the better behaviour for this link.

**F24. Fourteen distinct `/contact/?service=...` URLs are linked internally.**

Evidence, the set across the site includes `?service=Foraging%20excursion`, `?service=Foraging%20excursion&tier=3%20hours`, `&tier=6%20hours`, `&tier=12%20hours`, the same four for Private chef, Catering and events (plus `&tier=Larger%20event`), Cooking class, `?service=Forest%20bathing%20or%20farm%20tour` and `?service=Interactive%20dinner%20party`.

Every one self-canonicalises to `/contact/` (verified above), so there is no duplicate content problem. The cost is crawl requests on a nine-page site, which is negligible, and the parameters do real work: `site.js:361-372` pre-selects the service and tier. No change needed. Recorded so a later audit does not re-raise it.

**F25. `/api/notify` is reachable to crawlers.**

Evidence. `GET https://spontaneous-cafe.vercel.app/api/notify` returns 308 (to `/api/notify/` under `trailingSlash`). `robots.txt` is `Allow: /` with no exclusions.

Fix. Add `Disallow: /api/` to the robots.txt written at `build.py:309-310`:

```python
    with open(os.path.join(DIST, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {SITE}/sitemap.xml\n')
```

**F26. Items checked and correct, recorded so they are not re-raised.**

Sitemap `lastmod` from git (`build.py:193-202`) is correct practice: it reports the last commit date of the page source, not the build date, so a rebuild does not falsely refresh it. All eight currently read `2026-09-16` because commit `b7eb62b` touched every page. Google treats `lastmod` as a hint and ignores it when it is obviously unreliable ([Google, sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)); a git-derived date is the reliable kind.

`/privacy/` in the sitemap is correct. It is an indexable page with a canonical, and excluding it from the sitemap while leaving it indexable creates an inconsistency for no gain.

No `hreflang` is correct. One language, one region, one URL set.

`lang="en"` on `<html>` (`src/layout.html:2`) and `<meta name="viewport" content="width=device-width, initial-scale=1">` (`:5`) are present on all eight pages.

Exactly one `h1` per page on all eight.

`content-type: text/html; charset=utf-8` on HTML, `text/css; charset=utf-8` on CSS, `application/javascript; charset=utf-8` on JS, `image/jpeg` on images, `font/woff2` on fonts. All correct.

`http://` returns 308 to `https://`. `/about` returns 308 to `/about/`. `/index.html` returns 308 to `/`. `/about/index.html` returns 308 to `/about/`. An unknown path returns a true 404 with the styled 404 body. All correct.

Every cross-page fragment target exists. `/#build`, `/foraging/#more`, `/foraging/#prices`, `/private-chef/#menus`, `/private-chef/#prices` all resolve to real `id` attributes. No broken anchors.

No `nofollow` anywhere, which is right for a site with three outbound links, all of them the business's own Maps profile, `tel:` and `mailto:`.

**F27. Rendering: what a crawler actually gets. This passes, with two details worth recording.**

The `reveal` animation is correctly gated and does not hide content from a non-JS crawler. `src/assets/css/site.css:516-521`:

```css
.reveal { opacity: 1; transform: none; }
@media (prefers-reduced-motion: no-preference) {
  .js .reveal { opacity: 0; transform: translateY(14px); transition: ... }
  .js .reveal.is-in { opacity: 1; transform: none; }
}
```

The `opacity: 0` rule requires the `.js` class, which `site.js:8` adds to `<html>` at parse time. A crawler that does not execute JavaScript sees every section at `opacity: 1`. A crawler that does execute it gets `revealAll()` on any thrown exception (`site.js:13-18`), a synchronous pass marking everything already in the viewport (`site.js:308-312`), and an IntersectionObserver for the rest (`site.js:318-326`). Text is in the HTML either way. Nothing is injected by JavaScript except the hero pause button (`site.js:183-214`) and the copyright year (`site.js:430-433`), neither of which carries indexable content.

The nav drawer is in the HTML as eight plain `<a href>` elements (`src/layout.html:33-40`). `inert` is applied by `site.js:65` only below 900 px and only when closed, so a mobile render sees the drawer closed and `inert`. Per the HTML specification, `inert` removes an element from the accessibility tree and blocks interaction; it does not remove the element or its `href` attributes from the DOM ([WHATWG HTML, the inert attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute)). The same links are also duplicated in the footer (`src/layout.html:57-74`), which is never inert, so every destination has a second, unconditional path regardless of how a crawler treats `inert`. No risk.

The seasonal tab panels differ between a non-JS and a JS render. In the HTML, all four `<div role="tabpanel">` elements are present with no `hidden` attribute, so a non-rendering crawler reads all four seasons. `site.js:249` sets `p.hidden = i !== j`, so Googlebot's rendered DOM has one visible panel and three hidden. This is the supported pattern: Google's mobile-first indexing guidance permits moving content into accordions and tabs, and draws the line at content that needs an interaction to load, warning "don't lazy-load primary content upon user interaction" ([Google, Mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)). All four panels are in the served HTML, so no interaction is required to load anything. On `/foraging/` that is 24 seasonal basket items and on `/private-chef/` 24 dishes, all present either way. No defect, recorded so a later audit does not raise it.

**F28. `geo` precision.**

Evidence. `build.py:101`: `"latitude": 39.3077, "longitude": -123.7995`, four decimal places. Google's LocalBusiness reference asks for "at least 5 decimal places".

Fix. Take the coordinates from the Google Business Profile so they match exactly, rather than adding a fifth digit to town-centre coordinates.

**F29. The live deployment is two commits behind HEAD.**

Evidence. Live `/about/` serves an eager `matt-kitchen.jpg` hero image and alt text reading "A wooden bowl of salad and edible flowers on a deck rail above a green hillside"; HEAD's `src/pages/about.html:4` is a `hero--plain` with no image and `:80` reads "A plated course from a private dinner". Live CSS is `site.f4ae1c62.css`; HEAD builds `site.181b90e3.css`. The live `last-modified` is `Fri, 18 Sep 2026 15:14:26 GMT`, and commits `d00c323` and `864e4ed` both landed 2026-09-19.

`git diff --stat b7eb62b HEAD -- build.py vercel.json src/layout.html` is empty, so every finding above holds for both the deployed build and HEAD. Only page copy and image assets moved.

Fix. Redeploy before acting on any measurement in this report, then re-check F1's `<picture>` count on the live host as the acceptance test for the Pillow fix.

---

## Proposed JSON-LD

Four blocks, written to link into one graph through `@id`. Every value below comes from CONTEXT.md except the two marked `CONFIRM`, which must not ship until Matt answers.

### Home, LocalBusiness

Replaces the `else` branch of `jsonld()` at `build.py:88-105`.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://spontaneouscafe.com/#business",
  "name": "The Spontaneous Cafe",
  "alternateName": "Chef Matt Samuelson",
  "additionalType": "https://www.wikidata.org/wiki/Q1379834",
  "description": "Chef Matt Samuelson forages, shops and cooks on the Mendocino coast. Private dinners, catering, foraging days and cooking classes.",
  "url": "https://spontaneouscafe.com/",
  "image": [
    "https://spontaneouscafe.com/assets/img/matt-kitchen.jpg",
    "https://spontaneouscafe.com/assets/img/matt-square.jpg"
  ],
  "logo": "https://spontaneouscafe.com/assets/logo/wordmark.svg",
  "telephone": "+1-707-972-6647",
  "email": "chefmattsamuelson@gmail.com",
  "founder": { "@id": "https://spontaneouscafe.com/about/#matt" },
  "employee": { "@id": "https://spontaneouscafe.com/about/#matt" },
  "foundingDate": "2009",
  "slogan": "Local, Organic, Wild",
  "priceRange": "$300 to $1000",
  "currenciesAccepted": "USD",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Mendocino",
    "addressRegion": "CA",
    "postalCode": "95460",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 39.30765, "longitude": -123.79947 },
  "hasMap": "https://www.google.com/maps?cid=7343978535458024901",
  "areaServed": [
    { "@type": "AdministrativeArea", "name": "Mendocino County, California" },
    { "@type": "City", "name": "Mendocino" },
    { "@type": "City", "name": "Fort Bragg" },
    { "@type": "City", "name": "Albion" }
  ],
  "knowsAbout": [
    "Foraging", "Wild mushrooms", "Sea salt harvesting",
    "Farm-to-table cooking", "Private chef service", "Culinary instruction"
  ],
  "makesOffer": [
    {
      "@type": "Offer",
      "name": "Three hours",
      "price": "300",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://spontaneouscafe.com/contact/",
      "itemOffered": { "@type": "Service", "name": "Three-hour booking, any service" }
    },
    {
      "@type": "Offer",
      "name": "Six hours",
      "price": "500",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://spontaneouscafe.com/contact/",
      "itemOffered": { "@type": "Service", "name": "Six-hour booking, any service" }
    },
    {
      "@type": "Offer",
      "name": "Twelve hours",
      "price": "1000",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://spontaneouscafe.com/contact/",
      "itemOffered": { "@type": "Service", "name": "Twelve-hour booking, any service" }
    }
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Services",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Foraging excursions", "url": "https://spontaneouscafe.com/foraging/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Private chef", "url": "https://spontaneouscafe.com/private-chef/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Catering and events", "url": "https://spontaneouscafe.com/catering/" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Cooking classes", "url": "https://spontaneouscafe.com/cooking-classes/" } }
    ]
  }
}
```

Two values need Matt before this ships. `postalCode: "95460"` is the Mendocino town code and must instead match whatever address the Google Business Profile carries; CONTEXT.md records Matt's home kitchen in Albion (95410), so this is a real fork, not a typo. Tag it `<!-- CONFIRM postal code must match the GBP exactly -->`. The `geo` coordinates above are Mendocino town centre to five places and should be replaced with the GBP's own coordinates.

`openingHoursSpecification` is deliberately absent. Matt books by inquiry with no published hours, and inventing hours would misrepresent the business. Add it only if he states hours.

`aggregateRating` and `review` are deliberately absent. Google recommends them "only recommended for sites that capture reviews about other local businesses", and self-serving review markup breaks the structured data policies. Reviews belong on the Google Business Profile.

`additionalType` points at the Wikidata item for personal chef. Verify the QID resolves before shipping, or drop the line; it is optional.

### A service page, Service

Replaces the `if` branch of `jsonld()` at `build.py:69-86`. Shown with `/foraging/` filled in; `build.py` substitutes per page.

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://spontaneouscafe.com/foraging/#service",
  "name": "Foraging excursions",
  "serviceType": "Guided foraging excursion",
  "url": "https://spontaneouscafe.com/foraging/",
  "description": "Foraging days on the Mendocino coast with Chef Matt Samuelson. Beach salt, wild mushrooms, unstaffed farm stands and dinner cooked from the baskets.",
  "image": "https://spontaneouscafe.com/assets/img/foraging-poster.jpg",
  "provider": { "@id": "https://spontaneouscafe.com/#business" },
  "areaServed": { "@type": "AdministrativeArea", "name": "Mendocino County, California" },
  "audience": { "@type": "Audience", "audienceType": "Visitors to the Mendocino coast" },
  "offers": [
    {
      "@type": "Offer",
      "name": "Three hours",
      "price": "300",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://spontaneouscafe.com/contact/?service=Foraging%20excursion&tier=3%20hours",
      "itemOffered": { "@type": "Service", "name": "Foraging excursions, three hours" }
    },
    {
      "@type": "Offer",
      "name": "Six hours",
      "price": "500",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://spontaneouscafe.com/contact/?service=Foraging%20excursion&tier=6%20hours",
      "itemOffered": { "@type": "Service", "name": "Foraging excursions, six hours" }
    },
    {
      "@type": "Offer",
      "name": "Twelve hours",
      "price": "1000",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock",
      "url": "https://spontaneouscafe.com/contact/?service=Foraging%20excursion&tier=12%20hours",
      "itemOffered": { "@type": "Service", "name": "Foraging excursions, twelve hours" }
    }
  ]
}
```

Build code for `build.py:58-86`:

```python
BUSINESS_ID = SITE + '/#business'

SERVICE_SLUGS = {
    'foraging': ('Guided foraging excursion', 'Foraging%20excursion'),
    'private-chef': ('Private chef service', 'Private%20chef'),
    'catering': ('Event catering', 'Catering%20and%20events'),
    'cooking-classes': ('Cooking class', 'Cooking%20class'),
}


def offers(service_name=None, param=None):
    out = []
    for name, price in TIERS:
        offer = {
            "@type": "Offer",
            "name": name,
            "price": price,
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "itemOffered": {
                "@type": "Service",
                "name": (f'{service_name}, {name.lower()}' if service_name
                         else f'{name} booking, any service'),
            },
        }
        if param:
            tier = name.split()[0].lower()
            digits = {'three': '3', 'six': '6', 'twelve': '12'}[tier]
            offer["url"] = f'{SITE}/contact/?service={param}&tier={digits}%20hours'
        else:
            offer["url"] = f'{SITE}/contact/'
        out.append(offer)
    return out
```

### About, Person

New block, emitted only on `/about/`. Every fact below is from CONTEXT.md's "Resume facts (2026-09-11)" section.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://spontaneouscafe.com/about/#matt",
  "name": "Matthew Samuelson",
  "alternateName": "Chef Matt Samuelson",
  "jobTitle": "Chef and forager",
  "description": "Chef, forager and culinary instructor on the Mendocino coast. Head chef and instructor at Living Light Culinary Arts Institute, executive chef at Flow Restaurant and Lounge, and founder of The Spontaneous Cafe.",
  "image": "https://spontaneouscafe.com/assets/img/matt-kitchen.jpg",
  "url": "https://spontaneouscafe.com/about/",
  "worksFor": { "@id": "https://spontaneouscafe.com/#business" },
  "telephone": "+1-707-972-6647",
  "email": "chefmattsamuelson@gmail.com",
  "knowsAbout": [
    "Foraging", "Wild mushroom identification", "Sea salt harvesting",
    "Raw food cuisine", "Vegan cuisine", "Gluten free cuisine",
    "Menu development", "Culinary instruction"
  ],
  "hasOccupation": {
    "@type": "Occupation",
    "name": "Personal chef",
    "occupationLocation": { "@type": "AdministrativeArea", "name": "Mendocino County, California" }
  },
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "Living Light Culinary Arts Institute",
    "address": { "@type": "PostalAddress", "addressLocality": "Fort Bragg", "addressRegion": "CA", "addressCountry": "US" }
  },
  "homeLocation": { "@type": "Place", "name": "Albion, California" }
}
```

`sameAs` is deliberately absent. The business has no confirmed social profiles in CONTEXT.md, and `sameAs` pointing at anything unverified is worse than omitting it. Add profile URLs once Matt supplies them.

`alumniOf` is a compromise. Matt taught at Living Light rather than studying there; schema.org has no clean "taught at" property for a Person, and `worksFor` is already taken by the business. If exactness matters more than the association, replace `alumniOf` with:

```json
"affiliation": {
  "@type": "EducationalOrganization",
  "name": "Living Light Culinary Arts Institute"
}
```

### BreadcrumbList

Two levels on every page but the home page. `item` is omitted on the last entry, which Google explicitly permits.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://spontaneouscafe.com/" },
    { "@type": "ListItem", "position": 2, "name": "Foraging excursions" }
  ]
}
```

Build code. Add to `build.py` after `jsonld()`, and add `"crumb"` to the recognised meta keys documented at `build.py:13`:

```python
CRUMBS = {
    'foraging': 'Foraging excursions',
    'private-chef': 'Private chef',
    'catering': 'Catering and events',
    'cooking-classes': 'Cooking classes',
    'about': 'About Matt',
    'contact': 'Contact',
    'privacy': 'Privacy',
}


def breadcrumb_jsonld(slug):
    """Two-level trail on every page but the home page. Google allows the last
    ListItem to omit `item`; it then uses the containing page's URL."""
    label = CRUMBS.get(slug)
    if not label:
        return ''
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": label},
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'
```

and at `build.py:284`, change:

```python
        html = html.replace('{{content}}', responsive_images(body) + faq_jsonld(body))
```

to:

```python
        html = html.replace('{{content}}', responsive_images(body)
                            + breadcrumb_jsonld(slug) + faq_jsonld(body))
```

Add matching visible breadcrumbs above each `h1`. Google does not require the visible trail for the rich result, but structured data that describes nothing on the page contradicts the structured data guidelines.

### Blocks deliberately not proposed

`WebSite` with `potentialAction: SearchAction` buys nothing. Google retired the sitelinks search box in October 2023 ([Google Search Central blog, Sitelinks search box is going away](https://developers.google.com/search/blog/2023/10/sitelinks-search-box)), and the site has no search. A bare `WebSite` node with `name` and `url` is harmless and adds no signal the LocalBusiness node does not already carry.

`Event` is wrong. The classes and excursions have no fixed dates or venues; they are booked by inquiry. `Event` markup without a real `startDate` and `location` breaks the guidelines.

`Recipe` on the sample menus is wrong. The menus are lists of dish names with no ingredients, quantities or method, and CONTEXT.md's round-3 rules explicitly reject recipe framing.

---

## vercel.json before and after cutover

Both files assume the `SITE_URL` change from F2 and the `requirements.txt` from F1 are in place.

### Before DNS cutover

Three changes from the current file: the `/privacy-policy/` rule (F4), a host-scoped `X-Robots-Tag` on the Vercel alias (F5), and `Vary` (F20). The cache split from F19 is included.

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "buildCommand": "python3 build.py",
  "outputDirectory": "dist",
  "cleanUrls": true,
  "trailingSlash": true,
  "redirects": [
    { "source": "/privacy-policy", "destination": "/privacy/", "permanent": true },
    { "source": "/privacy-policy/", "destination": "/privacy/", "permanent": true }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "has": [{ "type": "host", "value": { "eq": "spontaneous-cafe.vercel.app" } }],
      "headers": [
        { "key": "X-Robots-Tag", "value": "noindex, nofollow" }
      ]
    },
    {
      "source": "/assets/(css|js|fonts)/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/assets/(img|video)/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Vary", "value": "Accept-Encoding" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; img-src 'self' data:; media-src 'self'; font-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self' https://formspree.io; form-action 'self' https://formspree.io; frame-ancestors 'none'; base-uri 'self'" }
      ]
    }
  ]
}
```

Also set the Vercel project environment variable `SITE_URL=https://spontaneous-cafe.vercel.app` for the Production environment, so the staging host self-canonicalises while the noindex is in force. Without that, the `noindex` sits on a page whose canonical names the live GoDaddy site, and the `noindex` can carry to the canonical target.

Verification after deploying:

```
curl -sI https://spontaneous-cafe.vercel.app/foraging/ | grep -i x-robots-tag
curl -s  https://spontaneous-cafe.vercel.app/foraging/ | grep -E 'canonical|og:url|og:image'
curl -sI https://spontaneous-cafe.vercel.app/privacy-policy/ | head -3
```

Expect `x-robots-tag: noindex, nofollow`, all three meta URLs on `spontaneous-cafe.vercel.app`, and a 308 to `/privacy/`.

The `has` with `type: "host"` should be confirmed on a preview deployment first. Vercel's published schema declares it valid for both `headers` and `redirects` and requires exactly `type` and `value`, but every worked example in the prose documentation uses `type: "header"`, so the host form has not been exercised on this project.

### After DNS cutover

The `X-Robots-Tag` header block becomes a host-scoped 308 to the real domain, and `SITE_URL` is deleted from the Vercel project so `build.py` falls back to `https://spontaneouscafe.com`.

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "buildCommand": "python3 build.py",
  "outputDirectory": "dist",
  "cleanUrls": true,
  "trailingSlash": true,
  "redirects": [
    {
      "source": "/:path*",
      "has": [{ "type": "host", "value": { "eq": "spontaneous-cafe.vercel.app" } }],
      "destination": "https://spontaneouscafe.com/:path*",
      "permanent": true
    },
    { "source": "/privacy-policy", "destination": "/privacy/", "permanent": true },
    { "source": "/privacy-policy/", "destination": "/privacy/", "permanent": true }
  ],
  "headers": [
    {
      "source": "/assets/(css|js|fonts)/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/assets/(img|video)/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Vary", "value": "Accept-Encoding" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; img-src 'self' data:; media-src 'self'; font-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self' https://formspree.io; form-action 'self' https://formspree.io; frame-ancestors 'none'; base-uri 'self'" }
      ]
    }
  ]
}
```

`permanent: true` produces a 308, which Google treats as equivalent to a 301 for canonicalisation ([Google, redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)). `"statusCode": 301` is also supported if a literal 301 is preferred for older tooling.

Note the two-hop path on slashless URLs. A request for `https://spontaneous-cafe.vercel.app/about` gets a 308 to `/about/` from `trailingSlash` first, then a 308 to `https://spontaneouscafe.com/about/`. Two hops is within Google's tolerance and costs nothing in practice, but it explains the extra redirect if anyone measures it.

Four cutover items that do not live in `vercel.json`:

1. Add `spontaneouscafe.com` and `www.spontaneouscafe.com` to the Vercel project, with the apex as primary. Vercel issues the `www` to apex redirect automatically when both are attached. GoDaddy currently answers `https://www.spontaneouscafe.com/` with a 301 to the apex, and that behaviour must survive.
2. Delete `SITE_URL` from the Production environment and redeploy, so canonical, `og:url`, `og:image`, sitemap and robots all return to `spontaneouscafe.com`.
3. Verify `https://spontaneouscafe.com/foraging/` serves the new page and not the cached GoDaddy one. That path is the only collision.
4. Add `spontaneouscafe.com` to Search Console, submit `https://spontaneouscafe.com/sitemap.xml`, and check that the old GoDaddy sitemap index at `/sitemap.website.xml` and `/sitemap.ols.xml` stops returning 200 after cutover. They 404 automatically once DNS moves, since the new site has no such files.

---

## PageSpeed results

No PageSpeed Insights scores were obtained. The keyless API is quota-capped at zero requests per day, not rate-limited, so retrying does not help:

```
home attempt1 http=429  |  foraging attempt1 http=429
home attempt2 http=429  |  foraging attempt2 http=429
home attempt3 http=429  |  foraging attempt3 http=429
(plus one further attempt on home, also 429)

"message": "Quota exceeded for quota metric 'Queries' and limit 'Queries per day'
            of service 'pagespeedonline.googleapis.com'",
"quota_limit": "defaultPerDayPerProject",
"quota_limit_value": "0"
```

All four targets (home mobile, `/foraging/` mobile, `/private-chef/` mobile, home desktop) failed across four attempts with sixty-second waits, per the brief. Lighthouse is not installed locally and installing it was out of scope. To get the scores, create a Google Cloud API key with the PageSpeed Insights API enabled and append `&key=...`, or run `npx lighthouse` locally.

What was measured instead, from resource timing in a real Chromium and from `curl` against the live host. Transfer sizes are exact; the LCP element is determined by analysis rather than measured, because the browser pane ran without a paint surface and reported no LCP or paint entries.

| Page | HTML (br) | HTML (raw) | Fonts | Images served | Images if `<picture>` worked (DPR 2) | LCP element |
|---|---|---|---|---|---|---|
| `/` | 4,456 B | 14,246 B | 181,804 B | 2,160,027 B | 497,738 B | `home-poster.jpg`, 64,376 B, video poster |
| `/foraging/` | est. 7,000 B | 25,201 B | 181,804 B | 1,085,100 B | 318,066 B | `foraging-poster.jpg`, 119,112 B, video poster |
| `/private-chef/` | est. 6,500 B | 23,424 B | 181,804 B | 492,322 B | 79,772 B | `chef-poster.jpg`, 69,097 B, video poster |
| `/catering/` | est. 6,800 B | 24,426 B | 181,804 B | 252,184 B | 50,850 B | `catering-poster.jpg`, 64,910 B, video poster |
| `/cooking-classes/` | est. 6,400 B | 22,874 B | 181,804 B | 1,004,921 B | 194,810 B | `classes-poster.jpg`, 58,356 B, video poster |
| `/about/` | est. 3,700 B | 12,120 B | 181,804 B | 1,550,311 B | 319,500 B | `h1` text block (hero has no image at HEAD) |
| `/contact/` | est. 4,000 B | 13,068 B | 181,804 B | 0 B | 0 B | `h1` text block |
| `/privacy/` | est. 2,600 B | 8,326 B | 181,804 B | 0 B | 0 B | `h1` text block |

Rows marked `est.` scale the measured home-page Brotli ratio of 3.20:1 to each page's raw size. The home-page figure of 4,456 B is measured.

Measured navigation timing on `/`, from `performance.getEntriesByType('navigation')` against the live host over a warm CDN cache: TTFB 221 ms, DOMContentLoaded 294 ms, load 295 ms, 224 DOM nodes, nine subresources, 251,053 B total on first view with images below the fold not yet lazy-loaded. Cumulative Layout Shift measured 0 on both `/` and `/foraging/`, which is expected given every `<img>` carries explicit `width` and `height` and the fonts use `font-display: swap` with no size-adjust gap.

The five hero pages all put a full-size JPEG poster on the critical path with no preload and no `fetchpriority`. On `/foraging/` that is 119,112 B where 49,802 B covers the same phone. LCP at 2.5 seconds or better is the target ([web.dev, Largest Contentful Paint](https://web.dev/articles/lcp)); the poster plus 181,804 B of fonts, of which 74,572 B is preloaded ahead of it, is the whole of the critical path to beat.

---

## Top 10 actions

Ordered by impact, then by effort within a tier.

1. **Add `requirements.txt` with `Pillow>=11.0`, and make `image_size()` exit on ImportError.** F1. Two files, ten minutes, restores `<picture>`, WebP and `og:image` dimensions across eight pages and cuts 5.08 MB from the six image-carrying pages. Nothing else in this list moves the needle as far for as little work.
2. **Move `SITE` to `os.environ.get('SITE_URL', ...)` and set `SITE_URL=https://spontaneous-cafe.vercel.app` on Vercel Production.** F2, F3. One line plus a dashboard variable. Stops the site advertising a canonical that resolves to a different page, and fixes the 404ing `og:image` in the same move. Reversed by deleting the variable at cutover.
3. **Add the host-scoped `X-Robots-Tag: noindex` to `vercel.json`, after action 2 is live.** F5. Keeps the staging host out of the index until the domain is real. Order matters: doing this before action 2 risks carrying the `noindex` to the live GoDaddy site through the canonical.
4. **Add the `/privacy-policy/` redirect.** F4. One line. It rescues one of the three URLs the old site has in its sitemap, and the rule that was meant to do it has never fired.
5. **Delete the Caveat preload from `src/layout.html:19` and preload `source-sans-3-latin.woff2` instead.** F6. One line moved. Takes 74,572 B off the top-priority critical path on all eight pages, including `/privacy/`, which uses the font for nothing. Subsetting Caveat later takes it further.
6. **Replace the five `poster=` attributes with a `<picture>` sibling and add a per-page poster preload.** F7. Five page edits plus about twelve lines in `build.py` and two CSS rules. The LCP image on every hero page then gets WebP, a real srcset and `fetchpriority="high"` instead of a single full-size JPEG.
7. **Rewrite `jsonld()` around a single `@id`, move the Maps CID to `hasMap`, swap the business `image` to a photo of Matt, and add the Person and BreadcrumbList blocks.** F8, F9, F11. One function plus two small ones, all drafted above. Collapses up to nine business entities into one, adds the one rich result the site can still earn, and ties the site to the Google Business Profile.
8. **Add the robots meta with `max-image-preview:large` to indexable pages.** F13. Four lines in `head_meta()`. On a business selling a visual experience, the large image preview in mobile results and Discover is worth more than its effort.
9. **Split the `/assets/` cache rule so images and video revalidate daily instead of never.** F19. Six lines in `vercel.json`. With Matt's photo swaps still open, the current `immutable` year means returning visitors keep placeholders after the real photos ship.
10. **Add `apple-touch-icon.png` and `favicon.ico`, set per-page `og_alt`, add `twitter:image`, trim the About description to 155 characters, and change the two footer `h2`s to paragraphs.** F12, F14, F15, F16, F17. Five small edits grouped because each is under five minutes and none is worth its own deploy.

Not on this list and worth saying out loud: leave the FAQPage markup alone (F10), leave the `/contact/?service=` links alone (F24), and do not add `aggregateRating` (F8). Redeploy before measuring anything, since the live build is two commits behind HEAD (F29).
