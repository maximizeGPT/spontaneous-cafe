# Verification, SEO round 2026-09-19

Independent check of branch `seo/2026-09-19` at merge commit `00d84d5`, against `main` at `218aa1a`. Run by an agent that wrote none of the code or copy. Nothing was committed, pushed or deployed. Working tree touched once, for the manifest fix in section "Fixes made".

## Verdict

Ship-ready once one decision is made. Every mechanical check passes: the build is deterministic with and without Pillow, all nine pages validate at the W3C with zero errors, every JSON-LD block parses and every `@id` resolves on its own page, the schema.org validator returns zero errors and zero warnings on the home graph, `vercel.json` validates against Vercel's own schema, every internal link and image path in `dist` resolves, and the new copy is clean of em dashes and of the banned vocabulary. The one thing that should be settled before deploy is decision 8's removal of the Caveat preload. Caveat still sets the accent word in every hero h1, so dropping its preload lets the heading reflow when the font swaps in. Measured on the foraging page, that is a cumulative layout shift of 0.183 against main's 0.077, and a Lighthouse performance score of 83 against main's 89. Restoring the preload on a scratch copy of the same build takes the shift to 0 and the score to 93, so the cause is settled and the fix is one line. Beyond that there are four items for a human: an Alignable `sameAs` that CONTEXT.md does not cover, three of the four retreat bullets that repeat the paragraph above them, the retreat block leaving the right half of its band empty, and two new FAQ answers that carry no first-person marker where the page's other answers do.

## Matrix

