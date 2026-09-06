/* Slanje obrazaca preko Web3Forms.
   Kljuc se dobiva na app.web3forms.com i po dizajnu stoji u kodu stranice.
   Zamijeni vrijednost ispod i oba obrasca proradе — konfigurator i stranica upita. */
const WEB3FORMS_KLJUC = '7d20329e-8d57-4350-9d71-4f618d8bd759';

async function posaljiObrazac(podaci){
  if(WEB3FORMS_KLJUC.indexOf('OVDJE') === 0){
    console.warn('Web3Forms kljuc nije postavljen — obrazac nije poslan.');
    return {ok:false, razlog:'nema-kljuca'};
  }
  try{
    const r = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: {'Content-Type':'application/json', 'Accept':'application/json'},
      body: JSON.stringify(Object.assign({access_key: WEB3FORMS_KLJUC}, podaci))
    });
    const j = await r.json();
    return {ok: !!j.success, razlog: j.message};
  }catch(e){
    return {ok:false, razlog:String(e)};
  }
}
