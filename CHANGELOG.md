# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] · 2026-05-02

### Changed · About page rewrite

The About page (a-propos.html) is rewritten to integrate the analytical
acquisitions of v0.2.9 (three-dimension reading frame) and v0.3.0 (TCO and
sovereignty layer), and to fill an editorial gap on the "Three principles"
section that previously had a title and sub but empty cards.

### Added · "The frame · 4 reading angles" section
- New section inserted between "Why this project" and "Who", structured as
  4 method-grid blocks (parallel to the methodology page layout):
  - 01 Demand trajectory: income effect (Imas & Comin 2026), with chef vs.
    credit analyst example
  - 02 Relational sector: indirect AI beneficiaries (care, hospitality,
    craft, training, performance)
  - 03 AI type: generative / specialized / robotic, with the canonical
    radiologist vs. journalist example
  - 04 TCO and sovereignty (4th blind spot): Singh Tomer 2026 TCO framework,
    Gartner $3-per-resolution prediction, 72% CIO breakeven/loss rate,
    European sovereign LLM ecosystem (Mistral, Apertus, Aleph Alpha,
    Minerva, PhariaAI, LightOn)

### Added · Three real principle cards
The "Trois principes" section had a title and intro but never displayed
the principles themselves (the `<div id="princGrid">` was a never-filled
placeholder). Now properly written as three method-grid cards:
- 01 Primary sources: never cite second-hand, traceability to original
  publication, Tier 1-4 source hierarchy
- 02 Explicit biases: documenting limits with as much care as findings,
  citing NBER w35110 (×3.6 LLM divergence) and Yale Budget Lab (variance
  0.03 vs 0.48), 9 structural biases acknowledged
- 03 Open data: 524 occupations + 23 indicators + 40 milestones + 38
  economists + 27 reports under CC BY 4.0, no paywall on Dispatches, code
  on GitHub

### Changed · KPI label refresh
- "Observatories connected in v0.2" → "CH + FR observatories mapped"
  (removes obsolete version reference)

### Notes
- The About page now spans 5 logical sections (Why · Frame · Who ·
  Principles · Contribute) instead of 4 (Why · Who · Principles ·
  Contribute), with the new Frame section providing the missing
  editorial bridge between the project's existence rationale and its
  practitioner.
- All new content uses formal-direct French voice, zero em-dashes,
  practitioner tone, with concrete examples and inline citations
  (Imas & Comin 2026, Singh Tomer 2026, NBER w35110, Yale Budget Lab,
  Mistral, Apertus).
- The existing Disclosure block (Naully + Claude Opus 4.7 production
  process) is preserved unchanged.
- Existing nav and footer links to a-propos.html were already correct.
  No link updates were needed across other pages.

---

## [0.3.0] · 2026-05-02

### Added · 4th analytical blind spot: real TCO and digital sovereignty

This release introduces a new analytical layer to the observatory, complementing
the three-dimension reading frame (demand trajectory, relational sector, AI type)
introduced in v0.2.9 with what the editorial team identifies as the 4th blind spot
that organizations systematically underestimate: the gap between published token
prices and real total cost of ownership, and the question of jurisdictional
sovereignty over data and inference infrastructure.

### Added · Homepage warning section
- New "Mise en garde · 4e angle mort" section inserted between the Cadre
  analytique and the field reports. Two cards:
  - **Coûts cachés**: Gartner's prediction of GenAI cost underestimation by
    500% to 1000%, $3 cost-per-resolution by 2030 exceeding offshore agents,
    72% CIO breakeven/loss rate, 50% PoC abandonment rate, 90% CIO cost-driven
    value limitation.
  - **Souveraineté**: Mistral's $830M debt raise from 7 European banks for
    sovereign Paris data center, Apertus EPFL/ETH/CSCS as the first public
    fully open Swiss LLM compliant with EU AI Act and Swiss FADP, the
    European sovereign ecosystem (Aleph Alpha, PhariaAI, LightOn, H Company,
    Minerva).

