/* Direct GA4. No Google requests until analytics consent is granted. */
(function () {
  'use strict';
  var config = document.currentScript.dataset;
  var win = window;
  var doc = document;
  var choice = 'denied';
  var loaded = false;
  var key = 'cafe-analytics-consent-v1';
  var lifetime = 180 * 24 * 60 * 60 * 1000;
  var services = {
    'Foraging excursion': 'foraging', 'Private chef': 'private_chef',
    'Catering and events': 'catering', 'Cooking class': 'cooking_class',
    'Forest bathing or farm tour': 'nature_tour',
    'Interactive dinner party': 'dinner_party', 'Something else': 'other'
  };
  var tiers = { '3 hours': '3_hours', '6 hours': '6_hours', '12 hours': '12_hours', 'Larger event': 'larger_event' };
  var allowed = ['generate_lead', 'phone_click', 'email_click', 'inquiry_error'];
  // Only known static paths enter Analytics, including when the visitor reaches a 404.
  var paths = ['/', '/about/', '/foraging/', '/private-chef/', '/catering/', '/cooking-classes/', '/contact/', '/privacy/'];
  var page = paths.indexOf(win.location.pathname) >= 0 ? win.location.pathname : '/404/';
  var enabled = /^G-[A-Z0-9]+$/.test(config.ga4Id || '') &&
    win.location.hostname === config.analyticsHost && win.location.protocol === 'https:';

  win.cafeAnalytics = { track: function (event, details) {
    if (!enabled || !loaded || choice !== 'granted' || allowed.indexOf(event) < 0) return;
    details = details || {};
    var data = pageDetails();
    data.send_to = config.ga4Id;
    if (event === 'generate_lead') {
      data.lead_service = services[details.service] || 'unspecified';
      data.lead_tier = tiers[details.tier] || 'unspecified';
    }
    if (event === 'inquiry_error') data.error_category = 'submission_failed';
    command('event', event, data);
  } };
  if (!enabled) return;

  var notice = doc.querySelector('[data-cookie-notice]');
  var settings = doc.querySelector('[data-privacy-settings]');

  function command() { win.dataLayer.push(arguments); }
  function pageDetails() {
    var referrer = '';
    try { referrer = new URL(doc.referrer).origin; } catch (e) { /* Direct visit. */ }
    return { page_location: win.location.origin + page, page_referrer: referrer,
      page_title: doc.title, page_path: page };
  }
  function readChoice() {
    try {
      var saved = JSON.parse(win.localStorage.getItem(key));
      if (saved && saved.at <= Date.now() && Date.now() - saved.at < lifetime &&
          (saved.choice === 'granted' || saved.choice === 'denied')) return saved.choice;
    } catch (e) { /* Storage is optional; unavailable means no remembered consent. */ }
    return null;
  }

  function start() {
    if (loaded || choice !== 'granted') return;
    loaded = true;
    win['ga-disable-' + config.ga4Id] = false;
    win.dataLayer = win.dataLayer || [];
    command('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied' });
    command('set', 'ads_data_redaction', true);
    command('set', 'url_passthrough', false);
    command('consent', 'update', { analytics_storage: 'granted', ad_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied' });
    command('js', new Date());
    var options = pageDetails();
    options.allow_google_signals = false;
    options.allow_ad_personalization_signals = false;
    options.send_page_view = true;
    command('config', config.ga4Id, options);
    var script = doc.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + config.ga4Id;
    doc.head.appendChild(script);
  }

  function clearAnalyticsCookies() {
    doc.cookie.split(';').forEach(function (entry) {
      var name = entry.split('=')[0].trim();
      if (!/^_ga(?:_|$)/.test(name) && name !== '_gid' && !/^_gat/.test(name)) return;
      var expiry = name + '=; Max-Age=0; path=/; SameSite=Lax';
      doc.cookie = expiry;
      doc.cookie = expiry + '; domain=' + config.analyticsHost;
      doc.cookie = expiry + '; domain=.' + config.analyticsHost;
    });
  }

  function apply(next, persist) {
    var wasLoaded = loaded;
    choice = next;
    if (persist) {
      try { win.localStorage.setItem(key, JSON.stringify({ choice: choice, at: Date.now() })); }
      catch (e) { /* The choice still applies to this page. */ }
    }
    notice.hidden = true;
    if (choice === 'granted') start();
    else {
      win['ga-disable-' + config.ga4Id] = true;
      clearAnalyticsCookies();
      // Unload the Google tag too, so it cannot continue processing automatic events.
      if (wasLoaded) win.location.reload();
    }
  }

  settings.hidden = false;
  settings.addEventListener('click', function () {
    notice.hidden = false;
    doc.querySelector('[data-consent="granted"]').focus();
  });
  doc.querySelectorAll('[data-consent]').forEach(function (button) {
    button.addEventListener('click', function () {
      apply(button.getAttribute('data-consent'), true);
      settings.focus();
    });
  });
  win.addEventListener('storage', function (event) {
    if (event.key === key || event.key === null) apply(readChoice() || 'denied', false);
  });
  doc.addEventListener('click', function (event) {
    var link = event.target.closest && event.target.closest('a[href]');
    if (!link) return;
    var href = link.getAttribute('href') || '';
    if (href.indexOf('tel:') === 0) win.cafeAnalytics.track('phone_click');
    if (href.indexOf('mailto:') === 0) win.cafeAnalytics.track('email_click');
  });
  var saved = readChoice();
  if (saved) apply(saved, false);
  else notice.hidden = false;
})();
