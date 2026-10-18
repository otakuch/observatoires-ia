#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insère la fiche pays cartographiée sous l'en-tête des pages Suisse et France.

Source unique : assets/data/fiche-pays.json (faits datés et sourcés, unités,
couches) et assets/geo/*.json (contours déjà projetés en chemins SVG).
Le nombre de métiers est lu dans metiers-ia-ch.json et metiers-ia-fr.json.

Le bloc est écrit entre marqueurs, juste après la section .dash-header :
    <!-- FICHE-PAYS:BEGIN ... -->  ...  <!-- FICHE-PAYS:END -->
Il fonctionne sans script (français, première couche) ; le script embarqué
ajoute la bascule des couches et suit la langue de la page (attribut lang de
<html>, que le moteur i18n du site met à jour).

Garde-fous : le reste de chaque page est vérifié identique octet pour octet ;
idempotent ; --remove retire le bloc ; --check sort en 1 si une page diffère
de ce que produiraient les données actuelles.

Usage : python3 tools/build_fiche_pays.py [--check | --remove]
"""
import html, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {"CH": "observatoires/suisse.html", "FR": "observatoires/france.html"}
BEGIN = "<!-- FICHE-PAYS:BEGIN · généré par tools/build_fiche_pays.py depuis assets/data/fiche-pays.json, ne pas éditer à la main -->"
END = "<!-- FICHE-PAYS:END -->"
DARK = {"#103454", "#30709C", "#5E9FCB", "#647092", "#E67E00"}
UI = {
    "fr": {"eyebrow": "Le pays en un coup d'œil", "layers": "Couche de la carte", "table": "Voir les données de la carte",
           "unit": {"CH": "Canton", "FR": "Région"}, "overseas": "Outre-mer", "overseas_note": "Formes non représentées à l'échelle.",
           "nd": "n.d.", "drom": "région d'outre-mer", "map": {"CH": "Carte des 26 cantons suisses", "FR": "Carte des 13 régions de France métropolitaine"}},
    "en": {"eyebrow": "The country at a glance", "layers": "Map layer", "table": "Show the map data",
           "unit": {"CH": "Canton", "FR": "Region"}, "overseas": "Overseas", "overseas_note": "Shapes not drawn to scale.",
           "nd": "n.a.", "drom": "overseas region", "map": {"CH": "Map of the 26 Swiss cantons", "FR": "Map of the 13 regions of mainland France"}},
}


def rd(rel):
    return io.open(os.path.join(ROOT, rel), encoding="utf-8", newline="").read()


def load(rel):
    return json.loads(rd(rel))


def esc(s):
    return html.escape(s, quote=True)


def tr(v, lang):
    return v[lang] if isinstance(v, dict) else v


def strip_block(s):
    if BEGIN not in s:
        return s
    a = s.index(BEGIN)
    b = s.index(END, a) + len(END)
    if s[b:b + 1] == "\n":
        b += 1
    return s[:a] + s[b:]


CSS = """
.fp{max-width:var(--max-w,1280px);margin:0 auto;padding:8px var(--cm-gutter,32px) 56px;box-sizing:border-box;color:var(--ink);}
.fp *{box-sizing:border-box;}
.fp-head{display:flex;flex-direction:column;gap:10px;margin-bottom:28px;}
.fp-eyebrow{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);}
.fp-title{margin:0;font-size:clamp(26px,3vw,34px);line-height:1.15;font-weight:600;letter-spacing:-.015em;}
.fp-lede{margin:0;font-size:17px;line-height:1.6;color:var(--ink-2);}
.fp-grid{display:flex;flex-wrap:wrap;gap:28px;align-items:flex-start;}
.fp-card{flex:999 1 560px;min-width:0;background:var(--surface);border-radius:12px;box-shadow:var(--shadow-1);padding:24px;display:flex;flex-direction:column;gap:16px;}
.fp-layers{display:flex;flex-wrap:wrap;gap:8px;}
.fp-layer{min-height:44px;padding:0 18px;border-radius:999px;border:0;font:600 14px var(--font-sans,inherit);cursor:pointer;background:var(--paper-2);color:var(--ink);box-shadow:inset 0 0 0 1px var(--rule);}
.fp-layer[aria-pressed="true"]{background:var(--signal);color:var(--on-signal);box-shadow:none;}
.fp-layer:focus-visible{outline:2px solid var(--signal);outline-offset:3px;}
.fp-mapwrap{display:flex;gap:20px;align-items:flex-start;}
.fp-svg{flex:1 1 auto;min-width:0;width:100%;height:auto;display:block;}
.fp-svg .fp-u{stroke:var(--surface);stroke-width:1.3;stroke-linejoin:round;transition:fill .25s;}
.fp-svg .fp-lake{fill:#EAF5FC;stroke:#A5CDE7;stroke-width:.8;}
.fp-svg text{font:700 12px var(--font-sans,sans-serif);text-anchor:middle;pointer-events:none;}
.fp-drom{flex:0 0 170px;display:flex;flex-direction:column;gap:8px;}
.fp-drom-h{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.fp-drom-t{display:flex;flex-direction:column;gap:2px;padding:10px 12px;border-radius:8px;background:#103454;color:#FFFFFF;font-size:14px;font-weight:600;}
.fp-drom-t span{font-size:12.5px;font-weight:500;color:#D9E4F2;}
.fp-drom-t.is-nd{background:repeating-linear-gradient(45deg,#EEF2F6 0 5px,#DCE3EB 5px 8px);color:#1A1D21;}
.fp-drom-t.is-nd span{color:#647092;}
.fp-drom-n{font-size:12.5px;line-height:1.5;color:var(--muted);}
.fp-legend{display:flex;flex-wrap:wrap;gap:8px 20px;margin:0;padding:0;list-style:none;font-size:14px;color:var(--ink-2);}
.fp-legend li{display:inline-flex;align-items:center;gap:8px;}
.fp-sw{width:16px;height:16px;border-radius:4px;flex:none;}
.fp-sw.is-nd{background:repeating-linear-gradient(45deg,#EEF2F6 0 4px,#B9C4D2 4px 6px);}
.fp-src,.fp-attr{margin:0;font-size:13.5px;line-height:1.55;color:var(--muted);max-width:none !important;}
.fp-src a{color:var(--signal);}
.fp-table summary{cursor:pointer;font-size:14px;font-weight:600;color:var(--signal);min-height:44px;display:flex;align-items:center;}
.fp-table table{width:100%;border-collapse:collapse;font-size:14px;margin-top:8px;display:table !important;}
.fp-table th,.fp-table td{text-align:left;padding:8px 10px;border-top:1px solid var(--rule);}
.fp-table th{font-weight:600;background:var(--paper-2);}
.fp-facts{flex:1 1 300px;max-width:400px;display:flex;flex-direction:column;gap:14px;}
.fp-fact{padding:20px 22px;border-radius:12px;background:var(--paper-2);}
.fp-v{font-size:38px;line-height:1;font-weight:600;color:var(--cm-navy,#103454);}
.fp-fact.is-accent .fp-v{color:var(--cm-orange,#D97706);}
.fp-l{margin-top:6px;font-size:15px;font-weight:600;}
.fp-s{margin-top:8px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:13.5px;color:var(--muted);}
.fp-s a{color:inherit;}
.fp-t{font-size:11.5px;font-weight:700;padding:2px 6px;border-radius:4px;box-shadow:inset 0 0 0 1px currentColor;color:var(--t1,#103454);}
.fp-langs{margin-top:10px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 16px;font-size:14px;}
.fp-langs b{font-size:20px;color:var(--cm-navy,#103454);margin-right:4px;}
.fp-note{padding:16px 18px;border-radius:12px;box-shadow:inset 0 0 0 1px var(--rule);font-size:14px;line-height:1.55;color:var(--ink-2);}
.fp-note b{color:var(--ink);}
html[data-theme="dark"] .fp-v,html[data-theme="dark"] .fp-langs b{color:#D9E4F2;}
html[data-theme="dark"] .fp-fact.is-accent .fp-v{color:var(--cm-orange);}
@media (max-width:720px){
  .fp{padding-bottom:40px;}
  .fp-mapwrap{flex-direction:column;}
  .fp-drom{flex-direction:row;flex-wrap:wrap;flex-basis:auto;}
  .fp-drom-t{flex:1 1 120px;}
  .fp-svg .fp-labels{display:none;}
  .fp-facts{max-width:none;}
  .fp-v{font-size:32px;}
}
"""

JS = r"""
(function(){
  var root=document.getElementById('fichePays'); if(!root) return;
  var D=JSON.parse(document.getElementById('fpData').textContent);
  var state={layer:D.layers[0].id};
  function lang(){ var l=(document.documentElement.lang||'fr').slice(0,2); return l==='en'?'en':'fr'; }
  function tr(v,l){ return (v&&typeof v==='object')?v[l]:v; }
  function fillOf(c){ return c==='nd'?'url(#fpNd)':c; }
  function render(){
    var l=lang(), L=null;
    D.layers.forEach(function(x){ if(x.id===state.layer) L=x; });
    root.querySelectorAll('[data-fp]').forEach(function(el){ var v=D.text[el.getAttribute('data-fp')]; if(v) el.textContent=v[l]; });
    root.querySelectorAll('.fp-layer').forEach(function(b){ var on=b.getAttribute('data-layer')===state.layer; b.setAttribute('aria-pressed',on?'true':'false'); D.layers.forEach(function(x){ if(x.id===b.getAttribute('data-layer')) b.textContent=x.label[l]; }); });
    D.units.forEach(function(u){
      var cls=L.classes[u[state.layer]], col=cls.color;
      var p=root.querySelector('[data-u="'+u.id+'"]'); if(p){ p.setAttribute('fill',fillOf(col)); var tt=p.querySelector('title'); if(tt) tt.textContent=u.name[l]+' · '+(cls.label?cls.label[l]:'' ); }
      var t=root.querySelector('[data-ut="'+u.id+'"]'); if(t) t.setAttribute('fill', D.dark.indexOf(col)>=0?'#FFFFFF':'#103454');
    });
    var lg=root.querySelector('.fp-legend'); lg.innerHTML='';
    Object.keys(L.classes).forEach(function(k){ var c=L.classes[k]; if(!c.label) return; var li=document.createElement('li'); var sw=document.createElement('span'); sw.className='fp-sw'+(c.color==='nd'?' is-nd':''); if(c.color!=='nd') sw.style.background=c.color; li.appendChild(sw); li.appendChild(document.createTextNode(c.label[l])); lg.appendChild(li); });
    var src=root.querySelector('.fp-src'); src.textContent=L.source[l]; if(L.url){ src.appendChild(document.createTextNode(' ')); var a=document.createElement('a'); a.href=L.url; a.target='_blank'; a.rel='noopener'; a.textContent=l==='en'?'Source':'Source'; src.appendChild(a); }
    var nd=L.id==='exposition';
    root.querySelectorAll('.fp-drom-t').forEach(function(t){ t.classList.toggle('is-nd',nd); var s=t.querySelector('span'); if(s) s.textContent=nd?D.ui[l].nd:D.ui[l].drom; var n=t.querySelector('b'); if(n) n.textContent=D.overseas[+t.getAttribute('data-o')][l]; });
    root.querySelectorAll('[data-cell]').forEach(function(td){ var p=td.getAttribute('data-cell').split(':'); var u=D.units[+p[0]]; var LL=null; D.layers.forEach(function(x){ if(x.id===p[1]) LL=x; }); if(p[1]==='name'){ td.textContent=u.name[l]; } else { var c=LL.classes[u[p[1]]]; td.textContent=c.label?c.label[l]:''; } });
    root.querySelectorAll('[data-th]').forEach(function(th){ var k=th.getAttribute('data-th'); if(k==='unit') th.textContent=D.ui[l].unit; else D.layers.forEach(function(x){ if(x.id===k) th.textContent=x.label[l]; }); });
  }
  root.querySelectorAll('.fp-layer').forEach(function(b){ b.addEventListener('click',function(){ state.layer=b.getAttribute('data-layer'); render(); }); });
  new MutationObserver(render).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
  render();
})();
"""


def counts():
    return {
        "@metiers_ch": str(len(load("assets/data/metiers-ia-ch.json")["metiers"])),
        "@metiers_fr": str(len(load("assets/data/metiers-ia-fr.json")["metiers"])),
    }


def block(country, C, geo):
    lang = "fr"
    cnt = counts()
    ui = UI[lang]
    L0 = C["layers"][0]
    units = C["units"]
    # textes traduisibles
    text = {"eyebrow": {"fr": UI["fr"]["eyebrow"], "en": UI["en"]["eyebrow"]},
            "title": C["title"], "lede": C["lede"], "attr": C["geo_attribution"], "note": C["note"],
            "tablesum": {"fr": UI["fr"]["table"], "en": UI["en"]["table"]},
            "ovh": {"fr": UI["fr"]["overseas"], "en": UI["en"]["overseas"]},
            "ovn": {"fr": UI["fr"]["overseas_note"], "en": UI["en"]["overseas_note"]}}
    facts_html = []
    for i, f in enumerate(C["facts"]):
        val = f["value"]
        if isinstance(val, str) and val.startswith("@"):
            val = cnt[val]
        k = f"f{i}"
        text[k + "v"] = val if isinstance(val, dict) else {"fr": val, "en": val}
        text[k + "l"] = f["label"]
        text[k + "s"] = f["source"]
        src = f'<span data-fp="{k}s">{esc(tr(f["source"], lang))}</span>'
        if f.get("url"):
            src = f'<a href="{esc(f["url"])}" target="_blank" rel="noopener">{src}</a>'
        tier = f' <span class="fp-t">{f["tier"]}</span>' if f.get("tier") else ""
        facts_html.append(
            f'<div class="fp-fact{" is-accent" if f.get("accent") else ""}"><div class="fp-v" data-fp="{k}v">{esc(tr(text[k + "v"], lang))}</div>'
            f'<div class="fp-l" data-fp="{k}l">{esc(tr(f["label"], lang))}</div><div class="fp-s">{src}{tier}</div></div>')
    if C.get("languages"):
        g = C["languages"]
        text["lgt"] = g["title"]
        text["lgs"] = g["source"]
        items = []
        for j, it in enumerate(g["items"]):
            text[f"lg{j}v"] = it["value"]
            text[f"lg{j}l"] = it["label"]
            items.append(f'<span><b data-fp="lg{j}v">{esc(tr(it["value"], lang))}</b> <span data-fp="lg{j}l">{esc(tr(it["label"], lang))}</span></span>')
        facts_html.insert(2,
            f'<div class="fp-fact"><div class="fp-l" data-fp="lgt">{esc(tr(g["title"], lang))}</div><div class="fp-langs">{"".join(items)}</div>'
            f'<div class="fp-s"><a href="{esc(g["url"])}" target="_blank" rel="noopener"><span data-fp="lgs">{esc(tr(g["source"], lang))}</span></a> <span class="fp-t">{g["tier"]}</span></div></div>')
    facts_html.append(f'<div class="fp-note" data-fp="note">{esc(tr(C["note"], lang))}</div>')

    # carte
    if country == "CH":
        vb, w, h = "0 0 760 480", 760, 480
        shapes, cents = geo["cantons"], geo["centroids"]
    else:
        vb, w, h = "0 0 560 560", 560, 560
        shapes, cents = geo["regions"], geo["centroids"]
    paths, labels = [], []
    for u in units:
        cls = L0["classes"][u[L0["id"]]]
        col = cls["color"]
        fill = "url(#fpNd)" if col == "nd" else col
        tip = tr(u["name"], lang) + (" · " + tr(cls["label"], lang) if cls.get("label") else "")
        paths.append(f'<path class="fp-u" data-u="{u["id"]}" d="{shapes[u["id"]]}" fill="{fill}"><title>{esc(tip)}</title></path>')
        x, y = cents[u["id"]]
        labels.append(f'<text data-ut="{u["id"]}" x="{x}" y="{y + 4}" fill="{"#FFFFFF" if col in DARK else "#103454"}">{u["abbr"]}</text>')
    lakes = "".join(f'<path class="fp-lake" d="{d}"></path>' for d in geo.get("lakes", []))
    svg = (f'<svg class="fp-svg" viewBox="{vb}" width="{w}" height="{h}" role="img" aria-label="{esc(ui["map"][country])}">'
           '<defs><pattern id="fpNd" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           '<rect width="8" height="8" fill="#EEF2F6"></rect><line x1="0" y1="0" x2="0" y2="8" stroke="#B9C4D2" stroke-width="3"></line></pattern></defs>'
           f'<g>{"".join(paths)}</g><g>{lakes}</g><g class="fp-labels" aria-hidden="true">{"".join(labels)}</g></svg>')
    drom = ""
    if C.get("overseas"):
        tiles = "".join(f'<div class="fp-drom-t" data-o="{i}"><b>{esc(o[lang])}</b><span>{ui["drom"]}</span></div>' for i, o in enumerate(C["overseas"]))
        drom = f'<div class="fp-drom"><span class="fp-drom-h" data-fp="ovh">{ui["overseas"]}</span>{tiles}<span class="fp-drom-n" data-fp="ovn">{ui["overseas_note"]}</span></div>'
    def swatch(c):
        if c["color"] == "nd":
            return '<span class="fp-sw is-nd"></span>'
        return f'<span class="fp-sw" style="background:{c["color"]}"></span>'
    legend = "".join(f'<li>{swatch(c)}{esc(tr(c["label"], lang))}</li>' for c in L0["classes"].values() if c.get("label"))
    buttons = "".join(
        f'<button type="button" class="fp-layer" data-layer="{x["id"]}" aria-pressed="{"true" if i == 0 else "false"}">{esc(tr(x["label"], lang))}</button>'
        for i, x in enumerate(C["layers"]))
    # tableau accessible
    heads = '<th data-th="unit">' + ui["unit"][country] + "</th>" + "".join(f'<th data-th="{x["id"]}">{esc(tr(x["label"], lang))}</th>' for x in C["layers"])
    rows = []
    for i, u in enumerate(units):
        cells = [f'<td data-cell="{i}:name">{esc(tr(u["name"], lang))}</td>']
        for x in C["layers"]:
            c = x["classes"][u[x["id"]]]
            cells.append(f'<td data-cell="{i}:{x["id"]}">{esc(tr(c["label"], lang)) if c.get("label") else ""}</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    src0 = esc(tr(L0["source"], lang))
    if L0.get("url"):
        src0 += f' <a href="{esc(L0["url"])}" target="_blank" rel="noopener">Source</a>'
    data = {"layers": C["layers"], "units": units, "overseas": C.get("overseas", []), "text": text, "dark": sorted(DARK),
            "ui": {l: {"nd": UI[l]["nd"], "drom": UI[l]["drom"], "unit": UI[l]["unit"][country]} for l in UI}}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return (BEGIN + "\n"
            f'<section class="fp" id="fichePays" aria-labelledby="fpTitle" data-country="{country}">\n'
            f"<style>{CSS}</style>\n"
            f'<div class="fp-head"><span class="fp-eyebrow" data-fp="eyebrow">{ui["eyebrow"]}</span>'
            f'<h2 class="fp-title" id="fpTitle" data-fp="title">{esc(tr(C["title"], lang))}</h2>'
            f'<p class="fp-lede" data-fp="lede">{esc(tr(C["lede"], lang))}</p></div>\n'
            '<div class="fp-grid">\n'
            f'<div class="fp-card"><div class="fp-layers" role="group" aria-label="{ui["layers"]}">{buttons}</div>'
            f'<div class="fp-mapwrap">{svg}{drom}</div>'
            f'<ul class="fp-legend">{legend}</ul><p class="fp-src">{src0}</p>'
            f'<p class="fp-attr" data-fp="attr">{esc(tr(C["geo_attribution"], lang))}</p>'
            f'<details class="fp-table"><summary data-fp="tablesum">{ui["table"]}</summary><div style="overflow-x:auto"><table><thead><tr>{heads}</tr></thead><tbody>{"".join(rows)}</tbody></table></div></details></div>\n'
            f'<aside class="fp-facts">{"".join(facts_html)}</aside>\n'
            "</div>\n"
            f'<script type="application/json" id="fpData">{payload}</script>\n'
            f"<script>{JS}</script>\n"
            "</section>\n" + END + "\n")


def main():
    mode = "--check" if "--check" in sys.argv else ("--remove" if "--remove" in sys.argv else "")
    data = load("assets/data/fiche-pays.json")
    drift = 0
    for C in data["countries"]:
        rel = PAGES[C["code"]]
        s = rd(rel)
        base = strip_block(s)
        if mode == "--remove":
            out = base
        else:
            m = re.search(r'<section class="dash-header">.*?</section>\n?', base, re.S)
            if not m:
                print("ARRÊT :", rel, "section .dash-header introuvable")
                sys.exit(2)
            geo = load(C["geo"])
            out = base[:m.end()] + block(C["code"], C, geo) + base[m.end():]
        assert strip_block(out) == base, rel
        if out != s:
            drift += 1
            print(("À METTRE À JOUR " if mode == "--check" else "OK [écrit] ") + rel)
            if mode != "--check":
                io.open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="").write(out)
        else:
            print("OK [à jour] " + rel)
    if mode == "--check" and drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