### Added · Sovereignty section in all 3 Dispatches
- New `brief-sov` section added to each Dispatch (banking Swiss, executives
  France, premium watchmaking), structured as 3-card pattern with
  context-specific framing:
  - **Banque suisse**: Apertus + Swisscom alignment with FADP/FINMA,
    Mistral for European-zone branches, CLOUD Act extra-territorial risk
    against banking secrecy
  - **Cadres France**: Mistral La Plateforme + Le Chat Pro, broader
    European ecosystem (Aleph Alpha, PhariaAI, LightOn, Apertus), GDPR/NIS2
    /upcoming AI Act compliance cost
  - **Horlogerie premium**: Apertus alignment with Swiss Made narrative,
    Mistral for European boutique markets, narrative inconsistency risk
    when sovereignty is undermined

### Fixed · TCO section bilingual coverage
- A latent bug from a previous session: the brief-tco section existed in HTML
  on all 3 Dispatches but its i18n strings (b1.tco.*, b2.tco.*, b3.tco.*)
  existed only in the English block. In French, the section displayed raw
  i18n keys instead of content. This release restores full FR + EN bilingual
  coverage for the TCO sections on all 3 Dispatches.

### Added · 5 new field reports in veille
- Singh Tomer · "Human Labor Versus AI: A Total Cost of Ownership and
  Task-Suitability Framework" · April 2026 (the central theoretical reference
  on TCO economic framing)
- Gartner · Patrick Quinlan · "GenAI cost per resolution will exceed
  offshore human agents by 2030" · January 2026 (the reference prediction)
- EPFL · ETH Zurich · CSCS · Apertus launch · September 2025 (Switzerland's
  first public fully open LLM)
- Mistral AI · "$830M debt raise from 7 European banks" · March 2026 (the
  largest European AI debt operation, sovereign infrastructure)
- Index.dev · BenchLM · EuropeanStack synthesis · "European LLM ecosystem
  2026" · February 2026 (Mistral, Aleph Alpha, Apertus, Minerva, PhariaAI,
  LightOn mapping)

### Added · 3 timeline milestones
- September 2025: Apertus public release (CHF 20M Swiss federal funding)
- January 2026: Gartner $3-per-resolution prediction
- March 2026: Mistral AI $830M debt round (consortium 6 European + 1 Japanese
  banks, no US bank, 13 800 Nvidia GB300 GPUs)

### Added · 2 new indicators
- France: "Souveraineté numérique IA · l'enjeu européen pour les organisations
  françaises" with Mistral, Aleph Alpha, Apertus, Minerva ecosystem
- Switzerland: "Souveraineté IA helvétique · Apertus et l'écosystème suisse
  de l'IA fully open" with CHF 20M Swiss AI Initiative funding, 1M+
  downloads, Meditron CHUV deployment May 2026

### Added · CSS components
- `.warning-section`, `.warning-card`, `.warning-grid` (homepage gradient
  paper card with red signal accent bar)
- `.brief-sov`, `.brief-sov-inner`, `.brief-sov-grid`, `.brief-sov-card`
  (dark ink card with signal red accent, parallel to `.brief-tco-*`)
- All with mobile breakpoints

### Site totals
571 occupations (FR + CH) + 23 indicators + 40 milestones + 38 economists
+ 27 verified field reports.

### Notes
- The X.com link cited in the user request was blocked by robots.txt and
  could not be fetched. Five primary and secondary web sources were
  collected as substitute and integrated into the corpus.
- The radiologist vs journalist canonical example, established in v0.2.9
  for AI type differentiation, is preserved unchanged. The TCO + sovereignty
  layer enriches the frame without contradicting it.
- All new content uses formal-direct French voice, zero em-dashes,
  practitioner tone, no "révolution" or "disruption" vocabulary, with
  concrete examples and inline academic citations.

---

## [0.3.0] · 2026-05-02

### Added · Total Cost of Ownership dimension fully sourced

