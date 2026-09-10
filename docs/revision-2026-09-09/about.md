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
