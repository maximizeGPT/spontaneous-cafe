# R2. Keywords, SERP and competitors

The Spontaneous Cafe, Chef Matt Samuelson, Mendocino CA. Research run 2026-09-19.
Read-only research. No repo file was edited. Every external claim carries a URL.

## How demand was measured

Google Trends refused every request (HTTP 429 and HTTP 400 on the explore endpoint), so
there is no trend figure in this report. No paid keyword tool was used. Nothing here is a
made-up volume number.

Demand is therefore classified three ways, and every claim is labelled:

- **Autocomplete present.** The phrase came back from Google's own suggest endpoint
  (`suggestqueries.google.com/complete/search?client=firefox`). Google only suggests
  phrases people actually type, so presence is evidence of standing demand. Absence is
  evidence of very low demand, not proof of zero.
- **Autocomplete absent.** Queried and returned nothing.
- **SERP composition.** Who fills the top of the results page, read from live US searches.

Bing autocomplete (`api.bing.com/osjson.aspx`) returned almost nothing for this whole
niche: ten seeds, three with any suggestion at all, and two of those were the LA sandwich
chain Mendocino Farms. Treat the entire keyword set as **low absolute volume, high
intent**. This is a niche where ten right visitors a month beat a thousand wrong ones.

---

## A. Keyword map

One row per existing page. Character counts verified: every proposed title is 60
characters or fewer, every proposed description is between 120 and 155.

### `/` Home

| Field | Value |
|---|---|
| **Primary query** | the spontaneous cafe (brand) + private chef mendocino |
| **Secondary** | chef mendocino coast, mendocino private dinner, personal chef mendocino, foraging and dinner mendocino, mendocino county chef |
| **Current title** (53) | The Spontaneous Cafe \| Chef Matt Samuelson, Mendocino |
| **Proposed title** (52) | The Spontaneous Cafe \| Private Chef, Mendocino Coast |
| **Proposed description** (135) | Chef Matt Samuelson has cooked on the Mendocino coast since 2009. Private chef dinners, foraging days, catering and classes, from $300. |
| **Current h1** | Wild food, cooked where you're staying. |
| **Proposed h1** | Leave it. See the note below. |

Why the title changes: "Chef Matt Samuelson" as the second half spends the tail of the
title on a name nobody searches for. `chef matt samuelson` returned **no Google
autocomplete at all**, so there is no standing brand demand on his name yet. Swapping in
"Private Chef, Mendocino Coast" puts the highest-intent service phrase and the place
modifier where a local searcher reads them, and keeps the brand first for the people who
do search the business name.

h1 note: "Wild food, cooked where you're staying" contains no service word and no place
word, which is a real keyword miss. It is also the approved brand line and the h2 directly
beneath it ("Foraging days, private dinners, catering and classes") carries the full
service cluster four lines into the DOM. Recommendation is to leave the h1 and let the h2
do the keyword work. If Mohammed wants the h1 changed anyway, the minimum-damage version
is "Wild food, cooked where you're staying on the Mendocino coast." That is the lowest
confidence item in this report.

**Who ranks now** for `private chef mendocino`:

