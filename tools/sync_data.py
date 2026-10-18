#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Relie chaque page aux fichiers de données de référence.

Les pages sont autonomes : chacune embarque des copies de données et des
chiffres écrits dans le texte. Ce script les dérive tous de assets/data/ (et
du catalogue des dépêches de briefings.html), sans jamais modifier un fichier
de données. Ce qu'il relie :

  1. Littéraux embarqués      veille.json -> window.VEILLE_DATA
                              observatoires.json -> window.OBSERVATOIRES_DATA
  2. Replis hors ligne        franceExpData, swissExpData, compareExpData,
                              diffusionData : projection exacte des fichiers
                              ai-exposure-*.json et ai-diffusion-microsoft.json
  3. Cohérence des radars     cmpRadarData (Comparer) = frRadarData + chRadarData
  4. Chiffres dans le texte   nombre de métiers, d'observatoires, d'indicateurs,
                              de jalons, d'économistes, de rapports de veille,
                              période couverte (accueil, méthodologie, à propos,
                              partenariats, pages pays, balise description)
  5. Dernière dépêche         bloc « Dernière dépêche » de l'accueil = numéro le
                              plus récent du catalogue BRIEFINGS (briefings.html)
  6. Veille du mois           sur-titre de la veille de l'accueil = mois de la
                              publication la plus récente
  7. Pied de page             date de dernière mise à jour (donnée la plus
                              récente) et version (première entrée du CHANGELOG)
  8. Page Données             entrées et poids affichés, et liste générée de tous
                              les jeux de données analytiques

Garde-fous : chaque remplacement est localisé (marqueurs, clés i18n ou motif
ancré) et doit trouver exactement le nombre d'occurrences attendu, sinon le
script s'arrête sans rien écrire. Les littéraux de données réécrits sont relus
et comparés à la source. Idempotent.

Usage : python3 tools/sync_data.py [--check]
        --check : n'écrit rien, liste les écarts, code de sortie 1 s'il y en a.
"""
import glob, html, io, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "assets", "data")

PAGES = [
    "index.html", "briefings.html", "contact.html", "donnees.html",
    "methodologie.html", "a-propos.html", "partenariats.html", "veille.html",
    "observatoires/france.html", "observatoires/suisse.html",
    "observatoires/comparer.html", "observatoires/europe.html",
]
TARGETS = ["assets/components.js"] + PAGES
# Sous-pages : seul le pied de page (date de mise à jour, version) est relié
FOOTER_ONLY = [
    "briefings/01-banque-suisse.html", "briefings/02-cadres-france.html",
    "briefings/02-cadres-france-postfactum.html", "briefings/03-luxe-horlogerie.html",
    "briefings/04-agents-ia-france.html",
    "infographies/matrice-france.html", "infographies/matrice-suisse.html",
]

LITERALS = {
    "VEILLE_DATA": "veille.json",
    "OBSERVATOIRES_DATA": "observatoires.json",
}

# (page, id du bloc JSON, fichier de référence, clé de liste, clé d'appariement,
#  champs propres au repli conservés tels quels)
FALLBACKS = [
    ("observatoires/france.html", "franceExpData", "ai-exposure-france.json", "families", "code", ()),
    ("observatoires/suisse.html", "swissExpData", "ai-exposure-switzerland.json", "families", "code", ()),
    ("observatoires/comparer.html", "compareExpData", "ai-exposure-compare.json", "families", "code", ()),
    ("observatoires/comparer.html", "diffusionData", "ai-diffusion-microsoft.json", "countries", "code", ("color",)),
    ("observatoires/comparer.html", "diffusionData", "ai-diffusion-microsoft.json", "periods", None, ()),
]

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


class Abort(Exception):
    pass


def rd(rel):
    return io.open(os.path.join(ROOT, rel), encoding="utf-8", newline="").read()


def load(name):
    return json.load(io.open(os.path.join(DATA, name), encoding="utf-8"))


def js_str(value):
    """Contenu d'une chaîne JS entre guillemets doubles."""
    return json.dumps(value, ensure_ascii=False)[1:-1]


def fr_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{'1er' if d == 1 else d} {MOIS[m - 1]} {y}"


