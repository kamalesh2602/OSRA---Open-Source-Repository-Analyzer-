from urllib.parse import urlparse


def parse_repo_url(url: str) -> tuple[str, str]:
    """
    Convert:
    https://github.com/facebook/react

    Into:
    ("facebook", "react")
    """

    path = urlparse(url).path.strip("/")
    owner, repo = path.split("/")[:2]
    return owner, repo

print(parse_repo_url("https://github.com/facebook/react"))