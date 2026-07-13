import httpx

from app.core.config import settings


class GitHubService:
    async def get_repository(self, owner: str, repo: str):
        headers = {}

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

        url = f"{settings.GITHUB_API}/repos/{owner}/{repo}"

        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(url, headers=headers)

        response.raise_for_status()

        return response.json()