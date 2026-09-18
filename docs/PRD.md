# PRD — Bioklimatske pergole, iteracija 2

| | |
|---|---|
| **Projekt** | `bioklimatske-pergole` — demo za TT Gradnja d.o.o. |
| **Repozitorij** | `git@github-makeitpro:iMakeITpro/bioklimatske-pergole.git` |
| **Objava** | https://imakeitpro.github.io/bioklimatske-pergole/ |
| **Klijent** | TT Gradnja d.o.o., Slavonski Brod · Josip Pudić |
| **Nositelj** | MakeIT PRO d.o.o. |
| **Verzija** | 2.0 |
| **Datum** | 5. rujna 2026. |
| **Izvori** | Zapisnik MIP-001-ZS-2026-002 (28.8.2026.) + upute Antonia |

---

## 1. Polazište

**Odobrena verzija je ona na GitHub Pagesu** — `index.html` u korijenu ovog repozitorija. Klijent ju je vidio i zadovoljan je.

Paralelna iteracija koju je radio Empir3 **se ne preuzima**. Iznimka: njihov SEO i konkurentski brief ostaje kao referenca za sadržaj i ključne riječi.

### Zašto stranica postoji

Klijent troši 2.500–3.000 € mjesečno na Google Ads uz ~1 % konverziju. Postojeća `bioklimatskepergole.hr` nigdje ne navodi cijenu, pa svatko mora nazvati samo da sazna red veličine. Prosječan projekt je ~20.000 €.

**Cilj nije više upita — nego manje, ali kvalificiranih.**

Dva načela nadjačavaju svaku pojedinačnu odluku o dizajnu:

1. **Kvalificiranje kroz konfigurator.** Posjetitelj mora doći do broja koji se odnosi na njegovu situaciju, a ne odustati jer ga nema.
2. **Brzina je poslovni zahtjev.** Brzina odredišne stranice ulazi u Google Ads Quality Score. Sporija stranica doslovno poskupljuje svaki plaćeni klik.

---

## 2. Tehnička ograničenja

- Sve ostaje u **jednoj `index.html`** datoteci, inline `<style>` i `<script>`
- **Bez build koraka, npm-a, frameworka i vanjskih biblioteka**
- Statička stranica na GitHub Pages, **relativne putanje**
- Postojeća paleta u CSS varijablama se ne mijenja bez razloga
- Bez refaktoriranja izvan opsega — uočeno se zapisuje, ne implementira

---

## 3. Faze

### FAZA 1 — Higijena repozitorija ✅ *gotovo*

- [x] `.gitignore` proširen: svi `.mp4` osim finalnog hero videa, svi `.pdf` / `.docx` / `.xlsx`, mapa s CSV-ovima, stare radne kopije `bioklimatskepergole/` i `bioklimatskepergole1/`
- [x] Interni klijentski dokumenti (Google Ads revizija, Analiza i rješenje, Aneks) više ne mogu otići na javni repozitorij

---

### FAZA 2 — Hero: video i raspored

**Video.** Izvor je `Isjecak_ttgradnja.mp4` (5,78 s, 1920×1080). Zvuk uklonjen.

Izvedba:

- Poster slika nosi prvi prikaz i učitava se odmah
- Video se dohvaća **tek nakon što se stranica iscrta** (`preload="none"`, pokretanje nakon `load`)
- Na mobitelu (≤768px) **video se ne učitava uopće** — ostaje poster
- `muted loop playsinline`, bez zvučnog zapisa u samoj datoteci

**Raspored teksta.** Trenutno je sav tekst u sredini i prekriva video.

- Uklanja se središnji blok: nadnaslov, naslov i odlomak koji stoje preko sredine videa
- Preostali sadržaj se preslaguje tako da video diše — poravnanje prema dnu ili u stranu, ne preko središta kadra
- Odlomak s tehničkim podacima (vjetar, jamstvo, montaža) **ostaje** — *čeka se Antoniov screenshot s označene dvije linije koje idu van*

**Kriteriji prihvaćanja:**

- [ ] Prvi prikaz stranice ne čeka video
- [ ] Na mobitelu se video ne prenosi
- [ ] Središte kadra vidljivo, tekst ne prekriva glavni motiv
- [ ] Kontrast teksta preko videa zadovoljava WCAG AA

---

### FAZA 3 — Fotografije na karticama modela

Kartice SB400 i SB500 trenutno nemaju sliku, a treći stupac je ima. Vizualno nedosljedno.

