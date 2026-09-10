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
