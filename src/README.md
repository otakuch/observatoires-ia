# observatoire[s]·ia

Cartographie indépendante et bilingue des observatoires emploi & IA en Suisse et en France.

**v0.2** — multi-pages · responsive · FR/EN

---

## Démarrage rapide

### Test local (sans serveur)
Décompressez l'archive et ouvrez `site/index.html` dans un navigateur. Les données sont embarquées dans `assets/components.js` — tout fonctionne via `file://`.

### Avec un serveur local (recommandé pour développement)
```bash
cd site
python3 -m http.server 8000
# puis ouvrez http://localhost:8000
```
Avec un serveur, vous pouvez basculer sur `fetch()` vers `assets/data/*.json` (les fichiers sont déjà là).

### Déploiement GitHub Pages
1. Créez un repo `otakuch/observatoires-ia`
2. Pushez le contenu du dossier `site/` à la racine
3. Settings → Pages → Source: `main` branch, root
4. Le site sera disponible à `https://otakuch.github.io/observatoires-ia/`

---

## Structure

```
site/
├── index.html              Accueil — manifeste + teasers CH/FR + dernière veille
├── observatoires/
│   ├── suisse.html         Dashboard Suisse (6 sources, KPIs, chart adoption sectorielle)
│   ├── france.html         Dashboard France (8 sources, KPIs, tensions ROME)
│   └── comparer.html       Tableau comparatif CH×FR + 3 angles morts
├── veille.html             Tous les rapports, filtre par pays
├── methodologie.html       Critères, taxonomies, biais reconnus
├── donnees.html            Téléchargements JSON/CSV + schéma + licence
├── a-propos.html           Naully Nicolas + Guerill-iA + 3 principes
└── assets/
    ├── style.css           CSS partagé (Fraunces + Instrument Sans + JetBrains Mono)
    ├── components.js       Nav, footer, i18n, lang toggle, données embarquées
    └── data/
        ├── observatoires.json   14 entrées CH+FR
        └── veille.json          6 rapports avril 2026
```

## Architecture i18n

- Toggle FR/EN dans la nav (persistant via `localStorage`)
- Traductions globales dans `components.js` (`I18N`)
- Traductions par page dans chaque HTML (`window.PAGE_I18N`)
- Hook `window.onLangChange` pour re-render des sections dynamiques

## Ajouter un observatoire

Éditez `assets/data/observatoires.json` ET la copie embarquée dans `assets/components.js` (`window.OBSERVATOIRES_DATA`).

Schéma : voir page `donnees.html`.

## Licence

- **Agrégation et code** : CC BY 4.0 — © 2026 Naully Nicolas
- **Sources sous-jacentes** : conservent leurs licences propres (OFS, DARES, etc.)

## Contact

- sayhi@naullynicolas.ch
- transitions-ia.ch
- naullynicolas.ch
