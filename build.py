#!/usr/bin/env python3
"""Assemble the static site from src/ into dist/.
Pillow is required for responsive images and social image dimensions.

Page files live in src/pages/<slug>.html. Each starts with a JSON block inside an
HTML comment, then the page body:

    <!--meta
    {"title": "...", "description": "...", "og_image": "home-poster.jpg"}
    -->
    <section>...</section>

Recognised meta keys: title, description, og_image, og_alt, service, noindex.

index.html builds to dist/index.html; 404.html builds to dist/404.html (Vercel
serves it for unknown paths); every other slug builds to dist/<slug>/index.html.
"""
import json, os, re, shutil, sys, datetime, hashlib, html as _html, subprocess
from urllib.parse import urlsplit
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
DIST = os.path.join(ROOT, 'dist')
SITE = os.environ.get('SITE_URL', 'https://spontaneouscafe.com').rstrip('/')
_origin = urlsplit(SITE)
if (_origin.scheme != 'https' or not _origin.hostname or _origin.path or
        _origin.query or _origin.fragment or _origin.username or _origin.port):
    raise ValueError('SITE_URL must be an HTTPS origin without a path, port or credentials')
PREVIEW = os.environ.get('VERCEL_ENV', 'production') != 'production' or os.environ.get('REVIEW') == '1'
GTM_ID = os.environ.get('GTM_ID', '').strip()
if GTM_ID and not re.fullmatch(r'GTM-[A-Z0-9]{5,}', GTM_ID):
    raise ValueError('GTM_ID must be a real GTM container ID, or unset')
GA4_ID = os.environ.get('GA4_ID', '').strip()
if GA4_ID and not re.fullmatch(r'G-[A-Z0-9]+', GA4_ID):
    raise ValueError('GA4_ID must be a GA4 measurement ID, or unset')
PHONE = '+1-707-972-6647'
EMAIL = 'chefmattsamuelson@gmail.com'
DEFAULT_OG_ALT = 'The Spontaneous Cafe, Mendocino'

# The three hour tiers. Any service, any page. See CONTEXT.md.
TIERS = [
    ('Three hours', '300'),
    ('Six hours', '500'),
    ('Twelve hours', '1000'),
]

CONFIRM_RE = re.compile(r'<!--\s*CONFIRM\b.*?-->', re.S)
TAG_CONFIRM_RE = re.compile(r'<span class="tag-confirm">.*?</span>', re.S)
CLASS_ATTR_RE = re.compile(r'class="([^"]*)"')


def strip_review_markup(html_src):
    """Production builds (no REVIEW=1) never ship internal review markup:
    the "confirm with Matt" chips, and the "ph" class that marks placeholder
    images/photos so visitors never see either."""
    html_src = TAG_CONFIRM_RE.sub('', html_src)

    def strip_ph(m):
        classes = [c for c in m.group(1).split() if c != 'ph']
        return f'class="{" ".join(classes)}"' if classes else ''

    return CLASS_ATTR_RE.sub(strip_ph, html_src)


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def offers():
    return [{
        "@type": "Offer",
        "name": name,
        "price": price,
        "priceCurrency": "USD",
        "itemOffered": {"@type": "Service", "name": "Culinary experience with Chef Matt"},
    } for name, price in TIERS]


def jsonld(meta, slug):
    if meta.get('service'):
        base = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": meta['service'],
            "serviceType": meta['service'],
            "provider": {
                "@type": "LocalBusiness",
                "@id": SITE + '/#business',
                "name": "The Spontaneous Cafe",
                "url": SITE + "/",
                "telephone": PHONE,
                "email": EMAIL,
            },
            "areaServed": "Mendocino County, California",
            "url": f"{SITE}/{slug}/",
            "description": meta['description'],
            "offers": offers(),
        }
    else:
        base = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "@id": SITE + '/#business',
            "name": "The Spontaneous Cafe",
            "alternateName": "Chef Matt Samuelson",
            "url": SITE + "/",
            "image": SITE + "/assets/img/home-poster.jpg",
            "telephone": PHONE,
            "email": EMAIL,
            "founder": {"@type": "Person", "@id": SITE + '/about/#matt', "name": "Matthew Samuelson", "url": SITE + '/about/'},
            "foundingDate": "2009",
            "areaServed": {"@type": "Place", "name": "Mendocino County, California"},
            "address": {"@type": "PostalAddress", "addressLocality": "Mendocino", "addressRegion": "CA", "addressCountry": "US"},
            "priceRange": "$$$",
            "makesOffer": offers(),
            "sameAs": ["https://www.google.com/maps?cid=7343978535458024901"],
            "hasMap": "https://www.google.com/maps?cid=7343978535458024901",
        }
    return json.dumps(base, indent=0)



IMG_RE = re.compile(r'<img\b([^>]*?)\ssrc="/assets/img/([A-Za-z0-9_-]+)\.jpg"([^>]*)>')
DEFAULT_SIZES = '(max-width: 600px) 100vw, (max-width: 1000px) 50vw, 640px'
_WIDTH_CACHE = {}


def pixel_width(path):
    """Real pixel width of an image file, or None when it cannot be read.

    Every srcset descriptor comes from here. The source photos are not all the
    same size (828 px phone crops, 1000, 1280, 1448, 1600, 1800), so a fixed
    1600w descriptor lies to the browser and it picks the wrong candidate.
    """
    if path not in _WIDTH_CACHE:
        size = image_size(path)
        _WIDTH_CACHE[path] = size[0] if size else None
    return _WIDTH_CACHE[path]


def responsive_images(body):
    """Wrap <img src="/assets/img/x.jpg"> in <picture> with WebP and JPEG srcsets when tools/images.py variants exist.
    Optional data-sizes="..." on the img overrides the sizes attribute. Posters and og images are untouched (not <img>)."""
    img_dir = os.path.join(SRC, 'assets', 'img')
    def repl(m):
        before, name, after = m.group(1), m.group(2), m.group(3)
        full_w = pixel_width(os.path.join(img_dir, f'{name}.jpg'))
        if not full_w or not os.path.exists(os.path.join(img_dir, f'{name}.webp')):
            return m.group(0)
        # tools/images.py writes a variant only when it is smaller than the
        # source, so absence is normal. Each descriptor is the file's own width.
        variants = []
        for w in (480, 800, 1200):
            vw = pixel_width(os.path.join(img_dir, f'{name}-{w}.jpg'))
            if vw:
                variants.append((w, vw))
        if not variants:
            return m.group(0)
        attrs = before + after
        sm = re.search(r'\sdata-sizes="([^"]+)"', attrs)
        sizes = sm.group(1) if sm else DEFAULT_SIZES
        attrs = re.sub(r'\sdata-sizes="[^"]+"', '', attrs)
        # The img keeps its class; the wrapping <picture> gets the same class so
        # rules like .ph and .span-2 still target it (picture is display:contents
        # by default, so it otherwise takes no part in layout).
        cm = re.search(r'\sclass="([^"]*)"', attrs)
        picture_class = f' class="{cm.group(1)}"' if cm else ''
        jpg = ', '.join([f'/assets/img/{name}-{w}.jpg {vw}w' for w, vw in variants]
                        + [f'/assets/img/{name}.jpg {full_w}w'])
        webp_w = pixel_width(os.path.join(img_dir, f'{name}.webp')) or full_w
        webp = ', '.join([f'/assets/img/{name}-{w}.webp {pixel_width(os.path.join(img_dir, f"{name}-{w}.webp")) or vw}w'
                          for w, vw in variants] + [f'/assets/img/{name}.webp {webp_w}w'])
        return (f'<picture{picture_class}><source type="image/webp" srcset="{webp}" sizes="{sizes}">'
                f'<img{attrs} src="/assets/img/{name}.jpg" srcset="{jpg}" sizes="{sizes}"></picture>')
    return IMG_RE.sub(repl, body)

def image_size(path):
    try:
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


def git_lastmod(path, fallback):
    try:
        out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', path],
                             cwd=ROOT, capture_output=True, text=True, timeout=10)
        d = out.stdout.strip()
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', d):
            return d
    except Exception:
        pass
    return fallback


def head_meta(meta, og_image):
    """og and twitter tags that vary per page, plus robots when noindex is set."""
    esc = lambda v: _html.escape(str(v), quote=True)
    tags = [
        '<meta property="og:locale" content="en_US">',
        f'<meta property="og:image:alt" content="{esc(meta.get("og_alt", DEFAULT_OG_ALT))}">',
    ]
    size = image_size(os.path.join(SRC, 'assets/img', og_image))
    if size:
        tags.append(f'<meta property="og:image:width" content="{size[0]}">')
        tags.append(f'<meta property="og:image:height" content="{size[1]}">')
    tags += [
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(meta["title"])}">',
        f'<meta name="twitter:description" content="{esc(meta["description"])}">',
    ]
    if meta.get('noindex') or PREVIEW:
        tags.append('<meta name="robots" content="noindex, follow">')
    return '\n'.join(tags)


def hash_assets():
    """Rename build-output CSS and JavaScript assets to include a content hash.

    Returns {original href: hashed href} for rewriting the layout.
    """
    mapping = {}
    for rel in ('css/site.css', 'css/fonts.css', 'js/site.js', 'js/analytics.js'):
        full = os.path.join(DIST, 'assets', rel)
        if not os.path.isfile(full):
            continue
        with open(full, 'rb') as f:
            digest = hashlib.sha256(f.read()).hexdigest()[:8]
        stem, ext = os.path.splitext(rel)
        new_rel = f'{stem}.{digest}{ext}'
        os.rename(full, os.path.join(DIST, 'assets', new_rel))
        mapping[f'/assets/{rel}'] = f'/assets/{new_rel}'
    return mapping


def build():
    review = os.environ.get('REVIEW') == '1'
    print(f'mode: {"review (chips and .ph kept)" if review else "production (chips and .ph stripped)"}')
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(DIST, 'assets'),
                    ignore=shutil.ignore_patterns('MANIFEST*.md'))
    assets = hash_assets()

    layout = read(os.path.join(SRC, 'layout.html'))
    layout = layout.replace('{{site_url}}', _html.escape(SITE, quote=True))
    layout = layout.replace('{{gtm_id}}', GTM_ID if not PREVIEW else '')
    layout = layout.replace('{{ga4_id}}', GA4_ID if not PREVIEW else '')
    layout = layout.replace('{{analytics_host}}', _html.escape(_origin.hostname, quote=True))
    for old, new in assets.items():
        layout = layout.replace(old, new)

    pages = sorted(f for f in os.listdir(os.path.join(SRC, 'pages')) if f.endswith('.html'))
    today = datetime.date.today().isoformat()
    urls = []
    for fn in pages:
        slug = fn[:-5]
        src_path = os.path.join(SRC, 'pages', fn)
        raw = read(src_path)
        m = re.match(r'\s*<!--meta\s*(\{.*?\})\s*-->\s*', raw, re.S)
        if not m:
            sys.exit(f'{fn}: missing meta block')
        meta = json.loads(m.group(1))
        body = CONFIRM_RE.sub('', raw[m.end():])
        og_image = meta.get('og_image', 'home-poster.jpg')
        canonical = '' if slug in ('index', '404') else slug + '/'
        title = _html.escape(meta['title'], quote=True)
        description = _html.escape(meta['description'], quote=True)

        html = layout
        html = html.replace('{{head_meta}}', head_meta(meta, og_image))
        html = html.replace('{{title}}', title)
        html = html.replace('{{description}}', description)
        html = html.replace('{{canonical}}', canonical)
        html = html.replace('{{og_image}}', og_image)
        html = html.replace('{{jsonld}}', jsonld(meta, slug))
        html = re.sub(r'\{\{active:([a-z-]+)\}\}', lambda mm: 'aria-current="page"' if mm.group(1) == slug else '', html)
        html = html.replace('{{content}}', responsive_images(body))
        if meta.get('noindex'):
            html = re.sub(r'\n<link rel="canonical"[^>]*>', '', html, count=1)
        html = CONFIRM_RE.sub('', html)
        if not review:
            html = strip_review_markup(html)

        if slug == '404':
            out_path = os.path.join(DIST, '404.html')
        else:
            out_dir = DIST if slug == 'index' else os.path.join(DIST, slug)
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, 'index.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        if slug != '404' and not meta.get('noindex') and not PREVIEW:
            urls.append((f'{SITE}/{canonical}', git_lastmod(src_path, today)))
        print(f'  {slug:20s} -> {os.path.relpath(out_path, ROOT)}')

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lastmod in urls:
        sm.append(f'  <url><loc>{u}</loc><lastmod>{lastmod}</lastmod></url>')
    sm.append('</urlset>')
    with open(os.path.join(DIST, 'sitemap.xml'), 'w') as f:
        f.write('\n'.join(sm))
    with open(os.path.join(DIST, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    for old, new in assets.items():
        print(f'  asset {old} -> {new}')
    print(f'built {len(pages)} pages')


if __name__ == '__main__':
    build()
