# Popis izmjena — bioklimatske pergole (TT Gradnja)

Repozitorij `iMakeITpro/bioklimatske-pergole`, grana `iteracija-2`.
Najnovije je na vrhu.

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
| Stvarne Google recenzije umjesto izmišljenih imena i ocjene 4,9/87 | Josip |
| Potvrda tvrdnje „najbrže u premium segmentu" | Josip |
| Brojke iz SELT deklaracije: 130 km/h, 200 kg/m² | Josip |
| Je li „500R" iz zapisnika isti model kao „Sunbreaker 500" | Josip |
| Tekst oznaka u interaktivnom prikazu — iz SELT tehničkog lista | Josip |
| Sadržaj podstranica — tehnički listovi, presjeci, odvodnja, galerije, snimke montaže | Faza 2 |
| Skraćivanje usporedne tablice i galerije na naslovnoj (zapisnik t. 7) | Faza 2 |
| Uklanjanje `noindex` prije objave | nakon potvrde brojki |
| Preklopnik „Tip kupca" ne mijenja glavni prikazani iznos i odabir ne stiže Josipu u e-mail — treba preimenovati u Fizička/Pravna osoba, premjestiti u obrazac prije slanja i za pravnu osobu automatski prikazati cijenu bez PDV-a | u radu, iduća sesija |
| „187 realizacija" → „Projekti"; usporediti trenutnih 8 kartica sa stvarnim portfolijem na bioklimatskepergole.hr/reference/ | u radu, iduća sesija |
