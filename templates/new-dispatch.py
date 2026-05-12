#!/usr/bin/env python3
"""
new-dispatch.py · Helper pour créer un nouveau Dispatch à partir du template.

Usage:
    python3 templates/new-dispatch.py 4 mon-secteur
    python3 templates/new-dispatch.py 5 banque-france-q3

Ce script :
1. Copie templates/TEMPLATE-dispatch.html vers briefings/0X-mon-secteur.html
2. Remplace tous les "bX." par "bN." (où N est le numéro fourni)
3. Remplace "briefingX" par "briefingN" dans initSite()
4. Conserve les [PLACEHOLDER ...] pour que tu les remplisses ensuite

Le script ne touche pas aux pages existantes (index.html, briefings.html).
Il faudra mettre à jour ces pages manuellement après publication.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Crée un nouveau Dispatch à partir du template.")
    parser.add_argument("number", type=int, help="Numéro du Dispatch (ex: 4)")
    parser.add_argument("slug", type=str, help="Slug court du fichier (ex: mon-secteur)")
    parser.add_argument(
        "--site-root",
        type=str,
        default=".",
        help="Racine du site (défaut: dossier courant)",
    )
    args = parser.parse_args()

    if args.number < 1 or args.number > 99:
        print(f"❌ Numéro de Dispatch invalide : {args.number} · doit être 1-99")
        sys.exit(1)

    site_root = Path(args.site_root).resolve()
    template_path = site_root / "templates" / "TEMPLATE-dispatch.html"
    target_filename = f"{args.number:02d}-{args.slug}.html"
    target_path = site_root / "briefings" / target_filename

    if not template_path.exists():
        print(f"❌ Template introuvable : {template_path}")
        sys.exit(1)

    if target_path.exists():
        print(f"❌ Le fichier existe déjà : {target_path}")
        print("   Supprime-le d'abord ou choisis un autre slug.")
        sys.exit(1)

    # Read template
    with open(template_path, encoding="utf-8") as f:
        content = f.read()

    # Replace bX. → bN.
    content = re.sub(r"\bbX\.", f"b{args.number}.", content)

    # Replace initSite("briefingX") → initSite("briefingN")
    content = content.replace('initSite("briefingX")', f'initSite("briefing{args.number}")')

    # Write target
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ Dispatch créé : {target_path}")
    print()
    print("Prochaines étapes :")
    print(f"  1. Ouvrir {target_path}")
    print(f"  2. Remplacer #XXX par #{args.number:03d} dans <title> et meta.num")
    print(f"  3. Remplir tous les [PLACEHOLDER ...] (rechercher dans le fichier)")
    print(f"  4. Vérifier FR + EN renseignés dans window.PAGE_I18N")
    print(f"  5. Lancer python3 build.py et vérifier la validation")
    print(f"  6. Ajouter une carte vers ce Dispatch dans briefings.html")


if __name__ == "__main__":
    main()
