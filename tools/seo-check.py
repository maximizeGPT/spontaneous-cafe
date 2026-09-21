#!/usr/bin/env python3
"""Mechanical SEO checks on a built dist/ plus page-body parity against a git ref.

Run from the repo root after `python3 build.py`:
    python3 tools/seo-check.py            # checks dist/ only
    python3 tools/seo-check.py origin/main  # also confirms src/pages bodies equal that ref
                                          # apart from the meta block and the hero poster markup

Checks: one h1 per page; title 60 characters or fewer and description 120 to 155 on
indexable pages; every JSON-LD block parses and every @id reference resolves on its page;
no Review or AggregateRating; no JSON-LD on the 404; hero pages carry a picture element
and a matching image preload; robots meta and twitter:image present; every internal
href, src and srcset candidate resolves to a file in dist/. Exit code 1 on any failure.
"""
import re, json, glob, os, html, sys, subprocess

def check_dist():
    pages = sorted(glob.glob('dist/**/index.html', recursive=True)) + ['dist/404.html']
    issues = []
    for f in pages:
        s = open(f, encoding='utf-8').read()
        name = f.replace('dist/', '').replace('/index.html', '') or 'home'
        h1 = len(re.findall(r'<h1\b', s))
        title = html.unescape(re.search(r'<title>(.*?)</title>', s).group(1))
        desc = html.unescape(re.search(r'<meta name="description" content="(.*?)"', s).group(1))
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        ids, refs, types = set(), set(), []
        def walk(n):
            if isinstance(n, dict):
                if '@type' in n: types.append(n['@type'])
                if '@id' in n and len(n) > 1: ids.add(n['@id'])
                if '@id' in n and len(n) == 1: refs.add(n['@id'])
                for v in n.values(): walk(v)
            elif isinstance(n, list):
                for v in n: walk(v)
        for b in blocks: walk(json.loads(b.replace('<\\/', '</')))
        noindex = 'noindex' in s
        pic = s.count('<picture class="hero__poster"')
        pre = len(re.findall(r'<link rel="preload" as="image"', s))
        robots = bool(re.search(r'<meta name="robots" content="index, follow, max-image-preview:large', s))
        print(f"{name:16s} h1={h1} title={len(title):2d} desc={len(desc):3d} ld={len(blocks)} "
              f"dangling={len(refs - ids)} picture={pic} preload={pre} "
              f"robots={'ok' if robots else ('noindex' if noindex else 'MISSING')}")
        if h1 != 1: issues.append(f'{name}: h1 count {h1}')
        if not noindex and (len(title) > 60 or not 120 <= len(desc) <= 155): issues.append(f'{name}: title or description length')
        if refs - ids: issues.append(f'{name}: dangling @id {sorted(refs - ids)}')
        if any(t in ('Review', 'AggregateRating') for t in types): issues.append(f'{name}: review markup')
        if name == '404' and blocks: issues.append('404 carries JSON-LD')
        if pic != pre: issues.append(f'{name}: picture {pic} vs preload {pre}')
        if not noindex and not (robots and 'twitter:image' in s): issues.append(f'{name}: head tags')
    missing = set()
    for f in pages:
        s = open(f, encoding='utf-8').read()
        for u in set(re.findall(r'(?:href|src)="(/[^"#?]*)"', s)) | set(re.findall(r'(/assets/[^\s",]+)\s+\d+w', s)):
            p = 'dist' + u + ('index.html' if u.endswith('/') else '')
            if not os.path.exists(p): missing.add(u)
    print('missing internal targets:', sorted(missing) or 'none')
    if missing: issues.append('missing targets')
    print('ISSUES:', issues or 'none')
    return not issues

def check_parity(base):
    META = re.compile(r'\A\s*<!--meta\s*\{.*?\}\s*-->', re.S)
    IMG = re.compile(r'<img class="hero__poster"[^>]*>\s*')
    POSTER = re.compile(r'\s*poster="[^"]*"')
    bad = 0
    for fn in sorted(glob.glob('src/pages/*.html')):
        rel = fn.replace('\\', '/')
        a = subprocess.run(['git', 'show', f'{base}:{rel}'], capture_output=True, text=True).stdout
        b = open(fn, encoding='utf-8').read()
        if POSTER.sub('', META.sub('', a)).strip() != IMG.sub('', META.sub('', b)).strip():
            bad += 1; print('body differs from', base, ':', rel)
    print(f'pages differing from {base} beyond the meta block and hero markup: {bad}')
    return bad == 0

if __name__ == '__main__':
    ok = check_dist()
    if len(sys.argv) > 1:
        ok = check_parity(sys.argv[1]) and ok
    sys.exit(0 if ok else 1)
