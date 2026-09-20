# SEO landscape, September 2026

Research date: 2026-09-19. Site under review: nine static HTML pages (eight indexable plus a 404) for a solo chef in Mendocino, California, built with a Python build script, deployed to Vercel, domain `spontaneouscafe.com` currently pointing at a one-page GoDaddy site. Read-only research. No repo file was edited.

## Summary

Google removed FAQ rich results on 7 May 2026, so the site's five `FAQPage` blocks (and its four `Service` blocks, which were never a rich result type) earn nothing visible in Search; Google says unused markup causes no problem and has "no visible effects".
Zero-click is at 68% of US Google searches for January to April 2026, but local and branded queries are the categories that still send clicks, which is exactly this business.
Google states there is no special markup, file or chunking that gets a page into AI Overviews or AI Mode, and says llms.txt will "neither harm nor help".
Most of what decides local rankings sits outside the repo: Google Business Profile carries about 25% of local pack weight, reviews about 20%, and on-page about 10%.
Two technical risks are live right now: the production `*.vercel.app` alias is indexable and will duplicate the site, and the GoDaddy cutover needs a redirect plan for `/privacy-policy`.

---

## 1. Structured data support in 2026

### Answer

Google's current gallery lists 26 feature families. FAQ, HowTo and the sitelinks search box are gone from it. What this site uses or could use:

| Type | Status in Google Search, Sept 2026 | Rich result? | Worth emitting? |
|---|---|---|---|
| LocalBusiness | Supported | Knowledge panel details, business carousels | Yes. Highest value type on the site. |
| Service | Not a rich result type, never was | No | Yes, for entity understanding only. No Search feature depends on it. |
| FAQPage | Restricted Aug 2023, feature retired 7 May 2026 | No | Neutral. Keep or drop. No visible effect either way. |
| BreadcrumbList | Supported, desktop only since 23 Jan 2025 | Yes, desktop URL line | Yes, and this site currently emits none. |
| Person | Supported via Profile page | Profile page result, mostly for social and forum profiles | Marginal. `founder` nesting inside LocalBusiness already carries the entity link. |
| WebSite | Supported for site names, not for the search box | Site name in results | Yes. Site is missing it. |
| Offer | Supported inside Product and inside LocalBusiness/Service | Only inside a supported parent | Yes, keep as nested. A standalone Offer earns nothing. |
| Event | Supported | Event rich result and Google event experiences | Only if he publishes dated, ticketed events. Not applicable today. |
| Course / Course list | `Course info` deprecated 12 June 2025. `Course list` still supported | Carousel only | No. Requires at least three courses, a `provider`, an `ItemList` carousel, and Google defines a course as curriculum with lectures or modules. A four-hour cooking class does not qualify. |

### Evidence

- Current gallery and its full feature list, last updated 2026-06-15: https://developers.google.com/search/docs/appearance/structured-data/search-gallery . FAQ, HowTo and sitelinks search box are absent from the page.
- FAQ and HowTo restriction, August 2023: https://developers.google.com/search/blog/2023/08/howto-faq-changes . Exact words: "Going forward, FAQ (from FAQPage structured data) rich results will only be shown for well-known, authoritative government and health websites. For all other sites, this rich result will no longer be shown regularly." And on removal: "While you can drop this structured data from your site, there's no need to proactively remove it. Structured data that's not being used does not cause problems for Search, but also has no visible effects in Google Search."
- FAQ final retirement: Google's documentation updates page records a deprecation notice added 2025-05-08 reading "This feature will no longer appear in Google Search starting May 7, 2026", followed by removal of the FAQ documentation. https://developers.google.com/search/updates . The exact date the docs page was pulled is reported inconsistently by the source (it gives 2025-06-15 in one place, which conflicts with the 2026-05-07 retirement date). Treat the retirement date, 7 May 2026, as the verified fact and the doc-removal date as unverified.
- Sitelinks search box retired: announced 21 October 2024, removed globally 21 November 2024. https://developers.google.com/search/blog/2024/10/sitelinks-search-box . Google noted the WebSite type stays supported because site names use a variation of it.
- Seven types deprecated 12 June 2025: Book Actions, Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement, Vehicle Listing. Search Console reports, Rich Results Test support and appearance filters for them were removed 8 September 2025. https://searchengineland.com/google-drops-reporting-on-several-structured-data-types-461744 (Search Engine Land, June 2025). **Sources disagree**: the current gallery navigation, as of 2026-06-15, still lists "Book actions" and "Fact check" as live feature guides, and one secondary source reports the deprecation banner was later pulled from Book actions. Neither type matters here.
- Practice problem removed January 2026, per https://developers.google.com/search/updates .
- Breadcrumbs dropped from mobile results 23 January 2025, desktop retained, markup still supported: https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs .
- Course list requirements, last updated 2026-09-08: https://developers.google.com/search/docs/appearance/structured-data/course . "You must mark up at least three courses" and the definition restricts it to "a series or unit of curriculum that contains lectures, lessons, or modules".
- LocalBusiness still supported, last updated 2026-09-08: https://developers.google.com/search/docs/appearance/structured-data/local-business . Required properties are `name` and `address`. The page says nothing about service-area businesses or `areaServed`.
- Video rich results require a watch page, last updated 2025-12-18: https://developers.google.com/search/docs/appearance/video . "A watch page's main purpose is to show users a single video." Background and decorative loops do not qualify.

### Implication for this site

The site emits five `FAQPage` blocks (catering, contact, cooking-classes, foraging, private-chef) that produce no Search feature. They are harmless, and there is no verified evidence they help AI citation on Google (see section 2), so leave them alone and do not add more on that basis. Two real gaps: no `BreadcrumbList` anywhere, and no `WebSite` node for the site name. One real error: `dist/404.html` carries the full LocalBusiness JSON-LD, which is markup on a soft-error page. One structural weakness: the `LocalBusiness` node on the home page and the `Service` nodes on the four service pages share no `@id`, so Google sees five unconnected `LocalBusiness` declarations rather than one entity with four services. Adding `"@id": "https://spontaneouscafe.com/#business"` to the business node and pointing every `Service.provider` at `{"@id": "https://spontaneouscafe.com/#business"}` costs nothing and makes the graph one entity.

