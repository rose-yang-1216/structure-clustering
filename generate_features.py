import numpy as np
import pandas as pd

# Simulate structural feature vectors
# (in practice these could be TM-scores, secondary structure content, etc.)

np.random.seed(42)

num_structures = 100
num_features = 10

features = np.random.rand(num_structures, num_features)

df = pd.DataFrame(features)
df.to_csv("data/example_features.csv", index=False)

print("Feature matrix saved to data/example_features.csv")
