# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.2] · 2026-04-28

### Added
- **New page · Partenariats** (`partenariats.html`) targeting professional
  associations, sectoral federations, public institutions, and educational
  organizations who want tailored sectoral reports, memo series, conferences,
  workshops or territorial mappings. Includes a dedicated mailto-driven form
  with organization type and format selectors. All deliverables published
  under CC BY 4.0 like the rest of the editorial commons.
- **Three new nav entries**: Accueil (Home), Méthodologie (Methodology),
  and Partenariats (Partnerships). Total nav now 10 items.
- **Intermediate responsive breakpoint at 1100px** so the mobile menu kicks
  in before the 10-item nav becomes too crowded.

### Changed
- `nav-links` gap reduced from 28px to 22px and font-size from 14px to 13.5px
  to accommodate 10 items on desktop.
- Sitemap.xml updated to 14 URLs (was 12).

---

## [0.2.1] · 2026-04-28

### Added
- **Editorial disclosure section** on About page (block 02 in "Le qui"):
  three-paragraph statement explaining that the site is produced with AI
  assistance (Claude Opus 4.7) under factual verification against primary
  sources. Frames the disclosure as consistency with the methodological
  rigor required of indexed observatories.
- **Le Dispatch·iA #003 · Horlogerie premium et gouvernance IA** (3rd example
  dispatch in magazine format). Verified figures: -1.7% Swiss watch exports
  2025 (FH), +7% Richemont specialist watchmakers Q3 fiscal 2026 (Le Temps),
  +16.2%/year AI investment in luxury (Kearney 2026). Full Sources &
  traceability section with 3 primary URLs.
- **Swiss data integration · Angestellte Schweiz / DemoSCOPE study (April 2026)**.
  First nationally representative Swiss survey on AI/employment perception
  (n=1,028, three language regions, 23-30 March 2026). Integrated at 4 points:
  Swiss dashboard KPIs (17% / 24% / 22%), Veille (top of list), Timeline (29th
  milestone), economist references. AI cited as #1 individual cause of
  insecurity, formation continue rated most effective measure (M=3.27/4).
- **Static fallback logo link** on every page (`<a href="index.html">` or
  `../index.html`) inside the `<nav>` tag, ensuring the logo remains clickable
  even when JavaScript is disabled or delayed.
- **Methodology section 09 · Socle de données** (data foundation): full
  documentation of the 9 open datasets with descriptions and direct download
  links. Migrated from the Le Dispatch·iA hub to its proper home as a
  reference page for researchers and journalists.

### Changed
- **Top-of-page eyebrows removed** across all 10 affected pages
  (home, comparer, methodology, about, contact, suisse, france, veille,
  briefings, donnees). Pages now open directly with their main title without
  the small mono context line. Cleaner editorial entry into each page.
- **Comparer page main title** updated from "ce qui rapproche, ce qui sépare"
  to "deux modèles, une même question" (more direct and assertive).
- **Le Dispatch·iA hub data section**: replaced 9 dataset cards with a short
  CTA inviting readers to the Methodology page where the full data foundation
  is documented. Reinforces editorial architecture (commercial product page
  vs technical reference page).
- **Methodology page numbering bumped**: section 09 is now Socle de données,
  10 is Disclosure éditoriale, 11 is Contribuer.

### Fixed
- Various editorial em-dash residuals cleaned in dataset citations.

### Notes
- The "Presidential Daily Briefings" reference visible in earlier versions
  has been completely removed in favor of the Renaissance diplomatic
  dispatches metaphor.
- The transitions-ia.ch reference remains in the observatories cartography
  (assets/data/observatoires.json) as it is one of the 14 indexed
  observatories. No standalone link button to it on the About page.

---

## [0.2.0] · 2026-04-27

### Added
- **Le Dispatch·iA** product line (rebranded from Brief·iA) — sectoral strategic
  intelligence dispatches inspired by Renaissance diplomatic dispatches.
  Two editions: free HTML digest and paid executive PDF.
