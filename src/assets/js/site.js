// The Spontaneous Cafe. Small, dependency-free.
// Every feature runs inside its own try/catch. If one throws, the reveal
// fallback still fires so no content is left sitting at opacity 0.
(function () {
  'use strict';

  var doc = document;
  doc.documentElement.classList.add('js');

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  function noop() {}
  function list(sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); }
  function revealAll() {
    try { list('.reveal').forEach(function (el) { el.classList.add('is-in'); }); } catch (e) {}
  }
  function block(fn) {
    try { fn(); } catch (e) { revealAll(); }
  }
  function onWindowLoad(fn) {
    if (doc.readyState === 'complete') { window.setTimeout(fn, 0); return; }
    var done = false;
    window.addEventListener('load', function () { if (done) return; done = true; fn(); });
  }

  var SVG_NS = 'http://www.w3.org/2000/svg';
  function svgEl(tag, attrs) {
    var el = doc.createElementNS(SVG_NS, tag);
    for (var k in attrs) { if (attrs.hasOwnProperty(k)) el.setAttribute(k, attrs[k]); }
    return el;
  }
  // Pause = two bars, play = a triangle. currentColor so it follows the button's text color.
  function heroToggleIcon(kind) {
    var svg = svgEl('svg', { viewBox: '0 0 24 24', width: '18', height: '18', 'aria-hidden': 'true', focusable: 'false' });
    if (kind === 'play') {
      svg.appendChild(svgEl('polygon', { points: '7,4 20,12 7,20', fill: 'currentColor' }));
    } else {
      svg.appendChild(svgEl('rect', { x: '6', y: '5', width: '4', height: '14', fill: 'currentColor' }));
      svg.appendChild(svgEl('rect', { x: '14', y: '5', width: '4', height: '14', fill: 'currentColor' }));
    }
    return svg;
  }

  /* ---------------------------------------------------------------- nav */
  block(function () {
    var toggle = doc.querySelector('.nav-toggle');
    var nav = doc.querySelector('#nav');
    if (!toggle || !nav) return;

    var mq = window.matchMedia('(max-width: 900px)');
    var label = toggle.querySelector('.label');

    function isOpen() { return nav.classList.contains('is-open'); }

    function syncInert() {
      if (mq.matches && !isOpen()) nav.setAttribute('inert', '');
      else nav.removeAttribute('inert');
    }

    function setState(open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (label) label.textContent = open ? 'Close' : 'Menu';
      syncInert();
    }

    function close(refocus) {
      if (!isOpen()) return;
      setState(false);
      if (refocus) toggle.focus();
    }

    function outside(node) {
      return !(nav.contains(node) || toggle.contains(node));
    }

    syncInert();
    if (mq.addEventListener) mq.addEventListener('change', syncInert);
    else if (mq.addListener) mq.addListener(syncInert);

    toggle.addEventListener('click', function () { setState(!isOpen()); });

    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close(true);
    });

    // A link in the drawer navigates; the drawer should not stay open behind it.
    nav.addEventListener('click', function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a') : null;
      if (a && mq.matches) close(false);
    });

    // Focus leaving the drawer closes it, so tabbing past the last link
    // does not leave an open panel over the page.
    doc.addEventListener('focusin', function (e) {
      if (mq.matches && isOpen() && outside(e.target)) close(false);
    });

    doc.addEventListener('click', function (e) {
      if (mq.matches && isOpen() && outside(e.target)) close(false);
    });
  });

  /* ------------------------------------------------------- hero video */
  block(function () {
    var vids = list('video[data-hero]');
    if (!vids.length) return;

    if (reduce.matches) {
      vids.forEach(function (v) {
        v.removeAttribute('autoplay');
        try { v.pause(); } catch (e) {}
      });
      return;
    }

    // No observer, no scroll-driven playback. Leave the video exactly as the
    // markup left it rather than half-managing it.
    if (!('IntersectionObserver' in window)) return;

    vids.forEach(function (v) {
      var hero = v.closest ? v.closest('.hero') : null;
      var userPaused = false;
      var sourcesLoaded = false;
      var visible = false;
      var armed = false;
      var btn = null;
      var iconEl = null;
      var hiddenLabel = null;
      var visibleLabel = null;

      function start() {
        if (userPaused) return;
        if (!sourcesLoaded) {
          sourcesLoaded = true;
          try { v.load(); } catch (e) {}
        }
        var p = v.play();
        if (p && p.catch) p.catch(noop);
      }

      function syncButton() {
        if (!btn) return;
        var text = userPaused ? 'Play video' : 'Pause video';
        btn.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
        if (hiddenLabel) hiddenLabel.textContent = text;
        if (visibleLabel) visibleLabel.textContent = text;
        var nextIcon = heroToggleIcon(userPaused ? 'play' : 'pause');
        if (iconEl) btn.replaceChild(nextIcon, iconEl);
        iconEl = nextIcon;
      }

      if (hero) {
        btn = doc.createElement('button');
        btn.className = 'hero__toggle';
        btn.type = 'button';
        btn.setAttribute('aria-pressed', 'false');

        iconEl = heroToggleIcon('pause');
        // A visible label can stay on wide screens where the chip has room;
        // the CSS hides it once .hero__toggle becomes a 44px icon-only circle.
        visibleLabel = doc.createElement('span');
        visibleLabel.className = 'hero__toggle-label';
        visibleLabel.setAttribute('aria-hidden', 'true');
        visibleLabel.textContent = 'Pause video';
        // The accessible name: always present for assistive tech, never shown visually.
        hiddenLabel = doc.createElement('span');
        hiddenLabel.className = 'visually-hidden';
        hiddenLabel.textContent = 'Pause video';

        btn.appendChild(iconEl);
        btn.appendChild(visibleLabel);
        btn.appendChild(hiddenLabel);

        btn.addEventListener('click', function () {
          if (userPaused) {
            userPaused = false;
            if (visible && armed) start();
          } else {
            userPaused = true;
            try { v.pause(); } catch (e) {}
          }
          syncButton();
        });
        hero.appendChild(btn);
      }

      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          visible = en.isIntersecting;
          if (visible) { if (armed) start(); }
          else { try { v.pause(); } catch (e) {} }
        });
      }, { threshold: 0.1 });
      io.observe(v);

      // Wait for load so the video never competes with the poster, the fonts
      // or the first paint. Works whether or not 'load' has already fired.
      onWindowLoad(function () {
        armed = true;
        if (visible) start();
      });
    });
  });

  /* -------------------------------------------------------- menu tabs */
  // Runs before the reveal observer so panels are hidden before anything
  // animates in and nothing flashes.
  block(function () {
    list('[data-tabs]').forEach(function (root) {
      var tabs = list('[role="tab"]', root);
      var panels = list('[role="tabpanel"]', root);
      if (!tabs.length) return;

      function select(i) {
        tabs.forEach(function (t, j) {
          t.setAttribute('aria-selected', i === j ? 'true' : 'false');
          t.tabIndex = i === j ? 0 : -1;
        });
        panels.forEach(function (p, j) { p.hidden = i !== j; });
      }

      tabs.forEach(function (t, i) {
        t.addEventListener('click', function () { select(i); });
        t.addEventListener('keydown', function (e) {
          var n = null;
          if (e.key === 'ArrowRight') n = i + 1;
          else if (e.key === 'ArrowLeft') n = i - 1;
          else if (e.key === 'Home') n = 0;
          else if (e.key === 'End') n = tabs.length - 1;
          if (n === null) return;
          n = (n + tabs.length) % tabs.length;
          select(n);
          tabs[n].focus();
          e.preventDefault();
        });
      });

      var initial = 0;
      var m = new Date().getMonth();
      var season = m <= 1 || m === 11 ? 'winter' : m <= 4 ? 'spring' : m <= 7 ? 'summer' : 'autumn';
      tabs.forEach(function (t, i) { if (t.dataset && t.dataset.season === season) initial = i; });
      select(initial);
    });
  });

  /* ---------------------------------------------------- reveal on scroll */
  block(function () {
    if (reduce.matches || !('IntersectionObserver' in window)) { revealAll(); return; }
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); ro.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    list('.reveal').forEach(function (el) { ro.observe(el); });
  });

  /* ------------------------------------------------------ contact form */
  // AJAX to Formspree, with the plain POST as the no-JS fallback.
  block(function () {
    var form = doc.querySelector('form[data-contact]');
    if (!form) return;

    var status = form.querySelector('.form__status');
    var button = form.querySelector('button[type="submit"]');
    var sel = form.querySelector('select[name="service"]');
    var tierSel = form.querySelector('select[name="tier"]');
    var subject = form.querySelector('input[name="_subject"]');

    // ?service= and ?tier= only win if the select actually offers that option.
    var svc = new URLSearchParams(location.search).get('service');
    if (svc && sel) {
      var match = false;
      Array.prototype.forEach.call(sel.options, function (o) { if (o.value === svc) match = true; });
      if (match) sel.value = svc;
    }
    var tierParam = new URLSearchParams(location.search).get('tier');
    if (tierParam && tierSel) {
      var tierMatch = false;
      Array.prototype.forEach.call(tierSel.options, function (o) { if (o.value === tierParam) tierMatch = true; });
      if (tierMatch) tierSel.value = tierParam;
    }

    function setStatus(text, isError, isHTML) {
      if (!status) return;
      if (isError) status.setAttribute('role', 'alert');
      else status.removeAttribute('role');
      status.classList.toggle('is-error', !!isError);
      if (isHTML) status.innerHTML = text;
      else status.textContent = text;
    }

    form.addEventListener('submit', function (e) {
      if (subject) {
        var nameEl = form.querySelector('[name="name"]');
        var who = (nameEl && nameEl.value && nameEl.value.trim()) || 'a website visitor';
        var what = (sel && sel.value) || 'General';
        var tierVal = (tierSel && tierSel.value) || '';
        subject.value = tierVal
          ? 'Inquiry: ' + what + ', ' + tierVal + ' from ' + who
          : 'Inquiry: ' + what + ' from ' + who;
      }

      if (!window.fetch || !form.action) return;
      e.preventDefault();
      setStatus('Sending…', false);
      if (button) button.disabled = true;

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      })
        .then(function (r) { return r.ok ? r.json() : r.json().then(function (j) { throw j; }); })
        .then(function () {
          // Instant notification to Matt, fire and forget. Formspree already has the record.
          var payload = {};
          new FormData(form).forEach(function (v, k) { payload[k] = v; });
          fetch('/api/notify/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
            keepalive: true
          }).catch(noop);
          form.reset();
          setStatus('Sent. Matt will get back to you within a day or two.', false);
        })
        .catch(function () {
          setStatus(
            'That did not send. Email chefmattsamuelson@gmail.com or call <a href="tel:+17079726647">(707) 972-6647</a>.',
            true,
            true
          );
        })
        .then(function () { if (button) button.disabled = false; });
    });
  });

  /* -------------------------------------------------------------- year */
  block(function () {
    var y = doc.querySelector('[data-year]');
    if (y) y.textContent = new Date().getFullYear();
  });
})();
