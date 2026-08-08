"""
SensoPack — Shrimp Spoilage Prediction: Synthetic Data + ML Pipeline
Run top-to-bottom in a single Google Colab cell (or `python3 sensopack_colab.py` locally).

Literature grounding (see PHASE1_LITERATURE.md in this folder for full sourcing):
- TVB-N (mg N/100g):     Fresh 0-25 | Caution 25-35 | Spoiled >35
- pH:                    Fresh 6.5-7.2 | Caution 7.2-7.5 | Spoiled >7.5
- Ammonia headspace(ppm):Fresh 0-5   | Caution 5-15  | Spoiled >15   (MQ-137-class MOS sensor, enclosed pack — recalibrate against real hardware)
- Storage temp (C):      -2 to 30 (chill to retail-abuse), feeds Arrhenius rate
- Storage time (hrs):    0-360 (0-15 days)
- Humidity (%RH):        70-95, secondary/confounding covariate (weak spoilage signal by design)

Arrhenius: k(T) = A * exp(-Ea / (R*T)), Ea = 118 kJ/mol (chilled/frozen shrimp chemical indices,
literature range 118-156 kJ/mol), R = 8.314 J/mol.K, T in Kelvin.
"""

import os

import numpy as np
import pandas as pd
import matplotlib

if not os.environ.get("COLAB_RELEASE_TAG"):
    matplotlib.use("Agg")  # non-interactive backend for local/headless runs; Colab renders inline

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

RNG_SEED = 42
N_SAMPLES = 1500

EA = 118_000.0       # J/mol
R_GAS = 8.314         # J/mol.K
T_REF_K = 273.15      # 0 C reference for the rate multiplier

TVBN_FRESH_MAX = 25.0
TVBN_CAUTION_MAX = 35.0

rng = np.random.default_rng(RNG_SEED)


# ---------------------------------------------------------------------------
# PHASE 2.1 — Synthetic data generator (Arrhenius-kinetics driven)
# ---------------------------------------------------------------------------

def sample_temperature(n):
    """Mixture of realistic storage scenarios, weighted toward the chill band
    (real cold-chain data is mostly chilled product, not retail-abuse)."""
    band = rng.choice(["chill", "moderate", "abuse"], size=n, p=[0.55, 0.30, 0.15])
    temp = np.empty(n)
    temp[band == "chill"] = rng.uniform(-2, 4, size=(band == "chill").sum())
    temp[band == "moderate"] = rng.uniform(4, 10, size=(band == "moderate").sum())
    temp[band == "abuse"] = rng.uniform(10, 30, size=(band == "abuse").sum())
    return temp, band


def sample_storage_time(temperature_c, band):
    """Storage duration, sampled independently of temperature band.

    NOTE: an earlier version capped time inversely with temperature band (short cap for
    'abuse' samples) to avoid physically-odd combinations like 28C for 300 hours. That
    confounded band with time in a way that reversed the sign of the time<->spoilage
    correlation (abuse-band samples saturate spoilage almost instantly via the Arrhenius
    rate multiplier regardless of their short time cap, while chill-band samples got long
    time caps but tiny rate multipliers - so raw elapsed time ended up NEGATIVELY correlated
    with spoilage_status when marginalized over band). Sampling time independently of band
    lets the Arrhenius rate x time interaction alone determine spoilage progress, which is
    physically correct and reproduces the expected positive time<->spoilage correlation.
    High-temp + long-time combinations aren't wrong here - they just saturate S at 1.0
    (fully spoiled), which is the correct behavior, not an artifact to avoid.
    """
    n = len(temperature_c)
    return rng.uniform(0, 360.0, size=n)


def arrhenius_rate_multiplier(temperature_c):
    """Rate relative to the 0C reference rate."""
    t_k = temperature_c + 273.15
    k_t = np.exp(-EA / (R_GAS * t_k))
    k_ref = np.exp(-EA / (R_GAS * T_REF_K))
    return k_t / k_ref


