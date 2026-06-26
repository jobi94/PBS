(function () {
  var KEY = 'spbs_consent';
  var CATS = ['preference', 'analytics', 'marketing', 'addata', 'adperson'];
  var ALL_TRUE = { preference: true, analytics: true, marketing: true, addata: true, adperson: true };

  function updateGtag(prefs) {
    if (typeof window.gtag !== 'function') return;
    window.gtag('consent', 'update', {
      functionality_storage:   'granted',
      personalization_storage: prefs.preference ? 'granted' : 'denied',
      analytics_storage:       prefs.analytics  ? 'granted' : 'denied',
      ad_storage:              prefs.marketing  ? 'granted' : 'denied',
      ad_user_data:            prefs.addata     ? 'granted' : 'denied',
      ad_personalization:      prefs.adperson   ? 'granted' : 'denied'
    });
  }

  function loadPrefs() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (typeof parsed === 'object' && parsed !== null) return parsed;
      var g = raw === 'granted';
      var legacy = {};
      CATS.forEach(function(c) { legacy[c] = g; });
      return legacy;
    } catch (e) { return null; }
  }

  function savePrefs(prefs) {
    try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) {}
    updateGtag(prefs);
  }

  function readCheckboxes() {
    var prefs = {};
    CATS.forEach(function(cat) {
      var el = document.getElementById('cc-' + cat);
      prefs[cat] = el ? el.checked : false;
    });
    return prefs;
  }

  function applyCheckboxes(prefs) {
    CATS.forEach(function(cat) {
      var el = document.getElementById('cc-' + cat);
      if (el) el.checked = prefs ? !!(prefs[cat]) : true;
    });
  }

  function setVisible(show) {
    var overlay = document.getElementById('cookie-overlay');
    var banner  = document.getElementById('cookie-banner');
    if (!banner) return;
    if (show) {
      if (overlay) overlay.classList.remove('hidden');
      banner.classList.remove('hidden');
    } else {
      if (overlay) overlay.classList.add('hidden');
      banner.classList.add('hidden');
    }
  }

  function closeCategories() {
    var cats   = document.getElementById('cookie-cats');
    var toggle = document.getElementById('cookie-toggle');
    var save   = document.getElementById('cookie-save');
    if (cats)   { cats.classList.remove('open'); }
    if (toggle) { toggle.classList.remove('open'); }
    if (save)   { save.classList.remove('visible'); }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var prefs = loadPrefs();

    if (!prefs) {
      applyCheckboxes(ALL_TRUE);
      setVisible(true);
    } else {
      applyCheckboxes(prefs);
      updateGtag(prefs);
    }

    var toggleBtn   = document.getElementById('cookie-toggle');
    var acceptBtn   = document.getElementById('cookie-accept');
    var rejectBtn   = document.getElementById('cookie-reject');
    var saveBtn     = document.getElementById('cookie-save');
    var settingsBtn = document.getElementById('cookie-settings');
    var closeBtn    = document.getElementById('cookie-close');

    if (toggleBtn) {
      toggleBtn.addEventListener('click', function () {
        var cats = document.getElementById('cookie-cats');
        var isOpen = cats && cats.classList.contains('open');
        if (isOpen) {
          cats.classList.remove('open');
          toggleBtn.classList.remove('open');
          if (saveBtn) saveBtn.classList.remove('visible');
        } else {
          if (cats) cats.classList.add('open');
          toggleBtn.classList.add('open');
          if (saveBtn) saveBtn.classList.add('visible');
        }
      });
    }

    if (acceptBtn) {
      acceptBtn.addEventListener('click', function () {
        applyCheckboxes(ALL_TRUE);
        savePrefs(ALL_TRUE);
        closeCategories();
        setVisible(false);
      });
    }

    if (rejectBtn) {
      rejectBtn.addEventListener('click', function () {
        var none = {};
        CATS.forEach(function(c) { none[c] = false; });
        applyCheckboxes(none);
        savePrefs(none);
        closeCategories();
        setVisible(false);
      });
    }

    if (saveBtn) {
      saveBtn.addEventListener('click', function () {
        savePrefs(readCheckboxes());
        closeCategories();
        setVisible(false);
      });
    }

    if (settingsBtn) {
      settingsBtn.addEventListener('click', function () {
        var stored = loadPrefs();
        applyCheckboxes(stored || ALL_TRUE);
        closeCategories();
        setVisible(true);
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        if (loadPrefs()) {
          closeCategories();
          setVisible(false);
        }
      });
    }
  });
})();
