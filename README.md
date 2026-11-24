# Beehive Honey Yield Prediction – Linear Regression

A machine learning project comparing **Simple** and **Multiple Linear Regression** for predicting a beehive's seasonal honey yield (kg).


## Dataset
**Beehive_Honey_Yield.csv** – 500 rows, 7 columns.

| Column | Description |
|---|---|
| Hive_ID | Row identifier (not a feature) |
| Apiary_Type | Stationary / Migratory / Organic (no effect by design) |
| Colony_Size_k | Colony size in thousands of bees |
| Flowering_Area_ha | Hectares of flowering forage nearby |
| Avg_Temp_C | Average season temperature (°C) |
| Rainfall_mm | Average monthly rainfall (mm) |
| Honey_Yield_kg | Target: honey produced per season (kg) |

## Results (test set, 100 samples)
| Metric | Simple LR (Flowering Area) | Multiple LR (4 features) |
|---|---|---|
| MAE | 5.96 | 4.26 |
| MSE | 53.78 | 28.49 |
| RMSE | 7.33 | 5.34 |
| R² | 0.693 | 0.838 |

5-fold CV mean R² (multiple LR): 0.805. Because the data is simulated, learned coefficients can be compared with the true generating values documented in .

## Run it
```
pip install -r requirements.txt
python generate_dataset.py          # optional: regenerates the CSV
jupyter notebook Beehive_Honey_Yield_Linear_Regression.ipynb
```

## Structure
```
beehive-honey-yield-linear-regression/
├── Beehive_Honey_Yield.csv
├── generate_dataset.py
├── Beehive_Honey_Yield_Linear_Regression.ipynb
├── requirements.txt
└── README.md
```
