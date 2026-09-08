# Launch checklist: spontaneouscafe.com to Vercel

Everything below is reversible until the DNS records change. The GoDaddy site keeps serving until then.

## Before the switch
1. Matt has answered the questionnaire; every `<!-- CONFIRM -->` in `src/pages` is resolved or accepted. `grep -rn CONFIRM src/pages` is the list.
2. Matt's photos are in place (`docs/SWAP-LIST.md`), `python3 tools/images.py` has been run, and `python3 build.py` shows "production".
3. Privacy effective date set in `src/pages/privacy.html`.
4. Notifications: `TWILIO_*` and `OWNER_PHONE`, or `TELEGRAM_*`, set in Vercel > spontaneous-cafe > Settings > Environment Variables (Production). Send one test inquiry from the live form and confirm the text arrives.
5. Vercel plan: the site is commercial, so the project should sit on Pro ($20/month) rather than Hobby before the domain goes on.

## Add the domain in Vercel
1. Vercel > spontaneous-cafe > Settings > Domains > add `spontaneouscafe.com` and `www.spontaneouscafe.com`. Set the apex as primary; Vercel redirects www to apex.
2. Vercel shows the records it wants. As of 2026 the apex uses an A record to Vercel's IP (76.76.21.21) and www a CNAME to `cname.vercel-dns.com`. Use the values Vercel displays, not this file.

## In GoDaddy DNS (Matt's account, DNS stays at GoDaddy)
1. My Products > Domains > spontaneouscafe.com > DNS.
2. Note the current A record(s) for `@` and the CNAME for `www` (screenshot them; that is the rollback).
3. Change `@` A record to Vercel's IP. Change `www` CNAME to `cname.vercel-dns.com`. Leave MX and TXT records alone.
4. Propagation is usually minutes at GoDaddy's default TTL. Vercel issues the certificate automatically once it sees the records.

## Verify
```bash
dig +short spontaneouscafe.com A
dig +short www.spontaneouscafe.com CNAME
curl -sI https://spontaneouscafe.com/ | head -5
curl -sI https://www.spontaneouscafe.com/ | grep -i location
curl -sI https://spontaneouscafe.com/privacy-policy | grep -i location
```
Expect: Vercel's IP, the vercel-dns CNAME, a 200 with the security headers, a redirect from www to the apex, and a 308 from the old privacy URL to /privacy/.

## After
1. Google Search Console: add the property for `spontaneouscafe.com` (domain property, DNS TXT record in GoDaddy), submit `https://spontaneouscafe.com/sitemap.xml`.
2. Google Business Profile: set the website field to `https://spontaneouscafe.com/`, and take the review link from the dashboard ("Ask for reviews") for the QR code.
3. GoDaddy Website Builder subscription can be cancelled once the domain has served from Vercel for a week. Keep the domain registration.
4. Rotate the Vercel token and the fal.ai and Minimax keys that were pasted in chat; they live only in the gitignored `.env`.

## Rollback
Put the GoDaddy A and CNAME values back. The old site returns within minutes.
