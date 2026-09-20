# Google Ads plan, The Spontaneous Cafe

Prepared 2026-09-19 by MOSI Consulting. Media buying for Chef Matt Samuelson, Mendocino CA.
Research: four parallel agents on credit mechanics, county search demand, small-budget
campaign structure, and conversion tracking, plus the autocomplete study in
`docs/seo-2026-09-19/R2-keywords-serp.md`. Every external claim in the source briefs
carries a URL.

---

## 1. The budget is not $500

The Google offer is a spend match. Google's coupon terms require campaigns to "accrue
costs of at least [threshold] within 60 days" of redemption before any credit posts, and
state that "making a payment is not sufficient". Real billed spend has to happen first.

**So the shape is: $500 of Matt's cash goes in, which unlocks $500 of credit. Total media
$1,000. Cash at risk $500.**

That halves the effective click price. At the travel and restaurant benchmark of $2.10 to
$2.85 per click, $1,000 of media costs $500 of cash, so the effective CPC is roughly $1.05
to $1.43. For a business selling $300 to $1,000 days, that is a good rate.

### The three clocks

| Clock | Length | Starts |
|---|---|---|
| Redeem the code | 14 days | The account's first ad impression |
| Accrue $500 of real spend | 60 days | Redemption |
| Google validates and posts the match | up to 35 days | The day spend hits $500 |
| Spend the earned credit | 60 days | The day the credit posts |

Miss the 60-day spend window and the promotion flips to Expired with nothing issued.

Two consequences. **The Google Ads account gets created last**, once the site is ready,
because eligibility requires a new account. And the credit lands in a separate window from
the cash, which forces two flights rather than one.

---

## 2. Go / no-go: the volume check

The honest finding from the demand research is that **volume, not click price, is the
binding constraint.** Mendocino County has about 90,000 residents. No keyword tool
publishes a monthly figure for any local chef or foraging query.

What the autocomplete study did establish is which phrases Google itself suggests, which
is evidence that people type them. That evidence is good enough to bid on, and it is the
basis for the keyword list in `keywords.csv`.

**Gate: inside the new account, before scaling spend past $100, pull Keyword Planner
volumes for the phrases in `keywords.csv`.** If the combined searchable volume across the
Bay Area and Mendocino geos cannot absorb $1,000 over the flight, stop and move the cash
to the free and commission-only channels in section 8. Nothing is lost, because the credit
is only unlocked by spending, so unspent cash costs nothing.

### The competing recommendation, stated plainly

The demand research concluded that Search Ads is probably not the strongest $500 available
for a single operator this size, and that Google Business Profile work plus one
commission-only marketplace listing reach more real demand than a cold search campaign.

That conclusion is correct about fungible cash and wrong about this specific $500, for one
reason: the credit can only be spent on Google Ads. The real question is whether $500 of
cash buys more through $1,000 of Google media than through $500 of marketplace commission.
The 2x match tips it, on the condition that the volume gate clears.

**Recommendation: run both.** The GBP and partnership work in section 8 is free and starts
this week regardless. The ads run only if the volume gate clears.

---

## 3. Readiness gate, what ships before a dollar is spent

Audited on disk and live, 2026-09-19.

### Hard blockers

| # | Blocker | Detail |
|---|---|---|
| B1 | **DNS** | Ads would point at `spontaneous-cafe.vercel.app`. Worse, `build.py` writes canonicals and a sitemap pointing at `https://spontaneouscafe.com/`, which still serves the old GoDaddy one-pager. The paid landing page would declare a canonical to a URL with different content. Blocked on Matt. |
| B2 | **No measurement of any kind** | No GA4, no gtag, no Ads conversion tag, no GTM anywhere in `dist/` or `src/`. Spending blind is not a plan. Spec in section 6. |
| B3 | **47 unconfirmed claims** | `<!-- CONFIRM -->` tags across `src/pages` (catering 14, about 10, index 7, foraging 5, private-chef 5, cooking-classes 4, contact 1, privacy 1). They are stripped from production builds, so nothing leaks to a visitor, but the underlying facts are still unverified. Paying to drive strangers to unverified client claims is the one risk I will not carry. Matt's questionnaire answers close this. |
| B4 | **GBP verification state unknown** | The Maps CID does not render server-side. Verification gates the review link, the Map Pack and the local ad assets. Confirm from the dashboard. |