---

## 2. AI in search, and the AI crawlers

### Answer, Google

Google's position is that there is no separate optimisation surface. It says there are no additional requirements, no special schema, no required machine-readable file, and no need to chunk content. Appearing in AI Overviews and AI Mode runs through the same ranking systems as the blue links, with retrieval-augmented generation and query fan-out on top.

Click impact is real and measured, but the headline numbers disagree with each other because they measure different things. The honest range for an informational query with an AI Overview is a 34% to 47% relative drop in clicks. Local and branded queries are the categories that have held up best.

### Evidence, Google

- "There are no additional requirements to appear in AI Overviews or AI Mode." And "There's also no special schema.org structured data that you need to add." Last updated 2025-12-10: https://developers.google.com/search/docs/appearance/ai-features . The same page claims clicks from AI Overview pages are "higher quality (meaning, users are more likely to spend more time on the site)". That is Google's own unfalsifiable claim; treat it as a claim, not evidence.
- "You don't need to create new machine readable files, AI text files, markup, or Markdown to appear in Google Search" and such files "will neither harm nor help your site's visibility or rankings". Also: "There's no requirement to break your content into tiny pieces for AI to better understand it." And: "Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add." Last updated 2026-07-10: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide .
- Search Console now reports generative AI performance separately, announced June 2026: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports .
- Zero-click rate: 68.01% of US Google searches ended without a click, January to April 2026, from Similarweb panel data. Up from 60.45% in 2024 and 49% in 2019. AI Mode was used on 0.34% of searches in that window. Published 9 June 2026: https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ . The same post names "branded searches, local businesses, and high-intent transactional or tactical queries" as the categories that still benefit from SEO.
- Ahrefs, 300,000 keywords, March 2024 versus March 2025: AI Overview presence correlated with a 34.5% lower average CTR for the top-ranking page. Published 17 April 2025: https://ahrefs.com/blog/ai-overviews-reduce-clicks/ .
- Pew Research Center, behavioural panel of over 900 US adults, 68,879 unique queries in March 2025: users clicked a traditional result on 8% of searches with an AI summary versus 15% without. Published 22 July 2025: https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ .
- **Sources disagree.** Secondary 2026 write-ups widely quote "58% lower CTR" and "AI Overviews on 48% of queries" and "AI Overviews on 68% of local queries". I could not trace those to a primary dataset. Treat them as unverified. The Ahrefs and Pew figures are the ones with published methodology.

### Answer, non-Google assistants and robots.txt

| Agent | Purpose | Honours robots.txt | Recommendation for this site |
|---|---|---|---|
| `OAI-SearchBot` | Shows sites in ChatGPT search | Yes | Allow |
| `GPTBot` | Trains OpenAI foundation models | Yes | Allow (see note) |
| `ChatGPT-User` | User-initiated fetch from ChatGPT | "robots.txt rules may not apply" | Nothing to do |
| `PerplexityBot` | Perplexity's search index | Yes | Allow |
| `Perplexity-User` | User-initiated fetch | "generally ignores robots.txt rules" | Nothing to do |
| `ClaudeBot` | Trains Anthropic models | Yes | Allow (see note) |
| `Claude-SearchBot` | Indexes for Claude's search | Yes | Allow |
| `Claude-User` | User-initiated fetch | Yes | Allow |
| `Google-Extended` | Gemini training and grounding outside Search | Yes | Allow. Blocking it does not remove you from Google Search or AI Overviews. |

The practical robots.txt policy for a business that wants to be found by AI assistants is: allow everything, block nothing, and do not write an llms.txt. The two training-only crawlers (`GPTBot`, `ClaudeBot`) are a judgment call, since allowing them contributes the content to model training without any citation guarantee. For a nine-page brochure site with no proprietary text worth protecting, allowing them costs nothing and removes any risk of a misconfigured rule blocking the search-facing bot by accident.

### Evidence, non-Google

- OpenAI crawler documentation: https://developers.openai.com/api/docs/bots . "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers." `ChatGPT-User` is described as user-initiated, and "robots.txt rules may not apply".
- Perplexity crawler documentation: https://docs.perplexity.ai/docs/resources/perplexity-crawlers . "We recommend allowing `PerplexityBot` in your site's `robots.txt` file." `Perplexity-User` "generally ignores robots.txt rules". Neither is used for model training.
- Anthropic crawler documentation, three agents, all honouring robots.txt: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler . Coverage with dates: https://searchengineland.com/anthropic-claude-bots-470171 and https://www.seroundtable.com/anthropic-updates-its-crawler-docs-40978.html .
- Google-Extended: "Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search." https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers .
- llms.txt: no search engine or assistant vendor has a primary statement committing to read it for web content discovery. Google's own guide (2026-07-10, linked above) says AI text files "will neither harm nor help". The llms.txt files that OpenAI, Anthropic and Perplexity publish sit on their developer documentation sites and serve coding agents reading API docs, which is a different use case from a brochure site. Ahrefs analysed 137,000 sites in May 2026 and reported 97% of llms.txt files received zero traffic; that figure comes to me through secondary summary, so mark it **unverified** pending the original post.
- Bing and Copilot do read schema: Fabrice Canel, Principal Product Manager at Microsoft Bing, said on stage at SMX Munich that "schema markup helps Microsoft's LLMs understand your content". Reported 20 March 2025: https://www.seroundtable.com/schema-llms-copilot-bing-microsoft-39093.html and https://searchengineland.com/microsoft-bing-copilot-use-schema-for-its-llms-453455 . The widely repeated claim that schema raises Copilot citation probability by about 40% comes from vendor blogs with no published method. **Unverified.**

### Implication for this site

