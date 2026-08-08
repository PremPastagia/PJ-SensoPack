`# Phase 1 — Literature Parameters for Shrimp Spoilage (SensoPack)

Species: primarily *Litopenaeus vannamei* (whiteleg shrimp) — best-quantified in available literature.
*Penaeus monodon* (black tiger shrimp)-specific thresholds were not well quantified in this
research pass; both are penaeid shrimp with similar spoilage biochemistry (protein/amine
degradation via bacterial and enzymatic action), so these bounds are extended to monodon by
analogy, not independently verified for it. State this honestly if asked — don't claim
monodon-specific validation.

**Consistency note:** these bounds are chosen to align with numbers already stated in the
team's existing pitch materials (`R2_BioFilm_Report.md`, `SensoPack_PitchDeck.html`,
`SensoPack_Team_Prep.html`): TVB-N spoilage limit ~30-35 mg/100g, pH >7.5 = spoilage,
3-state Fresh/Caution/Unsafe classification, Arrhenius-style temperature notes.

---

## 1. Quantitative bounds by freshness class

| Parameter | Fresh (0) | Caution (1) | Spoiled (2) |
|---|---|---|---|
| TVB-N (mg N/100g) | 0–25 | 25–35 | >35 |
| pH | 6.5–7.2 | 7.2–7.5 | >7.5 |
| Ammonia headspace (ppm)* | 0–5 | 5–15 | >15 |
| Storage temperature (°C) | input feature, −2 to 30 | — | — |
| Storage duration (hours) | 0–120 (~0–5d) | 120–216 (~5–9d) | >216 (~>9d) |
| Relative humidity (%RH) | 70–95 (all classes — secondary covariate) | — | — |

\* **Read before trusting this number.** Lab studies using ultra-sensitive nanomaterial
sensors placed directly at the sample surface report ppb-level ammonia (100–300 ppb) at the
fresh/spoiling boundary. Consumer MOS sensors (MQ-137-class) in an enclosed package headspace
equilibrate differently and typically respond in the low-ppm range once spoilage volatiles
accumulate. The bounds above target the MQ-137/enclosed-headspace case, not the lab
surface-sensor case. **Recalibrate against your actual sensor + enclosure once hardware is
wired — this is a placeholder shape for synthetic data, not a validated constant.**

### Sources
- Quality assessment and acceptability of whiteleg shrimp (*L. vannamei*) using biochemical
  parameters — Springer/Fisheries and Aquatic Sciences: <25 mg N/100g fresh, 25–30 acceptable,
  >30 borderline; sensory rejection observed at 20–21 mg N/100g in refrigerated storage.
  https://link.springer.com/article/10.1186/s41240-020-00167-6
- Same study family (e-fas archive): pH 6.8–7.2 through 12 days (excellent/very good), rising
  to 7.4–7.5 by 15 days. https://www.e-fas.org/archive/view_article?pid=fas-23-0-21
- Integrated microbiological/physicochemical/sensory shrimp shelf-life study: pH 6.52 → 7.60
  over 14 days chilled storage at 2°C. https://doi.org/10.3390/microorganisms14061266
- TVB-N kinetics at 25°C (whole body/meat): 1.86 → 34.71 mg/100g, shelf life 17–20h at that
  temperature — illustrates how strongly temperature bends the timeline versus chill storage.
- Comprehensive review of shrimp spoilage indicators/sensors (ammonia, pH, TVB-N, TBARS as
  the standard biomarker set).
  https://www.sciencedirect.com/science/article/abs/pii/S0963996923008153
- Ammonia/TVB-N sensor correlation: fresh fish (TVB-N 18 mg/100g) ≈100 ppb effective ammonia;
  accepted freshness limit (TVB-N 28–35 mg/100g) ≈200–300 ppb — a lab surface-sensor
  calibration, flagged above as not directly transferable to an enclosed MQ-137 headspace
  reading.
- Frozen shrimp shelf-life Arrhenius modelling: activation energy 118–156 kJ/mol across
  quality indices (chemical indices ~118–119 kJ/mol used here).
  https://www.researchgate.net/publication/222809493_Shelf_life_modelling_of_frozen_shrimp_at_variable_temperature_conditions

---

## 2. Arrhenius kinetic relationship

k(T) = A · exp(−Ea / R·T)

- Ea ≈ 118 kJ/mol (literature range 118–156 kJ/mol for chilled/frozen shrimp chemical
  spoilage indices; the lower end — chemical indices specifically — was used since TVB-N/pH
  are chemical, not color/texture, indices).
- R = 8.314 J/mol·K
- T in Kelvin

This rate constant scales how fast TVB-N/pH/ammonia move from fresh toward spoiled bounds as
a function of storage temperature — it is used directly in the Phase 2 synthetic-data
generator (`sensopack_colab.py`) as a multiplier on elapsed storage time, rather than left as
a qualitative note.

---

## 3. Expected Pearson correlation matrix (target structure)

| | Ammonia | pH | Temp | Time | TVB-N | Spoilage |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Ammonia | 1.00 | 0.75 | 0.55 | 0.65 | 0.90 | 0.88 |
| pH | | 1.00 | 0.45 | 0.60 | 0.80 | 0.75 |
| Temp | | | 1.00 | ~0.10 | 0.55 | 0.45 |
| Time | | | | 1.00 | 0.60 | 0.55 |
| TVB-N | | | | | 1.00 | 0.90 |
| Spoilage | | | | | | 1.00 |

Temp–Time correlation is intentionally near zero: they are independently sampled inputs. It's
their *interaction* through the Arrhenius rate — not a direct correlation between the two
inputs — that drives TVB-N/ammonia/pH. The actual computed correlation matrix from the
generated 1500-sample dataset (see `correlation_heatmap.png` after running
`sensopack_colab.py`) should approximate this table; it won't match exactly since it's
generated from stochastic sampling, not hardcoded.

---

## 4. Known tension with existing pitch materials

`SensoPack_Team_Prep.html` explicitly instructs the team not to claim the AI model is *built*
or cite an accuracy% to judges — it was pitched as a conceptual "Cloud AI" / "Freshness-
Intelligence AI." This pipeline produces a real trained model with a real accuracy score,
which is appropriate for an internal working prototype but would contradict that specific
pitch instruction if quoted to judges as-is. Decide consciously whether/how this demo gets
shown externally.
