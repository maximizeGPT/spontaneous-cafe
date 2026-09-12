# About page, revision 2026-09-11: the resume goes into the story

Source for every dated fact below: `docs/source/matt-resume.txt`, received 2026-09-11. Story shape: `docs/REVISION-BRIEF-2026-09-09.md` section 5. Heading and lede rules: `docs/FIX-BRIEF-3.md`.

Story sections (h2s and body, hero and CTA excluded): **496 words**, down from a 572-word first draft, up from 341 before this revision. Under the ~500 brief.

CONFIRM tags on the page: **7 before, 7 after**. One came off (Living Light years), one went on (permission to name the Transsiberian cast).

---

## Hero

**Lede, revised**

> Retreat kitchens on four continents, then twenty-five years on the California coast, settled in Mendocino since 2009.

Was: "Peru, Thailand, India and Los Angeles, then thirty years up the California coast to Mendocino."

Changed: "thirty years" becomes "twenty-five years", and the country list becomes the four continents. Source: resume, International Consulting & Retreats (North America, South America, Asia, Australia) and Living Light 2000. **Thirty does not survive the dates.** The earliest dated role on the resume is Living Light in Fort Bragg in 2000, which is twenty-six years ago; a thirty-year climb up the coast would put Matt on it in 1996 with nothing on the resume to show for the first four years. Twenty-five is the number the dates support, and it still comfortably covers 2000 to 2026. If Matt says thirty and the early years are simply missing from the resume, it goes back in one edit. The question is in the questionnaire.

---

## Section 1: "Peru, Thailand, India"

**Copy**

> I have cooked for a living on four continents. In Peru I was the chef at yoga retreats, three meals a day for a house full of people I had not met, most of the table on some version of no gluten, no dairy or no meat.
>
> Thailand and India came after that, and the retreat work has never stopped: menus for twenty to eighty guests, and culinary intensives for hospitality teams, in North America, South America, Asia and Australia. Every one of those kitchens ran off the local market, so the first thing I did in a new place was look at what was for sale.

Changed: "a few countries" becomes "four continents", and the second paragraph gains the retreat scale and the four continents. Source: resume, International Consulting & Retreats ("Produced multi-day wellness retreat menus (20–80 guests) and led culinary intensives for hospitality teams and culinary professionals"). Peru, Thailand and India remain the brief's facts and keep their CONFIRM tags; the resume does not mention them. The Thailand/India CONFIRM was widened to ask for the individual countries behind the four continents.

---

## Section 2: "Los Angeles and a film set" (was "Los Angeles, then north")

**Copy**

> In Los Angeles I cooked privately for several celebrity clients. I am not going to name them on a website.
>
> In 2006 and 2007 I was the personal chef on the film Transsiberian, feeding Woody Harrelson and the rest of the cast on location. I co-founded High Integrity Foods the same year, an organic cold-pressed chocolate line I am still part of.

Changed: title renamed because the "then north" half moved to its own section. The Living Light sentence moved out. Two resume facts came in: the Transsiberian job (resume, "Film Production – Transsiberian, Personal Chef, 2006–2007") and High Integrity Foods (resume, "Co-Founder, 2006–Present, premium organic cold-pressed chocolate line"). The LA paragraph is unchanged and keeps its CONFIRM; the resume says nothing about LA.

**Cast naming.** The resume names Woody Harrelson, Sir Ben Kingsley and Emily Mortimer. Only the film and Woody Harrelson are on the page, under `<!-- CONFIRM: permission to name the cast publicly -->`. Naming a client on a resume and naming one on a public website are different permissions. **This comes off in one edit:** delete "Woody Harrelson and the rest of" and the line reads "feeding the cast on location". Kingsley and Mortimer can be added the same way if Matt says yes.

---

## Section 3: "Fort Bragg" (new section)

**Copy**

> I was head chef and culinary instructor at Living Light Culinary Arts Institute in Fort Bragg: 2000 to 2004, again in 2008 and 2009, and again from 2017 to 2019. The kitchen there put two or three meals a day in front of twenty to forty students and guests, and I taught the people cooking them.
>
> I moved north in stages over about twenty-five years, and Fort Bragg is forty minutes from where I stopped.

New section, built entirely from the resume ("Living Light Culinary Arts Institute — Fort Bragg, CA, Head Chef & Culinary Instructor, 2000–2004; 2008–2009; 2017–2019", "Lead kitchen operations and food production for 20–40 guests (2–3 meals daily)", "Train and mentor culinary students and interns"). It replaces the vague sentence that used to sit in the LA section ("Part of that stretch I taught at a culinary school in Fort Bragg"), and its CONFIRM about the years came off.

Full-width layout, no figure, so no image was reassigned. The section alternates paper/plain correctly with its neighbours.

**The 2008 grep.** The page contains one "2008", in the Living Light years. The retired 2008 is the settling date, and that is still 2009 everywhere (`grep -rn "settled in 2008\|since 2008" src/` returns nothing). The resume's 2008 to 2009 teaching stint is a different fact and is confirmed.

---

## Section 4: "Mendocino"

**Copy**

> I settled here in 2009 and started calling the work The Spontaneous Cafe. Foraging is what changed in Mendocino. I had picked things for years before I arrived, and here I studied it formally, the plants, the mushrooms and the shore, with as much time on the reading as on the walking. Both halves matter when you are looking at two mushrooms that are easy to mistake for each other.
>
> Two jobs ran alongside it. I was senior R&D chef at Alive & Radiant Foods from 2011 to 2015, on raw snacks that shipped across the US and Canada, and I designed the production kitchen. From 2015 to 2017 I was executive chef at Flow Restaurant and Lounge in Mendocino, where I rebuilt the menu around vegan, raw and gluten free dishes and set up the sourcing partnerships with local farmers.
>
> The cooking runs off that. I buy from a handful of small farms and the farmers market, meat and fish included. The salt, the mushrooms, the greens and the berries I go and get.
>
> One weekend I cooked for the town of Mendocino for free.

