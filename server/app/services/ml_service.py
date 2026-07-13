import os
import joblib
import pandas as pd

from ml.utils.feature_transformer import engineer_features

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

MODEL_DIR = os.path.join(BASE_DIR, "ml", "artifacts")


class MLService:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.encoder = None
        self.feature_columns = None

        self.load_models()

    def load_models(self):
        print(f"\n📁 Loading models from: {MODEL_DIR}\n")

        self.model = joblib.load(os.path.join(MODEL_DIR, "kmeans.pkl"))
        print("✅ kmeans.pkl loaded")

        self.scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
        print("✅ scaler.pkl loaded")

        self.encoder = joblib.load(os.path.join(MODEL_DIR, "encoder.pkl"))
        print("✅ encoder.pkl loaded")

        self.feature_columns = joblib.load(
            os.path.join(MODEL_DIR, "feature_columns.pkl")
        )
        print("✅ feature_columns.pkl loaded")

    def prepare_features(self, repo):
        # Create one-row DataFrame from GitHub API response
        df = pd.DataFrame([{
            "owner": repo["owner"]["login"],
            "repository": repo["name"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["watchers_count"],
            "open_issues": repo["open_issues_count"],
            "size": repo["size"],
            "language": repo["language"] or "Unknown",
            "license": (
                repo["license"]["name"]
                if repo.get("license")
                else "No License"
            ),
            "contributors": 0,
            "releases": 0,
            "readme_size": 0,
            "has_wiki": int(repo["has_wiki"]),
            "has_projects": int(repo["has_projects"]),
            "has_issues": int(repo["has_issues"]),
            "has_pages": int(repo["has_pages"]),
            "archived": int(repo["archived"]),
            "disabled": int(repo["disabled"]),
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"],
            "pushed_at": repo["pushed_at"],
            "default_branch": repo["default_branch"],
        }])

        # Apply feature engineering
        df = engineer_features(df)

        # Encode categorical features
        encoded = self.encoder.transform(df[["language", "license"]])

        encoded_df = pd.DataFrame(
            encoded,
            columns=self.encoder.get_feature_names_out(
                ["language", "license"]
            ),
        )

        # Drop columns removed during training
        df = df.drop(columns=[
            "owner",
            "repository",
            "language",
            "license",
            "created_at",
            "updated_at",
            "pushed_at",
            "default_branch",
        ])

        # Merge encoded columns
        df = pd.concat(
            [df.reset_index(drop=True), encoded_df.reset_index(drop=True)],
            axis=1,
        )

        # Match training column order
        for col in self.feature_columns:
            if col not in df.columns:
                df[col] = 0

        df = df[self.feature_columns]

        return df

    def predict_repository(self, repo):
        features = self.prepare_features(repo)

        scaled = self.scaler.transform(features)

        cluster = int(self.model.predict(scaled)[0])

        return {
            "cluster": cluster
        }


ml_service = MLService()