from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

from services.shortener import create_short_url, get_long_url
from database.db import SessionLocal, init_db

app = FastAPI()

init_db()


class URLRequest(BaseModel):
    url: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "URL Shortener System Running"}


@app.post("/shorten")
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):
    result = create_short_url(db, request.url)
    return result


@app.get("/{code}")
def redirect_to_url(code: str, db: Session = Depends(get_db)):
    long_url = get_long_url(db, code)

    if long_url:
        return RedirectResponse(long_url)

    return {"error": "URL not found"}