| # | Result | Page type |
|---|---|---|
| 1 | [yhangry.com/f/private-chefs/us-california-mendocino--county](https://yhangry.com/f/private-chefs/us-california-mendocino--county) | Marketplace |
| 2 | [yhangry.com/s/private-chef-jobs/...](https://yhangry.com/s/private-chef-jobs/us-california-mendocino--county/) | Marketplace (jobs) |
| 3 | [takeachef.com/en-us/private-chef/mendocino-county](https://www.takeachef.com/en-us/private-chef/mendocino-county) | Marketplace |
| 4 | [yelp.com search, personal chefs, Mendocino County](https://www.yelp.com/search?cflt=personalchefs&find_loc=Mendocino+County,+CA) | Directory |
| 5 | [meetachef.com/chefs/mendocino,california](https://meetachef.com/chefs/mendocino,california) | Marketplace |

Only two independent local business sites appear anywhere on page one:
[chefstablellc.com](https://www.chefstablellc.com/) and
[goodearthkitchen.net](https://www.goodearthkitchen.net/private-chef).

---

### `/foraging/`

| Field | Value |
|---|---|
| **Primary query** | mushroom foraging mendocino |
| **Secondary** | mushroom hunting mendocino, mushroom foraging tour mendocino, mushroom foraging mendocino county, coastal foraging mendocino, mendocino mushroom season, foraging class california |
| **Current title** (53) | Foraging Excursions \| The Spontaneous Cafe, Mendocino |
| **Proposed title** (51) | Mushroom Foraging Mendocino \| Guided Days from $300 |
| **Proposed description** (138) | Mushroom foraging on the Mendocino coast with Chef Matt Samuelson. Beach salt, wild mushrooms, farm stands, then dinner. 3, 6 or 12 hours. |
| **Current h1** | Foraging days on the Mendocino coast. |
| **Proposed h1** | **Mushroom foraging days on the Mendocino coast.** |

**This is the single biggest keyword miss on the site.** The word "mushroom" appears
nowhere in the title, the description or the h1 of the foraging page, and every piece of
demand evidence points at "mushroom" as the word people type. Confirmed in Google
autocomplete: `mendocino mushroom foraging`, `mushroom foraging mendocino county`,
`mushroom hunting mendocino`, `mushroom foraging tour mendocino`, `mendocino mushroom
hunting`, `mendocino mushroom season`. "Foraging excursions" is the client's own phrase.
It returned no autocomplete in any form.

h1 reason, one line: adding one word puts the primary query in the h1 without touching the
approved sentence shape, and "Mushroom foraging" becomes the load-bearing word pair the
accent face goes on.

A second title is worth A/B thinking about if the price in the title feels wrong for the
client: "Mushroom Foraging Tours, Mendocino Coast | Matt Samuelson" (57).

**Who ranks now** for `mendocino foraging tour`:

| # | Result | Page type |
|---|---|---|
| 1 | [mendovoice.com, storms bring mushroom foraging](https://mendovoice.com/2024/11/huge-storms-expected-to-bring-superb-mushroom-foraging-for-those-in-the-know/) | Article, local news |
| 2 | [marinmagazine.com, Mushroom Foraging in Mendocino](https://marinmagazine.com/travel/local-travel/mushroom-foraging-in-mendocino/) | Article, regional mag |
| 3 | [7x7.com, Mushroom Hunting in Mendocino](https://www.7x7.com/tis-the-season-mushroom-hunting-in-mendocino-2084146809.html) | Article, SF lifestyle |
| 4 | [ediblemendocino.com, Foraging Experiences](https://ediblemendocino.com/stories/mendocino-mushroom-foraging-experiences-in-fall-winter-2024-25/) | Article, roundup |
| 5 | [forkinthepath.org/schedule](https://www.forkinthepath.org/schedule) | Local business, class schedule |
| 6 | [visitmendocino.com/walk-on-the-wild-side](https://www.visitmendocino.com/walk-on-the-wild-side/) | Destination marketing listicle |
| 7 | [catchncookcalifornia.com, Private Foray Mendocino](https://www.catchncookcalifornia.com/event-details/private-foray-coastal-foraging-mendocino) | Local business, event page |

**Read this SERP carefully, it is the opportunity in this whole report.** Six of the top
seven results are editorial. Not one dedicated, well-structured service page from a local
guide ranks for the head term. The businesses that get the bookings get named *inside* the
articles (Mendo Insider Tours, Stanford Inn, Inn at Newport Ranch, Mar Vista, Jug Handle
Creek Farm), which means two things at once: a real service page has an unusually open
lane, and getting named in the next roundup is worth as much as ranking.

Marketplaces do **not** dominate this SERP. Airbnb Experiences listings exist for the
region ([Exclusive Foraging Tours on Private
Land](https://www.airbnb.com/experiences/6706680) at $225 per guest, [Learn to forage wild
food with a professional](https://www.airbnb.com/experiences/5510810)) but none of them
surfaced in the organic top ten.

---

### `/private-chef/`

| Field | Value |
|---|---|
| **Primary query** | private chef mendocino |
| **Secondary** | private chef mendocino county, private chef fort bragg ca, personal chef mendocino, in-home chef mendocino, private chef sea ranch ca, private chef cost per day |
| **Current title** (46) | Private Chef \| The Spontaneous Cafe, Mendocino |
| **Proposed title** (49) | Private Chef, Mendocino Coast \| Dinners from $300 |
| **Proposed description** (144) | A private chef in Mendocino for one to twelve guests. Matt Samuelson cooks in your rental or at his Albion kitchen. 3, 6 or 12 hours, from $300. |
| **Current h1** | A private chef on the Mendocino coast. |
| **Proposed h1** | Leave it. It contains the primary query verbatim. |

Why the title changes: the current one puts "Private Chef" and "Mendocino" 30 characters
apart with the brand wedged between them. Proximity matters for a local phrase match, and
the freed characters buy "from $300", which is the one thing every competitor page in this
SERP refuses to publish.

`private chef fort bragg ca` is a **confirmed autocomplete phrase**, as is `private chef
sea ranch ca`. Both deserve a line of body copy on this page, not a page of their own.

**Who ranks now**: same SERP as Home above. Five of the top five are marketplaces or
directories.

---

### `/catering/`

| Field | Value |
|---|---|
| **Primary query** | mendocino county catering (see the Mendocino Farms warning) |
| **Secondary** | wedding catering mendocino, mendocino ca catering, mendocino wedding catering, caterer fort bragg ca, mendocino retreat catering, rehearsal dinner mendocino |
| **Current title** (53) | Catering and Events \| The Spontaneous Cafe, Mendocino |
| **Proposed title** (57) | Mendocino County Catering \| Weddings, Retreats, 20 to 350 |
| **Proposed description** (142) | Catering in Mendocino County for weddings, rehearsal dinners, retreats and reunions, 20 to 350 guests. Seated, family style or grazing tables. |
| **Current h1** | Mendocino catering, from a rehearsal dinner to a wedding. |
| **Proposed h1** | Leave it. It already carries "Mendocino catering" and "wedding". |

**Mendocino Farms warning.** The bare phrase `catering mendocino` is polluted. Google
autocomplete for that seed returns `catering mendocino farms`, `catering mendocinofarms
com`, `catering mendocino catering coupon code` and `mendocino catering prices`, most of
which belong to [Mendocino Farms](https://www.mendocinofarms.com/catering), the Los
Angeles sandwich chain, which also ranks in the organic results for `catering mendocino
ca`. Do not build a page around the bare two-word phrase. Target `mendocino county
catering` and `mendocino ca catering` (both confirmed autocomplete) and `wedding catering
mendocino` (confirmed autocomplete), all of which disambiguate.

**Who ranks now** for `catering mendocino ca`:

| # | Result | Page type |
|---|---|---|
| 1 | [theknot.com/marketplace/catering-mendocino-ca](https://www.theknot.com/marketplace/catering-mendocino-ca) | Wedding marketplace |
| 2 | [yelp.com caterers near Mendocino 95460](https://www.yelp.com/search?cflt=catering&find_loc=Mendocino%2C+CA+95460) | Directory |
| 3 | [yelp.com caterers Mendocino County](https://www.yelp.com/search?cflt=catering&find_loc=Mendocino+County,+CA) | Directory |
| 4 | [mendocinofarms.com/catering](https://www.mendocinofarms.com/catering) | Brand collision, LA chain |
| 5 | [mendocinobbq.com](https://www.mendocinobbq.com/) | Local business |
| 6 | [chefstablellc.com](https://www.chefstablellc.com/) | Local business |
| 7 | [mendoughs.com](https://mendoughs.com/) | Local business |

`wedding catering mendocino` is where The Knot and Zola take over almost completely:
[The Knot, Fort Bragg catering](https://www.theknot.com/marketplace/catering-fort-bragg-ca),
[Zola Mendocino wedding catering](https://www.zola.com/wedding-vendors/search/mendocino-ca--wedding-catering--cuisine-types-seafood).

---

### `/cooking-classes/`

| Field | Value |
|---|---|
| **Primary query** | cooking class mendocino |
| **Secondary** | mendocino cooking class, cooking classes fort bragg ca, private cooking class mendocino, knife skills class, living light culinary arts fort bragg |
| **Current title** (48) | Cooking Classes \| The Spontaneous Cafe, Mendocino |
| **Proposed title** (52) | Cooking Classes, Mendocino \| Knife Skills, from $300 |
| **Proposed description** (148) | Cooking classes in Mendocino with Chef Matt Samuelson, who taught at Living Light in Fort Bragg. Knife skills and cooking with no recipe, from $300. |
| **Current h1** | Cooking classes in Mendocino. |
| **Proposed h1** | Leave it. It is the primary query, exactly. |

Demand honesty: `cooking class mendocino` returned exactly one autocomplete suggestion,
itself. `mendocino cooking class` returned two. Bing returned nothing. This is the
thinnest of the four services by search demand and should be resourced accordingly. Its
real value is as a **cross-sell surface** and as the page that carries the Living Light
credential, which is the strongest expertise signal on the whole site.

**Who ranks now** for `cooking classes mendocino`:

| # | Result | Page type |
|---|---|---|
| 1 | [stanfordinn.com cooking classes](https://stanfordinn.com/mendocino-oceanview-resort-cooking-classes/) | Local business, inn |
| 2 | [mendocino.edu culinary arts management](https://www.mendocino.edu/about/administration/administrative-departments/culinary-arts-management) | College programme |
| 3 | [yelp.com cooking classes Mendocino 95460](https://www.yelp.com/search?cflt=cookingclasses&find_loc=Mendocino%2C+CA+95460) | Directory |
| 4 | [localcookingclasses.com Mendocino](https://www.localcookingclasses.com/cooking-classes-in-mendocino-ca.html) | Thin directory, 2022 data |
| 5 | [wbwcenter.com healthy cooking classes](https://wbwcenter.com/healthy-cooking-classes/) | Local business, wellness |
| 6 | [assaggiare.com/classes](https://www.assaggiare.com/classes/) | Local business |

---

### `/about/`

| Field | Value |
|---|---|
| **Primary query** | chef matt samuelson (brand, currently zero demand) |
| **Secondary** | living light culinary arts instructor, mendocino chef, flow restaurant mendocino chef, spontaneous cafe mendocino |
| **Current title** (44) | About Matt \| The Spontaneous Cafe, Mendocino |
| **Proposed title** (53) | Chef Matt Samuelson, Mendocino \| The Spontaneous Cafe |
| **Proposed description** (140) | Chef Matt Samuelson cooked in Peru, Thailand and India, taught at Living Light in Fort Bragg, and has worked the Mendocino coast since 2009. |
| **Current h1** | I'm Matt. I forage and I cook. |
| **Proposed h1** | Leave it. This page's job is trust, not ranking. |

Why the title changes: "About Matt" is a navigation label, and it wastes the first ten
characters, the part Google weights hardest. The full name is the entity Google needs to
connect to the business, the Google Business Profile and the existing third-party
mentions. Making it the first thing in the title is how that connection gets made.

`chef matt samuelson` produced **no autocomplete suggestions at all**. There is no name
demand to capture today. This page is a credibility page whose job is to feed E-E-A-T
signals to the money pages and to give Google an entity to bind the citations to. Treat
its ranking performance as irrelevant for the next six months.

**Existing brand footprint found** for `"Spontaneous Cafe" Mendocino Matt Samuelson`:

| Result | Page type | Note |
|---|---|---|
| [spontaneouscafe.com](https://spontaneouscafe.com/) | Own site, old GoDaddy page | Indexed. Title is the bare word "Spontaneous Cafe", no meta description. |
| [alignable.com/mendocino-ca/spontaneous-cafe](https://www.alignable.com/mendocino-ca/spontaneous-cafe) | Business directory | Existing citation |
| [whbrewing.com, "The Spontaneous Cafe" w/ Chef Matt](https://www.whbrewing.com/event-details/the-spontaneous-cafe-w-chef-matt) | Event page | Existing citation and backlink |
| [Facebook, Mendocino Foodies group post](https://www.facebook.com/groups/mendocinofoodies/posts/490049247233269/) | Social | Existing mention |
| [Tripadvisor, Flow Restaurant and Lounge](https://www.tripadvisor.com/Restaurant_Review-g32701-d5267701-Reviews-Flow_Restaurant_and_Lounge-Mendocino_Mendocino_County_California.html) | Review site | Matches his 2015 to 2017 executive chef role per CONTEXT.md |

---

### `/contact/`

| Field | Value |
|---|---|
| **Primary query** | booking intent, no meaningful head term |
| **Secondary** | private chef mendocino cost, how much does a private chef cost per day, mendocino caterer prices, book a chef mendocino |
| **Current title** (41) | Contact \| The Spontaneous Cafe, Mendocino |
| **Proposed title** (55) | Book Chef Matt Samuelson, Mendocino \| Rates and Contact |
| **Proposed description** (139) | Book Chef Matt Samuelson for a foraging day, dinner, catering or a class in greater Mendocino. 3 hours $300, 6 hours $500, 12 hours $1,000. |
| **Current h1** | Send Matt the details. |
| **Proposed h1** | Leave it. |

Why the title changes: this page already carries the full price table, which is the thing
the pricing-intent queries want. "Rates" in the title is what lets it answer `private chef
cost per day` and `how much is a private chef for a day`, both confirmed autocomplete.

---

## B. Long-tail and questions

Everything below came back from Google autocomplete on 2026-09-19 unless marked
otherwise. Bing results are marked. Phrases with no source marker are **confirmed
autocomplete**.

### Foraging

| Phrase | Where it should land |
|---|---|
| mendocino mushroom foraging | `/foraging/` title, h1, first paragraph |
| mushroom foraging mendocino county | `/foraging/` body, one sentence naming the county |
| mushroom hunting mendocino | `/foraging/` body. "Hunting" is a synonym Matt's copy never uses. Add it once in prose. |
| mushroom foraging tour mendocino | `/foraging/` body. "Tour" is another word his copy avoids. |
| mendocino mushroom season | New page. Seasonal calendar, gap D1 |
| mendocino mushroom hunting | `/foraging/` body |
| coastal foraging mendocino | `/foraging/` body, the salt and shore section |
| mushroom foraging courses near me | `/foraging/` and `/cooking-classes/` cross-link |
| wild food foraging classes near me | `/foraging/` body |
| foraging class california | `/foraging/` body, one mention of California |
| california foraging laws | New page, gap D2 |
| can you forage in california state parks | FAQ on `/foraging/`, gap D2 |
| do you need a permit to pick mushrooms in california | FAQ on `/foraging/`, gap D2 |
| jackson demonstration state forest mushroom permit | New page, gap D2 |
| jackson state forest mushroom permit | Same |
| is foraging dangerous / is foraging safe | Existing FAQ "Is it safe to eat what we find?" already answers this. Reword the summary to include the word "safe" earlier. |
| what to wear foraging / what to bring foraging | Existing FAQ "What should I wear and bring?" Good as is. |
| what to wear mushroom foraging / what to bring mushroom foraging | Add "mushroom" to that FAQ answer body |
| benefits of foraging | Skip. Informational, no booking intent. |
| candy cap mushroom ice cream mendocino | Seasonal calendar page, candy cap entry, gap D1 |
| mendocino mushroom festival 2026 | Gap D6, event-adjacent page |
| mendocino mushroom club | External. Citation and partnership target, section C. |
| mendocino mushroom permit / mendocino mushroom guide | Gap D2 |
| how long does mushroom season last / is mushroom season over | Seasonal calendar FAQ, gap D1 |
| when is mushroom season in california | Seasonal calendar, gap D1 |
| mendocino sea urchin foraging, mendocino uni foraging | **Do not target.** Matt forages mushrooms, berries, greens and salt only (CONTEXT.md, round 3). This is the strongest foraging autocomplete in the set and he cannot serve it. |
| can you harvest mussels in california | **Do not target**, same reason |
| how to harvest sea salt from the ocean | Weak fit. Informational and national. One paragraph on `/foraging/`, no page. |
| are huckleberries edible | Seasonal calendar, summer entry. Informational, low priority. |
| huckleberry festival mendocino, huckleberry jam mendocino | Skip. Event queries Matt does not run. |

### Private chef

| Phrase | Where it should land |
|---|---|
| private chef mendocino county | `/private-chef/` body |
| private chef fort bragg ca | `/private-chef/` body, one sentence naming Fort Bragg |
| private chef sea ranch ca | `/private-chef/` body, one sentence in the area-served line |
| private chef cost per day | `/private-chef/` price block and `/contact/` |
| how much is a private chef for a day | New FAQ on `/private-chef/`, the 12-hour tier answers it exactly |
| how much does a private chef cost for a dinner party | New FAQ on `/private-chef/` |
| what is the difference between a personal chef and a private chef | New FAQ on `/private-chef/`. Cheap to write, captures the "personal chef" synonym Matt's copy never uses. |
| does a private chef do the dishes | Existing copy answers it ("clears the kitchen before he leaves"). Turn it into a one-line FAQ. |
| what does a private chef do | `/private-chef/` first paragraph |
| private chef at home near me | `/private-chef/` body |
| mendocino private dinner, hire a chef mendocino, in-home chef mendocino, mendocino airbnb chef | **Autocomplete absent.** Real phrasings, no standing demand. Use them once in body copy, never as a page target. |

### Catering

| Phrase | Where it should land |
|---|---|
| mendocino county catering, mendocino ca catering | `/catering/` title and body |
| mendocino wedding catering, wedding catering mendocino | `/catering/` h1 already has it. Add "wedding catering" as an exact pair once in body. |
| average cost to cater a wedding | New FAQ on `/catering/`. Matt quotes per event above twelve, so the honest answer is a range plus "quoted". Needs Matt to approve a stated range. |
| how much to cater a wedding for 50 people | Same FAQ |
| mendocino retreat center, mendocino yoga retreat, mendocino wellness retreat, mendocino writing retreat | Gap D4, a retreat catering section or page. Every one of these is confirmed autocomplete and the retreat business on this coast is real (see section C). |
| caterer fort bragg, mendocino county wedding catering, anderson valley catering | **Autocomplete absent.** Mention in body only. |
| mendocino bachelorette party | Weak but present. One line in the `/catering/` event-types list, no more. |

### Cooking classes

| Phrase | Where it should land |
|---|---|
| mendocino cooking class | `/cooking-classes/` title and body |
| cooking class mendocino | Same |
| mendocino grove cooking | Ignore. Refers to the campground. |
| what to cook with what is in the fridge | Adjacent, no local intent. Leave as body copy. |
| cooking class fort bragg, private cooking class mendocino | **Autocomplete absent.** Body copy only. |

### Trip planning, the upstream demand

These are the queries a Mendocino visitor runs *before* they know a private chef is an
option. They are the widest pool of potential customers and the site currently intercepts
none of them.

| Phrase | Where it should land |
|---|---|
| things to do in mendocino, things to do in mendocino ca | Gap D3 |
| things to do in mendocino this weekend | Gap D3 |
| things to do in mendocino with kids | Existing FAQ "Can we bring kids?" is the hook. Gap D3 links to it. |
| rainy day mendocino, mendocino rainy day activities | Gap D3. Mushroom season **is** the rainy season, which makes this a genuinely strong angle rather than a stretch. |
| mendocino winter activities | Gap D3 |
| best time to visit mendocino, best month to visit mendocino | Gap D1, the seasonal calendar answers it from a food angle |
| farm to table mendocino, farm to table restaurants mendocino | `/` and `/private-chef/` body. The phrase is already in the brand vocabulary per CONTEXT.md. |
| mendocino wild food | **Autocomplete absent.** Brand-voice phrase, no demand. |

### Questions the pages already answer

Worth noting so nobody rewrites them: the 21 existing `<details>` FAQs across the five
service pages are already emitted as `FAQPage` JSON-LD by `build.py:164` (`faq_jsonld`).
That is a real asset. The gaps above are additions to it, not replacements.

---

## C. Competitors

### Foraging and experiences

| Name | URL | Ranks for | What their page does that ours does not | What ours does better |
|---|---|---|---|---|
| **Mendo Insider Tours** | [mendoinsidertours.com/mendocino-mushroom-tours/](https://mendoinsidertours.com/mendocino-mushroom-tours/) | The closest thing to a direct competitor. Named first in the Marin Magazine and Edible Mendocino roundups. | Has a dedicated URL with "mendocino-mushroom-tours" in the slug, and an existing transport and tour business behind it. Runs Oct to Feb only. | Their page is roughly 550 words, publishes **no price**, states **no duration**, carries no schema, and the only reviews on the page are for their wedding transport service. Our foraging page is longer, priced, and ends at a dinner they cannot cook. |
| **Fork In the Path** | [forkinthepath.org/schedule](https://www.forkinthepath.org/schedule) | Ranks top five for `mendocino foraging tour` and top of `mushroom foraging classes bay area`. | A live, dated class schedule (roughly 3,500 words of event listings), a cart, and an Airtable waitlist. Recurring content that refreshes itself. They cover nine locations from Berkeley to Mount Shasta. | Regional generalist, Mendocino is one stop of nine. We are local and can pair the forage with a dinner in the guest's own rental. |
| **Flora & Fungi Adventures** | [floraandfungiadventures.com](https://www.floraandfungiadventures.com/event-details/mendocino-purple-sea-urchin-mussels-seaweed-extravaganza-4) | Coastal foraging events in Mendocino | Event-per-page structure with dates, which is what earns them long-tail seasonal traffic. | Their Mendocino offering leans sea urchin and mussels, which Matt does not do. Different customer. |
| **CatchNCookCalifornia** | [catchncookcalifornia.com](https://www.catchncookcalifornia.com/event-details/private-foray-coastal-foraging-mendocino) | `mendocino foraging tour`, page one | Publishes an exact price ($200) and an exact date and time on the event page, and shows "sold out", which is powerful social proof. | Again eels, mussels and rock crab, not Matt's field. |
| **Stanford Inn by the Sea** | [stanfordinn.com](https://stanfordinn.com/mendocino-vacation-packages-tours/) | Both foraging and cooking class queries | An inn with rooms, a restaurant and a captive audience. Named in the Visit Mendocino listicle. Mushroom tours with mycologist Adrienne Long cited at $35 by [7x7](https://www.7x7.com/tis-the-season-mushroom-hunting-in-mendocino-2084146809.html). | Package pricing is tied to a stay. We are bookable by anyone in any rental. |
| **Inn at Newport Ranch** | Cited in [Marin Magazine](https://marinmagazine.com/travel/local-travel/mushroom-foraging-in-mendocino/) | Roundup mentions | A four-hour UTV excursion, picnic lunch, mushroom log to take home, mushroom dinner, **$950 for two**. | Useful price anchor. Matt's 6-hour tier at $500 covers a whole group, not two people. That comparison is worth making somewhere. |
| **Mendocino Coast Mushroom Club** | [mendocinocoastmushroomclub.org](https://www.mendocinocoastmushroomclub.org/) | `mendocino mushroom club`, festival queries | Non-profit, runs forays and the Fungi Festival, meets monthly Sept to May at the First Presbyterian Church in Fort Bragg. | Not a competitor. **This is a partnership and citation target**, see action 9. |

### Private chef and catering

| Name | URL | Ranks for | What their page does that ours does not | What ours does better |
|---|---|---|---|---|
| **Good Earth Kitchen** | [goodearthkitchen.net/private-chef](https://www.goodearthkitchen.net/private-chef) | `private chef mendocino`, one of only two local sites on page one | Publishes productised packages with **from** prices: Modern Cocktail Party from $55 per person, Tiny Wedding Celebration Feast from $1,500, Brunch Grazing Table from $45 per person. Named packages are easy to link to and easy to compare. | Their h1 is "Our Private Chef Services", no place word. No meta description. No schema. Based in Willits, which is inland, an hour from the coast. Our hour-based pricing is clearer than per-person for a group that keeps changing size. |
| **Chef's Table Catering** | [chefstablellc.com](https://www.chefstablellc.com/) | `private chef mendocino`, `catering mendocino ca` | Title is keyword-dense and works: "Mendocino Farm to Table Wedding Catering \| Luxury Catering and Private Chef Services". Proof that a plain, stuffed title still ranks in this market. | The whole homepage is 350 to 400 words. No prices anywhere. No meta description. No schema. Split across Mendocino and Sonoma. Our service pages are several times deeper and priced. |
| **Assaggiare Mendocino** | [assaggiare.com](https://www.assaggiare.com/classes/) | Wedding catering and classes. Listed on [The Knot](https://www.theknot.com/marketplace/assaggiare-mendocino-fort-bragg-ca-627093). | Combines catering, event production and culinary education, the same bundle Matt offers. The closest strategic competitor. Fort Bragg based. | Their site served an invalid TLS certificate when fetched on 2026-09-19 (hostname does not match, cert is for `*.cleverconcepts.net`). A browser warning on a wedding vendor's site is a live conversion leak we do not have. |
| **Mendocino BBQ Catering** | [mendocinobbq.com](https://www.mendocinobbq.com/) | `catering mendocino ca` | Single clear cuisine, award-winning pitmaster angle, lists exactly what the rental package includes. | Narrow cuisine, no foraging, no classes. |
| **Feast Mendocino, Karina's Catering, Ellery Clark, Mendocino Catering Co., Mendoughs, Henny Penny, Good Thyme, Pilón Kitchen, Prasad Events** | via [Yelp](https://www.yelp.com/search?cflt=catering&find_loc=Mendocino%2C+CA+95460) and [The Knot](https://www.theknot.com/marketplace/catering-fort-bragg-ca) | Long tail of the catering SERP | Most hold Knot and Yelp profiles. That is how this market is actually shopped. | Catering is the most crowded of the four services and the least differentiated for Matt. Rank it third for effort, behind foraging and private chef. |
| **Sea Ranch Gourmet, Black Oak Catering, Chef Adair** | [alignable Sea Ranch Gourmet](https://www.alignable.com/gualala-ca/sea-ranch-gourmet), [chefadair.com](https://www.chefadair.com/) | The southern coast, Gualala, Sea Ranch, Annapolis | They own the Mendonoma and Sonoma coast end. Chef Adair has per-market landing pages (Sonoma, Napa, Marin, corporate retreats). | Matt is nearer the Mendocino village and Fort Bragg end. Do not fight for Sea Ranch. One mention on `/private-chef/` is the right investment. |

### Cooking classes

| Name | URL | Ranks for | What their page does that ours does not | What ours does better |
|---|---|---|---|---|
| **Stanford Inn Culinary Classes** | [stanfordinn.com/mendocino-oceanview-resort-cooking-classes/](https://stanfordinn.com/mendocino-oceanview-resort-cooking-classes/) | Number one for `cooking classes mendocino` | Publishes a full price grid: $135 per person, $205 per couple, $110 per person for 3 to 6, and $255 / $345 / $155 for the nutrition combination. Names each class. Roughly 1,200 words. | Strictly plant-based vegan, and tied to the resort. Matt's range (vegan, raw and gluten free per his resume, plus everything else) is wider, and he teaches in the guest's own kitchen. |
| **Living Light Culinary Arts Institute** | Fort Bragg, 301 N Main St | `culinary school fort bragg` | This is where **Matt taught** (2000 to 2004, 2008 to 2009, 2017 to 2019 per CONTEXT.md). | The credential is already ours and is the strongest expertise signal on the site. It is currently buried in a paragraph on `/cooking-classes/` and on `/about/`. Put it in the meta description. |
| **Whole Body Wellness** | [wbwcenter.com/healthy-cooking-classes/](https://wbwcenter.com/healthy-cooking-classes/) | `cooking classes fort bragg` | Local, wellness framing | Small operation, narrow. |

### Marketplace dominance, and whether to list

This is a business decision for Mohammed. The evidence:

**Private chef: marketplaces own the SERP outright.** Five of the top five results for
`private chef mendocino` are yhangry, Take a Chef, Yelp and MeetAChef. yhangry states
[17 private chefs available in Mendocino
County](https://yhangry.com/f/private-chefs/us-california-mendocino--county); Take a Chef
states [16 chefs, with guests booking around $173 per person for 3.48
courses](https://www.takeachef.com/en-us/private-chef/mendocino-county). Those are the
platforms' own published figures, not estimates of mine.

- **Option**: list on Take a Chef and yhangry. Upside, they already rank and Matt's
  per-hour pricing undercuts a $173 per person average badly for a table of six (6 hours
  $500 versus roughly $1,038). Downside, commission, a menu format built around per-person
  pricing that fights his hour tiers, and the platform owns the customer relationship and
  the review.
- **Recommendation**: worth testing one platform for one season, because ranking a new
  site above four marketplaces on a head term is a twelve-month project and the
  marketplaces convert today. Frame it as paid customer acquisition, not SEO.

**Catering: The Knot, Zola and Yelp own the wedding end.** Every wedding-catering query
surfaced them. Nine named local caterers were found through those two profiles alone.

- **Option**: a The Knot profile. Matt's catering range of 20 to 350 guests fits. Downside,
  The Knot's pricing is significant for a solo operator.
- **Recommendation**: a **free Yelp profile** is close to mandatory regardless, because
  Yelp fills three separate slots across these SERPs. The Knot is a spend decision that
  depends on how much wedding work Matt actually wants.

**Foraging: marketplaces do not dominate.** Editorial does. Airbnb Experiences listings
exist for the region ([$225 per
guest](https://www.airbnb.com/experiences/6706680)) but none ranked organically.

- **Option**: an Airbnb Experience listing. Upside, Matt's customers are already
  San Francisco weekenders in Mendocino rentals, which is exactly Airbnb's audience, and
  the $225-per-guest comparable suggests his 3-hour $300 for a whole group is competitive.
  Airbnb Experiences requires approval and has its own content rules.
- **Recommendation**: this is the strongest marketplace fit of the three, because the
  channel matches the customer. Worth an application.

**Tripadvisor, Viator, GetYourGuide and Eventbrite did not appear in any of the fourteen
SERPs run.** No evidence they matter here. Eventbrite only surfaced for mushroom festival
queries, which are events Matt does not run.

---

## D. Content gaps

Ranked by expected return. Maximum of eight, and I have kept it to seven because the
eighth candidate was not worth the maintenance.

### D1. Mendocino mushroom season calendar

- **Target query**: `mendocino mushroom season`, `when is mushroom season in california`,
  `chanterelle season northern california`, `best time to visit mendocino`, `how long does
  mushroom season last`. All confirmed autocomplete.
- **Page type**: seasonal calendar, one page, month by month.
- **Must contain**: a month-by-month table of what is up and when; the rain rule; what a
  guest can realistically expect to find in each month; and a booking CTA inside every
  season block. This is the page that earns links from the roundup writers.
- **Public facts, with sources**: chanterelles can fruit on the coast as early as August
  without rain ("summer chanterelles"), with heavier fruiting once the rains start and
  continuing to around January, and candy caps run roughly November to February in the
  coastal forests of Mendocino and Humboldt
  ([ForageSF California mushroom calendar](https://www.foragesf.com/blog/california-mushroom-calendar),
  [Wilderfolk, Reading the Mendocino Coast Through the Seasons](https://campcandycap.com/reading-the-mendocino-coast-through-the-seasons/)).
  Chanterelles, porcini and candy caps are broadly September to November
  ([Mushroom Tracker California guide](https://www.mushroomtracker.ca/blog/mushroom-foraging-california.html)).
  Mendo Insider Tours runs mushroom tours October through February
  ([their page](https://mendoinsidertours.com/mendocino-mushroom-tours/)). Mendocino County
  is cited as hosting over 3,000 fungi species
  ([North of Ordinary](https://northofordinaryca.com/blog/mushroom-feast-mendocino/)).
  Mendocino Coast Mushroom Club maintains a local species list
  ([MCMC](https://www.mendocinocoastmushroomclub.org/mushrooms-of-the-mendocino-coast.html)).
- **Needs Matt**: which species he actually takes guests to, in which months, on which kind
  of ground. The published calendars above are regional. His is the only one that can be
  specific to where he walks. Also whether he is comfortable being that specific in public.
  **Do not publish a single month claim that came from the sources above without Matt
  confirming it matches his own experience.**
- **Note**: the site already has four "baskets by season" blocks on `/foraging/`. This page
  is the expansion of that material into something a search engine can rank, and the
  existing blocks should link to it rather than be duplicated.

### D2. Foraging rules and permits, Mendocino

- **Target query**: `jackson demonstration state forest mushroom permit` (confirmed
  autocomplete, both the short and long form), `california foraging laws`, `can you forage
  in california state parks`, `do you need a permit to pick mushrooms in california`,
  `is mushroom foraging illegal`, `mendocino mushroom permit`.
- **Page type**: guide, or a deep FAQ section on `/foraging/`. Start as a section, promote
  to a page if it earns impressions.
- **Must contain**: who needs a permit and where; what is prohibited; what Matt handles on
  a booked day so the guest does not have to think about it. That last line is the
  commercial payload. Everyone else writes the rules; only the guide can say "I handle
  this".
- **Public facts, with sources**: a JDSF mushroom permit is **$20 annually**, runs
  **July 1 to June 30**, is issued from the JDSF Fort Bragg office, must be carried while
  gathering, requires a valid mushroom card on the vehicle dash, is non-transferable, has
  no daily limit, covers commercial or personal use, and **digging is prohibited**
  ([CAL FIRE mushroom permit packet, PDF](https://34c031f8-c9fd-4018-8c5a-4159cdff6b0d-cdn-endpoint.azureedge.net/-/media/calfire-website/what-we-do/natural-resource-management/demostration-forests/jackson/recreation-maps-and-permits/mushroom-permit-by-mail-packet2.pdf)).
  Mushroom gathering is prohibited in neighbouring State Parks
  (same source). California State Parks generally prohibit foraging, with Salt Point State
  Park a limited exception at 2 lb per person per day with a day-use permit, and fines up
  to $1,000 for unauthorised harvesting
  ([SOMA rules page](https://www.somamushrooms.org/foraging/rules.php),
  [Mushroom Tracker](https://www.mushroomtracker.ca/blog/mushroom-foraging-california.html)).
- **Needs Matt**: whether he holds a current JDSF permit; whether guests need their own
  permit on his days or are covered; which land he actually uses (state forest, private
  land, farm stands); and whether he wants any of that stated publicly. **This entire page
  is blocked on Matt. Do not guess any of it.** Verify the CAL FIRE fee and dates against
  the current-year packet before publishing, since the PDF found is not dated in its URL.

### D3. Mendocino food things to do

- **Target query**: `things to do in mendocino`, `things to do in mendocino this weekend`,
  `mendocino rainy day activities`, `mendocino winter activities`, `things to do in
  mendocino with kids`. All confirmed autocomplete, and the widest pool in the whole set.
- **Page type**: guide, written from a chef's point of view, not a generic listicle.
- **Must contain**: what to eat and do in each season; the rainy-day angle, which is
  genuinely strong here because mushroom season **is** the rainy season; honest links out
  to farm stands, the market and the mushroom club. Links out are what make this page
  linkable back.
- **Public facts, with sources**: the mushroom festival window, Mendocino County Mushroom
  Feast running November 1 to 10
  ([North of Ordinary](https://northofordinaryca.com/blog/mushroom-feast-mendocino/)); the
  MCMC Fungi Festival
  ([MCMC](https://www.mendocinocoastmushroomclub.org/fungi-festival-2026.html),
  [Arts Mendocino listing](https://artsmendocino.org/event/fungi-festival-and-cultural-convergence/)).
- **Needs Matt**: which farm stands he is willing to name in public. CONTEXT.md says the
  stands are unstaffed and trust-based, and naming them could ruin them. **Ask before
  naming a single one.**
- **Risk**: this is the one gap that can drift into thin travel-blog filler. Build it only
  if Matt gives real, local, specific material.

### D4. Retreat catering

- **Target query**: `mendocino retreat center`, `mendocino yoga retreat`, `mendocino
  wellness retreat`, `mendocino writing retreat`, `mendocino meditation retreat`, all
  confirmed autocomplete, plus `mendocino retreat catering`.
- **Page type**: a section on `/catering/`, promoted to its own page only if it earns
  traffic.
- **Must contain**: multi-day meal coverage; dietary range; the foraging walk plus catered
  dinner combination, which no other caterer on this coast can offer; and the group sizes
  he covers.
- **Public facts, with sources**: the retreat market here is real and venue-led.
  [Spirit Camp Retreat Center](https://www.spirit.camp/retreat-venue-rental-mendocino-california)
  in Little River connects groups with preferred caterers.
  [Mendocino Grove](https://mendocinogrove.com/retreats-workshops) has a commercial kitchen
  and hosts retreats. [Camp Mendocino](https://www.campmendocino.org/rent-camp) includes
  meals in rental fees.
- **Needs Matt**: nothing new. His resume already supports it, retreat menus for 20 to 80
  guests and culinary intensives, per CONTEXT.md.
- **Why this ranks high**: the venues are the customer, not the guest. Five venues on this
  coast, each booking multiple retreats a year, each needing a caterer. That is a
  referral channel a web page can open.

### D5. Private chef pricing FAQ

- **Target query**: `how much does a private chef cost per day`, `how much does a private
  chef cost for a dinner party`, `what is the difference between a personal chef and a
  private chef`, `does a private chef do the dishes`. All confirmed autocomplete.
- **Page type**: FAQ additions on `/private-chef/`, feeding the existing `FAQPage` JSON-LD.
- **Must contain**: the three hour tiers answering the cost questions directly; the
  personal-versus-private distinction, which captures the "personal chef" synonym the site
  never uses; and the washing-up answer, which the body copy already contains.
- **Public facts, with sources**: competitor anchors for context if Mohammed wants them,
  Take a Chef's stated $173 per person Mendocino average
  ([Take a Chef](https://www.takeachef.com/en-us/private-chef/mendocino-county)) and
  yhangry's stated $1,100 average for ten people
  ([yhangry](https://yhangry.com/f/private-chefs/us-california-mendocino--county)).
- **Needs Matt**: nothing. Every fact is already on the site.
- **Effort**: four short FAQ entries. This is the cheapest item in section D and should
  probably ship first on effort grounds alone.

### D6. Mushroom festival season page

- **Target query**: `mendocino mushroom festival 2026`, `mendocino mushroom festival`,
  confirmed autocomplete and clearly seasonal.
- **Page type**: a short, dated page, refreshed each autumn.
- **Must contain**: what the festival window is, what Matt offers during it, and a booking
  CTA. Nothing else.
- **Public facts, with sources**: the Mendocino County Mushroom Feast runs November 1 to 10
  ([North of Ordinary](https://northofordinaryca.com/blog/mushroom-feast-mendocino/)); the
  MCMC Fungi Festival and Cultural Convergence is at Caspar Community Center
  ([Arts Mendocino](https://artsmendocino.org/event/fungi-festival-and-cultural-convergence/)).
- **Needs Matt**: whether he participates, and whether he wants to be seen as festival
  adjacent. **Verify the 2026 dates on the official MCMC page before publishing.** The
  dates above come from secondary sources.
- **Risk**: dated pages rot. Only build this if someone owns refreshing it every September.

### D7. Albion kitchen dinners

- **Target query**: no meaningful head term. `mendocino private dinner` and `hire a chef
  mendocino` both returned **no autocomplete**.
- **Page type**: a section on `/private-chef/`, never a page.
- **Why it is on the list at all**: it is the only genuinely differentiated thing Matt
  offers in the private chef category, a chef's own kitchen for guests whose rental kitchen
  cannot cope. It will not win search traffic. It will win the visitor who is already on
  the page and unsure.
- **Needs Matt**: how many the Albion kitchen seats, and whether an Albion dinner is priced
  the same. Both questions are already tagged `<!-- CONFIRM -->` in `private-chef.html`.

### Do not build

- **Town-by-town doorway pages.** No `/private-chef-fort-bragg/`,
  `/catering-little-river/`, `/chef-elk-ca/`, `/private-chef-albion/`. Seven towns times
  four services is 28 near-identical pages with nothing to say. `caterer fort bragg` and
  `anderson valley catering` both returned **no autocomplete**, so the demand is not there
  to justify them, and thin doorway pages are the exact pattern Google's site reputation
  and scaled-content guidance targets. Place names belong in body copy, see section E.
- **Sea urchin, uni, mussel or abalone foraging.** `mendocino sea urchin foraging` and
  `mendocino uni foraging` are the strongest foraging autocompletes in the entire set, and
  Matt cannot serve them. CONTEXT.md round 3 is explicit that he forages mushrooms,
  berries, greens and salt, and does not hunt, fish or butcher. Writing this page would be
  inventing a client fact for traffic.
- **Generic recipe posts.** `chanterelle recipe`, `how to cook candy cap mushrooms` and
  similar are national queries against enormous food sites, with no local intent and no
  booking path.
- **A "best private chefs in Mendocino" listicle.** Ranking your own business first in your
  own roundup is transparent, and the format invites comparison with competitors on a page
  you control, which readers discount.
- **A services page listing all four again.** The home page already does this. A second one
  competes with it.
- **Anything about hunting, fishing, line-caught fish or whole-animal cookery.** Standing
  rule from CONTEXT.md round 3.

---

## E. Local modifiers

Seven place names, three tiers. The rule throughout: **place names go in body copy and in
one structured-data field, never into a page of their own.**

### Tier 1, use in titles, h1s, descriptions and schema

| Place | Where it belongs | Evidence |
|---|---|---|
| **Mendocino** | Every page title. Every meta description. The h1 of `/foraging/`, `/private-chef/`, `/catering/` and `/cooking-classes/`, where it already is. The `LocalBusiness` `addressLocality`. | Every confirmed autocomplete phrase in this report contains it |
| **Mendocino coast** | `/` title (proposed), `/foraging/` description, `/private-chef/` title (proposed). The phrase that separates the coastal towns from inland Ukiah and Willits, which matters because Good Earth Kitchen is in Willits. | `best time to visit mendocino coast`, `coastal foraging mendocino`, both confirmed autocomplete |
| **Mendocino County** | `/catering/` title (proposed). The `areaServed` field, already correct in `build.py`. The word that dodges the Mendocino Farms brand collision. | `mendocino county catering`, `private chef mendocino county`, `mushroom foraging mendocino county`, all confirmed autocomplete |

### Tier 2, one sentence of body copy each, no more

| Place | Where it belongs | Evidence |
|---|---|---|
| **Fort Bragg** | `/private-chef/` area line, and `/cooking-classes/` where Living Light already appears. Fort Bragg is the population centre of this coast and the Living Light connection makes the mention genuine rather than stuffed. | `private chef fort bragg ca` confirmed autocomplete |
| **Albion** | `/private-chef/`, where it already is, as the location of Matt's own kitchen. This is a real address fact, which is the only reason to name it. | No search demand. Named for accuracy, not ranking. |
| **Anderson Valley** | One line in the `/catering/` area-served sentence, and only because it is in the stated service area. | `anderson valley catering` returned **no autocomplete**. Do not invest further. |

### Tier 3, name once in the service-area line, and stop

**Little River**, **Elk**. These are in Matt's stated area per CONTEXT.md and belong in a
single "Matt cooks anywhere in the greater Mendocino area, including..." sentence on
`/contact/` and in the footer. Neither produced any autocomplete. Little River is worth
half a thought because Spirit Camp Retreat Center is there
([Spirit Camp](https://www.spirit.camp/retreat-venue-rental-mendocino-california)), which
makes it a retreat-catering mention rather than a search play.

### Named but not targeted

**Sea Ranch** and **Gualala** sit at the southern end of the Mendonoma coast, roughly 50
miles from Mendocino village, and are already served by Sea Ranch Gourmet and Black Oak
Catering. `private chef sea ranch ca` **is** confirmed autocomplete, which makes it
tempting. Resist it beyond one clause in `/private-chef/` body copy. Competing there means
competing away from home.

**North Coast** is a phrase the editorial sites use ("the North Coast") but almost nobody
searches with commercial intent. Fine in prose, worthless in a title.

---

## F. Top 10 actions

Ordered by impact first, then effort. Effort is my estimate of build time, not a quote.

| # | Action | Why | Effort |
|---|---|---|---|
| 1 | **Put "mushroom" into the `/foraging/` title, h1 and description.** Title to "Mushroom Foraging Mendocino \| Guided Days from $300", h1 to "Mushroom foraging days on the Mendocino coast." | The site's biggest keyword miss. Six confirmed autocomplete phrases contain "mushroom"; "foraging excursions" has none. Top of the SERP is six editorial articles and no real service page, which is an open lane. | One hour |
| 2 | **Rewrite all seven titles and descriptions** per the section A table. | Every current title buries the place modifier behind the brand, and no description carries a price. Both competitors that rank locally publish neither prices nor descriptions. | Two hours |
| 3 | **Point the domain at the new site.** `spontaneouscafe.com` still serves the GoDaddy one-pager, titled "Spontaneous Cafe", with no meta description, and it **is indexed**. | Every canonical and the sitemap in `build.py` already point at `spontaneouscafe.com`. Until DNS moves, the Vercel deployment is a crawlable copy whose canonicals point at a domain serving different content. Nothing else in this list compounds until this is done. | Blocked on Matt (DNS) |
| 4 | **Claim the free Yelp profile and finish the Google Business Profile.** | Yelp fills three separate slots across the SERPs run here. The GBP exists ([Maps CID link in CONTEXT.md](https://www.google.com/maps?cid=7343978535458024901)) but the Place ID is not extracted and the review link is not live. Local pack presence beats organic position for every one of these queries. | Half a day, plus GBP verification wait |
| 5 | **Add the four pricing FAQs to `/private-chef/`** (cost per day, cost for a dinner party, personal versus private chef, do you do the dishes). | Every fact is already on the site, `build.py` already emits `FAQPage` JSON-LD from `<details>` blocks, and all four are confirmed autocomplete. Highest ratio of value to work in this report. | One hour |
| 6 | **Build the Mendocino mushroom season calendar page (D1).** | The best link magnet available. Six editorial sites rank for foraging terms today and all of them need a source for seasonal timing. It also answers `best time to visit mendocino`, which is upstream of everything. | Two days, blocked on Matt for the species and months |
| 7 | **Add a retreat catering section to `/catering/` (D4).** | Five confirmed autocomplete retreat phrases, five named venues on this coast that outsource catering, and Matt's resume already covers retreat menus for 20 to 80. The venue is a repeat referrer in a way a wedding couple never is. | Half a day |
| 8 | **Apply to Airbnb Experiences for the foraging day.** | The only marketplace whose audience matches Matt's actual customer, San Francisco weekenders already in Mendocino rentals. Comparable listings run [$225 per guest](https://www.airbnb.com/experiences/6706680) against his $300 for the whole group at three hours. Business decision for Mohammed, presented as an option. | Application plus approval wait |
| 9 | **Get named in the roundups.** Pitch [Edible Mendocino](https://ediblemendocino.com/stories/mendocino-mushroom-foraging-experiences-in-fall-winter-2024-25/), [Visit Mendocino's Walk on the Wild Side](https://www.visitmendocino.com/walk-on-the-wild-side/) (which has a "Submit a Deal or Special" route and names no independent foraging guides), and join the [Mendocino Coast Mushroom Club](https://www.mendocinocoastmushroomclub.org/) (meets monthly Sept to May, Fort Bragg). | On the foraging SERP the editorial pages **are** the competition, and they get their names from somewhere. This is the cheapest route to ranking-adjacent visibility and it also earns real links. | Ongoing, a few hours to start |
| 10 | **Add `Person` schema for Matt to `/about/`, linked to the `LocalBusiness` as `founder`.** | `build.py:68` already emits `LocalBusiness` and per-service `Service` markup, which is ahead of every competitor found (none had schema). Adding `Person` with `alumniOf` / `worksFor` for Living Light, Esalen and Flow binds the name to the business as an entity. `chef matt samuelson` has zero autocomplete today, so this is entity-building for later, not a traffic play. | Two hours |

### Two things deliberately not in the top ten

**The Knot profile.** It would help the catering SERP, where The Knot and Zola dominate.
It is also a real recurring spend and catering is Matt's third priority service. Present it
to Mohammed as a spend question, not an SEO task.

**A `/cooking-classes/` push.** `cooking class mendocino` returns one autocomplete
suggestion and Bing returns none. The page is worth keeping accurate and worth carrying
the Living Light credential. It is not worth a content programme.

---

## Sources

- [7x7, Mushroom Hunting in Mendocino](https://www.7x7.com/tis-the-season-mushroom-hunting-in-mendocino-2084146809.html)
- [7x7, Foraging classes, guided tours and forays](https://www.7x7.com/mushroom-foraging-bay-area-2556316845/foraging-classes-guided-tours-and-forays)
- [Airbnb Experiences, Exclusive Foraging Tours on Private Land](https://www.airbnb.com/experiences/6706680)
- [Airbnb Experiences, Learn to forage wild food with a professional](https://www.airbnb.com/experiences/5510810)
- [Arts Mendocino, Fungi Festival and Cultural Convergence](https://artsmendocino.org/event/fungi-festival-and-cultural-convergence/)
- [CAL FIRE, JDSF mushroom permit packet (PDF)](https://34c031f8-c9fd-4018-8c5a-4159cdff6b0d-cdn-endpoint.azureedge.net/-/media/calfire-website/what-we-do/natural-resource-management/demostration-forests/jackson/recreation-maps-and-permits/mushroom-permit-by-mail-packet2.pdf)
- [CatchNCookCalifornia, Private Foray Mendocino](https://www.catchncookcalifornia.com/event-details/private-foray-coastal-foraging-mendocino)
- [Chef Adair](https://www.chefadair.com/)
- [Chef's Table Catering](https://www.chefstablellc.com/)
- [Edible Mendocino, Mushroom Foraging Experiences](https://ediblemendocino.com/stories/mendocino-mushroom-foraging-experiences-in-fall-winter-2024-25/)
- [Flora & Fungi Adventures, Mendocino](https://www.floraandfungiadventures.com/event-details/mendocino-purple-sea-urchin-mussels-seaweed-extravaganza-4)
- [ForageSF, California mushroom calendar](https://www.foragesf.com/blog/california-mushroom-calendar)
- [Fork In the Path, schedule](https://www.forkinthepath.org/schedule)
- [Good Earth Kitchen, private chef](https://www.goodearthkitchen.net/private-chef)
- [Marin Magazine, Mushroom Foraging in Mendocino](https://marinmagazine.com/travel/local-travel/mushroom-foraging-in-mendocino/)
- [Mendo Insider Tours, Mendocino Mushroom Tours](https://mendoinsidertours.com/mendocino-mushroom-tours/)
- [Mendocino BBQ Catering](https://www.mendocinobbq.com/)
- [Mendocino Coast Mushroom Club](https://www.mendocinocoastmushroomclub.org/)
- [MCMC, Mushrooms of the Mendocino Coast](https://www.mendocinocoastmushroomclub.org/mushrooms-of-the-mendocino-coast.html)
- [MCMC, Fungi Festival 2026](https://www.mendocinocoastmushroomclub.org/fungi-festival-2026.html)
- [Mendocino Farms catering](https://www.mendocinofarms.com/catering)
- [Mendocino Grove, retreats and workshops](https://mendocinogrove.com/retreats-workshops)
- [Mendocino Voice, storms bring mushroom foraging](https://mendovoice.com/2024/11/huge-storms-expected-to-bring-superb-mushroom-foraging-for-those-in-the-know/)
- [Mendoughs Woodfire Pizza](https://mendoughs.com/)
- [Mushroom Tracker, California permits and regulations](https://www.mushroomtracker.ca/blog/mushroom-foraging-california.html)
- [North of Ordinary, Mushroom Feast Mendocino](https://northofordinaryca.com/blog/mushroom-feast-mendocino/)
- [SOMA, mushroom picking rules and regulations](https://www.somamushrooms.org/foraging/rules.php)
- [Spirit Camp Retreat Center, venue rental](https://www.spirit.camp/retreat-venue-rental-mendocino-california)
- [Camp Mendocino, rent camp](https://www.campmendocino.org/rent-camp)
- [Stanford Inn, cooking classes](https://stanfordinn.com/mendocino-oceanview-resort-cooking-classes/)
- [Stanford Inn, Mendocino nature tours](https://stanfordinn.com/mendocino-vacation-packages-tours/)
- [Take a Chef, Mendocino County](https://www.takeachef.com/en-us/private-chef/mendocino-county)
- [The Knot, catering Fort Bragg CA](https://www.theknot.com/marketplace/catering-fort-bragg-ca)
- [The Knot, catering Mendocino CA](https://www.theknot.com/marketplace/catering-mendocino-ca)
- [The Knot, Assaggiare Mendocino](https://www.theknot.com/marketplace/assaggiare-mendocino-fort-bragg-ca-627093)
- [Visit Mendocino, Walk on the Wild Side](https://www.visitmendocino.com/walk-on-the-wild-side/)
- [Whole Body Wellness, healthy cooking classes](https://wbwcenter.com/healthy-cooking-classes/)
- [Wilderfolk, Reading the Mendocino Coast Through the Seasons](https://campcandycap.com/reading-the-mendocino-coast-through-the-seasons/)
- [yhangry, private chefs Mendocino County](https://yhangry.com/f/private-chefs/us-california-mendocino--county)
- [Yelp, caterers near Mendocino 95460](https://www.yelp.com/search?cflt=catering&find_loc=Mendocino%2C+CA+95460)
- [Yelp, personal chefs Mendocino County](https://www.yelp.com/search?cflt=personalchefs&find_loc=Mendocino+County,+CA)
- [Zola, Mendocino wedding catering](https://www.zola.com/wedding-vendors/search/mendocino-ca--wedding-catering--cuisine-types-seafood)
- [Alignable, Spontaneous Cafe](https://www.alignable.com/mendocino-ca/spontaneous-cafe)
- [Whitehorse Brewing, The Spontaneous Cafe w/ Chef Matt](https://www.whbrewing.com/event-details/the-spontaneous-cafe-w-chef-matt)

Autocomplete data collected 2026-09-19 from `suggestqueries.google.com/complete/search`
(45 seeds) and `api.bing.com/osjson.aspx` (10 seeds). Google Trends returned HTTP 429 and
HTTP 400 and is not cited anywhere in this report.
