from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "feature_dataset.csv"

OUTPUT_DATASET = BASE_DIR / "data" / "processed" / "clustered_dataset.csv"

ARTIFACTS = BASE_DIR / "artifacts"

MODEL_FILE = ARTIFACTS / "kmeans.pkl"

ELBOW_PLOT = ARTIFACTS / "elbow_plot.png"

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(INPUT_FILE)

X = df.values

# -----------------------------
# Find Best K
# -----------------------------
inertia = []
silhouette_scores = []

K = range(2, 11)

for k in K:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20,
    )

    labels = model.fit_predict(X)

    inertia.append(model.inertia_)

    silhouette_scores.append(
        silhouette_score(X, labels)
    )

# -----------------------------
# Print Scores
# -----------------------------
print("\nK Selection")

for k, score in zip(K, silhouette_scores):

    print(
    f"K={k} | "
    f"Silhouette={score:.4f} | "
    f"Inertia={inertia[k-2]:.2f}"
)

# -----------------------------
# Select Best K
# -----------------------------
best_k = K[silhouette_scores.index(max(silhouette_scores))]

print(f"\nBest K = {best_k}")

# -----------------------------
# Train Final Model
# -----------------------------
model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=20,
)

clusters = model.fit_predict(X)

df["cluster"] = clusters
print("\nCluster Distribution")
print(df["cluster"].value_counts().sort_index())

# -----------------------------
# Save Model
# -----------------------------
ARTIFACTS.mkdir(
    parents=True,
    exist_ok=True,
)

joblib.dump(
    model,
    MODEL_FILE,
)

# -----------------------------
# Save Dataset
# -----------------------------
df.to_csv(
    OUTPUT_DATASET,
    index=False,
)

# -----------------------------
# Elbow Plot
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(K, inertia, marker="o")

plt.xlabel("Number of Clusters")

plt.ylabel("Inertia")

plt.title("Elbow Method")

plt.grid(True)

plt.savefig(ELBOW_PLOT)

print("\nTraining Completed")
print(f"Model saved : {MODEL_FILE}")
print(f"Dataset saved : {OUTPUT_DATASET}")
print(f"Elbow plot : {ELBOW_PLOT}")