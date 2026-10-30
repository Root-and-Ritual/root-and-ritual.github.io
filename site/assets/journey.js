/* Root & Ritual reading path: adds a "Next step" panel above the footer of every page,
   so a reader is always told where to go next. Edit the order here; every page follows it.
   path: the guided route (Getting started, then the Collections). Each entry: page, next page,
   button text + one-line reason, optional "or" side door. */
(() => {
  const STEPS = [
    // Getting started
    ["root-and-ritual.html", "guide.html", "Start here", "A first passage through the archive: who keeps the records, how to read them, where to look."],
    ["guide.html", "organization.html", "Meet the firm", "Discover who keeps the records and why its authority depends on covenants.", ["glossary.html", "Look up a term in the glossary"]],
    ["organization.html", "handbook.html", "Read the Handbook", "Learn the threat tiers, contract statuses and the limits of an assessment.", ["ledger.html", "Meet the entities"]],
    ["handbook.html", "chat/", "Meet the Root & Ritual AI", "Now that you can read a record, ask the Root & Ritual AI for any name, universe or kind of being, or file a case of your own.", ["demons.html", "Explore the directory instead"]],
    ["demons.html", "ledger.html", "Meet the entities", "Open the Entity Master Ledger: every name, contract and record in one registry.", ["topics.html", "Browse the full directory"]],
    ["ledger.html", "entity.html?id=ENT-001", "Open your first dossier", "Start at the top of the registry with ENT-001, the Root Sovereign.", ["characters.html", "Browse every character"]],
    ["entity.html", "topics.html", "Browse the directory", "Every domain, topic and collection, listed in one place.", ["ledger.html", "Back to the ledger"]],
    ["topics.html", "characters.html", "Meet the characters", "The expanded character directory: every name the archive tracks."],
    ["characters.html", "lore.html", "Visit the Lore Library", "The supplied notes on mythology, faith traditions, cryptids and prophecy."],
    ["lore.html", "traditions.html", "Explore the traditions", "Folklore and mythology dossiers from around the world."],
    ["traditions.html", "glossary.html", "Learn the language", "The archive's terms in one glossary, so nothing in the collections trips you up."],
    ["glossary.html", "buffyverse.html", "Enter the collections", "You've finished the getting-started path. The franchise collections begin with Buffy & Angel."],
    // Collections
    ["buffyverse.html", "slayers.html", "Slayers", "The chosen ones, their watchers and their records."],
    ["slayers.html", "vampires.html", "Vampires", "Bloodlines, sires and the contracts that bind them."],
    ["vampires.html", "werewolves.html", "Werewolves", "The moon-bound and the packs that run the fen routes."],
    ["werewolves.html", "witches.html", "Witches & spellcasters", "Covens, practitioners and the rules of the craft."],
    ["witches.html", "norse.html", "Gods of the North", "The Norse collection."],
    ["norse.html", "comics.html", "Marvel & DC profiles", "Heroes across both universes."],
    ["comics.html", "x-men.html", "The X-Men", "The X-Men collection."],
    ["x-men.html", "films.html", "Film appearances", "From profile to screen: where the archive's names appear on film."],
    ["films.html", "ghostbusters.html", "Ghostbusters spotlight", "Strange activity? Meet the Ghostbusters."],
    ["ghostbusters.html", "sources.html", "Behind the entries", "Sources and editorial notes: what is supplied, what is new fiction."],
    ["sources.html", "image-credits.html", "Artwork & credits", "Who made the images in the archive."],
    ["image-credits.html", "root-and-ritual.html", "Return to the Sanctorum", "You've walked the whole archive. Go back to the start, or open any record from the ledger.", ["ledger.html", "Open the ledger"]],
  ];
  const START = 0, COLLECTIONS = 12;               // index where each section of the path begins
  const page = location.pathname.split("/").pop() || "root-and-ritual.html";
  const i = STEPS.findIndex(s => s[0] === page);
  if (i < 0) return;
  const [, next, title, why, alt] = STEPS[i];
  const inCollections = i >= COLLECTIONS && page !== "privacy.html";
  const section = page === "privacy.html" ? "Next" :
    inCollections ? `Collections · ${i - COLLECTIONS + 1} of ${STEPS.length - COLLECTIONS}` :
    `Getting started · Step ${i - START + 1} of ${COLLECTIONS}`;
  const prev = i > 0 && page !== "privacy.html" ? STEPS[i - 1][0] : null;

  const css = document.createElement("style");
  css.textContent = `.journey{max-width:1180px;margin:0 auto 10px;padding:0 30px}
.journey .jbox{border:1px solid var(--line);background:var(--panel);padding:26px 28px;display:grid;gap:10px}
.journey h2{margin:0;font-weight:normal;font-size:1.6rem}.journey p{margin:0;color:var(--muted)}
.journey .jrow{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;margin-top:8px}
.journey .jalt,.journey .jback{font:12px monospace;letter-spacing:1px;text-transform:uppercase}
@media(max-width:600px){.journey{padding:0 16px}.journey .jbox{padding:20px}}`;
  document.head.appendChild(css);

  const box = document.createElement("section");
  box.className = "journey";
  box.setAttribute("aria-label", "Next step");
  const esc = s => s.replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
  box.innerHTML = `<div class="jbox"><div class="eyebrow">${esc(section)}</div>
<h2>Next: ${esc(title)}</h2><p>${esc(why)}</p>
<div class="jrow"><a class="button" href="${esc(next)}">Continue →</a>
${alt ? `<a class="jalt" href="${esc(alt[0])}">or ${esc(alt[1])}</a>` : ""}
${prev ? `<a class="jback" href="${esc(prev)}">← Back</a>` : ""}</div></div>`;
  const footer = document.querySelector("footer");
  footer ? footer.parentNode.insertBefore(box, footer) : document.body.appendChild(box);
})();
