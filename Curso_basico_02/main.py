from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def hello_world():
    return { "hello" : "world" }

@app.get('/{id}')
def hello_world(id: int):
    return { "hello" : id }