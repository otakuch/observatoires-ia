// ═══════════════════════════════════════════════════════════
// SHARED COMPONENTS · observatoire[s]·ia
// ═══════════════════════════════════════════════════════════

// Embedded data (avoids CORS issues with file:// protocol)
window.OBSERVATOIRES_DATA = [
  {"id":"transitions-ia","nom":"transitions-ia.ch","org":{"fr":"Naully Nicolas · indépendant","en":"Naully Nicolas · independent"},"country":"CH","type":"independant","domains":["emploi","formation"],"freq":{"fr":"Mensuelle","en":"Monthly"},"desc":{"fr":"Observatoire indépendant des transitions emploi/IA en Suisse romande. Couvre formations SEFRI, exposition par métier, signaux faibles.","en":"Independent observatory of AI/employment transitions in French-speaking Switzerland. Covers SEFRI training, exposure by job, weak signals."},"last":"2026-04","url":"https://transitions-ia.ch"},
  {"id":"sefri","nom":"SEFRI","org":{"fr":"Confédération suisse · Formation, recherche, innovation","en":"Swiss Confederation · Education, research, innovation"},"country":"CH","type":"public","domains":["formation"],"freq":{"fr":"Annuelle","en":"Yearly"},"desc":{"fr":"Pilotage des programmes de formation continue et certifications professionnelles, dont les filières IA émergentes.","en":"Steering of continuing education programs and professional certifications, including emerging AI tracks."},"last":"2026-03","url":"https://www.sbfi.admin.ch"},
  {"id":"ofs","nom":"OFS","org":{"fr":"Office fédéral de la statistique","en":"Federal Statistical Office"},"country":"CH","type":"public","domains":["statistiques","emploi"],"freq":{"fr":"Trimestrielle","en":"Quarterly"},"desc":{"fr":"Statistiques officielles du marché du travail suisse : population active, professions, salaires, postes vacants.","en":"Official statistics on the Swiss labour market: active population, occupations, wages, vacancies."},"last":"2026-04","url":"https://www.bfs.admin.ch"},
  {"id":"epfl-aic","nom":"EPFL AI Center","org":{"fr":"École polytechnique fédérale de Lausanne","en":"Swiss Federal Institute of Technology Lausanne"},"country":"CH","type":"academique","domains":["gouvernance","formation"],"freq":{"fr":"Variable","en":"Variable"},"desc":{"fr":"Centre interdisciplinaire IA. Publications sur l'impact sociétal, l'éducation et la gouvernance des systèmes d'IA en Suisse.","en":"Interdisciplinary AI center. Publications on societal impact, education and governance of AI systems in Switzerland."},"last":"2026-03","url":"https://ai.epfl.ch"},
  {"id":"digital-ch","nom":"Digital Switzerland","org":{"fr":"Initiative cross-secteur","en":"Cross-sector initiative"},"country":"CH","type":"branche","domains":["emploi","formation"],"freq":{"fr":"Annuelle","en":"Yearly"},"desc":{"fr":"Coalition d'entreprises et institutions sur la transformation numérique. Études récurrentes sur les compétences IA en entreprise.","en":"Coalition of companies and institutions on digital transformation. Recurring studies on AI skills in business."},"last":"2026-02","url":"https://digitalswitzerland.com"},
  {"id":"skbf","nom":"CSRE / SKBF","org":{"fr":"Centre suisse de coordination pour la recherche en éducation","en":"Swiss Coordination Centre for Research in Education"},"country":"CH","type":"academique","domains":["formation"],"freq":{"fr":"Quadriennale","en":"Quadrennial"},"desc":{"fr":"Rapport quadriennal sur l'éducation en Suisse, intégrant les enjeux IA et compétences du XXIe siècle.","en":"Quadrennial report on education in Switzerland, integrating AI and 21st-century skills."},"last":"2025-12","url":"https://www.skbf-csre.ch"},
  {"id":"laboria","nom":"LaborIA","org":{"fr":"Inria × Ministère du Travail","en":"Inria × French Ministry of Labour"},"country":"FR","type":"public","domains":["emploi","gouvernance"],"freq":{"fr":"Variable","en":"Variable"},"desc":{"fr":"Laboratoire de recherche-action public sur les effets de l'IA au travail. Études de terrain en entreprises pilotes.","en":"Public research-action lab on AI effects in the workplace. Field studies in pilot companies."},"last":"2026-03","url":"https://www.laboria.ai"},
  {"id":"france-strategie","nom":"France Stratégie","org":{"fr":"Premier ministre · Conseil national de la productivité","en":"Prime Minister · National Productivity Council"},"country":"FR","type":"public","domains":["emploi","gouvernance"],"freq":{"fr":"Variable","en":"Variable"},"desc":{"fr":"Études prospectives sur les métiers, la productivité et l'IA. Rapports publics téléchargeables avec données ouvertes.","en":"Forward-looking studies on jobs, productivity and AI. Public reports with open data."},"last":"2026-04","url":"https://www.strategie.gouv.fr"},
  {"id":"dares","nom":"DARES","org":{"fr":"Ministère du Travail · Direction de l'animation, de la recherche, des études et des statistiques","en":"French Ministry of Labour · Statistics directorate"},"country":"FR","type":"public","domains":["statistiques","emploi"],"freq":{"fr":"Mensuelle","en":"Monthly"},"desc":{"fr":"Production statistique officielle sur l'emploi en France. Premières estimations chiffrées de l'exposition à l'IA générative.","en":"Official employment statistics in France. First quantitative estimates of generative AI exposure."},"last":"2026-02","url":"https://dares.travail-emploi.gouv.fr"},
  {"id":"france-travail","nom":"France Travail","org":{"fr":"Observatoire des métiers (ex-Pôle Emploi)","en":"Jobs Observatory (former Pôle Emploi)"},"country":"FR","type":"public","domains":["emploi"],"freq":{"fr":"Mensuelle","en":"Monthly"},"desc":{"fr":"Cartographie ROME des métiers, tensions de recrutement, baromètre BMO. Données ouvertes mensuelles.","en":"ROME jobs taxonomy, recruitment tensions, BMO survey. Monthly open data."},"last":"2026-04","url":"https://www.francetravail.org"},
  {"id":"apec","nom":"APEC","org":{"fr":"Association pour l'emploi des cadres","en":"Executive Employment Association"},"country":"FR","type":"branche","domains":["emploi"],"freq":{"fr":"Trimestrielle","en":"Quarterly"},"desc":{"fr":"Études trimestrielles sur le marché des cadres, intégrant l'évolution des compétences IA recherchées par les recruteurs.","en":"Quarterly studies on the executive market, including the evolution of AI skills sought by recruiters."},"last":"2026-03","url":"https://corporate.apec.fr"},
  {"id":"cnil","nom":"CNIL","org":{"fr":"Commission nationale de l'informatique et des libertés","en":"French data protection authority"},"country":"FR","type":"public","domains":["gouvernance"],"freq":{"fr":"Variable","en":"Variable"},"desc":{"fr":"Volet IA & travail : recommandations sur l'usage des outils d'IA dans le management, la sélection et le suivi des salariés.","en":"AI & workplace: recommendations on AI tools for management, hiring and monitoring of employees."},"last":"2026-01","url":"https://www.cnil.fr"},
  {"id":"france-num","nom":"France Num","org":{"fr":"Direction générale des entreprises","en":"Directorate General for Enterprise"},"country":"FR","type":"public","domains":["formation","emploi"],"freq":{"fr":"Annuelle","en":"Yearly"},"desc":{"fr":"Observatoire de la transformation numérique des TPE/PME françaises, dont l'adoption d'outils IA et la montée en compétences.","en":"Observatory of digital transformation of French SMEs, including AI tool adoption and upskilling."},"last":"2026-03","url":"https://www.francenum.gouv.fr"},
  {"id":"cge","nom":"CGE","org":{"fr":"Conférence des Grandes Écoles · Observatoire","en":"Conference of Grandes Écoles · Observatory"},"country":"FR","type":"academique","domains":["formation"],"freq":{"fr":"Annuelle","en":"Yearly"},"desc":{"fr":"Enquête annuelle insertion des diplômés. Premier signal sur l'impact IA sur les entrées en poste des juniors.","en":"Annual graduate insertion survey. First signal on AI impact on junior job entries."},"last":"2025-11","url":"https://www.cge.asso.fr"}
];

