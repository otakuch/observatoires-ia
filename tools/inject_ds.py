#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte assets/design-system.css inline dans chaque page, entre marqueurs.
Idempotent : si le bloc existe, il est remplacé. Insertion avant le premier <style>.
Opère par indices de chaîne · ne lit jamais VEILLE_DATA autrement qu'en mémoire."""
import io, os, shutil, sys

ROOTS = ["/home/claude/site/observatoires-ia-site", "/home/claude/repo/observatoires-ia"]
SRC = "/home/claude/site/observatoires-ia-site/assets/design-system.css"
PAGES = [
    "index.html", "briefings.html", "contact.html", "donnees.html",
    "methodologie.html", "a-propos.html", "partenariats.html", "veille.html",
    "styleguide.html",
    "observatoires/france.html", "observatoires/suisse.html",
    "observatoires/comparer.html", "observatoires/europe.html",
]
BEGIN = '<style id="designSystem">/* DS:BEGIN */'
END = '/* DS:END */</style>'

css = io.open(SRC, encoding="utf-8").read().strip()
block = BEGIN + "\n" + css + "\n" + END

# garder la source synchronisée dans le repo
shutil.copyfile(SRC, "/home/claude/repo/observatoires-ia/assets/design-system.css")

for root in ROOTS:
    for rel in PAGES:
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            print("SKIP (absent)", p); continue
        s = io.open(p, encoding="utf-8").read()
        if BEGIN in s:
            a = s.index(BEGIN); b = s.index(END, a) + len(END)
            s = s[:a] + block + s[b:]
            mode = "maj"
        else:
            i = s.find("<style")
            assert i > 0, f"{p}: pas de <style>"
            s = s[:i] + block + "\n" + s[i:]
            mode = "injecté"
        io.open(p, "w", encoding="utf-8").write(s)
        print(f"OK [{mode}]", rel, "·", os.path.basename(root))
print("done")
