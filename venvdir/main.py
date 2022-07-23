from sqlite3 import Timestamp
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

class Account(BaseModel):
    username: str
    email: str
    password: str

@app.post("/createaccount")
def accountreader(payload: dict = Body(...)):
    print(payload)
    return {"new_account": f"username {payload['username']} email: {payload['email']} password {payload['password']}"}

@app.get("/Accounts/ID")
def accountreader():
    return {"username": username, "email": email, "password": password}