- **2 example dispatches** (#001 Swiss banks, #002 French executives) with
  magazine-style format, paywall, and Sources & traceability section.
- **Editorial disclosure** section (methodology #08) + per-dispatch micro-block
  acknowledging AI-assisted production with Claude Opus 4.7 (Research + Web Search)
  followed by manual fact-checking against primary sources.
- **9 open datasets** in `assets/data/` (CC BY 4.0):
  - `metiers-ia-fr.json` — 200 ROME occupations with AI exposure scoring
  - `metiers-ia-ch.json` — 324 NP 2010 Swiss occupations
  - `indicateurs-ia-fr.json` — 15 prospective indicators (FR)
  - `indicateurs-ia-ch.json` — 10 prospective indicators (CH)
  - `scenarios-ia-fr.json` & `scenarios-ia-ch.json` — 5 productivity scenarios each
  - `economistes-ia.json` & `economistes-ia-ch.json` — 12 + 18 referenced economists
  - `timeline-ia-emploi.json` — 28 milestones 2019-2026
- **`ai_type` field** on every source (generative/agentic/automation_broad/unspecified)
  to disambiguate which family of AI a study refers to.
- **Methodology section 03 · Distinguer les types d'IA** — explains discriminative,
  generative, agentic, and specialized scientific AI with affected occupations.
- **Methodology section 06 · Biais reconnus** — 8 acknowledged biases including
  the structural American bias (Stanford HAI, Felten-Brynjolfsson, Goldman 300M,
  MIT/Brookings/Pew domination).
- **Contact page** with mailto-driven form, URL params support
  (`?type=exec&dispatch=001`), and bidirectional links to Le Dispatch·iA.
- **Veille page** rebuilt with 8 verified report URLs (Stanford HAI, Coface/OEM,
  France Stratégie, APEC, Swiss AI Center, OFS, PwC, DARES/LaborIA).
- **Google Analytics 4** (`G-Q52TZ7QT84`) auto-injected on all 12 pages.
- **Canonical URL + Open Graph + Twitter Card** auto-injected per page.
- **`sitemap.xml` and `robots.txt`** auto-generated by `scripts/build.py`.
- **Responsive completion** : 4 breakpoints (480/720/960/touch), iOS zoom
  prevention, 44px min touch targets, horizontal scroll guards.
- **GitHub Actions workflow** for automatic deployment on every push to main.

### Changed
- Rebrand from `Brief·iA` to `Le Dispatch·iA` (FR) / `The Dispatch·iA` (EN)
  across nav, hub, examples, paywalls, mailto subjects.
- About page restructured with three sections: why · who · how to contribute.
  Bio condensed to single block with mention of *Guérill-IA* and *Darwinisme
  numérique*. Added LinkedIn and X to contact buttons.
- Veille reports now clickable cards opening primary sources in new tab,
  with `ai_type` badge in signal red mono.

### Fixed
- Nav rendered untranslated keys (`nav.suisse`, `nav.france`...) on contact page.
  Caused by local `t()` function shadowing the global one. Removed local function,
  routed all calls to `window.t()`.

### Removed
- Old `Brief·iA` branding completely purged from source and bundled output.

---

## [0.1.0] · 2026-04 (initial release)

### Added
- Bilingual FR/EN cartography with shared nav and footer via `components.js`
- Dashboard pages for Switzerland and France with KPIs + filterable cards
- Methodology page with 7 sections (criteria, calculation methods, taxonomies,
  triangulation, biases, frequency, contributing)
- Open data page with `observatoires.json` (14 entries) and download buttons
- Field Report (Veille) page with country filter
- Editorial design system: Fraunces + Instrument Sans + JetBrains Mono,
  paper/ink/signal red palette, no em-dashes, no emojis
- Standalone bundling pipeline (`build.py`) for `file://` and GitHub Pages
  compatibility

---

[0.2.0]: https://github.com/otakuch/observatoires-ia/releases/tag/v0.2.0
[0.1.0]: https://github.com/otakuch/observatoires-ia/releases/tag/v0.1.0
