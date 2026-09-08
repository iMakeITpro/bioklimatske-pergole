# PRD — Konfigurator cijene i ispravci podataka

| | |
|---|---|
| **Projekt** | `bioklimatske-pergole` — TT Gradnja d.o.o. |
| **Repozitorij** | `git@github-makeitpro:iMakeITpro/bioklimatske-pergole.git`, grana `iteracija-2` |
| **Verzija** | 1.0 · 8. rujna 2026. |
| **Izvor podataka** | `dostavljeno/` — ispunjeni upitnik MIP-002-UP-2026-001 i šest Excel tablica |

> Priložiti na početku novog razgovora. Ne raditi ništa iz Faze 3 dok Faza 1 nije gotova i potvrđena.

---

## 1. Zašto

Konfigurator trenutno računa po izmišljenim brojkama iz prve verzije demoa. Klijent je dostavio stvarne cjenike i ispravio većinu tvrdnji na stranici.

Podsjetnik zašto stranica postoji: klijent troši 2.500–3.000 € mjesečno na Google Ads uz ~1 % konverziju, jer cijena nigdje nije bila navedena. **Konfigurator je jedini razlog postojanja stranice.** Sve ostalo mu služi.

---

## 2. Tehnička ograničenja

- Statička stranica na GitHub Pages, **bez build koraka i bez npm-a**, relativne putanje
- Zajednički `styles.css` za sve stranice, s oznakom verzije koja se podiže pri svakoj izmjeni
- Isto vrijedi za svaku datoteku koja se mijenja pod istim imenom
- Mapa `dostavljeno/` je u `.gitignore` — cjenici sadrže marže i **ne smiju** na javni repozitorij
- Sve mjeriti na 360, 390 i 768px prije commita, kroz lokalnu test-stranicu
- Bez vanjskih biblioteka

---

## FAZA 1 — Ispravci potvrđenih podataka

Klijent je ovo izričito potvrdio u upitniku. Radi se odmah, neovisno o konfiguratoru.

| Gdje | Sada | Ispravno |
|---|---|---|
| Traka pod herom, kartice, konfigurator | 36 boja | **33 boje** |
| Usporedna tablica, SB400 | Klasa 3 (≈62 km/h) | **Klasa 6** |
| Usporedna tablica | Rotacija 0–135° | **0–120°** za SB400 i SB500; 0–135° samo SB700 |
| Usporedna tablica, SB400 | Profil stupa 120×120 mm | **150×85 mm** |
| Jamstva | 48 h maksimalno vrijeme servisa | **72 h prosječno** |
| Jamstva, footer | poslujemo od 2016. | **2018.** |
| Cijela stranica | ovlašteni SELT zastupnik | **SELT/Aluprof** |
| Proces, korak 1 | isti dan | **unutar 2 radna dana** |
| Proces, korak 2 | 5 radnih dana | **unutar 3 radna dana od prihvaćanja ponude** |
| Proces, korak 5 | montaža 1–3 dana | **1–2 dana** |

**Usporedna tablica — izmjene redaka.** Van: nosivost snijega, uvlačive lamele. Unutra: profil konstrukcije (SB400 212×85, SB500 290×150, SB700 250×236,6 mm), integrirani ZIP u konstrukciju (ne / ne / da), rok proizvodnje (2–4 tjedna / 2–4 tjedna / **6–8 tjedana**). Plastifikacija: 33 boje standard za SB400 i SB500, **4 boje** za SB700.

**Preimenovanje trećeg modela.** Tarasola Technic View Pro → **Sunbreaker 700**. Isti proizvod, novi naziv radi sljedivosti. Mijenja se u kartici ponude, usporednoj tablici, padajućem izborniku, podnožju i na podstranici — uključujući naziv datoteke `tarasola-technic-view-pro.html` → `sunbreaker-700.html` i sve poveznice prema njoj.

**Kriteriji prihvaćanja Faze 1**

- [ ] Nijedna stara vrijednost iz tablice gore ne postoji više nigdje na stranicama
- [ ] Nema mrtvih poveznica nakon preimenovanja podstranice
- [ ] Strukturirani podaci u `<head>` usklađeni s novim vrijednostima
- [ ] Provjera na 360, 390 i 768px

