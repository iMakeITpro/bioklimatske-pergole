// ---------- mobile navigation (shared by all pages) ----------
// body.nav-open shows the menu and locks page scroll (css/styles.css, <=1024px)
(function(){
  const btn = document.querySelector('.burger');
  const nav = document.querySelector('header nav');
  if(!btn || !nav) return;
  const isOpen = () => document.body.classList.contains('nav-open');
  function setNav(open){
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
