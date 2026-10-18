// ---------- mobile navigation (shared by all pages) ----------
// body.nav-open shows the menu and locks page scroll (css/styles.css, <=1024px)
(function(){
  const btn = document.querySelector('.burger');
  const nav = document.querySelector('header nav');
  if(!btn || !nav) return;
  const isOpen = () => document.body.classList.contains('nav-open');
  // <=1024px: "Modeli" / "Sjenila za sunce" titles toggle their submenu instead of navigating
  const mobile = window.matchMedia('(max-width: 1024px)');
  const subTitles = nav.querySelectorAll(':scope > ul > .has-sub > a');
  function setSub(a, open){
    a.parentElement.classList.toggle('sub-open', open);
    a.setAttribute('aria-expanded', open);
  }
  function resetSubs(){
    subTitles.forEach(a => mobile.matches ? setSub(a, false) : (a.parentElement.classList.remove('sub-open'), a.removeAttribute('aria-expanded')));
  }
  resetSubs();
  mobile.addEventListener('change', resetSubs);
  // registered before the close-on-link handler below, so stopImmediatePropagation keeps the menu open
  subTitles.forEach(a => a.addEventListener('click', e => {
    if(!mobile.matches) return;
    e.preventDefault();
    e.stopImmediatePropagation();
    setSub(a, !a.parentElement.classList.contains('sub-open'));
  }));
  function setNav(open){
    if(open) resetSubs();
    document.body.classList.toggle('nav-open', open);
    btn.setAttribute('aria-expanded', open);
    btn.setAttribute('aria-label', open ? 'Zatvori izbornik' : 'Otvori izbornik');
    btn.textContent = open ? '✕' : '☰';
  }
  btn.addEventListener('click', () => setNav(!isOpen()));
  nav.querySelectorAll('a[href]').forEach(a => a.addEventListener('click', () => setNav(false)));
  // tap outside only closes the menu, it does not activate what is underneath
  document.addEventListener('click', e => {
    if(isOpen() && !nav.contains(e.target) && !btn.contains(e.target)){
      e.preventDefault();
      e.stopPropagation();
      setNav(false);
    }
  }, true);
  document.addEventListener('keydown', e => {
    if(e.key === 'Escape' && isOpen()){
      setNav(false);
      btn.focus();
    }
  });
})();
