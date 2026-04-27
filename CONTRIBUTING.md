# Contribuer à observatoire[s]·ia

Merci de votre intérêt pour ce projet. Quatre voies de contribution sont
documentées en [page À propos](https://observatoire.naullynicolas.ch/a-propos.html).
Ce document détaille la mécanique technique.

## Mise en place

```bash
git clone https://github.com/otakuch/observatoires-ia.git
cd observatoires-ia
python3 scripts/build.py
python3 -m http.server 8000
# Ouvrir http://localhost:8000
```

## Architecture éditoriale

Le projet suit trois principes non négociables :

1. **Sources primaires uniquement.** Chaque chiffre cité renvoie à sa
   publication d'origine. Pas d'aggrégateur intermédiaire.
2. **Bilingue dès le premier jour.** FR et EN sont citoyens de première classe.
3. **Données ouvertes.** L'agrégation est publiée en JSON sous CC BY 4.0.

## Règles éditoriales (style)

- **Pas de tirets cadratins** (`—`). Utiliser `·`, `:` ou `(...)`.
- **Pas d'emojis** dans le contenu textuel (sauf drapeaux 🇨🇭 🇫🇷 🌍 dans la veille).
- **Vouvoiement** systématique en français pour les CTAs et la communication.
- **Pas de marketing-speak.** « Délivre une valeur unique » → « explique
  comment X fonctionne ».
- **Pas d'AI-generated copy verbatim.** Si vous utilisez Claude/GPT pour
  drafter, relisez et reformulez.

## Workflow de contribution

### 1. Signaler un observatoire manquant

Le plus simple. Ouvrez une [issue avec le template Observatory](https://github.com/otakuch/observatoires-ia/issues/new?template=observatory.md).
Vérification + intégration en moins d'une semaine généralement.

### 2. Corriger une donnée

```bash
# Branch
git checkout -b fix/correct-cge-rate

# Modifier le JSON concerné
vim src/assets/data/observatoires.json

# Rebundle
python3 scripts/build.py

# Validate
python3 -c "import json; json.load(open('assets/data/observatoires.json'))"

# Commit + push
git add .
git commit -m "fix: correction taux insertion CGE 2024 (47% → 53%)"
git push origin fix/correct-cge-rate
```

Ouvrir une PR avec le template, citer la source primaire qui justifie la
correction, et attendre review.

### 3. Documenter un biais méthodologique

Particulièrement bienvenu. Deux options :

- **Issue avec template Bias** si vous voulez signaler sans drafter.
- **PR directe** sur `src/methodologie.html` si vous proposez du contenu prêt.

La méthodologie a une structure stable (sections numérotées 01 à 08), un
biais ajouté devient une nouvelle entrée dans la section 06 · Biais reconnus.
Toute contribution est créditée nommément dans `CHANGELOG.md`.

### 4. Ajouter une dépêche Le Dispatch·iA

Plus engageant. Suivre la structure des deux exemples existants
(`src/briefings/01-banque-suisse.html`, `02-cadres-france.html`). Composantes :

1. Hero avec meta (numéro, secteur, pays, date, édition)
2. **Le paysage** (2 paragraphes + 2-column install/ralenti)
3. **Par les chiffres** (3 stats avec source primaire)
4. **Verdict expert** (pull quote)
5. **Décision : 4 questions** (numbered checklist)
6. **L'IA comme levier** (6-tool grid)
7. **Sources & traçabilité** (3 sources avec lien primaire + lien observatoire)
8. **Paywall CTA** (édition exécutive)
9. **Back link** vers le hub

Naully gère personnellement la décision d'édition pour chaque dépêche.
Avant de drafter, ouvrir une issue de discussion pour caler le sujet et
le découpage. Voir le format détaillé dans
`.github/ISSUE_TEMPLATE/dispatch.md` (à venir).

## Validation pré-PR

Checklist minimale :

```bash
# 1. JS valide
node --check src/assets/components.js

# 2. HTML rebundlé
python3 scripts/build.py

# 3. Pas de tiret cadratin
! grep -rn "—" src/*.html src/*/*.html src/assets/*.css

# 4. Tous les JSON valides
for f in assets/data/*.json; do
  python3 -c "import json; json.load(open('$f'))" || echo "INVALID: $f"
done

# 5. Rapide test visuel
python3 -m http.server 8000
```

## Code de conduite

Engagement basique : respect mutuel, désaccords constructifs, débats
techniques sans attaques personnelles. Les contributeurs qui ne respectent
pas cette base se voient refuser leurs PRs sans appel.

Posture politique du projet : neutre sur les questions politiques,
explicitement critique sur les questions méthodologiques. Pas de signal
politique gratuit dans les contributions.

## Questions

Avant d'ouvrir une issue de support, vérifier :

- Le [README](README.md)
- La page [méthodologie](https://observatoire.naullynicolas.ch/methodologie.html)
- La page [À propos](https://observatoire.naullynicolas.ch/a-propos.html)
- Le [CHANGELOG](CHANGELOG.md)

Pour toute question hors scope, écrire à [sayhi@naullynicolas.ch](mailto:sayhi@naullynicolas.ch).
