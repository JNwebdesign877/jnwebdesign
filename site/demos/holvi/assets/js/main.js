(function () {
  'use strict';

  var root = document.documentElement;
  var reduce = root.classList.contains('reduce-motion'); /* set in the page head */
  var hasGsap = !!(window.gsap && window.ScrollTrigger);
  var lenis = null;

  /* Opening hours, Helsinki time. Day 0 is Sunday. [open, close, kitchen closes] in hours. */
  var HOURS = { 2: [17, 23, 22], 3: [17, 23, 22], 4: [17, 23, 22], 5: [17, 24, 23], 6: [17, 24, 23] };
  var DAY_NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  function helsinkiNow() {
    var parts = new Intl.DateTimeFormat('en-GB', {
      timeZone: 'Europe/Helsinki', weekday: 'short', hour: 'numeric', minute: 'numeric', hourCycle: 'h23'
    }).formatToParts(new Date());
    var get = function (t) { return (parts.find(function (p) { return p.type === t; }) || {}).value; };
    var day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(get('weekday'));
    return { day: day, time: Number(get('hour')) + Number(get('minute')) / 60 };
  }
  function fmt(h) { return (h === 24 ? '00' : String(h).padStart(2, '0')) + '.00'; }

  /* "Tonight" line on the home page */
  var tonight = document.querySelector('[data-tonight]');
  if (tonight) {
    var now = helsinkiNow();
    var today = HOURS[now.day];
    var text = tonight.querySelector('[data-tonight-text]');
    var state = 'closed', msg;
    if (today && now.time < today[2]) {
      state = 'open';
      msg = now.time < today[0]
        ? '<strong>Open tonight</strong> ' + fmt(today[0]) + ' to ' + fmt(today[1]) + '. Kitchen until ' + fmt(today[2]) + '.'
        : '<strong>Open now</strong> until ' + fmt(today[1]) + '. Last orders ' + fmt(today[2]) + '.';
    } else {
      for (var i = 1; i <= 7; i++) {
        var d = (now.day + i) % 7;
        if (HOURS[d]) {
          msg = '<strong>Closed tonight.</strong> Next open ' + (i === 1 ? 'tomorrow' : DAY_NAMES[d]) + ' from ' + fmt(HOURS[d][0]) + '.';
          break;
        }
      }
    }
    tonight.setAttribute('data-state', state);
    text.innerHTML = msg;
  }

  /* Hours table: mark today */
  var hoursTable = document.querySelector('[data-hours]');
  if (hoursTable) {
    var row = hoursTable.querySelector('[data-day="' + helsinkiNow().day + '"]');
    if (row) row.classList.add('is-today');
  }

  /* Smooth scroll, driven by GSAP's ticker so ScrollTrigger stays in sync */
  if (hasGsap) gsap.registerPlugin(ScrollTrigger);
  if (window.Lenis && !reduce) {
    lenis = new Lenis({ autoRaf: !hasGsap, anchors: { offset: -80 }, lerp: 0.12 });
    if (hasGsap) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    }
  }

  /* Header hairline once the page moves */
  var header = document.querySelector('.site-header');
  function onScroll(y) { header.classList.toggle('is-scrolled', y > 8); }
  if (lenis) lenis.on('scroll', function (e) { onScroll(e.scroll); });
  else window.addEventListener('scroll', function () { onScroll(window.scrollY); }, { passive: true });
  onScroll(window.scrollY);

  /* Mobile menu */
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    root.classList.toggle('menu-open', open);
    if (lenis) { if (open) lenis.stop(); else lenis.start(); }
  }
  toggle.addEventListener('click', function () { setMenu(toggle.getAttribute('aria-expanded') !== 'true'); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); toggle.focus(); }
  });
  window.matchMedia('(min-width: 861px)').addEventListener('change', function (mq) { if (mq.matches) setMenu(false); });

  /* Menu: filter by how the dish meets the fire */
  var filter = document.querySelector('[data-fire-filter]');
  if (filter) {
    var buttons = filter.querySelectorAll('button');
    var dishes = document.querySelectorAll('.dish');
    var status = document.querySelector('[data-filter-status]');
    filter.addEventListener('click', function (e) {
      var btn = e.target.closest('button');
      if (!btn) return;
      var fire = btn.getAttribute('data-fire');
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      var shown = 0;
      dishes.forEach(function (d) {
        var match = fire === 'all' || d.getAttribute('data-fire') === fire;
        d.hidden = !match;
        if (match) shown++;
      });
      document.querySelectorAll('.course').forEach(function (c) {
        var any = c.querySelector('.dish:not([hidden])');
        var empty = c.querySelector('.menu-empty');
        empty.hidden = !!any;
      });
      status.textContent = fire === 'all' ? 'Showing the whole menu.' : 'Showing ' + shown + ' dishes cooked ' + btn.textContent.toLowerCase() + '.';
      if (hasGsap && !reduce) {
        gsap.fromTo('.dish:not([hidden])', { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.45, stagger: 0.03, ease: 'expo.out' });
      }
      if (lenis) lenis.resize();
      if (hasGsap) ScrollTrigger.refresh();
    });
  }

  /* Booking form (visit.html) */
  var form = document.getElementById('book-form');
  if (form) initForm(form);

  function initForm(form) {
    var date = form.elements.date;
    var t = new Date();
    var todayIso = t.getFullYear() + '-' + String(t.getMonth() + 1).padStart(2, '0') + '-' + String(t.getDate()).padStart(2, '0');
    date.min = todayIso;

    function setError(field, message) {
      var err = document.getElementById(field.id + '-error');
      field.setAttribute('aria-invalid', message ? 'true' : 'false');
      if (err) err.textContent = message || '';
    }

    function check(field) {
      var v = field.value.trim();
      if (field.name === 'date') {
        if (!v) return 'Choose a date.';
        var d = new Date(v + 'T12:00:00');
        var day = d.getDay();
        if (!HOURS[day]) return 'We are closed on ' + DAY_NAMES[day] + 's. Pick Tuesday to Saturday.';
        if (v < todayIso) return 'That date has passed. Pick today or later.';
      }
      if (field.name === 'time' && !v) return 'Choose a time.';
      if (field.name === 'guests' && !v) return 'Choose how many of you are coming.';
      if (field.name === 'name' && !v) return 'Add the name the table is under.';
      if (field.name === 'email') {
        if (!v) return 'Add an email so we can confirm.';
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return 'That email looks incomplete, for example name@example.com.';
      }
      return '';
    }

    form.addEventListener('blur', function (e) {
      if (e.target.name && e.target.hasAttribute('required')) setError(e.target, check(e.target));
    }, true);

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var first = null;
      Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (f) {
        var msg = check(f);
        setError(f, msg);
        if (msg && !first) first = f;
      });
      if (first) { first.focus(); return; }
      var done = document.getElementById('book-done');
      var d = new Date(date.value + 'T12:00:00');
      done.querySelector('[data-summary]').textContent =
        form.elements.guests.value + ' at ' + form.elements.time.value + ' on ' +
        d.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' }) + ', under ' + form.elements.name.value.trim() + '.';
      form.hidden = true;
      done.hidden = false;
      done.focus();
    });
  }

  /* Motion. One authored moment: the vault opens. Everything else stays still. */
  if (!hasGsap || reduce) { root.classList.remove('intro'); return; }

  var heroArch = document.querySelector('.hero__arch');
  if (heroArch && root.classList.contains('intro')) {
    /* Explicit start values (x/y 0) so GSAP never inherits the CSS pre-hide transform as a pixel offset,
       and inline styles are cleared at the end so the CSS state is the source of truth again. */
    var introTargets = ['.hero__line > span', '.hero__lead', '.hero__actions', '.tonight', heroArch, heroArch.querySelector('img')];
    var tl = gsap.timeline({
      defaults: { ease: 'expo.out' },
      onComplete: function () { root.classList.remove('intro'); gsap.set(introTargets, { clearProps: 'all' }); }
    });
    tl.fromTo(heroArch, { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.6 })
      .fromTo(heroArch.querySelector('img'), { scale: 1.18 }, { scale: 1, duration: 2.2 }, 0)
      .fromTo('.hero__line > span', { x: 0, y: 0, yPercent: 105 }, { x: 0, y: 0, yPercent: 0, duration: 1.2, stagger: 0.08 }, 0.35)
      .fromTo(['.hero__lead', '.hero__actions', '.tonight'], { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 1, stagger: 0.08 }, 0.8);
  } else {
    root.classList.remove('intro');
  }

  /* Plates rise out of their arches as you reach them */
  gsap.utils.toArray('.plate .arch').forEach(function (arch) {
    gsap.fromTo(arch, { clipPath: 'inset(35% 0% 0% 0%)' }, {
      clipPath: 'inset(0% 0% 0% 0%)', ease: 'none',
      scrollTrigger: { trigger: arch, start: 'top 95%', end: 'top 55%', scrub: true }
    });
  });

  /* Slow drift on wide photos */
  gsap.utils.toArray('.wide-photo img, .vault .arch img').forEach(function (img) {
    gsap.fromTo(img, { yPercent: -6 }, {
      yPercent: 0, ease: 'none',
      scrollTrigger: { trigger: img.parentNode, start: 'top bottom', end: 'bottom top', scrub: true }
    });
  });
})();
