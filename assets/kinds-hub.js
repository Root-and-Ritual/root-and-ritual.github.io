/* Demons & Entities hub: every record grouped by kind of being (the "By Type" branch of the directory).
   Kinds and sub-kinds come from the records' DirectoryPaths, so new entries appear here automatically. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
  const db = window.ARCHIVE || [];
  const TOP = 'By Type';
  const ORDER = ['Demons & Dark Powers', 'Undead', 'Spirits & Ghosts', 'Shapeshifters & Werewolves', 'Witches, Wizards & Spellcasters',
    'Monsters & Beasts', 'Gods & Divine Beings', 'Folk & Fae', 'Aliens & Machines', 'Mutants & Super-Powered',
    'Villains & Rivals', 'Heroes & Humans', 'Traditions & Tools', 'Relics, Places & Mysteries'];
  const topic = p => 'topics.html?path=' + encodeURIComponent(JSON.stringify(p));
  const plural = (n, w) => n + ' ' + w + (n === 1 ? '' : 's');

  const kinds = new Map();
  for (const r of db) for (const p of r.DirectoryPaths || []) {
    if (p[0] !== TOP) continue;
    const k = p[1], sub = p.length > 3 ? p[2] : null;
    if (!kinds.has(k)) kinds.set(k, {records: new Set(), subs: new Map()});
    const g = kinds.get(k); g.records.add(r);
    if (sub) { if (!g.subs.has(sub)) g.subs.set(sub, new Set()); g.subs.get(sub).add(r); }
  }
  const names = [...kinds.keys()].sort((a, b) => (ORDER.indexOf(a) + 1 || 99) - (ORDER.indexOf(b) + 1 || 99) || a.localeCompare(b));

  // Insert type filter chips container above the tools / search
  const toolsEl = document.querySelector('.tools');
  if (toolsEl && !$('kind-chips')) {
    const chipsWrap = document.createElement('div');
    chipsWrap.id = 'kind-chips';
    chipsWrap.className = 'actions';
    chipsWrap.style.margin = '15px 0 25px';
    chipsWrap.style.display = 'flex';
    chipsWrap.style.flexWrap = 'wrap';
    chipsWrap.style.gap = '10px';

    // Build chips: 'All' + each kind in names, with counts
    let activeType = '';

    function renderChips() {
      const allCount = db.length;
      let html = `<button type="button" class="${activeType === '' ? '' : 'secondary'}" data-kind="">All (${allCount})</button>`;
      for (const k of names) {
        const size = kinds.get(k).records.size;
        html += `<button type="button" class="${activeType === k ? '' : 'secondary'}" data-kind="${esc(k)}">${esc(k)} (${size})</button>`;
      }
      chipsWrap.innerHTML = html;

      chipsWrap.querySelectorAll('button').forEach(btn => {
        btn.onclick = () => {
          activeType = btn.getAttribute('data-kind');
          renderChips();
          renderList();
        };
      });
    }

    toolsEl.insertAdjacentElement('afterend', chipsWrap);
    renderChips();
  }

  function renderList() {
    const activeType = document.querySelector('#kind-chips button:not(.secondary)')?.getAttribute('data-kind') || '';
    const filteredNames = activeType ? [activeType] : names;

    $('kind-count').textContent = `${plural(activeType ? kinds.get(activeType).records.size : db.length, 'record')} sorted into ${activeType ? 1 : names.length} kind${activeType ? '' : 's'} of being.`;

    $('kind-list').innerHTML = filteredNames.map(k => {
      const g = kinds.get(k);
      const subs = [...g.subs.entries()].sort((a, b) => a[0].localeCompare(b[0]));
      return `<section class="panel kind"><div class="eyebrow">${plural(g.records.size, 'record')}</div><h2><a href="${topic([TOP, k])}">${esc(k)} →</a></h2>`
        + (subs.length ? `<p class="kind-subs">${subs.map(([s, rs]) => `<a href="${topic([TOP, k, s])}">${esc(s)} <span>(${rs.size})</span></a>`).join('')}</p>` : '')
        + '</section>';
    }).join('');
  }

  $('kind-count').textContent = `${plural(db.length, 'record')} sorted into ${names.length} kinds of being.`;
  $('kind-list').innerHTML = names.map(k => {
    const g = kinds.get(k);
    const subs = [...g.subs.entries()].sort((a, b) => a[0].localeCompare(b[0]));
    return `<section class="panel kind"><div class="eyebrow">${plural(g.records.size, 'record')}</div><h2><a href="${topic([TOP, k])}">${esc(k)} →</a></h2>`
      + (subs.length ? `<p class="kind-subs">${subs.map(([s, rs]) => `<a href="${topic([TOP, k, s])}">${esc(s)} <span>(${rs.size})</span></a>`).join('')}</p>` : '')
      + '</section>';
  }).join('');

  function search() {
    const q = $('kind-search').value.trim().toLowerCase();
    $('kind-results').hidden = !q; $('kind-list').hidden = !!q;
    const chipsEl = $('kind-chips');
    if (chipsEl) chipsEl.style.display = q ? 'none' : 'flex';
    if (!q) return;
    const rs = db.filter(r => JSON.stringify([r.Name, r.Category, r.Universe, r['Notes / Description'], r.DirectoryPaths]).toLowerCase().includes(q)).slice(0, 60);
    $('kind-results').innerHTML = rs.length ? rs.map(r => {
      const p = (r.DirectoryPaths || []).find(x => x[0] === TOP);
      return `<a class="card" href="entity.html?id=${encodeURIComponent(r['Entity ID'])}"><img class="card-portrait" src="${esc(r.Image && r.Image.src)}" alt="" loading="lazy" width="640" height="640"><span class="number">${esc(p ? p.slice(1, -1).join(' · ') : r.Category)}</span><h3>${esc(r.Name)}</h3><p>${esc(r['Notes / Description'])}</p><span class="more">Open dossier →</span></a>`;
    }).join('') : '<p class="empty">Nothing matches. Try another name or kind.</p>';
  }
  $('kind-search').addEventListener('input', search);
})();
