#!/usr/bin/env python3
"""Check RSA copy against Google Ads character limits and policy basics."""
import re, sys

LIMITS = {'H': 30, 'D': 90}
bad = 0
ag = ''
for line in open('rsa-copy.md'):
    line = line.rstrip('\n')
    if line.startswith('## AG'):
        ag = line[3:].split('.')[0]
    m = re.match(r'^([HD])(\d+) \|(?:PIN \d\|)? ?(.+)$', line)
    if not m:
        continue
    kind, num, text = m.group(1), m.group(2), m.group(3).strip()
    limit = LIMITS[kind]
    n = len(text)
    flag = ''
    if n > limit:
        flag = f'  <-- OVER by {n - limit}'
        bad += 1
    if re.search(r'\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}', text):
        flag += '  <-- PHONE NUMBER, not allowed in ad text'
        bad += 1
    if '—' in text or '–' in text:
        flag += '  <-- DASH'
        bad += 1
    print(f'{ag:32} {kind}{num:<3} {n:>3}/{limit}{flag}')
print()
print('FAIL' if bad else 'All assets within limits, no phone numbers in ad text, no dashes.')
sys.exit(1 if bad else 0)
