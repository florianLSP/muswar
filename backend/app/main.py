from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db
from . import models, schemas

# creation des tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Muswar")


@app.get("/")
async def root():
    return {"message": "Muswar - v1"}
