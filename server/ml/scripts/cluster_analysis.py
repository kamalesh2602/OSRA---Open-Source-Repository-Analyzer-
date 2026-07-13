from pathlib import Path
import json

import pandas as pd

# ---------------------------------------------------
# Paths
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATASET = BASE_DIR / "data" / "processed" / "processed_dataset.csv"
CLUSTER_DATASET = BASE_DIR / "data" / "processed" / "clustered_dataset.csv"

ARTIFACTS = BASE_DIR / "artifacts"

SUMMARY_FILE = ARTIFACTS / "cluster_summary.csv"
JSON_FILE = ARTIFACTS / "cluster_metadata.json"

# ---------------------------------------------------
# Load datasets
# ---------------------------------------------------
raw_df = pd.read_csv(RAW_DATASET)
cluster_df = pd.read_csv(CLUSTER_DATASET)

raw_df["cluster"] = cluster_df["cluster"]

# ---------------------------------------------------
# Numeric Columns
# ---------------------------------------------------
numeric_columns = [
    "stars",
    "forks",
    "watchers",
    "subscribers",
    "contributors",
    "releases",
    "branches",
    "open_issues",
    "size",
    "readme_size",
]

summary = (
    raw_df.groupby("cluster")[numeric_columns]
    .mean()
    .round(2)
)

summary["repositories"] = raw_df.groupby("cluster").size()

# ---------------------------------------------------
# Identify Cluster Characteristics
# ---------------------------------------------------
popular_cluster = summary["stars"].idxmax()
active_cluster = summary["contributors"].idxmax()
stable_cluster = summary["releases"].idxmax()
lightweight_cluster = summary["size"].idxmin()
emerging_cluster = summary["stars"].idxmin()

summary["name"] = ""
summary["insight"] = ""

metadata = {}

for cluster in summary.index:

    tags = []

    if cluster == popular_cluster:
        tags.append("Popular")

    if cluster == active_cluster:
        tags.append("Actively Maintained")

    if cluster == stable_cluster:
        tags.append("Mature")

    if cluster == lightweight_cluster:
        tags.append("Lightweight")

    if cluster == emerging_cluster:
        tags.append("Emerging")

    if not tags:
        tags.append("General Purpose")

    cluster_name = " | ".join(tags)

    insight = (
        f"This cluster represents {cluster_name.lower()} repositories "
        f"with an average of "
        f"{int(summary.loc[cluster, 'stars'])} stars, "
        f"{int(summary.loc[cluster, 'contributors'])} contributors, "
        f"and {summary.loc[cluster, 'repositories']} repositories."
    )

    summary.loc[cluster, "name"] = cluster_name
    summary.loc[cluster, "insight"] = insight

    metadata[int(cluster)] = {
        "cluster": int(cluster),
        "name": cluster_name,
        "insight": insight,
        "repositories": int(summary.loc[cluster, "repositories"]),
        "average_stars": float(summary.loc[cluster, "stars"]),
        "average_forks": float(summary.loc[cluster, "forks"]),
        "average_watchers": float(summary.loc[cluster, "watchers"]),
        "average_contributors": float(summary.loc[cluster, "contributors"]),
        "average_releases": float(summary.loc[cluster, "releases"]),
        "average_size": float(summary.loc[cluster, "size"]),
    }

# ---------------------------------------------------
# Save
# ---------------------------------------------------
ARTIFACTS.mkdir(parents=True, exist_ok=True)

summary.to_csv(SUMMARY_FILE)

with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(metadata, file, indent=4)

print("\nCluster Analysis Completed")
print("=" * 60)

print(summary[["name", "repositories"]])

print(f"\nCSV  : {SUMMARY_FILE}")
print(f"JSON : {JSON_FILE}")