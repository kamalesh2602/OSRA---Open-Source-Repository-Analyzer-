from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "repository_dataset.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "processed_dataset.csv"


def preprocess():

    df = pd.read_csv(INPUT_FILE)
    print(df["category"].value_counts())
    
    # Remove duplicates
    df.drop_duplicates(
        subset=["owner", "repository"],
        inplace=True,
    )

    # Fill missing values
    df["language"] = df["language"].fillna("Unknown")
    df["license"] = df["license"].fillna("No License")
    df["readme_size"] = df["readme_size"].fillna(0)
    df["contributors"] = df["contributors"].fillna(0)
    df["releases"] = df["releases"].fillna(0)

    # Convert booleans
    bool_columns = [
        "has_wiki",
        "has_projects",
        "has_issues",
        "has_pages",
        "archived",
        "disabled",
    ]

    for col in bool_columns:
        df[col] = df[col].astype(int)

    # Convert dates
    date_columns = [
        "created_at",
        "updated_at",
        "pushed_at",
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("Preprocessing completed.")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    preprocess()