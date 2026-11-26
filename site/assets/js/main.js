(function () {
  'use strict';

  var root = document.documentElement;
  var reduce = root.classList.contains('reduce-motion'); /* set in the page head */
  var hasGsap = !!window.gsap;
  var lenis = null;

  /* Smooth scroll. With reduced motion Lenis keeps native scrolling. */
  if (window.Lenis) {
    lenis = new Lenis({ autoRaf: !hasGsap, anchors: true, respectReducedMotion: reduce });
    if (hasGsap) {
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    }
  }

  /* Header hairline once the page scrolls */
  var header = document.querySelector('.site-header');
  var scrolled = null;
  function onScroll(y) {
    var next = y > 8;
    if (next !== scrolled) { scrolled = next; header.classList.toggle('is-scrolled', next); }
  }
  if (lenis) lenis.on('scroll', function (e) { onScroll(e.scroll); });
  else window.addEventListener('scroll', function () { onScroll(window.scrollY); }, { passive: true });
  onScroll(window.scrollY);

  /* Mobile menu */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    root.classList.toggle('menu-open', open);
    if (lenis) { open ? lenis.stop() : lenis.start(); }
  }
  toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); toggle.focus(); }
  });
  window.matchMedia('(min-width: 901px)').addEventListener('change', function (mq) { if (mq.matches) setMenu(false); });

  /* Contact form */
  var form = document.getElementById('contact-form');
  if (form) initForm(form);

  function initForm(form) {
    var d = form.dataset;
    var status = form.querySelector('.form__status');
    var button = form.querySelector('button[type="submit"]');
    var select = document.getElementById('f-type');

    /* "Choose this" on the services page arrives as ?package=2 */
    var pkg = new URLSearchParams(location.search).get('package');
    if (pkg && select.querySelector('option[value="' + pkg + '"]')) select.value = pkg;

    function errorFor(input) {
      if (input.validity.valueMissing) return d.errReq;
      if (input.validity.typeMismatch) return d.errEmail;
      return '';
    }
    function check(input) {
      var field = input.closest('.field');
      var msg = errorFor(input);
      var el = field.querySelector('.field__error');
      field.classList.toggle('is-invalid', !!msg);
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (msg) {
        if (!el) {
          el = document.createElement('p');
          el.className = 'field__error';
          el.id = input.id + '-error';
          field.appendChild(el);
        }
        el.textContent = msg;
        input.setAttribute('aria-describedby', (input.id === 'f-msg' ? 'f-msg-hint ' : '') + el.id);
      } else if (el) {
        el.remove();
        if (input.id === 'f-msg') input.setAttribute('aria-describedby', 'f-msg-hint');
        else input.removeAttribute('aria-describedby');
      }
      return !msg;
    }
    var inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    inputs.forEach(function (input) {
      input.addEventListener('blur', function () { if (input.value) check(input); });
      input.addEventListener('input', function () { if (input.closest('.field').classList.contains('is-invalid')) check(input); });
    });

    function setStatus(text, kind) {
      status.textContent = text;
      status.classList.toggle('is-done', kind === 'done');
      status.classList.toggle('is-error', kind === 'error');
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      inputs.forEach(function (input) { if (!check(input) && !firstBad) firstBad = input; });
      if (firstBad) { setStatus(d.errCheck, 'error'); firstBad.focus(); return; }

      /* Web3Forms delivers the message to Julius's email */
      var data = Object.fromEntries(new FormData(form));
      if (data.botcheck) return; /* filled by a bot */
      var choice = select.options[select.selectedIndex];
      data.project = choice ? choice.text : data.project;
      button.disabled = true;
      setStatus(d.sending, '');
      fetch(form.action, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      })
        .then(function (res) { return res.json().then(function (json) { return { ok: res.ok, json: json }; }); })
        .then(function (r) {
          if (!r.ok || !r.json.success) throw new Error(r.json.message || 'failed');
          setStatus(d.sent, 'done');
          form.reset();
        })
        .catch(function () { setStatus(d.fail, 'error'); })
        .then(function () { button.disabled = false; });
    });
  }

  /* One orchestrated moment: the home hero on load */
  var hero = document.querySelector('.hero');
  if (!hasGsap || reduce || !hero) { root.classList.remove('intro'); return; }
  if (root.classList.contains('intro')) {
    gsap.timeline({ defaults: { ease: 'power3.out' }, onComplete: function () { root.classList.remove('intro'); } })
      .fromTo('.hero__title .line > span', { y: 0, yPercent: 105 }, { yPercent: 0, duration: 1, stagger: 0.12 }, 0.1)
      .fromTo(['.hero__lead', '.hero__actions'], { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.7, stagger: 0.08 }, 0.55)
      .fromTo('.hero__panel', { opacity: 0, x: 40 }, { opacity: 1, x: 0, duration: 1.1 }, 0.35);
  }
})();
