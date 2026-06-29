import os, re

HTML_DIR = '/Users/josefbina/Desktop/Web PBŘS'

# The canonical footer (from index.html)
FOOTER = """<footer>
  <div class="footer-main">

    <!-- Brand -->
    <div class="footer-brand">
      <a href="index.html" class="footer-logo">
        <img src="img/logo.svg" alt="SPBS logo" />
        SPBS<span>.</span>
      </a>
      <p class="footer-tagline">Specializovaná firma na požární bezpečnost staveb se sídlem v Hradci Králové.</p>
    </div>

    <!-- Služby -->
    <div class="footer-col">
      <h4>Služby</h4>
      <div class="footer-col-links">
        <a href="skoleni-zamestnancu.html">Školení zaměstnanců</a>
        <a href="eps.html">EPS</a>
        <a href="protipozarni-ucpavky.html">Protipožární ucpávky</a>
        <a href="hasici-pristroje.html">Hasicí přístroje</a>
        <a href="soucinnost-hzs.html">Součinnost HZS</a>
        <a href="pozarni-dokumentace.html">Požární dokumentace</a>
      </div>
    </div>

    <!-- Společnost -->
    <div class="footer-col">
      <h4>Společnost</h4>
      <div class="footer-col-links">
        <a href="o-nas.html">O nás</a>
        <a href="nase-projekty.html">Naše projekty</a>
        <a href="partneri.html">Partneři</a>
        <a href="slovnik-pojmu.html">Slovník pojmů</a>
      </div>
    </div>

    <!-- Sídlo -->
    <div class="footer-col">
      <h4>Sídlo</h4>
      <div class="footer-col-contact">
        <div class="footer-contact-row">
          Správa požární bezpečnosti staveb s.r.o.<br>Zemědělská 1145/4a<br>Slezské Předměstí<br>500 03 Hradec Králové
        </div>
        <div class="footer-contact-row">
          <div class="footer-contact-label">Otevírací doba</div>
          Po – Pá: 7:00 – 17:00<br>So – Ne: Zavřeno
        </div>
      </div>
    </div>

    <!-- Fakturační údaje -->
    <div class="footer-col">
      <h4>Fakturační údaje</h4>
      <div class="footer-col-contact">
        <div class="footer-contact-row">
          IČO: 22016295<br>DIČ: CZ22016295<br>Datová schránka: m8xca3n
        </div>
      </div>
    </div>

  </div>
  <div class="footer-bottom">
    <div class="footer-bottom-inner">
      <span class="footer-copy">&copy; 2026 SPBS – Správa požární bezpečnosti staveb s.r.o.</span>
      <div class="footer-bottom-links">
        <a href="kontakt.html">Kontakt</a>
        <a href="o-nas.html">O nás</a>
        <a href="sitemap.html">Mapa webu</a>
          <button id="cookie-settings" class="cookie-settings-link" type="button">Nastavení cookies</button>
      </div>
    </div>
  </div>
</footer>"""

FOOTER_PATTERN = re.compile(r'<footer>.*?</footer>', re.DOTALL)

# Skip index.html — it's the source of truth
skip = {'index.html'}

html_files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html') and f not in skip])

for filename in html_files:
    filepath = os.path.join(HTML_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<footer>' not in content:
        print(f'SKIP (no footer): {filename}')
        continue

    modified = FOOTER_PATTERN.sub(FOOTER, content, count=1)

    if modified == content:
        print(f'NO CHANGE: {filename}')
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f'Updated: {filename}')

print('\nDone.')