---

## FAZA 2 — Cjenik kao podatkovna datoteka

Iz šest Excel tablica u `dostavljeno/` nastaje **`cjenik.js`** — jedna datoteka koja postavlja globalni objekt s cijenama. Bez `fetch`, da radi i lokalno bez servera.

**Struktura tablica, kako jest:**

| Model | Projekcije [mm] | Širine [mm] |
|---|---|---|
| SB400 | 3400–7000, korak 200 (19 vrijednosti) | 1500, 2000, 2500, 3000, 3500, 4000 |
| SB500 | 3000–7000, korak 250 | 4000, 4500, 5000 |

Uz svaki redak ide iznos **transporta i montaže**, koji se mijenja u dvije razine ovisno o projekciji.

**Tri regije:** Kontinentalna Hrvatska do Karlovca · Od Karlovca do Šibenika · Od Splita do Dubrovnika.

**Pravila pretvorbe**

- Vrijednosti se prepisuju točno, bez zaokruživanja i bez interpolacije
- Datoteka nosi oznaku iz koje je tablice nastala i datum, radi kasnije provjere
- Skripta za pretvorbu ostaje u repozitoriju da se cjenik može ponovno izraditi kad klijent pošalje ispravke

**Kriteriji prihvaćanja Faze 2**

- [ ] Svaka vrijednost u `cjenik.js` odgovara ćeliji u Excelu — provjeriti nasumičnim uzorkom od najmanje 20 ćelija kroz sve tri regije
- [ ] Nema dupliranih ključeva
- [ ] `cjenik.js` ne sadrži marže ni interne troškove, samo konačne cijene

---

## FAZA 3 — Konfigurator

### Tijek

1. **Model** — Sunbreaker 400 ili Sunbreaker 500. SB700 nije u konfiguratoru, vodi na obrazac upita.
2. **Dimenzije** — projekcija i širina, **isključivo vrijednosti iz tablice**. Ne klizači s proizvoljnim korakom, nego stvarne vrijednosti. Tablica je diskretna, pa i izbor mora biti.
3. **Lokacija** — odabir županije, koja se preslikava u jednu od tri regije. Ne prvi korak; dolazi nakon što je korisnik već nešto odabrao.
4. **Oprema** — samo stavke sa cijenom ulaze u izračun. Ostale se mogu odabrati, ali se prikazuju kao „na upit" i prosljeđuju u e-mail.
5. **Kontakt podaci** — ime, prezime, e-mail, telefon. Cijena se otključava tek nakon toga, kao i sada.

### Izračun i prikaz

Osnovna cijena iz tablice, plus oprema, plus transport i montaža.

**Rabat 10 %** primjenjuje se jer je upit došao preko konfiguratora — to je stvarni uvjet, ne izmišljeno sidro. Prikazuje se kao zasebna stavka „popust za upit putem konfiguratora", a ne kao precrtana cijena koja se nikad ne naplaćuje.

**PDV** — preklopnik privatni / poslovni kupac. **Privatni je zadana vrijednost i cijena mu se prikazuje s uključenim PDV-om**; to je zakonska obveza prema potrošačima. Poslovni vidi iznos bez PDV-a i PDV zasebno.

**Bez postotaka odstupanja.** Klijent je odustao od raspona. Piše se samo da je izračun informativan i da su odstupanja moguća.

**Izvan raspona tablice** — ako korisnik traži dimenziju koju cjenik ne pokriva, ne prikazuje se nikakva cijena nego poziv na kontakt. Šire izvedbe traže srednji stup, koji mijenja konstrukciju i nije u cjeniku.

### Oprema s poznatom cijenom

| Stavka | Cijena |
|---|---|
| LED rasvjeta | 1.200 € |
| Senzor kiše | 500 € |
| Senzor vjetra | 400 € |

Ostalo je „na upit": pametno upravljanje, ZIP screen sjenila, klizne staklene stijenke, IR grijalice, bočne slide grilje, bočni brisoleji, RAL boja izvan standardne palete.

### E-mail koji stiže

