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

    df["documentation_score"] = (
        df["readme_size"] / 1024
)

    # -----------------------------
    # Growth Metrics
    # -----------------------------
    df["stars_per_day"] = (
        df["stars"] /
        (df["repository_age_days"] + 1)
    )

    df["contributors_per_day"] = (
        df["contributors"] /
        (df["repository_age_days"] + 1)
    )

    df["releases_per_year"] = (
        df["releases"] * 365 /
        (df["repository_age_days"] + 1)
    )

    # -----------------------------
    # Activity Metrics
    # -----------------------------
    df["commit_recency_score"] = (
        1 / (df["days_since_last_commit"] + 1)
    )

    df["update_recency_score"] = (
        1 / (df["days_since_last_update"] + 1)
    )

    # -----------------------------
    # Community Metrics
    # -----------------------------
    df["contributors_per_branch"] = (
        df["contributors"] /
        (df["branches"] + 1)
    )

    df["watchers_per_star"] = (
        df["watchers"] /
        (df["stars"] + 1)
    )

    df["subscribers_per_star"] = (
        df["subscribers"] /
        (df["stars"] + 1)
    )

    return df