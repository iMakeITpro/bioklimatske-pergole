#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dopuni alati/projekti.json s hero fotografijom i punom galerijom za svaki
od 67 projekata, dohvacajuci svaku pojedinacnu podstranicu s ttgradnja.hr
(polje "stranica" u projekti.json, upisano od alati/dohvati_projekte.py).

Struktura izvorne stranice (Divi/WordPress, potvrdjeno na uzorku "Zaton"):
  - hero (puna rezolucija): standardni Yoast/RankMath <meta property="og:image"
    content="FULL.jpg"> - pouzdanije od parsiranja Divi image-modula (koji
    zna varirati izmedju postova) jer je og:image generiran automatski iz
    "featured image" posta, isti za sve postove.
  - galerija: svaka stavka je <div class="et_pb_gallery_image ..."><a
    href="FULL.jpg" title="..."><img src="THUMB-400x284.jpg" ...></a></div> -
    trazi se svugdje na stranici (bez pokusaja odredjivanja pocetka/kraja
    cijelog gallery-modula, sto je krhko zbog razlicitog broja ugnijezdjenih
    <div> zatvaranja na kraju modula ovisno o postu).

Pokretanje:
    python3 alati/dohvati_galerije.py

Ponovno pokretanje samo prepisuje foto_hero/foto_galerija polja - ostatak
projekti.json (poziciju/naslov/lokaciju/model) ne dira.
"""
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJEKTI_JSON = os.path.join(ROOT, 'alati', 'projekti.json')
PAUZA_SEK = 0.4

GALERIJA_STAVKA_RE = re.compile(
    r'<div class="et_pb_gallery_image[^"]*">\s*'
    r'<a href="([^"]+)"[^>]*title="[^"]*">\s*'
    r'<img[^>]+src="([^"]+)"',
    re.S,
)
HERO_RE = re.compile(r'<meta property="og:image" content="([^"]+)"')


def dohvati(url):
    req = urllib.request.Request(
        url, headers={'User-Agent': 'Mozilla/5.0 (compatible; tt-gradnja-alati/1.0)'},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='replace')


def izvuci_hero_i_galeriju(html_str):
    m_hero = HERO_RE.search(html_str)
    hero = m_hero.group(1) if m_hero else None

    galerija = [
        {'full': m.group(1), 'thumb': m.group(2)}
        for m in GALERIJA_STAVKA_RE.finditer(html_str)
    ]
    return hero, galerija


def glavno():
    with open(PROJEKTI_JSON, encoding='utf-8') as f:
        zapisi = json.load(f)

    problemi = []
    for i, z in enumerate(zapisi):
        url = z['stranica']
        try:
            html_str = dohvati(url)
        except Exception as e:
            problemi.append(f"{z['lokacija']} ({url}): GRESKA dohvata - {e}")
            continue
        hero, galerija = izvuci_hero_i_galeriju(html_str)
        if not hero:
            problemi.append(f"{z['lokacija']} ({url}): hero NIJE pronadjen")
        if not galerija:
            problemi.append(f"{z['lokacija']} ({url}): galerija NIJE pronadjena (0 stavki)")
        z['foto_hero'] = hero
        z['foto_galerija'] = galerija
        print(f"[{i+1}/{len(zapisi)}] {z['lokacija']}: hero={'OK' if hero else 'X'}, "
              f"galerija={len(galerija)} fotki")
        time.sleep(PAUZA_SEK)

    with open(PROJEKTI_JSON, 'w', encoding='utf-8') as f:
        json.dump(zapisi, f, ensure_ascii=False, indent=2)
    print(f'\nZapisano: {PROJEKTI_JSON}')

    if problemi:
        print(f'\nUPOZORENJA ({len(problemi)}):')
        for p in problemi:
            print('  -', p)
        sys.exit(1)


if __name__ == '__main__':
    glavno()
