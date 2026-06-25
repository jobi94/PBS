(function () {
  var KEY = 'spbs_consent';

  function updateGtag(granted) {
    var val = granted ? 'granted' : 'denied';
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: val,
        ad_storage: val,
        ad_user_data: val,
        ad_personalization: val,
        functionality_storage: val,
        personalization_storage: val
      });
    }
  }

  function saveChoice(granted) {
    try { localStorage.setItem(KEY, granted ? 'granted' : 'denied'); } catch (e) {}
    updateGtag(granted);
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

  document.addEventListener('DOMContentLoaded', function () {
    var stored;
    try { stored = localStorage.getItem(KEY); } catch (e) {}

    if (!stored) {
      setVisible(true);
    }

    var acceptBtn  = document.getElementById('cookie-accept');
    var rejectBtn  = document.getElementById('cookie-reject');
    var settingsBtn = document.getElementById('cookie-settings');

    if (acceptBtn) {
      acceptBtn.addEventListener('click', function () {
        saveChoice(true);
        setVisible(false);
      });
    }

    if (rejectBtn) {
      rejectBtn.addEventListener('click', function () {
        saveChoice(false);
        setVisible(false);
      });
    }

    if (settingsBtn) {
      settingsBtn.addEventListener('click', function () {
        setVisible(true);
      });
    }
  });
})();