# --------------------------------------------------------------------------
# Valeurs dérivées des données
# --------------------------------------------------------------------------
def derive():
    v = {}
    veille = load("veille.json")
    obs = load("observatoires.json")
    mfr = load("metiers-ia-fr.json")["metiers"]
    mch = load("metiers-ia-ch.json")["metiers"]
    ifr = load("indicateurs-ia-fr.json")["indicators"]
    ich = load("indicateurs-ia-ch.json")["indicators"]
    ev = load("timeline-ia-emploi.json")["events"]
    efr = load("economistes-ia.json")["economists"]
    ech = load("economistes-ia-ch.json")["economists"]
    years = [int(y) for e in ev for y in re.findall(r"(?:19|20)\d\d", str(e.get("year", "")))]

    v["metiers_fr"] = len(mfr)
    v["metiers_ch"] = len(mch)
    v["metiers"] = len(mfr) + len(mch)
    v["domaines_ch"] = len({m["np_domain"] for m in mch})
    v["observatoires"] = len(obs)
    v["ind_fr"] = len(ifr)
    v["ind_ch"] = len(ich)
    v["ind"] = len(ifr) + len(ich)
    v["ind_fr_max_sources"] = max(i["n_sources"] for i in ifr)
    v["jalons"] = len(ev)
    v["jalons_periode"] = f"{min(years)}-{max(years)}"
    # Économistes : personnes distinctes (un nom peut apparaître deux fois)
    v["eco_fr"] = len({e["name"] for e in efr})
    v["eco_ch"] = len({e["name"] for e in ech})
    v["eco"] = len({e["name"] for e in efr} | {e["name"] for e in ech})
    v["veille"] = len(veille)
    v["veille_last"] = max(x["date"] for x in veille)

    compiled = []
    for p in glob.glob(os.path.join(DATA, "*.json")):
        d = json.load(io.open(p, encoding="utf-8"))
        if isinstance(d, dict) and d.get("compiled_at"):
            compiled.append(d["compiled_at"][:10])
    v["catalog"] = briefings_catalog()
    published = [b for b in v["catalog"] if not b.get("upcoming")]
    latest = sorted(published, key=lambda b: (b["date"], b["num"]))[-1]
    v["dispatch"] = latest
    v["last_update"] = max(compiled + [v["veille_last"], latest["date"]])
    v["version"], v["version_date"] = changelog_head()
    return v


def briefings_catalog():
    s = rd("briefings.html")
    a = s.index("const BRIEFINGS = [")
    b = s.index("\n];", a)
    literal = s[a + len("const BRIEFINGS = "):b + 2]
    out = subprocess.run(
        ["node", "-e", "let s='';process.stdin.on('data',d=>s+=d).on('end',()=>{"
         "const v=(new Function('return '+s))();process.stdout.write(JSON.stringify(v));})"],
        input=literal, capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def changelog_head():
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\] · (\d{4}-\d{2}-\d{2})", rd("CHANGELOG.md"), re.M)
    if not m:
        raise Abort("CHANGELOG.md : première entrée de version introuvable")
    return m.group(1), m.group(2)


# --------------------------------------------------------------------------
# Outils de remplacement
# --------------------------------------------------------------------------
def literal_span(s, start):
    """Fin du littéral [..] ou {..} qui commence à l'indice start."""
    opening = s[start]
    closing = {"[": "]", "{": "}"}[opening]
    depth, k, in_str, esc = 0, start, None, False
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
                return k + 1
        k += 1
    raise Abort("littéral non fermé")


def window_literal(s, name):
    i = s.find("window." + name)
    if i < 0:
        return None
    j = s.index("=", i) + 1
    while s[j].isspace():
        j += 1
    return j, literal_span(s, j)


def bind(s, pattern, values, expect, label):
    """Remplace les groupes nommés de chaque occurrence du motif par values[nom]."""
    rx = re.compile(pattern)
    matches = list(rx.finditer(s))
    if len(matches) != expect:
        raise Abort(f"{label} : {len(matches)} occurrence(s) au lieu de {expect}")
    out, last, notes = [], 0, []
    for m in matches:
        cuts = sorted((m.start(g), m.end(g), g) for g in rx.groupindex if m.group(g) is not None)
        for a, b, g in cuts:
            new = str(values[g])
            out.append(s[last:a])
            out.append(new)
            if s[a:b] != new:
                notes.append(f"{label} {g} {s[a:b]} -> {new}")
            last = b
    out.append(s[last:])
    return "".join(out), notes


