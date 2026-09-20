# R3. Local entity, Google Business Profile, citations and structured data

The Spontaneous Cafe, Chef Matt Samuelson, Mendocino CA. Research run 2026-09-19.
Read-only research. No repo file was edited and no listing, form or review was submitted.
Every external claim carries a URL. Anything not in CONTEXT.md or the brief is tagged **needs Matt**.

## Summary

1. The entity exists in nine places online and only two of them are business listings; the Google Business Profile is live and rated 5.0 from 8 reviews, and everything else is a gap.
2. The profile's category is right (Personal chef service) but its hours say 8 AM to 11 PM seven days, which no appointment business should publish.
3. All eight Google reviews were posted in the same week and one is from the consultant's own account, which is the exact pattern Google's conflict-of-interest policy names.
4. The site's JSON-LD is four disconnected per-page objects with no Person, no `@id` graph and no service area; the rewrite below is one `@graph` that ties Organization, Person, WebSite and four Services together.
5. Google has one URL indexed for spontaneouscafe.com and the old sitemap lists three, one of which (`/privacy-policy`) 404s on the new build because a `vercel.json` redirect is cancelled by `trailingSlash: true`.

---

## A. Entity footprint found

| # | Where | URL | What it says | Conflict with the facts |
|---|---|---|---|---|
| 1 | Old GoDaddy site | https://spontaneouscafe.com/ | `<title>Spontaneous Cafe</title>`, no meta description, `og:locale` = `en_IE`. Phone (707) 972-6647, chefmattsamuelson@gmail.com, "since 2009", "30+ years" foraging, "23 years" teaching. Seven services including forest bathing, farm and ranch tours, interactive dinner parties | Name is "Spontaneous Cafe", the GBP and the new site say "The Spontaneous Cafe". `og:locale` en_IE is a GoDaddy default and is wrong. Service list is wider than the new site's four |
| 2 | Google Business Profile | https://www.google.com/maps?cid=7343978535458024901 | "The Spontaneous Cafe". Category **Personal chef service**. 5.0 from **8 reviews**. Website `spontaneouscafe.com`. Phone (707) 972-6647. **Hours 8 AM to 11 PM, all seven days.** 3 photos. No "Claim this business" control, so it is owner-managed | Hours are a default nobody chose. No street address and no "Serves …" line render in the public Maps embed, so the service area is either unset or not exposed; check the dashboard |
| 3 | Alignable business page | https://www.alignable.com/mendocino-ca/spontaneous-cafe | "Spontaneous Cafe", owner Matt Samuelson, Mendocino CA, category Culinary Services. "15 years of North Coast experience". Services listed: private chef, private event catering **and food truck**, food styling, meal prep, tasting menus. 4 recommendations, one reading "Fantastic chef who throws great parties with music!" | Name without "The". "15 years" against a 2009 start reads as written years ago. **Food truck** appears nowhere in the brief or CONTEXT.md, **needs Matt**. No phone or website field visible |
| 4 | Alignable forum post | https://www.alignable.com/mendocino-ca/forum/13713012-1704837882/matt-samuelson | Matt Samuelson, Chef/Owner, Spontaneous Cafe, Mendocino CA. Posted 11 Jan 2024 | Consistent |
| 5 | Esalen faculty page | https://www.esalen.org/faculty/matt-samuelson | "the founder of **High Vitality Foods** and lead instructor for Living Light Culinary Institute", "20 years experience creating plant-based menus and products, working for numerous Hollywood celebrities and traveling internationally as a chef, consultant and instructor" | **"High Vitality Foods" contradicts the resume's "High Integrity Foods"**, needs Matt. Otherwise it independently corroborates Esalen, Living Light and the LA private work. This is the single most useful third-party page he has |
| 6 | Esalen teacher page, Retreat Guru | https://esalen.secure.retreat.guru/teacher/matt-samuelson/ | Same bio as #5 | Same |
| 7 | LinkedIn | https://www.linkedin.com/in/matt-samuelson-04013b17/ | Indexed title reads "matt samuelson - living light culinary arts institute". LinkedIn answers bots with HTTP 999, so the page body could not be read | Ownership **needs Matt** before it goes in `sameAs` |
| 8 | Facebook | https://www.facebook.com/chefmattsamuelson/ | Name "Matt Samuelson", handle `chefmattsamuelson`. Reads as a personal profile, not a Page | There is no Facebook **Page** for the business. Personal profiles do not appear in local finders |
| 9 | Instagram | https://www.instagram.com/chefmattsamuelson/ | Display name Matt Samuelson, 77 followers, most recent visible post 16 Jan 2024, Threads link. No bio text or website link returned | Dormant, no link back to the site. Ownership **needs Matt** |
| 10 | Yelp | https://www.yelp.com/search?cflt=personalchefs&find_loc=Mendocino,+CA+95460 | Ten personal chefs list for Mendocino. The Spontaneous Cafe is not one of them. Most of the ten are Napa and Sonoma chefs reaching in. Yelp's own footer: "Adding a business to Yelp is always free." | Gap, and an unusually soft category |
| 11 | Visit Mendocino County | https://www.visitmendocino.com/ | No listing. Living Light has one at https://www.visitmendocino.com/listing/living-light-culinary-institute/ , which is a direct precedent for a Fort Bragg culinary business | Gap |
| 12 | Mendocino Coast Chamber | https://mendocinocoast.com/list | Not a member | Gap |
| 13 | Name collision, local | https://en.wikipedia.org/wiki/Matthew_Kammerer | "Chef Matt Mendocino" returns Matthew Kammerer of Harbor House Inn, Elk CA, two Michelin stars, known for foraging | Direct competition for the same query shape, from a far stronger entity |
| 14 | Name collision, national | https://www.whbrewing.com/event-details/the-spontaneous-cafe-w-chef-matt | A **different** "The Spontaneous Cafe" with a "Chef Matt", serving street tacos at Whitehorse Brewing, 824 Diamond St, Berlin, **Pennsylvania**, 23 Feb 2024 | Exact business-name collision in another state. Nothing on that page links to spontaneouscafe.com |
| 15 | Unresolved mention | https://www.facebook.com/groups/mendocinofoodies/posts/490049247233269/ | "Spontaneous cafe at Dijon Seafood & Grill with Chef Matt", in a group named Mendocino Foodies | Venue not confirmed. Given #14 it may be the Pennsylvania operator. **Needs Matt** before it is claimed as his |
| 16 | Background noise | https://hospitalitydesign.com/people/interviews/chef-marcus-samuelsson/ | Marcus Samuelsson absorbs most "Samuelson chef" searches | Low risk, different spelling |

