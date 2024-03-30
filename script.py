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

    return ''.join(secrets.choice(chars) for i in range(length))


def get_holiday(country: str, year: str, month: str, day: str):
    API_KEY = '08ee5e03738c41339c84e89d34e3e0ea'
    BASE_URL = 'https://holidays.abstractapi.com/v1/'

    url = BASE_URL + '?api_key=' + API_KEY + '&country=' + \
        country + '&year=' + year + '&month=' + month + '&day=' + day

    response = requests.get(url).json()
    return response
