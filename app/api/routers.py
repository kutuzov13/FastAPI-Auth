from fastapi import APIRouter

from app.api.endpoints.about import router as about_route
from app.api.endpoints.auth import router as auth_route

router = APIRouter()

router.include_router(about_route, tags=['about'])
router.include_router(auth_route, tags=['auth'])