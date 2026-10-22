// ---------- galerija: lightbox ----------
// Shared by index.html and sunbreaker-400/500/700.html. Opening a card shows the photos of
// that card's project only (js/projekti.json: data-galerija -> full-size URLs), not the whole gallery.
// Cards without data-galerija (SB700 reference photos) cycle through the cards of their gallery.
// opts: gal = card selector, box = lightbox element id, p = id prefix of its buttons (p+'Img', 'Cap', 'Close', 'Prev', 'Next').
function lightbox(opts){
  var cards = Array.prototype.slice.call(document.querySelectorAll(opts.gal));
  var lb = document.getElementById(opts.box);
  if (!cards.length || !lb) return;
  var $ = function(s){ return document.getElementById(opts.p + s); };
  var lbImg = $('Img'), lbCap = $('Cap'), prev = $('Prev'), next = $('Next');
  var items = [], current = 0, token = 0;

  // "-1" / "-scaled" variants of the same upload count as one photo
  function norm(u){ return u.replace(/(-scaled)?(-1)?(-scaled)?\.\w+$/, ''); }

  function show(i){
    current = (i + items.length) % items.length;
    lbImg.style.background = ''; lbImg.style.minHeight = '';
    lbImg.src = items[current].src;
    lbImg.alt = items[current].alt;
    lbCap.textContent = items[current].cap;
    prev.hidden = next.hidden = items.length < 2;
  }
  function item(card, src){
    var img = card.querySelector('img');
    var loc = card.querySelector('.card-cap span');
    var model = card.querySelector('.card-cap .model-tag');
    // Full URL comes from the card's href, not img.src (the image error fallback removes img.src).
    return {
      src: src || card.getAttribute('href') || img.currentSrc || img.src,
      alt: img.alt || '',
      cap: (model ? model.textContent + ' \u00b7 ' : '') + (loc ? loc.textContent : '')
    };
  }
  function open(card){
    var main = item(card);
    var mine = ++token;
    var project = card.getAttribute('data-galerija');
    items = project ? [main] : cards.map(function(c){ return item(c); });
    show(project ? 0 : cards.indexOf(card));
    lb.classList.add('open');
    lb.setAttribute('aria-hidden', 'false');
    // lightbox-open on body: locks scroll and hides the sticky header / mobile CTA bar
    // (otherwise their burger/phone icon collides with the lightbox close/nav buttons).
    document.body.classList.add('lightbox-open');
    if (!project) return;

    lightbox.projects().then(function(all){
      var urls = all[project];
      if (!urls || mine !== token) return;
      var at = urls.map(norm).indexOf(norm(main.src));
      items = urls.map(function(u){ return item(card, u); });
      // Cover photo not on the project page: keep it as the first photo.
      if (at < 0){ items.unshift(main); at = 0; }
      show(at);
    });
  }
  function close(){
    token++;
    lb.classList.remove('open');
    lb.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lightbox-open');
  }

  cards.forEach(function(card){
    card.addEventListener('click', function(e){ e.preventDefault(); open(card); });
    card.addEventListener('keydown', function(e){
      if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); open(card); }
    });
  });
  $('Close').addEventListener('click', close);
  prev.addEventListener('click', function(){ show(current - 1); });
  next.addEventListener('click', function(){ show(current + 1); });
  lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
  document.addEventListener('keydown', function(e){
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(current - 1);
    else if (e.key === 'ArrowRight') show(current + 1);
  });

  // swipe: horizontal drag > 50px that is mostly horizontal
  var sx, sy;
  lb.addEventListener('touchstart', function(e){ sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
  lb.addEventListener('touchend', function(e){
    if (sx == null || items.length < 2) return;
    var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
    sx = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) show(current + (dx < 0 ? 1 : -1));
  }, { passive: true });
}
// Fetched once per page, on first open. On failure the lightbox shows just the clicked photo.
lightbox.projects = function(){
  return lightbox._p || (lightbox._p = fetch('js/projekti.json?v=1').then(function(r){ return r.json(); }).catch(function(){ return {}; }));
};
