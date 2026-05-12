# Templates · observatoire[s]·ia

Ce dossier contient les templates HTML réutilisables pour produire de
nouveaux contenus éditoriaux sur l'observatoire en respectant la grille
visuelle et la structure analytique établies en v0.3.16.

## TEMPLATE-dispatch.html

Template HTML complet pour un nouveau Dispatch sectoriel. Reproduit la
structure canonique en 5 blocs analytiques + CTA · 3 actions adoptée
en v0.3.16 et utilisée pour les Dispatches publiés (D01 banque suisse,
D02 cadres France, D03 luxe horlogerie).

### Structure éditoriale en 5 blocs analytiques

```
HERO                          ← titre + meta + byline + actions
PDF MODAL                     ← version concise printable
─────────────────────────────────────────────────────
BLOC 1 · LECTURE CRITIQUE     ← 5 objections au récit alarmiste
BLOC 2 · CARTOGRAPHIE BCG     ← 6 segments AI Labor Disruption
BLOC 3 · EMPIRIE LOCALE       ← 5 sources sectorielles + synthèse
BLOC 4 · DÉBAT 4 POSITIONS    ← bear / empirique / macro / bull
BLOC 5 · TCO 4 CARDS          ← économie réelle de l'IA
─────────────────────────────────────────────────────
SOURCES & TRAÇABILITÉ         ← rigueur académique
DISCLOSURE ÉDITORIALE         ← transparence CC BY 4.0
CTA · 3 ACTIONS               ← horizon 90 jours, sectoriel
BACK navigation
```

### Procédure pour produire un nouveau Dispatch

#### 1. Dupliquer le template

```bash
cp templates/TEMPLATE-dispatch.html briefings/04-mon-secteur.html
```

#### 2. Remplacer le préfixe i18n bX

Remplacer toutes les occurrences de `bX.` par le numéro du Dispatch
(ex: `b4.` pour le quatrième Dispatch). Sur Linux/macOS :

```bash
sed -i 's/bX\./b4./g' briefings/04-mon-secteur.html
```

Sur Windows VSCode : Recherche Ctrl+H sur `bX.` → `b4.` (avec match case).

#### 3. Mettre à jour l'identifiant initSite

Dans le bloc script en bas du fichier, remplacer :

```js
initSite("briefingX");
```

par l'identifiant correct, par exemple `briefing4`.

#### 4. Mettre à jour le numéro et le titre HTML

- `<title>Le Dispatch·iA #XXX · ...</title>` → `#004` ou autre
- Meta description
- Tous les `[PLACEHOLDER : ...]` partout

#### 5. Remplir les 5 blocs analytiques

##### Bloc 1 · LECTURE CRITIQUE

Les 5 objections suivent une grille intellectuelle stable :

| Objection | Dimension | Source canonique |
|---|---|---|
| 01 | Empirique macro | NYT, WaPo, données BLS · effectifs Big Tech 2026 ≈ 2022 |
| 02 | Conceptuel · bundle | Garicano · Silicon Continent avril 2026 |
| 03 | Théorique · human-intrinsic | Trammell · Stanford mars 2026 |
| 04 | Méta-épistémologique | Davenport & Paredes · HDSR automne 2025 |
| 05 | Psychologique-comportemental | Champniss HBR + Wu et al. Scientific Reports |

Chaque objection : title + body (~750-900 chars) + source line.
Le body se termine par : `<br><br><strong>Conséquence pour [audience]</strong> : ...`

##### Bloc 2 · CARTOGRAPHIE BCG

Étude BCG d'avril 2026 sur 1 500 rôles Revelio Labs / 165M emplois US.
6 segments en 3 groupes :

- Cadres remodelés en 2-3 ans : Amplified 5%, Rebalanced 14%, Divergent 12%
- Cadres éliminés en 4-5 ans : Substituted 12%
- Exposition limitée : Enabled 23%, Limited-Exposure 34%

Pour chaque segment : adapter au secteur du Dispatch avec exemples
concrets de fonctions.

##### Bloc 3 · EMPIRIE LOCALE

5 sources sectorielles locales · choisir parmi les bases existantes :

**Sources FR** :
- Coface/OEM avril 2026 (substitution macro)
- Kelio/OpinionWay 2026 (perception DRH)
- Bpifrance Le Lab (PME)
- Alegria (PME maturité)
- PwC AI Jobs Barometer (création emplois)
- France Stratégie / DARES (prospective)
- APEC (recrutement cadres)

**Sources CH** :
- KOF/ETH étude #186 (substitution effective)
- HSLU Swiss AI Jobs Report (création emplois IA)
- BNS Q1 2026 (perception entreprises)
- Colombus/Oracle/HEG (maturité organisationnelle)
- Angestellte Schweiz / DemoSCOPE (perception employés)
- Cortesi/aidentities (perception grand public)
- OFS STATEM (statistique officielle)

Pour chaque source : nom complet + body 200-300 chars.
Terminer le bloc par une **synthèse intégrant le cadre Davenport**.

##### Bloc 4 · DÉBAT · 4 POSITIONS

4 colonnes représentant la diversité analytique du débat 2026 :