def generate_dataset(n=N_SAMPLES):
    temperature_c, band = sample_temperature(n)
    storage_time_hrs = sample_storage_time(temperature_c, band)

    rate_mult = arrhenius_rate_multiplier(temperature_c)

    # Normalizing constant tuned so cut-points land mid-sample-range rather than
    # pushing everything into one class.
    NORM_CONST = 900.0
    spoilage_progress = rate_mult * storage_time_hrs / NORM_CONST  # ~[0, 1.5+]
    s_clip = np.clip(spoilage_progress, 0, 1.0)

    # Each indicator gets its own noise scale, large enough that the three sensors show
    # realistic partial disagreement (target ~0.75-0.90 pairwise correlation, not ~0.95+ -
    # near-perfect correlation would mean the sensors are redundant, undermining the case
    # for a multi-sensor fusion model over a single hard threshold).
    tvbn = 2.0 + 33.0 * s_clip + rng.normal(0, 4.0, size=n)
    tvbn = np.clip(tvbn, 0.5, None)

    ph_level = 6.6 + 0.9 * s_clip + rng.normal(0, 0.20, size=n)
    ph_level = np.clip(ph_level, 6.0, 8.2)

    ammonia_ppm = 1.0 + 14.0 * (s_clip ** 1.2) + rng.normal(0, 3.0, size=n)
    ammonia_ppm = np.clip(ammonia_ppm, 0.1, None)

    humidity_pct = rng.uniform(70, 95, size=n)  # weak/no relationship to spoilage, by design

    spoilage_status = np.where(
        tvbn <= TVBN_FRESH_MAX, 0,
        np.where(tvbn <= TVBN_CAUTION_MAX, 1, 2)
    )

    df = pd.DataFrame({
        "ammonia_ppm": ammonia_ppm,
        "ph_level": ph_level,
        "temperature_c": temperature_c,
        "storage_time_hrs": storage_time_hrs,
        "humidity_pct": humidity_pct,
        "tvbn_mg_100g": tvbn,          # kept for reference/inspection, not fed to the model
        "spoilage_status": spoilage_status,
    })
    return df


df = generate_dataset(N_SAMPLES)
print("Generated dataset shape:", df.shape)
print("\nClass distribution:\n", df["spoilage_status"].value_counts().sort_index())
print("\nSample rows:\n", df.head())


# ---------------------------------------------------------------------------
# PHASE 2.2 — Correlation heatmap
# ---------------------------------------------------------------------------

corr_cols = ["ammonia_ppm", "ph_level", "temperature_c", "storage_time_hrs",
             "tvbn_mg_100g", "spoilage_status"]
corr_matrix = df[corr_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1,
            square=True, cbar_kws={"label": "Pearson r"})
plt.title("SensoPack — Feature Correlation Matrix (synthetic, 1500 samples)")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
if os.environ.get("COLAB_RELEASE_TAG"):
    plt.show()
print("\nSaved correlation_heatmap.png")
print("\nCorrelation matrix:\n", corr_matrix.round(2))


# ---------------------------------------------------------------------------
# PHASE 2.3 — Preprocess + stratified split
# ---------------------------------------------------------------------------

FEATURE_COLS = ["ammonia_ppm", "ph_level", "temperature_c", "storage_time_hrs", "humidity_pct"]
X = df[FEATURE_COLS]
y = df["spoilage_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=RNG_SEED
)
print(f"\nTrain size: {len(X_train)}  Test size: {len(X_test)}")


# ---------------------------------------------------------------------------
# PHASE 2.4 — Train Random Forest
# ---------------------------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    class_weight="balanced",
    random_state=RNG_SEED,
)
model.fit(X_train, y_train)


# ---------------------------------------------------------------------------
# PHASE 2.5 — Evaluate
# ---------------------------------------------------------------------------

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=["SAFE", "CAUTION", "UNSAFE"])

print(f"\nAccuracy: {acc:.4f}")
print("\nConfusion Matrix (rows=true, cols=predicted; order SAFE/CAUTION/UNSAFE):\n", cm)
print("\nClassification Report:\n", report)

print("\nFeature importances:")
for feat, imp in sorted(zip(FEATURE_COLS, model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {feat:20s} {imp:.3f}")


# ---------------------------------------------------------------------------
# PHASE 2.6 — Export
# ---------------------------------------------------------------------------

joblib.dump(model, "shrimp_spoilage_model.joblib")
print("\nSaved model to shrimp_spoilage_model.joblib")
