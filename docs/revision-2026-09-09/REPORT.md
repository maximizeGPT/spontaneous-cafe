# Spontaneous Cafe revisions, 2026-09-09

Revised copy section by section with removal notes and guessed facts, one part per page. Compiled from the four agent reports.

---

# Home, revised copy (2026-09-09)

Files owned and changed: `src/pages/index.html`, `src/layout.html`. Brief sections 1 and 2, plus the "since 2009" rule.

---

## Meta description

> Chef Matt Samuelson forages, shops and cooks on the Mendocino coast. Private dinners, catering, foraging days and cooking classes.

130 characters. Removed: "from $300". Why: pricing comes off Home except the one Services line; the tiers live on the service pages and Contact.

---

## Hero

Eyebrow: **Mendocino, California · since 2009**
H1: **Wild food, _cooked_ where you're _staying_.** (unchanged, hand accent on the load-bearing pair)
Lede: **Chef Matt Samuelson forages, shops and cooks anywhere in the greater Mendocino area, in every season.**
Buttons: Plan a dinner / Go foraging (unchanged)
Note under the buttons: **Any service · 3, 6 or 12 hours** → `#services`

Removed: the second "since 2009" from the lede, the four-service list from the lede, and "From $300" from the note. Why: the eyebrow is the one "since 2009" on the page, the Services h2 is the one place the four services are listed, and the price line under the buttons was the first of five prices on the page. The note keeps its shape and its link so Home matches the service-page heroes; the hours are structure, not a price. New lede fact: the service area and the year-round point, neither of which appears elsewhere on Home.

---

## Services

Eyebrow: **Services**
H2: **Foraging days, private dinners, catering and classes**
Line under it: **Starting at $300.** (`p.small`, matching the price sub-line on the service pages)

Cards, meta row now carries the link text alone:

| Card | Copy | Link |
| --- | --- | --- |
| Foraging excursions | A guided walk on the shore, in the forest and at farm stands, gathering salt, mushrooms and berries with Matt. | See the day |
| Private chef | A multi-course dinner cooked and served for one to twelve people, in your rental, your house, or Matt's home kitchen in Albion. | How it works |
| Catering & events | Weddings, retreats and family weekends, catered on site or off, quoted per event above about twelve guests or with rentals. | Plan an event |
| Cooking classes | Knife skills, kitchen efficiency and cooking with whatever's already in the fridge, taught at Living Light and Esalen. | Book a class |

Removed: the three-tier ladder ("3 hours $300. 6 hours $500. 12 hours $1,000. Any service.") and the four "From $300" spans. Why: brief section 1, one price line on Home. The Private Chef card lost "from what Matt found and bought that morning" because that is the morning-forage-then-dinner story the Example day already tells; it now says what the service is (group size 1 to 12, and the three places it can happen, including the Albion kitchen).

---

## Build your own day (new section, after the services grid)

Eyebrow: **Build your own day**
H2: **Pick one, or stack them**
Line: **Any of the four services can go into one booking, on one day or across a stay.**

`.details` list, four two-line entries:

- **Foraging morning, dinner that night** — The morning out for salt, mushrooms and farm stands, then Matt cooks what came back.
- **A class that becomes the meal** — Your group cooks alongside Matt, then everyone sits down and eats what they made.
- **Retreat walk, then a catered dinner** — A foraging walk for the whole group in the day, a catered table at the end of it.
- **A different service each day** — Multi-day stays book one service a day across a weekend or a week.

Link-arrow: **Tell Matt what to combine** → `/contact/`

Nothing removed; this is brief section 2. Placed directly after the grid so the combining idea lands while the four services are still on screen. Background is `--paper`, which pushed the Example day section to plain linen and the About block off `--paper`, keeping the linen / paper alternation down the page.

---

## An example foraging day

Eyebrow **Foraging**, H2 **An example foraging day**, four timeline steps unchanged.
Link-arrow: **The twelve-hour foraging day** → `/foraging/#prices`