| Position | Auteurs représentatifs |
|---|---|
| Bear · apocalypse | Amodei, Suleyman, Dimon |
| Empirique · bundle | Garicano, Brynjolfsson |
| Macro · théorie | Trammell, Imas, Acemoglu |
| Bull historique-allocateur | a16z, NY Fed, NYT, Pearson |

Pour chaque position : 400-600 chars + sectoral takeaway final.

##### Bloc 5 · TCO · 4 CARDS

4 cards économiques structurelles :

1. **Coût total ≠ prix par token** · Singh Tomer · Gartner 5-10× sous-estimation
2. **LLM Cost Paradox** · prix unitaire baisse mais consommation explose
3. **Taxe linguistique** · +60% tokens FR vs EN
4. **Price Reversal** · Chen et al. · 21,8% inversions, 28× max

#### 6. CTA · 3 actions sectorielles

Format stable : eyebrow + title + lede + 3 cards (tag verbe + title + desc)
+ followup. Chaque action doit être :

- **Concrète et actionnable** · à entreprendre dans les 90 prochains jours
- **Différenciée par secteur** · pas générique
- **Reliée à au moins un des 5 blocs analytiques** · explicite la connexion

Exemples de verbes d'action utilisés dans les Dispatches existants :
Cartographier · Préserver · Trianguler · Piloter · Réviser · Différencier ·
Investir · Auditer.

#### 7. Validation avant build

Checklist :

- [ ] Tous les `[PLACEHOLDER ...]` remplacés
- [ ] Préfixe `bX.` remplacé partout (`grep "bX\." briefings/04-mon-secteur.html` doit retourner 0 ligne)
- [ ] Numéro Dispatch correct dans `<title>` et `meta.num`
- [ ] FR + EN remplis dans les deux blocs i18n
- [ ] Aucun em-dash (—) · utiliser middle dot (·) à la place
- [ ] Tous les éléments avec `<em>`, `<strong>`, `<a>`, `<br>` ont
      `data-i18n-html="true"` sur leur balise HTML
- [ ] Sources URL renseignées dans la section Sources

#### 8. Build et déploiement

```bash
python3 build.py
```

Vérifier dans la sortie :
- JS valide sur la page (Node `--check`)
- Em-dashes count = 0
- Toutes les clés i18n résolvent en FR et EN

Puis ajouter le Dispatch à :
- `briefings.html` (page index des Dispatches)
- Section `dispatch-tease` de `index.html` si c'est le dernier publié
- Footer CHANGELOG si publication

## Conventions éditoriales générales

### Typographie

- **Aucun em-dash** (—) · utiliser middle dot (·) partout
- **Pas d'emojis dans le corps de texte** · seulement dans les meta (drapeaux pays)
- **Guillemets français** « ... » avec espace insécable, pas «...» ni "..."
- **Citations en italique** via `<em>...</em>` uniquement, pas `<i>`
- **Chiffres** : espace fine pour les milliers en FR (3 562, pas 3,562)

### Voix éditoriale

- Posée, factuelle, anti-emotional
- Pas de jugement absolu sur les positions
- Toute affirmation chiffrée doit être sourcée
- Pas de prédiction sans citation
- Méta-cadre Davenport en arrière-plan : les chiffres sont des
  indicateurs directionnels, pas des projections actionnables à 5 ans

### Système i18n

- Préfixe par numéro de Dispatch : `b1.`, `b2.`, `b3.`, etc.
- Strings communes partagées : `brief.act.*`, `brief.modal.*`, `brief.back`
- Tout string contenant du HTML doit avoir `data-i18n-html="true"`
- FR et EN remplis systématiquement (les deux langues sont obligatoires)

### Architecture CSS

Le template utilise les classes CSS existantes définies dans
`assets/style.css` :

- `.brief-hero`, `.brief-hero-title`, `.brief-hero-meta`
- `.brief-critical`, `.brief-critical-list`, `.brief-critical-item`
- `.brief-bcgmap`, `.brief-bcgmap-grid`, `.brief-bcgmap-seg--*`
- `.brief-chempirie`, `.brief-chempirie-stats`, `.brief-chempirie-grid`
- `.brief-debate`, `.brief-debate-grid--4col`, `.brief-debate-pos--*`
- `.brief-tco`, `.brief-tco-grid--4col`, `.brief-tco-card`
- `.brief-cta-actions`, `.brief-cta-grid--3`, `.brief-cta-card--action`
- `.brief-sources`, `.brief-disclosure`, `.brief-back`

Aucune nouvelle classe CSS n'est requise pour un Dispatch standard.
Si besoin, ajouter dans `assets/style.css` plutôt que dans le HTML.

## Maintenance du template

Si la structure éditoriale évolue (ex: ajout d'un 6e bloc, restructuration
du CTA), mettre à jour ce template **avant** de produire le Dispatch
suivant pour préserver la cohérence visuelle.

Versions précédentes du template archivées dans `templates/archive/`.

---

Dernière mise à jour : 10 mai 2026 · v0.3.19
Maintenu par : Naully Nicolas · sayhi@naullynicolas.ch
