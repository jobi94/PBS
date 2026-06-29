import os, re

HTML_DIR = '/Users/josefbina/Desktop/Web PBŘS'

COOKIE_SVG = """<svg viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="cbg" cx="38%" cy="30%" r="68%">
          <stop offset="0%" stop-color="#f5c07a"/>
          <stop offset="55%" stop-color="#d9862e"/>
          <stop offset="100%" stop-color="#a85218"/>
        </radialGradient>
        <radialGradient id="cbg2" cx="40%" cy="35%" r="60%">
          <stop offset="0%" stop-color="#7a3c10"/>
          <stop offset="100%" stop-color="#3d1c08"/>
        </radialGradient>
      </defs>
      <!-- shadow -->
      <ellipse cx="40" cy="46" rx="30" ry="8" fill="rgba(0,0,0,0.15)"/>
      <!-- body -->
      <circle cx="40" cy="38" r="32" fill="url(#cbg)"/>
      <!-- highlight -->
      <ellipse cx="30" cy="24" rx="13" ry="8" fill="rgba(255,255,255,0.2)" transform="rotate(-20 30 24)"/>
      <!-- chips -->
      <ellipse cx="28" cy="28" rx="4.5" ry="3.5" fill="url(#cbg2)" transform="rotate(-15 28 28)"/>
      <ellipse cx="48" cy="24" rx="3.5" ry="4.5" fill="url(#cbg2)" transform="rotate(10 48 24)"/>
      <ellipse cx="23" cy="44" rx="4" ry="3.2" fill="url(#cbg2)" transform="rotate(-5 23 44)"/>
      <ellipse cx="43" cy="43" rx="4.5" ry="3.5" fill="url(#cbg2)" transform="rotate(20 43 43)"/>
      <ellipse cx="53" cy="50" rx="3.5" ry="4.5" fill="url(#cbg2)" transform="rotate(-10 53 50)"/>
      <ellipse cx="33" cy="55" rx="3.2" ry="4" fill="url(#cbg2)" transform="rotate(15 33 55)"/>
    </svg>"""

NEW_BLOCK = """
<!-- Cookie Consent -->
<div id="cookie-overlay" class="cookie-overlay hidden"></div>
<div id="cookie-banner" class="cookie-banner hidden" role="dialog" aria-modal="true" aria-label="Souhlas s cookies">
  <div class="cookie-banner-icon">
    """ + COOKIE_SVG + """
  </div>
  <strong class="cookie-banner-title">Cookies &amp; soukromí</strong>
  <p class="cookie-banner-body">Používáme analytické cookies pro měření návštěvnosti a zlepšení webu. Vaše data nesbíráme pro reklamu bez vašeho souhlasu.</p>
  <div class="cookie-banner-btns">
    <button id="cookie-reject" class="cookie-btn-reject" type="button">Odmítnout</button>
    <button id="cookie-accept" class="cookie-btn-accept" type="button">Přijmout vše</button>
  </div>
</div>
<!-- Cookie re-open FAB -->
<button id="cookie-fab" class="cookie-fab hidden" type="button" aria-label="Nastavení cookies" title="Nastavení cookies">
  <svg viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <radialGradient id="cfab" cx="38%" cy="30%" r="68%">
        <stop offset="0%" stop-color="#f5c07a"/>
        <stop offset="55%" stop-color="#d9862e"/>
        <stop offset="100%" stop-color="#a85218"/>
      </radialGradient>
    </defs>
    <ellipse cx="21" cy="24" rx="16" ry="4" fill="rgba(0,0,0,0.18)"/>
    <circle cx="21" cy="20" r="17" fill="url(#cfab)"/>
    <ellipse cx="16" cy="13" rx="7" ry="4" fill="rgba(255,255,255,0.18)" transform="rotate(-20 16 13)"/>
    <ellipse cx="15" cy="15" rx="2.4" ry="1.9" fill="#5c2e08" transform="rotate(-15 15 15)"/>
    <ellipse cx="26" cy="13" rx="1.9" ry="2.4" fill="#5c2e08" transform="rotate(10 26 13)"/>
    <ellipse cx="12" cy="23" rx="2.1" ry="1.7" fill="#5c2e08" transform="rotate(-5 12 23)"/>
    <ellipse cx="23" cy="23" rx="2.4" ry="1.9" fill="#5c2e08" transform="rotate(20 23 23)"/>
    <ellipse cx="28" cy="27" rx="1.9" ry="2.4" fill="#5c2e08" transform="rotate(-10 28 27)"/>
    <ellipse cx="17" cy="29" rx="1.7" ry="2.1" fill="#5c2e08" transform="rotate(15 17 29)"/>
  </svg>
</button>
<script src="cookie-consent.js"></script>
"""

# Pattern: from <!-- Cookie Consent Banner --> to <script src="cookie-consent.js"></script>
OLD_PATTERN = re.compile(
    r'\n<!-- Cookie Consent Banner -->.*?<script src="cookie-consent\.js"></script>',
    re.DOTALL
)

html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html')])

for filename in html_files:
    filepath = os.path.join(HTML_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- Cookie Consent Banner -->' not in content:
        print(f'SKIP (no old block): {filename}')
        continue

    new_content = OLD_PATTERN.sub(NEW_BLOCK, content)

    if new_content == content:
        print(f'NO CHANGE: {filename}')
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Updated: {filename}')

print('\nDone.')
