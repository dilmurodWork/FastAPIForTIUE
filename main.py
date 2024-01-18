from fastapi import FastAPI, Depends
from pydantic import BaseModel

from app import models
from app.database import engine, SessionLocale
from typing import Annotated
from sqlalchemy.orm import Session

from app.models import Music

app = FastAPI()


def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class MusicForm(BaseModel):
    title: str
    author: str
    genre: str


@app.get('/')
async def musics(db: db_dependency):
    return db.query(Music).all()


@app.post('/create')
async def create_music(db: db_dependency, music_form: MusicForm = Depends()):
    music_model = Music(**music_form.__dict__)

    db.add(music_model)
    db.commit()

    return music_model


models.Base.metadata.create_all(bind=engine)