The current `dist/robots.txt` is already `User-agent: * / Allow: / `plus a sitemap line, which is the correct policy. Adding the named user-agent blocks is optional documentation rather than a functional change, but writing them out makes the intent explicit and survives a future edit by someone who has read a blog post about blocking AI. Do not create an llms.txt. The one thing that genuinely improves the odds of being cited by an assistant is the same thing that improves the odds of ranking: a page that answers the actual question with a specific fact. The pricing tiers ($300 / $500 / $1,000 for three, six and twelve hours) are exactly the kind of extractable, non-commodity fact that gets quoted; they are already on the pages and already in `Offer` markup.

---

## 3. Core Web Vitals and page experience in 2026

### Answer

Three metrics, unchanged since INP replaced FID in March 2024:

- Largest Contentful Paint: 2.5 seconds or less
- Interaction to Next Paint: 200 milliseconds or less
- Cumulative Layout Shift: 0.1 or less

All assessed at the 75th percentile of real page loads, split by mobile and desktop. Google confirms Core Web Vitals are used by ranking systems, and equally confirms there is no single page-experience signal and that relevance wins over experience.

### Evidence

- Thresholds and the FID retirement, last updated 2024-10-31: https://web.dev/articles/vitals .
- "There is no single signal. Our core ranking systems look at a variety of signals that align with overall page experience." And "Core Web Vitals are used by our ranking systems." And "Google Search always seeks to show the most relevant content, even if the page experience is sub-par." Last updated 2025-12-10: https://developers.google.com/search/docs/appearance/page-experience .

### What matters on a static site with hero video posters and self-hosted fonts

The LCP element on each of this site's five hero pages is the poster JPEG, because every hero `<video>` is `preload="none"` with a `poster` attribute. That is already the right build. Three things decide the score:

1. The poster image must be discoverable in the initial HTML and fetched early. A `<link rel="preload" as="image">` with the matching `imagesrcset` and `imagesizes`, or `fetchpriority="high"` on the poster `<img>` if one is used, is the difference between a 1.2s and a 2.4s LCP on a slow connection.
2. Self-hosted fonts with `preload` are already in the head (`lora-latin.woff2`, `caveat-latin.woff2`). The remaining risk is CLS from a fallback-to-webfont swap. `font-display: swap` plus a size-adjusted fallback keeps the shift near zero.
3. CLS from the video swapping in over the poster. If the `<video>` and the poster share the same intrinsic aspect ratio and the container has a fixed aspect ratio in CSS, this is zero. Worth checking on the four service pages, not only the home page.

INP is close to free here: 20K of JavaScript across the whole site, no third-party tags, no chat widget.

### Implication for this site

Measure field data, not Lighthouse. Google ranks on Chrome UX Report field data over a 28-day window, and this site has no field data yet because the domain is not serving it. After cutover, watch the Core Web Vitals report in Search Console and PageSpeed Insights field section, and give it a month before judging. The 19MB of images and 12MB of video in `dist/assets` are fine because they are lazily requested, but confirm that no page requests more than one full-size hero at first paint.

---

## 4. Search Console, Bing Webmaster Tools, IndexNow and Vercel

### Answer, verification

Use a **Domain property** in Search Console, verified by a DNS TXT record added in the GoDaddy DNS manager. A domain property covers `http` and `https`, `www` and non-`www`, and every subdomain in one property, which matters here because the site will be served on `spontaneouscafe.com` and redirected from `www`. Search Console offers a guided flow for some registrars; for the rest you paste the TXT record yourself. GoDaddy is not named in Google's documentation, so use the manual TXT path: Search Console gives a string like `google-site-verification=...`, you add it as a TXT record on the root host (`@`) in GoDaddy DNS, wait for propagation, then click Verify.

Sitemap: submit `https://spontaneouscafe.com/sitemap.xml` in the Sitemaps report once. The site already generates one with eight URLs and `lastmod` dates.

URL Inspection: use it to confirm the live URL is indexable and to request indexing for the eight pages once, after cutover. It is rate-limited and not a ranking lever.

Bing: add the site at Bing Webmaster Tools and choose "Import from Google Search Console". Imported sites are automatically verified, and sitemaps come across. Bing re-validates ownership by syncing with the Google account, so if Google access is revoked you must re-verify by meta tag or DNS.

IndexNow: Bing supports it. Google does not. Google is absent from the participating-engine list on indexnow.org, and I found no Google statement adopting it after the 2021 "we will test it" remark. For a nine-page site that changes a few times a year, IndexNow is not worth wiring up.

### Answer, Vercel

- **Preview deployments are not indexable.** Vercel adds `X-Robots-Tag: noindex` to every preview deployment automatically. The one exception is a custom domain assigned to a preview branch, which does not get the header.
- **The production `*.vercel.app` alias is indexable.** Vercel's own knowledge base treats this as a duplicate-content problem to solve, not something the platform solves for you.
- **There is no dedicated dashboard toggle** named "redirect vercel.app to production domain" documented as of September 2026. Vercel's KB gives two routes: a `vercel.json` host-matched redirect (recommended, permanent, preserves paths and query strings), or a temporary hostname redirect rule in the Firewall section.

### Evidence

- Domain property versus URL-prefix, DNS TXT: https://support.google.com/webmasters/answer/9008080 . Domain properties "include data for all protocol (http/https) and subdomain variations of your property".
- Bing import from Google Search Console: https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools (September 2019, still the documented path) and https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b .
- IndexNow participants: Amazon, Bing, Naver, Seznam.cz, Yandex, Yep. Google is not listed. https://www.indexnow.org/faq .
- Vercel preview noindex, last updated 2026-08-03: https://vercel.com/kb/guide/are-vercel-preview-deployment-indexed-by-search-engines . "Preview Deployments aren't indexed by search engines" and the header to look for is `x-robots-tag: noindex`.
- Vercel duplicate-content guidance and the exact host redirect, last updated 2026-08-11: https://vercel.com/kb/guide/avoiding-duplicate-content-with-vercel-app-urls . It also recommends setting "an absolute `rel="canonical"` URL for the corresponding page on your custom domain", which this site already does.
- `has` with `type: "host"` is documented in the redirect object definition, last updated 2026-08-14: https://vercel.com/docs/project-configuration/vercel-json . `permanent: true` produces a 308; `statusCode: 301` is available if you want a 301 specifically, and the two cannot be combined.

