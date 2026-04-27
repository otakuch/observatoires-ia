# observatoire[s]·ia

> Cartographie indépendante et bilingue des observatoires de l'emploi face à l'IA en Suisse et en France.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-D03C2F.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status](https://img.shields.io/badge/status-v0.2-1F3A3D.svg)](https://observatoire.naullynicolas.ch)
[![Site](https://img.shields.io/badge/site-observatoire.naullynicolas.ch-D03C2F.svg)](https://observatoire.naullynicolas.ch)

**Site en production** : [observatoire.naullynicolas.ch](https://observatoire.naullynicolas.ch)

---

## Le projet

Cette cartographie répond à un constat simple, formulé sur la page « À propos » : aucune source francophone ne rassemblait jusqu'ici les observatoires français et suisses de l'emploi face à l'IA, dans les deux langues, avec une explicitation des biais méthodologiques. Le site agrège, traduit, compare et critique ces données. Il ne produit aucun chiffre nouveau.

Le projet est porté par [Naully Nicolas](https://naullynicolas.ch), consultant en IA, gouvernance et cybersécurité, basé entre Genève et la Vendée. Il est gratuit, sans publicité, sans tracker autre que Google Analytics, sous licence ouverte. C'est un bien commun, modestement contribué.

---

## Structure du repo

```
.
├── index.html                    # Page d'accueil (production)
├── briefings.html                # Hub Le Dispatch·iA
├── observatoires/
│   ├── suisse.html               # Dashboard CH
│   ├── france.html               # Dashboard FR
│   └── comparer.html             # Comparaison CH ↔ FR
├── briefings/
│   ├── 01-banque-suisse.html     # Dispatch #001 (exemple)
│   └── 02-cadres-france.html     # Dispatch #002 (exemple)
├── veille.html                   # Field Report (rapports du mois)
├── methodologie.html             # Méthodologie + types d'IA
├── donnees.html                  # Open data
├── a-propos.html                 # À propos
├── contact.html                  # Formulaire contact
│
├── assets/
│   ├── components.js             # Nav + footer + i18n + helpers
│   ├── style.css                 # Design system (~50 KB)
│   └── data/                     # 11 jeux de données JSON publics
│       ├── metiers-ia-fr.json    # 200 métiers ROME (FR)
│       ├── metiers-ia-ch.json    # 324 métiers NP 2010 (CH)
│       ├── indicateurs-ia-fr.json
│       ├── indicateurs-ia-ch.json
│       ├── scenarios-ia-fr.json
│       ├── scenarios-ia-ch.json
│       ├── economistes-ia.json
│       ├── economistes-ia-ch.json
│       ├── timeline-ia-emploi.json
│       ├── observatoires.json    # 14 observatoires CH+FR
│       └── veille.json           # 8 rapports récents
│
├── schemas/                      # JSON Schemas pour réutilisation
├── src/                          # Code source non-bundlé (édition)
│   ├── *.html                    # HTML avec <link> et <script src>
│   └── assets/                   # CSS + JS non-inlinés
│
├── scripts/
│   ├── build.py                  # Bundle src/ → root (auto GA + canonical)
│   ├── compile_data_fr.py        # ROME → metiers-ia-fr.json
│   └── compile_data_ch.py        # NP 2010 → metiers-ia-ch.json
│
├── .github/workflows/deploy.yml  # Auto-deploy GitHub Pages
├── CNAME                         # observatoire.naullynicolas.ch
├── sitemap.xml                   # Auto-généré par build.py
├── robots.txt
├── LICENSE
├── CHANGELOG.md
└── README.md                     # Ce fichier
```

---

## Installation locale

### Prérequis
- Python 3.10+ pour le build
- Node.js 18+ (optionnel, pour validation JS)
- Un serveur HTTP statique (le navigateur bloque `fetch()` en `file://`)

### Étapes

```bash
git clone https://github.com/otakuch/observatoires-ia.git
cd observatoires-ia

# Bundler les fichiers src/ en HTML autonomes (à la racine du repo)
python3 scripts/build.py

# Servir localement
python3 -m http.server 8000
# Ouvrir http://localhost:8000
```

### Workflow d'édition

Vous éditez les fichiers dans `src/`, vous lancez `python3 scripts/build.py`, le bundling met à jour les HTML autonomes à la racine. Les HTML racine intègrent CSS et JS inlinés, prêts pour GitHub Pages.

```bash
# Édition typique
vim src/briefings.html         # modifier le contenu
python3 scripts/build.py        # rebundle
git add . && git commit -m "fix: tarif Dispatch annuel"
git push                        # déploiement automatique
```

---

## Données ouvertes (Open Data)

Toutes les données sont publiées sous **licence CC BY 4.0** dans `assets/data/`. Citez-les comme :

> Naully Nicolas, *observatoire[s]·ia v0.2*, 2026, https://observatoire.naullynicolas.ch

### Schéma d'un métier (`metiers-ia-fr.json` ou `metiers-ia-ch.json`)

```json
{
  "label": "Conseiller bancaire",
  "rome_domain": "C",
  "rome_domain_label": "Banque, Assurance, Immobilier",
  "fap_code": "C2Z10",
  "median_salary_eur_month": 2680,
  "headcount_fr_2024": 158000,
  "exposure_score_primary": 25.4,
  "exposure_score_avg": 7.2,
  "exposure_scale": "0-100 (Coface) ou 0-10 (académiques). Voir methodologie.",
  "rationale_fr": "...",
  "reconversion_paths": [
    { "role": "Gestionnaire patrimoine premium", "explanation_fr": "..." }
  ],
  "sources": [
    {
      "tier": 1,
      "exposure_score": 7.0,
      "year": 2026,
      "citation": "Eloundou et al. (OpenAI 2023)",
      "ai_type": "generative"
    }
  ]
}
```

### Champ `ai_type` (important)

Chaque source est annotée avec la famille d'IA dont elle parle (voir [méthodologie · section 03](https://observatoire.naullynicolas.ch/methodologie.html#types-ia)) :

- `generative` : LLM, Stanford HAI 2026, Eloundou OpenAI, Anthropic, Brynjolfsson, etc.
- `agentic` : OpenAI Richmond, IA agentique, Coface phase Special Agent
- `automation_broad` : Frey & Osborne, McKinsey, OCDE, Coface phase Copilot
- `unspecified` : sources qui ne précisent pas

Cette annotation permet de filtrer une analyse par type d'IA, et de ne pas mélanger des estimations qui mesurent des phénomènes radicalement différents.

### Tiers de fiabilité

- **T1** : recherche académique avec peer review (Eloundou, Brynjolfsson, Acemoglu, Felten…)
- **T2** : institutionnel (DARES, OFS, Stanford HAI, Coface, BCG, McKinsey)
- **T3** : presse spécialisée vérifiable
- **T4** : expert nommé, déclaration publique

---

## Contribuer

Quatre voies, par ordre croissant d'engagement :

1. **Signaler** un observatoire CH/FR manquant via [issue GitHub](https://github.com/otakuch/observatoires-ia/issues) ou email
2. **Corriger** une donnée ou un libellé via Pull Request sur le JSON concerné
3. **Documenter un biais** méthodologique (particulièrement bienvenu)
4. **Traduire** ou améliorer la version EN, en particulier sur les terminologies CH/FR (ROME, PCS-ESE, NSP, SEFRI)

### Critères d'inclusion d'un observatoire

Un observatoire est inclus s'il satisfait simultanément :

- Produit des données ou analyses régulières (au moins 1 publication / an) sur emploi, formation, gouvernance ou statistiques liées à l'IA
- Émet depuis ou couvre principalement la Suisse ou la France
- Publie ses sources et sa méthodologie de manière vérifiable
- Reste accessible publiquement, sans paywall systématique

Voir [`methodologie.html`](https://observatoire.naullynicolas.ch/methodologie.html) section 01 pour la liste complète.

### Pull Request workflow

```bash
git checkout -b feat/add-bak-economics
# Éditer src/assets/data/observatoires.json
python3 scripts/build.py
git add .
git commit -m "feat: add BAK Economics (CH alémanique)"
git push origin feat/add-bak-economics
# Ouvrir une PR sur GitHub
```

Toute contribution acceptée est créditée dans le `CHANGELOG.md` et dans la prochaine version du site.

---

## Stack technique

- **HTML statique vanilla** (pas de framework, pas de build complexe)
- **CSS pur** avec variables custom (`--paper`, `--ink`, `--signal`, `--rule`)
- **JavaScript vanilla ES6** (pas de jQuery, pas de bundler)
- **Typographie** : Fraunces (variable serif) + Instrument Sans + JetBrains Mono, via Google Fonts
- **Responsive** : mobile-first, breakpoints à 480 / 720 / 960 px
- **i18n** : système maison avec `data-i18n` + `localStorage` (FR / EN)
- **Analytics** : Google Analytics 4 (`G-Q52TZ7QT84`)
- **Hosting** : GitHub Pages (statique) avec custom domain Infomaniak/Cloudflare
- **CDN polices** : Google Fonts (preconnect)

Aucun cookie de tracking en dehors de GA. Aucun service tiers pour le formulaire de contact (mailto direct).

### Pourquoi vanilla ?

Le site est conçu pour durer 5 à 10 ans sans dette technique. Pas de migration React 18 → 19 → 20 à venir. Pas de breakage npm. Le HTML d'aujourd'hui sera toujours lisible en 2035.

---

## Roadmap

### v0.3 (T2 2026)
- Sources alémaniques (KOF ETH, BAK Economics, BFH)
- Dispatch #003 sur secteur public CH/FR
- Schémas JSON formels publiés dans `schemas/`
- Comparaison automatique des indicateurs FR ↔ CH dans `comparer.html`

### v0.4 (T3 2026)
- API JSON publique stable avec versioning
- Embed widgets pour chercheurs et journalistes
- Dispatch #004-005-006 (RH, industrie, santé)
- Intégration des prochaines vagues OFS et DARES

### v1.0 (T4 2026)
- Couverture complète des 19 domaines NP 2010 et 14 domaines ROME
- Dispatches mensuelles établies en cadence
- Edition exécutive PDF templatée et industrialisable
- Section archives consultables

---

## Crédits & Licence

### Données
Les jeux de données dans `assets/data/` sont publiés sous **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. Réutilisation libre avec citation.

### Code
Le code source du site est sous **MIT License** (voir [LICENSE](LICENSE)).

### Polices
Fraunces, Instrument Sans, JetBrains Mono — toutes sous SIL Open Font License.

### Inspirations éditoriales
- *Renaissance Diplomacy* (Garrett Mattingly, 1955) — métaphore Le Dispatch·iA
- [dearcc.org](https://dearcc.org) — format magazine pour les éditions exécutives
- *Presidential Daily Brief* — structure de la version exécutive PDF

### Sources principales référencées
DARES · INSEE · France Stratégie · APEC · CGE · CNIL · Inria · LaborIA · OFS · ESPA · NP 2010 · SEFRI · EPFL AI Center · Swiss AI Center HES-SO · Stanford HAI · OCDE · OIT · Coface · OEM · BCG · PwC · McKinsey · Eloundou · Brynjolfsson · Acemoglu · Felten · Aghion · Cette · Massenkoff · McCrory.

---

## Contact

Pour toute question, contribution ou critique :

- **Email** : [sayhi@naullynicolas.ch](mailto:sayhi@naullynicolas.ch)
- **Site** : [naullynicolas.ch](https://naullynicolas.ch)
- **LinkedIn** : [naullynicolas](https://www.linkedin.com/in/naullynicolas)
- **X** : [@naullyn](https://x.com/naullyn)
- **Issues GitHub** : [github.com/otakuch/observatoires-ia/issues](https://github.com/otakuch/observatoires-ia/issues)

---

*Dernière mise à jour de ce README : avril 2026 · v0.2*
