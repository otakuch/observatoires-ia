# JSON Schemas

Schémas formels JSON Schema Draft 07 pour valider les datasets de
`assets/data/`. Référencés via le champ `$schema` dans chaque dataset.

## Schémas disponibles

| Schéma | Datasets validés |
|---|---|
| `metiers-ia.schema.json` | `metiers-ia-fr.json`, `metiers-ia-ch.json` |
| `indicateurs-ia.schema.json` | `indicateurs-ia-fr.json`, `indicateurs-ia-ch.json` |
| `scenarios-ia.schema.json` | `scenarios-ia-fr.json`, `scenarios-ia-ch.json` |

## Validation locale

```bash
pip install jsonschema
python3 -c "
import json
import jsonschema
schema = json.load(open('schemas/metiers-ia.schema.json'))
data = json.load(open('assets/data/metiers-ia-fr.json'))
jsonschema.validate(data, schema)
print('✓ valid')
"
```

## Validation CI

Le workflow `.github/workflows/deploy.yml` valide automatiquement chaque JSON
à chaque push sur `main`.

## Évolution des schémas

Les schémas suivent SemVer comme les datasets. Une rupture de compatibilité
incrémente le major. Les schémas sont versionnés via le tag du repo.

Les datasets indiquent leur version dans le champ `version` (ex. `"0.3.0"`).
La compatibilité avec un schéma donné est indiquée dans le `$schema` URL.
