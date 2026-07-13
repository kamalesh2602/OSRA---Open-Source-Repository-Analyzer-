import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply the same feature engineering used during training.
    """

    df = df.copy()

    # -----------------------------
    # Convert dates
    # -----------------------------
    df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
    df["updated_at"] = pd.to_datetime(df["updated_at"], utc=True)
    df["pushed_at"] = pd.to_datetime(df["pushed_at"], utc=True)

    today = pd.Timestamp.now(tz="UTC")

    df["repository_age_days"] = (
        today - df["created_at"]
    ).dt.days

    df["days_since_last_update"] = (
        today - df["updated_at"]
    ).dt.days

    df["days_since_last_commit"] = (
        today - df["pushed_at"]
    ).dt.days

    # -----------------------------
    # Ratio Features
    # -----------------------------
    df["fork_star_ratio"] = df["forks"] / (df["stars"] + 1)

    df["stars_per_contributor"] = (
        df["stars"] / (df["contributors"] + 1)
    )

    df["issues_per_star"] = (
        df["open_issues"] / (df["stars"] + 1)
    )

    df["readme_per_size"] = (
        df["readme_size"] / (df["size"] + 1)
    )

    return df