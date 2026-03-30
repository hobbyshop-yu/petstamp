# -*- coding: utf-8 -*-
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SITE = r'C:\Users\81808\Desktop\pet-stamp-lp'
BASE = '/petstamp'
count = 0

replacements = [
    ('href="/css/', f'href="{BASE}/css/'),
    ('src="/js/', f'src="{BASE}/js/'),
    ('src="/images/', f'src="{BASE}/images/'),
    ('href="/dogs/', f'href="{BASE}/dogs/'),
    ('href="/cats/', f'href="{BASE}/cats/'),
    ('href="/small-animals/', f'href="{BASE}/small-animals/'),
    ('href="/characters/', f'href="{BASE}/characters/'),
    ('href="/genre/', f'href="{BASE}/genre/'),
    ('href="/order/', f'href="{BASE}/order/'),
    ('href="/"', f'href="{BASE}/"'),
    ('href="/#', f'href="{BASE}/#'),
]

for root, dirs, files in os.walk(SITE):
    if '.git' in root:
        continue
    for f in files:
        if not f.endswith('.html'):
            continue
        fpath = os.path.join(root, f)
        with open(fpath, 'r', encoding='utf-8') as fp:
            content = fp.read()
        new = content
        for old, repl in replacements:
            new = new.replace(old, repl)
        if new != content:
            with open(fpath, 'w', encoding='utf-8') as fp:
                fp.write(new)
            count += 1
            print(f'  Fixed: {os.path.relpath(fpath, SITE)}')

print(f'Total fixed: {count} files')
