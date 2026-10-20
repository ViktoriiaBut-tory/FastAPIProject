from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to your first FastAPI project"}


@app.get("/welcome")
def welcome():
    return {"Msg": "Welcome to learning"}


@app.get("/students")
def getstudents():
    students = [
        {"id": "St01", "name": "John", "age": 16},
        {"id": "St02", "name": "Alice", "age": 19},
        {"id": "St03", "name": "Bob", "age": 22},
        {"id": "St04", "name": "Charli", "age": 21},
    ]
    return students


@app.get("/services")
def service():
    return {"message": "Our service"}