Removed: "$1,000 for the group" from the link. Why: brief section 1, the last of the four price mentions outside the Services line. The link still lands on the foraging prices, where the number lives.

---

## Where the food comes from

H2 unchanged. Body cut to two sentences:

> Matt has bought from the same small farms, honor-box stands and market growers for years. The salt, mushrooms, berries and greens he gathers himself.

Photo strip unchanged (five images). Removed: the sourcing paragraph, which re-explained what the Example day timeline shows and what About and Private Chef both say at length, and the "More about how Matt cooks" link-arrow, because the About block lower on the page already links to `/about/`. Also dropped the phrase "whatever the farms, the market and the forest have that week", which is on Private Chef too (brief section 4).

---

## Sample menus

Eyebrow: **Sample menus**
H2: **Six courses, by season**
Teaser: **The menu is agreed with you before the day, from what is actually available that week. Spring, summer, autumn and winter samples sit on the private chef page.**
Link-arrow: **See the seasonal sample menus** → `/private-chef/`

Removed: the entire six-course late-summer menu card (30 lines). Why: the same six courses tell the forage-then-dinner story a fourth time, and Private Chef carries four seasonal menus in a tab set. The link goes to `/private-chef/` rather than an anchor because that page is owned by another agent this round and has no `id` on its Sample menus section. **If that agent adds `id="menus"` there, change this href to `/private-chef/#menus`.**

---

## Testimonial

