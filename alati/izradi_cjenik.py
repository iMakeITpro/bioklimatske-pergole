#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Izradi cjenik.js iz Excel tablica u nove_tablice/ i dostavljeno/.

Pokretanje:
    python3 alati/izradi_cjenik.py            # izradi cjenik.js
    python3 alati/izradi_cjenik.py --provjeri  # izradi pa nasumicno provjeri N celija protiv Excela

dostavljeno/ je u .gitignore (sadrzi marze) — cjenik.js sadrzi samo
konacne cijene i sigurno se moze commitati. Ponovno pokrenuti ovu
skriptu kad klijent posalje ispravljene tablice — cjenik.js se NE
uredjuje rucno.

Izvori se traze redom: nove_tablice/, pa dostavljeno/. Ako tablice nema ni u
jednoj mapi, blok (model, regija) se preuzima iz postojeceg cjenik.js
(izvor i datum ostaju netaknuti) — tako se moze zamijeniti samo dio tablica.
"""
import json
import datetime
import os
import random
import sys
import unicodedata

import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIRS = [os.path.join(ROOT, 'nove_tablice'), os.path.join(ROOT, 'dostavljeno')]
OUT = os.path.join(ROOT, 'js', 'cjenik.js')

# Width slider range per model, in mm (1 cm step). Table columns are price classes
# ("up to that width"): the price for width w is taken from the first column >= w.
# The range is stated here because it cannot be derived from the columns
# (SB500 has no column below 4500, yet its slider starts at 4000; SB400 keeps a 1500 column
# but its slider starts at 2000 = minimum width of the system, so that column is never used).
RASPON_SIRINE = {
    '400': {'sirinaMin': 2000, 'sirinaMax': 4000, 'sirinaKorak': 10},
    '500': {'sirinaMin': 4000, 'sirinaMax': 5000, 'sirinaKorak': 10},
}

# Columns that are no longer a valid price class (client removed them: SB500 4000 m
# only meant "up to 4 m", which the 4000-5000 slider range never reaches).
IZBACENI_STUPCI = {'400': [], '500': [4000]}

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


def nadji_izvor(fname):
    """Vrati putanju do tablice u prvoj mapi u kojoj postoji, ili None.

    Imena se usporedjuju neosjetljivo na velika/mala slova i na Unicode
    normalizaciju. macOS zapisuje dijakritiku u NFD (S + kvacica), ovaj izvorni
    kod je u NFC, a klijent salje imena s varijacijama ("od" / "Od"). Stroga
    usporedba bi promasila, blok bi se tiho preuzeo iz starog cjenik.js i to bi
    izgledalo kao uspjeh dok cijena ostaje stara.
    """
    trazeno = unicodedata.normalize('NFC', fname).casefold()
    for d in SRC_DIRS:
        if not os.path.isdir(d):
            continue
        for stvarno in sorted(os.listdir(d)):
            if unicodedata.normalize('NFC', stvarno).casefold() == trazeno:
                return os.path.join(d, stvarno)
    return None


def odsijeci_prazne_stupce(rows):
    """Odbaci stupce s kraja koji su prazni u svim redcima.

    Excel zna nositi stupce izvan podataka: SB400 kontinentalna ima raspon
    A1:K24 iako podaci staju u A:H. Bez rezanja bi "transport je zadnji stupac"
    pokazivalo na praznu celiju i ucitavanje bi puklo.
    """
    zadnji = -1
    for r in rows:
        for j, v in enumerate(r):
            if v is not None and j > zadnji:
                zadnji = j
    return [r[:zadnji + 1] for r in rows]


def nadji_zaglavlje(rows):
    """Zaglavlje = prvi redak s barem 2 brojcane celije nakon prvog stupca (sirine u mm)."""
    for i, r in enumerate(rows):
        if len([v for v in r[1:] if isinstance(v, (int, float))]) >= 2:
            return i
    raise ValueError("zaglavlje nije pronadjeno")


def ucitaj_tablicu(path):
    """Vrati (sirine:list[int], redovi:dict[projekcija -> {cijene:dict, transport:float}])."""
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = [r for r in ws.iter_rows(values_only=True) if any(v is not None for v in r)]
    rows = odsijeci_prazne_stupce(rows)

    header_idx = nadji_zaglavlje(rows)
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


def ucitaj_postojeci_cjenik():
    """Vrati postojeci window.CJENIK iz cjenik.js (ili None ako datoteke jos nema)."""
    if not os.path.exists(OUT):
        return None
    src = open(OUT, encoding='utf-8').read()
    start = src.index('window.CJENIK = ') + len('window.CJENIK = ')
    return json.loads(src[start:].rstrip().rstrip(';'))


def izbaci_stupce(model, sirine, redovi):
    """Skini stupce koji vise nisu razred cijene (IZBACENI_STUPCI); ne mijenja ulaz."""
    izbaceni = set(IZBACENI_STUPCI[model])
    sirine = [s for s in sirine if s not in izbaceni]
    redovi = {
        p: {'cijene': {s: c for s, c in red['cijene'].items() if s not in izbaceni},
            'transport': red['transport']}
        for p, red in redovi.items()
    }
    return sirine, redovi


def normaliziraj_blok(blok):
    """JSON vraca kljuceve kao stringove — vrati int kljuceve kao iz ucitaj_tablicu()."""
    return (
        list(blok['sirine']),
        {
            int(p): {'cijene': {int(s): c for s, c in red['cijene'].items()}, 'transport': red['transport']}
            for p, red in blok['projekcije'].items()
        },
    )


def izgradi():
    cijene_out = {}
    izvor_out = {}
    putanje = {}  # (model, regija) -> putanja Excela; None = preuzeto iz postojeceg cjenik.js
    greske = []
    postojeci = ucitaj_postojeci_cjenik()

    for model, regije in IZVORI.items():
        cijene_out[model] = {}
        izvor_out[model] = {}
        for regija, fname in regije.items():
            path = nadji_izvor(fname)
            if path is None:
                # no fresh Excel for this block — carry it over from the current cjenik.js
                stari = postojeci and postojeci['cijene'].get(model, {}).get(regija)
                if not stari:
                    greske.append("NEDOSTAJE: %s (nema ga ni u jednoj mapi ni u postojecem cjenik.js)" % fname)
                    continue
                sirine, redovi = normaliziraj_blok(stari)
                izvor_out[model][regija] = postojeci['izvor'][model][regija]
                putanje[(model, regija)] = None
            else:
                try:
                    sirine, redovi = ucitaj_tablicu(path)
                except Exception as e:
                    greske.append("%s: %s" % (fname, e))
                    continue
                izvor_out[model][regija] = {
                    'datoteka': fname,
                    'datum_generiranja': datetime.date.today().isoformat(),
                }
                putanje[(model, regija)] = path
            sirine, redovi = izbaci_stupce(model, sirine, redovi)
            cijene_out[model][regija] = {'sirine': sirine, 'projekcije': redovi}

    # all regions of a model must share the same price classes and the same depths
    for model, regije in cijene_out.items():
        klase = {tuple(b['sirine']) for b in regije.values()}
        dubine = {tuple(sorted(b['projekcije'])) for b in regije.values()}
        if len(klase) > 1:
            greske.append("SB%s: regije nemaju iste stupce sirina: %s" % (model, sorted(klase)))
        if len(dubine) > 1:
            greske.append("SB%s: regije nemaju iste projekcije" % model)
        for regija, b in regije.items():
            r = RASPON_SIRINE[model]
            if b['sirine'] and r['sirinaMax'] > max(b['sirine']):
                greske.append("SB%s / %s: raspon sirine (%d) prelazi zadnji stupac (%d)" % (
                    model, regija, r['sirinaMax'], max(b['sirine'])))

    if greske:
        sys.stderr.write("\n".join(greske) + "\n")
        sys.exit(1)

    payload = {
        'generirano': datetime.date.today().isoformat(),
        'napomena': (
            'Cijene u tablicama vec sadrze odbijeni rabat od 10% (potvrdio klijent, '
            'e-mail 8.9.2026). Transport i montaza NIJE ukljucen u cijenu pergole i '
            'NE prima rabat — uvijek se prikazuje kao zasebna stavka. Stupci sirina su '
            'razredi cijene: cijena za sirinu w uzima se iz prvog stupca >= w.'
        ),
        'regije': REGIJE,
        'raspon': RASPON_SIRINE,
        'izvor': izvor_out,
        'cijene': cijene_out,
    }

    js = (
        "// cjenik.js — generirano skriptom alati/izradi_cjenik.py iz nove_tablice/ i dostavljeno/\n"
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
            print("  SB%s / %s: %d redova, stupci sirina %s, transport %s, izvor: %s" % (
                m, r, n, cijene_out[m][r]['sirine'],
                sorted(set(row['transport'] for row in cijene_out[m][r]['projekcije'].values())),
                'Excel' if putanje[(m, r)] else 'preuzeto iz postojeceg cjenik.js'
            ))
    print("Ukupno redova (svi modeli x regije): %d" % ukupno)
    return cijene_out, putanje


def provjeri(cijene_out, putanje, n=24):
    """Nasumicno uzmi N celija iz generiranog cjenik.js i usporedi s izvornim Excelom.

    Blokovi preuzeti iz postojeceg cjenik.js nemaju Excel pa se ne provjeravaju.
    """
    uzorci = []
    for model, regije in cijene_out.items():
        for regija, podaci in regije.items():
            if not putanje[(model, regija)]:
                continue
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
            wb = openpyxl.load_workbook(putanje[key], data_only=True)
            ws = wb[wb.sheetnames[0]]
            rows = [r for r in ws.iter_rows(values_only=True) if any(v is not None for v in r)]
            rows = odsijeci_prazne_stupce(rows)
            cache[key] = (rows, nadji_zaglavlje(rows))
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
    podaci, putanje = izgradi()
    if '--provjeri' in sys.argv:
        print()
        print("=== Nasumicna provjera (min. 20 celija kroz regije s Excel izvorom, PRD Faza 2) ===")
        provjeri(podaci, putanje, n=24)
