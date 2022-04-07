import re
from typing import Optional
from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import shutil
import uvicorn

# Create custom data type for hint checking
class Person(BaseModel):
    age: int
    name: str
    gender: Optional[str] = None


app = FastAPI()

# ALLOW CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET Method
@app.get("/")
def hello():
    return {"Message":"Hello from API"}


# Path params
@app.get("/get_age/{birth_year}")
def get_age(birth_year: int):
    return {"Age": 2022-birth_year}

# Query Params
@app.post("/add_user_qp")
def try_query_parmas(qp_name: str, qp_age: int):
    return {"Message": f'User Added with name {qp_name} and age {qp_age}'}


# Request Body
@app.post("/add_user")
def add_user(req_body: Person):
    return {"Message": f'User Added with name {req_body.name} and age {req_body.age} and Gender {req_body.gender}'}

# Form Data
@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "message": "Succesfully Logged in"}


# File Upload
@app.post("/upload_file")
def image(uploaded_file: UploadFile = File(...)):
    filename = uploaded_file.filename
    with open("temp/"+filename, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    
    return {"filename": uploaded_file.filename}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8032)