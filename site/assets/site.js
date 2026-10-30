/* Root & Ritual shared page helper (every page except the gate).
   1. Live counts: any element with data-rr="records|domains|universes" shows the number from assets/data.js,
      so the home page, guide and ledger can never disagree again.
   2. Back to results: when a reader opens a dossier from a list (ledger search, directory, characters,
      a collection), the dossier's top link returns to that exact list, filters and search included. */
(() => {
  'use strict';
  const page = location.pathname.split('/').pop() || 'root-and-ritual.html';
  const esc = s => String(s).replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
  const store = (k, v) => { try { v === undefined ? sessionStorage.removeItem(k) : sessionStorage.setItem(k, v); } catch (e) {} };
  const read = k => { try { return sessionStorage.getItem(k); } catch (e) { return null; } };

  function fill() {
    const db = window.ARCHIVE || [];
    const v = {records: db.length, domains: new Set(db.map(r => r.Category)).size,
               universes: new Set(db.map(r => r.Universe).filter(Boolean)).size};
    document.querySelectorAll('[data-rr]').forEach(el => { if (v[el.dataset.rr] != null) el.textContent = v[el.dataset.rr]; });
  }
  if (document.querySelector('[data-rr]')) {
    if (window.ARCHIVE) fill();
    else { const s = document.createElement('script'); s.src = 'assets/data.js'; s.onload = fill; document.head.appendChild(s); }
  }

  if (page !== 'entity.html') {
    // capture phase, so it runs before the browser follows the link
    document.addEventListener('click', e => {
      const a = e.target.closest && e.target.closest('a[href^="entity.html"]');
      if (!a) return;
      store('rr_back', location.href);
      store('rr_back_label', (document.querySelector('h1') || {}).textContent || document.title.split(' — ')[0]);
    }, true);
  } else {
    const crumb = document.querySelector('.crumb');
    const back = read('rr_back');
    if (crumb && back && back.startsWith(location.origin)) {
      const label = (read('rr_back_label') || 'results').trim().replace(/\.$/, '');
      crumb.innerHTML = `<a href="${esc(back)}">← Back to ${esc(label.length > 40 ? 'results' : label)}</a> · <a href="ledger.html">Master Ledger</a> / Entity dossier`;
    }
  }
})();
