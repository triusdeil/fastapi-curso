from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#models
class ItemModel(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
async def root():
    return 'hello world'

@app.get('/hola')
async def root():
    return ' world'

@app.get('/items/{item.id}')
async def read_item(item_id: int, q:Union[str, None] = None):
    return {"item_id":item_id, 'q':q}

@app.get('/calculadora')
async def calcular(operando1: float, operando2: float):
    return {"suma :", operando2 + operando1}

@app.put('/items/{item.id}')
async def update_item(item_id: int, item: ItemModel):
    return {'item_name': item.name, 'item_id': item_id}