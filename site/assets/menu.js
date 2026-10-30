/* Close the Directory dropdown when the reader taps elsewhere or presses Escape. */
(() => {
  const d = document.querySelector('.nav .menu-dir');
  if (!d) return;
  document.addEventListener('click', e => { if (d.open && !d.contains(e.target)) d.open = false; });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && d.open) { d.open = false; d.querySelector('summary').focus(); } });
})();
