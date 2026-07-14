from pathlib import Path

import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from ml.utils.feature_transformer import engineer_features

# ---------------------------------------------------
# Paths
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "processed_dataset.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "feature_dataset.csv"

ARTIFACTS_DIR = BASE_DIR / "artifacts"

SCALER_FILE = ARTIFACTS_DIR / "scaler.pkl"
ENCODER_FILE = ARTIFACTS_DIR / "encoder.pkl"
FEATURE_COLUMNS_FILE = ARTIFACTS_DIR / "feature_columns.pkl"


def feature_engineering():

    # ---------------------------------------------------
    # Load Dataset
    # ---------------------------------------------------
    df = pd.read_csv(INPUT_FILE)

    # ---------------------------------------------------
    # Reduce Language Categories
    # ---------------------------------------------------
    top_languages = [
        "Python",
        "JavaScript",
        "TypeScript",
        "Java",
        "C",
        "C++",
        "Go",
        "Rust",
    ]

    df["language"] = df["language"].apply(
        lambda x: x if x in top_languages else "Other"
    )

    # ---------------------------------------------------
    # Apply Feature Engineering
    # ---------------------------------------------------
    df = engineer_features(df)

    # ---------------------------------------------------
    # Encode ONLY Language
    # ---------------------------------------------------
    encoder = OneHotEncoder(
        sparse_output=False,
        handle_unknown="ignore",
    )

    encoded = encoder.fit_transform(
        df[["language"]]
    )

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(
            ["language"]
        ),
    )

    # ---------------------------------------------------
    # Drop Unused Columns
    # ---------------------------------------------------
    df = df.drop(
        columns=[
            "owner",
            "repository",
            "category",
            "language",
            "license",
            "created_at",
            "updated_at",
            "pushed_at",
            "default_branch",
        ]
    )

    # ---------------------------------------------------
    # Merge Encoded Features
    # ---------------------------------------------------
    df = pd.concat(
        [
            df.reset_index(drop=True),
            encoded_df.reset_index(drop=True),
        ],
        axis=1,
    )

    # ---------------------------------------------------
    # Save Feature Columns
    # ---------------------------------------------------
    feature_columns = list(df.columns)

    print(f"\nFeature Count : {len(feature_columns)}")

    # ---------------------------------------------------
    # Scale Features
    # ---------------------------------------------------
    scaler = StandardScaler()

    scaled = scaler.fit_transform(df)

    feature_df = pd.DataFrame(
        scaled,
        columns=feature_columns,
    )

    # ---------------------------------------------------
    # Save Artifacts
    # ---------------------------------------------------
    ARTIFACTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        scaler,
        SCALER_FILE,
    )

    joblib.dump(
        encoder,
        ENCODER_FILE,
    )

    joblib.dump(
        feature_columns,
        FEATURE_COLUMNS_FILE,
    )

    # ---------------------------------------------------
    # Save Dataset
    # ---------------------------------------------------
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    feature_df.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    # ---------------------------------------------------
    # Summary
    # ---------------------------------------------------
    print("\nFeature Engineering Completed")
    print("-" * 50)
    print(f"Repositories : {feature_df.shape[0]}")
    print(f"Features     : {feature_df.shape[1]}")
    print(f"\nDataset saved to:\n{OUTPUT_FILE}")
    print("\nArtifacts saved:")
    print(f"  • {SCALER_FILE.name}")
    print(f"  • {ENCODER_FILE.name}")
    print(f"  • {FEATURE_COLUMNS_FILE.name}")


if __name__ == "__main__":
    feature_engineering()