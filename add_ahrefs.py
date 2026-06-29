import os

HTML_DIR = '/Users/josefbina/Desktop/Web PBŘS'

SNIPPET = '<script src="https://analytics.ahrefs.com/analytics.js" data-key="YGo/YNWCs2VKpoZcsc5v7Q" async></script>\n'

html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html')])

for filename in html_files:
    filepath = os.path.join(HTML_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'analytics.ahrefs.com' in content:
        print(f'SKIP (already done): {filename}')
        continue

    modified = content.replace('</head>', SNIPPET + '</head>', 1)

    if modified == content:
        print(f'NO MATCH: {filename}')
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f'Updated: {filename}')

print('\nDone.')
