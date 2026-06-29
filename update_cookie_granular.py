import os, re

HTML_DIR = '/Users/josefbina/Desktop/Web PBŘS'

NEW_BANNER = '''\
<div id="cookie-overlay" class="cookie-overlay hidden"></div>
<div id="cookie-banner" class="cookie-banner hidden" role="dialog" aria-modal="true" aria-label="Nastavení cookies">
  <button class="cookie-banner-close" id="cookie-close" aria-label="Zavřít" type="button">&#x2715;</button>
  <div class="cookie-banner-icon">
    <svg viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
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
      <ellipse cx="40" cy="46" rx="30" ry="8" fill="rgba(0,0,0,0.15)"/>
      <circle cx="40" cy="38" r="32" fill="url(#cbg)"/>
      <ellipse cx="30" cy="24" rx="13" ry="8" fill="rgba(255,255,255,0.2)" transform="rotate(-20 30 24)"/>
      <ellipse cx="28" cy="28" rx="4.5" ry="3.5" fill="url(#cbg2)" transform="rotate(-15 28 28)"/>
      <ellipse cx="48" cy="24" rx="3.5" ry="4.5" fill="url(#cbg2)" transform="rotate(10 48 24)"/>
      <ellipse cx="23" cy="44" rx="4" ry="3.2" fill="url(#cbg2)" transform="rotate(-5 23 44)"/>
      <ellipse cx="43" cy="43" rx="4.5" ry="3.5" fill="url(#cbg2)" transform="rotate(20 43 43)"/>
      <ellipse cx="53" cy="50" rx="3.5" ry="4.5" fill="url(#cbg2)" transform="rotate(-10 53 50)"/>
      <ellipse cx="33" cy="55" rx="3.2" ry="4" fill="url(#cbg2)" transform="rotate(15 33 55)"/>
    </svg>
  </div>
  <strong class="cookie-banner-title">Cookies &amp; soukromí</strong>
  <p class="cookie-banner-body">Používáme cookies pro zlepšení webu a analýzu návštěvnosti. Sv&#367;j výběr m&#367;žete kdykoli změnit.</p>
  <div class="cookie-categories" id="cookie-cats">
    <label class="cookie-category">
      <div class="cookie-cat-check">
        <input type="checkbox" id="cc-essential" checked disabled>
        <span class="cookie-cat-checkmark"></span>
      </div>
      <div class="cookie-cat-text">
        <strong>Základní</strong>
        <p>Zaji&#353;&#357;ují fungování webu, bez nich budou stránky nefunk&#269;ní.</p>
      </div>
    </label>
    <label class="cookie-category">
      <div class="cookie-cat-check">
        <input type="checkbox" id="cc-preference">
        <span class="cookie-cat-checkmark"></span>
      </div>
      <div class="cookie-cat-text">
        <strong>Preferen&#269;ní</strong>
        <p>Díky nim vám m&#367;žeme zobrazit obsah p&#345;izp&#367;sobený va&#353;im preferencím.</p>
      </div>
    </label>
    <label class="cookie-category">
      <div class="cookie-cat-check">
        <input type="checkbox" id="cc-analytics">
        <span class="cookie-cat-checkmark"></span>
      </div>
      <div class="cookie-cat-text">
        <strong>Analytické</strong>
        <p>Pomáhají nám pochopit, jak máme web dále vylep&#353;ovat.</p>
      </div>
    </label>
    <label class="cookie-category">
      <div class="cookie-cat-check">
        <input type="checkbox" id="cc-marketing">
        <span class="cookie-cat-checkmark"></span>
      </div>
      <div class="cookie-cat-text">
        <strong>Marketingové</strong>
        <p>Díky nim vás m&#367;žeme znovu oslovit v p&#345;ípad&#283; akcí nebo novinek.</p>
      </div>
    </label>
    <label class="cookie-category">
      <div class="cookie-cat-check">
        <input type="checkbox" id="cc-addata">
        <span class="cookie-cat-checkmark"></span>
      </div>
      <div class="cookie-cat-text">
        <strong>Reklamní údaje</strong>
        <p>Va&#353;e údaje m&#367;žeme použít v reklamních systémech, jako je Google Ads.</p>
      </div>
    </label>
    <label class="cookie-category">
      <div class="cookie-cat-check">
        <input type="checkbox" id="cc-adperson">
        <span class="cookie-cat-checkmark"></span>
      </div>
      <div class="cookie-cat-text">
        <strong>Personalizace reklam</strong>
        <p>Va&#353;e údaje m&#367;žeme p&#345;idat do publik pro ná&#353; remarketing.</p>
      </div>
    </label>
  </div>
  <button class="cookie-toggle-details" id="cookie-toggle" type="button">
    <span>Podrobné nastavení</span>
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M2 5l5 5 5-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>
  <div class="cookie-banner-btns">
    <button id="cookie-reject" class="cookie-btn-reject" type="button">Zamítnout v&#353;e</button>
    <button id="cookie-accept" class="cookie-btn-accept" type="button">Schválit v&#353;e</button>
  </div>
  <button id="cookie-save" class="cookie-btn-save" type="button">Uložit nastavení</button>
</div>
<script src="cookie-consent.js"></script>'''

NEW_CONSENT_INLINE = '(function(){try{var r=localStorage.getItem(\'spbs_consent\');if(!r)return;var p;try{p=JSON.parse(r);}catch(e){var g=r===\'granted\';p={preference:g,analytics:g,marketing:g,addata:g,adperson:g};}gtag(\'consent\',\'update\',{functionality_storage:\'granted\',personalization_storage:p.preference?\'granted\':\'denied\',analytics_storage:p.analytics?\'granted\':\'denied\',ad_storage:p.marketing?\'granted\':\'denied\',ad_user_data:p.addata?\'granted\':\'denied\',ad_personalization:p.adperson?\'granted\':\'denied\'});}catch(e){}})();'

OLD_CONSENT_INLINE_PAT = re.compile(
    r'\(function\(\)\{try\{var [cr]=localStorage\.getItem\(\'spbs_consent\'\).*?\}\}\)\(\);',
    re.DOTALL
)

BANNER_PAT = re.compile(
    r'<div id="cookie-overlay".*?<script src="cookie-consent\.js"></script>',
    re.DOTALL
)

html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html')])

for filename in html_files:
    filepath = os.path.join(HTML_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'cookie-overlay' not in content:
        print(f'SKIP (no cookie banner): {filename}')
        continue

    modified = BANNER_PAT.sub(NEW_BANNER, content, count=1)
    modified = OLD_CONSENT_INLINE_PAT.sub(NEW_CONSENT_INLINE, modified, count=1)

    if modified == content:
        print(f'NO CHANGE: {filename}')
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f'Updated: {filename}')

print('\nDone.')
