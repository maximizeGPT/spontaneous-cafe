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
