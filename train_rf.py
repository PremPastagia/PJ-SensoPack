import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

print("=========================================")
print("  SensoPack Random Forest Model Trainer   ")
print("=========================================")

CSV_PATH = "esf_dataset.csv"

# Literature-grounded bounds (see PHASE1_LITERATURE.md from the original
# Phase 1 research pass): TVB-N Fresh 0-25 | Caution 25-35 | Spoiled >35
# mg N/100g; pH Fresh 6.5-7.2 | Caution 7.2-7.5 | Spoiled >7.5; ammonia
# headspace (MQ-135-class sensor) Fresh 0-5 | Caution 5-15 | Spoiled >15
# ppm; storage temp -2 to 30C; Arrhenius Ea=118 kJ/mol for chilled/frozen
# shrimp chemical spoilage indices.
EA = 118_000.0       # J/mol
R_GAS = 8.314         # J/mol.K
T_REF_K = 273.15      # 0C reference for the rate multiplier
TVBN_FRESH_MAX = 25.0
TVBN_CAUTION_MAX = 35.0

if os.path.exists(CSV_PATH):
    print(f"Loading real dataset from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)
    # Filter for shrimp
    if 'species' in df.columns:
        df = df[df['species'].str.lower() == 'shrimp']
else:
    print(f"Dataset {CSV_PATH} not found. Generating synthetic dataset from literature-grounded Arrhenius kinetics...")
    n_samples = 4000
    rng = np.random.default_rng(42)

    # Storage temperature: mixture of realistic scenarios, weighted toward
    # the chill band (real cold-chain data is mostly chilled product, not
    # retail-abuse). Matches the literature's -2 to 30C input range.
    band = rng.choice(["chill", "moderate", "abuse"], size=n_samples, p=[0.55, 0.30, 0.15])
    temp = np.empty(n_samples)
    temp[band == "chill"] = rng.uniform(-2, 4, size=(band == "chill").sum())
    temp[band == "moderate"] = rng.uniform(4, 10, size=(band == "moderate").sum())
    temp[band == "abuse"] = rng.uniform(10, 30, size=(band == "abuse").sum())

    humidity = rng.uniform(70, 95, size=n_samples)  # weak/no relationship to spoilage, by design
    time_exposed = rng.uniform(0, 360.0, size=n_samples)  # 0-15 days

    # Arrhenius rate multiplier relative to the 0C reference rate.
    t_k = temp + 273.15
    k_t = np.exp(-EA / (R_GAS * t_k))
    k_ref = np.exp(-EA / (R_GAS * T_REF_K))
    rate_mult = k_t / k_ref

    # Normalizing constant tuned so cut-points land mid-sample-range.
    spoilage_progress = rate_mult * time_exposed / 900.0
    s_clip = np.clip(spoilage_progress, 0, 1.0)

    # TVB-N is the ground-truth spoilage indicator; ammonia and pH are
    # noisy sensor proxies of it (target ~0.75-0.90 pairwise correlation,
    # not near-perfect -- real sensors partially disagree).
    tvbn = np.clip(2.0 + 33.0 * s_clip + rng.normal(0, 4.0, size=n_samples), 0.5, None)
    ph_level = np.clip(6.6 + 0.9 * s_clip + rng.normal(0, 0.20, size=n_samples), 6.0, 8.2)
    ammonia_ppm = np.clip(1.0 + 14.0 * (s_clip ** 1.2) + rng.normal(0, 3.0, size=n_samples), 0.1, None)

    status = np.where(
        tvbn <= TVBN_FRESH_MAX, 0,
        np.where(tvbn <= TVBN_CAUTION_MAX, 1, 2)
    )

    df = pd.DataFrame({
        'temp': temp,
        'humidity': humidity,
        'ammonia_ppm': ammonia_ppm,
        'time_exposed_hours': time_exposed,
        'ph_level': ph_level,
        'status': status
    })

# 1. Select Features
X = df[['temp', 'humidity', 'ammonia_ppm', 'time_exposed_hours', 'ph_level']].copy()
y = df['status']

# 2. Feature Engineering
print("Engineering features (degree_hours)...")
X['degree_hours'] = X['temp'] * X['time_exposed_hours']

# 3. Train Random Forest
print("Applying SMOTE for class balancing...")
try:
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    X, y = smote.fit_resample(X, y)
    print("SMOTE applied successfully. New class distribution:")
    print(y.value_counts())
except ImportError:
    print("imbalanced-learn not installed, skipping SMOTE.")

print("Training Random Forest Classifier...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 15 estimators keeps the m2cgen-exported pure-Python tree code small,
# since each tree gets fully unrolled into if/else branches.
clf = RandomForestClassifier(
    n_estimators=15,
    max_depth=8,
    random_state=42
)

clf.fit(X_train, y_train)

# 4. Evaluate
predictions = clf.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))

# 5. Save Model
model_path = 'shrimp_spoilage_model_rf.joblib'
joblib.dump(clf, model_path)
print(f"Model saved successfully to {model_path}")
