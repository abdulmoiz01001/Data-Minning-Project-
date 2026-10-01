import json
import os

notebook_path = "assignment-EDA.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# The new cells to append
cells = []

# Data Cleaning Cell
cleaning_code = """# Data Cleaning for Outlier Detection
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# Remove cancelled orders and negative prices
retail_clean = retail_clean[(retail_clean['Quantity'] > 0) & (retail_clean['UnitPrice'] > 0)]
# Drop rows with missing CustomerID to ensure clean continuous features
retail_clean = retail_clean.dropna(subset=['CustomerID'])

# We'll focus on 'Quantity' and 'UnitPrice' for outlier detection.
# To keep notebook execution fast and efficient for KNN, we sample 10,000 records.
df_sample = retail_clean.sample(10000, random_state=42).copy()
print("Sample size for Outlier Detection:", df_sample.shape)
"""
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "source": [line + "\n" for line in cleaning_code.split("\n")[:-1]],
    "outputs": []
})

# IQR Cell
iqr_code = """# 1. Statistical Approach: IQR (Interquartile Range)
Q1 = df_sample[['Quantity', 'UnitPrice']].quantile(0.25)
Q3 = df_sample[['Quantity', 'UnitPrice']].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
iqr_outliers = df_sample[((df_sample[['Quantity', 'UnitPrice']] < lower_bound) | (df_sample[['Quantity', 'UnitPrice']] > upper_bound)).any(axis=1)]
print(f"Number of IQR Outliers: {len(iqr_outliers)}")
print(iqr_outliers[['Quantity', 'UnitPrice']].head())
"""
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "source": [line + "\n" for line in iqr_code.split("\n")[:-1]],
    "outputs": []
})

# Z-Score Cell
zscore_code = """# 2. Statistical Approach: Z-Score
# stats.zscore returns a numpy array or dataframe depending on pandas version. 
# We'll apply it directly to the columns and create a new dataframe
z_scores = np.abs(stats.zscore(df_sample[['Quantity', 'UnitPrice']]))

# Threshold usually set to 3
threshold = 3
z_outliers = df_sample[(z_scores > threshold).any(axis=1)]
print(f"Number of Z-Score Outliers: {len(z_outliers)}")
print(z_outliers[['Quantity', 'UnitPrice']].head())
"""
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "source": [line + "\n" for line in zscore_code.split("\n")[:-1]],
    "outputs": []
})

# KNN Cell
knn_code = """# 3. Distance-based Approach: KNN
X = df_sample[['Quantity', 'UnitPrice']].values

# Fit KNN (n_neighbors=5 is a common default)
knn = NearestNeighbors(n_neighbors=5)
knn.fit(X)
distances, indices = knn.kneighbors(X)

# The outlier score is the distance to the 5th nearest neighbor
outlier_scores = distances[:, -1]

# Set threshold as the 95th percentile of distances (top 5% furthest points)
knn_threshold = np.percentile(outlier_scores, 95)

df_sample['knn_score'] = outlier_scores
knn_outliers = df_sample[df_sample['knn_score'] > knn_threshold]
print(f"Number of KNN Outliers: {len(knn_outliers)}")
print(knn_outliers[['Quantity', 'UnitPrice', 'knn_score']].head())
"""
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "source": [line + "\n" for line in knn_code.split("\n")[:-1]],
    "outputs": []
})

nb['cells'].extend(cells)

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
print("Notebook updated.")
