#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dopuni i posloži galeriju "Projekti" (#gal u index.html) prema live stranici
https://www.ttgradnja.hr/reference/ i redoslijedu iz "Pergole - referenca.docx".

Sto radi:
  1. Dohvaca https://www.ttgradnja.hr/reference/ i parsira svih 67
     bioklimatska-pergola <article> blokova (naslov, naslovna fotografija,
     URL podstranice). Stolarija/PVC/grilje reference se preskacu (nemaju
     "pergola" u naslovu).
  2. Cita "Pergole - referenca.docx" iz korijena repozitorija - tablica ima
     dva stupca (lijeva/desna strana live stranice). Konacan redoslijed je
     strogo naizmjenican: lijevi-1, desni-1, lijevi-2, desni-2, ...
  3. Cita postojecih 40 kartica iz index.html (#gal) - kartice koje se
     poklapaju (po nazivu slike) s nekim od 67 iz koraka 1+2 zadrzavaju
     TOCNO postojeci HTML (href/model/lokacija se ne diraju). Kartice koje
     ne postoje kod nas dodaju se novo, hotlink na ttgradnja.hr, model
     zadano SUNBREAKER 400 (500 samo za Gacku i Petrcane - potvrdjeno s
     klijentom). Kartica koja postoji kod nas ali NIJE u popisu od 67
     (trenutno: Peljesac/IMG-6447.jpg, stara zamijenjena fotografija) ispada.
  4. Preslaže #gal blok u index.html tocnim redoslijedom i sprema
     alati/projekti.json (izvor istine za buducu Fazu 2 - pune galerije po
     projektu).

Pokretanje:
    python3 alati/dohvati_projekte.py            # izradi promjene
    python3 alati/dohvati_projekte.py --provjeri # samo ispisi plan, ne diraj index.html

Skripta se moze ponovno pokrenuti kad se popis/redoslijed promijeni -
#gal blok u index.html se NE uredjuje rucno.
"""
import html
import json
import os
import re
import sys
import urllib.request
import zipfile
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_HTML = os.path.join(ROOT, 'index.html')
DOCX = os.path.join(ROOT, 'Pergole - referenca.docx')
OUT_JSON = os.path.join(ROOT, 'alati', 'projekti.json')
REFERENCE_URL = 'https://www.ttgradnja.hr/reference/'

W_NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

SPECIAL_500 = {'GACKA', 'PETRČANE'}


def dohvati_referenca_html():
    req = urllib.request.Request(
        REFERENCE_URL,
        headers={'User-Agent': 'Mozilla/5.0 (compatible; tt-gradnja-alati/1.0)'},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='replace')


def parsiraj_pergole(ref_html):
    """Vrati listu {title, href, img} za sve bioklimatska-pergola clanke (bez stolarije)."""
    # Napomena: prvi <article> na stranici je wrapper cijele stranice (Divi
    # "page" clanak) koji se u praksi proteze do prvog UNUTARNJEG </article>
    # (regex ne razumije ugnijezdjivanje) - njegov "class" je zato wrapperov,
    # ne stvarnog prvog projekta. Zato se NE filtrira po "category-reference-hr"
    # klasi (nepouzdano za prvu stavku), nego iskljucivo po tome sadrzi li
    # naslov rijec "pergola" (stolarija/PVC/grilje reference je nemaju).
    articles = re.findall(r'<article id="post-[^"]*" class="([^"]*)">(.*?)</article>', ref_html, re.S)
    items = []
    for cls, body in articles:
        m_href = re.search(r'<div class="et_pb_image_container"><a href="([^"]+)"', body)
        m_img = re.search(r'<img[^>]+src="([^"]+)"', body)
        m_title = re.search(r'<h2 class="entry-title">\s*<a href="[^"]+">([^<]+)</a>', body)
        if not (m_href and m_img and m_title):
            continue
        title = re.sub(r'\s+', ' ', html.unescape(m_title.group(1))).strip()
        if 'pergola' not in title.lower():
            continue  # stolarija/PVC/grilje
        items.append({'title': title, 'href': m_href.group(1), 'img': m_img.group(1)})
    return items


def citaj_docx_stupce(path):
    with zipfile.ZipFile(path) as z:
        xml_bytes = z.read('word/document.xml')
    root = ET.fromstring(xml_bytes)
    tbl = root.findall('.//w:tbl', W_NS)[0]
    row = tbl.findall('w:tr', W_NS)[0]
    cells = row.findall('w:tc', W_NS)
    stupci = []
    for c in cells:
        lines = []
        for p in c.findall('w:p', W_NS):
            text = ''.join(node.text or '' for node in p.findall('.//w:t', W_NS))
            text = text.strip()
            if text:
                lines.append(text)
        stupci.append(lines)
    return stupci[0], stupci[1]


def naizmjenicni_redoslijed(lijevo, desno):
    out = []
    for i in range(max(len(lijevo), len(desno))):
        if i < len(lijevo):
            out.append(lijevo[i])
        if i < len(desno):
            out.append(desno[i])
    return out


def norm(s):
    s = html.unescape(s).replace('–', '-').replace('—', '-')
    return re.sub(r'\s+', ' ', s).strip().upper()


def basename(url):
    ime = url.rsplit('/', 1)[-1]
    return re.sub(r'-\d+x\d+(?=\.\w+$)', '', ime)


def lokacija_iz_naslova(naslov):
    """Ocisti 'Bioklimatska pergola [SB400/SB500] X' -> 'X'."""
    t = naslov
    t = re.sub(r'(?i)^bioklimatska\s+pergola\s*[-–]?\s*', '', t).strip()
    t = re.sub(r'(?i)^sb[45]00\s+', '', t).strip()
    return t


CARD_RE = re.compile(
    r'<a class="card" href="(?P<href>[^"]+)"[^>]*>\s*'
    r'<img[^>]+>\s*'
    r'<div class="card-cap"><span>(?P<loc>[^<]*)</span>'
    r'<span class="model-tag">(?P<model>[^<]*)</span></div>\s*'
    r'</a>',
    re.S,
)


def ucitaj_postojece_kartice(index_html):
    m = re.search(
        r'(<div class="grid-g reveal" id="gal">)(.*?)(\n\s*</div>\s*\n\s*<div class="gal-more">)',
        index_html, re.S,
    )
    if not m:
        sys.exit('GRESKA: ne mogu pronaci #gal blok u index.html')
    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    kartice = []
    for cm in CARD_RE.finditer(body):
        kartice.append({
            'raw': cm.group(0),
            'href': cm.group('href'),
            'basename': basename(cm.group('href')),
            'loc': cm.group('loc'),
            'model': cm.group('model'),
        })
    return prefix, suffix, kartice, m.span()


def izgradi_novu_karticu(title, img, model):
    """href i img src moraju biti ISTI URL (sama fotografija) - lightbox
    (index.html) cita card.getAttribute('href') kao izvor uvecane slike, ne
    URL podstranice projekta."""
    lok = lokacija_iz_naslova(title)
    # "SUNBREAKER" u capsu ide samo na vidljivu .model-tag oznaku (trazeno od
    # klijenta); alt/aria-label prate postojecu konvenciju ("Sunbreaker").
    aria = f'Povećaj fotografiju: Sunbreaker {model}, {lok}'
    alt = f'Sunbreaker {model}, {lok}'
    return (
        f'      <a class="card" href="{img}" role="button" tabindex="0" '
        f'aria-label="{aria}">\n'
        f'        <img src="{img}" alt="{alt}" loading="lazy">\n'
        f'        <div class="card-cap"><span>{lok}</span>'
        f'<span class="model-tag">SUNBREAKER {model}</span></div>\n'
        f'      </a>'
    )


def glavno():
    provjeri = '--provjeri' in sys.argv

    with open(INDEX_HTML, encoding='utf-8') as f:
        index_html = f.read()
    prefix, suffix, postojece, span = ucitaj_postojece_kartice(index_html)
    postojece_po_slici = {k['basename']: k for k in postojece}
    print(f'Postojecih kartica u #gal: {len(postojece)}')

    ref_html = dohvati_referenca_html()
    pergole = parsiraj_pergole(ref_html)
    print(f'Pergola clanaka na live stranici: {len(pergole)}')
    if len(pergole) != 67:
        print(f'UPOZORENJE: ocekivano 67 pergola clanaka, dobiveno {len(pergole)}. Provjeri live stranicu.')

    lijevo, desno = citaj_docx_stupce(DOCX)
    redoslijed = naizmjenicni_redoslijed(lijevo, desno)
    print(f'Naslova u docx (naizmjenicno spojeno): {len(redoslijed)}')

    buckets = {}
    for p in pergole:
        buckets.setdefault(norm(p['title']), []).append(p)

    finalne_kartice = []
    zapisi = []
    nedostaju = []
    for pos, naslov in enumerate(redoslijed, start=1):
        kljuc = norm(naslov)
        red = buckets.get(kljuc)
        if not red:
            nedostaju.append(naslov)
            continue
        rec = red.pop(0)
        bn = basename(rec['img'])
        postoji = postojece_po_slici.get(bn)
        if postoji:
            finalne_kartice.append(postoji['raw'])
            model = re.sub(r'(?i)^sunbreaker\s+', '', postoji['model']).strip()
            zapisi.append({'pozicija': pos, 'naslov': naslov, 'href': postoji['href'],
                            'lokacija': postoji['loc'], 'model': model, 'status': 'postoji'})
        else:
            is_500 = 'SB500' in kljuc or kljuc.replace('BIOKLIMATSKA PERGOLA ', '').strip() in SPECIAL_500
            model = '500' if is_500 else '400'
            finalne_kartice.append(izgradi_novu_karticu(rec['title'], rec['img'], model))
            zapisi.append({'pozicija': pos, 'naslov': naslov, 'href': rec['img'],
                            'stranica': rec['href'],
                            'lokacija': lokacija_iz_naslova(rec['title']), 'model': model, 'status': 'novo'})

    if nedostaju:
        print('UPOZORENJE: naslovi iz docx-a bez podudaranja na live stranici:')
        for n in nedostaju:
            print('  -', n)

    zadrzano_basename = {basename(z['href']) for z in zapisi}
    ispalo = [k for k in postojece if k['basename'] not in zadrzano_basename]
    if ispalo:
        print(f'Kartice koje ISPADAJU (ne postoje u novom popisu od {len(redoslijed)}):')
        for k in ispalo:
            print(f"  - {k['loc']} ({k['basename']})")

    novih = sum(1 for z in zapisi if z['status'] == 'novo')
    print(f'Novih kartica: {novih} | Zadrzanih postojecih: {len(zapisi) - novih} | Ukupno: {len(zapisi)}')

    if provjeri:
        print('\n--provjeri: index.html NIJE promijenjen.')
        return

    kartice_uvucene = [
        k if k.startswith(' ') else '      ' + k
        for k in finalne_kartice
    ]
    novi_body = '\n' + '\n'.join(kartice_uvucene) + '\n    '
    novi_index_html = index_html[:span[0]] + prefix + novi_body + suffix + index_html[span[1]:]
    with open(INDEX_HTML, 'w', encoding='utf-8') as f:
        f.write(novi_index_html)
    print(f'Zapisano: {INDEX_HTML}')

    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(zapisi, f, ensure_ascii=False, indent=2)
    print(f'Zapisano: {OUT_JSON}')


if __name__ == '__main__':
    glavno()
