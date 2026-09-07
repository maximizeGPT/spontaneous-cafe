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
- Prices: experiences $500 full day, $250 half day. Private chef: from $500 per day, ingredients billed at cost (CONFIRM WITH MATT). Catering: quoted per event (CONFIRM WITH MATT).
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
- Prices shown on the site.
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
