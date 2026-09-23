# Launch checklist: spontaneouscafe.com to Vercel

Everything below is reversible until the DNS records change. The GoDaddy site keeps serving until then.

## Before the switch
1. Matt has answered the questionnaire; every `<!-- CONFIRM -->` in `src/pages` is resolved or accepted. `grep -rn CONFIRM src/pages` is the list.
2. Matt's photos are in place (`docs/SWAP-LIST.md`), `python3 tools/images.py` has been run, and `python3 build.py` shows "production".
3. Privacy effective date set in `src/pages/privacy.html`.
4. Notifications: `TWILIO_*` and `OWNER_PHONE`, or `TELEGRAM_*`, set in Vercel > spontaneous-cafe > Settings > Environment Variables (Production). Send one test inquiry from the live form and confirm the text arrives.
5. Vercel plan: the site is commercial, so the project should sit on Pro ($20/month) rather than Hobby before the domain goes on.
6. Lower the GoDaddy DNS TTL a week ahead of the switch, so the record change at cutover propagates fast (R4 section 5).
7. `vercel.json` is still in its pre-cutover state: a host-matched `X-Robots-Tag: noindex` header for `spontaneous-cafe.vercel.app`, and the staging pages self-canonicalising to the vercel.app host. Confirm with `curl -s https://spontaneous-cafe.vercel.app/ | grep -i canonical`; expect the canonical to read `spontaneous-cafe.vercel.app`, not `spontaneouscafe.com`.

## Add the domain in Vercel
1. Vercel > spontaneous-cafe > Settings > Domains > add `spontaneouscafe.com` and `www.spontaneouscafe.com`. Set the apex as primary; Vercel redirects www to apex.
2. Vercel shows the records it wants. As of 2026 the apex uses an A record to Vercel's IP (76.76.21.21) and www a CNAME to `cname.vercel-dns.com`. Use the values Vercel displays, not this file.
3. Redeploy once the domain is added. The build reads `VERCEL_PROJECT_PRODUCTION_URL`, and every canonical, `og:url`, `og:image`, sitemap and robots line switches to `spontaneouscafe.com` on its own. Nothing to set by hand; `SITE_URL` is only a manual override if that automatic value is ever wrong. Verify with curl (below the DNS step), not by reading the dashboard.

## In GoDaddy DNS (Matt's account, DNS stays at GoDaddy)
1. My Products > Domains > spontaneouscafe.com > DNS.
2. Note the current A record(s) for `@` and the CNAME for `www` (screenshot them; that is the rollback).
3. Change `@` A record to Vercel's IP. Change `www` CNAME to `cname.vercel-dns.com`. Leave MX and TXT records alone.
4. Propagation is usually minutes at GoDaddy's default TTL. Vercel issues the certificate automatically once it sees the records.

## Swap vercel.json
Remove the host-matched `X-Robots-Tag` block for `spontaneous-cafe.vercel.app`, and add a host-matched redirect from that host to `https://spontaneouscafe.com/:path*` instead. Exact JSON, from R1's "After DNS cutover" section:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "buildCommand": "python3 build.py",
  "outputDirectory": "dist",
  "cleanUrls": true,
  "trailingSlash": true,
  "redirects": [
    {
      "source": "/:path*",
      "has": [{ "type": "host", "value": { "eq": "spontaneous-cafe.vercel.app" } }],
      "destination": "https://spontaneouscafe.com/:path*",
      "permanent": true
    },
    { "source": "/privacy-policy", "destination": "/privacy/", "permanent": true },
    { "source": "/privacy-policy/", "destination": "/privacy/", "permanent": true }
  ],
  "headers": [
    {
      "source": "/assets/(css|js|fonts)/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/assets/(img|video)/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Vary", "value": "Accept-Encoding" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; img-src 'self' data:; media-src 'self'; font-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self' https://formspree.io; form-action 'self' https://formspree.io; frame-ancestors 'none'; base-uri 'self'" }
      ]
    }
  ]
}
```

Redeploy after saving.

## Verify
```bash
dig +short spontaneouscafe.com A
dig +short www.spontaneouscafe.com CNAME
curl -sI https://spontaneouscafe.com/ | head -5
curl -sI https://www.spontaneouscafe.com/ | grep -i location
curl -sI https://spontaneouscafe.com/privacy-policy | grep -i location
curl -sI https://spontaneouscafe.com/privacy-policy/ | grep -i location
curl -sI https://spontaneouscafe.com/foraging/ | head -5
curl -sI https://spontaneous-cafe.vercel.app/about/ | grep -i location
```
Expect: Vercel's IP, the vercel-dns CNAME, a 200 with the security headers, a redirect from www to the apex, a 308 from both privacy-policy forms to /privacy/, a 200 on /foraging/ (the one old URL that also exists on the new site), and a 308 from the vercel.app alias to the matching page on the apex.

## After
1. Google Search Console: add the property for `spontaneouscafe.com` (domain property, verified by a DNS TXT record at GoDaddy), submit `https://spontaneouscafe.com/sitemap.xml`. Do not file a Change of Address; this is the same domain, not a move between domains.
2. URL Inspection: use Request indexing once each for the eight live URLs. It is a quota-limited nudge, not a lever to lean on twice.
3. Watch the Search Console Pages report for `/privacy-policy` showing up as a 404 with a referring sitemap. That is the sign the old GoDaddy sitemap is still being crawled and the redirect did not ship.
4. Bing Webmaster Tools: add the site and choose "Import from Search Console" rather than verifying from scratch.
5. Two weeks after cutover, check Search Console Performance for the brand query "spontaneous cafe" and confirm the new title is what renders.
6. Google Business Profile: set the website field to `https://spontaneouscafe.com/`, and take the review link from the dashboard ("Ask for reviews") for the QR code. Update Alignable and any other listing that still carries the old bare "Spontaneous Cafe" name.
7. GoDaddy Website Builder subscription can be cancelled once the domain has served from Vercel for a week. Keep the domain registration.
8. Rotate the Vercel token and the fal.ai and Minimax keys that were pasted in chat; they live only in the gitignored `.env`.

## Rollback
Put the GoDaddy A and CNAME values back. The old site returns within minutes.
