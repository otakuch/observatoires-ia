#!/usr/bin/env python3
"""
Build self-contained HTML files by inlining CSS and components.js.
Reads from src/ and writes to repo root (deployable directly via GitHub Pages).

Usage from repo root:
    python3 scripts/build.py
"""
import os
import re
import shutil
import datetime
from pathlib import Path

# Paths relative to repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = REPO_ROOT / "src"
SITE_OUT = REPO_ROOT
SITE_URL = "https://observatoire.naullynicolas.ch"

# Snippet to inject in every <head> just before </head>
HEAD_INJECT = """<!-- Canonical & Social -->
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="observatoire[s]·ia">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="fr_FR">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@naullyn">
<meta name="theme-color" content="#D03C2F">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q52TZ7QT84"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-Q52TZ7QT84');
</script>
"""

# Read shared assets
with open(SITE_SRC / "assets" / "style.css", "r", encoding="utf-8") as f:
    CSS = f.read()

with open(SITE_SRC / "assets" / "components.js", "r", encoding="utf-8") as f:
    JS = f.read()


def bundle(src_path: Path, dst_path: Path):
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(
        r'<link\s+rel="stylesheet"\s+href="(?:\.\./)?assets/style\.css">',
        f"<style>\n{CSS}\n</style>",
        html,
    )
    html = re.sub(
        r'<script\s+src="(?:\.\./)?assets/components\.js"></script>',
        f"<script>\n{JS}\n</script>",
        html,
    )

    rel = dst_path.relative_to(SITE_OUT)
    if str(rel) == "index.html":
        canonical = SITE_URL + "/"
    else:
        canonical = SITE_URL + "/" + str(rel).replace(os.sep, "/")

    head_block = HEAD_INJECT.format(canonical=canonical)
    html = html.replace("</head>", head_block + "</head>", 1)

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  bundled: {dst_path.relative_to(REPO_ROOT)}  ({dst_path.stat().st_size // 1024} KB)")


# Bundle all HTML pages
print("Bundling pages...")
PAGES = [
    "index.html",
    "veille.html",
    "methodologie.html",
    "donnees.html",
    "a-propos.html",
    "contact.html",
    "briefings.html",
    "observatoires/suisse.html",
    "observatoires/france.html",
    "observatoires/comparer.html",
    "briefings/01-banque-suisse.html",
    "briefings/02-cadres-france.html",
]
for page in PAGES:
    bundle(SITE_SRC / page, SITE_OUT / page)

# Sync data assets to root assets/ (so they are publicly fetchable)
ASSETS_OUT = SITE_OUT / "assets"
if (SITE_SRC / "assets" / "data").exists():
    if (ASSETS_OUT / "data").exists():
        shutil.rmtree(ASSETS_OUT / "data")
    shutil.copytree(SITE_SRC / "assets" / "data", ASSETS_OUT / "data")
    print(f"  synced: assets/data/")

# Copy components.js and style.css too (for dev access via raw GitHub URL)
if not (ASSETS_OUT).exists():
    ASSETS_OUT.mkdir(parents=True)
shutil.copy(SITE_SRC / "assets" / "components.js", ASSETS_OUT / "components.js")
shutil.copy(SITE_SRC / "assets" / "style.css", ASSETS_OUT / "style.css")

# Generate sitemap.xml and robots.txt
print("\nGenerating sitemap.xml and robots.txt...")
today = datetime.date.today().isoformat()
sitemap_pages = [""] + [p for p in PAGES if p != "index.html"]
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in sitemap_pages:
    url = SITE_URL + "/" + p
    priority = "1.0" if p == "" else ("0.9" if "observatoires" in p or "briefings" in p else "0.7")
    lines.append("  <url>")
    lines.append(f"    <loc>{url}</loc>")
    lines.append(f"    <lastmod>{today}</lastmod>")
    lines.append(f"    <priority>{priority}</priority>")
    lines.append("  </url>")
lines.append("</urlset>")
(SITE_OUT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")

(SITE_OUT / "robots.txt").write_text(
    f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n",
    encoding="utf-8"
)

print(f"  sitemap.xml")
print(f"  robots.txt")
print("\nDone.")
