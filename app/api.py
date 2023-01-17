from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):

    name: str


@app.get('/')
def home():

    return {'msg': 'sucess'}

@app.post('/post')
def generate(user: User):

    print(user.name)