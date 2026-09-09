# Fix brief 3: block titles, ledes and the hand accent (Mohammed's review, 2026-09-08)

Mohammed went through Home and Foraging and every complaint was a block title, eyebrow or lede. The body copy is mostly fine. Apply these rules to EVERY page, then re-read every heading on your pages against them.

## Block titles
- A section heading names what the block is. "Prices". "What a foraging day includes". "Example day". "Sample menu". "Questions people ask". "Where classes happen". Two to five words, no verb needed.
- Never a title with a turn or a twist: no "X, and Y", no "Three lengths, one price for the group", no count-plus-reveal, no "Also out there", no "The practical side", no "How the day works" under an eyebrow that already says "The full day" (that pair is redundant, keep one).
- Eyebrow plus h2 must not say the same thing twice. If the eyebrow already names the block, the h2 can be the specific thing ("Prices" eyebrow, then "3, 6 or 12 hours" h2) or drop the eyebrow.
- Hero h1s stay as they are unless they break a rule above.

## Ledes and intro lines
- A lede exists only when it adds a fact the title does not. Otherwise delete it. Cut on sight: "The shape of the day holds", "Times move with the tide chart", "Rain, fog and tide move all of this by weeks. The list below is what a good day looks like", "A sample. It changes with the season and the weather", "Same three lengths and the same rates. Any of them can end with dinner", "Three lengths, the same price for any service:", "The rate covers the excursion however many of you come. Tell Matt the number and he plans the route around it", and anything of that family.
- The price ladder on Home becomes one plain line: "3 hours $300. 6 hours $500. 12 hours $1,000. Any service."
- Prices section on every service page: eyebrow "Prices", h2 "3, 6 or 12 hours", no lede except the single small line "Ingredients billed at cost on days that end with a meal." with its CONFIRM comment. Delete "Three lengths, one price for the group" and the group-size sentence.

## Descriptions of what a service is
- Every service gets a plain description of what it entails, the way a menu describes a dish: who it is for, what happens, how long, what is included. No narrative ("He reads the tide chart in advance and checks what has come up since the last rain, then sets the route"), no vignette ("Families book it for kids who want to hold something they picked"), no story unless it is the one example block.
- Foraging: replace the two narrative paragraphs under "What the day is" with: a two-sentence description (a guided walk on the shore, in the forest and at farm stands around Mendocino, gathering salt, mushrooms, greens and berries with Matt identifying everything before it goes in the basket; ends at a table if you book the longer tier), then a short list of what is included. Same shape on Classes, Private chef and Catering: description first, list second.
- Home service cards: each card's paragraph says what the service entails in one sentence. Foraging card: "A guided walk on the shore, in the forest and at farm stands, gathering salt, mushrooms and berries with Matt."
- The engagement-trip day on Home: eyebrow "Example experience", h2 "A full foraging day, start to finish" (or similar plain wording), keep the four steps but each step is one plain sentence.
- Delete the Home sample-menu section head text "What a late-summer dinner looks like. A sample. It changes with the season and the weather." Replace with eyebrow "Sample menu" and h2 "Late summer, six courses". The menu card stays.

## Hand accent (Caveat), restored
- CSS `.hand` exists again. Use it ONLY in the hero h1 and the CTA h2 of a page, and only on the load-bearing pair of words, both of them, so the accent reads as deliberate: "I <span class="hand">forage</span> and I <span class="hand">cook</span>." "Tell Matt the <span class="hand">date</span> and who's <span class="hand">coming</span>." "Wild food, <span class="hand">cooked</span> where you're <span class="hand">staying</span>." One accented word is allowed only when the sentence has one load-bearing word. Never on a connective, an article or an adverb. Never in section h2s, ledes, eyebrows or cards.

## Quote attribution
- Every `<cite>` gets a leading dash: `<cite>&mdash; Foraging day and private dinner guest</cite>`.

## Everything else from FIX-BRIEF-2 round 3 still holds
Third person on Home and service pages, first person on About and in FAQ answers, no invented facts (tag CONFIRM), no figcaptions, phone and email only in the footer and Contact, plain register, no em dashes in prose (the cite dash is the one exception), no "not X, Y".