### Implication for this site

`vercel.json` currently has one redirect (`/privacy-policy` to `/privacy/`) and no host rule. Add the host redirect before the domain goes live, so the `*.vercel.app` alias never accumulates index entries in the first place. Every page already has an absolute `rel="canonical"` pointing at `spontaneouscafe.com`, which is the second half of the fix.

---

## 5. Domain cutover

### Answer

This is two changes at once, and Google treats them separately:

1. **Hosting change, same URLs.** The domain and the home page URL stay the same, the server changes from GoDaddy to Vercel. Google's guidance: lower the DNS TTL at least a week before the switch, test that Googlebot can fetch the new host, remove any temporary crawl blocks, then flip DNS. Expect a temporary drop in Googlebot's crawl rate right after launch followed by a steady increase over the next few days.
2. **URL structure change, same domain.** The old site has two URLs (`/` and `/privacy-policy`); the new site has eight. Google's guidance: server-side permanent redirects from old URLs to new, submit a new sitemap, and do **not** use the Change of Address tool, which is only for moving between domains or subdomains.

Timing: Google gives no fixed number. For a medium site it says "a few weeks or more". For eight URLs on a domain Google already knows, most of the re-crawl will happen inside days, and the site is small enough that Googlebot will have visited every URL quickly. Keep the redirect in place for at least a year.

Request indexing per URL: yes, once, for all eight, after cutover. It is a one-off nudge, not a strategy.

GBP website link and citations: point the GBP website field at `https://spontaneouscafe.com/` (the home page), not a deep link. If the service pages are meant to be entry points, GBP's per-service and Booking link fields are the place for deep links. Then work through existing citations: anywhere the old URL string `/privacy-policy` or a GoDaddy-hosted asset path appears externally, and anywhere the business is listed with a different phone, name or URL. Name, address and phone consistency is a 12% weight signal (section 6), so the audit is worth a morning, not a month.

### Evidence

- Hosting change without URL changes, last updated 2025-12-10: https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes . "Lower the TTL value for your DNS records" a week ahead, and "it's normal to see a temporary drop in Googlebot's crawl rate immediately after the launch, followed by a steady increase over the next few days".
- Site move with URL changes, last updated 2026-08-20: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes . "We recommend server side permanent redirects from the old URLs to the new URLs as you indicated in your mapping." On the Change of Address tool: "You only need this tool when moving from one domain or subdomain to another." On timing: "for medium-sized websites, it can take a few weeks or more for Google to gradually start showing the new URLs instead of the old ones". Redirect chains should stay under three to five hops.

### Implication for this site

The one legacy URL that matters is `/privacy-policy`. `vercel.json` already redirects it to `/privacy/` with `"permanent": true`, which is a 308, and that is correct. Before flipping DNS, crawl the live GoDaddy site to confirm there is no third URL nobody has written down (an old `/contact`, a `/menu`, an image directory being hotlinked). After cutover, expect the old single-page site's rankings for "spontaneous cafe" to carry over immediately, because the home page URL does not change; the seven new URLs are net-new and start from zero.

---

## 6. Local ranking factors for a service-area business

### Answer

The current authority is Whitespark's 2026 Local Search Ranking Factors, published 6 November 2025 from 47 local search practitioners scoring 187 factors. Weights for the local pack and Maps:

| Signal group | Share |
|---|---|
| Google Business Profile | ~25% |
| Reviews | ~20% |
| Behavioural | ~18% |
| Citations | ~12% |
| Links | ~11% |
| On-page | ~10% |
| Personalisation and social | ~4% |

Top individual factors, by score: primary GBP category (227), proximity of the address to the point of search (225), keywords in the GBP business title (223), physical address in the city of search (213), business open at the time of search (189), high numerical ratings 4 to 5 stars (181), address displayed on GBP (176). Additional GBP categories sit at #8 (173).

The service-area-business finding matters here: "Showing Your Address on GBP When Business is a Service Area Business" scores 105 as a negative factor with suspension risk. A service-area business is supposed to hide the address, and the top-ranked positive factors reward having one visible. That tension is the structural disadvantage of a service-area business in the local pack, and there is no on-page fix for it.

What changed in 2025 and 2026: reviews and behavioural signals rose, on-page fell. The local pack is no longer the only local surface; Sterling Sky's tracking found AI-powered local packs on about 7% of tracked mobile US keywords, showing one or two businesses instead of three, and covering roughly 32% of the business inventory that the legacy three-pack does. Local pack ad units went from 1% of tracked queries in early 2025 to 22% by December 2025.

GBP feature changes, 2025 to 2026:
- Q&A: the API was discontinued 3 November 2025 and the consumer-facing section began being removed 3 December 2025, replaced by a Gemini-powered "Ask" button. **Sources disagree on where this ended up**: Sterling Sky logged "Revamped Q&A feature testing for GBP" on 19 August 2026, so the feature may be returning in a different form.
- Reviews: on 17 April 2026 Google added clauses to the Maps Rating Manipulation policy making review quotas, contests and per-staff incentives explicit violations, and making it a violation to ask a customer to name a specific employee. This is reported consistently across several local SEO sources; I could not pull a dated primary Google policy page to confirm the 17 April date, so treat the **date** as partially verified and the **substance** as verified by convergence.
- Messaging: Business Messages was discontinued 31 July 2024. GBP-hosted websites, in-profile chat and call history were retired earlier.
- Photos and posts: multiple practitioner sources report visibility drops for profiles that go 30+ days without new photos or updates. That is a correlation claim from agency blogs, not a controlled study. **Unverified as causal.**

### The ten things that matter most for this business

