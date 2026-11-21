"""Contenu du portfolio de Moncef Elmadi — à personnaliser ici."""

PROFILE = {
    "name": "Moncef Elmadi",
    "initials": "ME",
    "role": "Étudiant ingénieur · Data Science & IoT · Data Analyst / BI",
    "tagline": "Je transforme les données en informations claires pour aider à prendre de meilleures décisions.",
    "location": "Rabat, Maroc",
    "availability": "À la recherche d'un stage PFE en Data Analyst / Business Intelligence — 2027",
    "about": (
        "Étudiant en 5ème année du cycle ingénieur en informatique (spécialité Data Science et IoT) "
        "à SUP MTI Rabat, je m'intéresse à l'analyse de données, à la Business Intelligence et à "
        "l'intelligence artificielle. J'aime préparer et explorer les données, construire des "
        "indicateurs pertinents et concevoir des tableaux de bord qui facilitent la compréhension "
        "des enjeux métier. Je recherche un stage PFE en 2027 (Data Analyst / BI)."
    ),
    "linkedin": "https://www.linkedin.com/in/moncef-elmadi-data",
    "github": "https://github.com/moncef123321",
    "email": "moncef.elmadi@gmail.com",
    "formspree": "",  # Optionnel : https://formspree.io/f/XXXXXXXX
    "cv": "/static/cv-moncef-elmadi.pdf",
    "photo": "/static/photo.jpg",
    "cv_ats": "/static/cv-moncef-elmadi-ats.pdf",
}

STATS = [
    {"value": "2027", "label": "Diplôme prévu"},
    {"value": "PFE", "label": "Objectif professionnel"},
    {"value": "BI", "label": "Orientation Data"},
]

SKILLS = [
    {"name": "Power BI", "level": 85, "category": "Business Intelligence", "description": "Création de tableaux de bord, visualisation et suivi d'indicateurs."},
    {"name": "Excel", "level": 85, "category": "Data preparation", "description": "Préparation, nettoyage et consolidation de fichiers de données."},
    {"name": "SQL", "level": 70, "category": "Data", "description": "Requêtes et manipulation de données relationnelles."},
    {"name": "Python", "level": 75, "category": "Programming", "description": "Analyse et traitement de données avec l'écosystème Python."},
    {"name": "Pandas", "level": 70, "category": "Data analysis", "description": "Manipulation, nettoyage et exploration de données tabulaires."},
    {"name": "Machine Learning", "level": 55, "category": "AI", "description": "Scikit-learn et TensorFlow : préparation, entraînement et évaluation de modèles."},
    {"name": "Streamlit", "level": 65, "category": "Development", "description": "Développement d'interfaces simples pour des applications data."},
    {"name": "Git & GitHub", "level": 65, "category": "Tools", "description": "Gestion de versions et suivi de projets."},
]

EXPERIENCE = [
    {
        "company": "Lear Corporation — Technopolis",
        "role": "Stagiaire PFA · Data / IT Asset Management",
        "date": "03 août - 03 septembre 2026",
        "description": "Contribution à la création d'un dashboard Power BI pour l'analyse et le suivi des actifs informatiques à partir de données issues de Snipe-IT.",
        "tasks": [
            "Préparation et consolidation de fichiers Excel.",
            "Nettoyage et transformation des données.",
            "Conception de visualisations interactives pour faciliter le suivi des actifs IT.",
        ],
    }
]

PROJECTS = [
    {
        "number": "01",
        "title": "IT Asset Management Dashboard",
        "type": "Expérience · Lear Technopolis",
        "summary": "Tableau de bord Power BI dédié à l'analyse et au suivi des actifs informatiques à partir de données Snipe-IT.",
        "problem": "Faciliter la lecture et le suivi des informations relatives au parc informatique.",
        "approach": "Préparation et consolidation des fichiers Excel, nettoyage des données, création de visualisations interactives.",
        "tools": ["Power BI", "Excel", "Snipe-IT", "Data Cleaning"],
        "status": "Réalisé en stage PFA",
        "featured": True,
    },
    {
        "number": "02",
        "title": "Botola PRO AI",
        "type": "Projet académique · Analyse & prédiction sportive",
        "summary": "Plateforme d'analyse des performances de la Botola Pro avec dashboard interactif et prédiction des résultats.",
        "problem": "Rendre les statistiques sportives plus faciles à explorer, comparer et anticiper.",
        "approach": "Dashboard interactif de visualisation des statistiques et modèle de Machine Learning pour la prédiction des résultats.",
        "tools": ["Python", "Streamlit", "Pandas", "Plotly", "Scikit-learn"],
        "status": "Projet développé",
        "featured": True,
    },
    {
        "number": "03",
        "title": "Mental Wellness Predictor",
        "type": "Projet académique · Application IA",
        "summary": "Application web d'évaluation du bien-être mental basée sur l'IA, avec score personnalisé et recommandations.",
        "problem": "Proposer une évaluation simple du bien-être mental avec un retour clair pour l'utilisateur.",
        "approach": "Modèle de Deep Learning exposé via une API REST, et tableau de bord interactif côté interface.",
        "tools": ["Angular", "FastAPI", "Python", "TensorFlow", "Chart.js"],
        "status": "Projet développé",
        "featured": True,
    },
    {
        "number": "04",
        "title": "Chatbot documentaire DEPP",
        "type": "Projet académique · PFA",
        "summary": "Assistant conversationnel permettant d'interroger un rapport PDF de la DEPP et de retrouver des informations dans le document.",
        "problem": "Simplifier la recherche d'informations dans un document institutionnel volumineux.",
        "approach": "Extraction du contenu PDF, indexation et recherche sémantique pour retrouver les passages pertinents.",
        "tools": ["Python", "Streamlit", "LangChain", "FAISS", "PyMuPDF"],
        "status": "Projet développé",
        "featured": False,
    },
]

EDUCATION = [
    {"school": "SUP MTI — Rabat", "degree": "Génie Informatique · Data Science et IoT (5e année)", "date": "2024 – 2027", "detail": "Cycle ingénieur, diplôme prévu en 2027."},
    {"school": "SUP MTI — Rabat", "degree": "Classes préparatoires", "date": "2022 – 2024", "detail": "Cycle préparatoire intégré."},
    {"school": "Lycée Allal El Fassi — Rabat", "degree": "Baccalauréat en Sciences de la Vie et de la Terre", "date": "2020 – 2021", "detail": ""},
]

CERTIFICATIONS = [
    {"name": "Data Analyst & BI", "issuer": "GoMyCode", "detail": "4 mois · Power BI, DAX, Power Query, Excel avancé"},
    {"name": "Formation Python", "issuer": "GoMyCode", "detail": "3 mois · Python, Pandas, analyse de données"},
    {"name": "SQL and Relational Databases 101", "issuer": "IBM", "detail": "Novembre 2026"},
    {"name": "Deep Learning Fundamentals", "issuer": "IBM", "detail": "Octobre 2026"},
    {"name": "Management de projets innovants et entrepreneuriat", "issuer": "SUP MTI", "detail": "40 heures · Juillet 2026"},
]

LANGUAGES = [
    {"name": "Arabe", "level": "Langue maternelle"},
    {"name": "Français", "level": "Bon niveau"},
    {"name": "Anglais", "level": "Bon niveau"},
    {"name": "Allemand", "level": "B1"},
]
