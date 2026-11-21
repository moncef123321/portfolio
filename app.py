from flask import Flask, Response, jsonify, render_template, request, url_for

import content
import content_en
import i18n
import ml

app = Flask(__name__)

_EN = {"Longueur du sépale": "Sepal length", "Largeur du sépale": "Sepal width",
       "Longueur du pétale": "Petal length", "Largeur du pétale": "Petal width"}


def _tr(items):
    out = []
    for it in items:
        it = dict(it)
        for k, v in _EN.items():
            it["label"] = it["label"].replace(k, v)
        out.append(it)
    return out


def page(lang):
    data = {k: v for k, v in vars(content_en if lang == "en" else content).items() if k.isupper()}
    sliders, imps = ml.sliders(), ml.importances()
    if lang == "en":
        sliders, imps = _tr(sliders), _tr(imps)
    return render_template("index.html", **data, T=i18n.T[lang], lang=lang,
                           sliders=sliders, accuracy=ml.ACCURACY,
                           n_train=ml.N_TRAIN, n_test=ml.N_TEST, importances=imps)


@app.get("/")
def home():
    return page("fr")


@app.get("/en")
def home_en():
    return page("en")


@app.get("/health")
def health():
    return "ok"


@app.get("/robots.txt")
def robots():
    return Response(f"User-agent: *\nAllow: /\nSitemap: {url_for('sitemap', _external=True)}\n", mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap():
    urls = [url_for("home", _external=True), url_for("home_en", _external=True)]
    body = "".join(f"<url><loc>{u}</loc></url>" for u in urls)
    return Response('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + body + "</urlset>", mimetype="application/xml")


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


@app.after_request
def headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    return resp


@app.post("/api/predict")
def predict():
    data = request.get_json(silent=True) or {}
    try:
        values = [float(v) for v in data.get("values")]
        if len(values) != len(ml.FEATURES):
            raise ValueError
    except (TypeError, ValueError):
        return jsonify(error="Envoie 4 nombres dans « values »."), 400
    return jsonify(ml.predict(values))


if __name__ == "__main__":
    app.run(debug=True)
