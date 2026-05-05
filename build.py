#!/usr/bin/env python3
"""Build self-contained HTML files by inlining CSS and components.js."""
import os
import re
import shutil

SITE_SRC = "/home/claude/site"
SITE_OUT = "/home/claude/site_bundled"
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
with open(f"{SITE_SRC}/assets/style.css", "r", encoding="utf-8") as f:
    CSS = f.read()

with open(f"{SITE_SRC}/assets/components.js", "r", encoding="utf-8") as f:
    JS = f.read()

# Clean output dir
if os.path.exists(SITE_OUT):
    shutil.rmtree(SITE_OUT)
os.makedirs(SITE_OUT)
os.makedirs(f"{SITE_OUT}/observatoires")

def bundle(src_path, dst_path):
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace stylesheet link with inline <style>
    # Patterns: <link rel="stylesheet" href="assets/style.css"> OR href="../assets/style.css"
    html = re.sub(
        r'<link\s+rel="stylesheet"\s+href="(?:\.\./)?assets/style\.css">',
        lambda _: f"<style>\n{CSS}\n</style>",
        html,
    )

    # Replace component script with inline <script>
    # Use lambda to avoid backslash interpretation in JS content (e.g. \n in strings)
    html = re.sub(
        r'<script\s+src="(?:\.\./)?assets/components\.js"></script>',
        lambda _: f"<script>\n{JS}\n</script>",
        html,
    )

    # Compute canonical URL based on dst_path
    rel = os.path.relpath(dst_path, SITE_OUT)
    if rel == "index.html":
        canonical = SITE_URL + "/"
    else:
        canonical = SITE_URL + "/" + rel.replace(os.sep, "/")

    # Inject GA + canonical + OG before </head>
    head_block = HEAD_INJECT.format(canonical=canonical)
    html = html.replace("</head>", head_block + "</head>", 1)

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  bundled: {dst_path}  ({os.path.getsize(dst_path) // 1024} KB)")

# Bundle all HTML pages
print("Bundling pages...")
bundle(f"{SITE_SRC}/index.html", f"{SITE_OUT}/index.html")
bundle(f"{SITE_SRC}/veille.html", f"{SITE_OUT}/veille.html")
bundle(f"{SITE_SRC}/methodologie.html", f"{SITE_OUT}/methodologie.html")
bundle(f"{SITE_SRC}/donnees.html", f"{SITE_OUT}/donnees.html")
bundle(f"{SITE_SRC}/a-propos.html", f"{SITE_OUT}/a-propos.html")
bundle(f"{SITE_SRC}/partenariats.html", f"{SITE_OUT}/partenariats.html")
bundle(f"{SITE_SRC}/contact.html", f"{SITE_OUT}/contact.html")
bundle(f"{SITE_SRC}/briefings.html", f"{SITE_OUT}/briefings.html")
bundle(f"{SITE_SRC}/observatoires/suisse.html", f"{SITE_OUT}/observatoires/suisse.html")
bundle(f"{SITE_SRC}/observatoires/france.html", f"{SITE_OUT}/observatoires/france.html")
bundle(f"{SITE_SRC}/observatoires/comparer.html", f"{SITE_OUT}/observatoires/comparer.html")

# Briefings subfolder
os.makedirs(f"{SITE_OUT}/briefings", exist_ok=True)
bundle(f"{SITE_SRC}/briefings/01-banque-suisse.html", f"{SITE_OUT}/briefings/01-banque-suisse.html")
bundle(f"{SITE_SRC}/briefings/02-cadres-france.html", f"{SITE_OUT}/briefings/02-cadres-france.html")
bundle(f"{SITE_SRC}/briefings/03-luxe-horlogerie.html", f"{SITE_OUT}/briefings/03-luxe-horlogerie.html")

# Copy README and original assets folder for reference
shutil.copy(f"{SITE_SRC}/README.md", f"{SITE_OUT}/README.md")
shutil.copytree(f"{SITE_SRC}/assets", f"{SITE_OUT}/assets")

print("\nDone. Output:")
for root, dirs, files in os.walk(SITE_OUT):
    for f in sorted(files):
        path = os.path.join(root, f)
        rel = os.path.relpath(path, SITE_OUT)
        size = os.path.getsize(path) // 1024
        print(f"  {rel}  ({size} KB)")

# === Generate sitemap.xml and robots.txt ===
print("\nGenerating sitemap.xml and robots.txt...")
PAGES = [
    "",  # index
    "briefings.html",
    "observatoires/suisse.html",
    "observatoires/france.html",
    "observatoires/comparer.html",
    "veille.html",
    "methodologie.html",
    "donnees.html",
    "a-propos.html",
    "partenariats.html",
    "contact.html",
    "briefings/01-banque-suisse.html",
    "briefings/02-cadres-france.html",
    "briefings/03-luxe-horlogerie.html",
]
import datetime
today = datetime.date.today().isoformat()
sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in PAGES:
    url = SITE_URL + "/" + p
    sitemap_lines.append("  <url>")
    sitemap_lines.append(f"    <loc>{url}</loc>")
    sitemap_lines.append(f"    <lastmod>{today}</lastmod>")
    priority = "1.0" if p == "" else ("0.9" if "observatoires" in p or "briefings" in p else "0.7")
    sitemap_lines.append(f"    <priority>{priority}</priority>")
    sitemap_lines.append("  </url>")
sitemap_lines.append("</urlset>")

with open(f"{SITE_OUT}/sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_lines))

with open(f"{SITE_OUT}/robots.txt", "w", encoding="utf-8") as f:
    f.write(f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
""")

print(f"  sitemap.xml  ({os.path.getsize(SITE_OUT + '/sitemap.xml')} B)")
print(f"  robots.txt  ({os.path.getsize(SITE_OUT + '/robots.txt')} B)")
