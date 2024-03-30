from pydantic import BaseModel
import secrets
import string
import requests
import random


class PasswordRequest(BaseModel):
    length: int
    criteria1: str
    criteria2: str


def generate_password(length: int, criteria1: str, criteria2: str) -> str:
    """Generate a secure password."""
    if length <= 8 or not isinstance(length, int):
        raise ValueError(
            "Password must be an integer and length greater than 8 ")

    if criteria1 == criteria2:
        raise ValueError("Both criterials should be unique")

    if len(criteria1) == 0 or len(criteria2) == 0:
        raise ValueError("Provide unique additional criteria")

    chars = criteria1 + criteria2 + string.punctuation
    # chars = string.ascii_letters + criteria1 + criteria2

    return ''.join(secrets.choice(chars) for i in range(length))


def get_weather(city: str):
    API_KEY = '8d7cc46793b6442e9c2153422230112'
    BASE_URL = 'http://api.weatherapi.com/v1'
    CITY = city

    url = BASE_URL + '/current.json' + '?' + 'key=' + API_KEY + '&q=' + CITY

    response = requests.get(url).json()
    return response
