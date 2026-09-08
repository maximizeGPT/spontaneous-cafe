// Vercel serverless function: text Matt (and optionally the inquirer) when the contact form is submitted.
// Channels are chosen by environment variables set in Vercel > Project > Settings > Environment Variables:
//   TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM (E.164, e.g. +17075550100), OWNER_PHONE (E.164)   -> SMS via Twilio
//   TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID                                                   -> Telegram push (free)
//   CONFIRM_INQUIRER=1                                                                     -> also text the inquirer if they left a phone
// The form still posts to Formspree for email and storage. This is the instant channel on top.
//
// Hardening: POST with a JSON body only, same-site Origin or Referer only, five
// requests per IP per ten minutes. The only number this function will ever text
// besides OWNER_PHONE is the one in the request body, and only with CONFIRM_INQUIRER=1.

const ALLOWED_HOSTS = new Set(['spontaneouscafe.com', 'www.spontaneouscafe.com', 'spontaneous-cafe.vercel.app']);
const WINDOW_MS = 10 * 60 * 1000;
const MAX_PER_WINDOW = 5;
const hits = new Map(); // ip -> [timestamps]. Per warm instance; a coarse brake, not a guarantee.

const clean = (v, n = 300) => String(v || '').replace(/\s+/g, ' ').trim().slice(0, n);
const e164 = (v) => { const d = String(v || '').replace(/[^\d+]/g, ''); if (!d) return ''; if (d.startsWith('+')) return d; return d.length === 10 ? '+1' + d : d.length === 11 && d.startsWith('1') ? '+' + d : ''; };

function allowedOrigin(req) {
  const raw = req.headers.origin || req.headers.referer || '';
  if (!raw) return false;
  let host;
  try { host = new URL(raw).hostname.toLowerCase(); } catch { return false; }
  return ALLOWED_HOSTS.has(host) || /^[a-z0-9-]+(\.[a-z0-9-]+)*\.vercel\.app$/.test(host);
}

function throttled(req) {
  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  const now = Date.now();
  if (hits.size > 5000) hits.clear();
  const recent = (hits.get(ip) || []).filter((t) => now - t < WINDOW_MS);
  recent.push(now);
  hits.set(ip, recent);
  return recent.length > MAX_PER_WINDOW;
}

async function twilio(to, body) {
  const { TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM } = process.env;
  if (!TWILIO_SID || !TWILIO_TOKEN || !TWILIO_FROM || !to) return 'skipped';
  const r = await fetch(`https://api.twilio.com/2010-04-01/Accounts/${TWILIO_SID}/Messages.json`, {
    method: 'POST',
    headers: { Authorization: 'Basic ' + Buffer.from(`${TWILIO_SID}:${TWILIO_TOKEN}`).toString('base64'), 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ To: to, From: TWILIO_FROM, Body: body }),
  });
  return r.ok ? 'sent' : `twilio ${r.status}`;
}

async function telegram(body) {
  const { TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID } = process.env;
  if (!TELEGRAM_BOT_TOKEN || !TELEGRAM_CHAT_ID) return 'skipped';
  const r = await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: body }),
  });
  return r.ok ? 'sent' : `telegram ${r.status}`;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!/^application\/json\b/i.test(req.headers['content-type'] || '')) return res.status(415).json({ ok: false });
  if (!allowedOrigin(req)) return res.status(403).json({ ok: false });

  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch { return res.status(400).json({ ok: false }); } }
  if (!b || typeof b !== 'object' || Array.isArray(b)) return res.status(400).json({ ok: false });
  if (b._gotcha) return res.status(200).json({ ok: true }); // honeypot: pretend success

  const name = clean(b.name, 80), email = clean(b.email, 120), phone = clean(b.phone, 40), service = clean(b.service, 60);
  const date = clean(b.date, 20), guests = clean(b.guests, 6), message = clean(b.message, 400);
  if (!name || !email || !service) return res.status(400).json({ ok: false, error: 'name, email and service are required' });

  // Over the limit: look identical to success so a bot learns nothing, and send nothing.
  if (throttled(req)) return res.status(200).json({ ok: true });

  const owner = [`New inquiry: ${service}`, `${name} · ${email}${phone ? ' · ' + phone : ''}`, date ? `Date: ${date}` : '', guests ? `Guests: ${guests}` : '', message].filter(Boolean).join('\n');
  const results = { owner_sms: await twilio(e164(process.env.OWNER_PHONE), owner), telegram: await telegram(owner) };
  if (process.env.CONFIRM_INQUIRER === '1' && e164(phone)) {
    results.inquirer_sms = await twilio(e164(phone), `Thanks ${name.split(' ')[0]}, got your ${service.toLowerCase()} inquiry. I will reply within a day or two. Matt, The Spontaneous Cafe (707) 972-6647`);
  }
  return res.status(200).json({ ok: true, results });
}
