from sqlalchemy import Column, String

import uuid

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    spotify_id = Column(String, unique=True, nullable=False)
    display_name = Column(String, nullable=True)
