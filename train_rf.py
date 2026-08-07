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

if os.path.exists(CSV_PATH):
    print(f"Loading real dataset from {CSV_PATH}...")
    df = pd.read_csv(CSV_PATH)
    # Filter for shrimp
    if 'species' in df.columns:
        df = df[df['species'].str.lower() == 'shrimp']
else:
    print(f"Dataset {CSV_PATH} not found. Generating synthetic dataset based on ESF research...")
    # Generate realistic synthetic data based on expected ranges
    n_samples = 4000
    np.random.seed(42)

    # Storage temperature varies across real-world scenarios: cold-chain,
    # ambient room temp (matching the ESF dataset's ~25C baseline), and
    # heat-abuse conditions. A constant temp collapses to zero variance and
    # makes the gas/pH sensor features redundant proxies of time alone.
    scenario = np.random.choice(["cold", "ambient", "hot"], size=n_samples, p=[0.35, 0.4, 0.25])
    temp = np.where(
        scenario == "cold", np.random.uniform(0, 4, n_samples),
        np.where(scenario == "ambient", np.random.uniform(20, 28, n_samples),
                 np.random.uniform(28, 42, n_samples))
    )
    humidity = np.random.uniform(40, 100, n_samples)
    time_exposed = np.random.uniform(0.5, 200, n_samples)

    # Microbial spoilage only accumulates meaningfully above ~4C (cold-chain
    # storage halts it), and accumulates faster with heat.
    temp_effect = np.clip(temp - 4.0, 0, None)
    degree_hours = temp_effect * time_exposed

    # Real spoilage also varies batch-to-batch (initial microbial load,
    # packaging integrity, humidity) well beyond what temp*time alone
    # explains -- degree_hours is computable noise-free from raw temp/time
    # inputs, so unless batch variance is substantial, the model shortcuts
    # through degree_hours and never learns to trust the gas/pH sensors,
    # which are what the hardware actually measures in the field. This
    # "true" spoilage index is what the sensors actually measure.
    batch_factor = np.clip(np.random.normal(1.0, 0.7, n_samples), 0.15, 3.0)
    true_spoilage = degree_hours * batch_factor

    # Gas and pH sensors are direct (lightly-noisy) readings of the true
    # spoilage index -- more reliable in practice than reconstructing
    # elapsed temp*time history from a QR timestamp. true_spoilage has a
    # long right tail (heat-abuse + high batch_factor), so map it through a
    # saturating (Michaelis-Menten) curve rather than a linear scale -- a
    # linear map clips most samples to the sensor ceiling, collapsing them
    # to one indistinguishable value and starving the model of any graded
    # gas/pH signal near the actual decision boundaries.
    K = 1000.0  # half-saturation point, tuned below the Caution threshold
    saturation = true_spoilage / (true_spoilage + K)
    mq_raw = np.clip(90 + (saturation * 900) + np.random.normal(0, 20, n_samples), 0, 1023)
    ph_level = np.clip(6.3 + (saturation * 2.6) + np.random.normal(0, 0.08, n_samples), 5.0, 9.0)

    # 0 = Safe, 1 = Caution, 2 = Spoiled, thresholded on the true spoilage
    # index (not a sensor reading). Safe = bottom 50%, Caution = 50-75%,
    # Spoiled = top 25%.
    threshold_caution = np.quantile(true_spoilage, 0.50)
    threshold_spoiled = np.quantile(true_spoilage, 0.75)

    status = np.zeros(n_samples, dtype=int)
    status[true_spoilage > threshold_caution] = 1
    status[true_spoilage > threshold_spoiled] = 2

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