| # | Check | Result | Evidence |
|---|---|---|---|
| 1a | `python3 build.py` succeeds and prints the host | Pass | `mode: production (chips and .ph stripped)` / `host: https://spontaneouscafe.com` / `built 9 pages` |
| 1b | Second build with Pillow blocked produces an identical tree | Pass | Pillow 11.3.0 is installed and the block raises `ModuleNotFoundError: import of PIL halted`. `diff -r <scratch>/dist-pil dist` printed nothing. |
| 1c | `<picture>` count per page | Pass | index 11, about 7, cooking-classes 6, foraging 5, private-chef 3, catering 2, contact 0, privacy 0, 404 0 |
| 2a | Every JSON-LD block parses after unescaping `<\/` | Pass | 8 indexable pages, 1 graph block each plus the FAQPage blocks. Script `check_jsonld.py`, `RESULT: PASS`. |
| 2b | Every `@id` referenced on a page is defined on that page | Pass | Same script. Zero unresolved references across all pages. |
| 2c | Graph contains WebSite, LocalBusiness `#business`, Person `#matt`, WebPage | Pass | Same script, no missing-node failures. |
| 2d | Service on the four service pages, `provider` = `#business` | Pass | foraging, private-chef, catering, cooking-classes all carry a Service whose provider is `https://spontaneouscafe.com/#business` |
| 2e | Offers carry 300, 500 and 1000 as strings with `priceCurrency` USD | Pass | `[('300','USD'),('500','USD'),('1000','USD')]` on every business node and every Service node |
| 2f | `hasMap` with cid 7343978535458024901 | Pass | `https://www.google.com/maps?cid=7343978535458024901` on every page |
| 2g | Six `areaServed` places | Pass | Mendocino, Fort Bragg, Little River, Albion, Elk, Anderson Valley |
| 2h | No `openingHoursSpecification`, no `postalCode` | Pass | Neither key appears in any business node |
| 2i | No Review or AggregateRating anywhere | Pass | `"Review"`, `"review"`, `"AggregateRating"`, `"aggregateRating"` all absent from every parsed block |
| 2j | `dist/404.html` has no JSON-LD | Pass | Zero `application/ld+json` blocks |
| 2k | Every site-host image, logo and url in the graphs resolves in dist | Pass | 50 distinct `https://spontaneouscafe.com/...` URLs checked, 0 missing |
| 2l | Every `@type` and property exists in the schema.org vocabulary | Pass | 3,023 terms loaded from `schemaorg-current-https.jsonld`. 17 types and 53 property keys used, 0 unknown. |
| 2m | validator.schema.org on the home graph | Pass | 0 errors, 0 warnings. One top-level item (WebPage) with the rest nested by `@id`, which is itself confirmation the graph joins up. |
| 3a | Exactly one h1 per page | Pass | All nine pages |
| 3b | Title 60 characters or fewer | Pass | 404 37, about 53, catering 57, contact 55, cooking-classes 52, foraging 51, index 59, privacy 41, private-chef 49 |
| 3c | Meta description 120 to 155 | Pass | 404 138, about 139, catering 142, contact 139, cooking-classes 148, foraging 138, index 148, privacy 143, private-chef 144 |
| 3d | Canonical present and absolute on the eight indexable pages | Pass | All start `https://spontaneouscafe.com/` |
| 3e | og:title, og:description, og:url, og:image, og:image:alt, og:image:width, og:image:height | Pass | Present on all eight. Declared dimensions match the files on disk, checked page by page. |
| 3f | og:image:alt page-specific, no two service pages identical | Pass | Four distinct strings across the service pages. Each one also matches the photograph, checked against a contact sheet of the seven og images. |
| 3g | twitter:card, twitter:title, twitter:description, twitter:image | Pass | Present on all eight |
| 3h | robots meta carries `max-image-preview:large` | Pass | `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` |
| 3i | Icon links for favicon.ico, the SVG and apple-touch-icon, files present | Pass | `/favicon.ico`, `/assets/logo/favicon.svg`, `/apple-touch-icon.png` all linked and all present in dist |
| 3j | Font preloads point at files that exist, no Caveat preload | Pass | `lora-latin.woff2` and `source-sans-3-latin.woff2` both present. No Caveat preload. See section "For a human" item 1 for what that costs. |
| 3k | Hero preload `imagesrcset` byte-identical to the WebP `<source srcset>` | Pass | MATCH on all five hero pages. One network request per poster confirmed: loading `/foraging/` fetched `foraging-poster-480.webp` once and nothing else for that image. |
| 3l | 404 has robots noindex, no canonical, no og:url | Pass | `noindex, follow`, canonical stripped, og:url stripped |
| 4a | Every internal href, src, srcset candidate and poster resolves in dist | Pass | 270 hrefs, 361 asset references across 9 pages, 0 missing, cleanUrls honoured |
| 4b | Every fragment link resolves to an id on the target page | Pass | 33 fragments, 0 unresolved |
| 4c | sitemap.xml lists the eight indexable URLs with lastmod | Pass | 8 `<loc>` entries matching the expected set, 0 entries without `<lastmod>` |
| 4d | robots.txt has Allow /, Disallow /api/, sitemap line | Pass | All three present |
| 5 | W3C Nu validator, errors per page | Pass | 0 errors on all nine pages. Two warnings, both "Section lacks heading" (foraging line 646, private-chef line 644). Main build also returned 0 errors, so there is no inherited baseline to discount. |
| 6a | vercel.json validates against Vercel's schema | Pass | `jsonschema` 4.25.1 against `https://openapi.vercel.sh/vercel.json` (draft-04), 0 errors |
| 6b | Host regex matches staging and not the real domain | Pass | `re.fullmatch("spontaneous-cafe\\.vercel\\.app", "spontaneous-cafe.vercel.app")` is True; the same pattern against `"spontaneouscafe.com"` is False under both `fullmatch` and `search` |
| 6c | CSP byte-identical to main's | Pass | 251 bytes on both, equal as bytes |
| 7a | Zero U+2014 em dashes in changed copy | Pass | 0 in the added `src/pages` lines, 0 across the whole branch diff |
| 7b | Zero hits for the banned vocabulary list | Pass | All 20 terms at 0 in the added `src/pages` lines |
| 7c | No "not X, it's Y" or "not just" constructions | Pass | "not just", "isn't about", "is not about" and rhetorical " rather than " all absent |
| 7d | No claim-then-restate | Fail, reported | Three of the four Retreat catering bullets repeat the two paragraphs above them. Quoted in "For a human" item 2. |
| 7e | No trailing participial clauses that could be split | Pass for new copy | The one instance on the home service card ("gathering beach salt, wild mushrooms and berries with Matt") is inherited from main; only the adjectives changed this round. |
| 7f | FAQ answers in first person, service copy in third | Mostly pass | Two of the four new private chef answers carry no first-person marker. Quoted in "For a human" item 4. All new body copy is third person. |
| 7g | Block titles two to five words naming the block | Pass | One new block title, "Retreat catering", two words, no turn, no lede |
| 7h | about.html differs from main only in its first three lines | Pass | 146 lines in both files, line 2 is the only difference |
| 8 | New client claims traced to CONTEXT.md, main's pages, or a CONFIRM tag | One flag | Full trace below. Every page claim traces. The `sameAs` Alignable URL in build.py does not. |
| 9 | Public-repo hygiene | Pass | 0 hits for Rayed, 1ua7BsGJU, yahoo, sk-, token, password, Drive folder ids and `/Users/main` across every added line of the branch diff, and 0 in SEO-PLAN.md, the only file this branch adds to that folder. The branch in fact removes a name: `R3-local-entity.md:73` changed "one from the account \"Rayed Wasif\"" to "one from an account connected to the consultant". Two pre-existing items are noted under "For a human" item 5. |
| 10 | Heroes look the same as main apart from copy changes | Pass with one expected difference | Hero geometry measured in the DOM at 1280 and at 375. Identical on home, private chef, catering and cooking classes at both sizes. Foraging is 85 px taller at 1280 and 40 px taller at 375, because the h1 gains "Mushroom" and wraps to three lines. No horizontal overflow at either width. |
| 11 | Lighthouse | Regression | Table below. Accessibility, best practices and SEO are 100 on every run. Performance on foraging drops from 89 to 83, and CLS from 0.077 to 0.183. |
| 12 | Manifest entry for the four new logo files | Fixed | Added, see "Fixes made" |

