
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
import joblib

# Dataset
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
])

y = np.array([10, 14, 18, 22])

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Train
pipeline.fit(X, y)

# Save pipeline (not just model)
joblib.dump(pipeline, "model.joblib")

print("Pipeline trained and saved!")