1. Primary GBP category. One field, #1 factor. "Personal chef" or "Caterer" are different categories with different query sets; pick the one matching the highest-value service and put the rest in additional categories.
2. Review volume and, more than volume, recency. 74% of consumers look for reviews from the last three months. A steady trickle beats a burst.
3. Service area set honestly in GBP, address hidden, and within roughly two hours' driving time of where the business is based.
4. GBP completeness: services list, description, hours, photos, booking or appointment link, attributes.
5. Proximity, which cannot be changed. Accept that the pack will favour businesses whose addresses sit in the searched city, and win in local organic instead.
6. Dedicated service pages with the city in the title and real detail on each service. This site already has four.
7. Name, address and phone consistency everywhere the business is listed.
8. Links from Mendocino-specific sites (section 8).
9. Review responses, quickly. 32% of consumers now expect a response within a day.
10. Behavioural signals: photos, posts and updates that keep the profile active, plus clicks, calls and direction requests that follow from everything above.

### Evidence

- Whitespark 2026 Local Search Ranking Factors, published 6 November 2025, 47 contributors, 187 factors: https://whitespark.ca/local-search-ranking-factors/ . **Sources disagree on the exact weights.** Several 2026 summaries quote GBP 32%, on-page 19%, reviews 16%, links 15%, behavioural 8%, citations 7%, personalisation 3%. Those match the 2023 edition, not the 2026 one. The figures in the table above come from the 2026 report page itself.
- Sterling Sky, "The State of Local SEO in 2026", published 26 June 2026: https://www.sterlingsky.ca/the-state-of-local-seo-in-2026/ . AI local packs on ~7% of tracked mobile US keywords; 5,943 unique businesses in AI packs versus 18,330 in regular packs; local pack ads 1% to 22% over 2025; Local Services Ads 11% to 31%.
- Sterling Sky's dated local change log, including "Revamped Q&A feature testing for GBP" on 19 August 2026: https://www.sterlingsky.ca/google-local-changes/ .
- BrightLocal Local Consumer Review Survey, published 11 February 2026, 1,002 US adults: https://www.brightlocal.com/research/local-consumer-review-survey/ . 97% read reviews; 41% always do; 31% will only use a business rated 4.5+; 68% require 4+; 74% look for reviews from the last three months; 32% expect a response within a day. Google's share as a review source fell to 71% from 83% in 2025, while ChatGPT and AI tools rose to 45% from 6%. 82% read AI-generated review summaries and 23% would decide on the summary alone.
- GBP service-area rules: https://support.google.com/business/answer/3038177 . "If you're a service-area business, you should hide your business address from customers." Service area "shouldn't extend farther than about 2 hours of driving time from where your business is based."
- GBP Q&A removal confirmed by Google in the GBP Help forum, reported by Barry Schwartz 15 December 2025: https://www.seroundtable.com/google-maps-qa-feature-ask-40594.html .

### Implication for this site

The website is roughly 10% of the local pack outcome and a larger share of local organic. The other 90% lives in GBP, reviews and citations, and none of it is a code change. The single highest-value thing anyone can do for this business in the next 30 days is get the GBP primary category right and start a review habit. The site already links its GBP via `sameAs: https://www.google.com/maps?cid=7343978535458024901`, which is the correct entity link.

---

## 7. Titles, meta descriptions, headings and sitemap lastmod

### Answer

Google generates the title link automatically from the `<title>`, the visible H1, other headings, `og:title`, anchor text and WebSite structured data. There is no character limit, and titles are truncated to fit the device width. Google rewrites a majority of titles.

The practical length guidance comes from measurement, not from Google: Zyppy's analysis of 80,959 title tags across 2,370 sites found the lowest rewrite rate, around 40%, at 51 to 55 characters, and near-100% rewriting above 70 characters. Meta descriptions are rewritten more often than titles, because Google swaps in text that matches the query.

Location in the title for local queries: no published controlled experiment exists that isolates the effect. The evidence is indirect. On-page signals carry about 10% of local pack weight in Whitespark's 2026 report, "keywords in the title" is one of the on-page factors surveyed, and Whitespark's own service-area-business guidance recommends the pattern "Top Keywords + City + Localities – Your Business Name". Mark the direct causal claim **unverified** and treat city-in-title as low-cost conventional practice rather than a proven lever.

Sitemap `lastmod`: Google uses it, conditionally. "Google uses the `<lastmod>` value if it's consistently and verifiably (for example by comparing to the last modification of the page) accurate." The value must reflect the last significant content change, and a copyright-year bump does not count. `<priority>` and `<changefreq>` are ignored entirely. The sitemap ping endpoint was retired in June 2023; submission is via Search Console or the `Sitemap:` line in robots.txt.

### Evidence

- Title link generation, no limit, truncation by device width, last updated 2025-12-10: https://developers.google.com/search/docs/appearance/title-link .
- Zyppy title rewrite study, 80,959 titles across 2,370 sites: https://zyppy.com/seo/google-title-rewrite-study/ . The 51 to 55 character sweet spot and the near-total rewriting above 70 characters come from this dataset. The study dates to 2021 with later updates; a separate 2025 analysis by John McAlpin reports 76% of titles rewritten in Q1 2025, up from 61%. **Unverified**, secondary reporting only.
- `lastmod` accuracy requirement, `priority` and `changefreq` ignored, last updated 2026-07-08: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap .
- Whitespark on service-area-business city pages, published 10 February 2025: https://whitespark.ca/blog/rank-in-cities-with-no-physical-address/ . It also names what fails: duplicate boilerplate with city names swapped, keyword stuffing, doorway pages.

### Implication for this site

The eight titles are already in good shape and in range. Measured:

| Page | Title | Chars |
|---|---|---|
| Home | The Spontaneous Cafe \| Chef Matt Samuelson, Mendocino | 52 |
| Private chef | Private Chef \| The Spontaneous Cafe, Mendocino | 45 |
| Foraging | Foraging Excursions \| The Spontaneous Cafe, Mendocino | 52 |
| Cooking classes | Cooking Classes \| The Spontaneous Cafe, Mendocino | 48 |
| Catering | Catering and Events \| The Spontaneous Cafe, Mendocino | 52 |
| About | About Matt \| The Spontaneous Cafe, Mendocino | 43 |
| Contact | Contact \| The Spontaneous Cafe, Mendocino | 40 |
| Privacy | Privacy \| The Spontaneous Cafe, Mendocino | 40 |