Zadržati postojeće slanje preko Web3Formsa. Dodati u poruku: **županiju, regiju, odabrane stavke „na upit", primijenjeni rabat i je li kupac privatni ili poslovni.**

### Gdje živi

**Izmjena (8.9.2026., odluka klijenta):** Konfigurator ostaje na naslovnici (`index.html`), na mjestu gdje je i sada — ne seli se na zasebnu stranicu. Konfigurator je glavna funkcija cijele stranice i ne smije se micati s landinga.

Izvorni prijedlog (zasebna stranica radi Google Ads Quality Scorea za skupu ključnu riječ „bioklimatska pergola cijena", da oglas vodi ravno na konfigurator) ovime je svjesno odbačen u korist zadržavanja konfiguratora na landingu.

**Kriteriji prihvaćanja Faze 3**

- [ ] Za deset nasumičnih kombinacija model × dimenzija × regija, prikazana cijena odgovara ručnom izračunu iz Excela
- [ ] Dimenzija izvan raspona ne prikazuje cijenu
- [ ] Preklopnik PDV-a mijenja iznos ispravno u oba smjera, privatni je zadan
- [ ] Rabat je vidljiva stavka, nigdje nema precrtane cijene
- [ ] E-mail sadrži sva polja iz popisa gore
- [ ] Nema horizontalnog scrolla ni dodirne mete ispod 44px na 360, 390 i 768px

---

## Blokira Fazu 3 — odgovori klijenta (Josip, 8.9.2026.)

| # | Pitanje | Odgovor |
|---|---|---|
| 1 | Duplirane projekcije 4500 i 4750 u sve tri SB500 tablice | Riješeno — klijent poslao nove, ispravljene SB500 tablice (bez duplikata, niz 3000–7000 mm u koraku 250). Stare arhivirane u `dostavljeno/_staro/`. |
| 2 | Je li transport već u cijeni u tablici | **Ne.** Transport i montaža uvijek se prikazuju zasebno, kako i piše u tablici. |
| 3 | Je li rabat od 10 % u svim tablicama | **Da** — cijene u svim tablicama već imaju odbijeni rabat. Rabat se **ne odnosi** na transport/montažu, samo na cijenu same pergole. |
| 4 | Je li `SB_550` zapravo SB500 za Split–Dubrovnik | **Da**, sve je SB500. Nova tablica ispravno preimenovana. |
| 5 | Koje županije spadaju u koju regiju | Vidi tablicu ispod — klijent potvrdio "točno". |
| 6 | Cijene za opremu koja piše „na upit" | Klijent predlaže da ostane „na upit" za sada — cijena bi znatno porasla (npr. staklene stijenke koštaju koliko i sama pergola), komunicira se uživo/telefonski. Ne blokira Fazu 3 — PRD već predviđa „na upit" tijek za stavke bez cijene (vidi Oprema s poznatom cijenom gore). |

Sve stavke riješene 8.9.2026. Faza 3 može krenuti.

### Mapiranje županija → regija (potvrđeno)

| Regija (naziv iz cjenika) | Županije |
|---|---|
| Kontinentalna Hrvatska do Karlovca | Grad Zagreb, Zagrebačka, Krapinsko-zagorska, Varaždinska, Koprivničko-križevačka, Međimurska, Bjelovarsko-bilogorska, Virovitičko-podravska, Požeško-slavonska, Brodsko-posavska, Osječko-baranjska, Vukovarsko-srijemska, Sisačko-moslavačka, Karlovačka |
| Od Karlovca do Šibenika | Primorsko-goranska, Istarska, Ličko-senjska, Zadarska, Šibensko-kninska |
| Od Splita do Dubrovnika | Splitsko-dalmatinska, Dubrovačko-neretvanska |

Pokriva svih 21 hrvatskih jedinica (20 županija + Grad Zagreb), bez preklapanja i bez praznina.

---

## Način rada

Jedna faza po koraku, svaka završava prikazom izmjena i čekanjem potvrde. Ne commitati i ne pushati bez odobrenja; prije commita ispisati `git status` i popis datoteka. Ako rezultat ne valja — vraćanje na checkpoint i ispravak polazišta, ne krpanje.
