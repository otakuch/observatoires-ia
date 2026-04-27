#!/usr/bin/env python3
"""
Compile Swiss observatory data (transitions-ia.ch dist) into clean,
publishable JSON files for the observatoire[s]·ia GitHub repo.

Inputs:  /tmp/data_in_ch/dist/*
Outputs: /home/claude/site/assets/data/*-ch.json
"""
import json
from pathlib import Path

SRC_DIR = Path("/tmp/data_in_ch/dist")
OUT_DIR = Path("/home/claude/site/assets/data")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# === NP 2010 domain labels (Swiss occupation classification) ===
# Inferred from sample jobs in d.json/d_ext2.json + harmonised with French ROME
NP_DOMAINS = {
    "A": "Agriculture, sylviculture & pêche",
    "B": "Artisanat d'art & métiers d'art",
    "C": "Banque, assurance, immobilier",
    "D": "Commerce, vente & marketing",
    "E": "Communication, média, traduction",
    "F": "Construction & bâtiment",
    "G": "Hôtellerie, restauration, services personnels",
    "H": "Industrie & production",
    "I": "Maintenance, installation, réparation",
    "J": "Santé & soins",
    "K": "Services à la personne & sécurité publique",
    "L": "Spectacle & arts vivants",
    "M": "Support à l'entreprise (comptabilité, RH, juridique)",
    "N": "Transport & logistique",
    "O": "Audiovisuel & contenus numériques",
    "P": "Justice & sécurité publique spécialisée",
    "Q": "Professions juridiques",
    "R": "Éducation, formation, recherche",
    "S": "Numérique & systèmes d'information",
}

# === IA type inference (same heuristic as France) ===
def infer_ai_type(src_text: str) -> str:
    s = (src_text or "").lower()
    if any(k in s for k in ["agentique", "agent", "richmond", "openai jobs"]):
        return "agentic"
    if any(k in s for k in ["llm", "génératif", "generative", "chatgpt", "copilot",
                            "openai", "eloundou", "anthropic", "stanford hai",
                            "noy", "peng", "brynjolfsson"]):
        return "generative"
    if any(k in s for k in ["coface", "frey", "osborne", "automatisation",
                            "autor", "acemoglu", "mckinsey", "bcg", "ilo",
                            "tufts", "digital planet", "ocde", "france stratégie",
                            "ofs", "espa", "kof"]):
        return "automation_broad"
    return "unspecified"


# === 1. Compile metiers JSON (d.json + d_ext2.json) ===

def compile_metiers():
    d1 = json.loads((SRC_DIR / "d.json").read_text(encoding="utf-8"))
    d2 = json.loads((SRC_DIR / "d_ext2.json").read_text(encoding="utf-8"))
    raw = d1 + d2

    # De-duplicate by label (priority to d.json which appears first)
    seen = set()
    unique_jobs = []
    for j in raw:
        if j["l"] not in seen:
            seen.add(j["l"])
            unique_jobs.append(j)

    metiers = []
    for job in unique_jobs:
        sources = job.get("sources", [])
        sorted_src = sorted(sources, key=lambda s: (s["tier"], -s["year"])) if sources else []
        primary_score = sorted_src[0]["val"] if sorted_src else None

        scores = [s["val"] for s in sources if isinstance(s["val"], (int, float))]
        avg_score = round(sum(scores) / len(scores), 1) if scores else None

        sources_clean = []
        for s in sources:
            sources_clean.append({
                "tier": s["tier"],
                "exposure_score": s["val"],
                "year": s["year"],
                "citation": s["src"],
                "ai_type": infer_ai_type(s["src"]),
            })

        metier = {
            "label": job["l"],
            "np_domain": job["d"],
            "np_domain_label": NP_DOMAINS.get(job["d"], "Inconnu"),
            "fap_code": job.get("fap"),
            "median_salary_chf_month": job.get("sal"),
            "headcount_ch_2024": job.get("eff"),
            "exposure_score_primary": primary_score,
            "exposure_score_avg": avg_score,
            "exposure_scale": "0-10 (sources académiques) ou 0-100 (Tufts/Coface). Voir methodologie.",
            "rationale_value": job.get("rat"),  # numeric (0 or score)
            "reconversion_paths": [
                {"role": rn["t"], "explanation_fr": rn["x"]}
                for rn in job.get("rn", [])
            ],
            "sources": sources_clean,
            "_origin_set": job.get("_src"),  # "D" or other
        }
        metiers.append(metier)

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/metiers-ia-ch.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "country": "CH",
        "nomenclature": "NP 2010 (OFS · 394 groupes de professions)",
        "scope": "Métiers suisses · exposition à l'IA · 2026",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "underlying_dashboard": "https://observatoire.naullynicolas.ch/ch/",
        "count": len(metiers),
        "metiers": metiers,
    }


