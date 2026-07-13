from fastapi import APIRouter, HTTPException

from app.schemas.repository import (
    RepositoryRequest,
    RepositoryResponse,
)

from app.services.github import GitHubService
from app.utils.parser import parse_repo_url

router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
)

github = GitHubService()

from fastapi import APIRouter, HTTPException

...

@router.post("/analyze", response_model=RepositoryResponse)
async def analyze_repository(data: RepositoryRequest):
    try:
        owner, repo = parse_repo_url(data.url)
        repository = await github.get_repository(owner, repo)

        return RepositoryResponse(
            owner=repository["owner"]["login"],
            name=repository["name"],
            full_name=repository["full_name"],
            description=repository["description"],
            language=repository["language"],
            stars=repository["stargazers_count"],
            forks=repository["forks_count"],
            watchers=repository["watchers_count"],
            open_issues=repository["open_issues_count"],
            size=repository["size"],
            default_branch=repository["default_branch"],
        )

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))