def i18n_set(s, key, values, label):
    """Fixe la valeur d'une clé i18n, une valeur par langue, dans l'ordre fr, en."""
    rx = re.compile(r'("' + re.escape(key) + r'":\s*")((?:[^"\\]|\\.)*)(")')
    ms = list(rx.finditer(s))
    if len(ms) != len(values):
        raise Abort(f"{label} : clé {key} trouvée {len(ms)} fois au lieu de {len(values)}")
    notes = []
    for m, val in sorted(zip(ms, values), key=lambda t: -t[0].start()):
        new = js_str(val)
        if m.group(2) != new:
            notes.append(f"{label} {key}")
            s = s[:m.start(2)] + new + s[m.end(2):]
    return s, notes


# --------------------------------------------------------------------------
# 1 et 2 · littéraux et replis
# --------------------------------------------------------------------------
def sync_literals(rel, s):
    notes = []
    spans = []
    for name, fname in LITERALS.items():
        sp = window_literal(s, name)
        if sp:
            spans.append((sp, name, load(fname)))
    for (a, b), name, data in sorted(spans, key=lambda t: -t[0][0]):
        if json.loads(s[a:b]) == data:
            continue
        before = len(json.loads(s[a:b]))
        lit = json.dumps(data, ensure_ascii=False)
        out = s[:a] + lit + s[b:]
        assert out[:a] == s[:a] and json.loads(out[a:a + len(lit)]) == data, rel
        s = out
        notes.append(f"{name} {before} -> {len(data)}")
    return s, notes


def blob_span(s, bid):
    m = re.search(r'<script[^>]*id="' + re.escape(bid) + r'"[^>]*>', s)
    if not m:
        raise Abort(f"bloc {bid} introuvable")
    a = m.end()
    b = s.index("</script>", a)
    return a, b


def sync_fallbacks(rel, s):
    notes = []
    for page, bid, fname, key, match_key, keep in FALLBACKS:
        if page != rel:
            continue
        a, b = blob_span(s, bid)
        raw = s[a:b]
        blob = json.loads(raw)
        ref = load(fname)[key]
        cur = blob[key]
        if match_key:
            by_code = {x[match_key]: x for x in cur}
            new = []
            for item in ref:
                old = by_code.get(item[match_key], {})
                fields = list(old.keys()) if old else (list(cur[0].keys()) if cur else [])
                row = {}
                for f in fields:
                    row[f] = old.get(f) if f in keep and f in old else item.get(f)
                new.append(row)
        else:
            new = ref
        if new == cur:
            continue
        blob[key] = new
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        s = s[:a] + lead + json.dumps(blob, ensure_ascii=False) + trail + s[b:]
        notes.append(f"repli {bid}.{key} resynchronisé sur {fname}")
    return s, notes


def check_radars():
    def blob(rel, bid):
        s = rd(rel)
        a, b = blob_span(s, bid)
        return json.loads(s[a:b])
    fr = blob("observatoires/france.html", "frRadarData")
    ch = blob("observatoires/suisse.html", "chRadarData")
    cmp_ = blob("observatoires/comparer.html", "cmpRadarData")
    errs = []
    if not (len(fr) == len(ch) == len(cmp_)):
        errs.append("radars : nombre de familles différent")
    for a, b, c in zip(fr, ch, cmp_):
        for src, row, suffix in (("France", a, "FR"), ("Suisse", b, "CH")):
            for k, val in row.items():
                ck = {"theo": "theo" + suffix, "usage": "usage" + suffix, "src": "src" + suffix}.get(k, k)
                if ck in c and c[ck] != val:
                    errs.append(f"radar {c['k']!r} : {ck} {src}={val} Comparer={c[ck]}")
    return errs


