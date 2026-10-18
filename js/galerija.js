// ---------- galerija: postupno prikazivanje (6 -> 18 -> sve) ----------
// Shared by index.html #gal and the model pages' project galleries (there only <=1024px).
// Returns render() so a page can re-apply it after showing the cards its own way.
function galMore(cards, btn){
  var steps = [6, 18, Infinity];
  var idx = 0;
  function render(){
    var show = steps[idx];
    cards.forEach(function(c, i){ c.style.display = i < show ? '' : 'none'; });
    if (btn && show >= cards.length) btn.style.display = 'none';
  }
  render();
  if (btn) btn.addEventListener('click', function(){
    idx = Math.min(idx + 1, steps.length - 1);
    render();
  });
  return render;
}
