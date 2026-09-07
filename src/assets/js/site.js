// The Spontaneous Cafe. Small, dependency-free.
(function () {
  document.documentElement.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('#nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.querySelector('.label').textContent = open ? 'Close' : 'Menu';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) toggle.click();
    });
  }

  // Hero video: respect reduced motion, pause when off screen, never block paint.
  document.querySelectorAll('video[data-hero]').forEach(function (v) {
    if (reduce.matches) { v.removeAttribute('autoplay'); v.pause(); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { en.isIntersecting ? v.play().catch(function () {}) : v.pause(); });
    }, { threshold: 0.1 });
    io.observe(v);
  });

  // Reveal on scroll
  if (!reduce.matches && 'IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); ro.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { ro.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  // Menu season tabs
  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var tabs = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('[role="tabpanel"]');
    function select(i) {
      tabs.forEach(function (t, j) { t.setAttribute('aria-selected', i === j ? 'true' : 'false'); t.tabIndex = i === j ? 0 : -1; });
      panels.forEach(function (p, j) { p.hidden = i !== j; });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
        if (n === null) return; n = (n + tabs.length) % tabs.length; select(n); tabs[n].focus(); e.preventDefault();
      });
    });
    var initial = 0;
    var m = new Date().getMonth();
    var season = m <= 1 || m === 11 ? 'winter' : m <= 4 ? 'spring' : m <= 7 ? 'summer' : 'autumn';
    tabs.forEach(function (t, i) { if (t.dataset.season === season) initial = i; });
    select(initial);
  });

  // Contact form: AJAX to Formspree with the plain POST as the no-JS fallback.
  var form = document.querySelector('form[data-contact]');
  if (form) {
    var status = form.querySelector('.form__status');
    var button = form.querySelector('button[type="submit"]');
    var params = new URLSearchParams(location.search);
    var svc = params.get('service');
    var sel = form.querySelector('select[name="service"]');
    if (svc && sel) { sel.value = svc; }
    form.addEventListener('submit', function (e) {
      if (!window.fetch || !form.action) return;
      e.preventDefault();
      if (status) status.textContent = 'Sending\u2026';
      button.disabled = true;
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) { return r.ok ? r.json() : r.json().then(function (j) { throw j; }); })
        .then(function () {
          form.reset();
          if (status) status.textContent = 'Sent. I will get back to you within a day or two.';
        })
        .catch(function (err) {
          var msg = (err && err.errors && err.errors.map(function (x) { return x.message; }).join(', ')) || '';
          if (status) status.textContent = 'That did not send. ' + (msg || 'Email me directly at chefmattsamuelson@gmail.com.');
        })
        .then(function () { button.disabled = false; });
    });
  }

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