# --------------------------------------------------------------------------
# 4 · chiffres dans le texte
# --------------------------------------------------------------------------
def bindings(v):
    n = r"(?P<%s>\d+)"
    return {
        "index.html": [
            (r'name="description" content="' + n % "metiers" + r' métiers cartographiés, ' + n % "observatoires" + r' observatoires', 1, "description"),
            (r'<div class="stat-num">' + n % "metiers" + r'</div>\s*<div class="stat-label" data-i18n="home\.stat3\.label">', 1, "chiffre 3"),
            (r'"home\.stat3\.label": "(?:métiers cartographiés|occupations mapped) \(' + n % "metiers_fr" + r' ROME France \+ ' + n % "metiers_ch" + r' NP 2010', 2, "chiffre 3 libellé"),
        ],
        "partenariats.html": [
            (r'commun éditorial : ' + n % "metiers" + r' métiers cartographiés, ' + n % "observatoires" + r' observatoires', 1, "pourquoi FR"),
            (r'editorial commons: ' + n % "metiers" + r' occupations mapped, ' + n % "observatoires" + r' CH and FR', 1, "pourquoi EN"),
        ],
        "a-propos.html": [
            (r"\(" + n % "metiers" + r" métiers cartographiés, " + n % "ind" + r" indicateurs, " + n % "jalons" + r" jalons timeline, " + n % "eco" + r" économistes référencés, " + n % "veille" + r" rapports de veille\)", 1, "principe 3 FR"),
            (r"\(" + n % "metiers" + r" occupations mapped, " + n % "ind" + r" indicators, " + n % "jalons" + r" timeline milestones, " + n % "eco" + r" referenced economists, " + n % "veille" + r" veille reports\)", 1, "principe 3 EN"),
        ],
        "methodologie.html": [
            (r"(?:pour|for) " + n % "metiers_fr" + r" (?:métiers ROME|ROME occupations)", 2, "d1"),
            (r"indicateurs-ia-fr\.json</strong> · " + n % "ind_fr" + r" (?:indicateurs|prospective indicators)", 2, "d2"),
            (r"(?:jusqu'à|up to) " + n % "ind_fr_max_sources" + r" sources", 2, "d2 sources"),
            (r"timeline-ia-emploi\.json</strong> · " + n % "jalons" + r" (?:jalons|milestones) (?P<jalons_periode>\d{4}-\d{4})", 2, "d3"),
            (r"economistes-ia\.json</strong> · " + n % "eco_fr" + r" (?:économistes référencés|referenced economists)", 2, "d5"),
            (r"(?:pour|for) " + n % "metiers_ch" + r" (?:métiers NP 2010|NP 2010 occupations)", 2, "d6"),
            (r"(?:Couvre les|Covers all) " + n % "domaines_ch" + r" (?:grands domaines|main)", 2, "d6 domaines"),
            (r"indicateurs-ia-ch\.json</strong> · " + n % "ind_ch" + r" (?:indicateurs|prospective indicators)", 2, "d7"),
            (r"economistes-ia-ch\.json</strong> · " + n % "eco_ch" + r" (?:économistes|economists)", 2, "d9"),
            (r"Total ?: " + n % "metiers" + r" (?:métiers|occupations) \(FR \+ CH\), " + n % "ind" + r" (?:indicateurs|indicators), " + n % "jalons" + r" (?:jalons|milestones), " + n % "eco" + r" (?:économistes|economists)", 2, "total"),
        ],
        "observatoires/france.html": [
            (r"(?:explorer|Explorez) les " + n % "metiers_fr" + r" métiers (?:ROME|français) cartographiés", 2, "métiers FR"),
            (r"(?:dashboard France couvre|France dashboard covers) " + n % "metiers_fr" + r" (?:métiers|occupations)", 2, "couverture FR"),
        ],
        "observatoires/suisse.html": [
            (r"(?:explorer|Explorez) les " + n % "metiers_ch" + r" métiers (?:suisses )?cartographiés", 2, "métiers CH"),
            (r"(?:dashboard suisse couvre|Swiss dashboard covers) " + n % "metiers_ch" + r" (?:métiers|occupations)", 2, "couverture CH"),
        ],
    }


def sync_bindings(rel, s, v):
    notes = []
    for pattern, expect, label in bindings(v).get(rel, []):
        s, nn = bind(s, pattern, v, expect, label)
        notes += nn
    return s, notes


