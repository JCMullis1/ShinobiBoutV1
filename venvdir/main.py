from sqlite3 import Timestamp
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange
from operator import itemgetter


app = FastAPI()

class Account(BaseModel):
    username: str
    email: str
    password: str

my_accounts = [{"username": "username of account 1", "email": "email of account 1", "password": "password of account 1", "id": 0}]

def find_account(indexint):
    idlist = list(map(itemgetter('id'), my_accounts))
    try:
        if indexint == idlist[int(indexint)]:
            global selected_account
            selected_account = my_accounts[indexint]
            print(f"Here is account {indexint}")
    except:
        print(f"Post with id of {indexint} is not available for some reason")

@app.post("/accounts")
def accountreader(new_account: Account):
    print(new_account)
    account_dict = new_account.dict()
    account_dict['id'] = randrange(0, 10000000)
    my_accounts.append(account_dict)
    print(my_accounts)
    return {"data": account_dict}

@app.get("/accounts")
def get_accounts():
    return {"data": my_accounts}

@app.get("/accounts/{id}")
def get_account(id): 
    find_account(int(id))
    return {"account_data": selected_account}
