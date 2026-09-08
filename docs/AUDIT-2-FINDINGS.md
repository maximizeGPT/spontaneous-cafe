
## VISUAL-DESIGN  confirmed 12, refuted 0
- [major] Ink-on-linen hero text carries a drop shadow on About, Contact, 404 and Privacy
    where: src/assets/css/site.css lines 204-205 (.hero h1 / .hero .lede text-shadow) inherited by .hero--plain (line 210); rendered at http://localhost:8787/about/ and /contact/ he
    fix: Add `.hero--plain h1, .hero--plain .lede, .hero--plain .eyebrow, .hero--plain .hand { text-shadow: none; }` after line 214 in site.css.
- [major] Internal review markup ships on customer-facing pages
    where: src/pages/foraging.html line 156, private-chef.html line 184, cooking-classes.html line 194, catering.html line 214 (span.tag-confirm); src/pages/about.html lines 81-86 (
    fix: Move the notes into `<!-- CONFIRM: ... -->` comments so the build strips them, and delete the About dl until Matt supplies the list. If a visible marker is wanted during client review, gate it with a build flag the way the .ph badge is.
- [major] Catering price row: fourth card is taller and leaves the three siblings half empty
    where: src/pages/catering.html lines 177-225 (div.prices with four .price cards); site.css lines 310-318
    fix: Take the quoted card out of the three-tier grid: give it `grid-column: 1 / -1` with a two-column inner layout (a `.price--wide` modifier on .price), or render it as a `.details` row under the three cards. Replace `<p class="price__amount">Quoted <small>per event</small></p>` with `<p class="price__amount">Quoted</p><p class="small">per event</p>` so the amount line stays one line.
- [major] Private chef timeline drops step 05 alone on a second row
    where: src/pages/private-chef.html lines 30-36 (ol.day with five li.day__step); site.css line 262 (.day grid-template-columns: repeat(4, ...))
    fix: Add a modifier for five-step lists: `.day--five { grid-template-columns: repeat(5, minmax(0, 1fr)); }` inside the ≥900px range and put `class="day day--five"` on the private-chef ol. Alternatively fold step 05 into step 04 ("You sit down. He cleans up and leaves.").
- [major] Span-2 photo in the photo grid renders as a large square, not a 2:1 panel
    where: src/assets/css/site.css lines 257-258; src/pages/index.html line 97 and about.html line 65 (img class="ph span-2")
    fix: Change line 258 to `.photo-grid img.span-2 { aspect-ratio: 2 / 1; }`.
- [minor] Caveat accent used outside hero and CTA, and on a four-word phrase
    where: src/assets/css/site.css line 282 (.menu__stamp font-family: var(--font-hand)); src/pages/foraging.html lines 73, 92, 111, 130 ("changes with the weather"); index.html 111
    fix: Restyle .menu__stamp to the existing .eyebrow treatment (Source Sans, uppercase, letter-spaced, --red), or the .tag-confirm pill shape in --butter-soft, keeping the rotate if the stamp idea should survive. Change the 404 CTA to `Or say what you were looking <span class="hand">for.</span>`.
- [minor] Placeholder badge never renders on img.ph, and the corner differs between figures and cards
    where: src/assets/css/site.css lines 414-416 (.ph::after); src/pages/index.html lines 94-98, about.html lines 61-65, foraging.html lines 208-218, cooking-classes.html lines 49-5
    fix: In build.py move the ph class from the img to the wrapping `<picture>` and set `picture.ph { display: block; position: relative; }` (it is currently display: contents), then delete `.figure.ph::after { top: 8px }` so every badge sits in one corner.
- [minor] FAQ block runs 62ch on two pages and full 1180px on three
    where: src/pages/private-chef.html line 247 and catering.html line 252 (div.faq.measure) versus foraging.html line 232, cooking-classes.html line 242, contact.html line 97 (div.
    fix: Pick one. Recommended: keep `.faq { max-width: var(--measure); }` in site.css and drop the ad hoc `measure` class from the two pages, or if full width is wanted, remove `measure` on private-chef and catering.
- [minor] Contact aside floats mid-height next to the form
    where: src/pages/contact.html line 20 (div.split); src/assets/css/site.css line 124 (.split align-items: center) and line 378 (the :has(> .form) rule only fires ≤1100px)
    fix: Extend the existing rule so it applies at all widths: `.split:has(> .form) { align-items: start; }` outside the media query, leaving the column split in place.
- [minor] Catering uses the tall home hero while the other three service pages use hero--short
    where: src/pages/catering.html line 4 (section class="hero") versus foraging.html, private-chef.html, cooking-classes.html line 4 (hero hero--short)
    fix: Add `hero--short` to the catering section, or if the taller band is deliberate for the wedding audience, apply it to all four service pages.
- [minor] At 390 the season tabs orphan "Winter" and the footer tagline orphans "WILD"
    where: src/assets/css/site.css line 295 (.tabs flex-wrap) with private-chef.html lines 93-98, foraging.html 64, catering.html 88, cooking-classes.html 106; site.css line 389 (.s
    fix: `@media (max-width: 600px) { .tabs { display: grid; grid-template-columns: repeat(4, 1fr); } .tabs button { padding-inline: 0.5rem; } .site-footer .tagline { font-size: var(--text-xs); letter-spacing: 0.12em; } }` and wrap the CTA separator as `<span class="cta__sep">&middot;</span>` hidden below 600px.
- [minor] About copy closes two paragraphs on aphorisms
    where: src/pages/about.html line 40 ("Four ingredients that are right beat twelve that are close.") and line 58 ("None of it is guaranteed.")
    fix: Replace line 40 with the fact behind it, for example "If the fish off Noyo is mediocre on the day, I drop the course rather than dress it up." and delete line 58 or fold it into the preceding paragraph as "Some weeks the ridge gives nothing."

## COPY  confirmed 10, refuted 2
- [major] Price facts are vague on Home and inconsistent between service pages
    where: src/pages/index.html:28; src/pages/catering.html:175-208; src/pages/private-chef.html:32 and 203
    fix: Rewrite the Home .section-head .lede to state the ladder once: "Three lengths, the same price for any service: 3 hours $300, 6 hours $500, 12 hours $1,000. Ingredients billed at cost." Add one .small line under the catering Prices .section-head matching the private-chef wording ("Ingredients billed at cost with the receipts, on top of the tier") or state that food is included. Make private-chef line 203 read "that morning" to match the .day step.
- [major] Home duplicates the foraging day step by step and the engagement story runs on two pages with a tense shift
    where: src/pages/index.html:71-79; src/pages/foraging.html:29 and 47-52
    fix: Keep the engagement story in one place. Either cut the foraging.html:29 sentence, or replace the Home .day section with a single .quote or short .measure paragraph that links to /foraging/ ("Read the full day"). If the Home .day list stays, put all four steps in one tense and one point of view.
- [major] The honor-box farm stand appears eight times across six pages, twice on Home and three times on Foraging
    where: src/pages/index.html:78 and 88-89; src/pages/foraging.html:13, 50, 177; src/pages/private-chef.html:128; src/pages/catering.html:121; src/pages/about.html:55-56
    fix: Let the honor box live in the About Sourcing section (its natural home) and once in the Foraging .day step. Cut it from Home 78 and 89, foraging 13 and 177, and the two menu .course notes. Give the Home "Where the food comes from" .section-head a different h2 from About (for example "Bought within an hour of the table, or picked on the way.").
- [major] The free town weekend runs on Home and Catering, as a quotable closer, and is missing from About
    where: src/pages/index.html:152; src/pages/catering.html:29
    fix: Keep one occurrence. Move the fact to About ("Teaching" or "The short version" .stack) as a plain sentence with the year once the CONFIRM is answered, and use it on Catering only as a scale reference ("largest job: a free weekend for the town of Mendocino, [N] plates"). Cut it from Home 152 and drop the "would do again first" clause.
- [major] "Thirty years" is stated four times on the Foraging page; the credential block repeats on three pages
    where: src/pages/foraging.html:13, 28, 31, 247; src/pages/index.html:150; src/pages/cooking-classes.html:13; src/pages/about.html:9, 23, 24, 74
    fix: On Foraging, keep the number in the .lede and in the safety FAQ answer only; rewrite line 28 to the fact ("which ridge holds chanterelles in a dry November") and cut the line 31 aside. Let Home 150 and Classes 13 name the schools without the year count, and leave the full count to About.
- [major] Aphorisms and quotable closers on service pages and About
    where: src/pages/about.html:40, 58; src/pages/index.html:35, 79; src/pages/foraging.html:31, 215; src/pages/cooking-classes.html:30, 125; src/pages/catering.html:29
    fix: Cut each closer or replace it with the fact it gestures at. About 40 becomes the Noyo fish example alone; About 58 folds into the previous paragraph as "Any of it can be missing on the day."; Home 35 ends at "berries on the road in."; Foraging 215 becomes what guests see ("the ranch the lamb came from, the row the greens came out of") without the tasting claim; Classes 125 ends at "Pepper on strawberries changes them."
- [major] Sentences that only sound good, claims without a fact, and default groups of three
    where: src/pages/cooking-classes.html:51; src/pages/catering.html:28, 30, 48, 70; src/pages/private-chef.html:62; src/pages/about.html:9; src/pages/index.html:35
    fix: Replace each with a checkable number or cut: "Most bookings come from a previous guest" only if Matt confirms a share; "a dinner" for "one real dinner"; "barns, bluffs, back gardens and rented halls"; drop "the room is loud inside four minutes" and "your hands will know why". Vary the counts in the .lede lists to two or four items.
- [minor] "Book" buttons lead to an inquiry form that the site itself says is not a booking
    where: src/pages/foraging.html:15, 169, 181, 193, 273; src/pages/private-chef.html:196, 207, 218; src/pages/catering.html:187, 198, 209; src/pages/cooking-classes.html:15, 206, 
    fix: Keep the .btn component and change the label to match the outcome: "Ask about 3 hours" or "Inquire: 3 hours" on all twelve tier cards, "Plan a day" / "Plan a class" in the heroes, and "Send an inquiry" on every .cta band. Use numerals everywhere to match the .price h3 ("3 hours").
- [minor] The same CTA heading and the same testimonial recur across pages
    where: src/pages/index.html:134, 161; src/pages/foraging.html:260, 269; src/pages/private-chef.html:271, 280; src/pages/contact.html:8
    fix: Give each .cta h2 a service-specific line ("Tell Matt the tide and the date" on Foraging, "Tell Matt the kitchen and the head count" on Private chef) and keep the generic one for Home and Contact, with one apostrophe style. Use the testimonial once on Home and swap the About quote ("Matt is an expert in foraging...") onto Foraging.
- [minor] Voice slips: "we" in brand-voice eyebrows, third-person FAQ on Contact, adjective-only tagline
    where: src/pages/foraging.html:59, 64; src/pages/cooking-classes.html:101; src/pages/contact.html:100-108; src/pages/index.html:18; src/layout.html:52
    fix: Change the .eyebrow text to "What the baskets hold" and "What a class cooks". Rewrite the three Contact .faq answers in Matt's voice to match the other pages. Replace the .hero__note with a fact ("Mendocino coast · 3, 6 or 12 hours · from $300") and keep the four-word tagline in the footer only if it is the client's existing line.
  (refuted) Home contradicts itself on the founding year
  (refuted) Name and area terms drift across pages

## IA-NAVIGATION  confirmed 10, refuted 2
- [major] Price tiers sit four to five viewports deep on every service page, with no in-page route to them
    where: src/pages/private-chef.html:179 (Prices is section 6 of 10); src/pages/catering.html:170; src/pages/foraging.html:150; src/pages/cooking-classes.html:188. Rendered at 128
    fix: Add id="prices" to each Prices <section> and make the hero note a jump link: <p class="hero__note"><a href="#prices">3, 6 or 12 hours · From $300 · Ingredients at cost</a></p>. Then move the Prices section above the data-tabs sample menu section on all four pages so the tiers land within the second or third viewport.
- [major] A planner with forty guests cannot tell whether they are a $500 tier or a quote
    where: src/pages/catering.html:174-175, 211-215, 236; src/pages/index.html:51; src/pages/catering.html:66, 100
    fix: Put the cut on the cards: change the three .price h3 headings to e.g. '3 hours · up to about 12 guests' and the .price--confirm h3 to 'Larger events · above about 12 guests, or any event with rentals' (number to be confirmed by Matt). Rewrite index.html:51 to the same rule ('Above about twelve guests, or with rentals, it is quoted per event') so Home and Catering agree.
- [major] Foraging and Cooking Classes heroes omit price and length from the first viewport
    where: src/pages/foraging.html:18 (hero__note 'Salt · Mushrooms · Berries · Farm stands'); src/pages/cooking-classes.html:18 (hero__note 'Knife skills · Efficiency · Improvisati
    fix: Use the hero__note consistently across the four service pages: '3, 6 or 12 hours · From $300 · One price for the group' (linked to #prices per finding 1). Move the keyword list into the eyebrow or drop it.
- [major] Forest bathing, farm tours and interactive dinner parties are dead ends, and dinner parties are described in two places
    where: src/pages/foraging.html:207-221 (.sub cards, no links); src/pages/cooking-classes.html:48-62 (.sub cards, no links); src/pages/contact.html:62-63 (select options 'Forest 
    fix: Add a link-arrow inside each .sub: <a class="link-arrow" href="/contact/?service=Forest%20bathing%20or%20farm%20tour">Book a forest or farm day</a> and, for the dinner party, href="/contact/?service=Interactive%20dinner%20party". Keep the interactive dinner party on cooking-classes only and replace the foraging copy with a one-line link-arrow to /cooking-classes/. Add a footer <li><a href="/cooking-classes/">Interactive dinner parties</a></li> so all three are findable from every page.
- [major] The About page CTA preselects 'Something else' on the inquiry form
    where: src/pages/about.html:26 (href="/contact/?service=Something%20else")
    fix: Change line 26 to <a class="link-arrow" href="/contact/">Plan a day or a dinner</a> so the select stays on 'Choose one'.
- [major] Placeholder text 'Matt to add' ships to the live About page
    where: src/pages/about.html:81-86 (dl.details, dd 'Other places I have taught and cooked. Matt to add.'); built at dist/about/index.html:196
    fix: Delete the <dl class="details reveal"> block at lines 81-86, or move it inside the <!-- CONFIRM --> comment until Matt supplies the entries.
- [minor] Service pages barely cross-link, and the two links that exist land on page tops instead of the relevant tier
    where: src/pages/foraging.html (zero links to /private-chef/ or /cooking-classes/; line 51 'Dinner from the baskets' and 189 'A multi-course dinner in your kitchen' are plain te
    fix: With id="prices" in place (finding 1): private-chef.html:16 → href="/foraging/#prices"; add <a class="link-arrow" href="/private-chef/">How the dinner works</a> after the foraging 12-hour card (line 193) and after step 4 (line 51); cooking-classes.html:56 add a link-arrow to /foraging/; catering Good-to-know add a <dt>Retreats</dt> row linking to /cooking-classes/ for the interactive dinner party.
- [minor] The home 'full day' story is the twelve-hour product but links nowhere
    where: src/pages/index.html:67-82 (section 'A couple booked a full day on their engagement trip')
    fix: After the </ol> at line 80 add <a class="link-arrow" href="/foraging/#prices">The twelve-hour day, $1,000 for the group</a>.
- [minor] The contact page speaks to renters only, and its lead-time answer contradicts the catering page
    where: src/pages/contact.html:80 (help 'Where you're staying, dietary needs, anything else'); src/pages/contact.html:99-100 ('A few weeks is comfortable') vs src/pages/catering.
    fix: Change the message help at line 80 to 'Where you're staying or the venue, dietary needs, anything else'. In the contact FAQ at line 100 add: 'Weddings and retreats book months to a year out; the catering page has the detail.' Optionally add a class="help" line under Guests: 'For an event, a rough count and the venue is enough.'
- [minor] Contact page H1 repeats the CTA heading the visitor just clicked
    where: src/pages/contact.html:8 (h1 'Tell Matt the date and who's coming.') and :18 (h2 'Send Matt the details.'); same line as h2 on src/pages/index.html:161, private-chef.html
    fix: Make the contact H1 'Send Matt the details.' (the current h2 at line 18) and delete the h2, or keep the H1 and change line 18's section-head to the aside content. Vary the service-page CTA h2s so at most one of them uses the contact H1's wording.
  (refuted) Internal 'confirm with Matt' pills render on the price section of all four service pages
  (refuted) Nav and card order lead with Foraging while the hero and the audience lead with dinner

## CONVERSION  confirmed 10, refuted 2
- [major] Tier buttons discard the tier the visitor chose
    where: src/pages/private-chef.html:196,207,218; src/pages/foraging.html:169,181,193; src/pages/catering.html:187,198,209,223; src/pages/cooking-classes.html:206,218,230; src/pag
    fix: Append the tier to each card link (e.g. href="/contact/?service=Private%20chef&tier=12%20hours") and add a fifth .field to the form: <label for="tier">How long</label><select id="tier" name="tier"> with options "Not sure yet", "3 hours, $300", "6 hours, $500", "12 hours, $1,000", "Larger event, quoted". Prefill it in site.js the same way service is prefilled, and add it to the _subject string so Matt's inbox shows the tier.
- [major] Price is below the fold on four of five landing pages
    where: src/pages/index.html:18; src/pages/foraging.html:18; src/pages/catering.html:18; src/pages/cooking-classes.html:18 (compare src/pages/private-chef.html:18)
    fix: Use the same note on every service hero: "3, 6 or 12 hours · From $300 · Ingredients at cost" (catering: "· Larger events quoted"). On home: "Any service · 3, 6 or 12 hours · From $300". Add id="prices" to each Prices section and wrap the note's "From $300" in <a href="#prices"> so the number is also the shortcut.
- [major] Contact page never states the price
    where: src/pages/contact.html:21-35 (.contact-aside), 9 (lede)
    fix: Add a fourth block to .contact-aside above the reply-time line: <div><p class="eyebrow">Rates</p><p>3 hours $300 · 6 hours $500 · 12 hours $1,000, any service. Ingredients at cost. Weddings and larger events are quoted.</p></div>
- [major] Catering and cooking classes reach the CTA with no proof beside it
    where: src/pages/catering.html:211-224 (Get a quote card), 273-284 (.cta); src/pages/cooking-classes.html:263-274 (.cta)
    fix: Add a .section--green .quote before the .cta on both pages, using the existing blockquote/cite pattern, with a wedding or retreat guest line once Matt supplies one. Until then, put a one-line credential in the .price--confirm card: "Cooking on this coast since 2009. Largest job: a free weekend feeding the town of Mendocino." and on classes add to the .cta paragraph: "Twenty-three years teaching, at Living Light and Esalen."
- [minor] Secondary hero button sends the visitor off the buying page
    where: src/pages/private-chef.html:16; src/pages/cooking-classes.html:16; src/pages/index.html:16
    fix: On private-chef and cooking-classes change the secondary to <a class="btn btn--light" href="#prices">See the three lengths</a> and add id="prices" to the Prices section. Keep the cross-sell as the existing .link-arrow inside the 12-hour card ("See what a foraging morning finds"). Home can keep "Go foraging" since its job is routing.
- [minor] Form error copy is first person and omits the phone
    where: src/assets/js/site.js:276
    fix: Replace with: 'That did not send. Email chefmattsamuelson@gmail.com or call (707) 972-6647.' and render the phone as a tel: link inside .form__status.
- [minor] About page preselects "Something else" as the service
    where: src/pages/about.html:26
    fix: Link to /contact/ with no query, matching the About .cta band at line 107.
- [minor] Required fields do not match what the page asks for
    where: src/pages/contact.html:8, 69, 74, 79
    fix: Make Date required (keep the free-text input and "Rough is fine" help) and drop required from the textarea, relabelling it "Where you're staying, and anything else". Required count stays at four and the form now asks for what the headline promised.
- [minor] Catering CTA band promises a price the page says comes after a call
    where: src/pages/catering.html:277 vs 48 and 215
    fix: Change the .cta paragraph to: "For a small gathering he writes back with a menu direction and the tier. For a wedding or retreat he writes back to set up the first call, and the quote follows it."
- [minor] Same CTA headline on four pages
    where: src/pages/index.html:161; src/pages/private-chef.html:280; src/pages/foraging.html:269; src/pages/contact.html:8
    fix: Keep the line on home and contact (use "who's" on both). Private chef: "Tell Matt the night and the head count." Foraging: "Tell Matt the day and how many are walking."
  (refuted) Confirmation copy leaves the visitor with an empty form and no next step
  (refuted) No framed path for a visitor with a question but no date

## MOBILE-READING  confirmed 6, refuted 5
- [major] Private Chef page is 12.6 screens long with a single photo below the hero
    where: src/pages/private-chef.html lines 23-266; rendered http://localhost:8787/private-chef/ at 390 (docH 10618) and 360 (docH 11207)
    fix: Convert the Who-books-it `.grid-2` (lines 47-64) into the existing `.subs` component so each of the four bookings gets a 4:3 `.sub img` (renders 350x263 at 390), and add a `.figure` (4:3) between the Prices section head and `.prices`, or a `.figure--wide` above `.details`. Both components already stack correctly at <=600px.
- [major] Home photo grid on mobile leaves two empty cells and crops the wide farm photo to a square
    where: src/pages/index.html lines 93-99 (.photo-grid); src/assets/css/site.css lines 254-258
    fix: Change site.css line 257 to `.photo-grid img.span-2 { aspect-ratio: 2 / 1; }` and add, inside the 600px `.photo-grid` rule, `.photo-grid .span-2 { order: -1; }` so the farm photo takes the first full-width row and the remaining four images fill two complete rows (market + shore, forest + berries). The selector fix also restores the 2:1 crop at desktop.
- [minor] Season tabs wrap 3 + 1, leaving Winter orphaned on a second row at every phone width
    where: src/pages/foraging.html lines 64-69 and src/pages/private-chef.html lines 93-98 (.tabs); src/assets/css/site.css lines 294-295
    fix: In the existing 600px media block add `.tabs { display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); } .tabs button { padding-inline: 0.5rem; }` so the four seasons form a 2x2 grid of 44px-high, full-width thumb targets. Keep the flex layout above 600px.
- [minor] Private Chef hero does not fit a 360x780 screen: buttons wrap to two rows and the note wraps with 'COST' orphaned
    where: src/pages/private-chef.html lines 14-18 (.hero__actions and .hero__note); rendered http://localhost:8787/private-chef/ at 360
    fix: Shorten the note on line 18 to '3, 6 or 12 hours · From $300' (ingredients at cost is already in the lede and the prices intro) and add `@media (max-width: 400px) { .hero__actions .btn { padding-inline: 1rem; } }` so both buttons fit one row at 360 (about 316px needed in a 320px column).
- [minor] Pause chip occupies its own 90px row under the hero note on every video hero
    where: src/assets/css/site.css lines 226-230 (.hero:has(.hero__toggle) .wrap padding and .hero__toggle position); rendered heroes on /, /foraging/, /private-chef/ at 390 and 360
    fix: At <=760px move the control to the top-right corner under the header: `.hero__toggle { top: var(--space-4); bottom: auto; }`, drop the extra `.wrap` padding, and reduce the chip to the 44px circle with the label in `.visually-hidden` (the `min-width: 44px` and `border-radius: 999px` are already there).
- [minor] Footer tagline breaks with 'WILD' alone on a line at 390 and 360
    where: src/layout.html line 52 (.tagline); src/assets/css/site.css line 388
    fix: In the 600px media block add `.site-footer .tagline { letter-spacing: 0.12em; font-size: var(--text-xs); }` so the four words fit one line, or wrap each middot pair in a `span` with `white-space: nowrap` so a break lands on a separator.
  (refuted) Phone number is not one tap from anywhere on a phone; the mobile menu has no tel: link
  (refuted) Price cards stack cheapest-first on mobile and nothing marks the usual booking
  (refuted) Foraging hero eyebrow wraps to two lines and the five-line lede fills the whole first screen
  (refuted) Sticky header takes 77px of a 780/844px viewport
  (refuted) Foraging opens with 950px of unbroken text before the first photo