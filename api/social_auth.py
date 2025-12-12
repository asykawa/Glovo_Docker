from fastapi import APIRouter
from starlette.requests import Request
from authlib.integrations.starlette_client import OAuth
from FastApiCourse.config import settings



social_router = APIRouter(prefix='/oauth', tags=['Social Pauth'])


oauth = OAuth()
oauth.register(
    name = 'github',
    client_id = settings.GITHUB_CLIENT_ID,
    secret_key = settings.GITHUB_SECRET,
    authorize_url='https://github.com/login/oauth/authorize',
)

oauth.register(
    name = 'google',
    client_id = settings.GOOGLE_CLIENT_ID,
    secret_key = settings.GOOGLE_SECRET,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    client_kwargs={"scope": "openid profile email"},
)

@social_router.get('/github')
async def login_github(request: Request):
    redirect_uri = settings.GITHUB_URL
    return await oauth.github.authorize_redirect(request, redirect_uri)

@social_router.get('/google')
async def login_google(request: Request):
    redirect_uri = settings.GOOGLE_URL
    return await oauth.google.authorize_redirect(request, redirect_uri)