### Conversion fixes, ranked by what they cost and return

1. **Put "mushroom" in the `/foraging/` title and h1.** Today they read "Foraging
   Excursions" and "Foraging days on the Mendocino coast." Six of the seven confirmed
   foraging phrases contain "mushroom". This is the highest-value hour of work in the whole
   plan, because it lifts Quality Score on the largest keyword cluster and lowers CPC on
   every click in it.
2. **Put an enquiry path on the service pages.** The form exists only on `/contact/`.
   Every paid click currently needs an extra navigation before it can convert. Either
   inline the form on `/foraging/` and `/private-chef/`, or add a sticky CTA with the phone
   number visible on mobile.
3. **Make the form shorter.** Nine fields today. Compiled data puts the drop at 20 to 30
   percent per field past five. Keep name, email, date and service required. Mark phone,
   guests and message optional in the label itself.
4. **Repeat the price on the service pages.** The tiers sit on `/contact/` and in the
   select options. A visitor arriving from an ad on `/foraging/` should see $300 without
   scrolling.
5. **Add the four private-chef pricing FAQs** (cost per day, cost for a dinner party,
   personal versus private chef, do you do the dishes). All four are confirmed
   autocomplete, every fact is already on the site, and `build.py` already emits FAQPage
   JSON-LD from `<details>` blocks.

---

## 4. The calendar

Mendocino demand stacks into two windows, and the credit's clocks happen to split the
money across both.

| Window | What is live | Money |
|---|---|---|
| **Nov 1 to Dec 20** | First sustained rains trigger the mushroom flush about ten days later. The Fungi Festival runs Nov 14 to 15, 2026 and lifts branded search across the county. Thanksgiving week fills Bay Area vacation rentals. Christmas and New Year weeks follow. | Flight 1, $500 cash |
| **Jan to Feb** | Mushroom season at peak. Whale season at peak. Lodging at its cheapest, which brings the value traveller. Valentine's drives private dinner enquiries. | Flight 2, $500 credit |

Spending in September or October chases dead intent for the flagship service. The rains
have not started, so there are no mushrooms to forage and no reason for anyone to search.

### Sequence

- **Sept 22 to Oct 24.** Readiness work. Site fixes, GBP, tracking, Matt's questionnaire
  answers, DNS. No ad account exists yet.
- **Oct 26.** Create the Google Ads account, in Expert Mode, from `ads.google.com`.
  Redeem the promo code the same day. Launch.
- **Oct 26 to Dec 20.** Flight 1. Campaign total budget $500 across the flight.
- **Late Dec to late Jan.** Credit validates and posts.
- **Flight 2.** The $500 credit, reallocated on Flight 1's search-terms data.

---

## 5. The media plan

### Settings, all of them

- **Campaign type: Search only.** No Performance Max, no Demand Gen. PMax needs 30 to 50
  conversions a month to calibrate; this account might log three bookings in the whole
  flight. Local Services Ads are not an option at all, because Google's US category list
  has no personal chef, catering, tour guide or tour operator category.
- **Bidding: Manual CPC or Maximize Clicks.** Smart bidding needs 15 to 30 conversions per
  30 days before it beats manual. This flight will not get there.
- **Budget instrument: Campaign total budget.** Google opened this to Search. Set one
  number across a fixed window and Google paces it, and you are never charged more than the
  total. Use it instead of guessing a daily figure.
- **Match types: phrase and exact only.** No broad, for the entire flight.
- **Networks: uncheck Search Partners. Uncheck Display.** Both live at campaign Settings,
  Networks.
- **Location setting: Presence**, not "Presence or interest", on both campaigns.
  "Presence or interest" pulls in anyone anywhere who typed the word Mendocino.
- **AI Max: opt out.** Google is force-migrating Search campaigns this month. Opt-out is
  per-feature inside campaign settings.
