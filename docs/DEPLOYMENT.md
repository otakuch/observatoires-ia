# Guide de déploiement

## Production : `https://observatoire.naullynicolas.ch`

Le site est servi via **GitHub Pages** avec custom domain pointant vers
le DNS Infomaniak. Le déploiement est automatique à chaque push sur la
branche `main` via GitHub Actions.

## Configuration GitHub Pages

### 1. Activation Pages

Dans le repo GitHub :
1. Settings → Pages
2. Source : **GitHub Actions** (et non « Deploy from a branch »)
3. Le workflow `.github/workflows/deploy.yml` prend le relais

### 2. Custom Domain

Le fichier `CNAME` à la racine contient `observatoire.naullynicolas.ch`.
GitHub Pages le détecte automatiquement.

### 3. DNS chez Infomaniak

Configurer un CNAME chez Infomaniak :

```
observatoire.naullynicolas.ch.   CNAME   otakuch.github.io.
```

Ou un enregistrement ALIAS / ANAME selon ce que supporte le panneau.

Pour le HTTPS, GitHub Pages provisionne automatiquement un certificat
Let's Encrypt après la propagation DNS (peut prendre jusqu'à 24h).

### 4. Vérification post-deploy

```bash
# Vérifier que la page d'accueil charge
curl -I https://observatoire.naullynicolas.ch

# Vérifier le sitemap
curl https://observatoire.naullynicolas.ch/sitemap.xml | head -20

# Vérifier robots.txt
curl https://observatoire.naullynicolas.ch/robots.txt

# Vérifier qu'un dataset est servi
curl https://observatoire.naullynicolas.ch/assets/data/metiers-ia-fr.json | head
```

## Google Analytics

Le tag GA4 `G-Q52TZ7QT84` est injecté automatiquement dans le `<head>` de
chaque page par `scripts/build.py`. Pour vérifier que le tracking fonctionne :

1. Ouvrir [analytics.google.com](https://analytics.google.com) → propriété
   correspondante
2. Reports → Realtime
3. Visiter [observatoire.naullynicolas.ch](https://observatoire.naullynicolas.ch)
   dans un navigateur (sans bloqueur de publicité)
4. La visite doit apparaître dans les 30 secondes

## Search Console

Après le premier déploiement réussi :

1. Ajouter la propriété `https://observatoire.naullynicolas.ch` dans
   [Google Search Console](https://search.google.com/search-console)
2. Vérifier la propriété (méthode : balise HTML, déjà préparée pour DNS)
3. Soumettre le sitemap : `https://observatoire.naullynicolas.ch/sitemap.xml`

## Déploiement manuel (en cas de besoin)

Si le workflow GitHub Actions échoue, déploiement manuel :

```bash
# 1. Build local
python3 scripts/build.py

# 2. Vérifier le résultat
python3 -m http.server 8000
# Naviguer dans tout le site

# 3. Push avec --force-with-lease seulement en cas d'urgence
git add .
git commit -m "deploy: hotfix"
git push origin main
```

## Rollback

Pour revenir à une version antérieure :

```bash
# Lister les tags
git tag -l

# Revenir au tag v0.1.0
git checkout v0.1.0
git checkout -b hotfix/rollback-from-v0.2
git push origin hotfix/rollback-from-v0.2

# Puis merger sur main via PR
```

GitHub Pages servira la nouvelle version après que le workflow ait tourné.

## Troubleshooting

### Le site renvoie 404

- Vérifier que `Settings → Pages → Source = GitHub Actions`
- Vérifier que la branche est bien `main`
- Vérifier le run du workflow dans `Actions` tab

### Le custom domain ne fonctionne pas

- Vérifier que `CNAME` est bien à la racine
- Vérifier le DNS : `dig observatoire.naullynicolas.ch`
- Attendre la propagation DNS (jusqu'à 48h)
- Vérifier le statut SSL dans Settings → Pages

### Une page affiche les clés i18n brutes

Bug connu antérieur à v0.2.0. Corrigé dans `scripts/build.py` et
`src/contact.html`. Si vous le voyez réapparaître :

1. Vérifier que la page concernée n'a pas une fonction `t()` locale qui
   ombrage la fonction globale de `components.js`
2. Toutes les pages doivent utiliser `window.t()` plutôt que `t()`

### GA ne tracker pas

- Vérifier que le tag est présent dans le HTML servi : `view-source:` dans Chrome
- Désactiver les bloqueurs (uBlock, Ghostery) le temps du test
- Vérifier le mode debug dans GA4 : Reports → Realtime → Debug View
