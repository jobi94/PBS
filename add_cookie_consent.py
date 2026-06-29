import os

HTML_DIR = '/Users/josefbina/Desktop/Web PBŘS'

CONSENT_SCRIPT = """<script>
/* Google Consent Mode v2 — deny all by default until user chooses */
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {
  analytics_storage: 'denied',
  ad_storage: 'denied',
  ad_user_data: 'denied',
  ad_personalization: 'denied',
  functionality_storage: 'denied',
  personalization_storage: 'denied',
  security_storage: 'granted',
  wait_for_update: 1500
});
(function(){try{var c=localStorage.getItem('spbs_consent');if(c==='granted'){gtag('consent','update',{analytics_storage:'granted',ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',functionality_storage:'granted',personalization_storage:'granted'});}}catch(e){}})();
</script>
"""

CSS_LINK = '<link rel="stylesheet" href="cookie-consent.css">'

BODY_INJECT = """
<!-- Cookie Consent Banner -->
<div id="cookie-banner" class="cookie-banner hidden" role="dialog" aria-label="Souhlas s cookies">
  <div class="cookie-banner-inner">
    <div class="cookie-banner-text">
      <strong>Cookies &amp; soukromí</strong>
      <p>Používáme analytické cookies pro měření návštěvnosti a zlepšení webu. Vaše data nesbíráme pro reklamu bez vašeho souhlasu.</p>
    </div>
    <div class="cookie-banner-btns">
      <button id="cookie-reject" class="cookie-btn-reject" type="button">Odmítnout</button>
      <button id="cookie-accept" class="cookie-btn-accept" type="button">Přijmout vše</button>
    </div>
  </div>
</div>
<!-- Cookie FAB -->
<button id="cookie-fab" class="cookie-fab hidden" type="button" aria-label="Nastavení cookies" title="Nastavení cookies">
  <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <radialGradient id="cookie-fab-grad" cx="38%" cy="30%" r="68%">
        <stop offset="0%" stop-color="#f0b87a"/>
        <stop offset="55%" stop-color="#d4843a"/>
        <stop offset="100%" stop-color="#a0521a"/>
      </radialGradient>
    </defs>
    <ellipse cx="24" cy="27" rx="18" ry="5" fill="rgba(0,0,0,0.22)"/>
    <circle cx="24" cy="23" r="19" fill="url(#cookie-fab-grad)"/>
    <ellipse cx="18" cy="15" rx="8" ry="5" fill="rgba(255,255,255,0.18)" transform="rotate(-20 18 15)"/>
    <ellipse cx="17" cy="17" rx="2.8" ry="2.2" fill="#5c2e08" transform="rotate(-15 17 17)"/>
    <ellipse cx="29" cy="15" rx="2.2" ry="2.8" fill="#5c2e08" transform="rotate(10 29 15)"/>
    <ellipse cx="14" cy="27" rx="2.5" ry="2" fill="#5c2e08" transform="rotate(-5 14 27)"/>
    <ellipse cx="26" cy="26" rx="2.8" ry="2.2" fill="#5c2e08" transform="rotate(20 26 26)"/>
    <ellipse cx="32" cy="30" rx="2.2" ry="2.8" fill="#5c2e08" transform="rotate(-10 32 30)"/>
    <ellipse cx="20" cy="33" rx="2" ry="2.5" fill="#5c2e08" transform="rotate(15 20 33)"/>
  </svg>
</button>
<script src="cookie-consent.js"></script>
"""

html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html')])

for filename in html_files:
    filepath = os.path.join(HTML_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'cookie-banner' in content:
        print(f'SKIP (already done): {filename}')
        continue

    modified = content

    # 1. Insert consent default BEFORE GTM
    gtm_marker = '<!-- Google Tag Manager -->'
    if gtm_marker in modified:
        modified = modified.replace(gtm_marker, CONSENT_SCRIPT + gtm_marker, 1)
    else:
        print(f'  WARNING: no GTM marker in {filename}')

    # 2. Add CSS link before </head>
    if CSS_LINK not in modified:
        modified = modified.replace('</head>', CSS_LINK + '\n</head>', 1)

    # 3. Inject banner + FAB + JS before </body>
    modified = modified.replace('</body>', BODY_INJECT + '</body>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f'Updated: {filename}')

print('\nDone.')
