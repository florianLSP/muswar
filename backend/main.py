from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Request
from db.models import Base
from db.session import engine
from spotipy.oauth2 import SpotifyOAuth
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

spotiy_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="user-library-read",
)


@app.get("/")
async def read_root():
    return {"message": "Muswar App"}


@app.get("/auth/login")
def login():
    auth_url = spotiy_oauth.get_authorize_url()
    return RedirectResponse(auth_url)


@app.get("/auth/callback")
def auth_callback(request: Request):
    code = request.query_params.get("code")
    token_info = spotiy_oauth.get_access_token(code)
    access_token = token_info["access_token"]
    refresh_token = token_info["refresh_token"]

    return {"access_token": access_token, "refresh_token": refresh_token}
