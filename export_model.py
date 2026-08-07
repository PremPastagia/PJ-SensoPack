import joblib
import m2cgen as m2c

print("Loading model...")
clf = joblib.load('shrimp_spoilage_model_xgb.joblib')
clf.base_score = 0.5

print("Generating Python code...")
code = m2c.export_to_python(clf)

# We want predict_proba so we can threshold at 0.40.
# m2cgen's export_to_python() for a multi:softprob XGBClassifier already
# applies softmax internally and returns normalized class probabilities
# directly from score() -- it does NOT return raw margins needing another
# softmax. Applying softmax a second time flattens confident predictions
# toward a uniform distribution (e.g. 99.8% -> 57.6%), silently corrupting
# every confidence score without ever raising an error.
wrapper_code = """
import math

""" + code + """

def predict_proba(input_features):
    return score(input_features)
"""

with open('api/xgb_model.py', 'w') as f:
    f.write(wrapper_code)

print("Exported pure Python model to api/xgb_model.py!")
