import string
import random

BASE_URL = "http://localhost:8000/"

# temporary storage
url_database = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code


def create_short_url(long_url):
    code = generate_short_code()

    # store mapping
    url_database[code] = long_url

    short_url = BASE_URL + code

    return {
        "long_url": long_url,
        "short_url": short_url,
        "code": code
    }


def get_long_url(code):
    return url_database.get(code)
