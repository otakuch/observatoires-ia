# Architecture technique

## Vue d'ensemble

```
┌─────────────────────────────────────────────────────────────┐
│  src/  ← Code source édité par les contributeurs            │
│  ├── *.html (avec <link href="assets/style.css">            │
│  │           et <script src="assets/components.js">)        │
│  └── assets/ (CSS, JS, JSON séparés)                        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼  python3 scripts/build.py
┌─────────────────────────────────────────────────────────────┐
│  / (root)  ← HTML autonomes servis par GitHub Pages         │
│  ├── *.html (CSS+JS inlinés, GA + canonical injectés)       │
│  ├── assets/data/*.json (copiés tels quels)                 │
│  ├── assets/components.js + style.css (pour raw URLs)       │
│  ├── sitemap.xml + robots.txt (auto-générés)                │
│  └── CNAME (custom domain)                                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼  git push origin main
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions (.github/workflows/deploy.yml)              │
│  → rebuild + validate JSON + upload artifact                │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  GitHub Pages → observatoire.naullynicolas.ch (HTTPS)       │
└─────────────────────────────────────────────────────────────┘
```

## Pourquoi vanilla / pas de framework

Décision prise consciemment au démarrage du projet. Justifications :

1. **Pérennité 5-10 ans.** Le HTML écrit aujourd'hui sera toujours lisible
   en 2035. React 18 → 19 → 20 → 21 nécessitera des migrations.
2. **Pas de dette npm.** Aucun `package.json`, aucun `node_modules`, aucune
   vulnérabilité dans une dépendance transitive à patcher en urgence.
3. **Performances natives.** Le HTML servi est le HTML rendu, pas de
   hydration, pas de waterfall JS, pas de CLS post-load.
4. **Lisibilité.** Un contributeur peut éditer un fichier `.html` à la main
   sans connaître le projet, sans setup local, juste avec un éditeur de texte.
5. **Pas de SSR/SSG complexity.** Le bundling se fait en `python3
   scripts/build.py`, étape unique et déterministe.

Coût : pas de composants réutilisables au sens React. Géré via :

- Templates JS dans `src/assets/components.js` (nav, footer, mobile menu
  injectés au runtime via `innerHTML`)
- Inline data dans `window.OBSERVATOIRES_DATA` et `window.VEILLE_DATA`
  pour éviter les CORS issues en `file://`
- Système i18n maison : `data-i18n="key"` + `applyI18n()` qui parcourt le
  DOM et remplace, avec fallback sur clé brute si manquant

## Système d'internationalisation

```
┌───────────────────────────────────────────────────────────┐
│  components.js                                            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ const I18N = {                                      │  │
│  │   fr: {                                             │  │
│  │     "nav.suisse": "Suisse",                         │  │
│  │     "nav.france": "France",                         │  │
│  │     "nav.contact": "Contact",                       │  │
│  │     ...                                             │  │
│  │   },                                                │  │
│  │   en: { ... }                                       │  │
│  │ }                                                   │  │
│  └─────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
                            │
                            ▼  merge avec
┌───────────────────────────────────────────────────────────┐
│  page.html (script local)                                 │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ window.PAGE_I18N = {                                │  │
│  │   fr: {                                             │  │
│  │     "ct.title": "Écrivez-moi directement",          │  │
│  │     ...                                             │  │
│  │   }                                                 │  │
│  │ }                                                   │  │
│  └─────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
                            │
                            ▼  consommé par
┌───────────────────────────────────────────────────────────┐
│  HTML : <span data-i18n="ct.title"></span>                │
│         <h2 data-i18n="ct.body" data-i18n-html></h2>      │
└───────────────────────────────────────────────────────────┘
```

`t(key)` (dans components.js) merge les deux dictionnaires (page-specific
écrase global), `applyI18n()` parcourt tous les `[data-i18n]` et remplace.

**Important** : les pages ne doivent **pas** redéfinir `function t()` localement
(bug v0.1 corrigé en v0.2 sur contact.html). Toujours utiliser `window.t()`.

## Système d'analytics

GA4 tag `G-Q52TZ7QT84` injecté automatiquement par `scripts/build.py` via
`HEAD_INJECT` snippet. Aucune config par page nécessaire. Pour changer le tag :

1. Modifier `scripts/build.py` ligne `gtag('config', 'G-Q52TZ7QT84')`
2. Rebundler : `python3 scripts/build.py`

## Gestion des assets

Les fichiers JSON dans `assets/data/` sont copiés tels quels au root par
`scripts/build.py` (ne sont pas inlinés dans le HTML). Cela permet :

1. **Téléchargement direct** depuis `/assets/data/*.json` pour les utilisateurs
2. **Citation académique** avec URL stable
3. **Re-utilisation** par des tiers qui forkent le repo

## Bundling : pourquoi inliner CSS et JS dans le HTML ?

Choix éditorial : chaque page bundlée est un **document autonome** qui peut
être :

- Sauvegardé en local (Ctrl+S) et continuer de fonctionner
- Servi en `file://` pour démo sans serveur
- Envoyé par email comme pièce jointe vivante
- Archivé sur Wayback Machine en single shot

Trade-off : taille des HTML (80-130 KB chacun, vs 10 KB si externalisé +
50 KB une fois pour CSS/JS partagés). Acceptable pour un site éditorial
de 12 pages, où le facteur limitant est l'attention humaine pas le débit
réseau.

## Workflow Git suggéré

```
main ────────────────────┬────●──── (production, deploy auto)
                          │
feat/x ──●──●──●──────────┘ (PR mergée)

fix/y ──●──●──●─────────────●───── (hotfix branch)
```

Pas de branche `develop`, pas de Gitflow complexe. Branches feature
courtes, merge sur main via PR avec review (auto-merge possible pour
les corrections de typos).

## Dépendances externes (CDN)

- **Google Fonts** : Fraunces, Instrument Sans, JetBrains Mono
  (avec preconnect dans le `<head>`)
- **Google Analytics** : `googletagmanager.com/gtag/js?id=G-Q52TZ7QT84`

Aucun autre CDN. Pas de jQuery, pas de Tailwind, pas de Bootstrap, pas
de Google Maps, pas de Stripe.js (les paiements Le Dispatch·iA passent
par mailto et facturation manuelle).

## Scaling considerations

Le site est dimensionné pour ~10K visites/mois. Pour passer à 100K+ :

1. CDN devant GitHub Pages (Cloudflare gratuit suffit)
2. Image optimization si on ajoute des illustrations
3. Pour les datasets : déléguer le téléchargement à un mirror si > 50 MB

À 1M+ visites/mois, repenser : passer à un VPS Infomaniak avec nginx,
ou Netlify Pro. Pas avant.
