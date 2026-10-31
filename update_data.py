import json

with open('assets/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.ARCHIVE = '
assert content.startswith(prefix)
json_str = content[len(prefix):].rstrip(';\n')
data = json.loads(json_str)

count_before = len(data)
print('Count before:', count_before)

new_entries = [
    # Team
    {
        "Entity ID": "ENT-617",
        "Name": "Dr. Peter Venkman",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Bill Murray",
        "Notes / Description": "Lead parapsychologist with a skeptical wit, smooth delivery, and an unconventional approach to containment logistics.",
        "Archival Assessment": "Lead parapsychologist with a skeptical wit, smooth delivery, and an unconventional approach to containment logistics. Essential for morale during multi-dimensional breach negotiations.",
        "Binding Seal": "Sealed in unlicensed nuclear hardware and collegiate irony.",
        "Reference": {
            "Tradition / context": "Ghostbusters Team",
            "Background": "Lead parapsychologist with a skeptical wit, smooth delivery, and an unconventional approach to containment logistics.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Parapsychologist / Founder",
            "Capabilities in the series": "Rapid negotiation, ghost trap deployment, and charismatic deflection of angry gods.",
            "Limits / continuity notes": "Relies entirely on proton packs and teammates when spectral entities refuse humor.",
            "Key connections": "Ray Stantz, Egon Spengler, Winston Zeddemore, Dana Barrett.",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-617.webp",
            "alt": "Original illustrated interpretation of Dr. Peter Venkman",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },
    {
        "Entity ID": "ENT-618",
        "Name": "Dr. Ray Stantz",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Dan Aykroyd",
        "Notes / Description": "Enthusiastic heart and historian of the firm, deeply versed in occult lore, subterranean architecture, and mortgage refinancing.",
        "Archival Assessment": "Enthusiastic heart and historian of the firm, deeply versed in occult lore, subterranean architecture, and mortgage refinancing. Prone to choosing destructive celestial manifestations.",
        "Binding Seal": "Sealed in second mortgages and antique metaphysical texts.",
        "Reference": {
            "Tradition / context": "Ghostbusters Team",
            "Background": "Enthusiastic heart and historian of the firm, deeply versed in occult lore, subterranean architecture, and mortgage refinancing.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Parapsychologist / Historian",
            "Capabilities in the series": "Occult research, vehicle maintenance (ECTO-1), and proton pack operation.",
            "Limits / continuity notes": "Vulnerable to choosing the form of the destructor when confronted with massive deities.",
            "Key connections": "Peter Venkman, Egon Spengler, Winston Zeddemore.",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-618.webp",
            "alt": "Original illustrated interpretation of Dr. Ray Stantz",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },
    {
        "Entity ID": "ENT-619",
        "Name": "Dr. Egon Spengler",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Harold Ramis",
        "Notes / Description": "Brilliant theoretical physicist and designer of proton containment systems, collector of spore spores, molds, and fungus.",
        "Archival Assessment": "Brilliant theoretical physicist and designer of proton containment systems, collector of spore spores, molds, and fungus. Without his theoretical framework, the firm would have vaporized Manhattan.",
        "Binding Seal": "Sealed in high-voltage capacitors and topological equations.",
        "Reference": {
            "Tradition / context": "Ghostbusters Team",
            "Background": "Brilliant theoretical physicist and designer of proton containment systems, collector of spore spores, molds, and fungus.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Theoretical Physicist / Inventor",
            "Capabilities in the series": "Quantum engineering, proton pack design, psychokinetic energy meter calibration.",
            "Limits / continuity notes": "Socially restrained; occasionally suggests dangerous experiments involving the crossing of streams.",
            "Key connections": "Peter Venkman, Ray Stantz, Winston Zeddemore, Janine Melnitz.",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-619.webp",
            "alt": "Original illustrated interpretation of Dr. Egon Spengler",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },
    {
        "Entity ID": "ENT-620",
        "Name": "Winston Zeddemore",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Ernie Hudson",
        "Notes / Description": "Pragmatic everyday recruit who joined for the steady paycheck and stayed for the biblical destruction and cosmic architecture.",
        "Archival Assessment": "Pragmatic everyday recruit who joined for the steady paycheck and stayed for the biblical destruction and cosmic architecture. Grounding influence on academic eccentricity.",
        "Binding Seal": "Sealed in municipal contracts and steady nerves.",
        "Reference": {
            "Tradition / context": "Ghostbusters Team",
            "Background": "Pragmatic everyday recruit who joined for the steady paycheck and stayed for the biblical destruction and cosmic architecture.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Field Operative / Heavy Equipment Specialist",
            "Capabilities in the series": "Pragmatic tactical sense, Ecto-1 operation, and fearless reinforcement during containment grid crises.",
            "Limits / continuity notes": "Started without academic parapsychological background, but quickly mastered existential threats.",
            "Key connections": "Peter Venkman, Ray Stantz, Egon Spengler.",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-620.webp",
            "alt": "Original illustrated interpretation of Winston Zeddemore",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },
    {
        "Entity ID": "ENT-621",
        "Name": "Janine Melnitz",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Annie Potts",
        "Notes / Description": "Sharp-tongued administrative backbone and switchboard operator who keeps the franchise solvent amidst mounting property damage.",
        "Archival Assessment": "Sharp-tongued administrative backbone and switchboard operator who keeps the franchise solvent amidst mounting property damage. Unfazed by weeping statues or possessed callers.",
        "Binding Seal": "Sealed in rotary telephone switches and dry wit.",
        "Reference": {
            "Tradition / context": "Ghostbusters Support",
            "Background": "Sharp-tongued administrative backbone and switchboard operator who keeps the franchise solvent amidst mounting property damage.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Administrator / Secretary",
            "Capabilities in the series": "Client triage, dispatching, and occasional proton pack field deployment.",
            "Limits / continuity notes": "Confined mostly to headquarters dispatch during major containment emergencies.",
            "Key connections": "Egon Spengler, Peter Venkman, Ray Stantz, Winston Zeddemore.",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-621.webp",
            "alt": "Original illustrated interpretation of Janine Melnitz",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },
    {
        "Entity ID": "ENT-622",
        "Name": "Dana Barrett",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Sigourney Weaver",
        "Notes / Description": "Classical cellist whose Central Park West apartment became the architectural nexus for Gozer's return.",
        "Archival Assessment": "Classical cellist whose Central Park West apartment became the architectural nexus for Gozer's return. Demonstrated remarkable resilience after temporary spiritual tenancy by Zuul.",
        "Binding Seal": "Sealed in cello rosin and architectural zoning violations.",
        "Reference": {
            "Tradition / context": "Ghostbusters Associate",
            "Background": "Classical cellist whose Central Park West apartment became the architectural nexus for Gozer's return.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Classical Musician / Zuul Host",
            "Capabilities in the series": "Musical discipline and surviving multi-dimensional architectural hauntings.",
            "Limits / continuity notes": "Vulnerable to demonic possession when structural dimensions align.",
            "Key connections": "Peter Venkman, Louis Tully, Ivo Shandor (architect).",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-622.webp",
            "alt": "Original illustrated interpretation of Dana Barrett",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },
    {
        "Entity ID": "ENT-623",
        "Name": "Louis Tully",
        "Category": "Ghostbusters · Team",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "Ghostbusters (1984) — portrayed by Rick Moranis",
        "Notes / Description": "Meticulous tax attorney and party host who inadvertently served as the Keymaster of Gozer.",
        "Archival Assessment": "Meticulous tax attorney and party host who inadvertently served as the Keymaster of Gozer. Later demonstrated surprising competency with unlicensed nuclear accelerators in court.",
        "Binding Seal": "Sealed in tax code and colander headwear.",
        "Reference": {
            "Tradition / context": "Ghostbusters Legal Counsel",
            "Background": "Meticulous tax attorney and party host who inadvertently served as the Keymaster of Gozer.",
            "Source title": "Ghostbusters Official Character Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Tax Accountant / Keymaster",
            "Capabilities in the series": "Legal counsel, party organization, and hosting guests with glowing red eyes.",
            "Limits / continuity notes": "Prone to locking himself out of his apartment during demonic conjunctions.",
            "Key connections": "Dana Barrett, Peter Venkman, Egon Spengler.",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-623.webp",
            "alt": "Original illustrated interpretation of Louis Tully",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Team"],
            ["By Type", "Characters", "Ghostbusters", "Team"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the cinematic role, not a real person."
    },

    # Ghosts & Entities
    {
        "Entity ID": "ENT-624",
        "Name": "Slimer",
        "Category": "Ghostbusters · Ghosts & Entities",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman)",
        "Threat Level": "Class 5 Full Roaming Vapor",
        "Contract Status": "Contained / Semi-Resident",
        "First Appearance / Record": "Ghostbusters (1984) — Sedgewick Hotel",
        "Notes / Description": "Voracious green spud-like entity with an insatiable appetite for room service and heavy polysaccharide residues.",
        "Archival Assessment": "Voracious green spud-like entity with an insatiable appetite for room service and heavy polysaccharide residues. Leaves viscous ectoplasmic trails on all upholstered furniture.",
        "Binding Seal": "Sealed in hotel ballrooms and hot dog carts.",
        "Reference": {
            "Tradition / context": "Class 5 Full Roaming Vapor",
            "Background": "Voracious green spud-like entity with an insatiable appetite for room service and heavy polysaccharide residues.",
            "Source title": "Ghostbusters Official Entity Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Entity / Former Sedgewick Resident",
            "Capabilities in the series": "Flight, passing through solid matter, and depositing heavy slime on unsuspecting targets.",
            "Limits / continuity notes": "Easily distracted by food or the promise of a snack.",
            "Key connections": "Dr. Peter Venkman (first direct encounter target).",
            "Selected film references": "Ghostbusters (1984); Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-624.webp",
            "alt": "Original illustrated interpretation of Slimer",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Ghosts & Entities"],
            ["By Type", "Demons & Dark Powers", "Ghosts & Entities", "Ghostbusters"]
        ],
        "Types": [],
        "FictionNotice": "Fictional entity reference. This entry describes the cinematic entity, not a real phenomenon."
    },
    {
        "Entity ID": "ENT-625",
        "Name": "Gozer the Gozerian",
        "Category": "Ghostbusters · Ghosts & Entities",
        "Origin / Lore": "Ghostbusters (1984, dir. Ivan Reitman) — Sumerian deity",
        "Threat Level": "Omega",
        "Contract Status": "Exiled / Dispersed",
        "First Appearance / Record": "Ghostbusters (1984) — Central Park West Ziggurat",
        "Notes / Description": "Ancient shapeshifting god of destruction worshipped by the Sumerians, Hittites, and Mesopotamians, manifesting via architectural gateways.",
        "Archival Assessment": "Ancient shapeshifting god of destruction worshipped by the Sumerians, Hittites, and Mesopotamians, manifesting via architectural gateways. Demands visitors choose the form of their destructor.",
        "Binding Seal": "Sealed in crossed proton streams and a closed dimensional door.",
        "Reference": {
            "Tradition / context": "Extra-dimensional Deity",
            "Background": "Ancient shapeshifting god of destruction worshipped by the Sumerians, Hittites, and Mesopotamians, manifesting via architectural gateways.",
            "Source title": "Ghostbusters Official Entity Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Sumerian God of Destruction / Destructor",
            "Capabilities in the series": "Energy projection, telekinesis, lightning generation, and dimensional portal control.",
            "Limits / continuity notes": "Requires a physical architectural gateway and worshippers or architects to build it.",
            "Key connections": "Zuul, Vinz Clortho, Ivo Shandor.",
            "Selected film references": "Ghostbusters (1984)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-625.webp",
            "alt": "Original illustrated interpretation of Gozer the Gozerian",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Ghosts & Entities"],
            ["By Type", "Demons & Dark Powers", "Ghosts & Entities", "Ghostbusters"]
        ],
        "Types": [],
        "FictionNotice": "Fictional entity reference. This entry describes the cinematic entity, not a real phenomenon."
    },
    {
        "Entity ID": "ENT-626",
        "Name": "Zuul the Gatekeeper",
        "Category": "Ghostbusters · Ghosts & Entities",
        "Origin / Lore": "Ghostbusters (1984) — Minion of Gozer",
        "Threat Level": "Class 7",
        "Contract Status": "Exiled",
        "First Appearance / Record": "Ghostbusters (1984) — Central Park West",
        "Notes / Description": "Demonic demi-god and minion of Gozer who takes possession of Dana Barrett to guard the gateway.",
        "Archival Assessment": "Demonic demi-god and minion of Gozer who takes possession of Dana Barrett to guard the gateway. Possesses dog-like spectral features when fully manifested.",
        "Binding Seal": "Sealed in stone terror dog carvings and portal architecture.",
        "Reference": {
            "Tradition / context": "Minion of Gozer",
            "Background": "Demonic demi-god and minion of Gozer who takes possession of Dana Barrett to guard the gateway.",
            "Source title": "Ghostbusters Official Entity Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Gatekeeper of Gozer",
            "Capabilities in the series": "Possession, telekinesis, and anchoring dimensional rifts.",
            "Limits / continuity notes": "Requires union with the Keymaster to complete the gateway ritual.",
            "Key connections": "Gozer, Vinz Clortho, Dana Barrett.",
            "Selected film references": "Ghostbusters (1984)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-626.webp",
            "alt": "Original illustrated interpretation of Zuul the Gatekeeper",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Ghosts & Entities"],
            ["By Type", "Demons & Dark Powers", "Ghosts & Entities", "Ghostbusters"]
        ],
        "Types": [],
        "FictionNotice": "Fictional entity reference. This entry describes the cinematic entity, not a real phenomenon."
    },
    {
        "Entity ID": "ENT-627",
        "Name": "Vinz Clortho the Keymaster",
        "Category": "Ghostbusters · Ghosts & Entities",
        "Origin / Lore": "Ghostbusters (1984) — Minion of Gozer",
        "Threat Level": "Class 7",
        "Contract Status": "Exiled",
        "First Appearance / Record": "Ghostbusters (1984) — Central Park West / Louis Tully's apartment",
        "Notes / Description": "Demonic demi-god and minion of Gozer who possesses Louis Tully to unlock the dimensional portal.",
        "Archival Assessment": "Demonic demi-god and minion of Gozer who possesses Louis Tully to unlock the dimensional portal. Frequently found wandering city streets in strange headwear.",
        "Binding Seal": "Sealed in stone terror dog carvings and portal architecture.",
        "Reference": {
            "Tradition / context": "Minion of Gozer",
            "Background": "Demonic demi-god and minion of Gozer who possesses Louis Tully to unlock the dimensional portal.",
            "Source title": "Ghostbusters Official Entity Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Keymaster of Gozer",
            "Capabilities in the series": "Possession, portal unlocking, and seeking the Gatekeeper.",
            "Limits / continuity notes": "Requires union with the Gatekeeper to open the gateway.",
            "Key connections": "Gozer, Zuul, Louis Tully.",
            "Selected film references": "Ghostbusters (1984)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-627.webp",
            "alt": "Original illustrated interpretation of Vinz Clortho the Keymaster",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Ghosts & Entities"],
            ["By Type", "Demons & Dark Powers", "Ghosts & Entities", "Ghostbusters"]
        ],
        "Types": [],
        "FictionNotice": "Fictional entity reference. This entry describes the cinematic entity, not a real phenomenon."
    },
    {
        "Entity ID": "ENT-628",
        "Name": "The Stay Puft Marshmallow Man",
        "Category": "Ghostbusters · Ghosts & Entities",
        "Origin / Lore": "Ghostbusters (1984) — Destructor Form",
        "Threat Level": "Omega",
        "Contract Status": "Dispersed / Vaporized",
        "First Appearance / Record": "Ghostbusters (1984) — New York City streets",
        "Notes / Description": "Colossal manifestation of Gozer taking the form of an innocent corporate advertising mascot chosen inadvertently by Ray Stantz.",
        "Archival Assessment": "Colossal manifestation of Gozer taking the form of an innocent corporate advertising mascot chosen inadvertently by Ray Stantz. Proves that any thought, even a harmless snack brand, can become an existential threat under psychokinetic amplification.",
        "Binding Seal": "Sealed in toasted sugar and crossed proton streams.",
        "Reference": {
            "Tradition / context": "Destructor Manifestation",
            "Background": "Colossal manifestation of Gozer taking the form of an innocent corporate advertising mascot chosen inadvertently by Ray Stantz.",
            "Source title": "Ghostbusters Official Entity Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1984 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Form of the Destructor",
            "Capabilities in the series": "Colossal physical scale, urban destruction, and sugary resilience.",
            "Limits / continuity notes": "Directly tied to Gozer's portal stability.",
            "Key connections": "Gozer, Ray Stantz.",
            "Selected film references": "Ghostbusters (1984)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-628.webp",
            "alt": "Original illustrated interpretation of The Stay Puft Marshmallow Man",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Ghosts & Entities"],
            ["By Type", "Demons & Dark Powers", "Ghosts & Entities", "Ghostbusters"]
        ],
        "Types": [],
        "FictionNotice": "Fictional entity reference. This entry describes the cinematic entity, not a real phenomenon."
    },
    {
        "Entity ID": "ENT-629",
        "Name": "Vigo the Carpathian",
        "Category": "Ghostbusters · Ghosts & Entities",
        "Origin / Lore": "Ghostbusters II (1989, dir. Ivan Reitman)",
        "Threat Level": "Class 7 / Omega",
        "Contract Status": "Contained / Defeated",
        "First Appearance / Record": "Ghostbusters II (1989) — Manhattan Museum of Art",
        "Notes / Description": "16th-century tyrant, sorcerer, and warlord known as Vigo the Cruel, Scourge of Carpathia, who attempted to reincarnate through a museum portrait fueled by negative slime emotional energy.",
        "Archival Assessment": "16th-century tyrant, sorcerer, and warlord known as Vigo the Cruel, Scourge of Carpathia, who attempted to reincarnate through a museum portrait fueled by negative slime emotional energy. Defeated by the collective goodwill and positive mood of New York citizens.",
        "Binding Seal": "Sealed in museum canvas, negative mood suppression, and Siberian painting restoration.",
        "Reference": {
            "Tradition / context": "Possessing Spirit / Warlord",
            "Background": "16th-century tyrant, sorcerer, and warlord known as Vigo the Cruel, Scourge of Carpathia, who attempted to reincarnate through a museum portrait fueled by negative slime emotional energy.",
            "Source title": "Ghostbusters II Official Entity Reference",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Archival dossier compiled from 1989 operational records. Unofficial fan reference."
        },
        "Canon": {
            "Role / identity": "Carpathian Tyrant / Painting Entity",
            "Capabilities in the series": "Possession through portraiture, psychokinetic slime generation, and psychological intimidation.",
            "Limits / continuity notes": "Requires negative human emotion and a suitable infant host or painted vessel to anchor his spirit.",
            "Key connections": "Janosz Poha (curator/servant), Ray Stantz, Peter Venkman.",
            "Selected film references": "Ghostbusters II (1989)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-629.webp",
            "alt": "Original illustrated interpretation of Vigo the Carpathian",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Ghosts & Entities"],
            ["By Type", "Demons & Dark Powers", "Ghosts & Entities", "Ghostbusters"]
        ],
        "Types": [],
        "FictionNotice": "Fictional entity reference. This entry describes the cinematic entity, not a real phenomenon."
    },

    # Animated
    {
        "Entity ID": "ENT-630",
        "Name": "The Real Ghostbusters",
        "Category": "Ghostbusters · Animated",
        "Origin / Lore": "The Real Ghostbusters (animated series, 1986-1991)",
        "Threat Level": "Allies",
        "Contract Status": "Active Binding",
        "First Appearance / Record": "The Real Ghostbusters (1986) — animated continuity",
        "Notes / Description": "The animated continuation of the team featuring Peter Venkman voiced by Lorenzo Music, Ray Stantz by Frank Welker, Egon Spengler by Maurice LaMarche, Winston Zeddemore by Arsenio Hall (first season), and Slimer by Frank Welker.",
        "Archival Assessment": "The animated continuation of the team featuring Peter Venkman voiced by Lorenzo Music, Ray Stantz by Frank Welker, Egon Spengler by Maurice LaMarche, Winston Zeddemore by Arsenio Hall (first season), and Slimer by Frank Welker. Expanded the paranormal caseload across mythologies and dimensions.",
        "Binding Seal": "Sealed in Saturday morning animation cels and syndication archives.",
        "Reference": {
            "Tradition / context": "Animated Series Continuity",
            "Background": "The animated continuation of the team featuring Peter Venkman voiced by Lorenzo Music, Ray Stantz by Frank Welker, Egon Spengler by Maurice LaMarche, Winston Zeddemore by Arsenio Hall (first season), and Slimer by Frank Welker.",
            "Source title": "The Real Ghostbusters Official Archive",
            "Source URL": "https://www.ghostbusters.com/",
            "Editorial note": "Unofficial animated continuity reference. Broadcast 1986-1991."
        },
        "Canon": {
            "Role / identity": "Animated Parapsychological Investigation Unit",
            "Capabilities in the series": "Advanced containment tech, multi-dimensional traversal, and confronting folkloric spirits weekly.",
            "Limits / continuity notes": "Animated television continuity separate from live-action feature films.",
            "Key connections": "Peter Venkman, Ray Stantz, Egon Spengler, Winston Zeddemore, Slimer.",
            "Selected film references": "The Real Ghostbusters (animated series, 1986-1991)"
        },
        "Expansion": {},
        "Image": {
            "src": "assets/portraits/ENT-630.webp",
            "alt": "Original illustrated interpretation of The Real Ghostbusters",
            "credit": "AI-generated illustration; not official franchise artwork or a verified historical likeness.",
            "kind": "generated"
        },
        "Universe": "Ghostbusters",
        "DirectoryPaths": [
            ["Universes", "Ghostbusters", "Animated"],
            ["By Type", "Characters", "Ghostbusters", "Animated"]
        ],
        "Types": [],
        "FictionNotice": "Fictional character reference. This entry describes the animated series continuity."
    }
]

data.extend(new_entries)
count_after = len(data)
print('Count after:', count_after)

# Serialize back with window.ARCHIVE = ...
new_json_str = prefix + json.dumps(data, ensure_ascii=False, indent=None) + ';'
with open('assets/data.js', 'w', encoding='utf-8') as f:
    f.write(new_json_str)

print('Successfully updated assets/data.js')
