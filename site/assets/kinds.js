window.RR_KIND = function(record) {
  const types = record.Types || [];
  const universe = record.Universe || '';
  const category = record.Category || '';
  const origin = record['Origin / Lore'] || '';
  const text = (category + ' ' + origin).toLowerCase();

  const demonTypes = ['Vampires', 'Werewolves', 'Witches & Spellcasters', 'Dark Lords', 'Antagonists'];
  const monsterTypes = ['Dragons', 'Extraterrestrials', 'Ents', 'Phoenixes', 'Half-giants', 'House-elves'];

  if (types.some(t => demonTypes.includes(t)) || universe === 'Root & Ritual' || /demon|devil|fiend|succubus|incubus/.test(text)) {
    return 'Demon';
  }
  if (types.some(t => monsterTypes.includes(t)) || /creature|cryptid|monster|beast/.test(text)) {
    return 'Monster';
  }
  return 'Character';
};

window.RR_DOMAINS = (window.ARCHIVE ? [...new Set(window.ARCHIVE.map(r => r.Universe).filter(Boolean))] : []).sort().map(u => ({
  name: u,
  universe: u,
  count: window.ARCHIVE.filter(r => r.Universe === u).length
}));
