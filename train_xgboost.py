import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib

def generate_synthetic_data(n_samples=4000):
    np.random.seed(42)
    
    # Randomly distribute temperature and time
    scenario = np.random.choice(["cold", "ambient", "hot"], size=n_samples, p=[0.4, 0.4, 0.2])
    temp = np.where(
        scenario == "cold", np.random.uniform(0, 4, n_samples),
        np.where(scenario == "ambient", np.random.uniform(20, 28, n_samples),
                 np.random.uniform(28, 42, n_samples))
    )
    time_exposed = np.random.uniform(0.5, 200, n_samples)
    humidity = np.random.uniform(40, 100, n_samples)
    
    # Feature Engineering explicitly defined in training
    temp_effect = np.clip(temp - 4.0, 0, None)
    degree_hours = temp_effect * time_exposed

    # Generate physical sensor spikes (Ammonia and pH)
    # Most times, sensors follow the degree_hours curve. But we add noise and independent spikes
    # to simulate "Stealth Spoilage" (high temp/time, low gas yet) or "Hot Car" (extreme gas).
    base_gas = np.clip(1.0 + (degree_hours / 100.0) * 10.0, 0, 30.0)
    base_ph = np.clip(6.5 + (degree_hours / 150.0) * 1.5, 6.0, 8.5)
    
    # Add random bacterial spike noise (some packages rot differently)
    ammonia_ppm = np.clip(base_gas + np.random.normal(0, 3.0, n_samples), 0, 30)
    ph_level = np.clip(base_ph + np.random.normal(0, 0.2, n_samples), 6.0, 8.5)
    
    # GROUND TRUTH STATUS GENERATION (Overrides)
    # 0 = SAFE, 1 = CAUTION, 2 = UNSAFE
    status = np.zeros(n_samples, dtype=int)
    
    for i in range(n_samples):
        # 1. Biological Overrides (Physical sensors dictate reality)
        if ammonia_ppm[i] >= 12.0 or ph_level[i] >= 7.4 or degree_hours[i] >= 300:
            status[i] = 2 # UNSAFE
        # 2. Caution thresholds
        elif ammonia_ppm[i] >= 5.0 or ph_level[i] >= 7.1 or degree_hours[i] >= 100:
            status[i] = 1 # CAUTION
        # 3. Otherwise Safe
        else:
            status[i] = 0 # SAFE

    df = pd.DataFrame({
        'temp': temp,
        'humidity': humidity,
        'ammonia_ppm': ammonia_ppm,
        'time_exposed_hours': time_exposed,
        'ph_level': ph_level,
        'degree_hours': degree_hours,
        'status': status
    })
    
    return df

if __name__ == "__main__":
    print("Generating physically-grounded synthetic data...")
    df = generate_synthetic_data(5000)
    
    print("\nClass distribution in synthetic data:")
    print(df['status'].value_counts())
    
    # 1. Select Features exactly as the API expects
    X = df[['temp', 'humidity', 'ammonia_ppm', 'time_exposed_hours', 'ph_level', 'degree_hours']].copy()
    y = df['status']

    # 2. Train XGBoost
    print("\nTraining XGBoost Classifier...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Use RandomForestClassifier for seamless m2cgen pure-python multi-class transpilation
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(
        n_estimators=150,
        max_depth=5,
        class_weight="balanced",
        random_state=42
    )

    clf.fit(X_train, y_train)

    # 3. Evaluate
    print("Evaluating Model...")
    y_pred = clf.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["SAFE", "CAUTION", "UNSAFE"]))

    # 4. Feature Importance
    importance = clf.feature_importances_
    features = X.columns
    print("\nFeature Importances:")
    for f, imp in sorted(zip(features, importance), key=lambda x: x[1], reverse=True):
        print(f"{f}: {imp:.4f}")

    # 5. Export
    joblib.dump(clf, "shrimp_spoilage_model_xgb.joblib")
    print("\nModel saved to shrimp_spoilage_model_xgb.joblib")
