# Popis izmjena — bioklimatske pergole (TT Gradnja)

Repozitorij `iMakeITpro/bioklimatske-pergole`, grana `iteracija-2`.
Najnovije je na vrhu.

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

- `styles.css` dobio oznaku verzije — bez toga su preglednici nakon pusha služili staru kopiju stila, pa se izmjene nisu vidjele
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
| Cijene u konfiguratoru su izmišljene — treba stvarna kalkulacija | Josip |
| Obrasci ne šalju nikamo — treba ključ s web3forms.com | Antonio |
| Stvarne Google recenzije umjesto izmišljenih imena i ocjene 4,9/87 | Josip |
| Potvrda tvrdnje „najbrže u premium segmentu" | Josip |
| Brojke iz SELT deklaracije: 130 km/h, 200 kg/m², 187 projekata | Josip |
| Je li „500R" iz zapisnika isti model kao „Sunbreaker 500" | Josip |
| Sadržaj podstranica — tehnički listovi, presjeci, odvodnja, galerije, snimke montaže | Faza 2 |
| Skraćivanje usporedne tablice i galerije na naslovnoj (zapisnik t. 7) | Faza 2 |
| Uklanjanje `noindex` prije objave | nakon potvrde brojki |
