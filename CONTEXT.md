# Spontaneous Cafe website. Context

Engagement: MOSI Consulting Inc for Chef Matt Samuelson, Mendocino, CA. Proposal doc Phase 1 item 1 only (website refresh). Decisions below were settled in a grill session on 2026-09-06.

## Client facts
- Business: The Spontaneous Cafe, since 2009. Personal chef, catering, foraging excursions, cooking classes, forest bathing, farm and ranch tours, interactive dinner parties.
- Service priority: 1 Foraging, 2 Private chef, 3 Catering and events, 4 Cooking classes.
- Owner: Matthew "Chef Matt" Samuelson. (707) 972-6647, chefmattsamuelson@gmail.com.
- Teaching history: Living Light Culinary Arts Institute (Fort Bragg) and Esalen. Confirmed by Mohammed 2026-09-06. Leave slots for more.
- Sourcing: small local farm stands, trust-based payment, often the only people there. Farmers markets. Salt harvested from the beach. Huckleberries. Mushrooms.
- Customers: San Francisco weekenders, Mendocino tourists, referrals. Demand for private-event cheffing.
- Stories: free community weekend cheffing for Mendocino; a tourist couple's foraging day (salt harvest, mushrooms, farm stands) ending in a multi-course dinner in their rental; a couple who foraged as part of their engagement trip.
- Guest quote (paraphrased by Mohammed): freshest, most nature-to-table meal I have ever had; learned more about California nature and what is edible than expected; Matt is an expert with worldwide practical and theoretical foraging experience.
- Prices (changed by Mohammed 2026-09-07, supersedes the earlier $500/$250): three tiers by hours, for any service. 3 hours $300. 6 hours $500. 12 hours $1,000. Ingredients billed at cost on chef and class days. Catering beyond a day is quoted per event.
- Area: greater Mendocino. All seasons, experiences change with weather and what is growing. No group cap stated.
- Words for the brand: whole foods, farm-to-table, quality, local, organic, resourceful.

## Current site (2026-09-06)
- GoDaddy Website Builder, one page, no nav, no form, no analytics, no meta description. Cinzel headings, Source Sans Pro body, slate #828b99 ground.
- Photos on it are stock or third-party (forest shot is rights-marked to "cincas", 2017). None show Matt or his food.
- Domain spontaneouscafe.com registered at GoDaddy 2016, renews 2027-05-16. DNS stays at GoDaddy and can point at Vercel.

## Decisions
- Rebuild as plain static HTML, CSS and JS. No framework. Python build script assembles pages from a layout. Deploys to Vercel from this repo; portable to any host.
- Direction C "Cottage Kitchen" from docs/directions-board.html. Palette: oat linen #F1E9DA, logo red #8F1F1F, logo green #2B3A2C, sage #9AA88A, butter #E8B98A. Type: Lora display, Caveat accent (one word per section, max), Source Sans 3 body.
- Logo redrawn as SVG from the original JPG, kept as the wordmark.
- Nav: Foraging, Private Chef, Catering & Events, Cooking Classes, About Matt, Contact button. Forest bathing, farm tours, dinner parties are sections inside Foraging and Classes.
- Five hero video loops. Home: hands at a pan over flame. Foraging: moss and mushroom macro. Private Chef: plating at a home table. Catering: long table being set. Classes: knife on board. Stock loops first; AI-generated loops (Minimax Hailuo image-to-video, Kling via fal.ai) after design approval, ambience only, never a specific dish.
- Copy in first person (Matt). Reversible.
- Four seasonal sample menus drafted from Mendocino produce, labelled as samples that change with the season.
- Prices shown on the site as the three hour tiers.
- Placeholder photos with a swap list in docs/SWAP-LIST.md. Trust and safety copy skipped for the demo.
- Full name "Matt Samuelson" in page titles. "Chef Matt Mendocino" in search returns Matthew Kammerer of Harbor House.
- Skills: ui-ux-pro-max only (installed at .claude/skills/ui-ux-pro-max).

## Not in scope now
SEO beyond page basics, Google Business Profile, review link, contact form backend, analytics. Proposal items 2 to 6.

## Build state (2026-09-07)
- Eight pages built and reviewed at desktop and 375px: home, foraging, private-chef, catering, cooking-classes, about, contact, privacy. `python3 build.py` writes dist/, preview with `python3 -m http.server 8787 -d dist`.
- Placeholder media in place: 14 photos (Unsplash) and 5 loops (Mixkit), all trimmed to 8 s. Manifest in src/assets/MANIFEST.md. Swap plan in docs/SWAP-LIST.md.
- 34 `<!-- CONFIRM -->` tags in src/pages mark assumptions for Matt. Two prices carry a visible "confirm with Matt" chip.
- 2026-09-07 later: Mohammed approved. Committed. Deployed to https://spontaneous-cafe.vercel.app (Vercel project spontaneous-cafe, team mohsprojects). Formspree form maeypdpl wired with AJAX submit and plain-POST fallback. AI loops generated on fal.ai Hailuo 02 from the placeholder photos (see README). Prose anti-slop pass run over every page.
- Still open: DNS switch of spontaneouscafe.com to Vercel (needs Matt), Matt's own photos and the 34 CONFIRM answers, privacy effective date.

