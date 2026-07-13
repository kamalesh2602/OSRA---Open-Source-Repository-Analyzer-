from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import ml

router = APIRouter()

router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

router.include_router(
    ml.router,
    prefix="/ml",
    tags=["Machine Learning"]
)