const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');

function setup({ host = 'spontaneouscafe.com', id = 'G-ABC1234567', saved, storageThrows = false } = {}) {
  const listeners = {}, controls = {}, scripts = [], values = {};
  function element(key) {
    return controls[key] ||= { hidden: true, focus() {}, addEventListener(e, fn) { this[e] = fn; },
      getAttribute(name) { return name === 'data-consent' ? key : null; } };
  }
  if (saved) values['cafe-analytics-consent-v1'] = JSON.stringify({ choice: saved, at: Date.now() });
  const document = {
    currentScript: { dataset: { analyticsHost: 'spontaneouscafe.com', ga4Id: id } },
    cookie: '', title: 'Contact Matt', referrer: 'https://example.org/?email=secret@example.org',
    querySelector: element,
    querySelectorAll: () => [element('granted'), element('denied')],
    createElement: () => ({}), head: { appendChild: e => scripts.push(e) },
    addEventListener: (e, fn) => listeners[e] = fn,
  };
  let reloads = 0;
  const window = { document, location: { hostname: host, protocol: 'https:', origin: 'https://' + host,
    pathname: '/contact/', search: '?email=secret@example.org', reload() { reloads++; } },
    localStorage: { getItem(k) { if (storageThrows) throw Error(); return values[k] || null; },
      setItem(k, v) { if (storageThrows) throw Error(); values[k] = v; } },
    addEventListener: (e, fn) => listeners['window:' + e] = fn,
  };
  const filename = path.join(__dirname, '../src/assets/js/analytics.js');
  if (fs.existsSync(filename)) vm.runInNewContext(fs.readFileSync(filename, 'utf8'), { window, document, URL, Date });
  return { window, scripts, controls, listeners, values, get reloads() { return reloads; } };
}

test('first visit offers a choice but sends no events or Google requests', () => {
  const x = setup();
  assert.equal(x.controls['[data-cookie-notice]']?.hidden, false);
  assert.equal(x.scripts.length, 0);
  x.window.cafeAnalytics.track('generate_lead', { service: 'Private chef' });
  assert.equal(x.window.dataLayer, undefined);
});
test('accept loads once, keeps ads denied, and exposes no URL query or contact data', () => {
  const x = setup();
  assert.equal(typeof x.controls.granted?.click, 'function');
  x.controls.granted.click(); x.controls.granted.click();
  assert.equal(x.scripts.length, 1);
  assert.equal(x.scripts[0].src, 'https://www.googletagmanager.com/gtag/js?id=G-ABC1234567');
  const configs = x.window.dataLayer.filter(e => e[0] === 'config');
  assert.equal(configs.length, 1);
  assert.equal(configs[0][2].page_location, 'https://spontaneouscafe.com/contact/');
  assert.equal(configs[0][2].allow_google_signals, false);
  assert.equal(configs[0][2].send_page_view, true);
  x.window.cafeAnalytics.track('generate_lead', { service: 'Private chef', tier: '3 hours', email: 'secret@example.org' });
  const wire = JSON.stringify(x.window.dataLayer);
  assert.equal(wire.includes('secret@'), false);
  assert.ok(wire.includes('generate_lead'));
  assert.ok(wire.includes('private_chef'));
  assert.ok(wire.includes('ad_storage'));
  assert.equal(x.window.dataLayer.find(e => e[0] === 'event' && e[1] === 'generate_lead')[2].lead_tier, '3_hours');
});
test('reject persists across navigation and does not load Google', () => {
  const x = setup({ saved: 'denied' });
  assert.equal(x.controls['[data-cookie-notice]']?.hidden, true);
  assert.equal(x.scripts.length, 0);
  assert.equal(x.controls['[data-privacy-settings]']?.hidden, false);
});
test('local or unconfigured builds never expose tracking controls', () => {
  for (const options of [{ host: 'localhost' }, { host: 'preview.vercel.app' }, { host: 'spontaneous-cafe.vercel.app' }, { id: '' }]) {
    const x = setup(options);
    assert.equal(x.scripts.length, 0);
    assert.notEqual(x.controls['[data-cookie-notice]']?.hidden, false);
  }
});
test('withdrawal disables GA and reloads without collecting future events', () => {
  const x = setup({ saved: 'granted' });
  assert.equal(x.scripts.length, 1);
  x.controls.denied.click();
  const count = x.window.dataLayer.length;
  x.window.cafeAnalytics.track('generate_lead', {});
  assert.equal(x.window.dataLayer.length, count);
  assert.equal(x.window['ga-disable-G-ABC1234567'], true);
  assert.equal(x.reloads, 1);
});
test('storage failure defaults to no measurement and controls still work', () => {
  const x = setup({ storageThrows: true });
  assert.equal(x.scripts.length, 0);
  assert.equal(typeof x.controls.granted?.click, 'function');
  assert.doesNotThrow(() => x.controls.granted.click());
});
