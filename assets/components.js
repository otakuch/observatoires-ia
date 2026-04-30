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

window.VEILLE_DATA = [{"date":"2026-04-15","source":"NBER · Yin, Vu, Persico (w35110)","country":"INT","title":{"fr":"Quelle (in)stabilité des scores d'exposition LLM ? Evidence d'une réplication multi-modèles","en":"How (un)Stable Are LLM Occupational Exposure Scores? Evidence from Multi-Model Replication"},"excerpt":{"fr":"Démonstration que les mesures d'exposition à l'IA basées sur les LLM auto-évaluatifs sont hautement fragiles. Trois modèles frontière appliquant la même rubrique sur les mêmes tâches produisent une divergence d'un facteur 3,6 sur l'exposition moyenne, avec un accord descendant à 57%. Cette instabilité altère les conclusions empiriques en aval : les coefficients en panel diff-in-diff varient d'un facteur 2,4 selon l'annotateur, et les estimations county-level passent d'un effet négatif significatif à un effet positif non significatif selon le modèle utilisé. Conclusion radicale : traiter les LLM en évolution comme des instruments statiques est risqué.","en":"Demonstration that LLM-based self-assessed AI exposure measures are highly fragile. Three frontier models applying the same rubric on identical tasks produce a 3.6-fold divergence in mean exposure, with agreement as low as 57%. This instability alters downstream empirical conclusions: difference-in-differences coefficients vary 2.4-fold across annotators, and county-level estimates flip from significant negative to insignificant positive depending on the model. Radical conclusion: treating evolving LLMs as static instruments is risky."},"url":"https://www.nber.org/papers/w35110","ai_type":"generative"},{"date":"2026-02-19","source":"Yale Budget Lab · Gimbel, Kendall, Kulsakdinun","country":"INT","title":{"fr":"L'exposition à l'IA sur le marché du travail : que sait-on vraiment ?","en":"Labor Market AI Exposure: What Do We Know?"},"excerpt":{"fr":"Étude systématique comparant 7 métriques d'exposition à l'IA (Eloundou OpenAI, Felten AIOE, Webb, Eisfeldt, Tomlinson Microsoft Copilot, etc.) sur 867 métiers SOC 2018. Conclusion en trois points : les métriques s'accordent largement, mais elles divergent davantage sur les métiers fortement exposés. Le désaccord porte sur l'ampleur de l'exposition, pas sur le fait qu'un métier soit exposé. L'exposition n'indique pas qu'un métier sera automatisé, seulement qu'il pourrait être impacté. Exemples canoniques : les plombiers ont une variance de 0,03 (consensus total sur faible exposition), les programmeurs informatiques ont 0,48 (désaccord majeur sur l'ampleur). Données ouvertes téléchargeables.","en":"Systematic study comparing 7 AI exposure metrics (Eloundou OpenAI, Felten AIOE, Webb, Eisfeldt, Tomlinson Microsoft Copilot, etc.) across 867 SOC 2018 occupations. Three key takeaways: metrics broadly agree, but disagree more on highly exposed occupations. Disagreement is about magnitude, not whether an occupation is exposed. Exposure does not indicate which jobs AI will automate, only where AI could have an impact. Canonical examples: plumbers have variance 0.03 (full consensus on low exposure), computer programmers have 0.48 (major disagreement on magnitude). Open data downloadable."},"url":"https://budgetlab.yale.edu/research/labor-market-ai-exposure-what-do-we-know","ai_type":"generative"},{"date":"2026-04-25","source":"Financial Times · John Burn-Murdoch","country":"INT","title":{"fr":"Ce que rate le récit du « jobpocalypse » IA","en":"What the AI 'jobpocalypse' narrative misses"},"excerpt":{"fr":"Burn-Murdoch démontre par les chiffres historiques (BLS, James Bessen) que l'effet productivité-emploi dépend du rapport demande/offre dans chaque secteur, pas de la seule capacité technique de l'IA. Les logiciels et les services pro ont vu productivité et emploi croître ensemble (demande latente), tandis que la manufacture a vu l'emploi reculer (demande satisfaite). La radiologie et la santé restent protégées par la régulation. Critique radicale des prédictions basées uniquement sur les task-based exposure scores.","en":"Burn-Murdoch shows through historical BLS data and James Bessen's research that the productivity-employment relationship depends on demand/supply dynamics within each sector, not on AI's technical capability alone. Software and professional services saw both productivity and employment rise (pent-up demand), while manufacturing saw employment fall (satiated demand). Radiology and healthcare remain protected by regulation. Radical critique of predictions based solely on task-based exposure scores."},"url":"https://www.ft.com/content/8d3b02a3-c929-46a1-b79e-dbcdb1d10e15","ai_type":"generative"},{"date":"2026-04-23","source":"Focaldata · Financial Times Workforce AI Tracker · Wave 1","country":"INT","title":{"fr":"Two-Tier Transformation : comment l'IA change le travail au Royaume-Uni et aux États-Unis","en":"Two-Tier Transformation: How AI is Changing Work in the UK and US"},"excerpt":{"fr":"Première vague d'un tracker mensuel UK+US (n=4 119, février-mars 2026). 65% des actifs ont utilisé l'IA au moins une fois, mais moins de 1/5 quotidiennement. Distribution L-shape : grande majorité d'usagers rares + petite minorité de power users. Productivité IA marché : +3,5% (Tech +7,8%, Finance +5,1%). Effet formation +37 pts d'usage quotidien, mais seulement 14% ont reçu une formation formelle. Managers UK pessimistes (-25% prévoient réduction) vs US optimistes (+28% prévoient hausse). Scénarios ABC : Augmentation, Bifurcation (probable), Crash.","en":"First wave of monthly UK+US tracker (n=4,119, February-March 2026). 65% of workers have used AI at least once, but fewer than 1/5 daily. L-shaped distribution: large majority of rare users + small minority of power users. Market AI productivity: +3.5% (Tech +7.8%, Finance +5.1%). Training effect +37 pts daily usage, but only 14% have received formal training. UK managers pessimistic (-25% expect reduction) vs US optimistic (+28% expect increase). ABC scenarios: Augmentation, Bifurcation (likely), Crash."},"url":"https://focaldata.com","ai_type":"generative"},{"date":"2026-02-26","source":"Financial Times · Burn-Murdoch & O'Connor","country":"INT","title":{"fr":"Sait-on vraiment quels métiers sont les plus exposés à l'IA ?","en":"Do we really know which jobs are most at risk from AI?"},"excerpt":{"fr":"Critique méthodologique majeure : les sept mesures d'exposition par tâches (Eloundou OpenAI, Anthropic Economic Index, AIOE, Yale Budget Lab, etc.) s'accordent sur les métiers peu exposés mais divergent fortement sur les plus exposés. Au-delà de la capacité technique, trois facteurs pèsent : autonomie du travailleur, régulation institutionnelle (radiologie, thérapie), et effets de second ordre sur la demande. Citation centrale de David Autor (2003) : les technologies remplacent les exécutants de specs, complémentent les définisseurs.","en":"Major methodological critique: the seven task-based exposure measures (Eloundou OpenAI, Anthropic Economic Index, AIOE, Yale Budget Lab, etc.) agree on low-exposure jobs but diverge sharply on the most exposed. Beyond technical capability, three factors matter: worker autonomy, institutional regulation (radiology, therapy), and second-order demand effects. Central citation from David Autor (2003): technologies replace those who execute specs, complement those who define them."},"url":"https://www.ft.com/content/f55c4eba-6e10-4283-8eae-e9f475048b37","ai_type":"generative"},{"date":"2026-04-15","source":"British Progress · Pedro Serôdio","country":"INT","title":{"fr":"L'IA et le marché du travail britannique : l'état des preuves","en":"AI and the UK labour market: the evidence so far"},"excerpt":{"fr":"Rapport synthétisant les données disponibles sur l'impact de l'IA sur l'emploi au Royaume-Uni. Conclusion : peu de signes d'effets agrégés massifs, malgré 54% des PME britanniques utilisant l'IA selon BCC. Les prédictions Goldman Sachs (+7% PIB mondial) et McKinsey (12 millions de transitions) reposent sur ce que l'IA pourrait faire si toutes les organisations l'adoptaient pleinement. La réalité observée est plus étroite et plus collaborative. Divergence frappante entre exposition prédite (forte chez les professionnels et managers) et usage réel (en retard).","en":"Report synthesizing available data on AI's impact on UK employment. Conclusion: few signs of massive aggregate effects, despite 54% of UK SMEs using AI per BCC. Goldman Sachs (+7% world GDP) and McKinsey (12 million transitions) predictions rest on what AI could do if all organizations adopted it fully. Observed reality is narrower and more collaborative. Striking divergence between predicted exposure (high for professionals and managers) and actual usage (lagging)."},"url":"https://britishprogress.org/reports/ai-and-the-uk-labour-market-the-evidence-so-far","ai_type":"generative"},{"date":"2026-04-23","source":"Angestellte Schweiz · DemoSCOPE","country":"CH","title":{"fr":"Insécurité de l'emploi perçue et responsabilités · enquête nationale","en":"Perceived job insecurity and responsibilities · national survey"},"excerpt":{"fr":"Enquête représentative auprès de 1 028 actifs des trois régions linguistiques (23-30 mars 2026). 75% se sentent en sécurité, mais 24% perçoivent une dégradation sur 12 mois. L'IA est citée comme cause individuelle #1 d'insécurité (catégorie technologique 22%). Introduction d'outils IA déclarée dans 17% des environnements de travail, avec un écart frappant : 9% dans les TPE de moins de 10 salariés contre 24% dans les entreprises de 250+. La formation continue reste la mesure jugée la plus efficace (M=3.27/4).","en":"Representative survey of 1,028 active workers across the three language regions (23-30 March 2026). 75% feel secure, but 24% perceive a deterioration over 12 months. AI is cited as the #1 individual cause of insecurity (technology category 22%). AI tool introduction reported in 17% of work environments, with a striking gap: 9% in SMEs under 10 employees vs 24% in companies of 250+. Continuing education remains the measure deemed most effective (M=3.27/4)."},"url":"https://www.angestellte.ch","ai_type":"generative"},{"date":"2026-04-15","source":"Stanford HAI","country":"INT","title":{"fr":"AI Index Report 2026·neuvième édition","en":"AI Index Report 2026·ninth edition"},"excerpt":{"fr":"Plus de 400 pages de données vetées. Adoption générative à 53% en 3 ans (plus rapide que PC ou Internet). 88% des organisations utilisent désormais l'IA. Écart de perception : 73% des experts US sont positifs sur l'impact emploi, contre 23% du grand public.","en":"Over 400 pages of vetted data. Generative AI adoption at 53% within 3 years (faster than PC or internet). 88% of organisations now use AI. Perception gap: 73% of US experts are positive about employment impact, vs only 23% of the general public."},"url":"https://hai.stanford.edu/ai-index/2026-ai-index-report","ai_type":"generative"},{"date":"2026-04-10","source":"Coface · OEM","country":"FR","title":{"fr":"Emplois, compétences, valeur : ce que l'IA est en train de bouleverser","en":"Jobs, skills, value: what AI is disrupting"},"excerpt":{"fr":"Étude conjointe Coface / Observatoire des Emplois Menacés et Émergents. 16,3% des emplois français exposés à 2-5 ans (≈ 5 millions). 3,8% déjà fragilisés par l'IA générative actuelle. Méthodologie tâche par tâche sur 923 professions. Métiers qualifiés en première ligne, contrairement aux vagues précédentes.","en":"Joint Coface / OEM study. 16.3% of French jobs exposed within 2-5 years (≈ 5 million). 3.8% already weakened by current generative AI. Task-by-task methodology on 923 occupations. Qualified jobs on the front line, unlike previous waves."},"url":"https://www.coface.fr/actualites-economie-conseils/emplois-competences-valeur-ce-que-l-ia-est-en-train-de-bouleverser","ai_type":"agentic"},{"date":"2026-04-08","source":"France Stratégie · DARES","country":"FR","title":{"fr":"Les Métiers en 2030·révision post-IA générative","en":"Jobs in 2030·post-generative AI revision"},"excerpt":{"fr":"Mise à jour du rapport prospectif coréalisé par France Stratégie et la DARES. 800 000 postes à pourvoir par an d'ici 2030, dont 90% liés aux départs en retraite. 115 000 postes d'ingénieurs informatiques nets supplémentaires (+26%). Métiers de la santé en première ligne des recrutements.","en":"Update to the prospective report co-authored by France Stratégie and DARES. 800,000 positions to be filled per year by 2030, 90% linked to retirements. 115,000 additional net IT engineering positions (+26%). Healthcare occupations on the front line of recruitment."},"url":"https://www.strategie-plan.gouv.fr/publications/metiers-2030","ai_type":"automation_broad"},{"date":"2026-04-15","source":"APEC","country":"FR","title":{"fr":"Perspectives 2026 du recrutement cadre·IT en redémarrage","en":"2026 executive recruitment outlook·IT picking up"},"excerpt":{"fr":"305 800 recrutements cadres prévus en 2026 (+4%). Cadres IT : 61 160 recrutements (+4%). Reprise relative·encore loin du sommet 2023 (330 400). Trois moteurs explicites : transformation numérique, cybersécurité, montée en puissance de l'IA. Profils juniors peu favorisés (+1%).","en":"305,800 executive recruitments expected in 2026 (+4%). IT executives: 61,160 hirings (+4%). Relative pickup·still below the 2023 peak (330,400). Three explicit drivers: digital transformation, cybersecurity, AI ramp-up. Junior profiles disadvantaged (+1%)."},"url":"https://corporate.apec.fr/home/nos-etudes/toutes-nos-etudes/les-cadres-et-l'ia.html","ai_type":"generative"},{"date":"2026-04-02","source":"Swiss AI Center · HES-SO","country":"CH","title":{"fr":"Adoption de l'IA dans les PME suisses·bilan 2026","en":"AI adoption in Swiss SMEs·2026 review"},"excerpt":{"fr":"Centre dédié à l'accélération de l'adoption IA par les PME. PME = 3 millions d'emplois dans 590 000 entreprises (60% population active). Obstacles documentés : manque de connaissances, accès aux compétences locales, sécurité des données. AI Days 23-25 mars 2026 à Martigny et Fribourg.","en":"Centre dedicated to accelerating AI adoption by SMEs. SMEs = 3 million jobs in 590,000 companies (60% of the active population). Documented barriers: lack of knowledge, access to local skills, data security. AI Days 23-25 March 2026 in Martigny and Fribourg."},"url":"https://www.hes-so.ch/swiss-ai-center","ai_type":"generative"},{"date":"2026-04-01","source":"OFS · Statistique de l'emploi","country":"CH","title":{"fr":"STATEM Q1 2026·places vacantes et prévisions d'emploi","en":"STATEM Q1 2026·vacancies and employment forecasts"},"excerpt":{"fr":"Statistique trimestrielle officielle. Recul des places vacantes (-16,4% sur un an au T1 2025). Indicateur de prévision d'emploi à 1,042 (vs 1,05 l'an précédent). Chômage BIT 4,7% (vs 4,3%). Source de référence pour les indicateurs Suisse de l'observatoire.","en":"Official quarterly statistics. Vacancies declining (-16.4% year-on-year in Q1 2025). Employment forecast indicator at 1.042 (vs 1.05 the previous year). ILO unemployment 4.7% (vs 4.3%). Reference source for the observatory's Swiss indicators."},"url":"https://www.bfs.admin.ch/bfs/fr/home/statistiques/industrie-services/entreprises-emplois/statistique-emploi/places-vacantes.html","ai_type":"automation_broad"},{"date":"2026-04-12","source":"PwC","country":"INT","title":{"fr":"AI Jobs Barometer 2025·France 1ère en Europe","en":"AI Jobs Barometer 2025·France 1st in Europe"},"excerpt":{"fr":"Analyse de près d'un milliard d'offres d'emploi sur six continents. France : 166 000 offres IA en 2024, devant l'Allemagne (147 000) et le Royaume-Uni (125 000). Offres IA × 10 en Suisse entre 2018 et 2024 (2 000 → 20 000). Prime salariale IA : jusqu'à +56% par rapport aux postes équivalents.","en":"Analysis of nearly one billion job postings across six continents. France: 166,000 AI postings in 2024, ahead of Germany (147,000) and UK (125,000). AI postings × 10 in Switzerland between 2018 and 2024 (2,000 → 20,000). AI salary premium: up to +56% versus equivalent positions."},"url":"https://www.pwc.fr/fr/publications/series/ai-jobs-barometer.html","ai_type":"generative"},{"date":"2026-03-25","source":"DARES · LaborIA","country":"FR","title":{"fr":"Comment l'IA transforme les pratiques de recrutement","en":"How AI transforms recruitment practices"},"excerpt":{"fr":"Travaux du LaborIA (Ministère du Travail × Inria) sur l'usage des algorithmes dans le recrutement. Biais documentés, équité dans les recommandations d'emploi, hommes vs femmes. Régulation et encadrement des solutions IA en RH. Études de cas sur 250 décideurs RH.","en":"LaborIA (Ministry of Labour × Inria) work on algorithm use in recruitment. Documented biases, fairness in job recommendations, men vs women. Regulation and oversight of HR AI solutions. Case studies on 250 HR decision-makers."},"url":"https://dares.travail-emploi.gouv.fr/evenement/comment-lintelligence-artificielle-transforme-les-pratiques-de-recrutement","ai_type":"generative"}];


