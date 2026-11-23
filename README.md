# mlops-ml-project — baseline ML reproductible

## Installation

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/macOS : `source .venv/bin/activate`

## Entraînement

```powershell
python scripts/train.py
```

## Évaluation

```powershell
python scripts/evaluate.py
```

## Tests

```powershell
python -m pytest -q
```

## Artefacts (générés dans artifacts/, non versionnés)

- model.joblib : pipeline entraîné (prétraitement + modèle)
- metrics.json : accuracy et f1_macro sur le jeu de test
- confusion_matrix.png : matrice de confusion
- report.json : rapport de classification détaillé