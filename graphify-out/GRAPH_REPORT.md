# Graph Report - bioklimatske-pergole  (2026-10-02)

## Corpus Check
- 136 files · ~330,515 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 1, .css 1, .avif 1)

## Summary
- 298 nodes · 604 edges · 11 communities
- Extraction: 87% EXTRACTED · 12% INFERRED · 1% AMBIGUOUS · INFERRED: 71 edges (avg confidence: 0.84)
- Token cost: 526,749 input · 0 output

## Community Hubs (Navigation)
- Naslovnica i projekti
- Alati: dohvat projekata i galerija
- Konfigurator i upitni obrasci
- Pergola Solid i Shutters
- CHANGELOG i povijest izmjena
- SB400/SB500 i proizvodjac
- Izrada cjenika (Python)
- PRD konfiguratora
- Sunbreaker 700
- Vertoline
- Montazni videi i proces

## God Nodes (most connected - your core abstractions)
1. `Naslovnica (index.html)` - 107 edges
2. `Sunbreaker 400 - ulazni model (sunbreaker-400.html)` - 81 edges
3. `Konfigurator okvirne ponude (Model, Dimenzije, Lokacija, Oprema, Cijena)` - 30 edges
4. `CHANGELOG.md - popis izmjena (Faze 1-10, Otvoreno)` - 25 edges
5. `Stranica Zatražite ponudu (upit.html)` - 25 edges
6. `Sunbreaker 500 - srednji model (sunbreaker-500.html)` - 24 edges
7. `Sunbreaker 700 - ultra-premium s integriranim ZIP sjenilom (sunbreaker-700.html)` - 17 edges
8. `Sistem Slide - bočni klizni sustav zaštite (sistem-slide.html)` - 17 edges
9. `FAZA 3: Konfigurator` - 14 edges
10. `glavno()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `konfigurator:upit-poslan custom event (ads tracking hook)` --references--> `Naslovnica (index.html)`  [EXTRACTED]
  docs/PRD-konfigurator.md → index.html
- `Comparison table corrections (wind class 6, rotation 0-120, profile 150x85, 33 colours)` --references--> `Naslovnica (index.html)`  [INFERRED]
  docs/PRD-konfigurator.md → index.html
- `187 realizacija renamed to Projekti with real project photos (resolved)` --references--> `Naslovnica (index.html)`  [EXTRACTED]
  docs/PRD-konfigurator.md → index.html
- `Four UX fixes after first client test` --references--> `Naslovnica (index.html)`  [INFERRED]
  docs/PRD-konfigurator.md → index.html
- `Gacka - Sunbreaker 500 project` --references--> `Naslovnica (index.html)`  [EXTRACTED]
  projekti/bioklimatska-pergola-gacka.html → index.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Placeholder podstranice 'Stranica je u pripremi'** — klizne_stijene, sjenila, rolo, jamstveni_uvjeti, uvjeti_koristenja, izjava_o_privatnosti, kolacici [EXTRACTED 1.00]
- **Tijek konfiguratora: model, dimenzije, lokacija, oprema, tip kupca, cijena** — index_configurator, index_location_transport, index_configurator_equipment, index_customer_type_toggle, js_cjenik, js_slanje [EXTRACTED 1.00]
- **Zajednički karusel montažnih videa (isti YouTube ID-ovi) na više stranica** — index_process_video_carousel, sunbreaker_400_installation_video, sunbreaker_500_installation_video, sistem_slide_installation_video [INFERRED 0.95]
- **Generated per-project case-study pages (photo gallery + lightbox)** — projekti_bioklimatska_pergola_bale, projekti_bioklimatska_pergola_berlin, projekti_bioklimatska_pergola_biograd_na_moru_2, projekti_bioklimatska_pergola_biograd_na_moru, projekti_bioklimatska_pergola_brac, projekti_bioklimatska_pergola_brodarica, projekti_bioklimatska_pergola_cakovec, projekti_bioklimatska_pergola_ciovo, projekti_bioklimatska_pergola_crikvenica, projekti_bioklimatska_pergola_daruvar, projekti_bioklimatska_pergola_gacka, projekti_bioklimatska_pergola_grobnik, projekti_bioklimatska_pergola_imotski, projekti_bioklimatska_pergola_ivanic_grad [INFERRED 0.95]
- **Configurator pricing and display rules (discrete dimensions, regions, equipment, discount, VAT, out-of-range)** — docs_prd_konfigurator_discrete_dimensions, docs_prd_konfigurator_price_regions, docs_prd_konfigurator_equipment_pricing, docs_prd_konfigurator_rabat_10, docs_prd_konfigurator_vat_toggle, docs_prd_konfigurator_out_of_range [INFERRED 0.85]
- **PRD phased delivery plan (Faza 1 data fixes, Faza 2 price file, Faza 3 configurator)** — docs_prd_konfigurator_faza_1, docs_prd_konfigurator_faza_2, docs_prd_konfigurator_faza_3 [EXTRACTED 1.00]
- **Sunbreaker 400 realized-project case studies** — projekti_bioklimatska_pergola_kastel_sucurac, projekti_bioklimatska_pergola_korcula, projekti_bioklimatska_pergola_kutina, projekti_bioklimatska_pergola_labin_2, projekti_bioklimatska_pergola_labin, projekti_bioklimatska_pergola_luzani_slavonski_brod, projekti_bioklimatska_pergola_makarska_2, projekti_bioklimatska_pergola_makarska, projekti_bioklimatska_pergola_na_otoku_pagu, projekti_bioklimatska_pergola_opatija, projekti_bioklimatska_pergola_ostakljena, projekti_bioklimatska_pergola_otok_pag, projekti_bioklimatska_pergola_peljesac, projekti_bioklimatska_pergola_pisarovina, projekti_bioklimatska_pergola_porec, projekti_bioklimatska_pergola_pula_2, projekti_bioklimatska_pergola_pula, sunbreaker_400 [EXTRACTED 1.00]
- **Sunbreaker 400 realised-project case studies** — projekti_bioklimatska_pergola_razanj, projekti_bioklimatska_pergola_rovinj, projekti_bioklimatska_pergola_samobor, projekti_bioklimatska_pergola_savudria, projekti_bioklimatska_pergola_savudrija, projekti_bioklimatska_pergola_sb400_crikvenica, projekti_bioklimatska_pergola_sb400_kastel_luksic, projekti_bioklimatska_pergola_sb400_korcula, projekti_bioklimatska_pergola_sb400_krk, projekti_bioklimatska_pergola_sb400_ljubljana, projekti_bioklimatska_pergola_sb400_lumbarda_korcula, projekti_bioklimatska_pergola_sb400_makarska, projekti_bioklimatska_pergola_sb400_maribor, projekti_bioklimatska_pergola_sb400_murter, projekti_bioklimatska_pergola_sb400_peljesac, projekti_bioklimatska_pergola_sb400_porec, projekti_bioklimatska_pergola_sb400_sesvetski_kraljevec, projekti_bioklimatska_pergola_sb400_slavonski_brod_2, sunbreaker_400 [INFERRED 0.95]
- **Sunbreaker 400 realized-project case studies** — projekti_bioklimatska_pergola_sb400_slavonski_brod, projekti_bioklimatska_pergola_sb400_zagreb, projekti_bioklimatska_pergola_sesvetski_kraljevac, projekti_bioklimatska_pergola_slavonija, projekti_bioklimatska_pergola_slavonski_brod, projekti_bioklimatska_pergola_sljeme, projekti_bioklimatska_pergola_slovacka_michalovce, projekti_bioklimatska_pergola_split, projekti_bioklimatska_pergola_vodice, projekti_bioklimatska_pergola_vrbovec, projekti_bioklimatska_pergola_zagreb_2, projekti_bioklimatska_pergola_zagreb, projekti_bioklimatska_pergola_zlarin, sunbreaker_400 [EXTRACTED 1.00]
- **Sunbreaker 500 realized-project case studies** — projekti_bioklimatska_pergola_sb500_cerna, projekti_bioklimatska_pergola_sb500_diamond_vila_korcula, projekti_bioklimatska_pergola_sb500_zaton_kod_sibenika, projekti_bioklimatska_pergola_zaton, sunbreaker_500 [EXTRACTED 1.00]

## Communities (11 total, 0 thin omitted)

### Community 0 - "Naslovnica i projekti"
Cohesion: 0.06
Nodes (67): Naslovnica (index.html), Tri razine premium ponude (kartice SB400, SB500, SB700), Bale, Istra - Sunbreaker 400 project, Berlin - Sunbreaker 400 project, Biograd na Moru - Sunbreaker 400 project, Biograd na Moru (2) - Sunbreaker 400 project, Brač - Sunbreaker 400 project, Brodarica - Sunbreaker 400 project (+59 more)

### Community 1 - "Alati: dohvat projekata i galerija"
Cohesion: 0.08
Nodes (19): dohvati(), glavno(), izvuci_hero_i_galeriju(), basename(), citaj_docx_stupce(), dohvati_referenca_html(), glavno(), izgradi_novu_karticu() (+11 more)

### Community 2 - "Konfigurator i upitni obrasci"
Cohesion: 0.13
Nodes (28): Konfigurator: stvarna cijena iz cjenika (6 tablica SB400/SB500), klizači na stvarne korake, 21 županija u 3 regije, Obrasci stvarno šalju preko Web3Forms (slanje.js) na helpdesk@makeitpro.hr; događaj konfigurator:upit-poslan, Placeholder podstranice izrađene u 3. krugu (sjenila, rolo, pravne stranice, ZIP tende, veranda), Inquiry email via Web3Forms with county, region, on-inquiry items, discount, customer type, Konfigurator okvirne ponude (Model, Dimenzije, Lokacija, Oprema, Cijena), Oprema u konfiguratoru: LED +1.200 EUR, senzor kiše +500 EUR, senzor vjetra +400 EUR; ostalo na upit, Tip kupca: Fizička osoba (cijena s PDV-om) / Pravna osoba (bez PDV-a), Česta pitanja (7 prodajnih pitanja: cijena, razlika u cijeni, dozvola, servis, uživo, održavanje) (+20 more)

### Community 3 - "Pergola Solid i Shutters"
Cohesion: 0.09
Nodes (31): Nalaz: ttgradnja.hr nema opći prodajni FAQ; tehnički FAQ po modelu prebačen na podstranice (Faza 2), Pergola Solid - nakošeni pomični krov od tkanine (pergola-solid.html), 33 RAL/SELT boje + 6 dekora drva uz doplatu (R26, R27, R28, R30, R49, R52), Odvodnja: voda niz tkaninu u prednji oluk, kroz stupove van (krov mora biti potpuno otvoren), Tehnički FAQ Solid (stupovi, odvodnja, daljinski, LED, moduli, neravan teren), Zidna i samostojeća verzija; višemodulna s po jednom vodilicom po modulu, Nakošeni pomični krov od PVC/poliesterske tkanine (Serge Ferrari) na električni pogon, Solid specifikacije: do 4,0 x 7,0 m, visina 2,5 m, greda 165 mm, nagib 5-10 stupnjeva, jamstvo 10/5 god. (+23 more)

### Community 4 - "CHANGELOG i povijest izmjena"
Cohesion: 0.11
Nodes (23): CHANGELOG.md - popis izmjena (Faze 1-10, Otvoreno), Konfigurator vraćen na dvije stalno vidljive kolone (grid 1.15fr/.85fr, sticky desno), Audit konfiguratora naspram PDF upitnika i PRD-konfigurator.md - nije pronađen bug, Hero tekst + CTA grupirani i vertikalno centrirani, 'Pogledajte projekte' kao btn-ghost, Hero video: Faze 8-10 (loop2 -> iz izvornika -> TT-Gradnja-luxury-v15-FULL, CRF 24, 1440x810), Rizik: 40 slika galerije hotlinkano sa stare stranice bioklimatskepergole.hr, Josip - klijent TT Gradnja (potvrđuje brojke, šalje upitnik i fotografije), Stranica na noindex dok klijent ne potvrdi brojke (+15 more)

### Community 5 - "SB400/SB500 i proizvodjac"
Cohesion: 0.12
Nodes (25): Faza 1 ispravci: boje 36->33, vjetar SB400 klasa 6, rotacija 0-120, stup 150x85, servis 72 h, zastupnik od 2018., SELT by Aluprof, Aluprof grupacija: 70+ god., 590 mil. EUR prihoda, 61 zemlja, 2.600 partnera, Usporedba modela SB400 / SB500 / SB700 (tablica specifikacija), SELT by Aluprof - proizvođač, TT Gradnja ovlašteni zastupnik za RH od 2018., TT Gradnja d.o.o. (Slavonski Brod), Otpornost na vjetar klasa 6 (EN 13561, 400 Pa = 40,8 kg/m2), Gacka - Sunbreaker 500 project, Sunbreaker 500 — Petrčane (projekt) (+17 more)

### Community 6 - "Izrada cjenika (Python)"
Cohesion: 0.12
Nodes (9): izbaci_stupce(), izgradi(), nadji_izvor(), nadji_zaglavlje(), normaliziraj_blok(), odsijeci_prazne_stupce(), provjeri(), ucitaj_postojeci_cjenik() (+1 more)

### Community 7 - "PRD konfiguratora"
Cohesion: 0.12
Nodes (16): PRD: Konfigurator cijene i ispravci podataka, konfigurator:upit-poslan custom event (ads tracking hook), Client answers blocking Phase 3 (Josip, 8.9.2026), Configurator flow (model, dimensions, location, equipment, contact), Equipment pricing: LED 1200, rain sensor 500, wind sensor 400; rest 'na upit', FAZA 2: Cjenik kao podatkovna datoteka, FAZA 3: Konfigurator, Konfigurator cijene (price configurator) (+8 more)

### Community 8 - "Sunbreaker 700"
Cohesion: 0.18
Nodes (14): Tarasola Technic View Pro preimenovan u Sunbreaker 700 na svim stranicama, Comparison table corrections (wind class 6, rotation 0-120, profile 150x85, 33 colours), FAZA 1: Ispravci potvrđenih podataka, Rename Tarasola Technic View Pro to Sunbreaker 700, Traka prednosti: 2-4 tjedna isporuka, 10 god. jamstva, +200 km/h, 33 boje, Sunbreaker 700 - ultra-premium s integriranim ZIP sjenilom (sunbreaker-700.html), Tehnički FAQ SB700 (snijeg, cijela godina, rotacija, pametni dom, bočni zatvarači), Izvedbe: Pavilion (samostojeća), Gardena (zidna okomito/paralelno), Tende (bez stupova) (+6 more)

### Community 9 - "Vertoline"
Cohesion: 0.31
Nodes (9): Vertoline page, Vertoline colour palette (33 Aluprof colours + 6 wood decors; MAT/SATIN/STR), Vertoline compatibility (SB350, SB400, SB450, SB550), Vertoline modular expansion by adding panels, Vertoline module composition (5 profiles 40x50 mm, 60 mm spacing), Vertoline fastening (ground base + upper pergola frame), Vertoline technical specifications (Aluprof data), Vertoline vertical decorative profile system (+1 more)

### Community 10 - "Montazni videi i proces"
Cohesion: 0.29
Nodes (6): Karusel montažnih videa: 3 videa (dkhpdibODX8, WGlWvsD9phg, APwpL-y8fz4), centar uvećan, fiksna visina, Proces suradnje u 5 koraka (upit 24h, izlazak i 3D, fiksna ponuda 30 dana, proizvodnja 2-4 tjedna, montaža 1-2 dana), Montažni videi (Hotel Sumratin Dubrovnik) uz Sistem Slide u praksi, Montažni videi (Hotel Sumratin Dubrovnik: rooftop i prizemlje), Montažni videi (Hotel Sumratin Dubrovnik: rooftop i prizemlje), Obećani proces: poziv u 24h, izlazak na teren u 2 radna dana, 3D vizualizacija, fiksna ponuda 30 dana

## Ambiguous Edges - Review These
- `Sunbreaker 500 - srednji model (sunbreaker-500.html)` → `Usporedba modela SB400 / SB500 / SB700 (tablica specifikacija)`  [AMBIGUOUS]
  index.html · relation: conceptually_related_to
- `Sunbreaker 700 - ultra-premium s integriranim ZIP sjenilom (sunbreaker-700.html)` → `Traka prednosti: 2-4 tjedna isporuka, 10 god. jamstva, +200 km/h, 33 boje`  [AMBIGUOUS]
  index.html · relation: conceptually_related_to
- `Konfigurator okvirne ponude (Model, Dimenzije, Lokacija, Oprema, Cijena)` → `Obećanja o vremenu odgovora (2 radna dana / danas do 18 h / prosjek 3 h 20 min)`  [AMBIGUOUS]
  upit.html · relation: conceptually_related_to
- `Jamstvo i sigurnost kupnje (10 god. konstrukcija, 5 god. motori, 2 god. elektronika, 0 EUR razlike, servis 72 h)` → `SB400 specifikacije: do 4,0 x 7,0 m, visina 2,8 m, greda 212x85, stup 150x85, klasa vjetra 6, 33 boje, Inox A4, jamstvo 10/5 god.`  [AMBIGUOUS]
  sunbreaker-400.html · relation: conceptually_related_to
- `Karusel Google recenzija (3 vidljive, ručno listanje strelicama, podaci iz recenzije.js)` → `Strukturirani podaci JSON-LD (LocalBusiness, Product SB500, FAQPage)`  [AMBIGUOUS]
  index.html · relation: conceptually_related_to

## Knowledge Gaps
- **27 isolated node(s):** `Lokacija (županija) -> regija -> transport i montaža iz Slavonskog Broda`, `Motor i pogon unutar grede s revizijskim otvorom`, `Nožice: podesiva (niveliranje do 50 mm), poravnata (nevidljivo usidrenje), nožica E s centralnim odvodom DN50`, `Pregled sustava i presjeci profila (lamela 216x40, greda 212x85, stup 150x85 mm)`, `Krovni modul s okvirom bez stupova: samostalni ili linearno povezani duž uzdužnih i poprečnih greda` (+22 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 60 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Sunbreaker 500 - srednji model (sunbreaker-500.html)` and `Usporedba modela SB400 / SB500 / SB700 (tablica specifikacija)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Sunbreaker 700 - ultra-premium s integriranim ZIP sjenilom (sunbreaker-700.html)` and `Traka prednosti: 2-4 tjedna isporuka, 10 god. jamstva, +200 km/h, 33 boje`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Konfigurator okvirne ponude (Model, Dimenzije, Lokacija, Oprema, Cijena)` and `Obećanja o vremenu odgovora (2 radna dana / danas do 18 h / prosjek 3 h 20 min)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Jamstvo i sigurnost kupnje (10 god. konstrukcija, 5 god. motori, 2 god. elektronika, 0 EUR razlike, servis 72 h)` and `SB400 specifikacije: do 4,0 x 7,0 m, visina 2,8 m, greda 212x85, stup 150x85, klasa vjetra 6, 33 boje, Inox A4, jamstvo 10/5 god.`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Karusel Google recenzija (3 vidljive, ručno listanje strelicama, podaci iz recenzije.js)` and `Strukturirani podaci JSON-LD (LocalBusiness, Product SB500, FAQPage)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Naslovnica (index.html)` connect `Naslovnica i projekti` to `Konfigurator i upitni obrasci`, `Pergola Solid i Shutters`, `CHANGELOG i povijest izmjena`, `SB400/SB500 i proizvodjac`, `PRD konfiguratora`, `Sunbreaker 700`, `Vertoline`, `Montazni videi i proces`?**
  _High betweenness centrality (0.411) - this node is a cross-community bridge._
- **Why does `FAZA 2: Cjenik kao podatkovna datoteka` connect `PRD konfiguratora` to `Konfigurator i upitni obrasci`, `Izrada cjenika (Python)`?**
  _High betweenness centrality (0.338) - this node is a cross-community bridge._