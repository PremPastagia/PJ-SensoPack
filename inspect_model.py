import joblib
model = joblib.load('shrimp_spoilage_model.joblib')
print(model.feature_names_in_)