## Lighthouse

Mobile emulation, the default. Branch served from `dist` on port 8793, main built from `git archive main` and served on 8794.

| Run | Performance | Accessibility | Best practices | SEO | LCP | CLS | FCP |
|---|---|---|---|---|---|---|---|
| Branch, home | 93 (94 on a second run) | 100 | 100 | 100 | 3.0 s | 0.042 | 1.7 s |
| Branch, foraging | 83 (84 on a second run) | 100 | 100 | 100 | 3.2 s | 0.183 | 2.0 s |
| Main, home | 93 (93 on a second run) | 100 | 100 | 100 | 3.2 s | 0.000 | 1.4 s |
| Main, foraging (added for a baseline) | 89 | not run | not run | not run | 3.5 s | 0.077 | 1.7 s |
| Diagnostic: branch foraging plus a Caveat preload | 93 | not run | not run | not run | 3.2 s | 0.000 | not recorded |
| Diagnostic: branch home plus a Caveat preload | 94 | not run | not run | not run | 3.0 s | 0.000 | not recorded |

Lighthouse could not name the LCP element in any run: the `largest-contentful-paint-element` audit is absent from all six reports, so the LCP node is not available from this data. The layout shift audit did name the shifting element. On branch foraging the shift is scored 0.1834 against `<p class="lede">`, which sits directly under the h1 that contains the Caveat word. On branch home it is 0.0416 against `<div class="wrap">` with the cause "Media element lacking an explicit size". Main home shows the same cause at 0.0003. The two diagnostic rows are the proof: a scratch copy of the branch build with a Caveat preload added back to the head, and nothing else changed, scores 0 on both pages.

## Fixes made

1. `src/assets/MANIFEST.md:36` to `:48`. Added a "Logo raster files (rendered 2026-09-19)" section listing `favicon.ico` (32x32), `favicon-32.png` (32x32), `apple-touch-icon.png` (180x180) and `wordmark.png` (1024x368), each with the SVG it came from and what uses it. Sizes read from the files. Noted that all four are rendered from this project's own SVGs, so there is no licence question. The manifest is excluded from `dist` by `build.py`, and `diff -r` confirms the built tree is unchanged after the edit.

No other file was changed. Nothing else in the round needed a mechanical fix.

## For a human