### NAP consistency

Phone and email are consistent everywhere they appear: (707) 972-6647 and chefmattsamuelson@gmail.com. Two things are not consistent:

- **Name.** "Spontaneous Cafe" on the old site and Alignable, "The Spontaneous Cafe" on the GBP and the new site. Settle on **The Spontaneous Cafe**, because the GBP already uses it and the logo wordmark reads that way. Fix Alignable to match.
- **Email.** The resume carries mattsamuelson@yahoo.com; every public listing carries the gmail. Nothing public uses the yahoo address, so the gmail is the live one. Still on the questionnaire.

### Disambiguating from Matthew Kammerer

Kammerer owns the phrase "chef Matt Mendocino" and will keep it. Three moves that do not fight him:

1. Use the **full name plus the business name** as the entity anchor: "Matthew Samuelson" and "The Spontaneous Cafe" together in the `Person` and `Organization` nodes, in the GBP, and in every citation. "Chef Matt" alone is not a claimable identity.
2. Separate the two business shapes. Kammerer is a **restaurant** chef at a fixed address in Elk. Matt is a **service-area** business that travels to the guest. Google reads that difference from the category, the service area and the absence of an address, with no copy involved.
3. Use the Esalen page (#5) as the outside corroboration in `sameAs`. It names Matt Samuelson with a teaching role, which is a fact Kammerer's entity does not share.

The Pennsylvania "Spontaneous Cafe" (#14) is a real risk for a bare `"spontaneous cafe"` query. The defence is the city and the phone in the structured data and in the GBP. Copy will not do it.

---

## B. Google Business Profile: audit and recommendations

### What is on it today

| Field | Live value | Verdict |
|---|---|---|
| Name | The Spontaneous Cafe | Correct. No keywords appended, which is what Google requires: business names may not include "marketing taglines … or service or product information" (https://support.google.com/business/answer/3038177) |
| Primary category | Personal chef service | Correct. Confirmed to exist in the 2026 category set |
| Secondary categories | None visible | Gap |
| Hours | 8 AM to 11 PM, Sat through Fri | **Wrong.** Nobody set these deliberately |
| Website | spontaneouscafe.com | Correct, and it points at the domain that will carry the new site |
| Phone | (707) 972-6647 | Correct |
| Reviews | 5.0, 8 reviews, all posted in the same week | See the flag below |
| Photos | 3 | Thin |
| Address / service area | Neither renders in the public Maps embed | Verify in the dashboard |
| Verification | No "Claim this business" control appears, and the profile is publicly visible | Reads as owner-managed. The dashboard is the only place to confirm the verification badge |

### Two policy flags, in order of seriousness

**1. The review pattern.** Eight reviews, all "a week ago", one from the account "Rayed Wasif". Google's Maps content policy prohibits content arising from "a contractual or consultory relationship, or other professional or personal affiliations that demonstrate a conflict of interest", and separately prohibits reviews "not based on a real experience" (https://support.google.com/contributionpolicy/answer/7400114). A consultant reviewing the client he is building the site for lands inside the first clause whether or not the foraging day happened. A cluster of first-ever reviews inside one week is also the shape Google's spam systems look for. Recommendation: leave them alone rather than deleting in a batch, and from here on take reviews only from paying guests, one at a time, through the review link. If Google filters the cluster, the profile survives; if the profile is suspended, everything below is wasted.

**2. Hours.** Publishing 8 AM to 11 PM daily tells Google and a reader that someone answers at 10 PM on a Tuesday. The fix is the documented one for appointment businesses: Edit profile → Hours → Edit → **"Open with no main hours"**, then set the *Onsite services* and *Online appointments* attributes to Yes (https://www.brightlocal.com/learn/google-business-profile-opening-hours/). Google's own guidance is to publish "regular customer-facing hours of operation" and says businesses with varied hours should not publish a fixed set (https://support.google.com/business/answer/3038177).

Nothing else on the profile violates policy. The name is clean, no keyword stuffing.

### Categories

All of these exist in the 2026 Google category list (4,036 categories, checked against https://localdominator.co/google-business-profile-categories/ and cross-checked against the live profile, which already carries "Personal chef service"):

| Candidate | Exists in 2026 | Use it? |
|---|---|---|
| Personal chef service | Yes | **Primary.** Keep it |
| Caterer | Yes | **Secondary.** The 20 to 350 guest work is genuinely a caterer |
| Cooking class | Yes | **Secondary.** Matches the classes exactly |
| Tour operator | Yes | **Secondary.** The closest thing Google has to a foraging excursion. There is no "foraging", "forager" or "wild food" category at all |
| Cooking school | Yes | Skip. "Cooking class" is the more specific of the two for a one-off booking |
| Culinary school | Yes | Skip. That is Living Light, not him |
| Event planner | Yes | Skip. He cooks the event, he does not plan it |
| Chef | **No such category** | Cannot be used. The only chef-shaped category is Personal chef service |
| Tourist attraction, Hiking guide, Sightseeing tour agency, Farm household tour | Yes | Hold in reserve. "Hiking guide" is arguably closer to a foraging walk than "Tour operator", and "Farm household tour" matches the farm and ranch tours if those come back onto the site. Do not add them now |

Google's rule is "use as few categories as possible to describe your overall core business" and to answer "this business **is** a", not "this business **has** a" (https://support.google.com/business/answer/3038177). Four categories for four genuinely different services is defensible. Do not go past four.

### Service-area setup

Google: "If you don't serve customers at your business address: Remove your address and only enter your service area", "You can have up to 20 service areas", and the whole area should sit inside about two hours' drive (https://support.google.com/business/answer/3038163). Matt has no storefront and no on-site signage, which is Google's own test for a service-area business rather than a storefront.

Enter these six and stop:

```
Mendocino, CA
Fort Bragg, CA
Little River, CA
Albion, CA
Elk, CA
Anderson Valley, CA
```

The Albion home kitchen does not become an address on the profile. Guests who cook there are told at booking.

### Services and Products

Use **Services**, not Products. Services is the surface Google gives service businesses (https://support.google.com/business/answer/9455399), and each entry takes a price and a description. Products is a SKU surface and would read as a shop.

Four service groups, each with the three tiers under it:

| Service | Price field | Description (under 300 characters each) |
|---|---|---|
| Foraging excursion | From $300 | A guided half or full day on the Mendocino coast for mushrooms, berries, greens and beach salt, ending in a meal cooked from what the baskets hold. |
| Private chef dinner | From $300 | A multi-course dinner for one to twelve guests at your home or rental, or at Matt's kitchen in Albion. Menu agreed in advance. Vegan, raw and gluten free all covered. |
| Catering and events | From $300 | Weddings, rehearsal dinners, retreats and reunions from 20 to 350 guests. Seated, family style or grazing. |
| Cooking class | From $300 | Knife skills, kitchen efficiency and building a meal from what the market had that morning. |

Then three tier entries so the rate card is on the profile:

- Three hours, $300
- Six hours, $500
- Twelve hours, $1,000

Google rejects custom service names containing "profanity, gibberish, personal information, prices, or phone numbers", so the price lives in the price field and not in the name (https://support.google.com/business/answer/9455399).

### Attributes to set

- Identifies as: skip unless Matt wants it.
- **Onsite services: Yes.** **Online appointments: Yes** if he takes bookings by the form.
- Payments: whatever he actually takes, **needs Matt**.
- Accessibility attributes: leave blank, there is no venue.
- Service options: no dine-in, no takeout, no delivery. Leave them off rather than answering No where the option exists.

### Description, 742 characters

Google caps the description at 750 characters, bans URLs and HTML, and says not to "Focus on special promotions, prices, and offer sales" (https://support.google.com/business/answer/3039617 and https://support.google.com/business/answer/3038177). So the rate card stays in Services and out of this paragraph.

> The Spontaneous Cafe is Chef Matt Samuelson, cooking on the Mendocino coast since 2009. He forages mushrooms, berries, greens and salt, shops the farm stands and the market, and agrees the menu with you in advance from what is available that week. Four services: foraging excursions, private chef dinners for one to twelve guests at your home or rental or in his kitchen in Albion, catering for events of 20 to 350 guests, and cooking classes on knife skills and kitchen efficiency. Menus can be vegan, raw or gluten free. Matt was head chef and culinary instructor at Living Light in Fort Bragg and executive chef at Flow in Mendocino, and has taught at Esalen. He serves Mendocino, Fort Bragg, Little River, Albion, Elk and Anderson Valley.

Every fact in it is from the resume, CONTEXT.md or the brief. 742 characters counted.

### Posts

Google calls them Updates. They are worth a fortnightly cadence in season and monthly out of it, because each one is a fresh signal on a profile that otherwise never changes and because the Maps AI layer reads them. Six he already has the material for:

1. What is fruiting this week, one photo, two sentences.
2. A dinner that happened, no guest names, one plated photo.
3. The salt harvest, once a season.
4. A farm stand he bought from, named, once a month.
5. An open class date when there is one.
6. The wedding and retreat booking window, once a quarter.

No prices in Updates. No links to anything but the site.

### Q&A: the feature is gone

Do not plan Q&A seeding. Google discontinued the Business Profile Q&A API on **3 November 2025** ("we will be discontinuing the My Business Q&A API as we are in the process of updating the Q&A functionality and user experience", https://developers.google.com/my-business/content/qanda/change-log), and the public Q&A panel has been retired in favour of the Gemini-backed "Ask" experience in Maps (https://www.accrisoft.com/blog/2026/01/28/main/google-removes-business-profile-q-a-what-it-means-and-what-to-do-now/).

What replaces seeding: the answers now get drawn from the profile fields, the reviews and the linked website. That makes two things load-bearing that were optional before. First, the 20 `<details>` FAQ items already on the service pages, which the build already emits as `FAQPage` JSON-LD. Second, the description and Services above. Both are now feeding the Ask panel rather than a rich result. Keep the FAQ markup even though FAQ rich results themselves are retired (https://developers.google.com/search/docs/appearance/structured-data/faqpage).

### Photo plan

JPG or PNG, 10 KB to 5 MB, 720 × 720 recommended, 250 px minimum, "in focus and well lit, and have no significant alterations or excessive use of filters" (https://support.google.com/business/answer/6103862). Three photos is too few for a visual business. Target fifteen, from the real set that arrived on 2026-09-16:

- Logo: the wordmark exported to PNG.
- Cover: the plated dish.
- Two of Matt himself. Only two exist, so both go up.
- Four foraging: forest, mushroom basket, porcini log, salt.
- Three food: plate, table set, pan on flame.
- Two teaching: group cooking.
- Two sourcing: farm stand or market once real ones exist.

Hold back the three photos of other adults and the two of a child, same rule as the site. Hold the rockfish photo, because the copy says fish is bought.

### The review link and a script for Matt

Get the link from the dashboard: **Business Profile → Read Reviews → Get more reviews**, then copy the link or save the QR code (https://support.google.com/business/answer/16816815). Do not hand-build a `writereview` URL; the dashboard link is the one Google supports.

Google permits asking. It prohibits incentives: "Offering incentives, like free or discounted goods or services, in exchange for customers to post reviews … is strictly prohibited", and separately prohibits selectively soliciting only happy customers (https://support.google.com/business/answer/3474122, https://support.google.com/contributionpolicy/answer/7400114). So: ask everyone, offer nothing, and never screen for a rating first.

Text for Matt to send, the day after:

> Hi [name], thanks for having me. If you have a minute, would you leave a review? It is the main way people find me up here. [link] Either way it was good to cook for you. Matt

Two rules with it. Send it to every guest, not the ones he thinks liked it. Send it from his own phone, not in a batch.

---

## C. Citations to create, ordered by value

Ordered by what a Mendocino food and experience business actually gets back. Every URL below was requested on 2026-09-19 and the HTTP status is recorded. "Followed link" was verified by reading the live markup or the platform's own robots.txt where it says **verified**; where it says **not verified**, treat it as unknown rather than assuming.

| # | Platform | Where a listing is created | Status | Cost | Passes a followed link | Fit |
|---|---|---|---|---|---|---|
| 1 | **Bing Places** | https://www.bingplaces.com/ (301s to https://www.bing.com/forbusiness/) | 200 | Free | No web link, it is map data | Second map index, and it feeds Copilot answers. Twenty minutes of work |
| 2 | **Apple Business Connect** | https://businessconnect.apple.com/ (302s to business.apple.com sign-in) | 200 | Free | No web link, it is map data | Every iPhone guest who opens Maps. Supports service-area businesses |
| 3 | **Yelp** | https://biz.yelp.com/ , or "Add business" from https://www.yelp.com/search?cflt=personalchefs&find_loc=Mendocino,+CA+95460 | 200 | Free listing. Yelp Ads are separate and not needed | **No, verified.** The website link renders as `yelp.com/biz_redir?url=…` and `Disallow: /biz_redir` is in https://www.yelp.com/robots.txt | The Mendocino personal-chef category holds ten businesses, most of them Napa and Sonoma chefs reaching in. A genuinely local one would stand out. Highest-value non-Google listing here |
| 4 | **Mendocino Coast Chamber of Commerce** | https://mendocinocoast.com/member/newmemberapp | 200 | **$160/yr "Cottage Industry"**, or $310/yr "Standard Business 1-4 employees". Read from the live application form's own package table. Other tiers: Individual $150, Associate $235, Lodging $330 | **Yes, verified.** A member page links out as `<a href="http://www.gardenbythesea.org" … target="_blank">` with no `rel` (https://mendocinocoast.com/list/member/mendocino-coast-botanical-gardens-710) | The best value on this list. A followed local link plus the membership directory plus the visitor centre on N. Franklin St |
| 5 | **Visit Mendocino County** | No self-serve form exists. Ask via info@visitmendocino.com, 707.964.9010 (https://www.mendocinotourism.org/). Target listing types: https://www.visitmendocino.com/listing_type/tour-operators/ and https://www.visitmendocino.com/listing_type/things-to-do/cooking-classes-things-to-do/ | 200 | Not published. MCTC is funded by a lodging business improvement district, not member dues, so a listing is editorial rather than paid | **Yes, verified.** https://www.visitmendocino.com/listing/living-light-culinary-institute/ links out as `<a href="http://www.rawfoodchef.com" target="_blank">` with no `rel` | The strongest link in the county for a visitor business, and Living Light already has a listing, which is the precedent to cite in the email. Also free self-serve routes for events (https://www.visitmendocino.com/events/) and deals (https://www.visitmendocino.com/submit-a-deal-or-special/) |
| 6 | **Facebook Page** | https://www.facebook.com/pages/create | 400 to bots, works in a browser | Free | No, Facebook nofollows outbound links. **Not verified this run** | There is no Page today, only a personal profile. A Page is the container for events, the booking button and the photo set. Needs an hour |
| 7 | **Instagram professional account** | Convert the existing https://www.instagram.com/chefmattsamuelson/ in the app | 200 | Free | No, nofollow. **Not verified this run** | The account exists with 77 followers and has been dormant since Jan 2024. Converting it and adding the site link costs nothing |
| 8 | **Nextdoor Business Page** | https://business.nextdoor.com/en-us/small-business | 200 | Free page. Local Deals and ads are paid | **Not verified** | Weekenders do not read Nextdoor, but the property managers and rental owners who refer him do |
| 9 | **Tripadvisor, Things to Do** | https://www.tripadvisor.com/Owners | 403 to bots, works in a browser | Basic listing free | **No, verified by robots.txt.** `Disallow: /ExternalLinkInterstitial` and six other redirectors in https://www.tripadvisor.com/robots.txt | High tourist intent for foraging. Tripadvisor pushes experiences toward bookable inventory, which in practice means Viator, so expect this to be gated behind #10. Worth an attempt as an attraction first |
| 10 | **Viator supplier** | https://supplier.viator.com/ | 403 to bots | Commission per booking. **Rate not verified this run** | No | The route into Tripadvisor's Things to Do inventory. Only worth it if the foraging day becomes a fixed-price, fixed-duration, publicly bookable product. That is a business decision, **needs Matt** |
| 11 | **The Knot** | https://www.theknot.com/marketplace/join-us | 403 to bots | Paid, quoted on application. **Price not verified this run** | **Not verified** | Wedding catering only. Mendocino wedding volume is real but the storefront cost has to be earned back by one booking. Defer until the catering page has photos of an actual event |
| 12 | **WeddingWire** | https://vendors.weddingwire.com/ | 403 to bots | Paid, same company as The Knot since the 2018 XO Group merger, usually one storefront across both. **Not verified this run** | **Not verified** | Same call as #11. Do not buy both separately |
| 13 | **Eventbrite** | https://www.eventbrite.com/organizer/overview/ | 200 | Free to create; fees apply on paid tickets | **Not verified** | Only if classes go on sale as scheduled public dates. Until then it is an empty page |
| 14 | **Airbnb Experiences** | https://www.airbnb.com/host/experiences | 200 | Host service fee per booking. **Rate not verified this run** | No | The guest is already on Airbnb booking the rental the dinner will happen in, which is the strongest intent match on this whole list. Also the heaviest lift: fixed price, fixed itinerary, Airbnb's cut |
| 15 | **Thumbtack** | https://www.thumbtack.com/pro/ | 200 | Pay per lead. **Rate not verified this run** | **Not verified** | Wrong shape. It is a cheap-quote marketplace and he is a $300 to $1,000 booking |
| 16 | **Bark** | https://www.bark.com/ (the `/en/us/for-business/` path 404s) | 404 on the quoted path | Credit packs | **Not verified** | Skip. Lead quality is poor and the credit model burns money |
| 17 | **Foursquare** | https://foursquare.com/venue/claim | 200 | Free | **Not verified** | Low direct value, but it still feeds some downstream data aggregators |
| 18 | **Yellowpages** | https://www.yellowpages.com/ | 403 to bots | Free tier exists | **Not verified** | Last. Do it only if there is a spare hour |

Six unverified prices sit in that table. They are unverified because The Knot, WeddingWire, Tripadvisor, Viator, Thumbtack and Yellowpages all refuse automated requests, and none of them publishes a price list a bot can read. Every one of them quotes on application. Treat the "cost" column for rows 10 to 18 as a prompt to ask, not as a figure.

**Do the first five and stop.** Rows 1 to 5 are free or $160, all resolve, and two of them pass a followed link. Rows 6 and 7 cost nothing but Matt's time. Everything from row 9 down is a business decision about productising the foraging day, and that decision has not been made.

---

## D. Proposed JSON-LD

### What is wrong with `jsonld()` today

`build.py` lines 68 to 106 emit one of two disconnected objects per page:

- Service pages get a `Service` whose `provider` is an inline `LocalBusiness` with no `@id`. Five pages therefore declare five separate, unlinkable copies of the same business.
- Other pages get a `LocalBusiness` with a `sameAs` of one URL, a four-decimal `geo`, `priceRange: "$$$"`, and `areaServed` as a single string.
- There is no `Person` anywhere, so the one genuinely distinctive entity on the site is invisible.
- There is no `hasMap`, no `openingHoursSpecification`, no `WebSite`, no `@id` graph.

### Type choice

Google: "Use the most specific `LocalBusiness` sub-type possible" (https://developers.google.com/search/docs/appearance/structured-data/local-business). The candidates fail for concrete reasons:

- **`Caterer` does not exist in schema.org.** https://schema.org/Caterer returns 404. Anyone recommending it is guessing.
- **`FoodEstablishment`** exists and is a direct `LocalBusiness` child, but every one of its subtypes is a venue you walk into (Restaurant, Bakery, CafeOrCoffeeShop). Declaring it invites Google to look for a menu, opening hours and a reservation surface that a service-area chef does not have.
- **`LocalBusiness`** is therefore the honest node type. The specificity that `Caterer` would have carried goes into `additionalType` (three resolvable Product Ontology URIs, all checked 200) and into four named `Service` nodes.

One constraint to be clear-eyed about: Google's local business rich result lists `address` as **required**, with street address and postal code. A service-area business with no public address is unlikely to win that rich result. The markup below is not chasing it. Its job is entity resolution, which is what feeds the knowledge panel, the Maps AI answers and the disambiguation from Kammerer.

### Two values that need Matt

- **`openingHoursSpecification`** below says Monday to Sunday, 09:00 to 18:00. Those are the hours he answers the phone, and nobody has asked him. **Needs Matt.** Whatever he says goes in both here and in the GBP. Do not mirror the current 8 AM to 11 PM.
- **`sameAs`** contains only the three URLs verified as his: the Maps profile, the Alignable business page and the Esalen faculty page. The LinkedIn, Facebook and Instagram URLs are commented in the notes below and go in only after Matt confirms he owns them.

### The graph

Emit this once per page, from a rewritten `jsonld()`. The `Organization`, `Person`, `WebSite` and four `Service` nodes are identical on every page; only the trailing `WebPage` node changes.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://spontaneouscafe.com/#website",
      "url": "https://spontaneouscafe.com/",
      "name": "The Spontaneous Cafe",
      "inLanguage": "en-US",
      "publisher": { "@id": "https://spontaneouscafe.com/#business" }
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://spontaneouscafe.com/#business",
      "name": "The Spontaneous Cafe",
      "alternateName": "Spontaneous Cafe",
      "additionalType": [
        "http://www.productontology.org/id/Personal_chef",
        "http://www.productontology.org/id/Catering",
        "http://www.productontology.org/id/Foraging"
      ],
      "url": "https://spontaneouscafe.com/",
      "mainEntityOfPage": { "@id": "https://spontaneouscafe.com/#website" },
      "description": "Chef Matt Samuelson forages, shops and cooks on the Mendocino coast. Foraging excursions, private chef dinners, catering and cooking classes, by the hour block, anywhere in the greater Mendocino area.",
      "slogan": "Local, organic, wild",
      "foundingDate": "2009",
      "founder": { "@id": "https://spontaneouscafe.com/#matt" },
      "employee": { "@id": "https://spontaneouscafe.com/#matt" },
      "telephone": "+1-707-972-6647",
      "email": "chefmattsamuelson@gmail.com",
      "priceRange": "$300 to $1,000 per booking",
      "currenciesAccepted": "USD",
      "image": [
        "https://spontaneouscafe.com/assets/img/plate.jpg",
        "https://spontaneouscafe.com/assets/img/mushrooms-basket.jpg",
        "https://spontaneouscafe.com/assets/img/matt-kitchen.jpg"
      ],
      "logo": {
        "@type": "ImageObject",
        "url": "https://spontaneouscafe.com/assets/logo/wordmark.png",
        "width": 1024,
        "height": 368
      },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Mendocino",
        "addressRegion": "CA",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 39.30770,
        "longitude": -123.79950
      },
      "hasMap": "https://www.google.com/maps?cid=7343978535458024901",
      "areaServed": [
        { "@type": "City", "name": "Mendocino", "@id": "https://spontaneouscafe.com/#area-mendocino", "containedInPlace": { "@type": "AdministrativeArea", "name": "Mendocino County, California" } },
        { "@type": "City", "name": "Fort Bragg", "@id": "https://spontaneouscafe.com/#area-fort-bragg", "containedInPlace": { "@type": "AdministrativeArea", "name": "Mendocino County, California" } },
        { "@type": "City", "name": "Little River", "@id": "https://spontaneouscafe.com/#area-little-river", "containedInPlace": { "@type": "AdministrativeArea", "name": "Mendocino County, California" } },
        { "@type": "City", "name": "Albion", "@id": "https://spontaneouscafe.com/#area-albion", "containedInPlace": { "@type": "AdministrativeArea", "name": "Mendocino County, California" } },
        { "@type": "City", "name": "Elk", "@id": "https://spontaneouscafe.com/#area-elk", "containedInPlace": { "@type": "AdministrativeArea", "name": "Mendocino County, California" } },
        { "@type": "AdministrativeArea", "name": "Anderson Valley", "@id": "https://spontaneouscafe.com/#area-anderson-valley", "containedInPlace": { "@type": "AdministrativeArea", "name": "Mendocino County, California" } }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
          "opens": "09:00",
          "closes": "18:00"
        }
      ],
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "Bookings and enquiries",
        "telephone": "+1-707-972-6647",
        "email": "chefmattsamuelson@gmail.com",
        "areaServed": "US",
        "availableLanguage": "English"
      },
      "knowsLanguage": "en",
      "sameAs": [
        "https://www.google.com/maps?cid=7343978535458024901",
        "https://www.alignable.com/mendocino-ca/spontaneous-cafe",
        "https://www.esalen.org/faculty/matt-samuelson"
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Services",
        "itemListElement": [
          { "@type": "Offer", "itemOffered": { "@id": "https://spontaneouscafe.com/foraging/#service" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://spontaneouscafe.com/private-chef/#service" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://spontaneouscafe.com/catering/#service" } },
          { "@type": "Offer", "itemOffered": { "@id": "https://spontaneouscafe.com/cooking-classes/#service" } }
        ]
      }
    },
    {
      "@type": "Person",
      "@id": "https://spontaneouscafe.com/#matt",
      "name": "Matthew Samuelson",
      "alternateName": "Chef Matt Samuelson",
      "givenName": "Matthew",
      "familyName": "Samuelson",
      "jobTitle": "Chef",
      "description": "Chef, forager and culinary instructor on the Mendocino coast. Head chef and culinary instructor at Living Light Culinary Arts Institute in Fort Bragg across 2000 to 2004, 2008 to 2009 and 2017 to 2019. Executive chef at Flow Restaurant and Lounge in Mendocino, 2015 to 2017. Senior R&D chef at Alive & Radiant Foods, 2011 to 2015. Co-founder of High Integrity Foods since 2006. Personal chef on the film Transsiberian, 2006 to 2007. Settled in Mendocino in 2009 and founded The Spontaneous Cafe.",
      "url": "https://spontaneouscafe.com/about/",
      "mainEntityOfPage": { "@id": "https://spontaneouscafe.com/about/#webpage" },
      "image": "https://spontaneouscafe.com/assets/img/matt.jpg",
      "worksFor": { "@id": "https://spontaneouscafe.com/#business" },
      "hasOccupation": {
        "@type": "Occupation",
        "name": "Chef",
        "occupationLocation": { "@type": "AdministrativeArea", "name": "Mendocino County, California" }
      },
      "affiliation": [
        { "@type": "Organization", "name": "Living Light Culinary Arts Institute", "url": "https://www.golivinglight.com/" },
        { "@type": "Organization", "name": "Esalen Institute", "url": "https://www.esalen.org/" },
        { "@type": "Organization", "name": "High Integrity Foods" }
      ],
      "knowsAbout": [
        "Foraging",
        "Wild mushrooms",
        "Wild edible plants",
        "Farm to table cooking",
        "Plant-based cuisine",
        "Menu development",
        "Catering",
        "Culinary instruction"
      ],
      "sameAs": [
        "https://www.esalen.org/faculty/matt-samuelson"
      ]
    },
    {
      "@type": "Service",
      "@id": "https://spontaneouscafe.com/foraging/#service",
      "name": "Foraging excursions",
      "serviceType": "Foraging excursion",
      "url": "https://spontaneouscafe.com/foraging/",
      "description": "A guided day on the Mendocino coast for wild mushrooms, berries, greens and beach salt, ending in a meal cooked from what the baskets hold.",
      "provider": { "@id": "https://spontaneouscafe.com/#business" },
      "areaServed": [
        { "@id": "https://spontaneouscafe.com/#area-mendocino" },
        { "@id": "https://spontaneouscafe.com/#area-fort-bragg" },
        { "@id": "https://spontaneouscafe.com/#area-little-river" },
        { "@id": "https://spontaneouscafe.com/#area-albion" },
        { "@id": "https://spontaneouscafe.com/#area-elk" },
        { "@id": "https://spontaneouscafe.com/#area-anderson-valley" }
      ],
      "offers": [
        { "@type": "Offer", "name": "Three hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 300, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 3, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Six hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 500, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 6, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Twelve hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 1000, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 12, "unitCode": "HUR" } } }
      ]
    },
    {
      "@type": "Service",
      "@id": "https://spontaneouscafe.com/private-chef/#service",
      "name": "Private chef",
      "serviceType": "Private chef service",
      "url": "https://spontaneouscafe.com/private-chef/",
      "description": "Multi-course dinners for one to twelve guests at your home or rental in the greater Mendocino area, or at Matt's kitchen in Albion. Vegan, raw and gluten free menus included.",
      "provider": { "@id": "https://spontaneouscafe.com/#business" },
      "areaServed": [
        { "@id": "https://spontaneouscafe.com/#area-mendocino" },
        { "@id": "https://spontaneouscafe.com/#area-fort-bragg" },
        { "@id": "https://spontaneouscafe.com/#area-little-river" },
        { "@id": "https://spontaneouscafe.com/#area-albion" },
        { "@id": "https://spontaneouscafe.com/#area-elk" },
        { "@id": "https://spontaneouscafe.com/#area-anderson-valley" }
      ],
      "offers": [
        { "@type": "Offer", "name": "Three hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 300, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 3, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Six hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 500, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 6, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Twelve hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 1000, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 12, "unitCode": "HUR" } } }
      ]
    },
    {
      "@type": "Service",
      "@id": "https://spontaneouscafe.com/catering/#service",
      "name": "Catering and events",
      "serviceType": "Catering",
      "url": "https://spontaneouscafe.com/catering/",
      "description": "Weddings, rehearsal dinners, retreats and reunions from 20 to 350 guests in the greater Mendocino area. Seated, family style or grazing.",
      "provider": { "@id": "https://spontaneouscafe.com/#business" },
      "areaServed": [
        { "@id": "https://spontaneouscafe.com/#area-mendocino" },
        { "@id": "https://spontaneouscafe.com/#area-fort-bragg" },
        { "@id": "https://spontaneouscafe.com/#area-little-river" },
        { "@id": "https://spontaneouscafe.com/#area-albion" },
        { "@id": "https://spontaneouscafe.com/#area-elk" },
        { "@id": "https://spontaneouscafe.com/#area-anderson-valley" }
      ],
      "offers": [
        { "@type": "Offer", "name": "Three hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 300, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 3, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Six hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 500, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 6, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Twelve hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 1000, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 12, "unitCode": "HUR" } } }
      ]
    },
    {
      "@type": "Service",
      "@id": "https://spontaneouscafe.com/cooking-classes/#service",
      "name": "Cooking classes",
      "serviceType": "Cooking class",
      "url": "https://spontaneouscafe.com/cooking-classes/",
      "description": "Knife skills, kitchen efficiency and building a meal out of what the market had that morning, in your kitchen or Matt's.",
      "provider": { "@id": "https://spontaneouscafe.com/#business" },
      "areaServed": [
        { "@id": "https://spontaneouscafe.com/#area-mendocino" },
        { "@id": "https://spontaneouscafe.com/#area-fort-bragg" },
        { "@id": "https://spontaneouscafe.com/#area-little-river" },
        { "@id": "https://spontaneouscafe.com/#area-albion" },
        { "@id": "https://spontaneouscafe.com/#area-elk" },
        { "@id": "https://spontaneouscafe.com/#area-anderson-valley" }
      ],
      "offers": [
        { "@type": "Offer", "name": "Three hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 300, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 3, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Six hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 500, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 6, "unitCode": "HUR" } } },
        { "@type": "Offer", "name": "Twelve hours", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 1000, "priceCurrency": "USD", "referenceQuantity": { "@type": "QuantitativeValue", "value": 12, "unitCode": "HUR" } } }
      ]
    },
    {
      "@type": "WebPage",
      "@id": "https://spontaneouscafe.com/about/#webpage",
      "url": "https://spontaneouscafe.com/about/",
      "name": "About Matt | The Spontaneous Cafe, Mendocino",
      "description": "Matt Samuelson cooked at yoga retreats in Peru, in Thailand and India, and privately in Los Angeles. He taught at Living Light in Fort Bragg, settled in Mendocino in 2009 and studied foraging there.",
      "isPartOf": { "@id": "https://spontaneouscafe.com/#website" },
      "about": { "@id": "https://spontaneouscafe.com/#matt" },
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://spontaneouscafe.com/assets/img/matt-kitchen.jpg"
      },
      "inLanguage": "en-US"
    }
  ]
}
```

### Build notes for whoever implements it

- The last node is the only per-page part. On `/foraging/` it becomes `@id` `…/foraging/#webpage`, `about` points at `…/foraging/#service`, and so on. On `/` it becomes `…/#webpage` with `about` pointing at `#business`.
- Keep `faq_jsonld()` exactly as it is. It emits a second `<script>` and that is fine; two scripts on a page are valid and Google merges them.
- `logo` points at `wordmark.png`, which **does not exist yet**. `src/assets/logo/` holds SVG only. Google's logo requirements are 112 × 112 minimum in a format Google Images supports, and SVG is not on that list (https://developers.google.com/search/docs/appearance/structured-data/logo). Export a PNG from `wordmark.svg` before shipping this, or drop the `logo` property.
- `geo` gains a fifth decimal because Google asks for at least five. The coordinates are the Mendocino town centre, not Matt's address, which is correct for a service-area business.
- `address` deliberately carries no `streetAddress` and no `postalCode`. Google lists `address` as required and wants it complete, so this markup will probably not win the local rich result. That is the right trade for a business with no public address, and it matches what the GBP will show.
- `priceRange` moves from `"$$$"` to `"$300 to $1,000 per booking"`. Google allows any text under 100 characters, and a real figure is worth more than three dollar signs to a Maps AI answer.
- `sameAs` gains the LinkedIn, Facebook Page and Instagram URLs only after Matt confirms ownership. The `Person.sameAs` gains the LinkedIn URL on the same condition.
- Validate with the Rich Results Test and the Schema Markup Validator before merging.

---

## E. E-E-A-T and reviews

### What Google actually asks for

Google's helpful-content guidance frames this as who, how and why, and says **"trust is most important"** of the four (https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Two questions from that page apply directly:

- "Is it self-evident to your visitors who authored your content?"
- "Does your content clearly demonstrate first-hand expertise and a depth of knowledge?"

For a solo chef the "who" is the whole asset. Everything below turns it into something a machine can read.

### What the site already does right

- The About page is a dated career history. Job titles with years attached are exactly the "first-hand expertise" evidence the guidance asks for.
- Copy is first person on About and in FAQ answers, so authorship is obvious without a byline widget.
- Two guest quotes exist, both attributed to a role rather than a name ("Private dinner guest, Mendocino rental"), and neither is marked up as a `Review`. That is correct, and it must stay correct. See below.
- Real photos of Matt and of his own food landed on 2026-09-16, replacing eleven stock images. First-party photography is the cheapest experience signal there is.

### What to add

1. **A `Person` node in the structured data.** Section D. Without it, no machine reads "Matthew Samuelson" as an entity with a teaching history.
2. **Link the About page to the outside corroboration.** The Esalen faculty page names him with a role. One outbound link from `/about/` to it, plus the `sameAs`, turns a claim into a citation.
3. **Date the experience claims.** "More than thirty years" of foraging on `/foraging/` is a bare assertion. "Foraging on this coast since 2009, cooking professionally since the 1990s" is checkable against the same resume the About page already uses. The exact start year is **needs Matt**.
4. **Say what he does not do.** The copy already avoids hunting, fishing and butchering per the round-3 rules. State it once on `/foraging/`: meat and fish are bought. A practitioner naming the edge of his own practice reads as expertise; a page that claims everything reads as marketing.
5. **Named reviews, off-site.** Every review lives on Google, Yelp and the Chamber page. None of them lives in the site's markup.

### Self-serving Review and AggregateRating markup: not allowed

This is unambiguous. Google's review snippet documentation:

> "If the entity that's being reviewed controls the reviews about itself, their pages that use `LocalBusiness` or any other type of `Organization` structured data are ineligible for star review feature."

and it names the case exactly: reviews about entity A appearing on entity A's own site, "either directly in structured data or through embedded third-party widgets" including Google Business reviews and Facebook reviews (https://developers.google.com/search/docs/appearance/structured-data/review-snippet). The local business page repeats it: `aggregateRating` and `review` are "only recommended for sites that capture reviews about other local businesses" (https://developers.google.com/search/docs/appearance/structured-data/local-business).

So: **no `Review`, no `AggregateRating`, no star markup on spontaneouscafe.com**, and no embedded Google or Facebook review widget either, because the embed is covered by the same rule. The current `jsonld()` does not emit any, which is the right starting point.

What to do instead, in order:

1. Put the reviews where they count, on the Google profile, through the review link.
2. Show the quotes on the site as plain HTML `<blockquote>`, which is what the two existing ones already are. Human readers get the proof, Google gets no false rating signal.
3. Get real names on them. "Sarah T., San Francisco, private dinner, October 2026" is worth more to a reader than an anonymous superlative, and it costs one email. **Needs Matt** to ask the guests.
4. When there are enough, link the phrase "reviews on Google" to the Maps profile from the Contact page. One outbound link, no widget, no markup.

---

## F. Old-site index and the cutover

### What Google has now

A `site:spontaneouscafe.com` search returns **one URL**: the homepage, titled **"Spontaneous Cafe"**. The old site itself declares three indexable URLs in https://spontaneouscafe.com/sitemap.xml , which chains to `sitemap.website.xml`:

```
https://spontaneouscafe.com/            lastmod 2023-10-16
https://spontaneouscafe.com/foraging    lastmod 2023-10-16
https://spontaneouscafe.com/privacy-policy  lastmod 2023-10-16
```

The old `robots.txt` is `User-agent: * / Disallow: /404`. Nothing is blocked. The old page has no meta description and carries `og:locale` `en_IE`, a GoDaddy default.

### What the cutover means

This is not a domain migration. The domain does not change, the URLs mostly do not change, and only the content behind them changes. Google treats that as a normal recrawl, not a site move, so there is no Change of Address to file and no cross-domain redirect map to build. The homepage keeps whatever authority it has; it simply gets re-evaluated.

Three specifics:

**1. `/foraging` survives. `/privacy-policy` does not, and the existing fix is broken.**

`vercel.json` already contains `{ "source": "/privacy-policy", "destination": "/privacy/", "permanent": true }`. It never fires. With `"trailingSlash": true`, Vercel first 308s `/privacy-policy` to `/privacy-policy/`, and the redirect rule does not match the slashed form. Verified on staging:

```
GET /privacy-policy  -> 308  Location: /privacy-policy/
GET /privacy-policy/ -> 404
```

Fix: change the source to `/privacy-policy/`, or list both forms. `/foraging` is fine; it 308s to `/foraging/` and serves 200.

**2. The staging host is crawlable.** https://spontaneous-cafe.vercel.app/robots.txt is `Allow: /` with a sitemap pointing at the production domain, and there is no `X-Robots-Tag` header. The canonical tags all point at `spontaneouscafe.com`, which usually keeps the staging host out of the index, and `site:spontaneous-cafe.vercel.app` currently returns nothing. Low risk, cheap to close: add an `X-Robots-Tag: noindex` header for the `.vercel.app` host in `vercel.json` once DNS is live.

**3. The title changes from "Spontaneous Cafe" to "The Spontaneous Cafe | Chef Matt Samuelson, Mendocino".** That is the index entry the one currently-indexed URL will be replaced with, so expect the brand SERP to look different within a week or two of recrawl.

### Search Console, in order, after DNS flips

1. Verify the **domain property** `spontaneouscafe.com` (DNS TXT record), not the URL-prefix property. A domain property covers http, https, www and non-www in one place.
2. Submit `https://spontaneouscafe.com/sitemap.xml`. The build writes it, and it lists all eight live URLs with real `lastmod` dates pulled from git.
3. Use **URL Inspection → Request indexing** on the homepage and on the four service pages. Google's note: "there's a quota for submitting individual URLs and requesting a recrawl multiple times for the same URL won't get it crawled any faster", and "Crawling can take anywhere from a few days to a few weeks" (https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl). Five URLs, once each, then leave it.
4. Do **not** file a Change of Address. Same domain.
5. Watch the Pages report for `/privacy-policy` showing up as a 404 with a referring sitemap. If the old GoDaddy sitemap keeps being fetched, that is the signal the redirect fix did not ship.
6. Two weeks later, check Performance for the brand query `spontaneous cafe` and confirm the new title is what renders.

---

## G. Top 10 actions

Ordered by impact first, effort second.

| # | Action | Owner | Why it is here |
|---|---|---|---|
| 1 | Point `spontaneouscafe.com` DNS at Vercel | **Matt** | Every other item on this list writes into a profile, a citation or a schema graph that points at this domain. Until it serves the new site, all of it advertises a 2023 GoDaddy page |
| 2 | Set GBP hours to "Open with no main hours", confirm the address is hidden, and enter the six service areas (Mendocino, Fort Bragg, Little River, Albion, Elk, Anderson Valley) | **Mohammed** | Fixes the one published falsehood on the profile and turns on the service-area behaviour a no-storefront business needs. Fifteen minutes |
| 3 | Stop taking reviews from anyone connected to the business, and start sending the review-request text to real guests | **Mohammed** + **Matt** | Eight reviews in one week, one from the consultant's account, sits inside Google's conflict-of-interest clause. A suspended profile costs more than every other item here combined |
| 4 | Add the three secondary GBP categories (Caterer, Cooking class, Tour operator), the four Services with the three price tiers, and the 742-character description | **Mohammed** | Three of the four revenue lines are currently invisible to Google. This is also what the Maps AI panel reads now that Q&A is gone. Thirty minutes |
| 5 | Replace `jsonld()` with the `@graph` in section D | **site code** | Turns five disconnected objects into one entity graph with a Person, a service area and a map link. Also the main defence against the Kammerer and Pennsylvania name collisions |
| 6 | Fix the `/privacy-policy` redirect in `vercel.json` (source must be `/privacy-policy/`), and add `X-Robots-Tag: noindex` for the `.vercel.app` host | **site code** | One of the three URLs Google knows about will 404 on launch day. Ten minutes, and the current rule silently does nothing |
| 7 | Join the Mendocino Coast Chamber at the $160 Cottage Industry tier and create the member listing | **Mohammed** | The only verified followed link available for $160, plus the visitor centre on N. Franklin Street. Members' outbound links carry no `rel` |
| 8 | Email info@visitmendocino.com asking for a listing under Tour Operators and Cooking Classes, citing Living Light's existing listing as the precedent | **Mohammed** | The strongest county link for a visitor business, verified followed, and free. No self-serve form exists, so it takes a human asking |
| 9 | Create the free listings, in this order: Bing Places, Apple Business Connect, Yelp, a Facebook **Page**, and convert the Instagram account to professional with the site link | **Mohammed** | All free, all resolve, and Yelp's Mendocino personal-chef category is thin enough that a genuinely local listing stands out. Two hours total |
| 10 | Answer the four open facts: High Integrity vs High Vitality Foods, the hours he actually answers the phone, whether the LinkedIn, Facebook and Instagram accounts are his, and whether the Alignable "food truck" line is real | **Matt** | Four of them block the description, the `sameAs` array, the `openingHoursSpecification` and the Alignable cleanup. None takes more than a sentence to answer |
