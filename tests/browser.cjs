// Run after build.py. All network requests are intercepted; no inquiries leave this test.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({ headless: true, channel: process.env.BROWSER_CHANNEL || 'chrome' });
  try {
    for (const outcome of ['success', 'failure', 'blocked-analytics']) {
      const page = await browser.newPage();
      let submissions = 0;
      await page.route('**/*', async route => {
        const url = new URL(route.request().url());
        if (url.hostname === 'formspree.io') {
          submissions++;
          await new Promise(resolve => setTimeout(resolve, 100));
          return route.fulfill({ status: outcome === 'failure' ? 422 : 200,
            contentType: 'application/json', body: outcome === 'failure' ? '{"errors":[]}' : '{"ok":true}' });
        }
        if (url.pathname === '/api/notify/') return route.abort();
        if (url.hostname !== 'spontaneouscafe.com') return route.abort();
        const rel = url.pathname.endsWith('/') ? url.pathname + 'index.html' : url.pathname;
        const file = path.join(root, 'dist', rel);
        return fs.existsSync(file) ? route.fulfill({ path: file }) : route.fulfill({ status: 404, body: '' });
      });
      await page.goto('https://spontaneouscafe.com/contact/');
      await page.evaluate(blocked => {
        window.recorded = [];
        window.cafeAnalytics = { track: (...args) => {
          if (blocked) throw Error('analytics unavailable');
          window.recorded.push(args);
        } };
      }, outcome === 'blocked-analytics');
      await page.locator('[name="name"]').fill('Test Visitor');
      await page.locator('[name="email"]').fill('test@example.org');
      await page.locator('[name="date"]').fill('October');
      await page.locator('[name="service"]').selectOption('Private chef');
      await page.locator('[name="tier"]').selectOption('3 hours');
      await page.locator('[name="message"]').fill('Mocked request; never transmitted.');
      await page.evaluate(() => {
        const form = document.querySelector('[data-contact]');
        form.requestSubmit(); form.requestSubmit();
      });
      await page.waitForFunction(() => !document.querySelector('button[type="submit"]').disabled);
      const status = await page.locator('.form__status').textContent();
      const events = await page.evaluate(() => window.recorded);
      assert.equal(submissions, 1, 'duplicate submits must be suppressed');
      if (outcome === 'failure') {
        assert.ok(status.includes('did not send'));
        assert.equal(events.filter(e => e[0] === 'generate_lead').length, 0);
        assert.equal(events.filter(e => e[0] === 'inquiry_error').length, 1);
      } else {
        assert.ok(status.includes('Thank you'), 'analytics/notification failure cannot change form success');
        if (outcome === 'success') assert.deepEqual(events, [['generate_lead', { service: 'Private chef', tier: '3 hours' }]]);
      }
      await page.close();
      console.log('PASS form:', outcome);
    }
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exit(1); });
