from fastapi import APIRouter, HTTPException
from urllib.parse import urlparse

from app.schemas.ml import PredictRequest, PredictResponse
from app.services.ml_service import ml_service
from app.services.github import github_service

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    try:
        # Parse GitHub URL
        parsed = urlparse(request.repo_url)
        parts = parsed.path.strip("/").split("/")

        if len(parts) < 2:
            raise HTTPException(
                status_code=400,
                detail="Invalid GitHub repository URL."
            )

        owner = parts[0]
        repo_name = parts[1]

        # Fetch repository details
        repo = await github_service.get_repository(owner, repo_name)

        if not repo:
            raise HTTPException(
                status_code=404,
                detail="Repository not found."
            )

        # ML Prediction
        result = ml_service.predict_repository(repo)

        return PredictResponse(
    cluster=result["cluster"],
    repository=f"{owner}/{repo_name}",
    message=f"Repository belongs to Cluster {result['cluster']}"
)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )