#!/usr/bin/env python3
"""Assemble the static site from src/ into dist/. Standard library only. Pillow
is used when it is installed; a header parser in this file reads the same
dimensions when it is not.

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
import json, os, re, shutil, sys, hashlib, html as _html, subprocess
from urllib.parse import urlsplit

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
DIST = os.path.join(ROOT, 'dist')
IMG_DIR = os.path.join(SRC, 'assets', 'img')
LOGO_DIR = os.path.join(SRC, 'assets', 'logo')


def site_url():
    """The canonical host every absolute URL in the build is written against.

    SITE_URL wins when it is set, so a one-off build can be pointed anywhere.
    Vercel sets VERCEL_PROJECT_PRODUCTION_URL on every deployment to "the
    shortest production custom domain, or vercel.app domain if no custom domain
    is available", so before the DNS cutover the staging host canonicalises to
    itself and after the cutover the real domain takes over with no code change.
    """
    env = os.environ.get('SITE_URL')
    if env:
        return env.rstrip('/')
    vercel = os.environ.get('VERCEL_PROJECT_PRODUCTION_URL')
    if vercel:
        return 'https://' + vercel.strip().rstrip('/')
    return 'https://spontaneouscafe.com'


SITE = site_url()
_origin = urlsplit(SITE)
if (_origin.scheme != 'https' or not _origin.hostname or _origin.path or
        _origin.query or _origin.fragment or _origin.username or _origin.port):
    raise ValueError('SITE_URL must be an HTTPS origin without a path, port or credentials')
PREVIEW = os.environ.get('VERCEL_ENV', 'production') != 'production' or os.environ.get('REVIEW') == '1'
GA4_ID = os.environ.get('GA4_ID', 'G-VCT34ZQC92').strip()
if GA4_ID and not re.fullmatch(r'G-[A-Z0-9]+', GA4_ID):
    raise ValueError('GA4_ID must be a GA4 measurement ID, or unset')
PHONE = '+1-707-972-6647'
EMAIL = 'chefmattsamuelson@gmail.com'
DEFAULT_OG_ALT = 'The Spontaneous Cafe, Mendocino'

# The three hour tiers. Any service, any page. See CONTEXT.md.
# (offer name, price, hours for the contact-form query string, booking wording)
TIERS = [
    ('Three hours', '300', '3', 'Three-hour'),
    ('Six hours', '500', '6', 'Six-hour'),
    ('Twelve hours', '1000', '12', 'Twelve-hour'),
]

# meta "service" value -> (serviceType, slug, contact-form service parameter)
SERVICES = {
    'Foraging excursions': ('Guided foraging excursion', 'foraging', 'Foraging%20excursion'),
    'Private chef': ('Private chef service', 'private-chef', 'Private%20chef'),
    'Catering and events': ('Event catering', 'catering', 'Catering%20and%20events'),
    'Cooking classes': ('Cooking class', 'cooking-classes', 'Cooking%20class'),
}

# The places Matt travels to, each a node the Service nodes point at by @id.
COUNTY = 'Mendocino County, California'
AREAS = [
    ('City', 'Mendocino', 'area-mendocino'),
    ('City', 'Fort Bragg', 'area-fort-bragg'),
    ('City', 'Little River', 'area-little-river'),
    ('City', 'Albion', 'area-albion'),
    ('City', 'Elk', 'area-elk'),
    ('AdministrativeArea', 'Anderson Valley', 'area-anderson-valley'),
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


def area_nodes():
    """The six places, defined once per page inside the business node."""
    return [{
        "@type": kind,
        "@id": f'{SITE}/#{frag}',
        "name": name,
        "containedInPlace": {"@type": "AdministrativeArea", "name": COUNTY},
    } for kind, name, frag in AREAS]


def area_refs():
    return [{"@id": f'{SITE}/#{frag}'} for _, _, frag in AREAS]


def tier_offers(service_name=None, param=None):
    """The three hour tiers as Offers. With no service they are the generic
    booking tiers on the business node; with one they carry the service name and
    a contact link that pre-selects the service and the tier."""
    out = []
    for name, price, hours, booking in TIERS:
        if service_name:
            item_name = f'{service_name}, {name.lower()}'
            url = f'{SITE}/contact/?service={param}&tier={hours}%20hours'
        else:
            item_name = f'{booking} booking, any service'
            url = f'{SITE}/contact/'
        out.append({
            "@type": "Offer",
            "name": name,
            "price": price,
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "url": url,
            "itemOffered": {"@type": "Service", "name": item_name},
        })
    return out


def logo_image_object():
    """The PNG wordmark rendered from the SVG. Google's logo guidelines do not
    accept SVG, so the property is dropped when the PNG is missing."""
    path = os.path.join(LOGO_DIR, 'wordmark.png')
    size = image_size(path)
    if not size:
        return None
    return {
        "@type": "ImageObject",
        "url": SITE + "/assets/logo/wordmark.png",
        "width": size[0],
        "height": size[1],
    }


def business_ref():
    return {"@id": SITE + "/#business"}


def person_ref():
    return {"@id": SITE + "/about/#matt"}


def business_node(founder):
    """One LocalBusiness for the whole site. Every page carries it, either as
    the top-level node or nested under the node that is, so the eight pages
    describe one business rather than eight.

    No geo: the coordinates have not been checked against the Google Business
    Profile, and a wrong pin is worse than none.
    No sameAs: the LinkedIn, Facebook, Instagram and Alignable profiles found in
    R3 go in only after Matt confirms each one is his.
    No openingHoursSpecification: Matt books by inquiry and has not stated the
    hours he answers the phone.
    No aggregateRating and no review: a business may not mark up its own
    reviews. Reviews live on the Google Business Profile.
    """
    node = {
        "@type": "LocalBusiness",
        "@id": SITE + "/#business",
        "name": "The Spontaneous Cafe",
        "alternateName": "Spontaneous Cafe",
        # Both URIs checked on 2026-09-19: a 303 to /doc/<term>, which returns
        # 200. Product Ontology carries the specificity schema.org has no type
        # for, without claiming a venue the business does not have.
        "additionalType": [
            "http://www.productontology.org/id/Personal_chef",
            "http://www.productontology.org/id/Catering",
        ],
        "description": ("Chef Matt Samuelson forages, shops and cooks on the Mendocino coast. "
                        "Foraging excursions, private chef dinners, catering and cooking classes, "
                        "anywhere in the greater Mendocino area."),
        "url": SITE + "/",
        "slogan": "Local, Organic, Wild",
        "foundingDate": "2009",
        "founder": founder,
        "telephone": PHONE,
        "email": EMAIL,
        "priceRange": "$300 to $1,000 per booking",
        "currenciesAccepted": "USD",
        # Real photographs of Matt. The stock images never stand in for the
        # business here, because this is the image a knowledge panel may use.
        "image": [
            SITE + "/assets/img/matt-kitchen.jpg",
            SITE + "/assets/img/matt-square.jpg",
        ],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Mendocino",
            "addressRegion": "CA",
            "addressCountry": "US",
            # No streetAddress: the business is service-area, not a venue.
            # postalCode must match the Google Business Profile exactly and
            # Mendocino (95460) and Albion (95410) are both plausible. Needs Matt.
        },
        "hasMap": "https://www.google.com/maps?cid=7343978535458024901",
        "areaServed": area_nodes(),
        "knowsAbout": [
            "Foraging",
            "Wild mushrooms",
            "Sea salt harvesting",
            "Farm-to-table cooking",
            "Private chef service",
            "Catering",
            "Culinary instruction",
        ],
        "makesOffer": tier_offers(),
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Foraging excursions", "url": SITE + "/foraging/"}},
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Private chef", "url": SITE + "/private-chef/"}},
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Catering and events", "url": SITE + "/catering/"}},
                {"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": "Cooking classes", "url": SITE + "/cooking-classes/"}},
            ],
        },
    }
    logo = logo_image_object()
    if logo:
        node["logo"] = logo
    return node


def person_node(works_for):
    return {
        "@type": "Person",
        "@id": SITE + "/about/#matt",
        "name": "Matthew Samuelson",
        "alternateName": "Chef Matt Samuelson",
        "givenName": "Matthew",
        "familyName": "Samuelson",
        "jobTitle": "Chef",
        "description": ("Chef, forager and culinary instructor on the Mendocino coast. "
                        "Head chef and culinary instructor at Living Light Culinary Arts "
                        "Institute in Fort Bragg (2000 to 2004, 2008 to 2009, 2017 to 2019). "
                        "Executive chef at Flow Restaurant and Lounge in Mendocino "
                        "(2015 to 2017). Senior R&D chef at Alive & Radiant Foods "
                        "(2011 to 2015). Co-founder of High Integrity Foods since 2006. "
                        "Has lived on the Mendocino coast for over twenty-five years and founded The Spontaneous Cafe in 2009."),
        "url": SITE + "/about/",
        "image": SITE + "/assets/img/matt-kitchen.jpg",
        "worksFor": works_for,
        "hasOccupation": {
            "@type": "Occupation",
            "name": "Chef",
            "occupationLocation": {"@type": "AdministrativeArea", "name": COUNTY},
        },
        "affiliation": [
            {"@type": "Organization", "name": "Living Light Culinary Arts Institute"},
            {"@type": "Organization", "name": "Esalen Institute"},
        ],
        "knowsAbout": [
            "Foraging",
            "Wild mushroom identification",
            "Sea salt harvesting",
            "Raw food cuisine",
            "Vegan cuisine",
            "Gluten free cuisine",
            "Menu development",
            "Culinary instruction",
        ],
        "sameAs": ["https://www.esalen.org/faculty/matt-samuelson"],
    }


def website_node():
    return {
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": "The Spontaneous Cafe",
        "inLanguage": "en-US",
        "publisher": business_ref(),
    }


def webpage_node(meta, page_url, og_image):
    return {
        "@type": "WebPage",
        "@id": page_url + "#webpage",
        "url": page_url,
        "name": meta['title'],
        "description": meta['description'],
        "inLanguage": "en-US",
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": f'{SITE}/assets/img/{og_image}',
        },
        "isPartOf": website_node(),
    }


def service_node(meta, page_url, og_image):
    service = meta['service']
    service_type, _slug, param = SERVICES[service]
    return {
        "@type": "Service",
        "@id": page_url + "#service",
        "name": service,
        "serviceType": service_type,
        "url": page_url,
        "description": meta['description'],
        "image": f'{SITE}/assets/img/{og_image}',
        "areaServed": area_refs(),
        "offers": tier_offers(service, param),
    }


def jsonld(meta, slug, og_image):
    """One entity tree per page. The node the page is about sits at the top and
    the rest hang off it, each with its own @id, which is how Google reads
    nested nodes as the same entities across pages. Noindex pages get nothing,
    because markup for a page that asks not to be indexed has no reader.

    Every @id referenced on a page is also defined on it: the six place nodes
    are written out once inside the business node's areaServed, and a Service
    points at them by @id from the same page.
    """
    if meta.get('noindex'):
        return ''
    canonical = '' if slug == 'index' else slug + '/'
    page_url = f'{SITE}/{canonical}'
    if meta.get('service'):
        node = service_node(meta, page_url, og_image)
        node["provider"] = business_node(person_node(business_ref()))
    elif slug == 'about':
        node = person_node(business_node(person_ref()))
    else:
        node = business_node(person_node(business_ref()))
    node["mainEntityOfPage"] = webpage_node(meta, page_url, og_image)
    data = {"@context": "https://schema.org"}
    data.update(node)
    # A literal </ inside the script would close the element early.
    return json.dumps(data, indent=0).replace('</', '<\\/')


IMG_RE = re.compile(r'<img\b([^>]*?)\ssrc="/assets/img/([A-Za-z0-9_-]+)\.jpg"([^>]*)>')
ANY_IMG_RE = re.compile(r'<img\b[^>]*>')
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


def hero_preload(body):
    """Preload tag for the hero poster, which is the largest image on the five
    hero pages and the element the LCP is measured on.

    The poster is an <img class="hero__poster"> sibling of the video, so
    responsive_images() wraps it in <picture> and the browser has a WebP choice.
    The candidates named here are the same files with the same descriptors, so
    the preload and the picture resolve to one request. Pages with no such image
    get no preload."""
    for tag in ANY_IMG_RE.finditer(body):
        attrs = tag.group(0)
        cm = re.search(r'\sclass="([^"]*)"', attrs)
        if not cm or 'hero__poster' not in cm.group(1).split():
            continue
        sm = re.search(r'\ssrc="/assets/img/([A-Za-z0-9_-]+)\.jpg"', attrs)
        if not sm:
            continue
        name = sm.group(1)
        candidates = []
        for w in (480, 800, 1200):
            vw = pixel_width(os.path.join(IMG_DIR, f'{name}-{w}.webp'))
            if vw:
                candidates.append(f'/assets/img/{name}-{w}.webp {vw}w')
        full_w = pixel_width(os.path.join(IMG_DIR, f'{name}.webp'))
        if full_w:
            candidates.append(f'/assets/img/{name}.webp {full_w}w')
        if not candidates:
            return ''
        return ('<link rel="preload" as="image" '
                f'href="/assets/img/{name}.jpg" '
                f'imagesrcset="{", ".join(candidates)}" '
                'imagesizes="100vw" fetchpriority="high">')
    return ''


def _pillow_size(path):
    try:
        from PIL import Image
    except Exception:
        return None
    try:
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


def _jpeg_size(f):
    """Width and height from the first frame header. Every SOF marker from C0
    to CF carries them except C4 (Huffman tables), C8 (reserved) and CC
    (arithmetic coding conditioning), which are not frame headers."""
    f.seek(0)
    if f.read(2) != b'\xff\xd8':
        return None
    while True:
        byte = f.read(1)
        if not byte:
            return None
        if byte != b'\xff':
            continue
        marker = f.read(1)
        while marker == b'\xff':          # fill bytes before the marker
            marker = f.read(1)
        if not marker:
            return None
        code = marker[0]
        if code == 0x00 or code == 0x01 or 0xD0 <= code <= 0xD8:
            continue                      # standalone, no payload to skip
        if code == 0xD9:
            return None                   # end of image, no frame header found
        raw = f.read(2)
        if len(raw) < 2:
            return None
        length = int.from_bytes(raw, 'big')
        if 0xC0 <= code <= 0xCF and code not in (0xC4, 0xC8, 0xCC):
            payload = f.read(5)
            if len(payload) < 5:
                return None
            height = int.from_bytes(payload[1:3], 'big')
            width = int.from_bytes(payload[3:5], 'big')
            return width, height
        if length < 2:
            return None
        f.seek(length - 2, 1)


def _png_size(f):
    """IHDR is required to be the first chunk, and it opens with the size."""
    f.seek(0)
    head = f.read(24)
    if len(head) < 24 or head[:8] != b'\x89PNG\r\n\x1a\n' or head[12:16] != b'IHDR':
        return None
    return int.from_bytes(head[16:20], 'big'), int.from_bytes(head[20:24], 'big')


def _webp_size(f):
    """RIFF container, three encodings. VP8 is the lossy bitstream, VP8L the
    lossless one with the size packed into 14 bits each, VP8X the extended
    header whose canvas size is stored as 24-bit values minus one."""
    f.seek(0)
    head = f.read(30)
    if len(head) < 16 or head[:4] != b'RIFF' or head[8:12] != b'WEBP':
        return None
    fourcc = head[12:16]
    if fourcc == b'VP8 ':
        if len(head) < 30 or head[23:26] != b'\x9d\x01\x2a':
            return None
        return (int.from_bytes(head[26:28], 'little') & 0x3FFF,
                int.from_bytes(head[28:30], 'little') & 0x3FFF)
    if fourcc == b'VP8L':
        if len(head) < 25 or head[20] != 0x2F:
            return None
        bits = int.from_bytes(head[21:25], 'little')
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    if fourcc == b'VP8X':
        if len(head) < 30:
            return None
        return (int.from_bytes(head[24:27], 'little') + 1,
                int.from_bytes(head[27:30], 'little') + 1)
    return None


def _header_size(path):
    try:
        with open(path, 'rb') as f:
            magic = f.read(12)
            if magic[:2] == b'\xff\xd8':
                return _jpeg_size(f)
            if magic[:8] == b'\x89PNG\r\n\x1a\n':
                return _png_size(f)
            if magic[:4] == b'RIFF' and magic[8:12] == b'WEBP':
                return _webp_size(f)
    except Exception:
        return None
    return None


def image_size(path):
    """Width and height of an image file.

    Pillow first when it is importable, then the header parser above. The
    parser is what keeps srcsets and og:image dimensions working on a host
    where the install step did not run. A file that is on disk under
    src/assets/img and that neither reader can measure ends the build, because
    the alternative is shipping a site with every srcset quietly dropped.
    """
    if not os.path.isfile(path):
        return None
    size = _pillow_size(path) or _header_size(path)
    if not size and os.path.abspath(path).startswith(IMG_DIR + os.sep):
        sys.exit(f'cannot read the pixel size of {os.path.relpath(path, ROOT)}. '
                 'Responsive images and og:image dimensions would be dropped '
                 'without it, so the build stops here.')
    return size


def git_lastmod(path):
    """Commit date of the page source, or None when git cannot date it. A file
    git does not know about gets no lastmod rather than today's date, which
    would claim a change that did not happen."""
    try:
        out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', path],
                             cwd=ROOT, capture_output=True, text=True, timeout=10)
        d = out.stdout.strip()
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', d):
            return d
    except Exception:
        pass
    return None


def head_meta(meta, og_image, body):
    """og and twitter tags that vary per page, the robots directive, and the
    hero poster preload."""
    esc = lambda v: _html.escape(str(v), quote=True)
    tags = [
        '<meta property="og:locale" content="en_US">',
        f'<meta property="og:image:alt" content="{esc(meta.get("og_alt", DEFAULT_OG_ALT))}">',
    ]
    size = image_size(os.path.join(IMG_DIR, og_image))
    if size:
        tags.append(f'<meta property="og:image:width" content="{size[0]}">')
        tags.append(f'<meta property="og:image:height" content="{size[1]}">')
    tags += [
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(meta["title"])}">',
        f'<meta name="twitter:description" content="{esc(meta["description"])}">',
        f'<meta name="twitter:image" content="{SITE}/assets/img/{og_image}">',
    ]
    if meta.get('noindex') or PREVIEW:
        tags.append('<meta name="robots" content="noindex, follow">')
    else:
        tags.append('<meta name="robots" content="index, follow, max-image-preview:large, '
                    'max-snippet:-1, max-video-preview:-1">')
    preload = hero_preload(body)
    if preload:
        tags.append(preload)
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


def copy_root_icons():
    """Safari on iOS and several link-preview crawlers ignore an SVG favicon and
    ask the site root for these two files."""
    for name in ('favicon.ico', 'apple-touch-icon.png'):
        src = os.path.join(LOGO_DIR, name)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(DIST, name))
            print(f'  icon  {name}')
        else:
            print(f'  icon  {name} missing in src/assets/logo, not copied')


def build():
    review = os.environ.get('REVIEW') == '1'
    print(f'mode: {"review (chips and .ph kept)" if review else "production (chips and .ph stripped)"}')
    print(f'host: {SITE}')
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(DIST, 'assets'),
                    ignore=shutil.ignore_patterns('MANIFEST*.md'))
    assets = hash_assets()
    copy_root_icons()

    layout = read(os.path.join(SRC, 'layout.html'))
    layout = layout.replace('{{site_url}}', _html.escape(SITE, quote=True))
    layout = layout.replace('{{ga4_id}}', GA4_ID if not PREVIEW and _origin.hostname == 'spontaneouscafe.com' else '')
    layout = layout.replace('{{analytics_host}}', _html.escape(_origin.hostname, quote=True))
    for old, new in assets.items():
        layout = layout.replace(old, new)

    pages = sorted(f for f in os.listdir(os.path.join(SRC, 'pages')) if f.endswith('.html'))
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
        html = html.replace('{{head_meta}}', head_meta(meta, og_image, body))
        html = html.replace('{{title}}', title)
        html = html.replace('{{description}}', description)
        html = html.replace('{{canonical}}', canonical)
        html = html.replace('{{og_image}}', og_image)
        ld = jsonld(meta, slug, og_image)
        if ld:
            html = html.replace('{{jsonld}}', ld)
        else:
            html = re.sub(r'\n?<script type="application/ld\+json">\{\{jsonld\}\}</script>',
                          '', html, count=1)
        html = re.sub(r'\{\{active:([a-z-]+)\}\}', lambda mm: 'aria-current="page"' if mm.group(1) == slug else '', html)
        html = html.replace('{{content}}', responsive_images(body))
        if meta.get('noindex'):
            html = re.sub(r'\n<link rel="canonical"[^>]*>', '', html, count=1)
            html = re.sub(r'\n<meta property="og:url"[^>]*>', '', html, count=1)
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
            urls.append((f'{SITE}/{canonical}', git_lastmod(src_path)))
        print(f'  {slug:20s} -> {os.path.relpath(out_path, ROOT)}')

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lastmod in urls:
        stamp = f'<lastmod>{lastmod}</lastmod>' if lastmod else ''
        sm.append(f'  <url><loc>{u}</loc>{stamp}</url>')
    sm.append('</urlset>')
    with open(os.path.join(DIST, 'sitemap.xml'), 'w') as f:
        f.write('\n'.join(sm))
    with open(os.path.join(DIST, 'robots.txt'), 'w') as f:
        f.write('# Search and AI crawlers are welcome here. This is deliberate.\n'
                'User-agent: *\n'
                'Allow: /\n'
                'Disallow: /api/\n'
                f'Sitemap: {SITE}/sitemap.xml\n')
    for old, new in assets.items():
        print(f'  asset {old} -> {new}')
    print(f'built {len(pages)} pages')


if __name__ == '__main__':
    build()
