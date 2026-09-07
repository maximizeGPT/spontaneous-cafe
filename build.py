#!/usr/bin/env python3
"""Assemble the static site from src/ into dist/. Standard library only.

Page files live in src/pages/<slug>.html. Each starts with a JSON block inside an
HTML comment, then the page body:

    <!--meta
    {"title": "...", "description": "...", "og_image": "home-poster.jpg"}
    -->
    <section>...</section>

index.html builds to dist/index.html; every other slug builds to dist/<slug>/index.html.
"""
import json, os, re, shutil, sys, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
DIST = os.path.join(ROOT, 'dist')
SITE = 'https://spontaneouscafe.com'

def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def svg_inline(path, fill_override=None, cls=None):
    s = read(path)
    s = re.sub(r'\s(width|height)="[^"]+"', '', s, count=2)
    if fill_override:
        s = re.sub(r'fill="#[0-9A-Fa-f]{6}"', f'fill="{fill_override}"', s)
    if cls:
        s = s.replace('<svg ', f'<svg class="{cls}" ', 1)
    return s

def jsonld(meta, slug):
    base = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "The Spontaneous Cafe",
        "alternateName": "Chef Matt Samuelson",
        "url": SITE + "/",
        "telephone": "+1-707-972-6647",
        "email": "chefmattsamuelson@gmail.com",
        "founder": {"@type": "Person", "name": "Matthew Samuelson"},
        "foundingDate": "2009",
        "areaServed": {"@type": "Place", "name": "Mendocino County, California"},
        "address": {"@type": "PostalAddress", "addressLocality": "Mendocino", "addressRegion": "CA", "addressCountry": "US"},
        "priceRange": "$$$",
    }
    if meta.get('service'):
        base = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": meta['service'],
            "provider": {"@type": "LocalBusiness", "name": "The Spontaneous Cafe", "url": SITE + "/"},
            "areaServed": "Mendocino County, California",
            "url": f"{SITE}/{slug}/",
            "description": meta['description'],
        }
    return json.dumps(base, indent=0)

def build():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(DIST, 'assets'))
    layout = read(os.path.join(SRC, 'layout.html'))
    wordmark = svg_inline(os.path.join(SRC, 'assets/logo/wordmark.svg'))
    wordmark_light = svg_inline(os.path.join(SRC, 'assets/logo/wordmark-light.svg'))
    pages = sorted(f for f in os.listdir(os.path.join(SRC, 'pages')) if f.endswith('.html'))
    urls = []
    for fn in pages:
        slug = fn[:-5]
        raw = read(os.path.join(SRC, 'pages', fn))
        m = re.match(r'\s*<!--meta\s*(\{.*?\})\s*-->\s*', raw, re.S)
        if not m:
            sys.exit(f'{fn}: missing meta block')
        meta = json.loads(m.group(1))
        body = raw[m.end():]
        canonical = '' if slug == 'index' else slug + '/'
        html = layout
        html = html.replace('{{title}}', meta['title'])
        html = html.replace('{{description}}', meta['description'])
        html = html.replace('{{canonical}}', canonical)
        html = html.replace('{{og_image}}', meta.get('og_image', 'home-poster.jpg'))
        html = html.replace('{{jsonld}}', jsonld(meta, slug))
        html = html.replace('{{wordmark}}', wordmark)
        html = html.replace('{{wordmark_light}}', wordmark_light)
        html = re.sub(r'\{\{active:([a-z-]+)\}\}', lambda mm: 'aria-current="page"' if mm.group(1) == slug else '', html)
        html = html.replace('{{content}}', body)
        out_dir = DIST if slug == 'index' else os.path.join(DIST, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        urls.append(f'{SITE}/{canonical}')
        print(f'  {slug:20s} -> {os.path.relpath(os.path.join(out_dir, "index.html"), ROOT)}')
    today = datetime.date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>')
    sm.append('</urlset>')
    with open(os.path.join(DIST, 'sitemap.xml'), 'w') as f:
        f.write('\n'.join(sm))
    with open(os.path.join(DIST, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print(f'built {len(pages)} pages')

if __name__ == '__main__':
    build()