This minor release consolidates the economic-cost dimension introduced in
prior versions and grounds it on a substantially expanded source corpus.
The « cost beyond token price » angle is one of the most underweighted by
organizations in 2026 strategic planning. The observatory now treats it
with the same rigor as the other three analytical dimensions (demand
trajectory, relational sector, AI type).

**5 new reports added to veille.json (now 24 total):**
- **Gartner · Will Sommer (March 25, 2026)** · The LLM Cost Paradox:
  by 2030, inference cost on a 1-trillion-parameter LLM will drop by 90%
  for providers, but enterprise inference costs will rise because agentic
  models consume 5-30x more tokens per task and reasoning models hide
  internal consumption. Direct quote: « CPOs should not confuse the
  deflation of commodity tokens with the democratization of frontier
  reasoning. »
- **Gartner · Patrick Quinlan (January 26, 2026)** · GenAI customer
  service cost per resolution will exceed $3 by 2030, more than most B2C
  offshore human agents. Strategic implication: full automation will be
  prohibitively expensive for most organizations.
- **Gartner · Hung LeHong (November 20, 2025)** · Organizations
  underestimate GenAI total cost by 500% to 1000%. 72% of CIOs report
  break-even or losses on AI investments. 50% of GenAI projects abandoned
  after PoC.
- **AISuperior (March 16, 2026)** · LLM Cost Paradox empirically
  documented: per-token price -10x since 2022, but token consumption +100x
  for reasoning workloads. Documented extreme: 600 tokens consumed for
  2 words of output.
- **Roboto (April 10, 2026)** · The French linguistic tax: French
  consumes +60% tokens vs English on the same agent task. Strategic
  consequence for French and Romandie organizations: model selection
  must be even more rigorous than for English-speaking counterparts.

**2 new timeline milestones:**
- January 2026 · Gartner GenAI cost prediction (>$3/resolution by 2030)
- March 2026 · LLM Cost Paradox documented (tokens -90%, consumption +100x)

**1 new indicator FR + 1 new indicator CH:**
- France: « Coût total réel de l'IA · l'angle mort des organisations
  françaises » (4 sources, factor 5-10 underestimation, median 7)
- Switzerland: « Coût total réel de l'IA · vulnérabilité spécifique des
  PME suisses » (5 sources, including DemoSCOPE 9% TPE-PME and Roboto
  linguistic tax, calling for cantonal/SECO support on TCO calculation)

### Changed · home.frame.d4 reinforced

The 4th analytical card on the homepage (« Le prix par token n'est pas
le coût réel ») is enriched with the LLM Cost Paradox documentation and
the French linguistic tax (+60% tokens vs English). The card now stands
as the strongest economic argument on the homepage, complementing the
three existing dimensions (demand trajectory, relational sector, AI type).

### Notes
- The TCO section in methodologie.html (07) and the brief-tco sections
  in all 3 Dispatches were already in place from earlier work on the
  Tomer paper. This release consolidates them with the broader Gartner +
  AISuperior + Roboto corpus.
- All new datasets respect the formatting standards: ai_type tagged,
  tier scoring, CC BY 4.0 license, source URLs verified.
- No em-dashes in new content. JSON validates.
- The X.com URL referenced by the user was blocked by robots.txt, so
  source enrichment was conducted through the broader 2025-2026 web
  corpus, focusing on Gartner, AISuperior, and Roboto as the most
  rigorous sources on the TCO topic.

---

## [0.2.9] · 2026-04-30

### Added · Three-dimension analytical frame surfaced across the site

The observatory's three-dimension analytical frame (demand trajectory,
relational sector, AI type) is now explicitly surfaced on four key pages
of the site. Until now this frame was implicit in the methodology and the
metier datasets but not visible to a first-time visitor.

