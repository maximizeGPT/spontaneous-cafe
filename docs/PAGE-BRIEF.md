# Page brief for writers

Read CONTEXT.md first. Then src/pages/index.html: it is the reference for tone, structure and the component classes. Read src/assets/css/site.css for every class you may use. Do not invent classes; do not add inline styles beyond what index.html already does.

## File format
Each page is src/pages/<slug>.html:

    <!--meta
    {"title": "...", "description": "...", "og_image": "<poster>.jpg", "service": "<service name, service pages only>"}
    -->
    <section ...>...</section>

No <html>, <head>, <body>, header, footer. The layout wraps it. Title format: "<Page name> | The Spontaneous Cafe, Mendocino". Description 140 to 160 chars, plain, names Mendocino.

## Voice
First person, Matt speaking. Plain, specific, warm, unhurried. Short sentences mixed with a few long ones. He states facts and lets the reader conclude. No exclamation marks. No rhetorical questions as openers.

Banned, per Mohammed's writing rules: em dashes; "not X, it's Y" constructions; claim-then-restate; aphorisms; groups of three by default; trailing participial clauses; Furthermore/Moreover/Additionally; the words delve, leverage, robust, seamless, landscape, realm, tapestry, testament, crucial, pivotal, underscore, navigate (figurative), "it's worth noting"; false agency ("the forest offers", "the season decides"); "serves as", "boasts", "features". Specific facts beat adjectives. Vary sentence length hard.

## Components (from site.css), use what fits
- .hero with .hero__media video (data-hero autoplay muted loop playsinline preload="metadata" poster) + .hero__scrim + .wrap > .hero__inner (.eyebrow, h1 with at most one <span class="hand">word</span>, .lede, .hero__actions with .btn and .btn--light). Use .hero--short on service pages.
- .section (+ --paper, --deep, --green), .wrap, .section-head (.eyebrow, h2, .lede), .split / .split--flip, .stack, .grid-2/3, .measure, .link-arrow
- .day ordered timeline (li.day__step, .day__time, h3, p) for an itinerary
- .menu sample menu (.menu__stamp "sample", .menu__head, .menu__courses > .course (.course__label, h4, p), .menu__foot)
- Seasonal menus: wrap in <div data-tabs>: <div class="tabs" role="tablist"><button role="tab" data-season="spring" aria-selected="false" id="t-spring" aria-controls="p-spring">Spring</button>...</div> then <div role="tabpanel" id="p-spring" aria-labelledby="t-spring" hidden>.menu...</div>. Seasons: spring, summer, autumn, winter. JS picks the current season.
- .prices grid of .price cards (.price__amount with <small>, h3, p, ul, .btn). Add class .price--confirm and a <span class="tag-confirm">confirm with Matt</span> to any price Mohammed marked as unconfirmed (private chef "from $500 a day, ingredients billed at cost" and catering "quoted per event").
- .details definition list: <dl class="details"><div><dt>..</dt><dd>..</dd></div>...</dl>
- .subs grid of .sub (img, h3, p) for forest bathing, farm and ranch tours, interactive dinner parties
- .faq with <details><summary>..</summary><p>..</p></details>
- .quote inside .section--green
- .figure / .figure--tall / .figure--wide, .photo-grid (.span-2)
- .cta band at the end of every page (copy index.html's and vary the headline)
- Add class "reveal" to blocks that should fade up. Add class "ph" to placeholder images (it prints a small "placeholder" label).

## Assets (placeholders, fixed names; use only these)
Videos in /assets/video/: home-pan.mp4, foraging-moss.mp4, chef-plating.mp4, catering-table.mp4, classes-knife.mp4
Posters in /assets/img/: home-poster.jpg, foraging-poster.jpg, chef-poster.jpg, catering-poster.jpg, classes-poster.jpg
Photos in /assets/img/: svc-foraging.jpg, svc-chef.jpg, svc-catering.jpg, svc-classes.jpg, src-market.jpg, src-shore.jpg, src-forest.jpg, src-farm.jpg, src-berries.jpg, matt.jpg, coast.jpg, salt.jpg, plate.jpg, group-cooking.jpg, forager.jpg, table-set.jpg, knife.jpg, pan.jpg, mushrooms-basket.jpg
Always give width/height attributes (4:3 photos 800x600, 3:4 900x1200, square 600x600) and loading="lazy" below the hero. Alt text describes the picture, never says "image of".

## Facts you may use (nothing else; tag anything you must assume with <!-- CONFIRM --> in the HTML)
See CONTEXT.md "Client facts". Prices (final): 3 hours $300, 6 hours $500, 12 hours $1,000, for any service. Ingredients billed at cost on chef and class days. Catering beyond a day is quoted per event. The old $500 full day / $250 half day figures are gone. Greater Mendocino area. All seasons; experiences change with weather and what is growing. No group cap stated. 30+ years foraging, 23 years teaching, Living Light and Esalen. Since 2009 as The Spontaneous Cafe, on the North Coast since 2008. Phone (707) 972-6647. Email chefmattsamuelson@gmail.com.

Mendocino produce by season, for sample menus (plausible, mark the menu "sample"): 
- Spring: nettles, miner's lettuce, wild radish, morels, fiddleheads, spring lamb, Dungeness crab (season runs to June), asparagus, strawberries late.
- Summer: heirloom tomatoes, squash, sea beans, rockfish, salmon (when open), stone fruit from inland, blackberries, corn, basil.
- Autumn: chanterelles, boletes (porcini), hedgehogs, huckleberries, apples from Anderson Valley and Philo, winter squash, quince, black trumpets late.
- Winter: black trumpets, candy caps, yellowfoot, Dungeness crab, sea urchin, kale and chard, citrus from inland, beach salt any low tide.
Avoid naming a specific farm. "A farm stand on Comptche Road" style is fine (it is a real road).

## Links
Contact CTAs go to /contact/?service=<URL-encoded service name> where service is one of: Foraging excursion, Private chef, Catering and events, Cooking class, Forest bathing or farm tour, Interactive dinner party, Something else.
