from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return 'hello world'

@app.get('/hola')
async def root():
    return ' world'