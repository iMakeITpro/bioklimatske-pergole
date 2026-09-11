# Popis izmjena — bioklimatske pergole (TT Gradnja)

Repozitorij `iMakeITpro/bioklimatske-pergole`, grana `iteracija-2`.
Najnovije je na vrhu.

---

## 11. rujna 2026. — Faza 6, dopuna

**Recenzije — dva tekstualna ispravka nakon pregleda**

- Eyebrow „Što kažu vlasnici" → „Naši zadovoljni klijenti" (Toni, 11.9.2026.)
- Uklonjena rečenica „Stvarne recenzije s Google Business profila TT Gradnja d.o.o., Slavonski Brod." ispod ocjene 4,8/5 — Toni je primijetio da zvuči neuvjerljivo/ironično, kao da se opravdava da su recenzije stvarne. Ocjena i tri kartice ispod sad stoje bez dodatnog objašnjenja
- Napomena zapisana ovdje jer je relevantna za oboje: Toni je pitao mijenja li se Google ocjena s vremenom — da, mijenja se (nove recenzije, eventualno uklonjene). Trenutnih 4,8/5 iz 31 recenzije je snimka od 10.9.2026., upisana ručno u `recenzije.js`, `index.html` (h2 i JSON-LD) i footer. Vidi novu stavku u "Otvoreno" ispod

## 10. rujna 2026. — Faza 6

**Recenzije — stvarni Google podaci umjesto izmišljenih**

