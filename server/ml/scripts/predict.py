from pathlib import Path
import json

import joblib
import pandas as pd

from ml.scripts.collect_data import (
    get_repository,
    get_contributors,
    get_releases,
    get_branches,
    get_readme_size,
    extract_metadata,
)

from ml.utils.feature_transformer import engineer_features

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

ARTIFACTS = BASE_DIR / "artifacts"

MODEL = joblib.load(ARTIFACTS / "kmeans.pkl")
SCALER = joblib.load(ARTIFACTS / "scaler.pkl")
ENCODER = joblib.load(ARTIFACTS / "encoder.pkl")
FEATURE_COLUMNS = joblib.load(
    ARTIFACTS / "feature_columns.pkl"
)

with open(
    ARTIFACTS / "cluster_metadata.json",
    encoding="utf-8",
) as f:
    CLUSTER_METADATA = json.load(f)


def predict(owner: str, repo: str):

    repository = get_repository(owner, repo)

    if repository is None:
        print("Repository not found.")
        return

    contributors = get_contributors(owner, repo)
    releases = get_releases(owner, repo)
    branches = get_branches(owner, repo)
    readme = get_readme_size(owner, repo)

    metadata = extract_metadata(
        repository,
        contributors,
        releases,
        branches,
        readme,
    )

    df = pd.DataFrame([metadata])

    # -----------------------------
    # Feature Engineering
    # -----------------------------
    df = engineer_features(df)

    # -----------------------------
    # Encode
    # -----------------------------
    encoded = ENCODER.transform(
        df[["language", "license"]]
    )

    encoded_df = pd.DataFrame(
        encoded,
        columns=ENCODER.get_feature_names_out(
            ["language", "license"]
        ),
    )

    # -----------------------------
    # Drop unused columns
    # -----------------------------
    df = df.drop(
        columns=[
            "owner",
            "repository",
            "language",
            "license",
            "created_at",
            "updated_at",
            "pushed_at",
            "default_branch",
        ]
    )

    df = pd.concat(
        [
            df.reset_index(drop=True),
            encoded_df.reset_index(drop=True),
        ],
        axis=1,
    )

    # -----------------------------
    # Match training columns
    # -----------------------------
    df = df.reindex(
        columns=FEATURE_COLUMNS,
        fill_value=0,
    )

    # -----------------------------
    # Scale
    # -----------------------------
    X = SCALER.transform(df)

    cluster = MODEL.predict(X)[0]

    info = CLUSTER_METADATA[str(cluster)]

    print("\n==============================")
    print(f"Repository : {owner}/{repo}")
    print("==============================")
    print(f"Cluster : {cluster}")
    print(f"Name    : {info['name']}")
    print()
    print(info["insight"])


if __name__ == "__main__":

    url = input("GitHub URL : ").strip()

    url = url.rstrip("/")

    owner, repo = url.split("/")[-2:]

    predict(owner, repo)