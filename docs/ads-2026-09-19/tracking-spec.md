# Measurement implementation

Exact diffs. Not applied to the working tree, because the GTM container ID and the Ads
conversion ID do not exist yet and a placeholder container would ship on the next deploy.
Each step is a one-line ID swap once those exist.

Verified against the repo on 2026-09-19: `src/layout.html` is the single template
`build.py` wraps all eight pages in, `<head>` opens on line 3 and closes on line 23,
`<body>` opens on line 24. The form handler lives at `src/assets/js/site.js:399-425`.

---

## Step 1. GTM container, `src/layout.html`

Insert directly after line 3, `<head>`:

```html
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-REPLACE');</script>
```

Insert directly after line 24, `<body>`:

```html
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-REPLACE"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

The existing CSP in `vercel.json` will block this. Add `https://www.googletagmanager.com`
to `script-src`, and `https://www.google-analytics.com` plus
`https://www.googletagmanager.com` to `connect-src`. Check the browser console for CSP
violations after the first deploy, because a silently blocked tag looks exactly like a tag
that is working.

---

## Step 2. The lead event, `src/assets/js/site.js`

The form posts by AJAX and never navigates, so there is no thank-you URL and the
conversion has to be event-based. Insert in the success branch at line 415, immediately
before `form.reset();`:

```js
// Enhanced conversions: hash happens client-side inside Google's tag.
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'generate_lead',
  lead_service: (form.service && form.service.value) || '',
  lead_tier: (form.tier && form.tier.value) || '',
  user_data: {
    email: (form.email && form.email.value) || '',
    phone_number: (form.phone && form.phone.value) || ''
  }
});
```

`lead_service` and `lead_tier` ride along so the Ads reports can show which service and
which price tier the paid clicks actually asked for. That is the single most useful thing
this campaign can learn.

---

## Step 3. Observation-only signals, `src/assets/js/site.js`

Add one delegated listener near the same block:

```js
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!a) return;
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: a.href.indexOf('tel:') === 0 ? 'phone_click' : 'email_click'
  });
});
```

---

## Step 4. Conversion actions in Google Ads

| Action | Source | Tier | Count |
|---|---|---|---|
| Lead form | GTM `generate_lead` | **Primary** | One |
| Calls from ads, 60s+ | Google forwarding number | **Primary** | One |
| Phone click | GTM `phone_click` | Secondary, observation | One |
| Email click | GTM `email_click` | Secondary, observation | One |

The tier split is the part that matters. Smart bidding spends the whole budget chasing
whatever is marked primary, and a `tel:` tap is not a booking. Some are people saving the
number, some are stray thumbs. Marking it primary teaches Google to buy taps.

Turn Enhanced Conversions for leads on at Goals, Conversions, Settings. The `user_data`
object in step 2 is the entire requirement.

Do not also import the same event from GA4. Feeding Ads natively and through a GA4 import
double-counts it. GA4 stays for reporting.

---

## Step 5. Verification before the first dollar

1. GTM Preview mode, submit the form, confirm `generate_lead` fires once and carries
   `user_data`.
2. Google Ads, Goals, Conversions. Status must read "Recording conversions", not
   "Unverified".
3. Submit a live test through the real form. Confirm Formspree received it, `/api/notify/`
   fired, and the conversion landed in Ads within three hours.
4. Confirm no CSP violation in the console on all eight pages.

A campaign launched against an unverified conversion action spends the budget and learns
nothing. This step is not optional.
