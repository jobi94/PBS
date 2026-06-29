import os, re

HTML_DIR = '/Users/josefbina/Desktop/Web PBŘS'

# Insert cookie-settings button right after the Mapa webu link
SITEMAP_PATTERN = re.compile(
    r'(<a href="sitemap\.html">Mapa webu</a>)(\s*</div>)',
    re.DOTALL
)
SITEMAP_REPLACEMENT = r'\1\n          <button id="cookie-settings" class="cookie-settings-link" type="button">Nastavení cookies</button>\2'

html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html')])

for filename in html_files:
    filepath = os.path.join(HTML_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'cookie-banner' not in content:
        print(f'SKIP (no cookie consent): {filename}')
        continue

    if 'cookie-settings' in content:
        print(f'SKIP (already done): {filename}')
        continue

    modified = SITEMAP_PATTERN.sub(SITEMAP_REPLACEMENT, content, count=1)

    if modified == content:
        print(f'NO MATCH: {filename}')
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f'Updated: {filename}')

print('\nDone.')
