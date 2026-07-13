from pydantic import BaseModel


class RepositoryRequest(BaseModel):
    url: str


class RepositoryResponse(BaseModel):
    owner: str
    name: str
    full_name: str

    description: str | None
    language: str | None

    stars: int
    forks: int
    watchers: int
    open_issues: int

    size: int
    default_branch: str