# --------------------------------------------------------------------------
# 5, 6, 7 · dernière dépêche, veille du mois, pied de page
# --------------------------------------------------------------------------
def dispatch_title_html(title):
    t = title.strip()
    end = "." if not t.endswith((".", "?", "!")) else ""
    if " · " in t:
        a, b = t.split(" · ", 1)
        return f"{a} · <em>{b.rstrip('.')}</em>{'.' if t.endswith('.') or end else ''}"
    parts = re.split(r"(?<=\.)\s+", t, maxsplit=1)
    if len(parts) == 2:
        return f"{parts[0]} <em>{parts[1].rstrip('.')}</em>."
    return t + end


def sync_home(s, v):
    d = v["dispatch"]
    y, m, _ = d["date"].split("-")
    num_fr = f"Le Dispatch·iA · #{d['num']} · {MOIS[int(m) - 1]} {y}"
    num_en = f"The Dispatch·iA · #{d['num']} · {MONTHS[int(m) - 1]} {y}"
    notes = []
    s, nn = i18n_set(s, "home.dispatch.num", [num_fr, num_en], "dernière dépêche"); notes += nn
    s, nn = i18n_set(s, "home.dispatch.title", [dispatch_title_html(d["title"]["fr"]), dispatch_title_html(d["title"]["en"])], "dernière dépêche"); notes += nn
    s, nn = i18n_set(s, "home.dispatch.lede", [d["summary"]["fr"], d["summary"]["en"]], "dernière dépêche"); notes += nn
    href = "briefings/" + d["slug"] + ".html"
    if not os.path.exists(os.path.join(ROOT, href)):
        raise Abort(f"dépêche #{d['num']} : fichier {href} absent")
    s, nn = bind(s, r'<div class="dispatch-tease-actions">\s*<a href="(?P<href>[^"]+)" class="btn btn-primary">',
                 {"href": href}, 1, "lien dernière dépêche"); notes += nn
    vy, vm, _ = v["veille_last"].split("-")
    s, nn = i18n_set(s, "home.veille.eyebrow",
                     [f"Veille · {MOIS[int(vm) - 1].capitalize()} {vy}", f"Field report · {MONTHS[int(vm) - 1]} {vy}"],
                     "veille du mois"); notes += nn
    return s, notes


def sync_footer(rel, s, v):
    notes = []
    vals = {"date": fr_date(v["last_update"]),
            "ver": f"v{v['version']} · build {v['version_date'].replace('-', '.')}"}
    s, nn = bind(s, r'data-i18n="foot\.lastupdate">\$\{t\("foot\.lastupdate"\)\}</span>\s*<strong>(?P<date>[^<]+)</strong>',
                 vals, 1, "pied · mise à jour"); notes += nn
    s, nn = bind(s, r'<div class="foot-version mono">(?P<ver>[^<]+)</div>', vals, 1, "pied · version"); notes += nn
    return s, notes


def sync_footer_matrix(s, v):
    return bind(s, r"L\.lastupdate \+ ' \\u00b7 <strong>(?P<date>[^<]+)</strong>",
                {"date": fr_date(v["last_update"])}, 1, "pied · mise à jour")


# --------------------------------------------------------------------------
# 8 · page Données
# --------------------------------------------------------------------------
ANALYTICS_BEGIN = "<!-- DATASETS:BEGIN · généré par tools/sync_data.py, ne pas éditer à la main -->"
ANALYTICS_END = "<!-- DATASETS:END -->"


def dataset_rows():
    rows = []
    for p in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        name = os.path.basename(p)
        if name in LITERALS.values():
            continue
        d = json.load(io.open(p, encoding="utf-8"))
        lists = [(k, len(x)) for k, x in d.items() if isinstance(x, list) and k not in ("source_urls", "source_secondary", "periods")]
        key, count = lists[0]
        scope = d.get("scope")
        if not scope and isinstance(d.get("context"), dict):
            ctx = d["context"]["fr"]
            scope = re.sub(r"<[^>]+>", "", ctx.get("title") or ctx.get("headline") or "")
        rows.append({
            "name": name, "count": count,
            "kb": max(1, round(os.path.getsize(p) / 1024)),
            "date": (d.get("compiled_at") or "")[:10],
            "scope": scope or "",
        })
    return rows