window.VEILLE_DATA = [{"date":"2026-04-15","source":"Stanford HAI","country":"INT","title":{"fr":"AI Index Report 2026·neuvième édition","en":"AI Index Report 2026·ninth edition"},"excerpt":{"fr":"Plus de 400 pages de données vetées. Adoption générative à 53% en 3 ans (plus rapide que PC ou Internet). 88% des organisations utilisent désormais l'IA. Écart de perception : 73% des experts US sont positifs sur l'impact emploi, contre 23% du grand public.","en":"Over 400 pages of vetted data. Generative AI adoption at 53% within 3 years (faster than PC or internet). 88% of organisations now use AI. Perception gap: 73% of US experts are positive about employment impact, vs only 23% of the general public."},"url":"https://hai.stanford.edu/ai-index/2026-ai-index-report","ai_type":"generative"},{"date":"2026-04-10","source":"Coface · OEM","country":"FR","title":{"fr":"Emplois, compétences, valeur : ce que l'IA est en train de bouleverser","en":"Jobs, skills, value: what AI is disrupting"},"excerpt":{"fr":"Étude conjointe Coface / Observatoire des Emplois Menacés et Émergents. 16,3% des emplois français exposés à 2-5 ans (≈ 5 millions). 3,8% déjà fragilisés par l'IA générative actuelle. Méthodologie tâche par tâche sur 923 professions. Métiers qualifiés en première ligne, contrairement aux vagues précédentes.","en":"Joint Coface / OEM study. 16.3% of French jobs exposed within 2-5 years (≈ 5 million). 3.8% already weakened by current generative AI. Task-by-task methodology on 923 occupations. Qualified jobs on the front line, unlike previous waves."},"url":"https://www.coface.fr/actualites-economie-conseils/emplois-competences-valeur-ce-que-l-ia-est-en-train-de-bouleverser","ai_type":"agentic"},{"date":"2026-04-08","source":"France Stratégie · DARES","country":"FR","title":{"fr":"Les Métiers en 2030·révision post-IA générative","en":"Jobs in 2030·post-generative AI revision"},"excerpt":{"fr":"Mise à jour du rapport prospectif coréalisé par France Stratégie et la DARES. 800 000 postes à pourvoir par an d'ici 2030, dont 90% liés aux départs en retraite. 115 000 postes d'ingénieurs informatiques nets supplémentaires (+26%). Métiers de la santé en première ligne des recrutements.","en":"Update to the prospective report co-authored by France Stratégie and DARES. 800,000 positions to be filled per year by 2030, 90% linked to retirements. 115,000 additional net IT engineering positions (+26%). Healthcare occupations on the front line of recruitment."},"url":"https://www.strategie-plan.gouv.fr/publications/metiers-2030","ai_type":"automation_broad"},{"date":"2026-04-15","source":"APEC","country":"FR","title":{"fr":"Perspectives 2026 du recrutement cadre·IT en redémarrage","en":"2026 executive recruitment outlook·IT picking up"},"excerpt":{"fr":"305 800 recrutements cadres prévus en 2026 (+4%). Cadres IT : 61 160 recrutements (+4%). Reprise relative·encore loin du sommet 2023 (330 400). Trois moteurs explicites : transformation numérique, cybersécurité, montée en puissance de l'IA. Profils juniors peu favorisés (+1%).","en":"305,800 executive recruitments expected in 2026 (+4%). IT executives: 61,160 hirings (+4%). Relative pickup·still below the 2023 peak (330,400). Three explicit drivers: digital transformation, cybersecurity, AI ramp-up. Junior profiles disadvantaged (+1%)."},"url":"https://corporate.apec.fr/home/nos-etudes/toutes-nos-etudes/les-cadres-et-l'ia.html","ai_type":"generative"},{"date":"2026-04-02","source":"Swiss AI Center · HES-SO","country":"CH","title":{"fr":"Adoption de l'IA dans les PME suisses·bilan 2026","en":"AI adoption in Swiss SMEs·2026 review"},"excerpt":{"fr":"Centre dédié à l'accélération de l'adoption IA par les PME. PME = 3 millions d'emplois dans 590 000 entreprises (60% population active). Obstacles documentés : manque de connaissances, accès aux compétences locales, sécurité des données. AI Days 23-25 mars 2026 à Martigny et Fribourg.","en":"Centre dedicated to accelerating AI adoption by SMEs. SMEs = 3 million jobs in 590,000 companies (60% of the active population). Documented barriers: lack of knowledge, access to local skills, data security. AI Days 23-25 March 2026 in Martigny and Fribourg."},"url":"https://www.hes-so.ch/swiss-ai-center","ai_type":"generative"},{"date":"2026-04-01","source":"OFS · Statistique de l'emploi","country":"CH","title":{"fr":"STATEM Q1 2026·places vacantes et prévisions d'emploi","en":"STATEM Q1 2026·vacancies and employment forecasts"},"excerpt":{"fr":"Statistique trimestrielle officielle. Recul des places vacantes (-16,4% sur un an au T1 2025). Indicateur de prévision d'emploi à 1,042 (vs 1,05 l'an précédent). Chômage BIT 4,7% (vs 4,3%). Source de référence pour les indicateurs Suisse de l'observatoire.","en":"Official quarterly statistics. Vacancies declining (-16.4% year-on-year in Q1 2025). Employment forecast indicator at 1.042 (vs 1.05 the previous year). ILO unemployment 4.7% (vs 4.3%). Reference source for the observatory's Swiss indicators."},"url":"https://www.bfs.admin.ch/bfs/fr/home/statistiques/industrie-services/entreprises-emplois/statistique-emploi/places-vacantes.html","ai_type":"automation_broad"},{"date":"2026-04-12","source":"PwC","country":"INT","title":{"fr":"AI Jobs Barometer 2025·France 1ère en Europe","en":"AI Jobs Barometer 2025·France 1st in Europe"},"excerpt":{"fr":"Analyse de près d'un milliard d'offres d'emploi sur six continents. France : 166 000 offres IA en 2024, devant l'Allemagne (147 000) et le Royaume-Uni (125 000). Offres IA × 10 en Suisse entre 2018 et 2024 (2 000 → 20 000). Prime salariale IA : jusqu'à +56% par rapport aux postes équivalents.","en":"Analysis of nearly one billion job postings across six continents. France: 166,000 AI postings in 2024, ahead of Germany (147,000) and UK (125,000). AI postings × 10 in Switzerland between 2018 and 2024 (2,000 → 20,000). AI salary premium: up to +56% versus equivalent positions."},"url":"https://www.pwc.fr/fr/publications/series/ai-jobs-barometer.html","ai_type":"generative"},{"date":"2026-03-25","source":"DARES · LaborIA","country":"FR","title":{"fr":"Comment l'IA transforme les pratiques de recrutement","en":"How AI transforms recruitment practices"},"excerpt":{"fr":"Travaux du LaborIA (Ministère du Travail × Inria) sur l'usage des algorithmes dans le recrutement. Biais documentés, équité dans les recommandations d'emploi, hommes vs femmes. Régulation et encadrement des solutions IA en RH. Études de cas sur 250 décideurs RH.","en":"LaborIA (Ministry of Labour × Inria) work on algorithm use in recruitment. Documented biases, fairness in job recommendations, men vs women. Regulation and oversight of HR AI solutions. Case studies on 250 HR decision-makers."},"url":"https://dares.travail-emploi.gouv.fr/evenement/comment-lintelligence-artificielle-transforme-les-pratiques-de-recrutement","ai_type":"generative"}];


