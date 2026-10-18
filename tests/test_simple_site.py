from pathlib import Path
import re
import unittest
from html.parser import HTMLParser

class PhotoParser(HTMLParser):
 def __init__(self):
  super().__init__(); self.links=[]; self.photos=[]
 def handle_starttag(self, tag, attrs):
  attrs=dict(attrs)
  if tag=="a": self.links.append(attrs.get("href"))
  if tag=="img" and attrs.get("src"):
   self.photos.append((attrs["src"],self.links[-1] if self.links else None))
 def handle_endtag(self, tag):
  if tag=="a" and self.links: self.links.pop()

ROOT = Path(__file__).resolve().parents[1]
class SimpleSiteTests(unittest.TestCase):
 def test_pages_and_media(self):
  expected={'index','about','foraging','private-chef','catering','cooking-classes','gallery','contact','privacy','404'}
  self.assertEqual({p.stem for p in (ROOT/'src/pages').glob('*.html')},expected)
  for p in (ROOT/'dist').rglob('*.html'):
   html=p.read_text()
   with self.subTest(page=p.name):
    self.assertNotIn('<video',html)
    self.assertNotRegex(html,r'home-good-|home-poster|journey-')
    self.assertNotRegex(html,r'"(?:price|priceRange|offers|makesOffer)"\s*:')
    self.assertNotRegex(html,r'class="(?:prices|price|cta)"|id="prices"|\$\d')
 def test_photos_are_unique_within_each_page(self):
  for p in (ROOT/'src/pages').glob('*.html'):
   photos=re.findall(r'<img[^>]*src="([^"]+)"',p.read_text())
   self.assertEqual(len(photos),len(set(photos)),p.name+' repeats a photo')
 def test_photos_are_exclusive_except_linked_home_previews(self):
  owners={}
  for p in (ROOT/'src/pages').glob('*.html'):
   if p.stem=='index': continue
   parser=PhotoParser(); parser.feed(p.read_text())
   for photo,_ in parser.photos:
    self.assertNotIn(photo,owners,photo+' is repeated across pages')
    owners[photo]='/'+p.stem+'/'
  parser=PhotoParser(); parser.feed((ROOT/'src/pages/index.html').read_text())
  for photo,link in parser.photos:
   if photo in owners: self.assertEqual(link,owners[photo],photo+' needs a link to its dedicated page')
 def test_home_has_no_sample_menu_section(self):
  self.assertNotIn('Six courses, by season',(ROOT/'src/pages/index.html').read_text())
  self.assertIn('id="menus"',(ROOT/'src/pages/private-chef.html').read_text())
 def test_contact_has_no_booking_fields(self):
  html=(ROOT/'dist/contact/index.html').read_text()
  for field in ['tier','date','guests']:
   self.assertNotIn('name="'+field+'"',html)
if __name__=='__main__': unittest.main()