# === 2. Compile indicators JSON (preds.json + pred_summaries.json) ===

def compile_indicators():
    preds = json.loads((SRC_DIR / "preds.json").read_text(encoding="utf-8"))
    summaries_list = json.loads((SRC_DIR / "pred_summaries.json").read_text(encoding="utf-8"))
    # pred_summaries is a list of strings, in same order as preds

    indicators = []
    for i, p in enumerate(preds):
        sources = []
        for s in p["sources"]:
            sources.append({
                "tier": s["tier"],
                "value": s["val"],
                "year": s["year"],
                "citation": s["src"],
                "ai_type": infer_ai_type(s["src"]),
            })
        vals = [s["value"] for s in sources]
        summary = summaries_list[i] if i < len(summaries_list) else ""
        indicator = {
            "title": p["title"],
            "unit": p["unit"],
            "n_sources": len(sources),
            "value_min": min(vals) if vals else None,
            "value_max": max(vals) if vals else None,
            "value_median": round(sorted(vals)[len(vals)//2], 2) if vals else None,
            "summary_fr": summary,
            "description_fr": p.get("desc", ""),
            "sources": sources,
        }
        indicators.append(indicator)

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/indicateurs-ia-ch.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "country": "CH",
        "scope": "Indicateurs prospectifs IA & emploi · Suisse",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "underlying_dashboard": "https://observatoire.naullynicolas.ch/ch/",
        "count": len(indicators),
        "indicators": indicators,
    }


# === 3. Compile scenarios JSON ===

def compile_scenarios():
    raw = json.loads((SRC_DIR / "scenarios.json").read_text(encoding="utf-8"))
    scenarios = []
    for s in raw:
        scenarios.append({
            "name": s["name"],
            "annual_productivity_growth_range": s["range"],
            "probability_pct": s["pct"],
            "color_hex": s["color"],
        })

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/scenarios-ia-ch.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "country": "CH",
        "scope": "Scénarios prospectifs · gains de productivité IA en Suisse 2025-2030",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "method_note": "Probabilités agrégées à partir de 18 économistes/institutions référencés et de méta-analyses 2024-2026. Voir economistes-ia-ch.json pour le détail.",
        "count": len(scenarios),
        "scenarios": scenarios,
    }


# === 4. Compile economists JSON ===

def compile_economists():
    raw = json.loads((SRC_DIR / "economists.json").read_text(encoding="utf-8"))
    SCENARIO_NAMES = ["Stagnation", "Croissance modérée", "Accélération IA",
                      "Transformation majeure", "Rupture technologique"]

    economists = []
    for e in raw:
        bars = e["bars"]
        position = {SCENARIO_NAMES[i]: bars[i] for i in range(len(bars))}
        max_idx = bars.index(max(bars))
        economists.append({
            "name": e["name"],
            "institution": e["inst"],
            "scenario_distribution_pct": position,
            "most_likely_scenario": SCENARIO_NAMES[max_idx],
        })

    return {
        "$schema": "https://github.com/otakuch/observatoires-ia/blob/main/schemas/economistes-ia-ch.schema.json",
        "version": "0.3.0",
        "compiled_at": "2026-04-26",
        "scope": "Économistes & institutions référencés (focus Suisse) · positions sur scénarios IA",
        "license": "CC BY 4.0",
        "source_aggregator": "Naully Nicolas · observatoire[s]·ia",
        "documentation_url": "https://observatoire-ia.naullynicolas.ch/methodologie.html",
        "count": len(economists),
        "economists": economists,
    }


# === MAIN ===
if __name__ == "__main__":
    print("Compiling Swiss JSON datasets…")

    files = {
        "metiers-ia-ch.json": compile_metiers(),
        "indicateurs-ia-ch.json": compile_indicators(),
        "scenarios-ia-ch.json": compile_scenarios(),
        "economistes-ia-ch.json": compile_economists(),
    }

    for fname, data in files.items():
        path = OUT_DIR / fname
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        size_kb = path.stat().st_size / 1024
        count = data.get("count", "?")
        print(f"  ✓ {fname}: {count} entries · {size_kb:.1f} KB")

    print("\nDone. Files written to:", OUT_DIR)