const I18N = {
  fr: {
    "nav.suisse": "Suisse",
    "nav.france": "France",
    "nav.comparer": "Comparer",
    "nav.memos": "Le Dispatch·iA",
    "nav.veille": "Veille",
    "nav.about": "À propos",
    "nav.contact": "Contact",
    "foot.rights": "Données sous licences sources",
    "foot.method": "Méthodologie",
    "foot.data": "Données ouvertes",
    "card.last": "MAJ",
    "card.visit": "Source ↗",
    "filter.country": "Pays",
    "filter.type": "Type",
    "filter.domain": "Domaine",
    "filter.all": "Tous",
    "type.public": "Public",
    "type.academique": "Académique",
    "type.branche": "Branche",
    "type.independant": "Indépendant",
    "domain.emploi": "Emploi",
    "domain.formation": "Formation",
    "domain.gouvernance": "Gouvernance",
    "domain.statistiques": "Statistiques",
    "empty": "Aucun observatoire ne correspond à ces filtres."
  },
  en: {
    "nav.suisse": "Switzerland",
    "nav.france": "France",
    "nav.comparer": "Compare",
    "nav.memos": "The Dispatch·iA",
    "nav.veille": "Field Report",
    "nav.about": "About",
    "nav.contact": "Contact",
    "foot.rights": "Data under source licenses",
    "foot.method": "Methodology",
    "foot.data": "Open data",
    "card.last": "Updated",
    "card.visit": "Source ↗",
    "filter.country": "Country",
    "filter.type": "Type",
    "filter.domain": "Domain",
    "filter.all": "All",
    "type.public": "Public",
    "type.academique": "Academic",
    "type.branche": "Industry",
    "type.independant": "Independent",
    "domain.emploi": "Employment",
    "domain.formation": "Training",
    "domain.gouvernance": "Governance",
    "domain.statistiques": "Statistics",
    "empty": "No observatory matches these filters."
  }
};

