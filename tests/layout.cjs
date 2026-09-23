// Isolated browser QA with test-only IDs and mocked Google. Nothing reaches Google.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const config = require('../vercel.json');
const csp = config.headers.flatMap(rule => rule.headers).find(h => h.key === 'Content-Security-Policy').value;
(async () => {
  const browser = await chromium.launch({ headless: true, channel: process.env.BROWSER_CHANNEL || 'chrome' });
  try {
    for (const width of [390, 1440]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
      const page = await context.newPage();
      const errors = [];
      let googleRequests = 0;
      page.on('pageerror', error => errors.push(error.message));
      await context.route('**/*', async route => {
        const url = new URL(route.request().url());
        if (url.hostname === 'www.googletagmanager.com') {
          googleRequests++;
          return route.fulfill({ contentType: 'application/javascript', body: 'window.__ga4Loaded = true;' });
        }
        if (url.hostname !== 'spontaneouscafe.com') return route.abort();
        const file = path.join(root, 'dist', url.pathname.endsWith('/') ? url.pathname + 'index.html' : url.pathname);
        if (!fs.existsSync(file)) return route.fulfill({ status: 404, body: '' });
        if (file.endsWith('.html')) {
          const html = fs.readFileSync(file, 'utf8').replace(/data-ga4-id="[^"]*"/, 'data-ga4-id="G-ABC1234567"');
          return route.fulfill({ contentType: 'text/html', body: html, headers: { 'Content-Security-Policy': csp } });
        }
        return route.fulfill({ path: file });
      });
      await page.goto('https://spontaneouscafe.com/');
      assert.equal(await page.locator('[data-cookie-notice]').isVisible(), true);
      assert.equal(googleRequests, 0);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      await page.screenshot({ path: '/tmp/cafe-consent-' + width + '.png' });
      await page.locator('[data-consent="denied"]').click();
      await page.goto('https://spontaneouscafe.com/contact/');
      assert.equal(googleRequests, 0);
      assert.equal(await page.locator('[data-cookie-notice]').isVisible(), false);
      await page.locator('[data-privacy-settings]').click();
      await page.locator('[data-consent="granted"]').click();
      await page.waitForFunction(() => window.__ga4Loaded);
      assert.equal(googleRequests, 1);
      await page.locator('[data-privacy-settings]').click();
      await page.locator('[data-consent="denied"]').click();
      await page.waitForLoadState();
      for (const slug of ['about', 'foraging', 'private-chef', 'catering', 'cooking-classes', 'privacy']) {
        await page.goto('https://spontaneouscafe.com/' + slug + '/');
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, slug + ' overflows');
        assert.equal(await page.locator('h1').count(), 1, slug + ' main heading');
      }
      assert.equal(googleRequests, 1, 'no more Google requests after withdrawal');
      assert.deepEqual(errors, []);
      console.log('PASS layout, consent and CSP:', width);
      await context.close();
    }
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exit(1); });