- **Auto-apply recommendations: every category off**, at Recommendations, Auto-apply
  settings.

### Structure, two campaigns, four ad groups

**Campaign 1, "Bay Area Planning". $350 (70%).**
Geo, Presence: San Francisco, Marin, Alameda, Contra Costa, San Mateo, Santa Clara,
Sonoma, Napa, Sacramento counties. These are people at home, planning a Mendocino trip.

- *AG1 Mushroom Foraging.* The largest confirmed-demand cluster. Lands on `/foraging/`.
- *AG2 Forage and Dinner.* The bundle nobody else sells. Lands on `/foraging/#dinner`.
- *AG3 Private Chef and Retreats.* Lands on `/private-chef/` and `/catering/`.

**Campaign 2, "In Mendocino Now". $150 (30%).**
Geo, Presence: Mendocino County. These are people already on the coast, often with a
changed plan and a wet forecast.

- *AG4 In Market.* Near-me and same-week intent. Lands on `/contact/`.

Keywords in `keywords.csv`, importable through Google Ads Editor. Negatives in
`negatives.txt`, applied as a shared account-level list on day one.

### Flight 1 carries transactional intent only

The trip-planning cluster ("things to do in mendocino", "rainy day mendocino", "mendocino
winter activities") is the widest pool of potential customers and the site intercepts none
of it. It is also research intent that will not book this week. It stays out of Flight 1,
which has to prove that transactional intent converts. It goes into Flight 2 on credit
money, feeding a remarketing audience.

One angle there is worth naming now. Mushroom season **is** the rainy season. A visitor
searching "rainy day mendocino" is a visitor whose plan just fell through, and a guided
foraging walk is the answer to that search rather than a consolation for it.

---

## 6. Measurement

Nothing about this campaign can be judged without it, so it ships before the account
exists.

**Stack: Google Tag Manager holding two tags.** The Google Ads conversion tag, which feeds
bidding. A GA4 configuration tag, for reporting only, never imported into Ads. Feeding the
same event to Ads natively and through a GA4 import double-counts it.

GTM container goes once into `src/layout.html` after `<head>`, which is the single
template `build.py` wraps every page in, so one edit ships to all eight pages.

**Conversion actions, and the tier each sits in:**

| Signal | Tier | Why |
|---|---|---|
| Form submit success | **Primary** | A real lead. Name, email and date reach Matt's inbox. |
| Call through the Google forwarding number, 60s+ | **Primary** | The duration filter proves a real conversation happened. |
| `tel:` click on the site | Observation only | Proves intent, not that a call connected. |
| `mailto:` click | Observation only | Opens a mail client. No proof anything was sent. |
| Pricing or menu engagement | Observation only | Interest, not a lead. |

The tier split matters more than it looks. Smart bidding spends the entire budget chasing
whatever is marked primary. Mark a `tel:` tap primary and Google optimises for taps.

**The fire point is exact.** The form posts by AJAX and never navigates, so there is no
thank-you URL and the conversion has to be event-based. It goes in the success branch at
`src/assets/js/site.js:415`, beside `form.reset()`.

**Enhanced conversions for leads: yes.** One `gtag('set', 'user_data', ...)` call on data
the form already collects, placed before the event push. Low conversion volume is exactly
when a recovered match matters, because there is so little signal to learn from.

**Consent Mode v2: not required.** Google's EU User Consent Policy states its own scope,
end users in the EEA, the UK or Switzerland. A US-only advertiser can skip it. CCPA's
business thresholds put a sole proprietor well outside its scope; CalOPPA applies and
requires the posted privacy policy that `/privacy/` already carries.

**Call tracking: use a Google forwarding number, in the ad asset only.** Never on the
website, never on the Business Profile. A forwarding number appearing next to Yelp and
Facebook listings that still show (707) 972-6647 creates the citation mismatch that
demonstrably costs Map Pack rank. Call-only ads are being retired, no new ones after
February 2026, so use call assets on standard search ads.

---

## 7. What $500 of cash should return

Ranges, not a forecast. Every input is a benchmark from a different business.

| Step | Range | Basis |
|---|---|---|
| Total media | $1,000 | $500 cash plus $500 matched credit |
| Clicks | 200 to 330 | $2.10 to $2.85 CPC, derated for a new account with no history |
| Enquiries | 10 to 23 | 5 to 7% conversion, travel and restaurant benchmarks |
| Bookings | 3 to 9 | 25 to 40% close on a warm enquiry |
| Revenue | $1,500 to $4,500 | Blended $500 average across the three tiers |

Against $500 of cash that is roughly 3x to 9x. The downside case is real and worth saying
out loud: if county volume is as thin as the demand research suggests, this returns three
enquiries and one booking, and roughly breaks even. That is what the section 2 gate exists
to catch before the money is committed.

---

## 8. The free channel, which starts this week regardless

Whitespark's 2026 model puts Business Profile completeness at about 32% of local ranking
weight and review signals at about 20%, the top two factors. None of this costs money.

1. **Primary category "Personal chef service".** Secondary: Caterer, Cooking school, Tour
   operator. Google has no foraging category.
2. **Service area, not storefront.** Matt works from a home address in Albion and travels
   to clients. Google's guidance is to leave the business location blank and hide the
   address when customers are not served there. An exposed home address on a listing that
   should be hidden is one of the most common suspension triggers.
3. **Products.** Mirror the three tiers, $300 / $500 / $1,000. Free price-transparency
   real estate.
4. **Photos weekly.** Matt's own, not stock.
5. **Posts, one or two a week**, tied to the season.
6. **Q&A seeded** with the same questions `/contact/` already answers.
7. **Reviews, the first ten.** Use the GBP short link, sent personally within a day or two
   of each job. Never pay, discount or incentivise, and never route only the happy
   customers to it. Google strips every review a business collected when it catches
   gating, not only the tainted ones. Extend the existing `api/notify.js` alert to remind
   Matt 48 hours after a job.
8. **Claim the free Yelp profile.** Yelp filled three separate slots across the fourteen
   SERPs run in the keyword study.
9. **Apply to Airbnb Experiences.** The only marketplace whose audience is already Matt's
   customer, San Francisco weekenders in Mendocino rentals. Comparable listings run $225
   per guest against his $300 for the whole group at three hours. Commission only, so no
   cash risk.
10. **Pitch the roundups.** Edible Mendocino and Visit Mendocino's "Walk on the Wild Side"
    both rank for foraging terms and neither names an independent guide. The Mendocino
    Coast Mushroom Club meets monthly, September to May, in Fort Bragg.

Seller ratings on ads need 100+ reviews in the trailing 12 months, so they are a next-year
milestone, not part of this plan.

---

## 9. Handover lockdown

Five settings quietly wreck a small account after whoever built it stops watching.

1. **Auto-apply recommendations.** Tools and Settings, Recommendations, Auto-apply
   settings. Uncheck every item in both bundles.
2. **The yellow Apply banner.** Google cannot auto-apply a budget increase, but one click
   on the Recommendations or Overview tab does it. Matt's rule: never click Apply on a
   banner.
3. **Performance Max nudges.** They live in the same Recommendations feed with no
   permanent off switch. Decline each one.
4. **Ad rotation.** Campaign, Settings, Additional settings. Confirm it reads Optimize.
5. **Networks.** Campaign, Settings, Networks. Confirm Search Partners and Display are
   both still unchecked after any Google-suggested change.

---

## 10. Open questions for Mohammed

1. Whose card goes on the account, and is $500 of cash actually available to put at risk?
   The credit does not exist until that money is spent.
2. Does Matt want wedding work? It changes whether The Knot profile is worth its fee and
   whether catering keywords get budget.
3. Is the Albion home address currently exposed on the Business Profile? This needs
   checking before anything drives traffic to the listing.
4. Matt's questionnaire answers close 47 CONFIRM tags. Which are blocking, and when do
   they land?
5. Resume email `mattsamuelson@yahoo.com` still differs from the site's gmail. One of them
   is the address a paying customer should reach.