Four of the eight sit at 52 characters, inside Zyppy's lowest-rewrite band. Every title carries Mendocino. The H1s do not repeat the title, which is correct. The one improvement worth considering: the service titles lead with a generic service name, so "Private Chef" competes against every private chef page on the web before Mendocino appears. "Private Chef in Mendocino | The Spontaneous Cafe" is 48 characters and front-loads the query someone actually types. That is a judgment call, not a proven win.

Sitemap `lastmod` is currently emitted as a build-time date, and six of the eight URLs show `2026-09-19`, which is today's build rather than the date the content last changed. That breaks the "consistently and verifiably accurate" condition. Either derive `lastmod` from the source file's git commit date, or drop the element. A wrong `lastmod` is worse than none.

---

## 8. Links

### Answer

For a solo chef in a tourist county, the realistic link inventory is small and local, and all of it is earned by doing something a person writes about. In rough order of value:

1. Visit Mendocino County, the official destination marketing organisation. Listings on the county tourism site and any "things to do", "culinary" or "foraging" roundup it publishes.
2. Mendocino Coast Chamber of Commerce member directory. Typical chamber membership is a few hundred dollars a year and includes a directory listing and a link.
3. Local and regional press. The Mendocino Beacon, the Fort Bragg Advocate-News, the Anderson Valley Advertiser, and food coverage in the Press Democrat or the SF Chronicle. A foraging day is a story; a chef's website is not.
4. Partners with their own sites: inns, vacation rental managers, wineries, the Mendocino Art Center, retreat venues. A vacation rental manager's "what to do while you're here" page is the highest-intent link available, because the reader has already booked a house and needs a dinner.
5. Festival and event pages. The Mendocino Mushroom, Wine and Beer Festival and similar seasonal programmes list participating chefs and guides.
6. Anywhere he has taught, cooked or been credited previously (the About page names dated roles; each one is a potential link request).

What to avoid: paid directory submissions and any service selling links. Google's spam policies name "low-quality directory or bookmark site links" as link spam, and any paid placement must carry `rel="nofollow"` or `rel="sponsored"` to be compliant. A chamber membership is not a paid link scheme, because the membership buys the affiliation and the listing is incidental; a $99 "get listed on 200 directories" package is.

### Evidence

- Link spam definition and examples, last updated 2026-08-28: https://developers.google.com/search/docs/essentials/spam-policies . "Link spam is the practice of creating links to or from a site primarily for the purpose of manipulating search rankings." The examples list includes "Low-quality directory or bookmark site links" and "Exchanging money for links". Google acknowledges that "buying and selling links is a normal part of the economy of the web for advertising and sponsorship purposes" provided the links are marked.
- Links carry about 11% of local pack weight and a larger share of local organic, per Whitespark 2026 (linked in section 6).
- Citations carry about 12% of local pack weight, per the same report. Practitioner consensus is to prioritise 10 to 20 relevant listings rather than chasing volume.

### Implication for this site

The specific organisations named above are candidates from public knowledge of Mendocino County, not facts confirmed with the client. Tag them `<!-- CONFIRM -->` in any client-facing document. The About page already lists dated roles at named establishments; each of those is a concrete, non-speculative outreach target, and that is a better starting list than any directory.

---

## 9. Is a blog worth it

### Answer

Not as a general-purpose blog. Informational content is the single worst-hit category in 2026, and Google is explicit that generic content does not help. Sterling Sky's June 2026 analysis found businesses publishing blogs saw substantial organic traffic reductions, concentrated in the informational posts that previously fed the lead pages.

What still earns clicks and citations for a local experience business is content with a fact in it that cannot be generated:

- **A seasonal calendar.** What is findable on the Mendocino coast, month by month. Chanterelles after the first rain, matsutake in the fall, sea vegetables at a minus tide. This is the single strongest candidate: it is a real fact set, it is genuinely local, nobody else on the coast has published it well, and it answers the question a visitor actually has ("is it mushroom season when I'm there").
- **Pricing.** A page with real numbers on it survives, because a searcher comparing options has to land somewhere to get them. This site already has $300 / $500 / $1,000 on four pages.
- **FAQ content as page content, not as markup.** The FAQ blocks on the service pages are useful to a human and extractable by an assistant. The `FAQPage` JSON-LD wrapping them earns nothing in Google Search (section 1).
- **Itineraries.** "A day on the coast" as a structured thing a visitor can follow. Whitespark's new 2026 AI-search-visibility section ranks expert-curated lists first among factors that drive AI visibility, and dedicated service pages second.

What does not work: recipe posts (Recipe rich results exist but the category is saturated by publishers with Recipe carousels), generic "10 tips for" posts, and anything a language model can write without leaving the room.

### Evidence

- Google on unique content: "Create the content yourself based on what you know about the topic, and consider what in-depth experience you can bring to your content." Non-commodity content is contrasted against generic listicles. Last updated 2026-07-10: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide .
- Sterling Sky, 26 June 2026: businesses publishing blogs saw substantial organic traffic reductions, primarily on informational content. https://www.sterlingsky.ca/the-state-of-local-seo-in-2026/ .
- Whitespark 2026, AI search visibility section: expert-curated lists rank #1 (179 points), dedicated service pages #2, industry prominence #3. https://whitespark.ca/local-search-ranking-factors/ (6 November 2025).
- Ahrefs and Pew data on informational CTR loss, cited in section 2.

### Implication for this site

One page, not a blog. A seasonal foraging calendar at `/foraging/season/` or as a section on the existing foraging page. It needs facts from Matt about what comes up when, which is client input, not something to invent. Tag it `<!-- CONFIRM -->` until he supplies the months. Adding a blog with a posting schedule is the wrong commitment for a solo operator in 2026, because the format that lost the most traffic is exactly the format a blog produces.

---

## 10. What else a 2026 practitioner would insist on

### Image SEO and Google Images

Google's image guidance (last updated 2026-03-02, https://developers.google.com/search/docs/appearance/google-images) asks for descriptive filenames, real alt text, `srcset` and `<picture>` for responsive delivery, standard `<img>` elements rather than CSS backgrounds, and an image sitemap if images would otherwise be missed. For a business selling an experience, food photography is a genuine discovery channel, and this site has 19MB of real photographs in `dist/assets/img` with proper `srcset` widths.