## Google Business Profile (created by Mohammed 2026-09-07)
- Public Maps link: https://www.google.com/maps?cid=7343978535458024901 (name "Spontaneous Cafe"). Place ID not yet extracted; the review link comes from the GBP dashboard "Ask for reviews" once verified.

## Voice change (2026-09-07)
- Mohammed: first person throughout is too much, and sections that echo the interview answers verbatim ("Six words I actually mean") read as forced.
- Decision (docs/REWRITE-BRIEF.md): brand voice in third person on Home and service pages, Matt's first person only on About, in FAQ answers and in at most two short asides per page; CTAs address the reader. "Six words" section deleted. Register research was started but the rewrite went ahead on common sense, as Mohammed allowed.

## Audit (2026-09-07 to 08)
- Technical audit workflow: 7 dimensions, 75 agents, 68 confirmed findings (2 blockers, 21 major, 45 minor). Fixes landed: self-hosted fonts, hashed assets, security headers and CSP, 404, responsive images via build.py, contrast and focus fixes, mobile overflow, inert nav drawer, hero pause control, video preload=none with 720 variants, notify function hardening. Page-level fixes ride with the rewrite. Round two (design, copy, IA, conversion) runs after the rewrite.
- Real photo of Matt received 2026-09-07 (Drive, "Matt Cooking.png"): src/assets/img/matt.jpg (portrait), matt-kitchen.jpg, matt-square.jpg.

## Round 3 facts and rules (Mohammed, 2026-09-08). These are corrections; earlier lines that conflict are wrong.
- Matt forages mushrooms, berries, greens and salt. He does not hunt, fish or butcher. Meat and fish are bought. No whole-animal, nose-to-tail, "line-caught" or hunting lines anywhere.
- The menu is agreed with the guest in advance from what the farms, the market and the forest have that week. "Written the night before, sometimes the morning of" was invented and is not accurate.
- No Caveat accent word in headings. Caveat removed from the site.
- Tagline is "Local · Organic · Wild". Seasonal is not something to flaunt.
- Phone and email appear in the footer and on the Contact page only. CTA bands carry the button alone.
- No figure captions describing images.
- Tone: plainer. No count-plus-twist headings ("Four things, and none of them is a recipe"). Private chef page is prose, not a step list.
- Review markup (confirm chips, placeholder badges) is stripped from production builds; `REVIEW=1 python3 build.py` keeps it.

## Build state (2026-09-08)
- Live at https://spontaneous-cafe.vercel.app after rounds 2 and 3. Two audit workflows run (docs/AUDIT-1-FINDINGS.md technical, docs/AUDIT-2-FINDINGS.md design/copy/IA/conversion), fixes applied per docs/FIX-BRIEF-2.md including Mohammed's round-3 corrections.
- Questionnaire for Matt: docs/to-questionnaire-matt.md, Google Doc "Spontaneous Cafe website: questions for Matt" (30 questions). Earlier docs renamed "superseded".
- Still open: DNS switch (Matt), Matt's photos and answers, Twilio or Telegram credentials for /api/notify, the copy-register research agent never returned (rewrite proceeded on the brief).

## Round 4 (2026-09-08): block titles and ledes
- Mohammed: every remaining complaint was a section title, eyebrow or lede. Rules in docs/FIX-BRIEF-3.md. Caveat accent restored, on the load-bearing word pair of hero h1 and CTA h2 only. Cite lines carry a leading dash.

## Client facts added 2026-09-09 (from Mohammed's revision brief)
- Career: chef at yoga retreats in Peru; cooked in Thailand and India (other countries only if Matt confirms). In LA, private chef for several celebrities (no names without names and permission). Instructor at Living Light Culinary Arts Institute in Fort Bragg. Moved up the California coast over about thirty years and settled in Mendocino in 2009 (use 2009 everywhere; "2008" is retired). In Mendocino he formally studied nature and foraging; that training is the through-line that turned cooking into The Spontaneous Cafe.
- Private chef dinners happen at the guest's home or rental, or at Matt's home kitchen in Albion, CA (for guests who do not want to host or whose rental kitchen is limited).
- Group size for private dinners: one person (solo diners welcome) up to twelve; larger groups inquire directly.
- Services combine into one booking (foraging morning then dinner; class that becomes the meal; retreat foraging walk then catered dinner; multi-day stay with a different service each day).
- Home page shows pricing as one line, "Starting at $300"; full tiers stay on service pages and Contact.
