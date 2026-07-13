from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.repository import router as repository_router

router = APIRouter()

router.include_router(health_router)
router.include_router(repository_router)