Changed: one new paragraph carries two resume roles, both of which land inside the Mendocino years and keep the chronology intact. Sources: "Alive & Radiant Foods, Senior R&D Chef, 2011–2015, Led product innovation and national raw snack development (U.S. & Canada distribution), Designed new production kitchen" and "Flow Restaurant and Lounge — Mendocino, CA, Executive Chef, 2015–2017, Redesigned menu to include vegan, raw, and gluten-free offerings, Built sourcing partnerships with local farmers and producers".

The sourcing paragraph was trimmed for the word budget: "and I cook whole foods with the vegetables used end to end" and "A chef who arrives with a shopping list cannot put that part on the table" both came out. Both lines already run on /foraging/ and /private-chef/, and section 5 of the brief allows the sourcing block to be folded in briefly. The closing line was also the one sentence on the page closest to an aphorism. Say the word and it goes back; it costs 17 words.

The 2009 date, the formal foraging study, the free town weekend and their two CONFIRM tags are untouched.

Section background moved from `section` to `section--paper` so the new Fort Bragg section does not sit against a same-coloured neighbour. No other layout change; the photo grid and split--flip are as they were.

---

## Section 5: "Teaching"

**Copy**

> I have taught cooking since 2000. At Living Light it was raw and plant-based technique, knife work, and how to run a prep list so the day does not run you. At Esalen, down the coast in Big Sur, it was cooking for a house full of people and teaching while doing it.

Changed: "I have taught cooking for twenty-three years" becomes "since 2000". Twenty-three was a guess; the resume dates the first Living Light stint to 2000, so the page can now state the year instead of a number nobody can check. Living Light is named here and once in the story, which is the limit set for this revision. Esalen is unchanged and still carries the CONFIRM asking for the rest of the teaching history.

---

## Other pages touched

**`src/pages/private-chef.html`**, the menu paragraph. "vegan, gluten free, no dairy" becomes "vegan, raw, gluten free, no dairy". Source: resume, Core Competencies, "Menu Development (including vegan, raw, gluten-free)". One clause, no CONFIRM needed.

**`src/pages/catering.html`**, Good to know, Guest counts. New first sentence: "Matt has catered events from 20 to 350 guests." Source: resume, Core Competencies, "Retreat & Event Catering (20–350 guests)", cited in an HTML comment on the line. No CONFIRM. It sits in Good to know rather than the Prices head because FIX-BRIEF-3 allows only the ingredients line under Prices.

**`src/pages/index.html`**, the About teaser. **Unchanged.** It says Matt cooked at yoga retreats in Peru, in Thailand and India, and as a private chef in Los Angeles, then studied foraging in Mendocino. Nothing in it names a year or a span, so nothing in it contradicts the revised About. Its CONFIRM tag still covers the same open facts.

**`CONTEXT.md`**, new "Resume facts (2026-09-11)" block listing every dated role plus the catering capacity, the dietary range, the twenty-five-year decision, the email mismatch and what the resume does not cover.

**`docs/to-questionnaire-matt.md` and `.html`.** Removed: the Living Light years (folded into a Peru-and-LA-only years question) and the LA-client-names question. Added: permission to name the Transsiberian cast, which email to publish, and the countries behind the four continents. The old "Besides Peru, Thailand and India, where else have you cooked?" was absorbed by the countries question. Question count 39 to 38. HTML regenerated with the same conversion (h1/h2/h3, italics, "Your answer:" stubs, HTML-escaped, Arial 11pt); the diff against the committed file is confined to the five changed questions and the new Context sentence, so the conversion is byte-identical everywhere else.

---

## Email mismatch, not acted on

The resume gives **mattsamuelson@yahoo.com**. The site uses **chefmattsamuelson@gmail.com** in the footer and on /contact/. Nothing was changed. The question is in the questionnaire, section 8.

---

## Still unconfirmed

The resume does not cover any of these, so their CONFIRM tags stay on the page:

1. **Peru.** That it was yoga retreats, the three meals a day, the dietary makeup of the table, and roughly which years.
2. **Thailand and India.** What the work actually was (retreats, restaurants, private houses), how long each lasted, and the individual countries behind North America, South America, Asia and Australia.
3. **Los Angeles.** How Matt wants the private celebrity work described, and whether any client can be named with permission.
4. **The Transsiberian cast.** Permission to name Woody Harrelson (and whether Sir Ben Kingsley and Emily Mortimer should join him) on a public page.
5. **The formal foraging study in Mendocino.** What it was (a course, a mentor, a certification, a mycological society) and when. Still the single most load-bearing unconfirmed fact on the site.
6. **The free town weekend.** Which year, and whether it was for the town of Mendocino or a named event.
7. **The rest of the teaching history.** Other schools, residencies and guest classes beyond Living Light and Esalen.

Not a CONFIRM tag, but open:

8. **Twenty-five years or thirty.** The dates support twenty-five. Matt can restore thirty.
9. **Which email to publish.**
10. **/foraging/ still says "more than thirty years" of foraging.** That is a claim about his own practice, not about moving up the coast, so it does not contradict the About page. It was left alone because that page is not owned by this revision, but it is worth a look once Matt answers the years question.
