/* Navigation, contact form and photo viewer. */
(function () {
  'use strict';
  var doc = document;
  function noop() {}
  function list(sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); }
  function block(fn) { try { fn(); } catch (e) { /* Keep independent controls available. */ } }
  /* ---------------------------------------------------------------- nav */
  block(function () {
    var toggle = doc.querySelector('.nav-toggle');
    var nav = doc.querySelector('#nav');
    if (!toggle || !nav) return;

    var mq = window.matchMedia('(max-width: 900px)');
    var label = toggle.querySelector('.label');

    // Never cache the breakpoint. mq.matches is read fresh every time any
    // of these run, so a resize is never the only thing keeping state
    // correct — a toggle click, a link click or Escape all recompute it too.
    function isMobile() { return mq.matches; }
    function isOpen() { return nav.classList.contains('is-open'); }

    // The single place that writes state. inert is derived from the
    // breakpoint and the open flag every time, so desktop can never end up
    // stuck inert (or stuck open) no matter how it got there.
    function render(open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (label) label.textContent = open ? 'Close' : 'Menu';
      if (isMobile() && !open) nav.setAttribute('inert', '');
      else nav.removeAttribute('inert');
    }

    function close(refocus) {
      if (!isOpen()) return;
      render(false);
      if (refocus) toggle.focus();
    }

    // The one invariant this block exists to protect: on desktop the drawer
    // is always closed and never inert. A resize crossing 900px is NOT
    // guaranteed to fire a 'resize' or media-query 'change' event (some
    // programmatic viewport changes skip both), so this is also called
    // defensively at the top of every document-level listener below —
    // whatever the next click, keypress or focus change is, it self-heals
    // the state first instead of trusting a stale is-open/inert combo.
    function correct() {
      if (!isMobile() && isOpen()) { render(false); return true; }
      render(isMobile() && isOpen()); // just resync inert to the current flag
      return false;
    }

    function outside(node) {
      return !(nav.contains(node) || toggle.contains(node));
    }

    correct();
    doc.documentElement.classList.add('js');
    if (mq.addEventListener) mq.addEventListener('change', correct);
    else if (mq.addListener) mq.addListener(correct);
    // Belt and suspenders: a plain resize listener too, since it and the
    // media-query change event can each fire without the other in some
    // browsers and automated/emulated resizes.
    window.addEventListener('resize', correct);

    toggle.addEventListener('click', function () {
      correct();
      // Guard even though the toggle is display:none above 900px: ignore a
      // stray activation on desktop instead of trusting whatever state the
      // drawer happened to be left in.
      render(isMobile() ? !isOpen() : false);
    });

    doc.addEventListener('keydown', function (e) {
      correct();
      if (e.key === 'Escape') close(true);
    });

    // A link in the drawer navigates; the drawer should not stay open behind it.
    nav.addEventListener('click', function (e) {
      correct();
      var a = e.target && e.target.closest ? e.target.closest('a') : null;
      if (a && isMobile()) close(false);
    });

    // Focus leaving the drawer closes it, so tabbing past the last link
    // does not leave an open panel over the page.
    doc.addEventListener('focusin', function (e) {
      if (correct()) return;
      if (isMobile() && isOpen() && outside(e.target)) close(false);
    });

    doc.addEventListener('click', function (e) {
      if (correct()) return;
      if (isMobile() && isOpen() && outside(e.target)) close(false);
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

  /* ------------------------------------------------------ contact form */
  // AJAX to Formspree, with the plain POST as the no-JS fallback.
  block(function () {
    var form = doc.querySelector('form[data-contact]');
    if (!form) return;

    var status = form.querySelector('.form__status');
    var button = form.querySelector('button[type="submit"]');
    var sel = form.querySelector('select[name="service"]');
    var subject = form.querySelector('input[name="_subject"]');

    // Only preselect a topic that is offered by the form.
    var svc = new URLSearchParams(location.search).get('service');
    if (svc && sel) {
      var match = false;
      Array.prototype.forEach.call(sel.options, function (o) { if (o.value === svc) match = true; });
      if (match) sel.value = svc;
    }

    function setStatus(text, isError, isHTML) {
      if (!status) return;
      if (isError) status.setAttribute('role', 'alert');
      else status.removeAttribute('role');
      status.classList.toggle('is-error', !!isError);
      if (isHTML) status.innerHTML = text;
      else status.textContent = text;
    }

    var submitting = false;
    function trackInquiry(event, details) {
      try { if (window.cafeAnalytics) window.cafeAnalytics.track(event, details); }
      catch (error) { /* Measurement must never affect an inquiry. */ }
    }
    form.addEventListener('submit', function (e) {
      if (submitting) { e.preventDefault(); return; }
      if (subject) {
        var nameEl = form.querySelector('[name="name"]');
        var who = (nameEl && nameEl.value && nameEl.value.trim()) || 'a website visitor';
        var what = (sel && sel.value) || 'General';
        subject.value = 'Inquiry: ' + what + ' from ' + who;
      }

      if (!window.fetch || !form.action) return;
      e.preventDefault();
      submitting = true;
      var submitted = new FormData(form);
      var lead = { service: submitted.get('service') };
      setStatus('Sending…', false);
      if (button) button.disabled = true;

      fetch(form.action, {
        method: 'POST',
        body: submitted,
        headers: { 'Accept': 'application/json' }
      })
        .then(function (r) { return r.ok ? r.json() : r.json().then(function (j) { throw j; }); })
        .then(function () {
          trackInquiry('generate_lead', lead);
          // Instant notification to Matt, fire and forget. Formspree already has the record.
          var payload = {};
          submitted.forEach(function (v, k) { payload[k] = v; });
          fetch('/api/notify/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
            keepalive: true
          }).catch(noop);
          form.reset();
          setStatus('Sent. Thank you for your inquiry. Matt will get back to you to discuss the details.', false);
        })
        .catch(function () {
          trackInquiry('inquiry_error');
          setStatus(
            'That did not send. Email chefmattsamuelson@gmail.com or call <a href="tel:+17079726647">(707) 972-6647</a>.',
            true,
            true
          );
        })
        .then(function () { submitting = false; if (button) button.disabled = false; });
    });
  });

  /* ---------------------------------------------------------- gallery */
  block(function () {
    var photos = list('[data-gallery-photo]');
    var viewer = doc.querySelector('.gallery-viewer');
    if (!photos.length || !viewer || !viewer.showModal) return;
    var index = 0;
    var opener;
    function show(next) {
      index = (next + photos.length) % photos.length;
      var original = photos[index].querySelector('img');
      var image = viewer.querySelector('[data-gallery-image]');
      image.src = photos[index].href;
      image.alt = original.alt;
      viewer.querySelector('[data-gallery-caption]').textContent = photos[index].parentNode.querySelector('figcaption').textContent;
      viewer.querySelector('[data-gallery-count]').textContent = (index + 1) + ' / ' + photos.length;
    }
    photos.forEach(function (photo, i) {
      photo.addEventListener('click', function (event) {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        opener = photo;
        show(i);
        viewer.showModal();
        doc.documentElement.classList.add('gallery-open');
        viewer.querySelector('[data-gallery-close]').focus();
      });
    });
    viewer.querySelector('[data-gallery-close]').addEventListener('click', function () { viewer.close(); });
    viewer.querySelector('[data-gallery-prev]').addEventListener('click', function () { show(index - 1); });
    viewer.querySelector('[data-gallery-next]').addEventListener('click', function () { show(index + 1); });
    viewer.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
        event.preventDefault();
        show(index + (event.key === 'ArrowRight' ? 1 : -1));
      }
    });
    viewer.addEventListener('click', function (event) { if (event.target === viewer) viewer.close(); });
    viewer.addEventListener('close', function () {
      doc.documentElement.classList.remove('gallery-open');
      if (opener) opener.focus();
    });
  });

  /* -------------------------------------------------------------- year */
  block(function () {
    var y = doc.querySelector('[data-year]');
    if (y) y.textContent = new Date().getFullYear();
  });
})();
