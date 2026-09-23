#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generira po jednu statičku HTML podstranicu (projekti/<slug>.html) za svaki
zapis u alati/projekti.json koji ima popunjen foto_hero/foto_galerija
(alati/dohvati_galerije.py).

Header/nav/footer/mobilna CTA traka i njihov <script> kopirani su iz
sunbreaker-400.html (referentni predložak svih proizvodnih stranica), s
relativnim putanjama prilagođenim za direktorij projekti/ (dodan "../").
Sadržaj stranice (hero fotografija, grid galerije, lightbox) je nov, po
uzoru na live ttgradnja.hr podstranicu projekta.

Pokretanje:
    python3 alati/izradi_projekt_stranice.py

Ponovno pokretanje prepisuje sve fileove u projekti/ - ne uređivati ih ručno.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJEKTI_JSON = os.path.join(ROOT, 'alati', 'projekti.json')
PREDLOZAK = os.path.join(ROOT, 'sunbreaker-400.html')
IZLAZ_DIR = os.path.join(ROOT, 'projekti')

LOKALNI_FILEOVI = [
    'index.html', 'sunbreaker-400.html', 'sunbreaker-500.html', 'sunbreaker-700.html',
    'sjenila.html', 'zip-tende.html', 'rolo.html', 'veranda.html', 'upit.html',
    'jamstveni-uvjeti.html', 'uvjeti-koristenja.html', 'izjava-o-privatnosti.html',
    'kolacici.html', 'css/styles.css',
]


def prefiksiraj_putanje(html_str):
    """Doda '../' ispred referenci na lokalne fileove (href/src), jer stranica
    zivi u projekti/ podmapi."""
    for ime in LOKALNI_FILEOVI:
        html_str = html_str.replace(f'href="{ime}', f'href="../{ime}')
        html_str = html_str.replace(f'src="{ime}', f'src="../{ime}')
    return html_str


TELEFON_IKONICA = (
    '<span class="hd-phone-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="6" y="2" width="12" height="20" rx="2.4" ry="2.4"></rect>'
    '<line x1="12" y1="18" x2="12.01" y2="18"></line></svg></span>'
)


def ucitaj_header_i_footer():
    with open(PREDLOZAK, encoding='utf-8') as f:
        predlozak = f.read()
    m_head = re.search(r'.*?</header>', predlozak, re.S)
    m_foot = re.search(r'<footer>.*\Z', predlozak, re.S)
    if not (m_head and m_foot):
        raise SystemExit('GRESKA: ne mogu pronaci header/footer u sunbreaker-400.html')
    head = prefiksiraj_putanje(m_head.group(0))
    # sunbreaker-400.html (predlozak) nema ikonicu telefona u headeru koju index.html
    # ima - dodajemo je ovdje da podstranice projekta budu vizualno dosljedne indexu.
    head = head.replace(
        '<a href="tel:+385993637777" class="hd-phone">099 363 7777</a>',
        f'<a href="tel:+385993637777" class="hd-phone">{TELEFON_IKONICA}099 363 7777</a>',
    )
    return head, prefiksiraj_putanje(m_foot.group(0))


def izgradi_karticu(full, thumb, model, lokacija):
    aria = f'Povećaj fotografiju: Sunbreaker {model}, {lokacija}'
    return (
        f'      <a class="card" href="{full}" role="button" tabindex="0" aria-label="{aria}">\n'
        f'        <img src="{thumb}" alt="{aria}" loading="lazy">\n'
        f'      </a>'
    )


