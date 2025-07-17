from pydantic import BaseModel


class UserCreate(BaseModel):
    spotify_id: str
    display_name: str = None


class UserResponse(BaseModel):
    id: str
    spotify_id: str
    display_name: str = None

    class Config:
        from_attributes = True
