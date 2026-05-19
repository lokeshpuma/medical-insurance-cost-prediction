import pickle
with open('medical_insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)
print(model)
print(getattr(model, "feature_names_in_", "No feature names"))