// Page-level translations are merged in by each page before init()
window.PAGE_I18N = window.PAGE_I18N || { fr: {}, en: {} };

let CURRENT_LANG = localStorage.getItem("obs-lang") || "fr";

function t(key) {
  const merged = {
    ...I18N[CURRENT_LANG],
    ...(window.PAGE_I18N[CURRENT_LANG] || {})
  };
  return merged[key] || key;
}

function applyI18n() {
  document.documentElement.lang = CURRENT_LANG;
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    const html = el.hasAttribute("data-i18n-html");
    const value = t(key);
    if (html) el.innerHTML = value;
    else el.textContent = value;
  });
  document.querySelectorAll(".lang-toggle span").forEach((s) => {
    s.classList.toggle("active", s.getAttribute("data-lang") === CURRENT_LANG);
  });
  // Re-render dynamic sections if the page has a hook
  if (typeof window.onLangChange === "function") window.onLangChange(CURRENT_LANG);
}

function setupLangToggle() {
  const toggle = document.getElementById("langToggle");
  if (!toggle) return;
  toggle.addEventListener("click", () => {
    CURRENT_LANG = CURRENT_LANG === "fr" ? "en" : "fr";
    localStorage.setItem("obs-lang", CURRENT_LANG);
    applyI18n();
  });
}

