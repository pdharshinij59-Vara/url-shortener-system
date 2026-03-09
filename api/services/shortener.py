import string
import random
from sqlalchemy.orm import Session
from database.models import URL

BASE_URL = "http://localhost:8000/"


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code


def create_short_url(db: Session, long_url: str):

    code = generate_short_code()

    db_url = URL(
        long_url=long_url,
        short_code=code
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    short_url = BASE_URL + code

    return {
        "long_url": long_url,
        "short_url": short_url,
        "code": code
    }


def get_long_url(db: Session, code: str):

    url = db.query(URL).filter(URL.short_code == code).first()

    if url:
        return url.long_url

    return None
