"""Mini modèle de machine learning exécuté en direct sur le site (dataset Iris, scikit-learn)."""
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

_iris = load_iris(as_frame=True)
FEATURES = [
    ("sepal length (cm)", "Longueur du sépale (cm)"),
    ("sepal width (cm)", "Largeur du sépale (cm)"),
    ("petal length (cm)", "Longueur du pétale (cm)"),
    ("petal width (cm)", "Largeur du pétale (cm)"),
]
LABELS = {"setosa": "Iris setosa", "versicolor": "Iris versicolor", "virginica": "Iris virginica"}
_COLS = [f[0] for f in FEATURES]
_X, _y = _iris.data[_COLS], _iris.target
_Xtr, _Xte, _ytr, _yte = train_test_split(_X, _y, test_size=0.25, random_state=42, stratify=_y)
_model = RandomForestClassifier(n_estimators=200, random_state=42).fit(_Xtr, _ytr)

ACCURACY = round(accuracy_score(_yte, _model.predict(_Xte)) * 100, 1)
N_TRAIN, N_TEST = len(_Xtr), len(_Xte)


def sliders():
    """Min / max / moyenne de chaque variable, pour construire les curseurs."""
    out = []
    for i, (col, label) in enumerate(FEATURES):
        s = _X[col]
        out.append({"id": f"f{i}", "label": label, "min": round(float(s.min()), 1),
                    "max": round(float(s.max()), 1), "value": round(float(s.mean()), 1)})
    return out


def predict(values):
    row = pd.DataFrame([values], columns=_COLS)
    proba = _model.predict_proba(row)[0]
    names = [LABELS[n] for n in _iris.target_names]
    return {"best": names[int(proba.argmax())],
            "classes": [{"label": n, "p": round(float(p) * 100, 1)} for n, p in zip(names, proba)]}


def importances():
    imp = sorted(zip([f[1] for f in FEATURES], _model.feature_importances_), key=lambda x: -x[1])
    return [{"label": l, "p": round(float(v) * 100, 1)} for l, v in imp]