function setupMobileMenu() {
  const menuBtn = document.getElementById("menuBtn");
  const closeBtn = document.getElementById("closeMenu");
  const mobileMenu = document.getElementById("mobileMenu");
  if (!menuBtn || !mobileMenu) return;
  menuBtn.addEventListener("click", () => mobileMenu.classList.add("open"));
  if (closeBtn) closeBtn.addEventListener("click", () => mobileMenu.classList.remove("open"));
  mobileMenu.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => mobileMenu.classList.remove("open"));
  });
}

function setupReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add("visible");
    });
  }, { threshold: 0.1 });
  document.querySelectorAll(".manifesto-text, .section-title, .stat, .kpi, .card, .field-card, .country-card, .dash-title")
    .forEach((el) => {
      el.classList.add("reveal");
      observer.observe(el);
    });
}

// Detect if we're in a subfolder (observatoires/ or briefings/) and build relative root
function rootPath() {
  // Pages in /observatoires/ or /briefings/ have one extra path segment
  const path = window.location.pathname;
  return (path.includes("/observatoires/") || path.includes("/briefings/")) ? "../" : "";
}

// Render shared nav into a placeholder
function renderNav(currentPage) {
  const nav = document.getElementById("siteNav");
  if (!nav) return;
  const root = rootPath();
  const link = (href, key, current) => {
    const cls = current === currentPage ? ' class="current"' : "";
    return `<a href="${root}${href}"${cls} data-i18n="nav.${key}">${t("nav." + key)}</a>`;
  };
  nav.innerHTML = `
    <div class="nav-inner">
      <a href="${root}index.html" class="logo">
        observatoire<span class="bracket">[s]</span><span class="dot">·</span>ia
      </a>
      <div class="nav-links">
        ${link("observatoires/suisse.html", "suisse", "suisse")}
        ${link("observatoires/france.html", "france", "france")}
        ${link("observatoires/comparer.html", "comparer", "comparer")}
        ${link("briefings.html", "memos", "briefings")}
        ${link("veille.html", "veille", "veille")}
        ${link("a-propos.html", "about", "about")}
        ${link("contact.html", "contact", "contact")}
      </div>
      <div class="nav-actions">
        <button class="lang-toggle" id="langToggle" aria-label="Switch language">
          <span class="active" data-lang="fr">FR</span>
          <span data-lang="en">EN</span>
        </button>
        <button class="menu-btn" id="menuBtn" aria-label="Open menu"><span></span></button>
      </div>
    </div>
  `;
  // Mobile menu
  const mob = document.getElementById("mobileMenu");
  if (mob) {
    mob.innerHTML = `
      <button class="close-btn" id="closeMenu">×</button>
      <a href="${root}observatoires/suisse.html" data-i18n="nav.suisse">${t("nav.suisse")}</a>
      <a href="${root}observatoires/france.html" data-i18n="nav.france">${t("nav.france")}</a>
      <a href="${root}observatoires/comparer.html" data-i18n="nav.comparer">${t("nav.comparer")}</a>
      <a href="${root}briefings.html" data-i18n="nav.memos">${t("nav.memos")}</a>
      <a href="${root}veille.html" data-i18n="nav.veille">${t("nav.veille")}</a>
      <a href="${root}a-propos.html" data-i18n="nav.about">${t("nav.about")}</a>
      <a href="${root}contact.html" data-i18n="nav.contact">${t("nav.contact")}</a>
    `;
  }
}

function renderFooter() {
  const f = document.getElementById("siteFooter");
  if (!f) return;
  const root = rootPath();
  f.innerHTML = `
    <div class="foot-inner">
      <span>© 2026 observatoire[s]·ia · <span data-i18n="foot.rights">${t("foot.rights")}</span></span>
      <div class="foot-links">
        <a href="${root}methodologie.html" data-i18n="foot.method">${t("foot.method")}</a>
        <a href="${root}donnees.html" data-i18n="foot.data">${t("foot.data")}</a>
      </div>
      <span class="foot-version">v0.2 · build 2026.04</span>
    </div>
  `;
}

// Bootstrap
function initSite(currentPage) {
  renderNav(currentPage);
  renderFooter();
  setupLangToggle();
  setupMobileMenu();
  applyI18n();
  setupReveal();
}

window.initSite = initSite;
window.t = t;
window.applyI18n = applyI18n;
Object.defineProperty(window, "CURRENT_LANG", {
  get() { return CURRENT_LANG; }
});
