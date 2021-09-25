from fastapi import HTTPException, Security, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.core.auth import Auth
from deta import Deta
from app.db.models.model import AuthModel


deta = Deta()
users_db = deta.Base('users')
security = HTTPBearer()
auth_handler = Auth()

router = APIRouter()


@router.post('/signup')
def signup(user_details: AuthModel):
    if users_db.get(user_details.username) is not None:
        return 'Account already exists'
    try:
        hashed_password = auth_handler.encode_password(user_details.password)
        user = {'key': user_details.username, 'password': hashed_password}
        return users_db.put(user)
    except Exception as e:
        error_msg = 'Failed to signup user'
        return {e, error_msg}


@router.post('/login')
def login(user_details: AuthModel):
    user = users_db.get(user_details.username)
    if user is None:
        raise HTTPException(status_code=401, detail='Invalid username')
    if not auth_handler.verify_password(user_details.password, user['password']):
        raise HTTPException(status_code=401, detail='Invalid password')

    access_token = auth_handler.encode_token(user.get('key'))
    refresh_token = auth_handler.encode_refresh_token(user.get('key'))
    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.get('/refresh-token')
def update_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}


@router.post('/secret')
def secret_data(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if auth_handler.decode_token(token):
        return 'Top Secret data only authorized users can access this info'


@router.get('/no-secret')
def not_secret_data():
    return 'Not secret data'