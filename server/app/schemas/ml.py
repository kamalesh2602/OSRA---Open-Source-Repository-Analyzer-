from pydantic import BaseModel


class PredictRequest(BaseModel):
    repo_url: str


class PredictResponse(BaseModel):
    cluster: int
    repository: str
    message: str