const I18N = {
  fr: {
    "nav.home": "Retour à l'accueil",
    "nav.accueil": "Accueil",
    "nav.suisse": "Suisse",
    "nav.france": "France",
    "nav.comparer": "Comparer",
    "nav.memos": "Le Dispatch·iA",
    "nav.veille": "Veille",
    "nav.method": "Méthodologie",
    "nav.about": "À propos",
    "nav.partner": "Partenariats",
    "nav.contact": "Contact",
    "foot.rights": "Données sous licences sources",
    "foot.method": "Méthodologie",
    "foot.data": "Données ouvertes",
    "foot.tagline": "Comprendre l'impact des IA sur le travail · Suisse & France",
    "foot.explore": "Explorer",
    "foot.about": "À propos",
    "foot.lastupdate": "Dernière mise à jour",
    "foot.license": "Données ouvertes · CC BY 4.0",
    "foot.by": "Conçu et opéré par",
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
    "nav.home": "Back to home",
    "nav.accueil": "Home",
    "nav.suisse": "Switzerland",
    "nav.france": "France",
    "nav.comparer": "Compare",
    "nav.memos": "The Dispatch·iA",
    "nav.veille": "Field Report",
    "nav.method": "Methodology",
    "nav.about": "About",
    "nav.partner": "Partnerships",
    "nav.contact": "Contact",
    "foot.rights": "Data under source licenses",
    "foot.method": "Methodology",
    "foot.data": "Open data",
    "foot.tagline": "Understanding AI's impact on work · Switzerland & France",
    "foot.explore": "Explore",
    "foot.about": "About",
    "foot.lastupdate": "Last update",
    "foot.license": "Open data · CC BY 4.0",
    "foot.by": "Designed and operated by",
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
      <a href="${root}index.html" class="logo" title="${t("nav.home")}" aria-label="${t("nav.home")}">
        observatoire<span class="bracket">[s]</span><span class="dot">·</span>ia
      </a>
      <div class="nav-links">
        ${link("index.html", "accueil", "home")}
        ${link("observatoires/suisse.html", "suisse", "suisse")}
        ${link("observatoires/france.html", "france", "france")}
        ${link("observatoires/comparer.html", "comparer", "comparer")}
        ${link("briefings.html", "memos", "briefings")}
        ${link("veille.html", "veille", "veille")}
        ${link("methodologie.html", "method", "methodologie")}
        ${link("a-propos.html", "about", "about")}
        ${link("partenariats.html", "partner", "partenariats")}
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
      <a href="${root}index.html" data-i18n="nav.accueil">${t("nav.accueil")}</a>
      <a href="${root}observatoires/suisse.html" data-i18n="nav.suisse">${t("nav.suisse")}</a>
      <a href="${root}observatoires/france.html" data-i18n="nav.france">${t("nav.france")}</a>
      <a href="${root}observatoires/comparer.html" data-i18n="nav.comparer">${t("nav.comparer")}</a>
      <a href="${root}briefings.html" data-i18n="nav.memos">${t("nav.memos")}</a>
      <a href="${root}veille.html" data-i18n="nav.veille">${t("nav.veille")}</a>
      <a href="${root}methodologie.html" data-i18n="nav.method">${t("nav.method")}</a>
      <a href="${root}a-propos.html" data-i18n="nav.about">${t("nav.about")}</a>
      <a href="${root}partenariats.html" data-i18n="nav.partner">${t("nav.partner")}</a>
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
      <div class="foot-col foot-col-brand">
        <div class="foot-brand">observatoire<span class="bracket">[s]</span><span class="dot">·</span>ia</div>
        <div class="foot-tagline" data-i18n="foot.tagline">${t("foot.tagline")}</div>
      </div>
      <div class="foot-col foot-col-links">
        <div class="foot-col-label mono" data-i18n="foot.explore">${t("foot.explore")}</div>
        <a href="${root}observatoires/suisse.html" data-i18n="nav.suisse">${t("nav.suisse")}</a>
        <a href="${root}observatoires/france.html" data-i18n="nav.france">${t("nav.france")}</a>
        <a href="${root}observatoires/comparer.html" data-i18n="nav.comparer">${t("nav.comparer")}</a>
        <a href="${root}briefings.html" data-i18n="nav.memos">${t("nav.memos")}</a>
      </div>
      <div class="foot-col foot-col-links">
        <div class="foot-col-label mono" data-i18n="foot.about">${t("foot.about")}</div>
        <a href="${root}methodologie.html" data-i18n="foot.method">${t("foot.method")}</a>
        <a href="${root}veille.html" data-i18n="nav.veille">${t("nav.veille")}</a>
        <a href="${root}partenariats.html" data-i18n="nav.partner">${t("nav.partner")}</a>
        <a href="${root}contact.html" data-i18n="nav.contact">${t("nav.contact")}</a>
      </div>
      <div class="foot-col foot-col-meta">
        <div class="foot-update mono">
          <span data-i18n="foot.lastupdate">${t("foot.lastupdate")}</span>
          <strong>29 avril 2026</strong>
        </div>
        <div class="foot-license mono" data-i18n="foot.license">${t("foot.license")}</div>
        <div class="foot-version mono">v0.2.5 · build 2026.04.29</div>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 observatoire<span class="bracket">[s]</span><span class="dot">·</span>ia · <span data-i18n="foot.rights">${t("foot.rights")}</span></span>
      <span class="foot-author">
        <span data-i18n="foot.by">${t("foot.by")}</span>
        <a href="https://naullynicolas.ch" target="_blank" rel="noopener">Naully Nicolas</a>
      </span>
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