Two additions worth making:
- `<meta name="robots" content="max-image-preview:large">` in the head, so Google may show a large image thumbnail. Documented at https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag (last updated 2026-03-24).
- Image entries in `sitemap.xml`, or at minimum confirm that every photo is reachable from a crawled page's HTML.

### Video SEO for hero loops

Do not mark them up. Google requires a watch page whose "main purpose is to show users a single video", and explicitly excludes videos that are "complementary to the rest of the content" (last updated 2025-12-18, https://developers.google.com/search/docs/appearance/video). The five hero loops here are `aria-hidden="true"` decorative backgrounds. `VideoObject` markup on them would be inaccurate and would earn nothing. If Matt ever publishes a real instructional video, YouTube is the distribution channel, and Sterling Sky's 2026 recommendations name YouTube and Reddit as authority surfaces worth building on.

### Google "Things to do"

The Operator Business Module lets a tour or activity operator show bookable products on their Google Business Profile. Requirements, per Google's own partner documentation (last updated 2026-04-01, https://developers.google.com/actions-center/verticals/things-to-do/guides/partner-integration/overview): the operator's business must be findable on Google Maps, products are submitted as a JSON feed over SFTP, the full activity set must be re-uploaded at least once every 30 days, and Google reserves the right to take down inactive feeds. That is a booking-platform integration, not a website change. Secondary sources describe a self-serve "Tickets & Activities Editor" and one-to-two-week onboarding through a connectivity partner; I could not confirm either from Google's documentation. **Unverified.** For a solo chef with no booking system, this is a "revisit if he adopts a booking platform" item, not a now item.

### Reserve with Google

Requires a supported scheduling provider in a supported country (https://support.google.com/reserve/answer/9172607). Google expanded Local Services Ads booking partners from roughly 20 to over 500 in August 2026, which suggests the door is wider than it was. Same conclusion as Things to do: it follows a booking system, it does not precede one. GBP's plain "Appointment link" field points at the contact page today and costs nothing.

### Google Posts

Still live. Behavioural signals are about 18% of pack weight in the 2026 Whitespark report, and posts and photos are how a solo operator generates them. A post when mushroom season starts and a post when the summer calendar opens is two posts a year and probably enough.

### Apple

Apple Business Connect was folded into a platform called Apple Business. `businessconnect.apple.com` now issues a 302 to `business.apple.com` (verified 2026-09-19). Listing management stays free, and the listing drives Apple Maps, Siri, Spotlight, Safari and Wallet. Apple Maps Ads is the paid layer. For a business whose customers are iPhone-carrying visitors renting houses on the coast, a claimed Apple listing with good photos is genuinely worth 30 minutes. The rebrand date of 14 April 2026 comes from secondary sources; the redirect is verified, the date is **unverified**.

### Bing Places and Bing Webmaster Tools

Free, and it feeds Bing Search, Bing Maps and Microsoft Copilot. Microsoft moved it to `bing.com/forbusiness` in a late-2025 relaunch. The widely repeated claim that ChatGPT search runs on Bing's index is stale; OpenAI documents its own `OAI-SearchBot` crawler, so treat "Bing powers ChatGPT" as **unverified and probably wrong** in 2026. Bing Places still matters for Copilot and for Bing Maps data licensees. Claim it, then leave it.

### Merchant Center for experiences

Google opened Search campaigns for Travel to Things to Do and Events in beta on 8 July 2026 (secondary sources). This is a paid-advertising surface. Not relevant to an unpaid solo operator.

---

## Exact snippets

### robots.txt

Replace `src/assets/robots.txt` (or wherever the build sources it) with this. It changes nothing functionally versus the current allow-all file; it makes the intent explicit so a future editor does not "helpfully" block the AI crawlers.

```
# Allow every crawler, including AI search and assistant crawlers.
User-agent: *
Allow: /

# Google generative AI training and grounding outside Search.
# Allowing this does not affect Google Search inclusion either way.
User-agent: Google-Extended
Allow: /

# OpenAI: ChatGPT search surface, then model training.
User-agent: OAI-SearchBot
Allow: /

User-agent: GPTBot
Allow: /

# Perplexity search index.
User-agent: PerplexityBot
Allow: /

# Anthropic: search index, user-initiated fetch, model training.
User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: ClaudeBot
Allow: /

# Microsoft Bing and Copilot.
User-agent: bingbot
Allow: /

Sitemap: https://spontaneouscafe.com/sitemap.xml
```

Do not create an `llms.txt`. Google states AI text files "will neither harm nor help" (https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-07-10).

### vercel.json, redirect the vercel.app host to the custom domain

This is Vercel's own snippet from https://vercel.com/kb/guide/avoiding-duplicate-content-with-vercel-app-urls (last updated 2026-08-11), adapted to this project. Replace `your-project` with the actual Vercel project subdomain.

```json
{
  "redirects": [
    {
      "source": "/:path*",
      "has": [{ "type": "host", "value": "your-project\\.vercel\\.app" }],
      "destination": "https://spontaneouscafe.com/:path*",
      "permanent": true
    },
    { "source": "/privacy-policy", "destination": "/privacy/", "permanent": true }
  ]
}
```

Notes from the `vercel.json` reference (https://vercel.com/docs/project-configuration/vercel-json, last updated 2026-08-14):

- `has` accepts `type` values `header`, `cookie`, `host` and `query`. The `host` entry takes no `key`.
- The dots in the host value are escaped because `value` is treated as a regex-like string.
- `"permanent": true` emits a 308. If a 301 is required instead, use `"statusCode": 301` and drop `"permanent"`. The two cannot be combined.
- `has` does not work under `vercel dev` locally, only when deployed.
- Order matters: the host rule must not match requests already on the custom domain, or you get a loop. It does not, because `has` only fires when the request host is the vercel.app one.

### Meta tags to add to the shared head

```html
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
```

`max-image-preview:large` allows a large image thumbnail. `max-snippet:-1` and `max-video-preview:-1` set no limit, which is the default; stating them explicitly documents the choice and prevents an accidental restriction. All three directives are documented at https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag (last updated 2026-03-24).

### WebSite node for the site name (add once, on the home page)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://spontaneouscafe.com/#website",
  "url": "https://spontaneouscafe.com/",
  "name": "The Spontaneous Cafe",
  "publisher": { "@id": "https://spontaneouscafe.com/#business" }
}
```

Do not add `potentialAction` / `SearchAction`. The sitelinks search box it powered was removed on 21 November 2024 (https://developers.google.com/search/blog/2024/10/sitelinks-search-box).

### Entity graph fix, one business instead of five

On the home page, add an `@id` to the existing `LocalBusiness` node:

```json
{ "@type": "LocalBusiness", "@id": "https://spontaneouscafe.com/#business", "...": "..." }
```

On the four service pages, replace the inline `provider` object with a reference:

```json
{
  "@type": "Service",
  "provider": { "@id": "https://spontaneouscafe.com/#business" }
}
```

And remove the `LocalBusiness` JSON-LD block from `404.html`.

### BreadcrumbList, per service page

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://spontaneouscafe.com/" },
    { "@type": "ListItem", "position": 2, "name": "Foraging Excursions", "item": "https://spontaneouscafe.com/foraging/" }
  ]
}
```

Desktop-only since 23 January 2025, and the markup is still supported (https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs).

---

## Top 10 actions for this site

Ordered by impact first, then by effort.

| # | Action | Impact | Effort | Source |
|---|---|---|---|---|
| 1 | Set the GBP primary category correctly, hide the address as a service-area business, set the service area inside a two-hour drive, and fill services, description, hours and photos. Nothing on the website beats this. | Highest. GBP is ~25% of pack weight and primary category is the #1 individual factor. | 1 to 2 hours, client-side | https://whitespark.ca/local-search-ranking-factors/ (2025-11-06); https://support.google.com/business/answer/3038177 |
| 2 | Start a review habit: ask every completed booking, respond within a day, keep it continuous rather than bursty. No quotas, no contests, no asking anyone to name staff. | Very high. Reviews ~20% of pack weight; 74% of consumers want reviews from the last three months. | Ongoing, client-side | https://www.brightlocal.com/research/local-consumer-review-survey/ (2026-02-11); Google Maps Rating Manipulation policy update, 17 April 2026 |
| 3 | Add the `vercel.json` host redirect before DNS cutover so `*.vercel.app` never gets indexed. | High. Prevents a duplicate-content problem that is cheap now and annoying later. | 10 minutes | https://vercel.com/kb/guide/avoiding-duplicate-content-with-vercel-app-urls (2026-08-11) |
| 4 | Run the cutover properly: lower GoDaddy DNS TTL a week ahead, crawl the old site for any URL not in the redirect map, flip DNS, verify the Search Console Domain property by DNS TXT, submit the sitemap, inspect and request indexing for all eight URLs once. | High. This is the difference between a two-day recovery and a two-month one. | Half a day | https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes (2025-12-10); https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes (2026-08-20) |
| 5 | Fix `lastmod` in the sitemap so it reflects the last real content change per page, or remove the element entirely. Six of eight URLs currently carry today's build date. | Medium-high. Google only uses `lastmod` when it is "consistently and verifiably accurate"; a wrong one is worse than none. | 30 minutes in `build.py` | https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap (2026-07-08) |
| 6 | Add `@id` to the LocalBusiness node, point every `Service.provider` at it, add `WebSite`, add `BreadcrumbList` to the four service pages, remove the JSON-LD from `404.html`. | Medium-high. Turns five disconnected business declarations into one entity and restores the desktop breadcrumb line. | 1 hour | https://developers.google.com/search/docs/appearance/structured-data/search-gallery (2026-06-15) |
| 7 | Add `max-image-preview:large` to the shared head and verify LCP: preload the hero poster with a matching `imagesrcset`, and confirm the video container has a fixed aspect ratio so the loop swap causes no layout shift. | Medium. LCP 2.5s and CLS 0.1 are the thresholds; the posters are already the right architecture. | 1 hour | https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag (2026-03-24); https://web.dev/articles/vitals (2024-10-31) |
| 8 | Publish one seasonal foraging calendar page built on facts Matt supplies. Not a blog. | Medium. Expert-curated lists rank #1 in Whitespark's new AI-visibility section, and this is the one piece of content nobody else on the coast has. | Half a day plus client input | https://whitespark.ca/local-search-ranking-factors/ (2025-11-06); https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (2026-07-10) |
| 9 | Work six local links: Visit Mendocino County, the Mendocino Coast Chamber, two vacation rental or inn partners, one festival page, one press pitch on a foraging day. Skip every paid directory package. | Medium. Links ~11% and citations ~12% of pack weight, more in local organic. | Ongoing, a few hours a month | https://developers.google.com/search/docs/essentials/spam-policies (2026-08-28) |
| 10 | Claim the free listings: Bing Places at `bing.com/forbusiness`, Apple Business at `business.apple.com`, then import the site into Bing Webmaster Tools from Search Console. | Low-medium individually, near-zero cost. Apple Maps matters for iPhone-carrying visitors; Bing feeds Copilot. | 1 hour total | https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b; https://business.apple.com/ |

Explicitly not recommended, with reasons:

- **llms.txt.** Google says it neither helps nor harms, and no vendor has a primary commitment to read one for web discovery.
- **IndexNow.** Bing supports it, Google does not, and eight pages that change a few times a year do not need a push protocol.
- **New FAQPage markup.** The rich result is gone as of 7 May 2026. Keep the FAQ text as page content, which is where its value is.
- **VideoObject on the hero loops.** They are decorative and do not meet Google's watch-page requirement.
- **Course markup on the cooking classes.** `Course info` was deprecated 12 June 2025, and `Course list` needs three courses in a carousel with an educational-curriculum definition this does not meet.
- **Google Things to do and Reserve with Google.** Both need a booking platform first. Revisit if one is adopted.
- **A blog.** Informational posts are the worst-hit format in 2026.
