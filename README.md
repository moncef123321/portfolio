# Portfolio — Moncef El Madi

Flask · bilingue FR/EN · démo ML (Random Forest) · thème clair/sombre.

## Lancer en local (Windows)
Double-clique sur `lancer.bat` (crée l'environnement la 1re fois, puis ouvre le site).
Manuellement : `python -m venv .venv` → `.venv\Scripts\activate` → `pip install -r requirements.txt` → `python app.py`
- Français : http://127.0.0.1:5000  ·  Anglais : http://127.0.0.1:5000/en

## Modifier le contenu
- Français : `content.py`  ·  Anglais : `content_en.py`  ·  Textes de l'interface : `i18n.py`
- CV FR : `static/cv-moncef-elmadi.pdf` (pro) et `-ats.pdf` ; CV EN : `static/cv-moncef-elmadi-en.pdf` et `-ats-en.pdf` ; photo : `static/photo.jpg`
- Lien GitHub d'un projet : ajoute `"github": "https://..."` dans le projet (dans `content.py`).
- Formulaire de contact : renseigne `"formspree"` dans `PROFILE` (https://formspree.io).

## Déployer (Render, gratuit)
1. Pousse le dossier sur GitHub (sans `.venv`).
2. Render → New → Blueprint (utilise `render.yaml`) ou Web Service : Build `pip install -r requirements.txt`, Start `gunicorn app:app`.
3. Optionnel : UptimeRobot sur `/health` pour éviter la mise en veille.
