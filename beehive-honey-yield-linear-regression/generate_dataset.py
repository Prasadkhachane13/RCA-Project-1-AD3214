"""Generates Beehive_Honey_Yield.csv  (SIMULATED data, fixed seed -> reproducible).

Generating rule (simplified beekeeping logic):
  Honey_Yield_kg = 2 + 0.35*colony_size + 1.8*flowering_area + 0.9*avg_temp - 0.05*rainfall + noise(sd 6)
Colony size and flowering area are mildly correlated (strong colonies sit in good forage areas).
Apiary_Type is random and has NO effect on yield (kept as a distractor column).
"""
import numpy as np, pandas as pd
rng = np.random.default_rng(7)
n = 500
area = np.clip(rng.gamma(3.0, 3.0, n) + 1, 1, 30)
colony = np.clip(35 + 1.2 * area + rng.normal(0, 12, n), 15, 90)
temp = np.clip(rng.normal(23, 4, n), 12, 34)
rain = np.clip(rng.gamma(4, 20, n), 10, 250)
yield_kg = 2 + 0.35 * colony + 1.8 * area + 0.9 * temp - 0.05 * rain + rng.normal(0, 6, n)
df = pd.DataFrame({"Hive_ID": np.arange(3001, 3001 + n),
                   "Apiary_Type": rng.choice(["Stationary", "Migratory", "Organic"], n),
                   "Colony_Size_k": colony.round(1), "Flowering_Area_ha": area.round(1),
                   "Avg_Temp_C": temp.round(1), "Rainfall_mm": rain.round(1),
                   "Honey_Yield_kg": np.clip(yield_kg, 0, None).round(1)})
df.to_csv("Beehive_Honey_Yield.csv", index=False)
print(df.shape, df.Honey_Yield_kg.describe().round(1).to_dict())
