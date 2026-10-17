#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte assets/ciel-marine.css en fin de <head> de chaque page, entre marqueurs.

Idempotent : si le bloc existe, il est remplacé ; sinon il est inséré juste avant
</head>, donc après le bloc designSystem et la feuille de page (Encre & ardoise).
Opère par indices de chaîne. Ne touche ni aux données inline ni aux scripts.

Usage :  python3 tools/inject_cm.py            (injecte ou met à jour)
         python3 tools/inject_cm.py --remove   (retire le bloc, retour à Encre & ardoise)
"""
import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "ciel-marine.css")
PAGES = [
    "index.html", "briefings.html", "contact.html", "donnees.html",
    "methodologie.html", "a-propos.html", "partenariats.html", "veille.html",
    "styleguide.html",
    "observatoires/france.html", "observatoires/suisse.html",
    "observatoires/comparer.html", "observatoires/europe.html",
]
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
    css = io.open(SRC, encoding="utf-8").read().strip()
    block = BEGIN + "\n" + css + "\n" + END + "\n"
    for rel in PAGES:
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
