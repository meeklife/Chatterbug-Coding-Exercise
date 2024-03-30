from fastapi import FastAPI, HTTPException, Request, Query
from script import PasswordRequest, generate_password
import requests

app = FastAPI()