- Po **jedna fotografija** na SB400 i SB500 karticu, u istom formatu kao treći stupac
- Izvor: postojeće fotografije s `bioklimatskepergole.hr` — koriste se iste apsolutne adrese kao već postojeća galerija, bez preuzimanja
- **Opisi i popisi značajki ostaju netaknuti** — ništa se ne gubi
- Vizualno mora biti dotjerano, ne samo funkcionalno

**Kriteriji prihvaćanja:**

- [ ] Sve tri kartice imaju sliku i jednaku visinu medija
- [ ] Nijedna postojeća stavka teksta nije uklonjena
- [ ] `loading="lazy"` na svim novim slikama
- [ ] Raspored ostaje čitak na 360 / 390 / 768px

---

### FAZA 4 — Treći stupac: Tarasola Technic View Pro

Želja klijenta. Zamjenjuje **SB500 Diamond**, koji izlazi iz demoa.

- Pozicioniranje: vrhunac ponude, ultra-premium, **drugi partner koji se slabije gura jer je najskuplji** — bez agresivne promocije
- **Bez konfiguratora.** CTA vodi na kontakt formu, „Cijena na upit"
- Specifikacije s `tarasola.co.uk/products/technic-view-pro/`
- Red „Cijena (od)" za taj stupac ne postoji

**Ovisnost:** fotografije Tarasole mora dostaviti Antonio. Ne preuzimaju se s tuđe domene.

---

### FAZA 5 — Stavke iz zapisnika *(opseg za potvrdu)*

Ovo su točke iz potpisanog zapisnika koje još nisu izvedene na odobrenoj verziji. Antonio potvrđuje ulaze li u ovu iteraciju ili idu kasnije.

| # | Zapisnik | Stavka |
|---|---|---|
| 1 | t. 3 | Uklanjanje javnih fiksnih cijena s kartica i iz usporedne tablice |
| 2 | t. 4 | Konfigurator i forma kao jedan proces — okvirna ponuda tek nakon unosa imena, prezimena, e-maila i telefona; napomena o varijaciji 10–15 % i kontaktu u roku 3–4 dana |
| 3 | t. 3 | „Premium" terminologija kroz naslove |
| 4 | t. 6 | USP blok ispod heroa |

---

### FAZA 6 — `noindex`

Vraća se `<meta name="robots" content="noindex, nofollow">`.

Razlog: na stranici stoje brojke koje klijent nije potvrdio (187 projekata, 87 recenzija, ocjena 4,9), recenzije s punim imenima i `aggregateRating` u strukturiranim podacima. Dok to nije potvrđeno, stranica se ne indeksira.

---

## 4. Nefunkcionalni zahtjevi

| Područje | Zahtjev |
|---|---|
| **Performanse** | Prvi prikaz ne čeka video. Na mobitelu se video ne prenosi. Sve nove slike `loading="lazy"` |
| **Mobitel** | Provjera na 360 / 390 / 768px. Nema horizontalnog scrolla. Tap targeti ≥44px. Polja forme ≥16px |
| **Pristupačnost** | WCAG AA — 4,5:1 za tekst, 3:1 za velike naslove |
| **Indeksiranje** | `noindex, nofollow` dok klijent ne potvrdi brojke |

---

## 5. Način rada

1. **Jedna faza po koraku.** Svaka završava prikazom izmjena i čekanjem potvrde
2. **Ne commita se i ne pusha** bez odobrenja
3. Ako rezultat ne valja — vraćanje na checkpoint i ispravak polazišta, ne krpanje

---

## 6. Otvorene stavke

| # | Stavka | Nositelj |
|---|---|---|
| 1 | Screenshot s označene dvije linije koje idu iz odlomka o vjetru | Antonio |
| 2 | Fotografije Tarasola Technic View Pro | Antonio |
| 3 | Odabir varijante hero videa (B ili A) | Antonio |
| 4 | Potvrda opsega Faze 5 | Antonio |
| 5 | Stvarne Google recenzije umjesto trenutnih | Klijent |
| 6 | Potvrda: rok isporuke 2–4 tjedna (u konfliktu s 5–7 tjedana proizvodnje), 36 boja, jamstva, vjetar, snijeg | Klijent |

---

## 7. Izvan opsega

**Faza 2 projekta — višestranica.** Zapisnik t. 1 i 7: podstranice po modelu, tehničke specifikacije, poprečni presjeci, sustavi odvodnje, galerije, videozapisi montaže s YouTubea. Kreće tek kad je ova iteracija dovršena i odobrena.

**Odoo 19 Enterprise.** Antonio podiže server i uvozi stranicu preko modula. Nije dio ovog dokumenta.
