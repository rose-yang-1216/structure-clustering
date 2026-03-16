import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load features
data = pd.read_csv("data/example_features.csv")

# Cluster structures
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(data)

print("Cluster assignments:")
print(labels)

# PCA visualization
pca = PCA(n_components=2)
projection = pca.fit_transform(data)

plt.scatter(projection[:,0], projection[:,1], c=labels)
plt.title("Structure Clustering Visualization")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
