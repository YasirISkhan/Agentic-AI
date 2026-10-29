from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Hello World'}

@app.get("/about")
def my_app():
    return {'Message': 'Welcome to My Company'}

@app.get("/data")
def data():
    with open('patients.json') as f:
        data = json.load(f)
        return data