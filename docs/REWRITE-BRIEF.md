# Rewrite brief (2026-09-07). Read with docs/PAGE-BRIEF.md and CONTEXT.md.

## Why
Mohammed's review: first person everywhere is too much, and some sections echo his interview answers verbatim ("Six words I actually mean" is literally the "pick five words" question). Copy should read like a small studio wrote it about a real person, with Matt's own voice used where it earns its place.

## Register, by place
- Home hero and section headings: brand voice, no "I". Plain and specific. Example hero: "Wild food, cooked where you're staying." Lede in third person: "Chef Matt Samuelson forages, shops and cooks on the Mendocino coast. Private dinners, catering, foraging days and cooking classes, since 2009."
- Service pages: third person by name ("Matt", "Chef Matt") for what happens, how it works, what is included, prices. Short first-person lines are allowed where they carry a fact only he could say, set as a pull quote or a one-sentence aside (at most two per page). FAQ answers may be in Matt's first person, because they are answers to a question.
- About: first person. This is the one place his voice runs the page. Keep the story, cut anything that restates the interview. Delete the "Six words I actually mean" section outright; the words (whole foods, farm to table, local, organic, resourceful, quality) appear inside the sourcing and cooking paragraphs, never as a list or a definition block.
- Contact and CTA bands: address the reader ("Tell Matt the date and who is coming"). Never "I'll come back with".
- Privacy and 404: neutral site voice ("this site", "we").
- Remove every line that exists only because it was in the interview: "five words", "one of the only people there" is fine as a fact but not repeated on three pages, the engagement-trip story appears once on Home (the day timeline) and once on Foraging, nowhere else.

## Prices (final, replaces every earlier figure)
Three tiers, any service: **3 hours $300**, **6 hours $500**, **12 hours $1,000**. Ingredients billed at cost on private chef and class days. Catering beyond a day is quoted per event. Present as three .price cards with .price__amount, the hour count as the h3, and two or three bullets on what fits in that length for that service (for example, foraging: 3 hours is one stop, 6 hours is two or three stops, 12 hours is the whole day and dinner). Remove every "$500 full day / $250 half" and "from $500 a day" string, including in home service cards (use "From $300", "3, 6 or 12 hours") and hero notes. Keep .price--confirm and .tag-confirm ONLY on the catering "quoted per event" card and the "ingredients at cost" line.

## SEO in copy
Each service page h1 or first h2 must contain "Mendocino" and the service phrase naturally (private chef Mendocino, Mendocino catering, foraging Mendocino, cooking classes Mendocino). Home h1 can stay evocative; the first h2 should carry "Mendocino". Alt text on the four home service cards and hero-adjacent images should mention Mendocino or the coast where true. Meta descriptions 120 to 158 characters. Catering description is currently 161: shorten.

## Page-level audit fixes to apply in the same pass
- Drop `style="list-style:none;padding:0"` from every .day list (CSS handles it now). No inline styles anywhere.
- Season tab panels: remove the `hidden` attribute from all four panels (JS sets it). Keep role/aria wiring.
- Hero video markup on every service page and Home becomes:
  `<video data-hero muted loop playsinline preload="none" poster="/assets/img/<x>-poster.jpg" aria-hidden="true"><source media="(max-width: 700px)" src="/assets/video/<x>-720.mp4" type="video/mp4"><source src="/assets/video/<x>.mp4" type="video/mp4"></video>` (no autoplay attribute; JS starts it).
- Footer heading levels are in layout, not yours. But page heading order must be h1 then h2 then h3 with no skips.
- Contact page: the service select gets a first `<option value="" disabled selected>Choose one</option>`; the date field becomes `type="text"` with placeholder "e.g. mid-October, or a weekend in May" and autocomplete="off"; help text is associated with its field via `aria-describedby` pointing at the help element's id; required markers get `<span class="req" aria-hidden="true">*</span>` and a single visible line above the form "Fields marked * are required"; the phone number and email appear above the form on mobile (put the .contact-aside first in source order and let CSS order handle desktop, or add a short line with the tel link under the hero lede); add a hidden input `_next`? No: leave Formspree's default.
- About: add a CTA band or link-arrow after the story section, not only at the end.
- Privacy: name Formspree (receives and stores form submissions, US), Vercel (hosting, server logs), and the notification function that may send a text to Matt; say fonts are served from this site (no Google Fonts any more).
- Every image keeps width/height and loading="lazy" below the hero. Placeholder photos keep class "ph"; the Matt photos (matt.jpg, matt-kitchen.jpg, matt-square.jpg) are real: no "ph", alt describes the kitchen photo (Chef Matt in a kitchen above the Mendocino coast, finishing a bowl of roasted vegetables).
- Keep `<!-- CONFIRM ... -->` comments where a fact is still an assumption; the build strips them from production.

## Voice rules still apply
CLAUDE.md bans (no em dashes, no "not X, Y", no claim-then-restate, no aphorisms, no default tricolons, no trailing participials, no mechanical transitions, no LLM vocabulary, no false agency, no vague attribution, no "serves as"). Prose anti-slop: no throat-clearing, no demonstrative kickers, no quotable closers, no "and here is how everyone reacts" endings. Every sentence adds a fact. Vary sentence length.
