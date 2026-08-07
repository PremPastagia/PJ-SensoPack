import joblib
import m2cgen as m2c

print("Loading model...")
clf = joblib.load('shrimp_spoilage_model_rf.joblib')

print("Generating Python code...")
code = m2c.export_to_python(clf)

# m2cgen's export_to_python() for a RandomForestClassifier already sums
# each tree's per-class probability vector and divides by n_estimators --
# score() returns the exact same normalized [p_safe, p_caution, p_unsafe]
# vector as clf.predict_proba() (verified empirically against the trained
# model, not assumed). No further transform is needed; predict_proba is
# just a thin pass-through, kept for API naming clarity.
wrapper_code = """
import math

""" + code + """

def predict_proba(input_features):
    return score(input_features)
"""

with open('api/rf_model.py', 'w') as f:
    f.write(wrapper_code)

print("Exported pure Python model to api/rf_model.py!")