1. **The Caveat preload.** Decision 8 drops it on the reasoning that Caveat sets four words. Caveat still sets the accent word in all five hero h1s, and those h1s are the first paint on every hero page, so the swap moves the heading. Foraging pays 0.183 CLS and six Lighthouse points for it; home pays 0.042. Three ways out: put the preload back and accept 74 KB, subset Caveat to the handful of glyphs the heroes use (the plan already defers this at roughly 10 KB), or set `font-display: optional` on Caveat so a late font never reflows. The first is one line and reproduces a score of 93 on both pages. Mohammed's call, because the plan decided the other way on purpose.
2. **Three retreat bullets restate the paragraph above them.** The paragraph says "book Matt for a whole stay, every meal for the group" and the bullet says "Every meal across a multi-day stay". The paragraph says "A stay can open with a foraging walk for the whole group, and a cooking class can stand in for one of the dinners" and the bullet says "A foraging walk or a cooking class booked into the same stay". The paragraph says "retreat menus for twenty to eighty guests" and the bullet says "Twenty to eighty at the table, and larger events with a crew". Only the second bullet adds anything, the word "allergy". Copy call, so it is reported rather than changed.
3. **The Retreat catering block sits in one narrow column.** The two bands above it and the band below it use the full width: "Service styles" is a three-column grid, "Sample event menus" is a wide card. The new block leaves the right half of its band empty, which breaks the page's rhythm. Screenshot: `<scratch>/shots/catering-retreat-in-context.png`. Design call.
4. **Two new FAQ answers have no first-person marker.** "How much does a private chef cost for a day?" and "How much does a private chef cost for a dinner party?" are written neutrally ("Twelve hours is $1,000", "Most dinner parties run six hours"). Every other answer on that page uses "I", including the two other new ones. Neither drifts into third person about Matt, so this is a consistency question rather than a rule break.
5. **`sameAs` points at Alignable, which CONTEXT.md does not cover.** `build.py:188` puts `https://www.alignable.com/mendocino-ca/spontaneous-cafe` in the business node's `sameAs`, which tells Google that page is this business. The evidence is R3 section A, not CONTEXT.md, and R3 records that the same listing advertises a food truck that appears nowhere else in Matt's history and that the off-site checklist still holds open for him. A `sameAs` endorses the whole listing. Two options: hold the URL until Matt answers, or leave it in and move the Alignable cleanup ahead of the deploy. The Person node's `sameAs`, the Esalen faculty page, is covered by CONTEXT.md's teaching history line and returns 200.
6. **Two pre-existing hygiene items, outside this branch's diff.** `docs/seo-2026-09-19/R3-local-entity.md:43` carries `mattsamuelson@yahoo.com`, Matt's personal address from the resume, in a repo that is headed for public. The same file at line 34 carries a third party's street address in Pennsylvania, which is a published business address and lower risk. Both predate this branch, so neither fails check 9, and both are worth a decision before the repo goes public.

## Client facts trace

Every new or changed claim in `git diff 218aa1a..HEAD -- src/pages` and in the schema nodes in `build.py`, with what supports it.

| Claim | Where | Support |
|---|---|---|
| Retreat centers, camps and rented houses book Matt for a whole stay | catering.html, retreat section | `<!-- CONFIRM: retreat venues as a channel... -->` immediately above the section |
| Retreat menus for twenty to eighty guests, culinary intensives for hospitality teams | catering.html, retreat section | CONTEXT.md, resume facts: "Retreat menus for 20 to 80 guests, plus culinary intensives for hospitality teams and culinary professionals" |
| The dietary list is built into the first draft | catering.html, retreat section | main `catering.html`, Good to know: "designed with the menu on the first draft" |
| A stay can open with a foraging walk, a class can stand in for a dinner | catering.html, retreat section | CONTEXT.md: "Services combine into one booking (... retreat foraging walk then catered dinner ...)" |
| I quote every event above about twelve guests after the first call | catering.html, wedding FAQ | main `catering.html:103` "above about twelve guests" and `:104` "The quote is written after the first call" |
| The quote lists courses, service style, staff, rentals and travel | catering.html, wedding FAQ | main `catering.html:239` staff and rentals, `:242` travel into the quote |
| A typical wedding figure is withheld | catering.html, wedding FAQ | `<!-- CONFIRM: Matt, do you want a typical range published... -->` above it |
| Greater Mendocino, on the coast of Mendocino County | catering.html, Travel | main `catering.html:242`, existing `<!-- CONFIRM: travel radius -->` retained |
| Six named places in the service area | contact.html, Where | main `catering.html:242` "Fort Bragg to Elk and inland to Anderson Valley". Albion is Matt's own kitchen in CONTEXT.md. Little River and the other four sit inside that stated range. |
| Fort Bragg to Elk and inland to Anderson Valley | private-chef.html, Where | Same. Note that the same claim on `catering.html` carries a CONFIRM and the two repetitions do not. |
| Matt forages mushrooms, greens, berries and salt; meat and fish are bought | foraging.html | CONTEXT.md round 3: "Matt forages mushrooms, berries, greens and salt. He does not hunt, fish or butcher. Meat and fish are bought." |
| Bought from ranches inland and the boats at Noyo | foraging.html | main `catering.html:52` "a ranch inland, the boats at Noyo", `foraging.html:132` "Lamb comes from a ranch inland", `foraging.html:148` "Rockfish from Noyo Harbor" |
| Waterproof boots on mushroom days | foraging.html, wear FAQ | Generic advice, no claim about Matt or the business |
| Twelve hours $1,000, six $500, three $300, ingredients at cost | private-chef.html, FAQs 1 and 2 | CONTEXT.md prices line |
| Foraging or market morning then dinner, or breakfast and dinner for a full house | private-chef.html, FAQ 1 | main `private-chef.html:78` and `:82` |
| Six hours covers shopping, dinner for up to twelve, cleanup | private-chef.html, FAQ 2 | main `private-chef.html:67` |
| Ingredients at cost with the receipts | private-chef.html, FAQ 2 | main `private-chef.html:222` |
| Arrives with the shopping done, carries each course, clears up | private-chef.html, FAQ 3 | main `private-chef.html:31`, `:33`, `:56` |
| Cleans the kitchen, leftovers in your containers | private-chef.html, FAQ 4 | main `private-chef.html:33` |
| Personal chef versus private chef definition | private-chef.html, FAQ 3 | General industry definition, no claim about Matt beyond "I do the second" |
| og:image:alt on all eight pages | page meta | Each string checked against the photograph. All accurate. The About alt names Matt, and CONTEXT.md records `matt-kitchen.jpg` as a real photo of him. |
| Business description, slogan "Local, Organic, Wild", founding 2009, price range, phone, email | build.py business node | CONTEXT.md client facts and tagline line |
| `hasMap` cid | build.py business node | CONTEXT.md Google Business Profile line |
| Business images are `matt-kitchen.jpg` and `matt-square.jpg` | build.py business node | CONTEXT.md 2026-09-07 photo line |
| Person node dated roles: Living Light 2000 to 2004, 2008 to 2009, 2017 to 2019; Flow 2015 to 2017; Alive & Radiant 2011 to 2015; High Integrity Foods since 2006; Mendocino 2009 | build.py person node | CONTEXT.md resume facts, 2026-09-11, line by line |
| Person affiliations Living Light and Esalen | build.py person node | CONTEXT.md teaching history line |
| Person `sameAs` Esalen faculty page | build.py person node | CONTEXT.md teaching history plus R3 section A. URL returns 200. |
| Business `sameAs` Alignable page | build.py business node | **Not in CONTEXT.md and not on main's pages.** R3 section A only. See "For a human" item 5. The URL returned 429 from here, so it could not be re-read; R3 recorded its contents on 2026-09-19. |
| `additionalType` Product Ontology URIs | build.py business node | Not a client fact. Both URIs return 303 to `/doc/<term>` which returns 200, as the code comment claims. |
| Offer URLs pre-select the contact form | build.py offers | The emitted values (`service=Foraging%20excursion`, `tier=3%20hours`) match the `<option value>` strings in `contact.html` exactly, so `site.js` applies them. |