- **index.html · Hero pitch line**. New short statement between H1 and lede:
  « Les IA ne menacent pas tous les métiers de la même façon. Ce n'est pas la
  même IA qui affecte un radiologue, un journaliste et un chauffeur. Et tous
  les métiers exposés ne sont pas sous pression : certains en bénéficient. »
  Styled in Fraunces italic to read as a manifesto pitch, between the title
  and the more developed lede paragraph.

- **index.html · "Cadre analytique" section**. New section after the manifesto,
  three side-by-side cards with mono icons (↑ → ↓, ⌭, ✦ ◉ ⬡) presenting:
  - 01 Trajectoire de demande (citing Imas & Comin 2026 income effect, with
    chef gastronomique vs analyste crédit example)
  - 02 Secteur relationnel (with social educator example)
  - 03 Type d'IA (with the canonical radiologist vs journalist example,
    linking to Methodology)

- **methodologie.html · Synthesis table**. New three-column synthesis at the
  end of section 03 (Distinguer les types d'IA), with icons ✦ (generative),
  ◉ (specialized), ⬡ (robotic). Each card lists what the family does and
  occupations affected in priority. Complements without contradicting the
  existing four-category breakdown (a/b/c/d).

- **observatoires/comparer.html · Cadre commun block**. New section between
  the institutional context block and the comparison table, presenting the
  three dimensions as the shared reading grid that makes the cross-border
  comparison possible without flattening national specificities.

- **partenariats.html · Three strategic questions**. New section between
  audience cards and delivery formats, translating the three dimensions
  into actionable questions for an executive committee or HR leadership:
  - "Quels sont nos métiers sous pression baissière réelle, et pas
    seulement exposés ?"
  - "Avons-nous des métiers relationnels que nous sous-valorisons dans
    notre stratégie de transformation ?"
  - "Quelle IA affecte réellement chaque fonction, et avec quel calendrier ?"

### Added · CSS components
- `.frame-section`, `.frame-grid`, `.frame-card` (3-column home cards with
  icon, tag, title, body, example)
- `.hero-pitch` (Fraunces italic between H1 and lede)
- `.aitype-summary`, `.aitype-summary-grid`, `.aitype-summary-card` (synthesis
  cards in methodology)
- `.cmp-dim-section`, `.cmp-dim-grid`, `.cmp-dim-card` (3-dim block on
  Comparer page)
- `.pt-questions-section`, `.pt-questions-list`, `.pt-question` (numbered
  list of strategic questions on Partnerships page)
- All with mobile breakpoints (single column at 720px or 960px)

### Notes
- All new content uses the radiologist vs journalist example as canonical
  illustration of AI-type differentiation, per the editorial direction.
- No em-dashes anywhere in the new content. Voice is formal-direct,
  practitioner tone, without the words "révolution" or "disruption".
- Existing content (methodology section 03 a/b/c/d breakdown, manifesto
  three paragraphs, partnership audience cards) is untouched.
- Each new block reads independently. Visitors who skip the manifesto and
  jump to the cadre analytique still get the frame in 30 seconds.

---

## [0.2.8] · 2026-04-30

### Changed · Editorial pivot: from paywall to open access + dual action bridges

This release marks a significant editorial shift in how Le Dispatch·iA is
distributed and monetized. The two-tier model (free HTML edition + paid PDF
"executive edition" at $99/unit or annual subscription) is replaced by a
single integral edition, fully and freely accessible online, with two
contact-driven passerelles for organisations needing customisation or
operational support.

### Added · Dispatch enrichments

- **New ROLES section** added to all three published Dispatches (Banque
  suisse #001, Cadres France #002, Horlogerie premium #003). Each Dispatch
  now articulates **five professional archetypes** (cards with exposure
  score, headcount, narrative shift, and pivot suggestion). The section
  bridges the architectural-strategic level of the Dispatch with the
  individual-professional level addressed by the Pistes de réinvention on
  the country dashboards. Each card links back to the dashboard for the
  full 200-324 occupation map.
- **New ACTION CTA section** at the foot of each Dispatch, replacing the
  former paywall block. Two cards:
  - **Une dépêche dédiée à votre établissement** (custom Dispatch on the
    organisation's exact perimeter, ~12-15 page, calibrated on internal
    constraints, sourced like the public Dispatches)
  - **Du cadrage à l'architecture des workflows** (operational engagement,
    moving from diagnosis to implementation: workflow architecture,
    governance, training paths)
  Both cards link to `contact.html?type=custom&dispatch=00X` and
  `contact.html?type=ops&dispatch=00X` with parameter pre-filling.

### Changed · Le Dispatch·iA hub
- Title: "Rapports sectoriels stratégiques" → "Dépêches sectorielles
  stratégiques"
- Lede rewritten: "Une dépêche par mois en deux éditions" → "Une dépêche
  par mois en intégralité, librement accessible"
- Subscription CTA replaced by Dual CTA (custom Dispatch + operational
  engagement)
- Numbers updated: ~1500 mots → ~2500 mots, 12-18 pages → 12-15 pages

### Changed · Methodology
- Section "Le Dispatch·iA · format" rewritten:
  - "Deux éditions" → "Une dépêche intégrale"
  - Paragraph rewritten to describe the single complete version, the
    absence of paywall or hidden premium tier, and the two action bridges
    described at the foot of every Dispatch.

### Changed · Contact form
- Form options `dispatch-exec` (executive PDF) and `dispatch-sub`
  (subscription) replaced by `dispatch-custom` (custom Dispatch) and
  `dispatch-ops` (operational engagement), aligned with the new Dispatch
  CTA cards.

### Added · CSS components
- `.brief-roles-section`, `.brief-roles-grid`, `.brief-role-card` (with
  num, domain, name, stats, shift, pivot, link)
- `.brief-cta-actions`, `.brief-cta-grid`, `.brief-cta-card` (with tag,
  title, desc, arrow)
- Mobile responsive overrides at 960px

### Notes
- This pivot is consistent with the editorial commons positioning
  reinforced in v0.2.0 (Methodology disclosure, CC BY 4.0 datasets) and
  with the Partenariats page added in v0.2.2. The Dispatch becomes a
  loss leader for the consultative engagement model, rather than a
  standalone paid product.
- All 13 i18n key blocks (FR + EN, 3 Dispatches × 2 langues + hub) updated
  consistently. No orphaned keys, all new keys resolve correctly under
  Node test.
- The methodological caveats added in v0.2.7 (NBER w35110, Yale Budget
  Lab figures) are fully preserved.

---

## [0.2.7] · 2026-04-29

### Added · Methodological reinforcement: AI exposure scores instability

Integration of two major studies that strengthen the methodological backbone
of the cartography on the (in)stability of task-based AI exposure scores.

- **Yin, Vu, Persico · NBER w35110** (April 2026). Empirical demonstration
  that LLM-based self-assessed AI exposure measures are highly fragile.
  Three frontier models applying the same rubric on identical tasks produce
  a 3.6-fold divergence in mean exposure, with agreement as low as 57%.
  Difference-in-differences coefficients vary 2.4-fold across annotators.
  County-level estimates flip from significant negative to insignificant
  positive depending on the model. The paper formalizes this non-classical
  measurement error and warns against treating evolving LLMs as static
  instruments.
- **Gimbel, Kendall, Kulsakdinun · Yale Budget Lab** (February 19, 2026).
  Systematic comparison of 7 dominant AI exposure metrics (Eloundou OpenAI,
  Felten AIOE, Webb, Eisfeldt, Tomlinson Microsoft Copilot, etc.) across
  867 SOC 2018 occupations. Three key takeaways: metrics broadly agree;
  disagreement is about magnitude not whether an occupation is exposed;
  exposure indicates impact zones, not automation predictions. Canonical
  examples: variance 0.03 for plumbers (full consensus on low exposure)
  vs. 0.48 for computer programmers (major disagreement on magnitude).
  Open data XLSX downloadable.

### Changed · Methodology section reinforced

- **Bias block 06.2 "Limits of task-based exposure scores"** rewritten to
  cite both new studies with their precise figures (3.6-fold divergence,
  57% agreement, 2.4-fold DiD variance, variance 0.03 vs 0.48). The block
  now reads as the strongest methodological caveat in the cartography:
  exposure scores are technical capability indicators, not employment
  predictions, and must never be read from a single measure or a single
  annotator model.

### Datasets updated
- veille.json: 13 → 15 reports (+ NBER w35110, Yale Budget Lab)
- timeline-ia-emploi.json: 33 → 35 milestones
- economistes-ia.json: 16 → 17 (+ Yin/Vu/Persico as joint entry)
- economistes-ia-ch.json: 20 → 21 (same, as international anchor)
- indicateurs-ia-fr.json: 17 → 18 (+ "Instabilité des scores d'exposition")
- indicateurs-ia-ch.json: 12 → 13 (+ "Robustesse des prédictions IA appliquées au tissu suisse")

### Site totals
524 occupations (FR + CH) + 31 indicators + 35 milestones + 38 economists.
The methodological caveats now constitute one of the most rigorous critiques
publicly available on AI labor-market exposure scoring.

---

## [0.2.6] · 2026-04-29

### Added · Pre-publication polish pack

Six attractivity improvements applied to the homepage and footer before
official public launch.

- **Homepage `<title>` and meta description rewritten** for SEO. Old:
  "Cartographie indépendante des observatoires emploi & IA · CH/FR" (too long,
  insider jargon). New: "Comprendre l'impact des IA sur le travail · Suisse &
  France" (shorter, search-friendly, contains the keywords people actually
  type). Meta description now mentions concrete numbers (524 métiers, 14
  observatoires) and the editorial postulate (lecture factuelle plutôt
  qu'émotionnelle).
- **Three hero KPI stats refreshed** with April 2026 data:
  - **65%** of UK+US workers have used AI at work (Focaldata × FT Wave 1,
    April 2026), with the L-shaped distribution caveat
  - **24%** of large Swiss firms have introduced AI vs 9% for SMEs
    (DemoSCOPE / Angestellte Schweiz, April 2026), highlighting the Swiss
    asymmetry
  - **524** mapped occupations (200 ROME France + 324 NP 2010 Switzerland),
    promoting the open data dimension
- **Latest field reports section moved from bottom to top** of homepage
  (right after manifesto). Three most recent verified reports now appear
  immediately as clickable cards. The most powerful editorial asset of the
  site is now the most visible.
- **New "Latest dispatch" tease section** added between field reports and
  country teasers. Dark ink card with signal red accent bar, featuring The
  Dispatch·iA #003 (Premium watchmaking and AI governance). Two CTAs: read
  the dispatch + see all dispatches.
- **Third "Compare both" card** added to the country teasers grid. Layout
  expanded from 2 to 3 columns. The Comparer card uses a feature variant
  (paper-2 background, ink hover) to signal it as the project's unique value
  proposition. Mobile collapses to 1 column.
- **Footer entirely rewritten** as 4-column grid:
  1. Brand + tagline
  2. Explore links (Suisse, France, Comparer, Le Dispatch·iA)
  3. About links (Méthodologie, Veille, Partenariats, Contact)
  4. Meta column with **last update date** (29 avril 2026), open data license,
     version
  Plus a bottom row with copyright and "Designed and operated by Naully
  Nicolas" with link to naullynicolas.ch. Mobile collapses to single column.

### Changed
- `country-teasers` grid changed from 2 columns to 3 columns on desktop
- `footer` wrapper: removed redundant padding (now handled by `.foot-inner`
  and `.foot-bottom` to enable the new layered layout)

### Notes
- One Open Graph image (1200×630) and a favicon are still pending. These
  should ideally be designed by a graphic designer rather than auto-generated,
  given they are the first signal of quality when the link is shared on
  LinkedIn, WhatsApp, Slack.

---

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
