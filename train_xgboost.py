import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

print("=========================================")
print("  SensoPack XGBoost Model Trainer        ")
print("=========================================")

CSV_PATH = "esf_dataset.csv"

if os.path.exists(CSV_PATH):
    print(f"Loading real dataset from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)
    # Filter for shrimp
    if 'species' in df.columns:
        df = df[df['species'].str.lower() == 'shrimp']
else:
    print(f"Dataset {CSV_PATH} not found. Generating synthetic dataset based on ESF research...")
    # Generate realistic synthetic data based on expected ranges
    n_samples = 1000
    np.random.seed(42)
    
    # ESF dataset was recorded at room temperature (25°C)
    temp = np.full(n_samples, 25.0)
    humidity = np.random.uniform(40, 100, n_samples)
    time_exposed = np.random.uniform(0.5, 72, n_samples)
    
    # Gas and pH naturally rise with temperature and time
    spoilage_factor = (temp * time_exposed) / 500.0
    mq_raw = np.clip(100 + (spoilage_factor * 800) + np.random.normal(0, 50, n_samples), 0, 1023)
    ph_level = np.clip(6.5 + (spoilage_factor * 2.5) + np.random.normal(0, 0.2, n_samples), 5.0, 9.0)
    
    # 0 = Safe, 1 = Caution, 2 = Spoiled.
    # We will sort by spoilage factor and use percentiles to assign classes.
    # E.g. Safe = Bottom 50%, Caution = 50%-75%, Spoiled = Top 25%
    df_temp = pd.DataFrame({'mq_raw': mq_raw, 'ph_level': ph_level, 'spoilage_factor': spoilage_factor})
    threshold_caution = df_temp['spoilage_factor'].quantile(0.50)
    threshold_spoiled = df_temp['spoilage_factor'].quantile(0.75)
    
    status = np.zeros(n_samples, dtype=int)
    status[spoilage_factor > threshold_caution] = 1
    status[spoilage_factor > threshold_spoiled] = 2
    
    df = pd.DataFrame({
        'temp': temp,
        'humidity': humidity,
        'mq_raw': mq_raw,
        'time_exposed_hours': time_exposed,
        'ph_level': ph_level,
        'status': status
    })

# 1. Select Features
X = df[['temp', 'humidity', 'mq_raw', 'time_exposed_hours', 'ph_level']].copy()
y = df['status']

# 2. Feature Engineering
print("Engineering features (degree_hours)...")
X['degree_hours'] = X['temp'] * X['time_exposed_hours']

# 3. Train XGBoost
print("Applying SMOTE for class balancing...")
try:
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    X, y = smote.fit_resample(X, y)
    print("SMOTE applied successfully. New class distribution:")
    print(y.value_counts())
except ImportError:
    print("imbalanced-learn not installed, skipping SMOTE.")

print("Training XGBoost Classifier...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = xgb.XGBClassifier(
    n_estimators=150,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    objective='multi:softprob',
    num_class=3,
    eval_metric='mlogloss',
    num_parallel_tree=1
)

clf.fit(X_train, y_train)

# 4. Evaluate
predictions = clf.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))

# 5. Save Model
model_path = 'shrimp_spoilage_model_xgb.joblib'
joblib.dump(clf, model_path)
print(f"Model saved successfully to {model_path}")