## Screenshots

All under `/private/tmp/claude-502/-Users-main-MOSI-Spontaneous-Cafe/63f47f85-1ed0-4a02-89ea-03ecbe93b07b/scratchpad/verify/shots/`.

| File | What it shows |
|---|---|
| `branch-{home,foraging,private-chef,catering,cooking-classes}-desktop.png` | Branch heroes at 1280x900 |
| `main-{same}-desktop.png` | Main heroes at 1280x900 |
| `branch-{same}-mobile.png`, `main-{same}-mobile.png` | Both builds at 375x812 |
| `cmp-{page}-{desktop,mobile}.png` | Branch beside main, one file per page and size |
| `cmp-all-mobile.png` | All five mobile pairs on one sheet |
| `catering-retreat-section.png` | The new Retreat catering band |
| `catering-retreat-in-context.png` | The same band with the bands above and below it |
| `private-chef-new-faqs-open.png` | The four new private chef FAQs open |
| `full-private-chef-faqs-open.png` | Full-page capture the crop came from |
| `foraging-h1.png`, `foraging-h1-crop.png` | The new foraging h1 |
| `og-images-contact-sheet.png` | The seven og images, used to check the alt text |

## How to reproduce

```
cd /Users/main/MOSI/spontaneous-cafe-seo
python3 build.py                                   # check 1a
cp -R dist /tmp/dist-pil
python3 -c "import sys; sys.modules['PIL']=None; import runpy; runpy.run_path('build.py', run_name='__main__')"
diff -r /tmp/dist-pil dist                          # check 1b, must be silent
curl -s -H "Content-Type: text/html; charset=utf-8" --data-binary @dist/foraging/index.html \
  "https://validator.w3.org/nu/?out=json"           # check 5
python3 -m http.server 8793 -d dist &
npx --yes lighthouse@latest http://localhost:8793/foraging/ \
  --only-categories=performance --chrome-flags="--headless=new" --quiet   # check 11
```

