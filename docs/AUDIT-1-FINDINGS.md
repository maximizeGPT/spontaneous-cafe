
## PERFORMANCE  confirmed 7
- [blocker] Mobile LCP fails on every page, including /contact/, because the Google Fonts stylesheet is render-blocking
    where: src/layout.html:19 (link rel=stylesheet href=https://fonts.googleapis.com/css2?...&display=swap); live: https://spontaneous-cafe.vercel.app/contact/
    fix: Self-host the woff2 files under /assets/fonts/ (Lora 400/500/400i, Caveat 700, Source Sans 3 400/600/400i; they are variable files, Lora 500 and 600 already share one file), declare @font-face in site.css with font-display: swap, add <link rel=preload as=font type=font/woff2 crossorigin> for only the two hero faces (Lora 500, Caveat 700), and delete the fonts.googleapis.com lin
- [major] Hero video autoplays a 2.8-3.9 MB 1280px MP4 on mobile during page load and competes with LCP resources
    where: src/pages/index.html:6-8 and src/pages/foraging.html:6-8 (video autoplay muted loop preload="metadata"); dist/assets/video/foraging-moss.mp4, dist/ass
    fix: Re-encode both loops at ~1.0-1.2 Mbps (ffmpeg -c:v libx264 -crf 28 -preset slow -movflags +faststart -an) and add a 720 px wide variant; serve it with <source media="(max-width: 700px)" src="...-720.mp4"> before the 1280 source. Change to preload="none" and drop the autoplay attribute; in site.js, after window 'load' (and only when prefers-reduced-motion is not set and the elem
- [major] One-year immutable cache on unfingerprinted CSS and JS means returning visitors keep stale assets after a deploy
    where: vercel.json:7 ('/assets/(.*)' -> Cache-Control: public, max-age=31536000, immutable); src/layout.html:20 and :81 reference /assets/css/site.css and /a
    fix: Fingerprint in build.py: hash site.css and site.js (and ideally images) at build time, write them as site.<hash>.css / site.<hash>.js, and substitute the hashed paths into layout.html output. Keep the immutable header for hashed files only; add a second vercel.json header rule for unhashed assets (or the img/video folders) of 'public, max-age=86400, stale-while-revalidate=60480
- [major] Below-fold JPEGs are served at 1600-1800 px with no srcset or modern format, adding ~1.8 MB per page
    where: src/pages/index.html:34,42,50,58 (service cards, 800x600 slots), :95-99 (photo grid, 600x600 slots), :142; src/pages/foraging.html:35,214-224; dist/as
    fix: Add an image step to build.py (Pillow, or a one-off script in tools/) that emits 480, 800 and 1200 px widths as WebP (quality 75) plus a JPEG fallback, then render <img srcset="...480w, ...800w, ...1200w" sizes="(max-width: 700px) 100vw, 33vw"> for the cards/grid and sizes="(max-width: 700px) 100vw, 50vw" for the figures. Cap source width at 1200 px; nothing on the site renders
- [minor] The wordmark SVG is a 20.7 KB traced bitmap inlined twice in every page, 41 KB of the 47-67 KB HTML
    where: src/assets/logo/wordmark.svg and wordmark-light.svg (20,689 bytes each, 2 <path> elements with thousands of nodes, viewBox 2050x736); inlined by build
    fix: Run the SVG through svgo with path simplification (or re-trace with fewer nodes; a wordmark this size should be 2-4 KB), and inline only the header copy. For the footer use the same symbol via <svg><use href="#wordmark"/></svg> with a currentColor fill so wordmark-light.svg is not needed at all.
- [minor] prefers-reduced-motion users still download the hero video because the fetch starts before site.js runs
    where: src/assets/js/site.js:21-22 (removeAttribute('autoplay') after DOM parse); src/pages/index.html:6 and foraging.html:6 (autoplay attribute in markup)
    fix: Covered by the video fix above: ship the <video> without autoplay and with preload="none", and let site.js attach the source and call play() only when the reduced-motion query is false. Alternatively wrap the <source> in a <template> and clone it in JS.
- [minor] Web-font swap causes small layout shifts on the hero h1 and body text
    where: src/assets/css/site.css:22-24 (font stacks: Lora/Georgia, Caveat/Bradley Hand, Source Sans 3/Helvetica Neue); src/layout.html:19 (display=swap)
    fix: When self-hosting, add size-adjusted fallbacks: @font-face { font-family: 'Lora Fallback'; src: local('Georgia'); size-adjust: 106%; ascent-override: 92%; } (tune with fontaine or the Chrome DevTools font-metrics overrides) and put the fallback family between the web font and the system font in each stack. Preloading Lora 500 and Caveat 700 also shortens the swap window.

## ACCESSIBILITY  confirmed 11
- [major] Focus ring (butter on linen/paper) is below 3:1, so keyboard focus is barely visible on every light section
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/css/site.css:74 (`:focus-visible { outline: 3px solid var(--butter) }`)
    fix: Use a dark ring on light backgrounds and keep butter only on dark ones: `:focus-visible { outline: 3px solid var(--green); outline-offset: 3px; }` (green on linen 9.98:1, paper 11.17:1, linen-deep 8.78:1) and `.section--green :focus-visible, .cta :focus-visible, .site-footer :focus-visible, .hero :focus-visible, .btn:focus-visible { outline-color: var(--butter); }` (butter on g
- [major] --ink-mute text fails 4.5:1 everywhere it is used at 13-15px (help text, captions, timeline times, course labels, menu footers, price units)
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/css/site.css:10 (token), :224 (.figure figcaption), :236 (.day__time), :258 (.course__label), :261 (.menu
    fix: Darken the token so it clears 4.5:1 on the darkest surface it sits on: `--ink-mute: #655F52` (linen 5.26:1, paper 5.88:1, linen-deep 4.62:1). If the lighter look must stay, restrict --ink-mute to 24px+ text and give the 13-15px uses --ink-soft (#5A564C, 6.07:1 on linen).
- [major] Contact form field boundaries are below 3:1, so inputs are hard to find on the linen page
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/css/site.css:333 (`.field input, .field select, .field textarea { border: 1px solid var(--line-strong); b
    fix: Raise the border to a colour that clears 3:1 on both surfaces, e.g. `border-color: var(--ink-mute)` (#7E786A: 4.07:1 on paper, 3.64:1 on linen) or a 2px `--line-strong` plus `--ink-mute` on hover/focus. Keep the green focus border at site.css:335.
- [major] Closed mobile nav stays in the tab order and accessibility tree (hidden with opacity only)
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/css/site.css:165-172 (`.nav { opacity: 0; pointer-events: none }` / `.nav.is-open { opacity: 1 }`); toggl
    fix: Add `visibility: hidden` to the closed state and keep the fade: `.nav { visibility: hidden; transition: opacity var(--dur) var(--ease-out), transform var(--dur) var(--ease-out), visibility 0s linear var(--dur); }` and `.nav.is-open { visibility: visible; transition-delay: 0s; }` inside the max-width:900px block. Alternatively toggle the `inert` attribute in site.js alongside is
- [major] Autoplaying looped hero video has no pause/stop control
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/index.html:6, src/pages/foraging.html:6, src/pages/private-chef.html:6, src/pages/catering.html:6, src/pag
    fix: Add a small toggle inside `.hero__inner` (or bottom-right of .hero__media): `<button class="hero__pause btn btn--ghost" type="button" aria-pressed="false">Pause video</button>` and in site.js wire it to `v.paused ? v.play() : v.pause()`, updating the label/aria-pressed. Hide the button when reduced motion already stopped the video.
- [major] Contact page does not reflow at 320px: the 24px email link is an unbreakable 353px string
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/contact.html:70 (`<p class="big"><a href="mailto:chefmattsamuelson@gmail.com">chefmattsamuelson@gmail.com<
    fix: Add `.contact-aside .big a[href^="mailto"] { overflow-wrap: anywhere; }` (or `word-break: break-all` for that one link), or drop the email to `var(--text-lg)` on screens under 400px.
- [major] 13px butter hero eyebrow depends on the photo for its contrast; the scrim alone does not guarantee 4.5:1
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/css/site.css:187 (.hero__scrim gradients) and :190 (`.hero .eyebrow { color: var(--butter) }`); markup sr
    fix: Either switch the eyebrow to `var(--paper)` (5.04:1 over the same worst-case pixel) or strengthen the vertical gradient start from rgba(38,30,22,0.22) to about 0.45 so the top of the text block gets the same protection as the bottom. Re-check with the final posters.
- [minor] Form help text is not programmatically associated with its field
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/contact.html:46 (`<span class="help">Rough is fine</span>`) and :55 (`<span class="help">Where you're stay
    fix: Give each span an id and reference it: `<input type="date" id="date" name="date" aria-describedby="date-help">` + `<span class="help" id="date-help">Rough is fine</span>`; same for the textarea with `aria-describedby="message-help"`.
- [minor] Required-field asterisks are read aloud as 'star' and are never explained
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/contact.html:20, 24, 32, 53 (`<span class="req">*</span>`)
    fix: Add `aria-hidden="true"` to each `.req` span and a one-line note above the form such as `<p class="small">Fields marked <span class="req">*</span> are required.</p>`, or replace the span with `<abbr class="req" title="required">*</abbr>`.
- [minor] Footer headings jump from h2 to h4 on every page
    where: /Users/main/MOSI/Spontaneous Cafe/src/layout.html:55 and :65 (`<h4>Experiences</h4>`, `<h4>Chef Matt</h4>`)
    fix: Change both footer headings to `<h2 class="footer-heading">` and move the current h4 styling in site.css:349 to `.site-footer .footer-heading` (or use `<p class="footer-heading">` if they should not appear in the heading outline at all).
- [minor] Season tabs: no-JS users see no season content, and Home/End keys are not handled
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/foraging.html:76, 95, 114, 133 (every `<div role="tabpanel" ... hidden>`); same pattern in private-chef.ht
    fix: Remove `hidden` from the first panel in the HTML and set the first tab to aria-selected="true" tabindex="0" (JS re-selects by season anyway). In site.js extend the keydown map: `e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : ...`.

## MOBILE  confirmed 10
- [blocker] Contact page overflows the viewport at 360px; form inputs run 13px off the right edge
    where: src/assets/css/site.css:118 (.split { grid-template-columns: 1fr } at max-width 900px) with src/assets/css/site.css:341 (.contact-aside .big 24px) and
    fix: In the max-width 900px block change `.split { grid-template-columns: 1fr }` to `minmax(0, 1fr)` (same fix for the 760px footer rule). Then let the email break: `.contact-aside .big a { overflow-wrap: anywhere; }` or drop `.contact-aside .big` to `clamp(1.05rem, 5.5vw, 1.5rem)` so the address fits 320px.
- [major] Footer email link overflows its column between 761px and 950px, causing horizontal page scroll on every page (iPad 768/820/834)
    where: src/assets/css/site.css:346 (.site-footer .wrap grid minmax(0,2fr) repeat(2, minmax(0,1fr)), gap 2rem) and :354 (2-column switch only at max-width 760
    fix: Move the footer's two-column breakpoint from 760px to 960px (`@media (max-width: 960px) { .site-footer .wrap { grid-template-columns: minmax(0,1fr) minmax(0,1fr); } }`) and add `.site-footer a { overflow-wrap: anywhere; }` as a guard.
- [major] Header and nav-drawer 'Contact' button renders dark ink text on the red background (1.76:1)
    where: src/assets/css/site.css:157 (.nav a { color: var(--ink) }) overriding :131 (.btn color); :160 and :175 (.nav .btn) never set color; src/layout.html:38
    fix: Add `color: var(--linen);` to `.nav .btn` (line 160) and `.nav .btn:hover { color: var(--linen); }`, or write the button as `.nav a.btn`.
- [major] Private chef and catering price amounts render at 15px instead of 36px because they are <p> elements
    where: src/pages/private-chef.html:190, 204, 216 and src/pages/catering.html:181, 195 (<p class="price__amount">); src/assets/css/site.css:282 (.price__amoun
    fix: Either change the five <p class="price__amount"> to <span> to match foraging/cooking-classes, or raise the CSS specificity: `.price .price__amount { font-size: var(--text-3xl); }`.
- [major] Tap targets under 44px: footer links, season tabs, drawer Contact button, inline phone/email links
    where: src/assets/css/site.css:350 (.site-footer ul gap 0.5rem, 15px links), :266 (.tabs button min-height 40px), :160/:175 (.nav .btn min-height 42px), :323
    fix: Footer: `.site-footer ul { gap: var(--space-3) } .site-footer li a { display: inline-block; padding: 0.3rem 0; }`. Tabs: `min-height: 44px`. Drawer: `.nav .btn { min-height: 48px }` in the 900px block. CTA band: `.cta__contact a { display: inline-block; padding: 0.4rem 0; }` and break the two links onto separate lines under 600px.
- [minor] Most secondary reading copy is 15px and labels are 13px on mobile, below the 16px threshold
    where: src/assets/css/site.css:26-27 (--text-xs 13px, --text-sm 15px) applied by :212 .service__body p, :238 .day__step p, :247, :260 .course p, :285-286 .pr
    fix: In `@media (max-width: 600px)` set `:root { --text-sm: 1rem; --text-xs: 0.875rem; }`, or at minimum promote the reading copy (`.day__step p, .price p, .price ul, .details dd, .course p, .service__body p, .field label`) to `var(--text-md)` on mobile.
- [minor] Footer columns collapse to 97px / 203px at phone widths; link labels wrap and the email spills into the gutter
    where: src/assets/css/site.css:354 (.site-footer .wrap { grid-template-columns: 1fr 1fr } at max-width 760px); src/layout.html:56-73
    fix: Use `grid-template-columns: repeat(2, minmax(0, 1fr))` at the 760px breakpoint plus `.site-footer a { overflow-wrap: anywhere; }`, or stack the footer to one column at max-width 480px.
- [minor] 'Confirm with Matt' tag stretches to the full width of the price card
    where: src/assets/css/site.css:281 (.price display:flex; flex-direction:column) and :289 (.tag-confirm display:inline-block); src/pages/foraging.html:190, sr
    fix: Add `align-self: flex-start;` to `.tag-confirm` (or wrap it in a div).
- [minor] 600 to 900px gap: price cards and sub-experience cards are forced to one column, producing 707px-wide cards and three stacked 530px-tall images at 768px
    where: src/assets/css/site.css:290 (.prices { grid-template-columns: 1fr } at max-width 900px) and :305 (.subs one column at max-width 900px)
    fix: Remove the 900px override for `.prices` (auto-fit already yields one column below ~600px) and move `.subs` to two columns between 600px and 900px: `@media (max-width: 900px) { .subs { grid-template-columns: repeat(2, minmax(0,1fr)); } } @media (max-width: 600px) { .subs { grid-template-columns: 1fr; } }`.
- [minor] Contact form inputs shrink to 169-196px wide between 901px and about 1100px
    where: src/assets/css/site.css:111 (.split minmax(0,5fr) minmax(0,6fr)) with :328 (.form two columns) and :339 (single column only below 600px); src/pages/co
    fix: Give the form the wider column on this page (`.split--form { grid-template-columns: minmax(0,7fr) minmax(0,4fr); }`) or use a container query: `.split { container-type: inline-size } @container (max-width: 520px) { .form { grid-template-columns: 1fr } }`.

## SEO  confirmed 11
- [major] Canonical, robots Sitemap and sitemap <loc> all point at spontaneouscafe.com, where 5 of 7 target URLs currently return 404 on the old GoDaddy site, and there is no host redirect plan for the vercel.app domain
    where: src/layout.html:8 and :13 (canonical, og:url); build.py:17 SITE constant feeding sitemap.xml lines 105-113 and robots.txt line 116; vercel.json (no ho
    fix: Until DNS switch: add to vercel.json a headers rule with "has": [{"type":"host","value":"spontaneous-cafe.vercel.app"}] and "X-Robots-Tag: noindex" so the staging host is not indexed against 404 canonicals. After DNS switch: replace it with a redirects rule (same has:host match, "destination": "https://spontaneouscafe.com/:path*", "permanent": true) so vercel.app 308s to the ap
- [minor] Target phrases appear in zero headings; 'Mendocino' is absent from every h1/h2/h3 on all 8 pages
    where: src/pages/private-chef.html:14, src/pages/catering.html:14, src/pages/foraging.html:14, src/pages/cooking-classes.html:14, src/pages/index.html:14 (h1
    fix: Keep the voice h1s but give each service page one keyword-bearing heading near the top, e.g. add an h2 under the hero: private-chef 'Private chef on the Mendocino coast', catering 'Catering and event cooking in Mendocino County', foraging 'Foraging excursions around Mendocino', cooking-classes 'Cooking classes in Mendocino, in your kitchen'. Alternatively extend the h1 with a s
- [minor] Service pages carry no business entity and the Service schema has no offers, serviceType or provider contact details
    where: build.py:49-57 (Service block replaces LocalBusiness entirely when meta.service is set); output in dist/private-chef/index.html, dist/catering/index.h
    fix: Emit a single @graph per page: the full LocalBusiness object with "@id": SITE + "/#business" (and image, geo, hours per the next finding), plus the Service with "provider": {"@id": SITE + "/#business"}, "serviceType": meta['service'], "image": og image URL, and an "offers": {"@type":"Offer","priceCurrency":"USD","price" or "priceSpecification":{"@type":"PriceSpecification","min
- [minor] LocalBusiness lacks image, geo, openingHoursSpecification and streetAddress/postalCode; foundingDate disagrees with page copy
    where: build.py:32-48 (base LocalBusiness dict); src/pages/about.html:9 and src/pages/index.html:147 say 'since 2008', build.py:41 says foundingDate 2009
    fix: Add "image": [SITE+"/assets/img/matt.jpg", SITE+"/assets/img/home-poster.jpg"], "geo": {"@type":"GeoCoordinates","latitude":39.3077,"longitude":-123.7995} (Mendocino village, adjust to Matt's base), "openingHoursSpecification": [{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday",...,"Sunday"],"opens":"08:00","closes":"20:00"}] if he takes calls on a schedule, and postal
- [minor] No Twitter card tags, no og:image:width/height/alt, no og:locale; the About og:image is portrait and will be cropped
    where: src/layout.html:9-14 (Open Graph block); src/pages/about.html:2 og_image matt.jpg
    fix: After src/layout.html:14 add: <meta name="twitter:card" content="summary_large_image">, <meta name="twitter:title" content="{{title}}">, <meta name="twitter:description" content="{{description}}">, <meta name="twitter:image" content="https://spontaneouscafe.com/assets/img/{{og_image}}">, plus <meta property="og:locale" content="en_US"> and og:image:width/height emitted by build
- [minor] Catering meta description is 161 characters, one over the 160 cap
    where: src/pages/catering.html:2
    fix: Drop 'greater' ('across Mendocino') or 'rehearsal' from the catering description to land at 150-155 characters.
- [minor] sitemap.xml stamps every URL with the build date as lastmod
    where: build.py:105-113 (today = datetime.date.today(); same value written to every <lastmod>)
    fix: Derive lastmod per page from git: subprocess.run(['git','log','-1','--format=%cs','--',src_path]) with fallback to file mtime, and also bump it when src/layout.html changes. Or drop <lastmod> entirely until per-page dates exist.
- [minor] FAQPage extraction regex only captures the first paragraph of each answer and requires a bare <details> tag
    where: build.py:62-68 (faq_jsonld), regex at line 64
    fix: Change the regex to r'<details[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>' and run clean() on the whole captured answer body so multi-paragraph answers serialize fully.
- [minor] Old-site URL /privacy-policy has no redirect and will 404 after cutover
    where: vercel.json (no redirects array)
    fix: Add to vercel.json: "redirects": [{"source": "/privacy-policy", "destination": "/privacy/", "permanent": true}]. Check the GoDaddy site for any other linked anchors (none in its sitemap) before switching DNS.
- [minor] No custom 404 page; Vercel serves an unbranded plain-text NOT_FOUND with no title or navigation
    where: dist/ (no 404.html); build.py:83-101 builds every src page to <slug>/index.html so a 404 page would need a special case
    fix: Add src/pages/404.html with the standard meta block and in build.py write slug '404' to dist/404.html instead of dist/404/index.html (Vercel serves a root 404.html automatically for static output). Exclude it from the sitemap loop.
- [minor] Only 2 of 27 unique alt texts carry a location term; the four home service cards are natural spots for one
    where: src/pages/index.html:34, :42, :50, :58 (svc-*.jpg alts); src/pages/private-chef.html plate.jpg alt; src/pages/foraging.html src-forest.jpg alt
    fix: Where the photo is actually local, add the place: index.html:34 'Chanterelles in a basket on a Mendocino forest floor', :42 'Plating a private chef dinner in a Mendocino rental kitchen', :50 'Long catering table set under trees in Mendocino County', :58 'Knife skills class on a cutting board in Mendocino'. Do this only for real local photos once the placeholders are swapped; do

## SECURITY  confirmed 8
- [major] One-year immutable cache on unfingerprinted site.css and site.js
    where: https://spontaneous-cafe.vercel.app/assets/js/site.js header cache-control: public, max-age=31536000, immutable; /Users/main/MOSI/Spontaneous Cafe/ver
    fix: In build.py, compute sha256 of site.css and site.js, write them as dist/assets/css/site.<hash8>.css and dist/assets/js/site.<hash8>.js, and replace the two references in layout.html at build time. Alternatively keep the names and append ?v=<hash8> to the two hrefs. If neither, split the vercel.json rule: /assets/(img|video|logo)/(.*) keeps immutable, and /assets/(css|js)/(.*) g
- [minor] No Content-Security-Policy on any response
    where: https://spontaneous-cafe.vercel.app/ (curl -sI: no content-security-policy header; same on /contact/, /assets/css/site.css, /assets/js/site.js); /User
    fix: Add to vercel.json headers: { "source": "/(.*)", "headers": [ { "key": "Content-Security-Policy", "value": "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; style-src-attr 'unsafe-inline'; font-src https://fonts.gstatic.com; img-src 'self' data:; media-src 'self'; connect-src 'self' https://formspree.io; form-action 'self' https://formspree.
- [minor] api/notify.js is an unauthenticated SMS relay (pending, wired in uncommitted site.js)
    where: /Users/main/MOSI/Spontaneous Cafe/api/notify.js lines 32-46; /Users/main/MOSI/Spontaneous Cafe/src/assets/js/site.js line 81 (uncommitted, not yet liv
    fix: Before deploying: (1) keep CONFIRM_INQUIRER unset, or drop inquirer SMS entirely; (2) reject requests whose Origin header is not the site origin; (3) add a per-IP limiter (Vercel KV or Upstash, e.g. 5 per hour) and return 429; (4) require a shared token in a custom header that site.js sends, or better, switch to a Formspree webhook so only Formspree can trigger the notify path;
- [minor] No clickjacking protection on the contact form page
    where: https://spontaneous-cafe.vercel.app/contact/ (curl -sI: no x-frame-options, no content-security-policy frame-ancestors)
    fix: Add to the /(.*) header block in vercel.json: { "key": "X-Frame-Options", "value": "DENY" } and include frame-ancestors 'none' in the CSP from finding 1. Both are needed: XFO for older browsers, frame-ancestors for current ones.
- [minor] Privacy page omits Formspree, the third party that receives and stores every inquiry
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/privacy.html line 21 and lines 26-27; /Users/main/MOSI/Spontaneous Cafe/src/pages/contact.html line 16
    fix: Add one sentence under "What I collect" or "Other people's servers": "The form is handled by Formspree (formspree.io), which forwards it to my email and keeps a copy of the submission on its servers under its privacy policy." Name Vercel as the host ("hosted on Vercel") so the server-log sentence is concrete. If api/notify.js ships, add Twilio and Telegram in the same sentence.
- [minor] Missing X-Content-Type-Options, Referrer-Policy and Permissions-Policy
    where: https://spontaneous-cafe.vercel.app/ and https://spontaneous-cafe.vercel.app/assets/css/site.css (curl -sI: none of the three headers present); /Users
    fix: Add to the /(.*) header block in vercel.json: { "key": "X-Content-Type-Options", "value": "nosniff" }, { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }, { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=()" }.
- [minor] Internal CONFIRM comments shipped to production HTML on 7 of 8 pages
    where: https://spontaneous-cafe.vercel.app/contact/ line 430, https://spontaneous-cafe.vercel.app/privacy/ line 349, https://spontaneous-cafe.vercel.app/fora
    fix: In build.py after line 88 (body = raw[m.end():]) add: body = re.sub(r'<!--.*?-->', '', body, flags=re.S). The meta block is already consumed by then, so only body comments are stripped. Keep the notes in src.
- [minor] Internal media manifests are published under /assets/
    where: https://spontaneous-cafe.vercel.app/assets/MANIFEST.md (200, text/markdown) and https://spontaneous-cafe.vercel.app/assets/MANIFEST-photos.md (200); /
    fix: Change build.py:75 to shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(DIST, 'assets'), ignore=shutil.ignore_patterns('*.md')) or move both manifests to docs/.

## FORMS  confirmed 10
- [major] Service select silently defaults to "Foraging excursion" on every path that arrives without ?service=
    where: src/pages/contact.html:33-41 (live: https://spontaneous-cafe.vercel.app/contact/)
    fix: Add `<option value="" disabled selected>Choose one</option>` as the first option. The JS prefill (site.js `sel.value = svc`) still overrides it when ?service= matches, and `required` now actually blocks an unchosen submit. Optionally reorder options so Private chef (the home hero's default) is first.
- [major] No phone number above the fold on the mobile contact page
    where: src/pages/contact.html:16-77 with src/assets/css/site.css:118 (.split stacks to 1 column under 900px)
    fix: Either move `.contact-aside` before the form in the source (or add `@media (max-width:900px){ .contact-aside { order:-1 } }` on the split), or add one line under the lede in the hero (contact.html:9): `<p class="hero__contact">Call or text <a href="tel:+17079726647">(707) 972-6647</a></p>`. Desktop is fine (phone at y=733 of 900).
- [major] New /api/notify endpoint is unauthenticated and unthrottled and can send SMS to arbitrary numbers
    where: api/notify.js:32-46 and src/assets/js/site.js:78-81 (not yet live: GET https://spontaneous-cafe.vercel.app/api/notify returns 308 to /api/notify/ then
    fix: Do not trigger the SMS from the browser. Use Formspree's webhook (signed, fires only on a real submission) or a Formspree/Zapier integration to call Twilio/Telegram server-side, or at minimum: drop the inquirer SMS to arbitrary numbers, add a per-IP rate limit (Vercel KV/Upstash, e.g. 3 per hour), check `req.headers.origin` against the site, and cap daily sends. Add the new cha
- [minor] Error state is rendered in success green with only a polite live region
    where: src/assets/css/site.css:338 and src/assets/js/site.js:81-84, src/pages/contact.html:59
    fix: Toggle `is-error` on `.form__status` in the catch branch and add `.form__status.is-error { color: var(--red) }`; set `role="alert"` (or aria-live="assertive") when writing an error; on success call `status.focus()` (add tabindex="-1") or scroll it into view, and re-apply the prefill after reset.
- [minor] No-JS fallback lands on Formspree's generic thank-you page and loses the service prefill
    where: src/pages/contact.html:16-17 and src/assets/js/site.js:66-69
    fix: Add `<input type="hidden" name="_next" value="https://spontaneouscafe.com/contact/?sent=1">` and show a "Sent" message when `?sent=1` is present (server-rendered text is fine; it can be a hidden block toggled by CSS `:target` or by JS). Prefill fix comes with the placeholder option in finding 1.
- [minor] tel: and mailto: links in CTA bands and footer are 21px-tall inline targets
    where: src/assets/css/site.css:323-324 (.cta__contact) and :350-351 (.site-footer ul/a); markup in src/pages/*.html closing `<p class="cta__contact">` and sr
    fix: `.cta__contact a, .site-footer li a { display:inline-block; padding-block:.55rem; min-height:44px; }` and give `.contact-aside .big a` `display:inline-block; padding-block:.35rem`. On mobile stack the two CTA-band links on separate lines instead of the middot separator.
- [minor] Help text is not associated with its field
    where: src/pages/contact.html:46 and :55
    fix: Give each help span an id (`date-help`, `message-help`) and add `aria-describedby="date-help"` / `aria-describedby="message-help"` to the matching input and textarea.
- [minor] type="date" demands an exact day while the field is meant to accept a rough date
    where: src/pages/contact.html:45-46
    fix: Use `type="text" inputmode="text" autocomplete="off" placeholder="e.g. mid October, or a weekend in May"`, or keep the date input and add a `type="month"` alternative. api/notify.js:38 already treats it as a 20-char string, so nothing downstream depends on ISO format.
- [minor] About page has no CTA until the last screen
    where: src/pages/about.html:4-9 (hero--plain with no hero__actions)
    fix: Add `<div class="hero__actions"><a class="btn" href="/contact/">Send an inquiry</a></div>` under the lede in the about hero, matching the service pages.
- [minor] Every inquiry email has the same subject line
    where: src/pages/contact.html:17 and src/assets/js/site.js:70-75
    fix: In site.js, before building FormData set `form.querySelector('[name=_subject]').value = 'Inquiry: ' + sel.value + ' from ' + form.name.value` (Formspree honours `_subject` from the posted data), and keep the static value as the no-JS fallback.

## CODE  confirmed 11
- [major] All four season tab panels ship with `hidden` in the HTML, so the seasonal menus are empty without JavaScript on every service page
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/foraging.html lines 76, 95, 114, 133; private-chef.html lines 102, 121, 140, 159; catering.html lines 97, 
    fix: Remove `hidden` from the panels in the source and let site.js apply it: in the `[data-tabs]` loop, after collecting `panels`, call `select(initial)` which already sets `p.hidden = i !== j`. Optionally add `html:not(.js) .tabs { display: none }` so the non-functional buttons are hidden when scripts never run.
- [major] /assets/ is served with `immutable, max-age=31536000` but site.css and site.js have no cache-busting, so shipped CSS/JS changes will not reach returning visitors for up to a year
    where: /Users/main/MOSI/Spontaneous Cafe/vercel.json line 7; src/layout.html lines 20 and 81; build.py line 75
    fix: In build.py, compute a content hash for site.css and site.js (hashlib.md5 of the bytes, first 8 chars), write them to dist as `site.<hash>.css` / `site.<hash>.js` (or append `?v=<hash>` to the href/src), and replace the two references in the layout during the build. Keep the immutable header for hashed files only, or narrow the header source to `/assets/(img|video|logo)/(.*)` a
- [minor] Unguarded IntersectionObserver in hero-video block throws before the reveal fallback runs, leaving every page blank below the hero
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/js/site.js line 23 (and line 3, line 30)
    fix: Move the hero-video block inside `if ('IntersectionObserver' in window)`, or wrap it in try/catch. Better still, add the `js` class only after the observer is successfully created (`document.documentElement.classList.add('js')` immediately before `ro.observe`), so a thrown error anywhere else in the file leaves `.reveal` content visible. Also guard line 74 (`if (button) button.
- [minor] A 20 KB wordmark SVG is inlined twice into every page, making the logo about 73 percent of each HTML document
    where: /Users/main/MOSI/Spontaneous Cafe/build.py lines 77-78, 96-97; src/layout.html lines 27 and 50; src/assets/logo/wordmark.svg and wordmark-light.svg (2
    fix: Reference the logo once as a cached asset: `<img src="/assets/logo/wordmark.svg" width="2050" height="736" alt="">` (styled via `.brand img { height: 46px }`, already in site.css line 155), with `currentColor` or a CSS `filter` for the footer variant, or a single inline `<svg><symbol>` sprite plus `<use>`. If inlining must stay, delete wordmark-light.svg and derive it with `svg
- [minor] build.py injects title and description into HTML attributes and <title> without escaping
    where: /Users/main/MOSI/Spontaneous Cafe/build.py lines 91-92; src/layout.html lines 6-7, 10-11
    fix: Escape once at substitution: `from html import escape` and use `escape(meta['title'], quote=True)` for the title/description/og replacements. For the JSON-LD, post-process the dumped string with `.replace('</', '<\\/')` before inserting it into the <script> block.
- [minor] Internal `<!-- CONFIRM ... -->` review notes are shipped to production HTML
    where: /Users/main/MOSI/Spontaneous Cafe/build.py line 99; e.g. src/pages/foraging.html lines 32, 166-172, 245, 257; contact.html line 98
    fix: Strip them at build time: `body = re.sub(r'<!--\s*CONFIRM.*?-->', '', body, flags=re.S)` after reading the page (line 88), and keep the questionnaire in docs/ as the source of truth for open items.
- [minor] Inline styles repeated across pages and in the layout instead of one CSS rule
    where: /Users/main/MOSI/Spontaneous Cafe/src/pages/foraging.html lines 48 and 54; private-chef.html line 32; catering.html line 49; index.html line 76; src/l
    fix: Add `list-style: none; padding: 0;` to `.day` in site.css line 232 and delete the four inline attributes. Give the footer paragraph a class (e.g. `.site-footer .blurb { color: inherit; margin-top: var(--space-4); max-width: 36ch }`) and the foraging half-day block a utility such as `.mt-6 { margin-top: var(--space-6) }`.
- [minor] Nine CSS classes are defined but no page uses them
    where: /Users/main/MOSI/Spontaneous Cafe/src/assets/css/site.css lines 94 (.tabular), 99 (.section--tight), 107 (.rule), 110 (.grid-4, plus 117 and 122), 114
    fix: Delete the nine rules, or keep the small utilities (.rule, .cluster, .grid-4) and delete .sources/.source, .btn--ghost, .section--tight, .stack-lg, .tabular. Add a one-line check to build.py that warns when a defined class is unused, since the dead-CSS list will grow as sections are cut.
- [minor] Internal asset manifests are copied into dist and served publicly with a one-year immutable cache
    where: /Users/main/MOSI/Spontaneous Cafe/build.py line 75; src/assets/MANIFEST.md and src/assets/MANIFEST-photos.md
    fix: Pass `ignore=shutil.ignore_patterns('*.md', '.DS_Store')` to copytree on line 75, or move the manifests to docs/.
- [minor] No custom 404 page; unknown paths take a 308 hop and then land on Vercel's plain-text error
    where: /Users/main/MOSI/Spontaneous Cafe/vercel.json lines 4-5; dist/ (no 404.html)
    fix: Add src/pages/404.html with the normal meta block and have build.py write it to dist/404.html (not dist/404/index.html); Vercel serves a root 404.html automatically for not-found routes. Exclude it from sitemap.xml.
- [minor] sitemap.xml stamps every URL with the build date, so lastmod carries no information
    where: /Users/main/MOSI/Spontaneous Cafe/build.py lines 106-109
    fix: Use each page file's mtime (`datetime.date.fromtimestamp(os.path.getmtime(path))`) or the last git commit date for the file (`git log -1 --format=%cs -- src/pages/<fn>`), or drop the element entirely.