- Naslovnica je do sada prikazivala tri izmišljene recenzije (Marin Kovačević, Ivana Perić, Damir Tomić) i izmišljenu ocjenu 4,9/5 iz 87 recenzija — hardkodirano u `index.html`, sekcija „Što kažu vlasnici"
- Dohvaćeni stvarni podaci izravno s Google Business profila (maps.google.com, pretraga „TT Gradnja d.o.o. Slavonski Brod"): **4,8/5, 31 recenzija**. Ažurirano svugdje gdje se broj pojavljivao — h2 naslov sekcije, footer na svih 13 stranica koje ga dijele, i `aggregateRating` u JSON-LD (LocalBusiness i Product)
- Tri izmišljene recenzije zamijenjene trima stvarnim, ručno prepisanim izvornim hrvatskim tekstom (ne Googleov prijevod): Manuela Matić i Anita Marković (obje izrijekom o bioklimatskoj pergoli), i Vladimir Jurić (dugogodišnji kupac stolarije, pergola mu je sljedeći planirani projekt). Uklonjeni izmišljeni detalji koji se ne mogu potvrditi (lokacija kupca, model, brzina bure, iznos investicije) — Google recenzije ne otkrivaju te podatke, pa "lead" rečenica iznad kartica više ne tvrdi da je svaka recenzija povezana s projektom iz galerije
- Toni je zatražio da popis bude lako uredljiv bez diranja `index.html`, po uzoru na `cjenik.js`, i da se po mogućnosti automatski ažurira s Googlea. Istraženo: postoje treće-strane widgeti (npr. EmbedSocial, Tagembed) koji mogu automatski povlačiti Google recenzije bez backend-a, ali zahtijevaju da vlasnik poslovnog Google profila osobno autorizira spajanje (OAuth) preko njihovog sučelja — to ne mogu napraviti u ime korisnika, a i free planovi obično nose vanjski branding/watermark i ograničenje na svega nekoliko najnovijih recenzija. Zaključak: **odvojena podatkovna datoteka** (opcija koju je Toni odobrio kao zamjenu ako automatika nije izvediva)
- Novo: `recenzije.js` — sadrži 4 stvarne, provjerene recenzije (prikazuju se prve 3 iz niza); Josip/Toni mogu dodati novu ili promijeniti poredak bez diranja `index.html`. U datoteci je upisan i kratki postupak "kako dodati novu recenziju"
- `index.html`: statični blok triju kartica zamijenjen praznim kontejnerom koji se puni iz `recenzije.js` (inline skripta na istom mjestu u dokumentu, izvršava se prije `IntersectionObserver` postavljanja za "reveal" animaciju, pa animacija radi identično kao prije)
- Napomena: zbog vremenskog pritiska (Toni je morao otići usred sesije) izmjena nije provjerena na 360/390/768px kroz preglednik kao inače — tekst novih recenzija je slične dužine kao stari, a CSS grid (`.revs`) je već testiran u Fazi 5, ali vizualnu provjeru vrijedi napraviti prije objave
- Preostalih 27 Google recenzija (od ukupno 31) nije prepisano — dovoljno je bilo tri/četiri najrelevantnije za pergolu; puni popis je dostupan na Google profilu ako zatreba više

## 10. rujna 2026. — Faza 5, prvi dio

**Jamstva — pet novih tvrdnji o povjerenju**

- Dodan novi kompaktan red ispod postojećih 9 kartica u sekciji „Jamstvo i sigurnost kupnje" (eyebrow „Još razloga za povjerenje" — namjerno bez riječi „zašto", da se ne ponavlja s naslovom sekcije "Zašto odabrati naš premium proizvod"): izravno iz tvornice, proizvodnja po EU standardima, 40+ godina iskustva (SELT/Aluprof), izgled nepromijenjen nakon 10 godina, i kompletan proizvod u jednoj kompaniji (istaknuto kao jedinstvena prednost na tržištu, zauzima cijeli red)
- Provjereno naspram punog teksta upitnika (ne samo sažetka u pripremnoj bilješci): odjeljak „6. Jamstva" u dokumentu nema zaseban „Vaš odgovor" — Josip je svojih 5 novih tvrdnji upisao izravno u popis postojećih, kao odgovor na pitanje „Postoji li još nešto što kupca uvjerava, a ovdje ne piše?". To je **dodavanje**, ne zamjena — svih 6 „trenutnih" stavki iz upitnika (10 god., 0 €, 72h, SELT/Aluprof zastupnik, poslovanje od 2018., HR/SI/DE) već postoji na stranici (s ispravkama iz Faze 1). Nijedna postojeća kartica nije uklonjena niti bi trebala biti
- Novi stil `.trustlist`/`.ti` u `styles.css` — lakši od `.gc` kartica (bez velikog broja, kvačica + naslov + kratak opis), 2 stupca na desktopu, 1 stupac ispod 1024px isto kao `.gcols`. Zadržana pozadina sekcije (`alt`/krem) — ritam susjednih pozadina nije mijenjan
- Tekst preuzet iz Josipovog upitnika (MIP-002-UP-2026-001); stilizirano radi dužine, značenje nepromijenjeno — Josip je već najavio da će tekst doraditi u završnoj fazi
- `styles.css` v18 → v19, podignuto na svih 13 stranica koje ga dijele
- Provjereno na 360, 390 i 768px (Playwright) — bez horizontalnog scrolla

**FAQ — nalaz umjesto implementacije**

- ttgradnja.hr **nema** opći prodajni FAQ (cijena/usporedba/dozvola/rok/servis/plaćanje) kakav je Josip u upitniku implicirao da postoji za preuzimanje. Ono što tamo stvarno postoji je tehnički FAQ **po modelu** (SB400, SB500, Pergola Solid — pitanja o dimenzijama, bojama, odvodnji, daljinskom upravljaču, opterećenju snijegom/vjetrom), na zasebnim stranicama modela
- Odluka (Toni, 10.9.2026.): trenutnih 7 prodajnih pitanja na naslovnici ostaje bez izmjene — nisu pokrivena onim što na ttgradnja.hr postoji. Tehnički FAQ po modelu prebacuje se u Fazu 2, na placeholder podstranice `sunbreaker-400.html` / `sunbreaker-500.html` / `sunbreaker-700.html`, kad se radi sadržaj podstranica
- Nema izmjena koda za ovaj dio — samo nalaz i odluka, zapisano ovdje i u „Otvoreno"

## 9. rujna 2026. — osmi krug

**Konfigurator — Tip kupca**

- Preklopnik privatni/poslovni preimenovan u „Fizička osoba" / „Pravna osoba" i premješten iz rezultata u obrazac, prije slanja upita — dosad odabir nije mijenjao glavni prikazani iznos i nije stizao Josipu u e-mail
- Za pravnu osobu se odmah prikazuje cijena bez PDV-a, uz oznaku „Pravna osoba · cijena bez PDV-a" uz naslov ponude; za fizičku osobu ostaje cijena s PDV-om kao dosad
- Uklonjen pravokutni obrub oko preklopnika koji je izgledao kao da stoji u tablici

**Konfigurator — klizači i navigacija**

- Klizači za dubinu i širinu sad klize glatko pod prstom/kursorom umjesto skakanja između par zaustavnih točaka (npr. 2,5 m → 3 m → 3,5 m) — vrijednost i cijena i dalje se računaju na najbližu stvarnu točku iz cjenika, tipkovnica radi kao prije
- Gumb „Natrag na opremu" premješten s vrha na dno ploče s cijenom, u istom stilu kao „Natrag"/„Dalje" na ostalim koracima

**Konfigurator — Lokacija (županija)**

- Padajući popis županija je na Windows Chrome/Edge znao prikazati ogroman, gotovo prazan okvir s tek pokojim vidljivim nazivom — nije bio problem keširanja (provjereno uz potpuno brisanje keša i drugi preglednik), nego kako sam Windows crta taj popis. Popis je zamijenjen vlastitim, koji stranica sama iscrtava — i dalje grupiran po regijama, isti tamni izgled, radi na dodir i tipkovnicu (strelice, Home/End, Enter, Esc, upisivanje slova za skok na naziv)
- U raščlambi cijene retku „Transport i montaža — Od Splita do Dubrovnika" (naziv cjenovne regije) zamijenio naziv stvarno odabrane županije, npr. „Transport i montaža — Splitsko-dalmatinska" — dosad je tekst zvučao kao da se doprema baš iz Splita u Dubrovnik

**Naslovnica — Projekti**

- „Pogledajte 187 realizacija" u uvodnoj poveznici promijenjeno u „Pogledajte projekte" (ostatak teksta koji spominje 187 namjerno zasad nepromijenjen, po dogovoru)
- Tri kartice u galeriji ispravljene prema stvarnom portfoliju na bioklimatskepergole.hr/reference/: Murter SB500 → SB400; kartica pogrešno označena „Zadar" zapravo je Krk; kartica pogrešno označena „Rovinj" zapravo je Pelješac

**Sadržaj**

- Naslov „Zašto je premium investicija kod nas manje rizična" promijenjen u „Zašto odabrati naš premium proizvod"; riječ „premium" u tom naslovu i u „Tri razine premium ponude" sad je u istoj bakreno-zlatnoj boji kao i ostali zlatni naglasci na stranici

**Mobitel**

- Lebdeća traka za poziv/izračun pri dnu ekrana više ne preklapa gumb „Dalje" unutar koraka konfiguratora — sklanja se dok je konfigurator u fokusu, isto kao i dok je vidljiv početni dio stranice

**Klijentov pregled**

- Pripremljen prijedlog: `main` grana ostaje čist, ručno objavljen snimak za Josipa (bez svakog pojedinog commita), `iteracija-2` ostaje radna grana s punom poviješću — čeka primjenu i provjeru GitHub Pages postavke izvora (vidi Otvoreno)

**Tehnički**

- Podignuta oznaka verzije CSS datoteke (`styles.css?v=17` → `v=18`) na svih 13 stranica — v=17 je stajao nepromijenjen kroz nekoliko rundi izmjena, pa su preglednici mogli servirati stari kešani izgled

---

## 9. rujna 2026. — sedmi krug

**Konfigurator — 4 ispravka nakon prvog testiranja uživo**

- Gumb „Natrag" na koraku Dimenzije i „Natrag na opremu" na koraku Cijena bili su skoro nevidljivi — tamni tekst na tamnoj podlozi, naslijeđen s tijela stranice. Sada su bijeli, s vidljivim rubom, i dobili su jedinstven zlatni prsten pri tabulatoru umjesto zadanog plavog obruba preglednika
- Klizači za dubinu i širinu imaju samo 3–6 stvarnih zaustavnih točaka, pa je povlačenje zahtijevalo veliki pomak prsta prije skoka na sljedeću vrijednost. Sada svaki pomak od 12 piksela odmah skoči na sljedeću/prethodnu stvarnu vrijednost, u oba smjera — tipkovnica radi kao prije
- Otkljucana cijena se više ne mijenja tiho kad se korisnik vrati i promijeni model, dimenzije, županiju ili opremu — vraća na obrazac s porukom „Promijenili ste konfiguraciju od zadnjeg upita", tako da svaka izmjena traži novi upit umjesto da stara cijena samo nestane bez objašnjenja. Kontakt podaci ostaju popunjeni, treba samo ponovno kliknuti gumb. Prebacivanje privatni/poslovni ne broji se kao izmjena konfiguracije i ostaje živo
- Drugi gumb „Zatraži točnu ponudu" ispod okvirne cijene je uklonjen — bio je suvišan uz „Prikaži okvirnu ponudu" koji već otključava cijenu. Umjesto njega stoji poruka „Hvala na interesu! Vaš upit je zaprimljen — naš stručnjak će vam se javiti u roku 3–4 dana s ponudom."

**Tehnički**

- Nakon svakog uspješnog slanja upita stranica sada odašilje jedan dokumentiran signal (`konfigurator:upit-poslan`) — mjesto na koje se kasnije zakvači eventualno praćenje oglasa, bez diranja konfiguratora
- Nova specifikacija `PRD-konfigurator.md` — tijek, izračun i zapisnik klijentovih odgovora, referenca za sve buduće izmjene konfiguratora

---

## 8. rujna 2026. — šesti krug

**Konfigurator — stvarna cijena umjesto izmišljene**

- Konfigurator sada radi u pravom tijeku **Model → Dimenzije → Lokacija → Oprema → Cijena**, s brojčanim koracima i indikatorom napretka — dosad je cijena bila izmišljena procjena po m², bez stvarnog cjenika
- Cijena dolazi isključivo iz stvarnog proizvodnog cjenika (6 tablica: 3× SB400 + 3× SB500), učitanog kao `cjenik.js`. Svaka vrijednost provjerena nasumičnim uzorkom od 24 ćelije protiv izvornog Excela — nema izmišljenih formula ni marži
- Klizači za dubinu i širinu ograničeni na točno one korake koje proizvodni cjenik pokriva (npr. SB400 dubina 3,4–7 m po 20 cm) — nema pozicije klizača koja ne postoji u tablici; izvan raspona nema cijene, nego poziv na kontakt
- Lokacija (županija) određuje regiju i transport — sve 21 hrvatska jedinica mapirana u tri regije bez preklapanja
- Popust od 10 % za upit putem konfiguratora prikazuje se kao zasebna stavka, nikad kao precrtana cijena
- Preklopnik privatni/poslovni kupac — privatni prikazuje cijenu s PDV-om (zakonska obveza), poslovni bez PDV-a i PDV zasebno
- Rezultat (cijena i kontakt obrazac) više se ne prikazuje stalno pored koraka 1–4, nego tek kad se stvarno dođe do kraja — peti korak preimenovan iz „Kontakt" u „Cijenu"

**Podaci na stranici (Faza 1 — ispravci potvrđenih podataka)**

- Boje u osnovnoj cijeni: 36 → 33
- Vjetar SB400: klase 3 → 6
- Rotacija lamela SB400/SB500: 0–135° → 0–120°
- Profil stupa SB400: 120×120 → 150×85 mm
- Servis: „u roku 48 h" → „u prosjeku unutar 72 h"
- Zastupnik/poslovanje od: 2016. → 2018.
- Naziv proizvođača posvuda: „ovlašteni SELT zastupnik" → „SELT by Aluprof" (Aluprof je kupio SELT, nije riječ o dva ravnopravna partnera); dodana nova sekcija s tri brojke o Aluprof grupaciji (70+ god. iskustva, 590 mil. € prihoda, 61 zemlja / 6 kontinenata / 2.600 partnera)
- Proces: korak 1 „isti dan" → „unutar 2 radna dana"; korak 2 „5 radnih dana" → „unutar 3 radna dana od prihvaćanja ponude"; korak 5 montaža „1–3 dana" → „1–2 dana"
- Usporedna tablica modela: uklonjeni redovi nosivost snijega i uvlačive lamele; dodani profil konstrukcije, integrirani ZIP i rok proizvodnje
- „Tarasola Technic View Pro" preimenovan u „Sunbreaker 700" na svih 14 stranica (izbornik, kartice, tablica, structured data)
- Uklonjene marketinške tvrdnje ovisne o staroj, pogrešnoj klasi vjetra SB400 („četverostruka razlika", „pojačana konstrukcija klase 6") — zamijenjene stvarnim razlikama (veći raspon, marinski inox vijci)

**Fotografije**

- Kartice SB400, SB500 i SB700 dobile stvarne fotografije umjesto starih vanjskih WP poveznica i placeholder Tarasola slike
- Podstranica Sunbreaker 400 dobila naslovnu fotografiju — prije nije imala nikakav medijski sadržaj
- Podstranica Sunbreaker 500: fotografija u interaktivnom prikazu zamijenjena, 5 oznaka repozicionirano prema novoj slici
- Podstranica Sunbreaker 700 dobila naslovnu fotografiju

**Podstranica SB400**

- Preneseno 15 tehničkih pitanja i odgovora (širina, rotacija lamela, boje, LED, odvodnja, snijeg...) u novu FAQ sekciju
- Na naslovnoj, u odjeljku Proces, dodan video montaže — učitava se tek na klik, ne odmah sa stranicom

---

## 6. rujna 2026. — peti krug

- Nazivi sekcija „Projekti" i „Modeli" u izborniku skraćeni

---

## 6. rujna 2026. — četvrti krug

**Redoslijed sekcija**

- Sekcija o jamstvima premještena **ispred recenzija** — čovjek prvo dobije razloge zašto je investicija sigurna, pa tek onda tuđe riječi kao potvrdu
- Presložen ritam pozadina da tamna sekcija ne padne ispod tamne: proces (tamno) → jamstva (krem) → recenzije (svijetlo) → pitanja (krem) → podnožje (tamno). Nijedne dvije susjedne sekcije više nemaju istu pozadinu
- Kartice jamstava prilagođene svijetloj podlozi — bijela ispuna, tamniji obrub i tamnija mjed za velike brojke. Kontrast provjeren: brojka 5,8:1, naslov 19:1, tekst 5,9:1 (prag 4,5:1). Iste kartice i dalje rade na tamnoj podlozi, ako ih negdje vratimo

**Obrasci**

- **Oba obrasca sada stvarno šalju** — konfigurator i stranica upita, preko Web3Formsa na `helpdesk@makeitpro.hr`. Dosad su samo ispisivali „Upit zaprimljen" bez obzira na sve, a nijedan podatak nigdje nije odlazio
- Konfigurator uz kontakt podatke šalje i cijelu konfiguraciju: model, tip montaže, dimenzije, površinu, odabranu opremu i izračunatu okvirnu ponudu. U mailu se odmah vidi što je čovjek slagao
- Cijena se korisniku prikazuje odmah, slanje ide u pozadini da ne čeka mrežu. Ako slanje padne, ispod cijene se pojavi napomena s telefonom
- Poruka o uspjehu više ne laže: ako slanje ne uspije, obrazac to kaže i nudi telefon i e-mail
- Ključ stoji u dijeljenoj datoteci `slanje.js`, na jednom mjestu za oba obrasca — zamjena na Josipovu adresu je izmjena jedne linije

**Podstranice modela**

- Podstranica Sunbreaker 500 dobila **interaktivni prikaz konstrukcije** — pet oznaka na fotografiji, klik otvara detalj o tom dijelu: rotirajuće lamele, nosiva greda, stup s odvodnjom, plastifikacija, statika i temeljenje
- Na desktopu se detalj otvara kao oblačić uz oznaku, a oblačić se sam prebacuje na lijevu stranu kad je oznaka u desnoj polovici fotografije. Na mobitelu se otvara u panelu ispod fotografije, jer bi oblačić iskakao izvan ekrana
- Oznake su pravi gumbi veličine 44px, dostupni tipkovnicom, zatvaraju se tipkom Escape ili klikom izvan
- **Tekst oznaka je privremen** i zamjenjuje se vrijednostima iz SELT tehničkog lista
- Pregledane sve fotografije s klijentove stranice. Dvije koje koristimo na karticama nisu prikladne za ovakav prikaz: na jednoj je pergola uz sam rub i odrezana, na drugoj zauzima petinu kadra. Uzeta je fotografija iz galerije referenci na kojoj je cijela konstrukcija u tročetvrtinskom pogledu
- **Otvoreno:** nazivi datoteka su generički, pa Josip mora potvrditi koja fotografija prikazuje koji model prije nego prikaz ide na obje podstranice

---

## 5. rujna 2026. — treći krug

**Hero**

- **Novi hero isječak bez ljudi** — na traženje kolege. Iz pune snimke montaže uzet je kadar od 153. do 157. sekunde, gdje kamera kreće ispod krova od lamela i otvara se prema fasadi. Petlja ide naprijed pa unatrag, pa nema vidljivog reza pri ponavljanju. Prethodni isječak počinjao je prerano i hvatao montera u kadru
- Video se sada vrti **i na mobitelu**, iz manje datoteke (960px, 1,1 MB umjesto 2,2 MB). Poster i dalje nosi prvi prikaz, video se dohvaća tek nakon iscrtavanja stranice
- Provjeren kontrast bijelog naslova preko novog kadra: 7,5:1 u najsvjetlijoj točki, 9,8:1 u prosjeku (prag za velike naslove je 3:1)
- Uklonjen odlomak „Konfigurirajte pergolu u 60 sekundi…"
- Uklonjen donji red s podacima „Cijena odmah nakon konfiguratora · Ponuda u 3–4 dana · RH · SI · DE"
- Naslov drži gornji rub, gumb donji — video dobiva sredinu kadra
- Poveznica „Pogledajte 187 realizacija" ostala bez podvlake i strelice; na desktopu stoji pored glavnog gumba, na mobitelu centrirana ispod njega
- Gumb „Izračunajte cijenu" na mobitelu je bez strelice i s centriranim tekstom u pravokutniku
- Uveden `CHANGELOG.md` — ovaj dokument, s cijelom poviješću izmjena i popisom otvorenih stavki

**Navigacija i struktura**

- Uklonjena crna traka na vrhu s ocjenom i brojem recenzija
- Uklonjen gumb „Besplatna procjena" iz zaglavlja — konfigurator je jedini poziv na akciju u prvom ekranu
- „Cijene" preimenovano u „Ponuda", jer sekcija više ne prikazuje cijene
- „Reference" preimenovano u „Projekti"
- „Modeli" dobili padajući izbornik sa sedam podstranica
- Izrađeno jedanaest podstranica kao placeholderi: SB400, SB500, Tarasola, sjenila, ZIP tende, rolo, veranda, jamstveni uvjeti, uvjeti korištenja, izjava o privatnosti, kolačići
- Sve mrtve poveznice povezane — nema više nijednog `href="#"`; e-mail otvara poštanski program
- Naslovi kartica postali poveznice na podstranice; podstranice proizvoda otvaraju se u novoj kartici

**Kartice ponude**

- Sva tri gumba dobila isti stil; SB500 je već ispunjen bojom koju druga dva dobiju na prijelaz mišem, a on tada samo potamni
- Značka „Najčešći izbor" premještena na sliku i podignuta iznad nje — prije je nestajala na prijelaz mišem
- Gumbi na svijetlim karticama dobili vidljiv prijelaz; ranije je bio bijela prozirnost na bijeloj podlozi, dakle nevidljiv

**Sadržaj**

- Uklonjen izvedeni rok „4–6 tjedana od upita do montaže" — ostaje samo Josipovih potvrđenih 2–4 tjedna
- Traka s prednostima skraćena: „isporuka" umjesto „isporuka — najbrže u premium segmentu"; superlativ premješten u odgovor na pitanje o roku, gdje stoji uz objašnjenje
- Iz strukturiranih podataka uklonjen blok s rasponom cijena koji je ostao od prije

**Mobitel**

- Lebdeća traka „Nazovi / Izračunaj cijenu" pojavljuje se tek nakon hera — prije se udvajala s gumbom u herou
- Traka s cijenom u konfiguratoru pojavljuje se tek kad je cijena otključana; prije je pisala „Nakon upita" i lijepila se pod zaglavlje
- Stranica se više ne otvara na konfiguratoru — sidro se briše iz adrese nakon skoka
- Sve dodirne mete sada su preko 44px na 360, 390 i 768px; poveznice u podnožju bile su visoke 17px
- Logotip više ne prelama u dva reda
- Visina hera koristi `svh` umjesto `vh`, pa ne skače kad se skriva adresna traka

**Tehnički**

- `styles.css`, hero video i poster dobili oznaku verzije — bez toga preglednik nakon pusha služi staru kopiju datoteke jer joj se ime nije promijenilo, pa se izmjene ne vide. Vrijedi za svaku datoteku koja se zamijeni na istom imenu
- Padajući izbornik dobio nevidljivi most preko praznine i odgodu zatvaranja od 280 ms; prije je nestajao prije nego što se stigne kliknuti stavku
- Uvedena lokalna test-stranica koja učitava naslovnu u tri okvira širine 360, 390 i 768px. Sve mjere u ovom popisu — dodirne mete, horizontalni scroll, veličine fonta, kontrast — izmjerene su na njoj prije objave, ne procijenjene

---

## 5. rujna 2026. — drugi krug

- Hero dobio video u pozadini; poster se učitava odmah, video tek nakon iscrtavanja radi brzine
- Hero presložen u jedan lijevi stupac, uklonjen odlomak koji je ponavljao brojke iz trake ispod
- Fiksne cijene uklonjene sa svih javnih mjesta — naslova, opisa, kartica, usporedne tablice i FAQ-a
- Konfigurator radi u dva koraka: cijena se otključava tek nakon imena, prezimena, e-maila i telefona, i prikazuje se odmah
- Kartice SB400 i SB500 dobile fotografije
- SB500 Diamond zamijenjen s Tarasola Technic View Pro — cijena na upit, bez konfiguratora
- Rok isporuke usklađen na 2–4 tjedna na svim mjestima
- Dodano „36 boja u osnovnoj cijeni"; riješena ranija kontradikcija s doplatom za RAL
- Traka ispod hera nosi prednosti: 2–4 tjedna · 10 god. · 130 km/h · 36 boja
- Forma za upit preseljena na zasebnu stranicu `upit.html`
- CSS izdvojen u `styles.css` koji dijele sve stranice
- Stranica postavljena na `noindex` dok klijent ne potvrdi brojke

---

## Kolovoz 2026. — prvi krug

- Uklonjena fraza „ključ u ruke" sa svih sedam mjesta na stranici
- Puna mobilna prilagodba: provjera na 360, 390 i 768px, bez horizontalnog scrolla, polja forme na 16px zbog iOS zumiranja
- Sticky prikaz cijene u konfiguratoru na mobitelu
- Izrađena i druga vizualna verzija u klijentovoj paleti (navy `#49566F`, tirkiz `#59C2AA`, krem `#FFFAF4`), s provjerom kontrasta na svih 80 kombinacija teksta i pozadine
- `.gitignore` proširen — klijentski PDF-ovi, veliki videi i radne kopije ne mogu na javni repozitorij

---

## Otvoreno

| Stavka | Čeka |
|---|---|
| Prebacivanje primatelja obrazaca s helpdesk@makeitpro.hr na Josipovu adresu | nakon testiranja |
| Osvježiti ocjenu/broj Google recenzija (trenutno 4,8/31, snimka od 10.9.2026.) — provjeriti na Google Mapsu i ažurirati `recenzije.js` + h2 + footer + JSON-LD ako se promijenilo | povremeno, npr. svaka 2-3 mjeseca |
| Potvrda tvrdnje „najbrže u premium segmentu" | Josip |
| Brojke iz SELT deklaracije: 130 km/h, 200 kg/m² | Josip |
| Tekst oznaka u interaktivnom prikazu — iz SELT tehničkog lista | Josip |
| Sadržaj podstranica — tehnički listovi, presjeci, odvodnja, galerije, snimke montaže | Faza 2 |
| Skraćivanje usporedne tablice i galerije na naslovnoj (zapisnik t. 7) | Faza 2 |
| Uklanjanje `noindex` prije objave | nakon potvrde brojki |
| Primjena squash-merge snimka na `main` granu (čist prikaz za Josipa) i provjera/promjena izvorne grane za GitHub Pages u postavkama repozitorija | Toni |
| Fotografije po modelu (SB400/SB500/SB700, imenovane po modelu) preko drive linka | Josip |
| Je li popis dodatne opreme (LED, senzori, ZIP, staklene stijenke, IR grijalice...) kompletan i koje su konačne cijene | Josip |
| **Faza 2** — Sadržaj podstranica modela: prenijeti tehnički FAQ po modelu (dimenzije, boje, odvodnja, daljinski, snijeg/vjetar) s ttgradnja.hr na `sunbreaker-400.html` / `-500.html` / `-700.html` | Faza 2 |
