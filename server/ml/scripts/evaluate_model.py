from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "data" / "processed" / "clustered_dataset.csv"

ARTIFACTS = BASE_DIR / "artifacts"

PCA_PLOT = ARTIFACTS / "clusters_pca.png"

MODEL_FILE = ARTIFACTS / "kmeans.pkl"

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(DATASET)

X = df.drop(columns=["cluster"])

labels = df["cluster"]

# -----------------------------
# Evaluation Metrics
# -----------------------------
silhouette = silhouette_score(X, labels)

davies = davies_bouldin_score(X, labels)

calinski = calinski_harabasz_score(X, labels)

print("\nCluster Evaluation")
print("-" * 40)

print(f"Silhouette Score      : {silhouette:.4f}")
print(f"Davies-Bouldin Index  : {davies:.4f}")
print(f"Calinski-Harabasz     : {calinski:.2f}")

# -----------------------------
# Cluster Counts
# -----------------------------
print("\nRepositories per Cluster")

print(df["cluster"].value_counts().sort_index())

# -----------------------------
# PCA Visualization
# -----------------------------
pca = PCA(n_components=2)

components = pca.fit_transform(X)

plot_df = pd.DataFrame(
    {
        "PC1": components[:, 0],
        "PC2": components[:, 1],
        "cluster": labels,
    }
)

plt.figure(figsize=(8, 6))

for cluster in sorted(plot_df["cluster"].unique()):
    cluster_data = plot_df[plot_df["cluster"] == cluster]

    plt.scatter(
        cluster_data["PC1"],
        cluster_data["PC2"],
        label=f"Cluster {cluster}",
    )

plt.title("Repository Clusters (PCA)")

plt.xlabel("Principal Component 1")

plt.ylabel("Principal Component 2")

plt.legend()

plt.grid(True)

ARTIFACTS.mkdir(parents=True, exist_ok=True)

plt.savefig(PCA_PLOT)

print(f"\nPCA plot saved to:\n{PCA_PLOT}")