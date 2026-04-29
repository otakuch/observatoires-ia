# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.5] · 2026-04-29

### Added · Reinvention pathways section

New editorial section "Pistes de réinvention" (Reinvention pathways) added
to both Swiss and France dashboard pages. For each country, five professional
archetypes with a plausible 3-5 year reinvention trajectory, presented as a
clickable accordion menu (drop-down) to avoid page overload.

**Five archetypes selected per country**, spanning a range of AI exposure
levels and economic domains:

1. **Bank advisor** (banking, high exposure) — pivot to wealth advisor with
   strong human relationship
2. **Social educator** (personal services, low exposure) — pivot to
   human-technology mediator in institutions
3. **Accountant** (business support, very high exposure) — pivot to expert
   reviewer & strategic SME partner
4. **Journalist** (communication, high exposure) — pivot to investigative
   journalist & epistemic guardian
5. **Software developer** (digital, very high exposure) — pivot to AI
   architect & systems orchestrator

**Each pathway articulates three elements**:
- **Future role**: what the person would do
- **Transferable skills**: what they already know that becomes valuable
- **Recommended training pathway**: calibrated on national systems

**Training pathways adapted by country**:
- **Switzerland**: CFC, ES, HES, EPF, ETHZ, CAS HES-SO, MAS, federal diplomas
  (Brevet fédéral, Diplôme fédéral), continuing education through professional
  associations (Veb.ch, SAQ, avastp, impressum, SGAICO), CFJM, MAZ
- **France**: DCG/DSCG/DEC for accounting, DEES/CAFERUIS/DEIS for social
  sector, Master 2/CGPC/AMF for banking, CPNEJ-recognized journalism schools,
  Polytechnique/Centrale/Mines/Télécom/INSA for engineering, CNAM, CPF, OPCO
  Atlas, OPCO Santé

**Each card cites supporting evidence**:
- DemoSCOPE April 2026 (24% large Swiss firms with AI tools)
- Coface OEM April 2026 (16.3% French jobs threatened 2-5 years)
- Indeed UK (-7% junior postings 2025)
- France Stratégie Métiers 2030

**Disclaimer**: explicit caveat that these are projections, not predictions.
Actual trajectories will depend on individual context, region/canton,
industry, and AI adoption pace within the company.

**CTA at the bottom** invites visitors to explore the full dashboard (200
ROME occupations FR, 324 NP 2010 occupations CH) or to see Le Dispatch·iA
sectoral reports.

### Changed
- New CSS components added: `.reinvent-section`, `.reinvent-list`,
  `.reinvent-item`, `.reinvent-trigger` (grid 60px/1fr/auto/auto),
  `.reinvent-content` (display:none by default), `.reinvent-future-role`
  (Fraunces italic 26px), `.reinvent-skills` (teal left border),
  `.reinvent-formation` (signal red left border), `.reinvent-cta-block`
  (dark background, paper text). Mobile breakpoint 720px hides exposure
  chips for compactness.
- New JavaScript handler in both pages for `.reinvent-trigger` clicks
  (toggles `.open` class on parent `.reinvent-item`).

---

## [0.2.4] · 2026-04-28

### Added · Major international research integration

Four new primary sources integrated to strengthen the methodological backbone
of the cartography:

- **Focaldata × Financial Times Workforce AI Tracker · Wave 1** (April 2026,
  n=4,119 UK+US). Monthly tracker. Key findings: 65% of workers used AI at
  least once, fewer than 1/5 daily, L-shaped adoption distribution. Aggregate
  productivity gain +3.5% (Tech +7.8%, Finance +5.1%). Training effect +37
  points daily usage but only 14% formally trained. UK managers pessimistic
  vs US optimistic on hiring expectations. ABC scenarios (Augmentation,
  Bifurcation, Crash) with Bifurcation as most likely near-term outcome.
- **Burn-Murdoch & O'Connor · FT** (26 February 2026). Methodological
  critique of seven task-based AI exposure scores. Yale Budget Lab finding
  cited: measures agree on low-exposure occupations but diverge sharply on
  the most exposed. Three factors typically missed: worker autonomy
  (Autor 2003), institutional regulation (radiology, therapy), second-order
  demand effects (Bessen).
- **Burn-Murdoch · FT** (25 April 2026). "What the AI 'jobpocalypse'
  narrative misses". Empirical demonstration via BLS historical data that
  productivity-employment relationship depends on demand elasticity, not
  AI's technical capability alone. Software and pro services: productivity
  ↑ + employment ↑. Manufacturing: productivity ↑ + employment ↓. Spreadsheets
  killed bookkeepers but created financial analysts. Bank tellers: smartphones
  killed them, not ATMs.
- **British Progress · Pedro Serôdio** (April 2026). UK labour market
  evidence synthesis. Conclusion: few signs of massive aggregate effects
  despite 54% UK SMEs using AI. Goldman Sachs and McKinsey predictions rest
  on theoretical full adoption. Anthropic Economic Index (Sep 2025, Jan 2026,
  March 2026): stable gap between predicted exposure and actual usage.

### Changed
- **Methodology page**: new bias block "Limits of task-based exposure scores"
  added to section 06 (recognized biases). Citing Yale Budget Lab,
  Burn-Murdoch/O'Connor, David Autor 2003, James Bessen.
- **Swiss dashboard**: new "International perspective" block after the three
  KPIs, contextualizing DemoSCOPE 2026 with Focaldata UK+US findings. Three
  new key facts: +37 pts training effect, 14% formally trained, +3.5%
  aggregate productivity gain.
- **Veille (Field Reports)**: 4 new reports at top of list. 13 reports total.
- **Timeline**: 4 new milestones. 33 events total.
- **Datasets**:
  - indicateurs-ia-fr.json: 15 → 17 indicators (added aggregate productivity
    and AI training gap)
  - indicateurs-ia-ch.json: 10 → 12 indicators (Swiss-adapted versions)
  - economistes-ia.json: 12 → 16 economists (added Autor, Bessen, Gimbel,
    Serôdio)
  - economistes-ia-ch.json: 18 → 20 (added Gimbel and Serôdio as
    international anchors)

### Notes
- All Focaldata and FT figures verified against the source PDFs and FT
  articles. The methodological critique (Burn-Murdoch/O'Connor + Yale Budget
  Lab) is now central to how the cartography frames its own exposure scores.
- The site now totals: 524 occupations (FR + CH) + 29 prospective indicators
  + 33 timeline milestones + 36 economists. Editorial commons keeps growing
  while methodological caveats become more rigorous.

---

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
