// recenzije.js — stvarne Google recenzije za TT Gradnja d.o.o. (Slavonski Brod)
// NE IZMISLJATI TEKST. Svaka recenzija dolazi izravno s Google Business profila
// (maps.google.com, pretraga "TT Gradnja d.o.o. Slavonski Brod" -> tab Recenzije).
// Provjereno i prepisano rucno 10.9.2026., dopunjeno 12.9.2026. (izvorni hrvatski tekst, ne Googleov prijevod).
//
// KAKO DODATI NOVU RECENZIJU (Josip/Toni, bez diranja index.html):
// 1. Otvori Google Maps, pronadi recenziju, klikni "Prikazi izvornik" ako je prevedena.
// 2. Kopiraj JEDAN blok ispod (od { do }), zalijepi ga na POCETAK niza "recenzije" (najnovije prve).
// 3. Popuni ime, inicijale (za avatar krug), tocan tekst i kontekst (npr. "Bioklimatska pergola" ili ostavi prazno).
// 4. Poredak = redoslijed prikaza na stranici. Ako ih ima vise od 3, na desktopu (>1024px) se
//    prikazuju kroz automatski karusel (3 vidljive, klize udesno->ulijevo, ciklicki kroz sve);
//    na mobitelu i za "prefers-reduced-motion" prikazuju se sve, staticki, bez animacije.
// 5. Azuriraj i "agregat" (ocjena/broj) ako se promijenio prosjek na Google profilu.
window.RECENZIJE = {
  "azurirano": "2026-09-12",
  "izvor": "Google Business profil — TT Gradnja d.o.o., Ul. Andrije Štampara 53, Slavonski Brod",
  "agregat": { "ocjena": "4,8", "broj": 31 },
  "recenzije": [
    {
      "ime": "Krešimir Šimić Šima",
      "inicijali": "KŠ",
      "kontekst": "",
      "kada": "prije 3 tjedna",
      "tekst": "Sve pohvale za ekipu iz TT gradnje, od inicijalnih dogovora preko izmjera pa sve do ugradnje. Svaka preporuka za ove profesionalce i njihov proizvod!"
    },
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
      "ime": "Marko Ravlić",
      "inicijali": "MR",
      "kontekst": "",
      "kada": "prije 11 mjeseci",
      "tekst": "Svaka preporuka za TT gradnju. Brzo odradili, točni, ažurni. Svaka pohvala i za Inu Luciju na suradnji i izlaženju u susret!"
    },
    {
      "ime": "Marijana Rakigjija",
      "inicijali": "MR",
      "kontekst": "Bioklimatska pergola",
      "kada": "prije 3 godine",
      "tekst": "Svakako svake pohvale za rad a posebno za ekipu.Iskrene preporuke za pergole hvala vam"
    },
    {
      "ime": "Dejan Sestan",
      "inicijali": "DS",
      "kontekst": "Bioklimatska pergola",
      "kada": "prije 3 godine",
      "tekst": "Sta da kazem? Sve je bilo odlicno. Super rad i vrhonska kvaliteta pergole. Pozdrav iz Zadra"
    }
  ]
};