LIGHTBOX_SKRIPTA = """
<script>
(function(){
  var cards = Array.prototype.slice.call(document.querySelectorAll('#gal .card'));
  var lb = document.getElementById('lightbox');
  if (!cards.length || !lb) return;
  var lbImg = document.getElementById('lbImg');
  var current = 0;

  function open(i){
    current = (i + cards.length) % cards.length;
    var card = cards[current];
    var img = card.querySelector('img');
    lbImg.src = card.getAttribute('href') || img.currentSrc || img.src;
    lbImg.alt = img.alt || '';
    lb.classList.add('open');
    lb.setAttribute('aria-hidden', 'false');
    document.body.classList.add('lightbox-open');
  }
  function close(){
    lb.classList.remove('open');
    lb.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lightbox-open');
  }

  cards.forEach(function(card, i){
    card.addEventListener('click', function(e){ e.preventDefault(); open(i); });
    card.addEventListener('keydown', function(e){
      if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); open(i); }
    });
  });
  document.getElementById('lbClose').addEventListener('click', close);
  document.getElementById('lbPrev').addEventListener('click', function(){ open(current - 1); });
  document.getElementById('lbNext').addEventListener('click', function(){ open(current + 1); });
  lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
  document.addEventListener('keydown', function(e){
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') open(current - 1);
    else if (e.key === 'ArrowRight') open(current + 1);
  });

  // reveal animacija za galeriju (isto kao index.html)
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(x){
      if (x.isIntersecting){ x.target.classList.add('in'); io.unobserve(x.target); }
    });
  }, {threshold: .08, rootMargin: '0px 0px -40px'});
  document.querySelectorAll('.reveal').forEach(function(el, i){
    el.style.transitionDelay = (i % 3 * 70) + 'ms';
    io.observe(el);
  });

  // scroll cue: skip it entirely when the gallery is already on screen, and
  // retire it for good once the gallery scrolls up into view
  var cue = document.querySelector('.scroll-cue');
  var gal = document.getElementById('gal');
  if (cue && gal){
    var cueIo = new IntersectionObserver(function(entries){
      var galleryInView = entries[0].isIntersecting;
      cue.classList.toggle('cue-on', !galleryInView);
      if (galleryInView) cueIo.disconnect();
    }, {threshold: 0, rootMargin: '0px 0px -25% 0px'});
    cueIo.observe(gal);
  }

  // fallback za slike koje se ne uspiju ucitati (isto kao index.html)
  document.querySelectorAll('img').forEach(function(img){
    img.addEventListener('error', function(){
      img.style.background = 'linear-gradient(140deg,#2A2622,#14120F)';
      img.style.minHeight = '100%';
      img.removeAttribute('src');
    });
  });
})();
</script>
"""


def izgradi_stranicu(head, foot, zapis):
    model = zapis['model']
    lokacija = zapis['lokacija']
    naslov_stranice = f'{lokacija} — Sunbreaker {model} | TT Gradnja bioklimatske pergole'
    opis = (f'Bioklimatska pergola Sunbreaker {model}, {lokacija}. '
            f'Pogledajte sve fotografije ovog realiziranog projekta.')

    head = re.sub(r'<title>.*?</title>', f'<title>{naslov_stranice}</title>', head, count=1, flags=re.S)
    head = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{opis}">',
        head, count=1,
    )

    kartice = '\n'.join(
        izgradi_karticu(g['full'], g['thumb'], model, lokacija) for g in zapis['foto_galerija']
    )

    tijelo = f'''
<div class="proj-hero">
  <div class="media">
    <img src="{zapis['foto_hero']}" alt="" loading="lazy">
    <div class="content">
      <a href="../index.html#projekti" class="btn btn-ghost">← Natrag na sve projekte</a>
      <div class="eyebrow">Projekt</div>
      <h1>SUNBREAKER {model} — {lokacija}</h1>
    </div>
  </div>
</div>

<a class="scroll-cue" href="#gal" aria-label="Pomakni se na galeriju fotografija">
  <span class="scroll-cue-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"></path></svg></span>
  <span class="scroll-cue-txt">Povuci</span>
</a>

<section>
  <div class="wrap">
    <div class="grid-g reveal" id="gal">
{kartice}
    </div>
  </div>
</section>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-hidden="true" aria-label="Pregled fotografije">
  <button type="button" class="lightbox-close" id="lbClose" aria-label="Zatvori">&times;</button>
  <button type="button" class="lightbox-nav lightbox-prev" id="lbPrev" aria-label="Prethodna fotografija">&#10094;</button>
  <img class="lightbox-img" id="lbImg" src="" alt="">
  <div class="lightbox-cap-top">SUNBREAKER {model}</div>
  <div class="lightbox-cap">{lokacija}</div>
  <button type="button" class="lightbox-nav lightbox-next" id="lbNext" aria-label="Sljedeća fotografija">&#10095;</button>
</div>
{LIGHTBOX_SKRIPTA}
'''
    return head + '\n' + tijelo + '\n' + foot


def glavno():
    with open(PROJEKTI_JSON, encoding='utf-8') as f:
        zapisi = json.load(f)

    head, foot = ucitaj_header_i_footer()
    os.makedirs(IZLAZ_DIR, exist_ok=True)

    izradjeno = 0
    preskoceno = []
    for z in zapisi:
        if not z.get('foto_hero') or not z.get('foto_galerija'):
            preskoceno.append(z['lokacija'])
            continue
        html_str = izgradi_stranicu(head, foot, z)
        put = os.path.join(IZLAZ_DIR, f"{z['slug']}.html")
        with open(put, 'w', encoding='utf-8') as f:
            f.write(html_str)
        izradjeno += 1

    print(f'Izradjeno stranica: {izradjeno}')
    if preskoceno:
        print(f'Preskoceno (nema foto_hero/foto_galerija): {len(preskoceno)}')
        for p in preskoceno:
            print('  -', p)


if __name__ == '__main__':
    glavno()