The scripts for checks 2, 3 and 4 are in the scratchpad as `check_jsonld.py`, `check_head.py` and `check_crawl.py`.

## Housekeeping

Both static servers were killed, along with the two diagnostic servers on 8795 and 8796. The browser viewport was returned to desktop. Nothing outside the scratchpad was deleted. `docs/seo-2026-09-19/OFFSITE-CHECKLIST.md`, `docs/LAUNCH-CHECKLIST.md`, `docs/to-questionnaire-matt.md`, `CONTEXT.md` and `README.md` were left alone for the session that owns them. CONTEXT.md was read once at the start of this run for the client facts trace and changed under us afterwards; the nine added lines are a build-state note for this round and do not bear on any claim in the trace above.

## Note on the rebase (0bab633 on main a0142af)

After the two verification passes below were run, Sidd pushed two commits to main (df41bff and a0142af) and this branch was regenerated on top of them: page bodies are his, byte for byte, and only the meta block and the hero poster markup differ (checked with `python3 tools/seo-check.py origin/main`, zero differences, zero issues). The build was rebuilt with and without Pillow and the two trees are identical. The About share image and its alt text follow his new photo; the About description and the Person node drop the 2009 settling claim per his correction in CONTEXT.md. Lighthouse and the screenshots were not re-run after the rebase; the stylesheet rules and head markup they measure are unchanged, and the Vercel build log for the branch deployment shows the production host read from the environment and nine pages built without error.

## Re-check on the final branch (seo/metadata-2026-09-19, 19138f1)

Independent re-check of branch `seo/metadata-2026-09-19` at `19138f1`, five commits on `main` at `218aa1a`, run in the worktree `/Users/main/MOSI/spontaneous-cafe-seo-pages`. This branch is narrower than the one checked above: the retreat-catering and FAQ body copy is gone, so every page body is byte-identical to main except the meta block and the hero poster markup. Two of the five items raised above are addressed in this branch: the Caveat preload is back in `src/layout.html`, and the Alignable URL is out of `sameAs` in `build.py` (the comment there now reads "sameAs deliberately empty... after Matt confirms each one is his"). Items 2, 3 and 4 from the prior round (the repeated retreat bullets, the half-empty retreat band, the two neutral-voice FAQ answers) no longer apply, because the copy they were about is not in this branch. Nothing was committed, pushed or deployed, and no file in the worktree was edited; `dist/` was rebuilt twice by the checks below and is gitignored.

### Matrix

| # | Check | Result | Evidence |
|---|---|---|---|
| 1a | `python3 build.py` succeeds and prints the host | Pass | `host: https://spontaneouscafe.com`, `built 9 pages` |
| 1b | Second build with Pillow blocked (`sys.modules['PIL']=None`) produces an identical tree | Pass | Normal build copied to scratch as `dist-normal`, Pillow-blocked build run in place, `diff -rq dist-normal dist` printed nothing, exit 0 |
| 2a | Three font preloads on `dist/index.html`, all three files exist | Pass | `lora-latin.woff2`, `caveat-latin.woff2`, `source-sans-3-latin.woff2` all present as `<link rel="preload" as="font">` and all three `.woff2` files exist in `dist/assets/fonts` (37,792 / 74,572 / 28,792 bytes) |
| 2b | `<picture class="hero__poster">` on the five hero pages, with a matching image preload | Pass | index, foraging, private-chef, catering, cooking-classes each carry the picture element and a `<link rel="preload" as="image">`; `imagesrcset` on the preload equals the webp `<source srcset>` as an exact string match on all five |
| 2c | robots meta carries `max-image-preview:large`, `twitter:image` present | Pass | Checked on all 8 indexable pages (index, about, catering, contact, cooking-classes, foraging, privacy, private-chef). Both present on every one. |
| 2d | `dist/404.html` has no JSON-LD | Pass | 0 `<script type="application/ld+json">` blocks |
| 2e | `dist/index.html` JSON-LD graph: LocalBusiness has `hasMap`, no `sameAs`, every `@id` resolves | Pass | Graph has 4 top-level nodes (WebSite, LocalBusiness, Person, WebPage). `hasMap` = `https://www.google.com/maps?cid=7343978535458024901`. `sameAs` key absent from the LocalBusiness node. 10 `@id` values defined in the graph, 0 referenced-but-undefined. |
| 3 | Page bodies equal main after stripping the meta block, `poster="..."` (main) and `<img class="hero__poster">` (HEAD) | Pass | 0 of 9 pages differ. The 5 hero pages (index, foraging, private-chef, catering, cooking-classes) each had exactly one `poster` attribute in main and one `hero__poster` img in HEAD, both stripped cleanly; about, contact, privacy and 404 had none of either and matched on the meta strip alone. |
| 4 | Lighthouse: branch CLS at or near 0, branch performance at or above main | Pass | See Lighthouse table. Branch CLS is 0.000 on both home and foraging. Branch performance is 94 vs main's 93 on home, 93 vs main's 89 on foraging. Neither branch page clears 0.01 CLS, so the shifting-element lookup this check calls for does not apply. |
| 5 | Screenshots: branch heroes match main at desktop and mobile | Pass | 8 inline views, home and foraging, desktop and mobile, branch and main. See Screenshots note below for what was seen and a tooling limitation on saving them to disk. |
| 6 | Both servers killed at the end | Pass | `lsof -ti tcp:8795` and `tcp:8796` empty after `kill`; `curl` to both returns no response (exit on connection refused) |

