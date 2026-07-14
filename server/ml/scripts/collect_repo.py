import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

SEARCH_URL = "https://api.github.com/search/repositories"
PER_PAGE = 100

QUERIES = [
    ("Enterprise", "stars:>50000", 25),
    ("Growing", "stars:1000..10000", 40),
    ("SmallActive", "stars:50..500 pushed:>2025-01-01", 40),
    ("Dormant", "pushed:<2022-01-01 archived:false", 40),
    ("Archived", "archived:true", 35),
    ("New", "created:>2025-01-01 stars:<100", 35),
    ("Hobby", "stars:10..50 fork:false", 35),
]

repositories = []

for category, query, limit in QUERIES:

    print(f"\nCollecting {category} repositories...")

    page = 1

    while len([r for r in repositories if r["category"] == category]) < limit:

        response = requests.get(
            SEARCH_URL,
            headers=HEADERS,
            params={
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": PER_PAGE,
                "page": page,
            },
        )

        if response.status_code != 200:
            print(response.json())
            break

        items = response.json()["items"]

        if not items:
            break

        for repo in items:

            repositories.append(
                {
                    "owner": repo["owner"]["login"],
                    "repository": repo["name"],
                    "category": category,
                }
            )

            if len([r for r in repositories if r["category"] == category]) >= limit:
                break

        page += 1
        time.sleep(1)

df = pd.DataFrame(repositories)

df.drop_duplicates(
    subset=["owner", "repository"],
    inplace=True,
)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_FILE = BASE_DIR / "data" / "raw" / "repositories.csv"

df.to_csv(
    OUTPUT_FILE,
    index=False,
)

print("\nCategory Distribution:")
print(df["category"].value_counts())
print(f"\nCollected {len(df)} repositories.")
print(f"Saved to: {OUTPUT_FILE}")