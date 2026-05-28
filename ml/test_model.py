"""Smoke test for the trained model (run from repo root: python ml/test_model.py)."""
import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "medical_insurance_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

sample = [[30, 0, 25.0, 0, 1, 0]]
prediction = model.predict(sample)[0]
print(f"Sample prediction: ${prediction:,.2f}")
