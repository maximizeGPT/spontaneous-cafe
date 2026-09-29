const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  try {
    for (const width of [390, 1440]) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      await page.route('**/*', route => {
        const url = new URL(route.request().url());
        if (url.hostname !== 'spontaneouscafe.com') return route.abort();
        const file = path.join(__dirname, '../dist', url.pathname.endsWith('/') ? url.pathname + 'index.html' : url.pathname);
        return fs.existsSync(file) ? route.fulfill({ path: file }) : route.fulfill({ status: 404, body: '' });
      });
      await page.goto('https://spontaneouscafe.com/');
      await page.locator('.gallery-preview').click();
      await page.waitForURL('**/gallery/');
      const photos = page.locator('[data-gallery-photo]');
      assert.equal(await photos.count(), 9);
      await photos.first().click();
      const viewer = page.getByRole('dialog');
      assert.equal(await viewer.isVisible(), true);
      const initial = await viewer.locator('img').getAttribute('src');
      await page.keyboard.press('ArrowRight');
      assert.notEqual(await viewer.locator('img').getAttribute('src'), initial);
      await page.keyboard.press('ArrowLeft');
      assert.equal(await viewer.locator('img').getAttribute('src'), initial);
      await page.keyboard.press('Escape');
      assert.equal(await viewer.isVisible(), false);
      assert.equal(await photos.first().evaluate(el => el === document.activeElement), true);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
      await page.locator('[data-consent="denied"]').click();
      for (const photo of await photos.all()) {
        await photo.scrollIntoViewIfNeeded();
        await photo.locator('img').evaluate(img => img.decode());
      }
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.screenshot({ path: '/tmp/cafe-gallery-' + width + '.png', fullPage: true });
      console.log('PASS gallery navigation, keyboard viewer, focus and layout:', width);
      await page.close();
    }
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exit(1); });
