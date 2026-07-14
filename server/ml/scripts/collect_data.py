from pathlib import Path
import os

import pandas as pd
import requests
from dotenv import load_dotenv
from tqdm import tqdm

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "repositories.csv"
OUTPUT_FILE = BASE_DIR / "data" / "raw" / "repository_dataset.csv"


# -----------------------------
# GitHub API Helper
# -----------------------------
def github_get(url: str):
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()

    return None


# -----------------------------
# GitHub API Functions
# -----------------------------
def get_repository(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    data = github_get(url)

    if data is None:
        print(f"Failed: {owner}/{repo}")

    return data


def get_contributors(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

    data = github_get(url)

    if data is None:
        return 0

    return len(data)


def get_releases(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"

    data = github_get(url)

    if data is None:
        return 0

    return len(data)


def get_branches(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"

    data = github_get(url)

    if data is None:
        return 0

    return len(data)


def get_readme_size(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    data = github_get(url)

    if data is None:
        return 0

    return data.get("size", 0)


# -----------------------------
# Metadata Extraction
# -----------------------------
def extract_metadata(
    repo_data,
    contributors,
    releases,
    branches,
    readme_size,
    category
):
    license_name = None

    if repo_data.get("license"):
        license_name = repo_data["license"]["spdx_id"]

    return {
        # Repository
        "owner": repo_data["owner"]["login"],
        "repository": repo_data["name"],
        "category": category,

        # Popularity
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "watchers": repo_data["watchers_count"],
        "subscribers": repo_data["subscribers_count"],

        # Issues
        "open_issues": repo_data["open_issues_count"],

        # Repository Info
        "size": repo_data["size"],
        "language": repo_data["language"],
        "topics_count": len(repo_data.get("topics", [])),
        "license": license_name,
        "default_branch": repo_data["default_branch"],

        # Community
        "contributors": contributors,
        "releases": releases,
        "branches": branches,

        # Documentation
        "readme_size": readme_size,

        # Repository Flags
        "has_wiki": repo_data["has_wiki"],
        "has_projects": repo_data["has_projects"],
        "has_issues": repo_data["has_issues"],
        "has_pages": repo_data["has_pages"],
        "archived": repo_data["archived"],
        "disabled": repo_data["disabled"],

        # Dates
        "created_at": repo_data["created_at"],
        "updated_at": repo_data["updated_at"],
        "pushed_at": repo_data["pushed_at"],
    }


# -----------------------------
# Main Function
# -----------------------------
def collect_data():
    repositories = pd.read_csv(INPUT_FILE)

    dataset = []

    for _, row in tqdm(repositories.iterrows(), total=len(repositories)):
        owner = row["owner"]
        repo = row["repository"]
        category = row["category"]

        repository = get_repository(owner, repo)

        if repository is None:
            continue

        contributors = get_contributors(owner, repo)
        releases = get_releases(owner, repo)
        branches = get_branches(owner, repo)
        readme_size = get_readme_size(owner, repo)

        dataset.append(
            extract_metadata(
                repository,
                contributors,
                releases,
                branches,
                readme_size,
                category
            )
        )

    df = pd.DataFrame(dataset)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nDataset saved to:\n{OUTPUT_FILE}")
    print(f"Repositories collected: {len(df)}")


if __name__ == "__main__":
    collect_data()