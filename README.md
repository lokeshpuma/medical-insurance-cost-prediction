# Medical Insurance Cost Predictor

A machine learning project that estimates annual medical insurance charges from demographic and health inputs. The **live predictor** runs as a static site on GitHub Pages; training artifacts and notebooks live under `ml/`.

## Live demo

After deployment, open:

**https://lokeshpuma.github.io/medical-insurance-cost-prediction/**

Enable GitHub Pages once: **Settings → Pages → Build and deployment → GitHub Actions**.

## Features

- **Linear regression model** trained on the [insurance dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Static web UI** (HTML/CSS/JS) — no server required for predictions
- **Automated deploy** via GitHub Actions on every push to `main`

## Repository layout

| Path | Description |
|------|-------------|
| `index.html` | Predictor page (GitHub Pages entry) |
| `assets/` | Styles and client-side prediction logic |
| `ml/insurance.csv` | Training data |
| `ml/medical_insurance.ipynb` | EDA and model training |
| `ml/medical_insurance_model.pkl` | Serialized scikit-learn model |
| `ml/test_model.py` | Quick model smoke test |

## Local development

### Run the website locally

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

### Retrain or verify the model

```bash
pip install -r ml/requirements.txt
python ml/test_model.py
```

Use `ml/medical_insurance.ipynb` for full exploratory analysis and training.

## Usage

1. Open the live site (or local server).
2. Enter **age**, **sex**, **BMI**, **children**, **smoker**, and **region**.
3. Click **Predict insurance cost** to see the estimated annual charge.

## About

Predictions in the browser use the same linear regression coefficients as the Python model in `ml/medical_insurance_model.pkl`. Categorical fields use the same encodings as the notebook (`sex`, `smoker`, `region`).
