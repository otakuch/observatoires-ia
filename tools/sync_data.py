#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Relie chaque page aux fichiers de données de référence.

Les pages sont autonomes : chacune embarque une copie de window.VEILLE_DATA et
window.OBSERVATOIRES_DATA dans son script partagé. Ces copies dérivent quand
assets/data/*.json avance. Ce script les remplace par le contenu exact des
fichiers de référence, sans modifier aucune valeur :

  assets/data/veille.json        -> window.VEILLE_DATA
  assets/data/observatoires.json -> window.OBSERVATOIRES_DATA

Il met aussi à jour, sur donnees.html, le nombre d'entrées et le poids affichés
pour chaque fichier téléchargeable.

Garde-fous : seul le littéral de données est remplacé (repéré par appariement
de crochets, chaînes comprises) ; le reste du fichier est vérifié identique
octet pour octet ; le littéral réécrit est relu et comparé au JSON source.
Idempotent. Usage : python3 tools/sync_data.py [--check]
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = [
    "assets/components.js",
    "index.html", "briefings.html", "contact.html", "donnees.html",
    "methodologie.html", "a-propos.html", "partenariats.html", "veille.html",
    "observatoires/france.html", "observatoires/suisse.html",
    "observatoires/comparer.html", "observatoires/europe.html",
]
SOURCES = {
    "VEILLE_DATA": "assets/data/veille.json",
    "OBSERVATOIRES_DATA": "assets/data/observatoires.json",
}


def literal_span(s, name):
    """Début et fin du littéral [..] ou {..} affecté à window.<name>."""
    i = s.find("window." + name)
    if i < 0:
        return None
    j = s.index("=", i) + 1
    while s[j].isspace():
        j += 1
    opening = s[j]
    closing = {"[": "]", "{": "}"}[opening]
    depth, k, in_str, esc = 0, j, None, False
    while k < len(s):
        c = s[k]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == in_str:
                in_str = None
        elif c in "\"'`":
            in_str = c
        elif c == opening:
            depth += 1
        elif c == closing:
            depth -= 1
            if depth == 0:
                return j, k + 1
        k += 1
    raise ValueError(f"littéral {name} non fermé")


def load(rel):
    return json.load(io.open(os.path.join(ROOT, rel), encoding="utf-8"))


def main():
    check = "--check" in sys.argv
    data = {name: load(rel) for name, rel in SOURCES.items()}
    literals = {name: json.dumps(d, ensure_ascii=False) for name, d in data.items()}
    drift = 0
    for rel in TARGETS:
        p = os.path.join(ROOT, rel)
        s = io.open(p, encoding="utf-8", newline="").read()
        out = s
        notes = []
        # Remplacer en partant de la fin pour garder les indices valides
        spans = []
        for name in SOURCES:
            sp = literal_span(out, name)
            if sp:
                spans.append((sp, name))
        for (a, b), name in sorted(spans, reverse=True):
            current = json.loads(out[a:b]) if out[a] in "[{" else None
            if current == data[name]:
                continue
            before = len(current) if isinstance(current, list) else "?"
            out = out[:a] + literals[name] + out[b:]
            notes.append(f"{name} {before} -> {len(data[name])}")
            # Garde-fou : le reste du fichier est inchangé
            assert out[:a] == s[:a], rel
            assert json.loads(out[a:a + len(literals[name])]) == data[name], rel
        if rel == "donnees.html":
            out, n = update_download_meta(out)
            notes += n
        if out != s:
            drift += 1
            print(f"{'À SYNCHRONISER' if check else 'OK [synchronisé]'} {rel} · " + " · ".join(notes))
            if not check:
                io.open(p, "w", encoding="utf-8", newline="").write(out)
        else:
            print(f"OK [à jour] {rel}")
    if check and drift:
        sys.exit(1)


def update_download_meta(s):
    notes = []
    for fname in ("observatoires.json", "veille.json"):
        rel = "assets/data/" + fname
        n = len(load(rel))
        kb = max(1, round(os.path.getsize(os.path.join(ROOT, rel)) / 1024))
        pat = re.compile(
            r'(<h3 class="dl-name">' + re.escape(fname) +
            r'</h3>\s*<div class="dl-meta">\s*<span><span data-i18n="dn.records"></span> )(\d+)(</span>\s*<span>~)(\d+)( KB</span>)'
        )
        m = pat.search(s)
        assert m, f"donnees.html : carte {fname} introuvable"
        new = m.group(1) + str(n) + m.group(3) + str(kb) + m.group(5)
        if m.group(0) != new:
            notes.append(f"{fname} affiché {m.group(2)} entrées ~{m.group(4)} KB -> {n} entrées ~{kb} KB")
            s = s[:m.start()] + new + s[m.end():]
    return s, notes


if __name__ == "__main__":
    main()
