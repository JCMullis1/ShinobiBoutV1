from sqlite3 import Timestamp
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

class Account(BaseModel):
    username: str
    email: str
    password: str

my_accounts = [{"username": "username of account 1", "email": "email of account 1", "password": "password of account 1", "id": 1}]

@app.post("/accounts")
def accountreader(new_account: Account):
    print(new_account)
    my_accounts.append(new_account)
    print(my_accounts)
    return {"data": new_account}

@app.get("/accounts")
def get_accounts():
    return {"data": my_accounts}