### Lighthouse

Mobile emulation, the default, confirmed via `configSettings.formFactor: "mobile"` in each report. Branch served from `dist` on port 8795, main built with `git archive main` into scratch and served on 8796. Lighthouse 13.5.0, one run per page.

| Run | Performance | Accessibility | Best practices | SEO | LCP | CLS | LCP element |
|---|---|---|---|---|---|---|---|
| Branch, home | 94 | 100 | 100 | 100 | 3.0 s | 0.000 | not reported |
| Branch, foraging | 93 | 100 | 100 | 100 | 3.2 s | 0.000 | not reported |
| Main, home | 93 | 100 | 100 | 100 | 3.2 s | 0.000 | not reported |
| Main, foraging | 89 | 100 | 100 | 100 | 3.5 s | 0.079 | not reported |

The `largest-contentful-paint-element` audit is absent from all four JSON reports, the same gap the prior round hit, so Lighthouse names no LCP element in this data either time. Main foraging's 0.079 CLS is inherited from main itself, outside this branch's diff, and sits in the same range the prior round measured for it (0.077 to 0.079 across runs). Both branch pages come back at 0.000, matching what restoring the Caveat preload was expected to do and confirming the fix from the wider-branch round holds on this narrower one.

### Screenshots

Captured with the Browser pane tool: `preview_start` by URL, `resize_window` for the mobile preset (375x812), `computer` screenshot, for branch (8795) and main (8796), home and foraging, at desktop and mobile. Eight captures, each viewed inline and compared by eye. This tool returns the image inline rather than to a file path, so, unlike the Lighthouse JSON and the two check scripts in this scratch folder, there are no PNGs on disk to cite as evidence for this check. A second attempt to also save on-disk copies through a headless "Chrome for Testing" binary (from the Puppeteer cache at `~/.cache/puppeteer`) was tried as a supplement: the foraging pages saved correctly on the first pass, but every attempt at the home page hung past a 15-second timeout, most likely because the autoplaying hero video never reaches headless Chrome's idle signal for the `--screenshot` flag. The foraging PNGs that did save were deleted during cleanup before this section was written, so nothing from that attempt survived either. The finding below rests on the inline views alone.

- Foraging, desktop and mobile: pixel-identical between branch and main. Same mushroom-basket photograph, same headline, same layout, same crop, at both sizes.
- Home, desktop: same photograph (the pan over the gas flame), same headline and layout on both builds, but the first pair of captures landed on different frames of the looping video, one darker and one mid-flame. A second branch capture a few seconds later landed on the same bright frame main showed, which points to video playback timing rather than a layout or asset difference. Both builds show a "Pause video" control in the same position, so the video is playing on both, not stalled on one.
- Home, mobile: same photograph, same frame this time, same headline and layout, no horizontal overflow on either build.

No broken images, no missing hero content and no layout difference traceable to this branch's changes turned up in any of the eight views. Desktop viewport was restored with `resize_window` preset `desktop` after the mobile captures.

### Verdict

All six checks pass: the build is deterministic with and without Pillow, the font and hero-image preloads point at real files and match each other, the JSON-LD graph on the home page resolves with `hasMap` present and `sameAs` gone, all nine page bodies are byte-identical to main outside the meta block and the hero poster markup, branch CLS is 0.000 on home and foraging against main's 0.000 and 0.079, branch performance (94, 93) is at or above main's (93, 89) on both pages, and the hero screenshots match main apart from video frame timing. Nothing found here blocks a deploy.

## Merge with b272f3e

