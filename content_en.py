"""English version of the portfolio content (inherits links/emails from content.py)."""
import content as fr

PROFILE = {**fr.PROFILE,
    "cv": "/static/cv-moncef-elmadi-en.pdf",
    "cv_ats": "/static/cv-moncef-elmadi-ats-en.pdf",
    "role": "Engineering student · Data Science & IoT · Data Analyst / BI",
    "tagline": "I turn data into clear insights that support better decisions.",
    "location": "Rabat, Morocco",
    "availability": "Looking for a final-year (PFE) internship in Data Analytics / Business Intelligence — 2027",
    "about": (
        "I am a 5th-year computer engineering student (Data Science and IoT track) at SUP MTI Rabat, "
        "interested in data analysis, Business Intelligence and artificial intelligence. I enjoy preparing "
        "and exploring data, building relevant indicators and designing dashboards that make business "
        "challenges easier to understand. I am looking for a PFE internship in 2027 (Data Analyst / BI)."
    ),
}

STATS = [
    {"value": "2027", "label": "Expected graduation"},
    {"value": "PFE", "label": "Career goal"},
    {"value": "BI", "label": "Data focus"},
]

_sk = [
    ("Business Intelligence", "Building dashboards, visualisations and KPI tracking."),
    ("Data preparation", "Cleaning, preparing and consolidating data files."),
    ("Data", "Querying and manipulating relational data."),
    ("Programming", "Data analysis and processing with the Python ecosystem."),
    ("Data analysis", "Manipulating, cleaning and exploring tabular data."),
    ("AI", "Scikit-learn and TensorFlow: preparing, training and evaluating models."),
    ("Development", "Building simple interfaces for data applications."),
    ("Tools", "Version control and project tracking."),
]
SKILLS = [{**s, "category": c, "description": d} for s, (c, d) in zip(fr.SKILLS, _sk)]

EXPERIENCE = [{
    "company": "Lear Corporation — Technopolis",
    "role": "PFA Intern · Data / IT Asset Management",
    "date": "3 Aug – 3 Sep 2026",
    "description": "Contributed to building a Power BI dashboard to analyse and track IT assets using data from Snipe-IT.",
    "tasks": [
        "Preparation and consolidation of Excel files.",
        "Data cleaning and transformation.",
        "Design of interactive visualisations to make IT asset tracking easier.",
    ],
}]

_pr = [
    ("Experience · Lear Technopolis", "Power BI dashboard for analysing and tracking IT assets from Snipe-IT data.",
     "Make IT inventory information easier to read and monitor.",
     "Excel file consolidation, data cleaning and interactive visualisations.", "Delivered during PFA internship"),
    ("Academic project · Sports analytics & prediction", "Platform analysing Botola Pro performance, with an interactive dashboard and match outcome prediction.",
     "Make sports statistics easier to explore, compare and anticipate.",
     "Interactive statistics dashboard and a Machine Learning model to predict results.", "Project completed"),
    ("Academic project · AI application", "AI-based web application assessing mental well-being, with a personalised score and recommendations.",
     "Offer a simple mental well-being assessment with clear feedback for the user.",
     "Deep Learning model exposed through a REST API, with an interactive dashboard on the front end.", "Project completed"),
    ("Academic project · PFA", "Conversational assistant to query a DEPP PDF report and find information in the document.",
     "Simplify information retrieval in a large institutional document.",
     "PDF content extraction, indexing and semantic search to retrieve relevant passages.", "Project completed"),
]
PROJECTS = [{**p, "type": t, "summary": s, "problem": pb, "approach": a, "status": st}
            for p, (t, s, pb, a, st) in zip(fr.PROJECTS, _pr)]

EDUCATION = [
    {"school": "SUP MTI — Rabat", "degree": "Computer Engineering · Data Science & IoT (5th year)", "date": "2024 – 2027", "detail": "Engineering cycle, expected graduation in 2027."},
    {"school": "SUP MTI — Rabat", "degree": "Preparatory classes", "date": "2022 – 2024", "detail": "Integrated preparatory cycle."},
    {"school": "Lycée Allal El Fassi — Rabat", "degree": "Baccalaureate in Life and Earth Sciences", "date": "2020 – 2021", "detail": ""},
]

CERTIFICATIONS = [
    {"name": "Data Analyst & BI", "issuer": "GoMyCode", "detail": "4 months · Power BI, DAX, Power Query, advanced Excel"},
    {"name": "Python Training", "issuer": "GoMyCode", "detail": "3 months · Python, Pandas, data analysis"},
    {"name": "SQL and Relational Databases 101", "issuer": "IBM", "detail": "November 2026"},
    {"name": "Deep Learning Fundamentals", "issuer": "IBM", "detail": "October 2026"},
    {"name": "Innovative Project Management & Entrepreneurship", "issuer": "SUP MTI", "detail": "40 hours · July 2026"},
]

LANGUAGES = [
    {"name": "Arabic", "level": "Native"},
    {"name": "French", "level": "Good level"},
    {"name": "English", "level": "Good level"},
    {"name": "German", "level": "B1"},
]
