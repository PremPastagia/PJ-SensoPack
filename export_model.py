import joblib
import m2cgen as m2c

print("Loading model...")
clf = joblib.load('shrimp_spoilage_model_xgb.joblib')
clf.base_score = 0.5

print("Generating Python code...")
code = m2c.export_to_python(clf)

# We want predict_proba so we can threshold at 0.40.
# m2cgen generates a 'score' function. For XGBClassifier, the score is usually the log-odds (margin).
# We can convert log-odds to probability using the sigmoid function: 1 / (1 + exp(-score)).

# Wait, m2cgen for XGBClassifier returns an array if multi-class, but for binary classification, it usually returns a single score (the log odds of class 1).
# We can wrap it in a helper function.
wrapper_code = """
import math

""" + code + """

def predict_proba(input_features):
    # m2cgen score function returns raw margins for each class
    scores = score(input_features)
    
    # Softmax conversion
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    sum_exp = sum(exp_scores)
    
    probs = [e / sum_exp for e in exp_scores]
    return probs
"""

with open('api/xgb_model.py', 'w') as f:
    f.write(wrapper_code)

print("Exported pure Python model to api/xgb_model.py!")
