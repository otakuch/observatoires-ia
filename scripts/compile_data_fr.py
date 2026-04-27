#!/usr/bin/env python3
"""
Compile ROME IA observatory data into clean, publishable JSON files
for the observatoire[s]·ia GitHub repo.
"""
import json
from pathlib import Path

SRC_DIR = Path("/tmp/data_in/rome-ia-observatoire")
OUT_DIR = Path("/home/claude/site/assets/data")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# === ROME domain labels (from official France Travail nomenclature) ===
ROME_DOMAINS = {
    "A": "Agriculture & Pêche & Espaces naturels",
    "B": "Arts & Façonnage d'ouvrages d'art",
    "C": "Banque, Assurance, Immobilier",
    "D": "Commerce, Vente & Grande distribution",
    "E": "Communication, Média & Multimédia",
    "F": "Construction, Bâtiment & Travaux publics",
    "G": "Hôtellerie-Restauration, Tourisme, Loisirs & Animation",
    "H": "Industrie",
    "I": "Installation & Maintenance",
    "J": "Santé",
    "K": "Services à la personne & à la collectivité",
    "L": "Spectacle",
    "M": "Support à l'entreprise",
    "N": "Transport & Logistique",
    "P": "Éducation, Formation",
    "Q": "Immobilier (services)",
    "R": "Recherche",
    "S": "Numérique & Systèmes d'information",
    "T": "Industrie de process",
}

# === IA type inference from source text (heuristic) ===
def infer_ai_type(src_text: str) -> str:
    """Guess which type of AI a source refers to based on its description."""
    s = src_text.lower()
    if any(k in s for k in ["agentique", "agent", "richmond", "openai jobs"]):
        return "agentic"
    if any(k in s for k in ["llm", "génératif", "generative", "chatgpt", "copilot",
                            "openai", "eloundou", "anthropic", "stanford hai",
                            "noy", "peng", "brynjolfsson"]):
        return "generative"
    if any(k in s for k in ["coface", "frey", "osborne", "automatisation",
                            "autor", "acemoglu", "mckinsey", "bcg", "ilo",
                            "tufts", "digital planet", "ocde", "france stratégie"]):
        return "automation_broad"
    return "unspecified"


# === 1. Compile metiers JSON (jobs.json → metiers-ia-fr.json) ===

