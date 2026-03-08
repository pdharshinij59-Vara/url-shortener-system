from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from services.shortener import create_short_url, get_long_url

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


@app.get("/{code}")
def redirect_to_url(code: str):
    long_url = get_long_url(code)

    if long_url:
        return RedirectResponse(long_url)

    return {"error": "URL not found"}
