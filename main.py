from fastapi import FastAPI, HTTPException, Request, Query
from script import PasswordRequest, generate_password
import requests

app = FastAPI()


@app.post("/generate-password")
def generate_password_endpoint(password_request: PasswordRequest):
    try:
        length = password_request.length
        criteria1 = password_request.criteria1
        criteria2 = password_request.criteria2

        password = generate_password(length, criteria1, criteria2)

        return {"password": password, "length": length}
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
