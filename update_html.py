with open('ghostbusters.html', 'r', encoding='utf-8') as f:
    text = f.read()

section_html = '''<section class="lore-section"><h2>Who you're calling</h2>
<p>Archival records of the team, animated continuity, and entities from the Ghostbusters files.</p>
<h3>Team</h3>
<ul>
<li><a href="entity.html?id=ENT-617">Dr. Peter Venkman</a> (Bill Murray)</li>
<li><a href="entity.html?id=ENT-618">Dr. Ray Stantz</a> (Dan Aykroyd)</li>
<li><a href="entity.html?id=ENT-619">Dr. Egon Spengler</a> (Harold Ramis)</li>
<li><a href="entity.html?id=ENT-620">Winston Zeddemore</a> (Ernie Hudson)</li>
<li><a href="entity.html?id=ENT-621">Janine Melnitz</a> (Annie Potts)</li>
<li><a href="entity.html?id=ENT-622">Dana Barrett</a> (Sigourney Weaver)</li>
<li><a href="entity.html?id=ENT-623">Louis Tully</a> (Rick Moranis)</li>
</ul>
<h3>Animated</h3>
<ul>
<li><a href="entity.html?id=ENT-630">The Real Ghostbusters</a> (animated series, 1986-1991: Peter Venkman voiced by Lorenzo Music, Ray Stantz by Frank Welker, Egon Spengler by Maurice LaMarche, Winston Zeddemore by Arsenio Hall, Slimer by Frank Welker)</li>
</ul>
<h3>Ghosts & Entities</h3>
<ul>
<li><a href="entity.html?id=ENT-624">Slimer</a> (Ghostbusters 1984)</li>
<li><a href="entity.html?id=ENT-625">Gozer the Gozerian</a> (1984)</li>
<li><a href="entity.html?id=ENT-626">Zuul the Gatekeeper</a> (1984, possessed Dana Barrett)</li>
<li><a href="entity.html?id=ENT-627">Vinz Clortho the Keymaster</a> (1984, possessed Louis Tully)</li>
<li><a href="entity.html?id=ENT-628">The Stay Puft Marshmallow Man</a> (1984)</li>
<li><a href="entity.html?id=ENT-629">Vigo the Carpathian</a> (Ghostbusters II, 1989)</li>
</ul>
</section>'''

target = '<section class="lore-section"><h2>Start with the films</h2>'
assert target in text, "Target not found in ghostbusters.html"

new_text = text.replace(target, section_html + '\n' + target)
with open('ghostbusters.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully inserted Who you're calling section into ghostbusters.html")
