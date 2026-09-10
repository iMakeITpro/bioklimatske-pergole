// recenzije.js — stvarne Google recenzije za TT Gradnja d.o.o. (Slavonski Brod)
// NE IZMISLJATI TEKST. Svaka recenzija dolazi izravno s Google Business profila
// (maps.google.com, pretraga "TT Gradnja d.o.o. Slavonski Brod" -> tab Recenzije).
// Provjereno i prepisano rucno 10.9.2026. (izvorni hrvatski tekst, ne Googleov prijevod).
//
// KAKO DODATI NOVU RECENZIJU (Josip/Toni, bez diranja index.html):
// 1. Otvori Google Maps, pronadi recenziju, klikni "Prikazi izvornik" ako je prevedena.
// 2. Kopiraj JEDAN blok ispod (od { do }), zalijepi ga na POCETAK niza "recenzije" (najnovije prve).
// 3. Popuni ime, inicijale (za avatar krug), tocan tekst i kontekst (npr. "Bioklimatska pergola" ili ostavi prazno).
// 4. Prikazuju se PRVE 3 stavke iz niza — poredak = redoslijed prikaza na stranici.
// 5. Azuriraj i "agregat" (ocjena/broj) ako se promijenio prosjek na Google profilu.
window.RECENZIJE = {
  "azurirano": "2026-09-10",
  "izvor": "Google Business profil — TT Gradnja d.o.o., Ul. Andrije Štampara 53, Slavonski Brod",
  "agregat": { "ocjena": "4,8", "broj": 31 },
  "recenzije": [
    {
      "ime": "Manuela Matić",
      "inicijali": "MM",
      "kontekst": "Bioklimatska pergola",
      "kada": "prije mjesec dana",
      "tekst": "Sve pohvale tvrtki TT Gradnja na ugradnji bioklimatske pergole. Od prvog kontakta do završetka radova sve je odrađeno maksimalno profesionalno, brzo i u dogovorenom roku. Sama pergola je fantastična – dizajn je moderan, konstrukcija je izuzetno čvrsta, a zakretne lamele pružaju savršen hlad i potpunu zaštitu od kiše."
    },
    {
      "ime": "Anita Marković",
      "inicijali": "AM",
      "kontekst": "Bioklimatska pergola",
      "kada": "prije mjesec dana",
      "tekst": "Od prvog upita do završne montaže pergole sve je proteklo besprijekorno. Komunikacija je bila brza i jasna, a cijeli tim profesionalan. Svakako preporučujemo ovu tvrtku svima koji traže vrhunsku kvalitetu i profesionalan pristup. Hvala!"
    },
    {
      "ime": "Vladimir Jurić",
      "inicijali": "VJ",
      "kontekst": "Stolarija, u planu pergola",
      "kada": "prije 2 mjeseca",
      "tekst": "Stolariju smo uzimali već drugi put i ponovno smo izuzetno zadovoljni kompletnom uslugom. Od samog početka sve je bilo profesionalno, korektno i točno prema dogovoru — od komunikacije s vlasnikom i kontakt osobom, pa sve do isporuke i montaže. Monteri su bili profesionalni, točni, ljubazni i posao su odradili kvalitetno i uredno. Zbog odličnog iskustva sa stolarijom, TT Gradnja ostaje naš izbor i za sljedeći projekt — pergolu."
    },
    {
      "ime": "Marko Ravlić",
      "inicijali": "MR",
      "kontekst": "",
      "kada": "prije 11 mjeseci",
      "tekst": "Svaka preporuka za TT gradnju. Brzo odradili, točni, ažurni. Svaka pohvala i za Inu Luciju na suradnji i izlaženju u susret!"
    }
  ]
};