Cut entirely. The `.section--green` quote band, its blockquote and its cite are gone from Home. Why: brief section 1, the same guest quote runs on Private Chef and a near variant on Foraging. Its `<!-- CONFIRM -->` (quote is Mohammed's paraphrase, wording and attribution permission unconfirmed) was rewritten in place as a standing note in `index.html`, because neither Private Chef nor Foraging carries that flag and it would otherwise have left the site.

---

## About Matt

Photo `matt-square.jpg` kept, still beside the text.
H2: **About Matt**

> Matt cooked at yoga retreats in Peru, in Thailand and India, and as a private chef in Los Angeles.
>
> He moved up the California coast over about thirty years and settled in Mendocino, where he studied nature and foraging formally. The Spontaneous Cafe started there.

Link-arrow: **Read the rest** → `/about/`

Removed: the three stat rows (On the coast / Foraging / Teaching) and the sentence about Living Light and Esalen. Why: all four restated the hero, the Cooking classes card and the Foraging page. Replaced with the career narrative from brief section 5, compressed to the two sentences a home page can carry. No year in this block: the hero eyebrow is the page's one "since 2009", and the full chronology belongs on About. No celebrity names, per the brief.

---

## CTA

Unchanged. H2 keeps the hand accent on `date` / `coming`.

---

## Footer (`src/layout.html`)

> Cooking, foraging and teaching on the Mendocino coast.

Removed: "since 2009". Why: the count across `index.html` and `layout.html` had to be one, and the footer is site-wide, so keeping it there would have given Catering, Cooking Classes and Private Chef two mentions each on top of their hero eyebrows. Home now carries it once, in the hero eyebrow.

Side effect worth knowing: this dropped one "since 2009" from every page. Built counts now: Home 1, Private Chef 1, About 0, Foraging 0, Contact 0, Catering 2, Cooking Classes 2. **Catering and Cooking Classes still say it twice** (hero eyebrow plus body copy); those files belong to the other agents this round.

---

## Guessed facts

Everything below is tagged `<!-- CONFIRM: ... -->` in `src/pages/index.html`.

1. **The four combinations in "Build your own day"** come from Mohammed's revision brief, not from Matt directly. Matt to confirm he actually books all four shapes, particularly the multi-day one-service-a-day stay.
2. **Matt's career order and places** (Peru yoga retreats, Thailand, India, private chef in Los Angeles, up the coast over about thirty years, formal foraging study in Mendocino). Same source. Matt to confirm the sequence and whether other countries belong in the list. Celebrity clients are deliberately absent, pending names and permission.
3. **Private chef group size, one to twelve.** From the new client facts; it now appears on the Home card as well as the Private Chef page, so the two must stay in step.
4. **Matt's home kitchen in Albion, CA** as a place a dinner can happen. New client fact, first appearance on Home. Matt to confirm it should be advertised publicly on the home page rather than only on Private Chef.
5. **"honor-box stands"** in "Where the food comes from" compresses the existing unstaffed-farm-stand fact already on Foraging and About. No new claim, but the shorthand is mine.

Seven `<!-- CONFIRM -->` comments now sit in `src/pages/index.html`; the build strips all of them from `dist/` (production and `REVIEW=1` alike).

Carried over unchanged from the previous build: the Example day CONFIRM (the four steps blend two guests' days, order unconfirmed), the `matt-square.jpg` alt-text CONFIRM (kitchen location), and the guest-quote CONFIRM described under Testimonial.

---

## Verification

`python3 build.py` succeeded, 9 pages. Greps over `src/pages/index.html`:

| Pattern | Count | Expected |
| --- | --- | --- |
| `$300` | 1 (the "Starting at $300." line) | 1 |
| `$1,000` | 0 | 0 |
| `From $` | 0 | 0 |
| `since 2009` across index + layout | 1 | 1 |
| em dash outside a `<cite>` | 0 | 0 |
| `not just` | 0 | 0 |
| ` rather than ` | 0 | 0 |

Rendered check at 1280px and 375px: eight sections in linen / paper / linen / paper / deep / linen / green order, the `.details` grid falls from two columns to one on mobile, `.service__meta` reads correctly with the price span gone, no horizontal overflow at 375px, no console errors.

---

# About page, revised 2026-09-09

Brief section 5. Top half replaced with a first-person chronological story under plain block titles. 345 words across the four story sections (336 in the body paragraphs). 2009 everywhere, "2008" retired. Seven `<!-- CONFIRM -->` tags.

---

## Meta

> title: About Matt | The Spontaneous Cafe, Mendocino
> description: Matt Samuelson cooked at yoga retreats in Peru, in Thailand and India, and privately in Los Angeles. He settled in Mendocino in 2009 and studied foraging there.

Removed: "foraged for thirty years and taught cooking for twenty-three. Since 2008": the description carried the retired 2008 date and the same two stats as the hero and the Home "About Matt" block.

---

## Hero (kept, one line changed)

> **About Matt**
> # I'm Matt. I forage and I cook.
> Peru, Thailand, India and Los Angeles, then thirty years up the California coast to Mendocino.
> [Plan a day or a dinner]

Removed: "Thirty years in the woods, twenty-three teaching people to cook, and since 2008 all of it on the North Coast." It repeated the Home stats block and carried 2008. The new lede adds four facts the h1 does not and sets up the story that follows. Media, h1, the Caveat pair and the button are untouched.

---

## Peru, Thailand, India

> I have cooked for a living in a few countries. In Peru I was the chef at yoga retreats, three meals a day for a house full of people I had not met, most of the table on some version of no gluten, no dairy or no meat.
>
> Thailand and India came after that. Every one of those kitchens ran off the local market, so the first thing I did in a new place was go and look at what was for sale.

Figure: plate.jpg (kept, moved up from the old "How I cook" section).
Removed: the whole "The short version / How Matt cooks" block, which restated the Home hero (thirty years foraging, twenty-three teaching, Living Light, Esalen) before the story could start.

---

## Los Angeles, then north

> In Los Angeles I cooked privately for several celebrity clients. I am not going to name them on a website.
>
> After that I kept moving north, in stages, over about thirty years. Part of that stretch I was an instructor at Living Light Culinary Arts Institute in Fort Bragg, up the coast from where I live now.

Removed: nothing existed here before. This section resolves the brief's "culinary school in Mendocino" against the site's existing "Living Light in Fort Bragg" by naming the school once, in Fort Bragg, inside the chronology.

---

## Mendocino

> I settled here in 2009 and started calling the work The Spontaneous Cafe. Foraging is what changed in Mendocino. I had picked things for years before I arrived, and here I studied it formally, the plants, the mushrooms and the shore, with as much time on the reading as on the walking. Both halves matter when you are looking at two mushrooms that are easy to mistake for each other.
>
> The cooking runs off that. I buy from a handful of small farms and the farmers market, meat and fish included, and I cook whole foods with the vegetables used end to end. The salt, the mushrooms, the greens and the berries I go and get. A chef who arrives with a shopping list cannot put that part on the table.

Figures: the five-image sourcing photo grid (kept, moved here).
Removed: both long sourcing paragraphs (honor boxes, "nobody staffs", citrus from inland, chanterelles and boletes by season) and the "Whole foods, farm to table" section. The Foraging page already covers unstaffed stands with the cash box, the seasonal baskets and the salt, and Private Chef already covers whole foods, local and organic. What survives is one paragraph, kept because it says the thing no service page says: he buys the meat and fish and gathers the wild part himself. "Quality is the part I will argue about" and the Noyo fish line went with the cut section; they are good lines but they duplicated the Private Chef menu section.

---

## Teaching

> I have taught cooking for twenty-three years. At Living Light it was raw and plant-based technique, knife work, and how to run a prep list so the day does not run you. At Esalen, down the coast in Big Sur, it was cooking for a house full of people and teaching while doing it.
>
> One weekend I cooked for the town of Mendocino for free.

Figure: group-cooking.jpg (kept).
Removed: "Most weeks the guests are people who drove up from San Francisco, or friends of theirs who heard about the food": the Private Chef page says the same thing under "Who books a private chef". The Living Light sentence lost its second naming of the school (it is now in the story above) and became what he taught there. Both existing CONFIRM comments kept.

---

## CTA (unchanged)

> ## Come out for a day, or stay in for dinner.
> Tell Matt when you're here and how many of you there are. You'll hear back with what's growing.
> [Send an inquiry]

---

## Guessed facts (7 CONFIRM tags in the HTML; items 3 and 8 ride inside the tag above them)

1. **Peru**: that the retreat cooking was three meals a day for a full house with gluten, dairy and meat restrictions across the table, and which years it ran. The brief gives "chef at yoga retreats in Peru" and nothing more.
2. **Thailand and India**: the page says only that they came after Peru. Whether they were retreats, restaurants or private houses, how long, and whether other countries belong in the list, is unknown.
3. **"Every one of those kitchens ran off the local market"**: my inference from the way he works now, not something Matt said about Peru, Thailand or India.
4. **The LA clients**: described as "several celebrity clients" with no names, per the brief. Needs Matt's yes to the wording, and names plus permission if he wants any.
5. **Living Light years and content**: "part of that stretch" is deliberately vague because no dates exist. The raw and plant-based technique, knife work and prep-list line is carried over from the previous page and has never been confirmed.
6. **The formal foraging study**: the single most important gap. "Studied it formally, the plants, the mushrooms and the shore" covers a course, a mentor, a certification or years of reading equally well, and the brief makes this the through-line, so it needs a real answer.
7. **The free community weekend**: existing CONFIRM, still unanswered: which year, and whether it was the town of Mendocino or a named event.
8. **Fort Bragg "up the coast from where I live now"**: geography stated loosely on purpose; no distance or drive time invented.

## Checks run

- `python3 build.py` clean, 9 pages.
- `grep "2008"` src and dist: zero.
- `grep "—"` (em dash) outside cite: zero. No `<cite>` on this page.
- `grep "not just"`, `grep " rather than "`: zero.
- "farms, the market and the forest": zero on this page.
- Caveat `.hand` appears only in the hero h1 and the CTA h2, on both words of each pair.
- No figcaptions, no phone or email on the page.

## Questionnaire

`docs/to-questionnaire-matt.md` gained section "8. Your story" (seven questions, existing h3 + italic "On the page" + `>` stub format): other countries, what Thailand and India were, the LA clients and permission, years for Peru / LA / Living Light, what the Mendocino foraging study was, the Albion home kitchen wording, and the one-to-twelve group range. Section 6 already asks about other teaching, the guest quotes and the free town weekend, so those were not repeated.

---

# Private Chef, revised copy (2026-09-09)

Brief sections 2, 3 and 4. Source file: `src/pages/private-chef.html`. Testimonial kept (Home is dropping its copy of it).

## Meta description

> Chef Matt Samuelson cooks multi-course dinners in Mendocino homes and rentals, or at his own kitchen in Albion. Three, six or twelve hours, from $300.

Removed "ingredients billed at cost" to make room for Albion. The cost line is still on the page twice, in the Prices head and in the FAQ.

## Hero lede

> Chef Matt Samuelson forages and shops in the morning, cooks in the afternoon, serves the courses, and washes up before he goes.

Removed "on your stove", which contradicted the new Albion option.

## How a dinner works

> Dinner happens at your home or your rental, or at Chef Matt's home kitchen in Albion, CA. Guests who would rather not host, or whose rental kitchen is short on burners and counter space, come to him instead.
>
> Matt shops the farm stands and the market, forages what the woods have that week, then cooks that afternoon with his own knives and pans. Courses come out one at a time straight to the table, and he clears the kitchen before he leaves.
>
> - Date, head count, address and dietary needs collected in advance
> - Shopping and foraging done before he arrives
> - Courses cooked, plated and served in your kitchen
> - Kitchen cleaned and leftovers left in your own containers

Added the location paragraph as the first thing under the heading, and removed "in your kitchen" from the second paragraph because the kitchen may be his.

## Who books a private chef

> Most nights are for couples and families in vacation rentals, from a table for two up to twelve. Weekend groups up from San Francisco book the night everyone is finally under one roof, and birthdays and anniversaries move a restaurant reservation into the kitchen instead. A steady share of the work comes back through guests who passed the number on.
>
> A dinner can start with a foraging morning the same day, and the four services combine into one booking. [Build your own day](/#build).

Removed "to a full house with three generations in it", which contradicts the twelve cap. Added the combine line (brief section 2) at the end of the opening section.

## How the menu is set

> The menu is set in advance, from what is at its best the week you are here. Whole foods, local, organic where he can get it. Dietary needs and allergies go into the plan at the start: vegan, gluten free, no dairy, a nine year old who eats nothing green. All of it is workable with notice.

Removed "from what the farms, the market and the forest have that week" (brief section 4). That triad stays once on this page, in "How a dinner works", and once on Foraging.

## Good to know

> **Where** Your vacation rental, second home or full-time home in the greater Mendocino area, or Chef Matt's home kitchen in Albion, CA for guests who would rather not host. Further out, ask.
>
> **Group size** One person up to twelve, and solo diners are welcome. Above twelve, inquire with Matt directly. A table close to twelve usually means he brings a second pair of hands.

Removed "Vacation rentals, second homes and full-time homes" as a flat list in favour of second person, and removed "Two people up to a full house, with no fixed cap. Past about twelve he brings a second pair of hands." The second-pair-of-hands fact is reconciled against the new cap and still carries a CONFIRM. The other four entries (Kitchen needs, Dietary needs, Timing, What he brings) are unchanged.

## Questions people ask

> **How many people will you cook for?**
> Anything from one person up to twelve. Solo diners are welcome, and plenty of my dinners are for two, which three hours covers as a two-course dinner. If there are more than twelve of you, write to me directly and we will work out what the night needs.

Replaced "Will you cook for only two people?" entirely. The old answer's useful half (three hours covers a two-course dinner for a small table) is folded into the new one. The other three questions are unchanged.

## Unchanged

Prices (three tiers, CONFIRM intact), the four seasonal sample menus, the testimonial and cite, the CTA.

## Guessed facts

All new CONFIRM tags on this page:

1. `<!-- CONFIRM: how many the Albion kitchen seats, and whether an Albion dinner is priced the same as a dinner at the guest's address -->` in "How a dinner works". Neither number is in the brief.
2. `<!-- CONFIRM: the headcount at which Matt brings help, now that twelve is the cap -->` in Good to know / Group size. Rewritten from the existing CONFIRM, which said "about twelve" back when there was no cap.

Wording I supplied that Matt should sanity-check, without a tag because it paraphrases the brief: "short on burners and counter space" as the description of a limited rental kitchen, and "write to me directly" as the route for groups above twelve (the brief says inquire with Matt directly, it does not say whether those become catering quotes).

Existing CONFIRMs kept: ingredients at cost, booking lead time, service staffing.

---

# Foraging, Catering, Cooking Classes and Contact, revised copy (2026-09-09)

Brief sections 2 and 4. Private Chef has its own file. Only the sections that changed are below; everything else on these four pages is untouched.

## Foraging, "What a foraging day includes"

New last line of the section, under the three-item list:

> The four services combine into one booking, most often a foraging morning and a private dinner that night. [Build your own day](/#build).

Nothing removed. The pairing named is the one the brief asks for on this page.

## Catering, "What Matt caters"

New line under the four-item list, above the existing "Tell Matt about your event" link:

> A retreat or a wedding party can start with a foraging walk for the group and end at the catered table. [Build your own day](/#build).

Nothing removed.

## Catering, "How an event comes together", step 3

> **He sources it** Sourcing runs the week of the event: a ranch inland, the boats at Noyo, and whatever the woods have. Final counts lock a few days before.

Removed "Farm stands, the market" from the front of the list (brief section 4). The ranch and the boats are the parts of this list that are specific to catering, and neither appears on another page. The step's CONFIRM on the final-count deadline is intact.

## Cooking Classes, "What a class covers"

New line under the three-item list:

> A class can end as the dinner the group sits down to, and the four services combine into one booking. [Build your own day](/#build).

Nothing removed.

## Contact

No change. The Rates block already reads "3 hours $300 · 6 hours $500 · 12 hours $1,000, any service. Ingredients at cost. Weddings and larger events are quoted", which matches the brief (full tiers stay on Contact), and the form's "How long" select carries the same three prices. No price line on this page contradicts anything.

## Consistency check across the five pages I own

- "2008" appears zero times. It was only ever on About, which another agent owns.
- The "farms, the market and the forest" triad now appears on two of my five pages: Foraging ("on the shore, in the forest and at farm stands", which is the mandated FIX-BRIEF-3 service description) and Private Chef ("the farm stands and the market, forages what the woods have that week", in How a dinner works). It was cut from Private Chef's menu section and from Catering's sourcing step. Cooking Classes says "the market or the forest" about where a class starts, which names no farms and is about the class route rather than sourcing, so I left it. Contact has none.
- No em dashes outside `<cite>`, no "not just", no " rather than ".

## Guessed facts

None. Every new sentence on these four pages restates the combine-into-one-booking fact and the per-page pairing from the brief, so no new CONFIRM tags were needed. All existing CONFIRMs are intact: Foraging 5, Catering 14, Cooking Classes 4, Contact 1.

---

# Overlap fixes, 2026-09-09 (fresh-eyes editor pass)

Six items, four files. No new client facts. Every existing `<!-- CONFIRM -->` kept; the one on Home's sourcing block was rewritten to describe the cut instead of the deleted phrase.

## 1. Home, missing anchor
- Before: `<section class="section section--paper">` for "Build your own day". The `/#build` links on Foraging, Private chef, Catering and Classes landed at the top of Home.
- After: `<section class="section section--paper" id="build">`. Verified in `dist/index.html`.

## 2. Home, the forage-then-dinner story told twice
- Before (list): "Foraging morning, dinner that night / The morning out for salt, mushrooms and farm stands, then Matt cooks what came back", plus three more narrated lines.
- After: four pairings that name the combination and add a booking fact. "Foraging morning + private dinner / Book both and Matt plans the day around the tide." "Cooking class + dinner for the group / One booking, in the kitchen where you are staying." "Retreat walk + catering / Quoted per event above about twelve guests." "A different service each day / Multi-day stays book one service a day."
- Before (timeline step 1): "...sea salt off the rocks to use at dinner that night."
- After: "...sea salt off the rocks to use at the table." The timeline keeps the story; the list no longer competes with it.

## 3. Home, About block restated About
- Before: two paragraphs carrying Peru/Thailand/India/LA, the thirty-year move, Mendocino, the formal foraging study and the Spontaneous Cafe origin.
- After, two sentences: "Matt cooked at yoga retreats in Peru, in Thailand and India, and as a private chef in Los Angeles. He studied nature and foraging formally later, in Mendocino, and the About page tells that part." The thirty years, 2009 and the Spontaneous Cafe origin now live only on About.

## 4. Home, "Where the food comes from"
- Before: h2 plus two sentences on farms, honor-box stands, market growers and what Matt gathers himself, then the photo strip.
- After: h2, one `link-arrow` "How Matt sources" to `/about/`, photo strip unchanged. Sourcing is stated once on Foraging and once on About.

## 5. Foraging, the shore / forest / farm-stands triple four times
- Before (hero lede): "A day with him runs the shore at low tide, the forest under the redwoods and farm stands along the way, ending at a table."
- After: "A day with him gathers salt, mushrooms, greens and berries, and the twelve-hour day ends at a table." Names the harvest instead of the three locations.
- Before (description): "A guided walk on the shore, in the forest and at farm stands around Mendocino, gathering salt, mushrooms, greens and berries, with Matt identifying everything before it goes in the basket. It ends at a table if you book the longer tier."
- After, leading with what a guest does and learns: "You walk with Matt, carry a basket, and learn to tell each plant and mushroom from the thing that looks like it. What you gather goes home with you, and the twelve-hour day ends with dinner cooked from it."
- Kept: the included-list line and the 6-hour tier line ("Beach and forest, or forest and farm stands"). Triple now appears twice.

## 6a. About, Living Light twice
- Before ("Los Angeles, then north"): "Part of that stretch I was an instructor at Living Light Culinary Arts Institute in Fort Bragg, up the coast from where I live now."
- After: "Part of that stretch I taught at a culinary school in Fort Bragg, up the coast from where I live now." The named school stays in "Teaching" only.

## 6b. About, the town weekend
- Before: "One weekend I cooked for the town of Mendocino for free" sat in "Teaching", after Esalen.
- After: moved (with its CONFIRM comment) to the end of "Mendocino". "Teaching" now ends on Esalen.

## 6c. Private chef, Albion justification twice
- Before ("Good to know", Where): "...or Chef Matt's home kitchen in Albion, CA for guests who would rather not host."
- After: "Your vacation rental, second home or full-time home in the greater Mendocino area. The other address is Chef Matt's own kitchen in Albion, CA. Further out, ask." The reason to use Albion is given once, in "How a dinner works".

## 6d. Private chef, group size three times
- Before ("Who books a private chef"): "Most nights are for couples and families in vacation rentals, from a table for two up to twelve."
- After: "Most nights are for couples and families in vacation rentals." The one-to-twelve range stays in "Good to know" and in the FAQ answer.

## Build checks after `python3 build.py`
- `id="build"` in `dist/index.html`: 1
- "dinner that night" on Home: 0
- "Living Light" on About: 1
- shore / forest / farm-stands triple on Foraging: 2 (included-list, 6-hour tier)
- em dash outside `<cite>` across `dist/`: 0
