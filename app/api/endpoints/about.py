from fastapi import APIRouter, Depends

from app.core.config import Settings, get_setting

router = APIRouter()


@router.get('/about')
def about(setting: Settings = Depends(get_setting)):
    return {
        'Framework': 'FastAPI',
        'Version': setting.API_VERSION,
        'Environment': setting.ENVIRONMENT,
        'Debug': setting.DEBUG,
    }