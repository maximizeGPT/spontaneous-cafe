import importlib.util
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class BuildTests(unittest.TestCase):
    def render(self, **env):
        spec = importlib.util.spec_from_file_location('site_build', ROOT / 'build.py')
        module = importlib.util.module_from_spec(spec)
        with patch.dict(os.environ, env, clear=True):
            spec.loader.exec_module(module)
            with tempfile.TemporaryDirectory() as folder:
                module.DIST = folder + '/dist'
                module.build()
                return {str(p.relative_to(module.DIST)): p.read_text()
                        for p in Path(module.DIST).rglob('*')
                        if p.is_file() and p.suffix in ('.html', '.xml', '.txt')}

    def test_production_has_one_origin_and_no_retired_faq_schema(self):
        pages = self.render(SITE_URL='https://example.com', VERCEL_ENV='production')
        home = pages['index.html']
        self.assertIn('href="https://example.com/"', home)
        self.assertNotIn('https://spontaneouscafe.com', home)
        self.assertIn('<picture>', home)
        self.assertNotIn('FAQPage', pages['foraging/index.html'])
        self.assertIn('https://example.com/foraging/', pages['sitemap.xml'])
        self.assertIn('noindex', pages['404.html'])

    def test_preview_is_noindex_and_cannot_enable_tracking(self):
        pages = self.render(VERCEL_ENV='preview', GA4_ID='G-ABC1234567')
        self.assertIn('noindex', pages['index.html'])
        self.assertNotIn('data-ga4-id="G-', pages['index.html'])
        self.assertNotIn('<loc>', pages['sitemap.xml'])

    def test_tracking_requires_valid_configuration(self):
        with self.assertRaisesRegex(ValueError, 'GA4_ID'):
            self.render(GA4_ID='bad-id')

    def test_valid_tracking_config_is_escaped_and_hashed(self):
        home = self.render(VERCEL_ENV='production', GA4_ID='G-ABC1234567')['index.html']
        self.assertIn('data-ga4-id="G-ABC1234567"', home)
        self.assertRegex(home, r'/assets/js/analytics\.[a-f0-9]{8}\.js')
        self.assertNotIn('googletagmanager.com/gtm.js', home)

    def test_business_has_stable_identity_without_unverified_coordinates(self):
        pages = self.render()
        data = json.loads(re.search(r'application/ld\+json">(.*?)</script>', pages['index.html'], re.S)[1])
        self.assertIn('@id', data)
        self.assertNotIn('geo', data)


if __name__ == '__main__':
    unittest.main()
