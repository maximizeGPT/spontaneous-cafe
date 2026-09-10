# Revision brief, 2026-09-09 (Mohammed, verbatim intent)

Site: https://spontaneous-cafe.vercel.app. Keep the existing tone (plain, first person where already used, specific about places and ingredients) and the existing design system. Change content and structure, not visual style. Read all pages before editing so the overlap is visible.

Core problem: the home page repeats itself, and the About page repeats the home page.

## 1. Home page, reduce repetition
- Strip pricing on Home to one line. Under the Services heading, replace "3 hours $300 / 6 hours $500 / 12 hours $1,000. Any service." with "Starting at $300." Remove every other price on the page: the "From $300" line under the hero buttons, the "From $300" on each of the four service cards, the "$1,000 for the group" link under the example foraging day, and the "$300" in the meta description. Full pricing stays on the service pages and the contact page.
- Cut duplicate phrasing. "Since 2009" appears in the hero eyebrow, the hero subtitle and the footer; keep it once. The list "foraging days, private dinners, catering and classes" appears in the hero subtitle and as the Services heading; keep it once.
- The "morning forage, then dinner that night" story is told four times: the Private Chef card, the Example Foraging Day timeline, "Where the food comes from", and the sample menu. Keep the timeline. Cut or heavily shorten "Where the food comes from" so it does not re-explain sourcing; the photo strip can stay. Move the six-course sample menu off Home (it lives on Private Chef) and replace it with a two-line teaser linking there.
- The "About Matt" block near the bottom (three stats and one sentence) repeats the hero. Replace it with two or three sentences of the new bio story (section 5) and a link to About.
- The Home testimonial is the same one used on Private Chef. Use a different quote on one of them, or cut it from Home.

## 2. Home page, add "Build your own day"
Add a section making clear that guests can combine any of the four services into one booking. Show example combinations: a foraging morning followed by a private dinner; a cooking class that turns into the meal you eat; a foraging walk for a retreat group followed by a catered dinner; a multi-day stay with a different service each day. Frame it as choose your own adventure: pick one, or stack them. Repeat the idea briefly on each service page (one line plus a link is enough).

## 3. Private Chef page
- State clearly, near the top and in the "Good to know / Where" entry, that dinners can happen at the guest's home or rental, or at Chef Matt's home kitchen in Albion, CA. Explain the Albion option in a sentence: guests who do not want to host, or whose rental kitchen is limited, can come to him.
- In "Questions people ask", replace "Will you cook for only two people?" with a question about group size. Answer: anything from one person (solo diners welcome) up to twelve; for groups larger than twelve, inquire with Chef Matt directly. Update the "Group size" line in "Good to know" to match (it currently says "two people up to a full house").

## 4. Consistency across the site
- About says "since 2008" in the hero and body; the rest of the site says 2009. Use 2009 everywhere.
- Check that "farms, the market and the forest" (or close variants) is not on every page; vary or cut it where redundant.

## 5. About page, rewrite as a story
The current About restates Home (thirty years foraging, twenty-three years teaching, Living Light, Esalen, sourcing philosophy). Replace the top half with a chronological narrative of Matt's career. Keep the sourcing and teaching sections only if they add something the service pages do not already say; otherwise fold them in briefly.

The story, in roughly this order:
- Matt has spent his career cooking around the world. He was a chef at yoga retreats in Peru, and cooked in Thailand and India (add other places only if the client confirms).
- In LA he worked as a private chef for several celebrities (no names unless the client provides names and permission).
- He was an instructor at a culinary school in Mendocino (this is Living Light Culinary Arts Institute in Fort Bragg, already on the site; reconcile the two).
- Over about thirty years he moved progressively up the California coast and settled in Mendocino in 2009.
- In Mendocino he formally studied nature and foraging, which is what makes the nature-to-table experience different from a standard private chef. Make this the through-line: everything before Mendocino was cooking; Mendocino is where the foraging training turned it into what The Spontaneous Cafe is now.
- Keep the existing details not repeated elsewhere: cooking for the whole town of Mendocino for free one weekend, and the Esalen teaching.

First person, to match the existing About voice. Specific places, a sense of movement, and a reason to trust him with wild mushrooms. Under about 500 words.

## Output required from every agent
For each page you own: the revised copy section by section, each section with a one-line note on what was removed and why. Flag every fact you had to guess (and tag it `<!-- CONFIRM: ... -->` in the HTML) so Mohammed can confirm it with Matt. Write that report to docs/revision-2026-09-09/<page>.md (one file per page) and return a short summary.

## Standing rules that still apply
docs/FIX-BRIEF-3.md (block titles name the block, ledes only with a fact, hand accent on the load-bearing pair in hero h1 and CTA h2 only), CLAUDE.md writing bans (no em dashes in prose, no "not X, Y", no aphorisms, no invented specifics), keep every existing `<!-- CONFIRM -->`, no figcaptions, phone and email only in the footer and on Contact, review markup stripped by the build.
