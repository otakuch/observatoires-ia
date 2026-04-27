# Checklist de mise en route GitHub

Ce document liste tout ce qu'il faut **remplir, vérifier ou ajuster**
avant de faire le premier push. Tout est pré-rempli avec les valeurs
les plus probables, mais à confirmer.

## 1. Création du repo GitHub

Sur [github.com/new](https://github.com/new) :

- **Owner :** `otakuch` (votre handle)
- **Repository name :** `observatoires-ia` ⚠️ exactement ce nom (référencé partout)
- **Description :** `Cartographie indépendante des observatoires emploi & IA en Suisse et en France`
- **Visibility :** **Public**
- **Initialize with :** ❌ rien (pas de README, .gitignore ou LICENSE — déjà fournis)

## 2. Variables à vérifier dans les fichiers

| Fichier | Ligne / champ | Valeur actuelle | À ajuster ? |
|---|---|---|---|
| `CNAME` | (tout) | `observatoire.naullynicolas.ch` | ⚠️ Confirmer le sous-domaine final |
| `scripts/build.py` | `SITE_URL` | `https://observatoire.naullynicolas.ch` | Idem |
| `scripts/build.py` | tag GA | `G-Q52TZ7QT84` | OK (votre tag confirmé) |
| `README.md` | `github.com/otakuch/observatoires-ia` | `otakuch` | ⚠️ Confirmer le owner GitHub |
| `CITATION.cff` | `email`, `website`, `affiliation` | `sayhi@naullynicolas.ch` etc. | OK |
| `.github/ISSUE_TEMPLATE/*.md` | `assignees: otakuch` | `otakuch` | ⚠️ Confirmer le owner |

Si votre handle GitHub est différent de `otakuch`, faire un find-replace
global avant le premier push :

```bash
cd observatoires-ia
grep -rln "otakuch" . | xargs sed -i 's/otakuch/VOTRE_HANDLE/g'
```

## 3. Premier push

```bash
cd observatoires-ia
git init
git add .
git commit -m "feat: initial commit · v0.2.0 ready for production"
git branch -M main
git remote add origin https://github.com/otakuch/observatoires-ia.git
git push -u origin main
```

## 4. Activer GitHub Pages

Une fois le push fait :

1. Aller dans **Settings → Pages**
2. **Source :** sélectionner `GitHub Actions` (et non « Deploy from a branch »)
3. Le workflow `.github/workflows/deploy.yml` se déclenche automatiquement
4. Suivre l'exécution dans l'onglet **Actions**

## 5. Configurer le DNS chez Infomaniak

Une fois Pages actif, configurer le DNS pour le custom domain :

```
Type    Hôte                                 Cible
CNAME   observatoire.naullynicolas.ch        otakuch.github.io
```

Ou ALIAS / ANAME selon le panneau Infomaniak.

**Délai de propagation :** 1-24h (souvent 30 min)
**Délai certificat HTTPS :** automatique après propagation (jusqu'à 24h)

Dans le panneau GitHub Pages, vous verrez :
- ⏳ « DNS check in progress »
- ✅ « DNS check successful » → site accessible
- ✅ « HTTPS enabled » → certificat Let's Encrypt provisionné

## 6. Soumettre le sitemap à Google

Une fois le site accessible en HTTPS :

1. Aller sur [Google Search Console](https://search.google.com/search-console)
2. Ajouter une propriété : `https://observatoire.naullynicolas.ch`
3. Vérifier la propriété (méthode HTML balise meta — vous pouvez ajouter
   la balise dans `scripts/build.py` HEAD_INJECT temporairement)
4. Soumettre le sitemap : `https://observatoire.naullynicolas.ch/sitemap.xml`

## 7. Vérifier que GA tracker

1. Naviguer sur [https://observatoire.naullynicolas.ch](https://observatoire.naullynicolas.ch)
   (en navigation privée pour éviter le cache et les bloqueurs)
2. Aller sur [analytics.google.com](https://analytics.google.com) →
   propriété `G-Q52TZ7QT84`
3. **Reports → Realtime** : votre visite doit apparaître dans les 30 secondes
4. Si pas de tracking, vérifier que le tag est bien dans le HTML :
   ```bash
   curl -s https://observatoire.naullynicolas.ch | grep -c "G-Q52TZ7QT84"
   # Doit retourner 1 ou plus
   ```

## 8. Tagger la première release

Une fois le site déployé et fonctionnel :

```bash
git tag -a v0.2.0 -m "v0.2.0 · Le Dispatch·iA + open data + responsive"
git push origin v0.2.0
```

Sur GitHub : **Releases → Draft new release** → choisir le tag `v0.2.0` →
copier le contenu correspondant du `CHANGELOG.md`.

## 9. (Optionnel) Submit aux directories open data

Une fois en production :

- [data.gouv.fr](https://www.data.gouv.fr) — section open data CC BY
- [opendata.swiss](https://opendata.swiss) — pour les datasets CH
- [Dataverse](https://dataverse.org) — pour citation académique long terme

## Variables qui ne sont **pas** à modifier

- Les noms de fichiers HTML (référencés dans `scripts/build.py` PAGES list)
- Les chemins relatifs `assets/style.css` et `assets/components.js`
- Les noms de champs JSON (référencés dans les schémas)
- Les routes mailto `?type=exec&dispatch=001` (utilisées par les liens)
- La structure i18n `data-i18n="key"` (utilisée par `applyI18n()`)

## Si vous voulez changer le tag GA plus tard

```bash
# Find/replace dans build.py uniquement
sed -i 's/G-Q52TZ7QT84/G-NEWTAG/g' scripts/build.py

# Rebundle
python3 scripts/build.py

# Commit
git add .
git commit -m "chore: rotate GA4 tag"
git push
```

Le workflow GitHub Actions rebundle automatiquement et déploie.

## Ce qui est **déjà fait** (pas besoin de toucher)

- ✅ Bundling automatique CSS+JS dans tous les HTML
- ✅ Injection automatique GA + canonical + Open Graph dans tous les `<head>`
- ✅ Génération automatique sitemap.xml et robots.txt
- ✅ Validation JSON automatique au moment du build (CI)
- ✅ Templates issue / PR pré-remplis
- ✅ License double (MIT pour le code, CC BY 4.0 pour les données)
- ✅ Deploy workflow GitHub Actions complet

## Aide

En cas de difficulté :

- Lire [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) section Troubleshooting
- Lire [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- Lire [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Email : [sayhi@naullynicolas.ch](mailto:sayhi@naullynicolas.ch)
