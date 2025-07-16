from fastapi import FastAPI
from db.models import Base
from db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_root():
    return {"message": "Muswar App"}
