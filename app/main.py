import uvicorn
from fastapi import FastAPI
from app.api.routers import router

from app.core.config import settings


def get_application() -> FastAPI:
    """Create configured server application instance."""
    application = FastAPI(
        title=settings.API_TITLE,
        description=settings.API_DESCRIPTION,
        version=settings.API_VERSION,
        redoc_url=None,
    )

    application.include_router(router)
    return application


app = get_application()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)