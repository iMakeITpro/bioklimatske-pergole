#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Izradi cjenik.js iz Excel tablica u dostavljeno/.

Pokretanje:
    python3 alati/izradi_cjenik.py            # izradi cjenik.js
    python3 alati/izradi_cjenik.py --provjeri  # izradi pa nasumicno provjeri N celija protiv Excela

dostavljeno/ je u .gitignore (sadrzi marze) — cjenik.js sadrzi samo
konacne cijene i sigurno se moze commitati. Ponovno pokrenuti ovu
skriptu kad klijent posalje ispravljene tablice — cjenik.js se NE
uredjuje rucno.
"""
import json
import datetime
import os
import random
import sys

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'dostavljeno')
OUT = os.path.join(ROOT, 'cjenik.js')

REGIJE = {
    'kontinentalna': 'Kontinentalna Hrvatska do Karlovca',
    'karlovac-sibenik': 'Od Karlovca do Šibenika',
    'split-dubrovnik': 'Od Splita do Dubrovnika',
}

IZVORI = {
    '400': {
        'kontinentalna': 'Pergola_SB400_kalkulacija_Kontinentalna Hrvatska do Karlovca.xlsx',
        'karlovac-sibenik': 'Pergola_SB400_kalkulacija_Od Karlovca do Šibenika .xlsx',
        'split-dubrovnik': 'Pergola_SB400_kalkulacija Split do Dubrovnika.xlsx',
    },
    '500': {
        'kontinentalna': 'Pergola_SB500_kalkulacija Kontinentalna Hrvatska do Karlovca.xlsx',
        'karlovac-sibenik': 'Pergola_SB500_kalkulacija Od Karlovca do Šibenika.xlsx',
        'split-dubrovnik': 'Pergola_SB_500_kalkulacija od Splita do Dubrovnika.xlsx',
    },
}


def ucitaj_tablicu(path):
    """Vrati (sirine:list[int], redovi:dict[projekcija -> {cijene:dict, transport:float}])."""
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = [r for r in ws.iter_rows(values_only=True) if any(v is not None for v in r)]

    # zaglavlje = prvi redak s barem 3 brojcane celije nakon prvog stupca (sirine u mm)
    header_idx = None
    for i, r in enumerate(rows):
        nums = [v for v in r[1:] if isinstance(v, (int, float))]
        if len(nums) >= 3:
            header_idx = i
            break
    if header_idx is None:
        raise ValueError("zaglavlje nije pronadjeno")

    header = rows[header_idx]
    sirine = [int(v) for v in header[1:] if isinstance(v, (int, float))]
    transport_col = len(header) - 1  # stupac transporta uvijek zadnji u retku

    redovi = {}
    for r in rows[header_idx + 1:]:
        if not isinstance(r[0], (int, float)):
            continue  # npr. "PDV nije ukljuceno u cijenu"
        projekcija = int(r[0])
        if projekcija in redovi:
            raise ValueError("DUPLICIRANA projekcija %s" % projekcija)
        cijene = {}
        for j, sirina in enumerate(sirine, start=1):
            v = r[j] if j < len(r) else None
            if v is None:
                continue
            cijene[sirina] = round(float(v), 2)
        transport = r[transport_col]
        redovi[projekcija] = {'cijene': cijene, 'transport': round(float(transport), 2)}
    return sirine, redovi


def izgradi():
    cijene_out = {}
    izvor_out = {}
    greske = []

    for model, regije in IZVORI.items():
        cijene_out[model] = {}
        izvor_out[model] = {}
        for regija, fname in regije.items():
            path = os.path.join(SRC, fname)
            if not os.path.exists(path):
                greske.append("NEDOSTAJE: %s" % path)
                continue
            try:
                sirine, redovi = ucitaj_tablicu(path)
            except Exception as e:
                greske.append("%s: %s" % (fname, e))
                continue
            cijene_out[model][regija] = {'sirine': sirine, 'projekcije': redovi}
            izvor_out[model][regija] = {
                'datoteka': fname,
                'datum_generiranja': datetime.date.today().isoformat(),
            }

    if greske:
        sys.stderr.write("\n".join(greske) + "\n")
        sys.exit(1)

    payload = {
        'generirano': datetime.date.today().isoformat(),
        'napomena': (
            'Cijene u tablicama vec sadrze odbijeni rabat od 10% (potvrdio klijent, '
            'e-mail 8.9.2026). Transport i montaza NIJE ukljucen u cijenu pergole i '
            'NE prima rabat — uvijek se prikazuje kao zasebna stavka.'
        ),
        'regije': REGIJE,
        'izvor': izvor_out,
        'cijene': cijene_out,
    }

    js = (
        "// cjenik.js — generirano skriptom alati/izradi_cjenik.py iz dostavljeno/\n"
        "// NE UREDJIVATI RUCNO. Ponovno pokrenuti skriptu kad klijent posalje ispravljene tablice.\n"
        "// Vrijednosti prepisane tocno iz Excela — bez zaokruzivanja i bez interpolacije (jedina obrada:\n"
        "// zaokruzivanje na 2 decimale radi ciscenja Excelovog binarnog zapisa, npr.\n"
        "// 12251.300000000001 -> 12251.3 — sama vrijednost ostaje ista, samo se cisti float sum).\n"
        "window.CJENIK = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
    )

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)

    print("OK — cjenik.js zapisan: %s" % OUT)
    ukupno = 0
    for m in cijene_out:
        for r in cijene_out[m]:
            n = len(cijene_out[m][r]['projekcije'])
            ukupno += n
            print("  SB%s / %s: %d redova x %d sirina, transport %s" % (
                m, r, n, len(cijene_out[m][r]['sirine']),
                sorted(set(row['transport'] for row in cijene_out[m][r]['projekcije'].values()))
            ))
    print("Ukupno redova (svi modeli x regije): %d" % ukupno)
    return cijene_out


def provjeri(cijene_out, n=24):
    """Nasumicno uzmi N celija iz generiranog cjenik.js i usporedi s izvornim Excelom."""
    uzorci = []
    for model, regije in cijene_out.items():
        for regija, podaci in regije.items():
            for projekcija, red in podaci['projekcije'].items():
                for sirina, cijena in red['cijene'].items():
                    uzorci.append((model, regija, projekcija, sirina, cijena))
                uzorci.append((model, regija, projekcija, 'transport', red['transport']))

    random.seed()
    izbor = random.sample(uzorci, min(n, len(uzorci)))
    # grupiraj po (model, regija) da ne otvaramo isti excel vise puta nepotrebno
    cache = {}
    neuspjeh = 0
    for model, regija, projekcija, sirina, ocekivano in izbor:
        key = (model, regija)
        if key not in cache:
            fname = IZVORI[model][regija]
            path = os.path.join(SRC, fname)
            wb = openpyxl.load_workbook(path, data_only=True)
            ws = wb[wb.sheetnames[0]]
            rows = [r for r in ws.iter_rows(values_only=True) if any(v is not None for v in r)]
            header_idx = next(i for i, r in enumerate(rows) if len([v for v in r[1:] if isinstance(v, (int, float))]) >= 3)
            cache[key] = (rows, header_idx)
        rows, header_idx = cache[key]
        header = rows[header_idx]
        sirine = [int(v) for v in header[1:] if isinstance(v, (int, float))]
        transport_col = len(header) - 1

        redak = next(r for r in rows[header_idx + 1:] if isinstance(r[0], (int, float)) and int(r[0]) == projekcija)
        if sirina == 'transport':
            stvarno = round(float(redak[transport_col]), 2)
        else:
            idx = sirine.index(sirina) + 1
            stvarno = round(float(redak[idx]), 2)

        oznaka = "OK " if stvarno == ocekivano else "NE VALJA"
        if stvarno != ocekivano:
            neuspjeh += 1
        print("  [%s] SB%s / %s / proj=%s / %s: cjenik.js=%s  excel=%s" % (
            oznaka, model, regija, projekcija, sirina, ocekivano, stvarno))

    print()
    if neuspjeh:
        print("PROVJERA NIJE PROSLA — %d/%d ne odgovara Excelu" % (neuspjeh, len(izbor)))
        sys.exit(1)
    print("PROVJERA OK — svih %d nasumicno odabranih celija odgovara Excelu tocno." % len(izbor))


if __name__ == '__main__':
    podaci = izgradi()
    if '--provjeri' in sys.argv:
        print()
        print("=== Nasumicna provjera (min. 20 celija kroz sve regije, PRD Faza 2) ===")
        provjeri(podaci, n=24)
