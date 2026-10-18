#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte la charte Ciel & Marine en fin de <head> de chaque page, entre marqueurs.

Pages du site : assets/ciel-marine.css.
Sous-pages : dépêches 01 à 04, gabarit et matrices (gabarit du site) reçoivent
ciel-marine.css puis ciel-marine-sous-pages.css ; dépêches 05 à 10 (gabarit
Dispatch·iA, jetons propres) reçoivent ciel-marine-sous-pages.css seule.

Idempotent : si le bloc existe, il est remplacé ; sinon il est inséré juste avant
</head>, donc après le bloc designSystem et la feuille de page (Encre & ardoise).
Opère par indices de chaîne. Ne touche ni aux données inline ni aux scripts.

Usage :  python3 tools/inject_cm.py            (injecte ou met à jour)
         python3 tools/inject_cm.py --remove   (retire le bloc, retour à Encre & ardoise)
"""
import glob, io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = "assets/ciel-marine.css"
SUB = "assets/ciel-marine-sous-pages.css"
PAGES = [
    "index.html", "briefings.html", "contact.html", "donnees.html",
    "methodologie.html", "a-propos.html", "partenariats.html", "veille.html",
    "styleguide.html",
    "observatoires/france.html", "observatoires/suisse.html",
    "observatoires/comparer.html", "observatoires/europe.html",
]
# Sous-pages découvertes automatiquement, y compris les futures dépêches :
# gabarit du site (barre #siteNav ou .site-nav) -> les deux couches ;
# gabarit Dispatch·iA (jetons propres)          -> la couche sous-pages seule.
SUBDIRS = ["briefings", "infographies", "templates"]


def _family(rel):
    head = io.open(os.path.join(ROOT, rel), encoding="utf-8").read()
    return [MAIN, SUB] if ('id="siteNav"' in head or 'class="site-nav"' in head) else [SUB]


LAYERS = {rel: [MAIN] for rel in PAGES}
for d in SUBDIRS:
    for f in sorted(glob.glob(os.path.join(ROOT, d, "*.html"))):
        rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
        LAYERS[rel] = _family(rel)
BEGIN = '<style id="cielMarine">/* CM:BEGIN */'
END = '/* CM:END */</style>'


def strip_block(s):
    if BEGIN not in s:
        return s
    a = s.index(BEGIN)
    b = s.index(END, a) + len(END)
    if s[b:b + 1] == "\n":
        b += 1
    return s[:a] + s[b:]


def main():
    remove = "--remove" in sys.argv
    cache = {}
    for rel, layers in LAYERS.items():
        key = tuple(layers)
        if key not in cache:
            css = "\n\n".join(io.open(os.path.join(ROOT, f), encoding="utf-8").read().strip() for f in layers)
            cache[key] = BEGIN + "\n" + css + "\n" + END + "\n"
        block = cache[key]
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print("SKIP (absent)", rel)
            continue
        s = io.open(p, encoding="utf-8", newline="").read()
        base = strip_block(s)
        if remove:
            out = base
            mode = "retiré"
        else:
            i = base.find("</head>")
            assert i > 0, f"{rel}: pas de </head>"
            out = base[:i] + block + base[i:]
            mode = "maj" if BEGIN in s else "injecté"
        assert strip_block(out) == base, f"{rel}: contenu hors bloc altéré"
        io.open(p, "w", encoding="utf-8", newline="").write(out)
        print(f"OK [{mode}] {rel}")
    print("done")


if __name__ == "__main__":
    main()
