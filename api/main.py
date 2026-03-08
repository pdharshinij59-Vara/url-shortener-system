from fastapi import FastAPI
from pydantic import BaseModel
from services.shortener import create_short_url

app = FastAPI()

class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "URL Shortener System Running"}


@app.post("/shorten")
def shorten_url(request: URLRequest):
    result = create_short_url(request.url)
    return result