def analytics_block(rows):
    cards = []
    for r in rows:
        cards.append(
            '  <div class="dl-card">\n'
            '    <div class="dl-format">JSON · UTF-8</div>\n'
            f'    <h3 class="dl-name">{r["name"]}</h3>\n'
            '    <div class="dl-meta">\n'
            f'      <span><span data-i18n="dn.records"></span> {r["count"]}</span>\n'
            f'      <span>~{r["kb"]} KB</span>\n'
            f'      <span><span data-i18n="dn.compiled"></span> {r["date"]}</span>\n'
            '    </div>\n'
            f'    <p class="dl-desc">{html.escape(r["scope"], quote=False)}</p>\n'
            '    <div class="dl-actions">\n'
            f'      <a class="dl-btn primary" href="assets/data/{r["name"]}" download><span data-i18n="dn.download"></span> .json</a>\n'
            '    </div>\n'
            '  </div>')
    return (ANALYTICS_BEGIN + "\n"
            '<div class="section-head">\n'
            f'  <div class="section-eyebrow mono"><span data-i18n="dn.ds.eyebrow"></span> · {len(rows)}</div>\n'
            '  <h2 class="section-title" data-i18n="dn.ds.title"></h2>\n'
            '  <p class="section-sub" data-i18n="dn.ds.sub"></p>\n'
            '</div>\n\n'
            '<div class="dl-grid dl-grid--datasets">\n' + "\n\n".join(cards) + "\n</div>\n" + ANALYTICS_END)


def sync_donnees(s):
    notes = []
    for fname in LITERALS.values():
        n = len(load(fname))
        kb = max(1, round(os.path.getsize(os.path.join(DATA, fname)) / 1024))
        s, nn = bind(s, r'<h3 class="dl-name">' + re.escape(fname) +
                     r'</h3>\s*<div class="dl-meta">\s*<span><span data-i18n="dn.records"></span> (?P<n>\d+)</span>\s*<span>~(?P<kb>\d+) KB</span>',
                     {"n": n, "kb": kb}, 1, fname)
        notes += nn
    block = analytics_block(dataset_rows())
    if ANALYTICS_BEGIN in s:
        a = s.index(ANALYTICS_BEGIN)
        b = s.index(ANALYTICS_END, a) + len(ANALYTICS_END)
        if s[a:b] != block:
            s = s[:a] + block + s[b:]
            notes.append("liste des jeux de données mise à jour")
    else:
        anchor = "<!-- SCHEMA -->"
        if s.count(anchor) != 1:
            raise Abort("donnees.html : ancre <!-- SCHEMA --> introuvable")
        s = s.replace(anchor, block + "\n\n" + anchor)
        notes.append("liste des jeux de données ajoutée")
    return s, notes


# --------------------------------------------------------------------------
def main():
    check = "--check" in sys.argv
    try:
        v = derive()
        results = []
        for rel in TARGETS:
            s0 = rd(rel)
            s, notes = sync_literals(rel, s0)
            if rel != "assets/components.js":
                s, nn = sync_fallbacks(rel, s); notes += nn
                s, nn = sync_bindings(rel, s, v); notes += nn
            if rel == "index.html":
                s, nn = sync_home(s, v); notes += nn
            if rel == "donnees.html":
                s, nn = sync_donnees(s); notes += nn
            s, nn = sync_footer(rel, s, v); notes += nn
            results.append((rel, s0, s, notes))
        for rel in FOOTER_ONLY:
            s0 = rd(rel)
            if rel.startswith("infographies/"):
                s, notes = sync_footer_matrix(s0, v)
            else:
                s, notes = sync_footer(rel, s0, v)
            results.append((rel, s0, s, notes))
        radar_errors = check_radars()
    except Abort as e:
        print("ARRÊT :", e)
        sys.exit(2)

    drift = 0
    for rel, s0, s, notes in results:
        if s != s0:
            drift += 1
            print(f"{'À SYNCHRONISER' if check else 'OK [synchronisé]'} {rel}")
            for n in notes:
                print("   ·", n)
            if not check:
                io.open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="").write(s)
        else:
            print(f"OK [à jour] {rel}")
    for e in radar_errors:
        print("INCOHÉRENCE", e)
    d = v["dispatch"]
    print(f"\nDernière dépêche #{d['num']} ({d['date']}) · veille {v['veille']} entrées, dernière {v['veille_last']}"
          f" · mise à jour affichée {fr_date(v['last_update'])} · v{v['version']}")
    if check and (drift or radar_errors):
        sys.exit(1)


if __name__ == "__main__":
    main()