def compile_metiers():
    with open(SRC_DIR / "jobs.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    metiers = []
    for job in raw:
        # Extract latest validated tier-1 or tier-2 source for the headline score
        sorted_src = sorted(job["sources"],
                            key=lambda s: (s["tier"], -s["year"]))
        primary_score = sorted_src[0]["val"] if sorted_src else None

        # Average of all source values (rounded)
        scores = [s["val"] for s in job["sources"] if isinstance(s["val"], (int, float))]
        avg_score = round(sum(scores) / len(scores), 1) if scores else None

        # Sources transformed
        sources = []
        for s in job["sources"]:
            sources.append({
                "tier": s["tier"],
                "exposure_score": s["val"],
                "year": s["year"],
                "citation": s["src"],
                "ai_type": infer_ai_type(s["src"]),
            })

        metier = {
            "label": job["l"],
            "rome_domain": job["d"],
            "rome_domain_label": ROME_DOMAINS.get(job["d"], "Inconnu"),
            "fap_code": job.get("fap"),
            "median_salary_eur_month": job.get("sal"),
            "headcount_fr_2024": job.get("eff"),
            "applicable_regulations": job.get("reg", []),
            "exposure_score_primary": primary_score,
            "exposure_score_avg": avg_score,
            "exposure_scale": "0-100 (sources Tufts/Coface) ou 0-10 (sources académiques). Voir methodologie.",
            "impact_pattern": job.get("impact"),  # "pol" (polarisation) ou "vol" (volume)
            "openai_archetype": job.get("archetype_openai"),
            "rationale_fr": job.get("rat"),
            "reconversion_paths": [
                {"role": rn["t"], "explanation_fr": rn["x"]}
                for rn in job.get("rn", [])
            ],
            "sources": sources,
        }
        metiers.append(metier)

    out = {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/metiers-ia-fr.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "country": "FR",
        "nomenclature": "ROME 4.0 (France Travail)",
        "scope": "Métiers français · exposition à l'IA · 2026",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "count": len(metiers),
        "metiers": metiers,
    }
    return out


# === 2. Compile predictions/indicators JSON ===

def compile_indicators():
    with open(SRC_DIR / "sources.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    indicators = []
    for p in raw["predictions"]:
        sources = []
        for s in p["sources"]:
            sources.append({
                "tier": s["tier"],
                "value": s["val"],
                "year": s["year"],
                "citation": s["src"],
                "ai_type": infer_ai_type(s["src"]),
            })
        # Compute simple statistics
        vals = [s["value"] for s in sources]
        indicator = {
            "title": p["title"],
            "unit": p["unit"],
            "n_sources": len(sources),
            "value_min": min(vals) if vals else None,
            "value_max": max(vals) if vals else None,
            "value_median": round(sorted(vals)[len(vals)//2], 2) if vals else None,
            "description_fr": p.get("desc", ""),
            "sources": sources,
        }
        indicators.append(indicator)

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/indicateurs-ia-fr.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "country": "FR",
        "scope": "Indicateurs prospectifs IA & emploi · France",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "count": len(indicators),
        "indicators": indicators,
    }


# === 3. Compile timeline JSON ===

def compile_timeline():
    with open(SRC_DIR / "sources.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    timeline = []
    for evt in raw["timeline"]:
        timeline.append({
            "year": evt["year"],
            "title": evt["title"],
            "summary_fr": evt.get("body", ""),
            "headline_value": evt.get("val"),
            "tier": evt.get("tier"),
            "citation": evt.get("src"),
            "ai_type": infer_ai_type(evt.get("src", "") + " " + evt["title"]),
        })

    timeline.sort(key=lambda x: x["year"])

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/timeline-ia-emploi.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "scope": "Jalons IA & emploi · 2019-2026 · monde + France",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "count": len(timeline),
        "events": timeline,
    }


# === 4. Compile scenarios JSON ===

def compile_scenarios():
    with open(SRC_DIR / "sources.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    scenarios = []
    for s in raw["scenarios"]:
        scenarios.append({
            "name": s["name"],
            "annual_productivity_growth_range": s["range"],
            "probability_pct": s["pct"],
            "color_hex": s["color"],
        })

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/scenarios-ia-fr.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "country": "FR",
        "scope": "Scénarios prospectifs · gains de productivité IA en France 2025-2030",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "method_note": "Probabilités agrégées à partir de 12 économistes référencés et de méta-analyses 2024-2026. Voir economistes-ia.json pour le détail des positions.",
        "count": len(scenarios),
        "scenarios": scenarios,
    }


# === 5. Compile economistes JSON ===

def compile_economistes():
    with open(SRC_DIR / "sources.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    SCENARIO_NAMES = ["Stagnation", "Croissance modérée", "Accélération IA",
                      "Transformation majeure", "Rupture technologique"]

    economists = []
    for e in raw["economists"]:
        bars = e["bars"]
        position = {SCENARIO_NAMES[i]: bars[i] for i in range(len(bars))}
        # Most-likely scenario = max bar
        max_idx = bars.index(max(bars))
        economists.append({
            "name": e["name"],
            "institution": e["inst"],
            "scenario_distribution_pct": position,
            "most_likely_scenario": SCENARIO_NAMES[max_idx],
        })

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/economistes-ia.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "scope": "Économistes & chercheurs référencés · positions sur scénarios IA",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "method_note": "Positions reconstruites à partir des publications académiques et déclarations publiques 2023-2026.",
        "count": len(economists),
        "economists": economists,
    }


# === MAIN ===
if __name__ == "__main__":
    print("Compiling JSON datasets…")

    files = {
        "metiers-ia-fr.json": compile_metiers(),
        "indicateurs-ia-fr.json": compile_indicators(),
        "timeline-ia-emploi.json": compile_timeline(),
        "scenarios-ia-fr.json": compile_scenarios(),
        "economistes-ia.json": compile_economistes(),
    }

    for fname, data in files.items():
        path = OUT_DIR / fname
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        size_kb = path.stat().st_size / 1024
        count = data.get("count", "?")
        print(f"  ✓ {fname}: {count} entries · {size_kb:.1f} KB")

    print("\nDone. Files written to:", OUT_DIR)