Branch `seo/metadata-merge`, cut from `origin/main` (b4d9534, two commits past b272f3e: both change only the Vercel build command and one runbook line). Sidd's page bodies, analytics, preview mode, tests, Content Security Policy and Pillow pin are kept as written; the metadata, structured data, build, head and hosting changes from `seo/metadata-2026-09-19` are ported by hand on top.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | `python3 build.py` | Pass | `host: https://spontaneouscafe.com`, `built 9 pages`, both root icons copied, four hashed assets including `js/analytics.js` |
| 2 | `python3 tools/seo-check.py origin/main` | Pass | `ISSUES: none`, `missing internal targets: none`, `pages differing from origin/main beyond the meta block and hero markup: 0`, exit 0 |
| 3 | Pillow-free parity | Pass | `dist` copied aside, rebuilt with `sys.modules['PIL']=None`, `diff -rq` between the two trees printed nothing |
| 4 | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | Pass | Ran 5 tests, OK, no test file edited. The home page's first ld+json block is the LocalBusiness node itself, with `@id` and without `geo`, which is what `test_business_has_stable_identity_without_unverified_coordinates` reads. |
| 5 | `node tests/analytics.test.cjs` | Pass | 6 tests, 6 pass, 0 fail |
| 6 | `node tests/layout.cjs`, `node tests/browser.cjs` | Not run | `Error: Cannot find module 'playwright'`. There is no `package.json` in the repo and nothing was installed for this merge. |
| 7 | Every ld+json block in `dist` parses, every `@id` reference resolves on its page | Pass | 8 pages, one block each, 0 dangling references. Home, contact and privacy top out at LocalBusiness (10 defined ids, 1 reference); about at Person; the four service pages at Service (11 defined ids, 6 area references plus 1 provider reference). |
| 8 | No Review, AggregateRating or FAQPage anywhere; nothing on the 404 | Pass | 0 occurrences of all three types across `dist`; `dist/404.html` carries 0 ld+json blocks and no canonical or og:url |
| 9 | Head tags on the built home page | Pass | Three font preloads (lora, caveat, source-sans-3), three icon links (`/favicon.ico` with sizes, the svg, `/apple-touch-icon.png`), the cookie notice, the analytics script tag, `robots` with `max-image-preview:large`, `twitter:image`, and the hero image preload |
| 10 | `dist/robots.txt` and the root icons | Pass | `Disallow: /api/` present under the comment line; `dist/favicon.ico` (885 bytes) and `dist/apple-touch-icon.png` (5,323 bytes) both exist |
| 11 | No em dash (U+2014) in anything written for this merge | Pass | The two hits in the tree (a sample testimonial in `src/pages/index.html` and two in `src/assets/js/site.js`) are Sidd's and predate this branch |

`vercel.json` was not validated against `https://openapi.vercel.sh/vercel.json`: `jsonschema` is not importable in this environment and this run is offline. Structure checked by hand instead, and the file parses as JSON: `$schema`, `buildCommand`, `outputDirectory`, `cleanUrls`, `trailingSlash`, `redirects` (three, each with source, destination and permanent, the host rule carrying `has`), `headers` (four, each with source and a headers array, two carrying `has`).

### Descriptions against Sidd's bodies

- `/privacy/`: the description reads "What this site collects, which is almost nothing." Sidd's body now describes consent-gated Google Analytics through Tag Manager, what Google receives (pages, browser, device, referrers, IP address), an analytics cookie and a six-month preference. The page's own lede, which is his and unchanged, says "How inquiries and basic website information are handled." Left as written, flagged for a decision.
- `/about/`: the description names Peru, Thailand and India. The body names none of the three; since the 2026-09-11 rewrite it says "Retreat kitchens on four continents" with the journey rows labelled North America, South America, Asia and Australia. The three countries are CONTEXT.md facts and still carry an open CONFIRM tag. Left as written, flagged.
- `/cooking-classes/`: the description says Matt "taught at Living Light in Fort Bragg". True on the About page and in CONTEXT.md, but the cooking classes body never says it. Left as written, flagged.
- The other five descriptions check out against the bodies: the tier prices on `/contact/` ("3 hours $300 · 6 hours $500 · 12 hours $1,000"), "3, 6 or 12 hours" and "From $300" on `/foraging/`, "One person up to twelve" and the Albion kitchen on `/private-chef/`, "20 to 350" and the service styles on `/catering/`, "no recipe" and "$300" on `/cooking-classes/`, the four services and "from $300" on the home page.
