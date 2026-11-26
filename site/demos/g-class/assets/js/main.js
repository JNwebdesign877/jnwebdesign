(function () {
  'use strict';

  var root = document.documentElement;
  var hasGsap = !!(window.gsap && window.ScrollTrigger);
  var reduce = root.classList.contains('reduce-motion'); /* set in the page head */
  var lenis = null;

  /* Smooth scroll: Lenis, driven by GSAP's ticker so ScrollTrigger stays in sync.
     With reduced motion Lenis stops smoothing on its own (respectReducedMotion). */
  if (hasGsap) gsap.registerPlugin(ScrollTrigger);

  if (window.Lenis) {
    lenis = new Lenis({ autoRaf: !hasGsap, anchors: true, respectReducedMotion: reduce });
    if (hasGsap) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    }
  }

  /* Header: solid on inner pages, and on the home page once you scroll */
  var header = document.querySelector('.site-header');
  var alwaysSolid = document.body.classList.contains('is-inner');
  var solid = null;
  function setHeader(y) {
    var next = alwaysSolid || y > 24;
    if (next !== solid) { solid = next; header.classList.toggle('is-solid', next); }
  }
  if (lenis) lenis.on('scroll', function (e) { setHeader(e.scroll); });
  else window.addEventListener('scroll', function () { setHeader(window.scrollY); }, { passive: true });
  setHeader(window.scrollY);

  /* Mobile menu */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    root.classList.toggle('menu-open', open);
    if (lenis) { open ? lenis.stop() : lenis.start(); }
  }
  toggle.addEventListener('click', function () {
    setMenu(toggle.getAttribute('aria-expanded') !== 'true');
  });
  nav.addEventListener('click', function (e) {
    if (e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); toggle.focus(); }
  });
  window.matchMedia('(min-width: 861px)').addEventListener('change', function (mq) {
    if (mq.matches) setMenu(false);
  });

  /* Booking form (test-drive.html only) */
  var form = document.getElementById('booking-form');
  if (form) initForm(form);

  function initForm(form) {
  /* "Test drive the G 550" on the models page arrives as ?model=G%20550 */
  var modelSelect = document.getElementById('f-model');
  var wanted = new URLSearchParams(location.search).get('model');
  if (wanted) modelSelect.value = wanted;

  /* Validates, then says plainly that nothing is sent */
  var status = form.querySelector('.form__status');
  var dateInput = document.getElementById('f-date');
  dateInput.min = new Date(Date.now() + 864e5).toISOString().slice(0, 10);

  function fieldError(input) {
    if (input.validity.valueMissing) return 'Fill in this field.';
    if (input.validity.typeMismatch) return 'Enter an email address like name@example.com.';
    if (input.validity.patternMismatch) return 'Enter a 5-digit ZIP code.';
    if (input.validity.rangeUnderflow) return 'Pick a date from tomorrow onward.';
    return '';
  }
  function showError(input) {
    var field = input.closest('.field');
    var msg = fieldError(input);
    var el = field.querySelector('.field__error');
    field.classList.toggle('is-invalid', !!msg);
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (msg) {
      if (!el) {
        el = document.createElement('p');
        el.className = 'field__error';
        el.id = input.id + '-error';
        field.appendChild(el);
        input.setAttribute('aria-describedby', el.id);
      }
      el.textContent = msg;
    } else if (el) {
      el.remove();
      input.removeAttribute('aria-describedby');
    }
    return !msg;
  }
  form.querySelectorAll('input, select').forEach(function (input) {
    input.addEventListener('blur', function () { if (input.value) showError(input); });
    input.addEventListener('input', function () {
      if (input.closest('.field').classList.contains('is-invalid')) showError(input);
    });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var firstBad = null;
    form.querySelectorAll('input[required], select[required]').forEach(function (input) {
      if (!showError(input) && !firstBad) firstBad = input;
    });
    if (firstBad) {
      status.classList.remove('is-done');
      status.textContent = 'Check the highlighted fields.';
      firstBad.focus();
      return;
    }
    var name = document.getElementById('f-first').value.trim();
    status.classList.add('is-done');
    status.textContent = 'Thanks, ' + name + '. This site is a design concept, so your request was not sent anywhere.';
    form.reset();
  });
  }

  var isHome = !!document.querySelector('.hero');
  var gturn = document.querySelector('.gturn');
  if (!hasGsap || reduce || !isHome) root.classList.remove('intro');
  if (!hasGsap || reduce) return;

  (function () {
    /* 1. Page-load sequence for the hero (home page) */
    if (isHome && root.classList.contains('intro')) {
      gsap.timeline({ defaults: { ease: 'power3.out' }, onComplete: function () { root.classList.remove('intro'); } })
        .fromTo('.hero__media img', { scale: 1.06 }, { scale: 1, duration: 2.4, ease: 'power2.out' }, 0)
        .fromTo('.hero__line > span', { y: 0, yPercent: 105 }, { yPercent: 0, duration: 1.1, stagger: 0.12 }, 0.2)
        .fromTo(['.hero__sub', '.hero__actions'], { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.8, stagger: 0.1 }, 0.85);
    }

    /* 2. G-TURN page: scroll spins the car two full turns, like the real feature */
    if (!gturn) return;
    var readout = document.querySelector('[data-gturn-deg]');
    var last = -1;
    gsap.fromTo('#gturn-car', { rotation: 0 }, {
      rotation: 720,
      ease: 'none',
      svgOrigin: '200 200',
      scrollTrigger: {
        trigger: '.gturn',
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.6
      },
      onUpdate: function () {
        var deg = Math.round(gsap.getProperty('#gturn-car', 'rotation'));
        if (deg !== last) { last = deg; readout.textContent = deg; }
      }
    });
  })();

  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
