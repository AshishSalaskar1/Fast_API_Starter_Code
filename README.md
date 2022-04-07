# Fast API

> **Official Documentation:** [https://fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial)
> 

### Installation

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install python-multipart
pip install pydantic
```

### Starter Code

- **Default Port**
    
    Execution : $ uvicorn main:app --reload
    
    ```python
    from fastapi import FastAPI, Form, File, UploadFile
    
    app = FastAPI()
    
    @app.get("/")
    def hello():
        return {"Message":"Hello from API"}
    ```
    
- **Custom Port**
    
    Execution: $ python file_name.py
    
    ```python
    from fastapi import FastAPI, Form, File, UploadFile
    
    app = FastAPI()
    
    @app.get("/")
    def hello():
        return {"Message":"Hello from API"}
    
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8032)
    ```
    
<hr>

## Fast API Code References
<hr>

### Path Parameters

```python
# Path params
@app.get("/get_age/{birth_year}")
def get_age(birth_year: int):
    return {"Age": 2022-birth_year}
```
<br>

### Query Parameters

- When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

```python
# Query Params
@app.post("/add_user_qp")
def try_query_parmas(qp_name: str, qp_age: int):
    return {"Message": f'User Added with name {qp_name} and age {qp_age}'}
```
<br>

### Passing Path Param + Request Body

- In the defined function call `last argument` holds the request data. Method arguments before last_argument can map to the path_parameters
- In case only req_body is needed → You can only pass 1 param in function
- Only PUT and POST method

```python
# Data is sent as Request Body
@app.put("/add_user/{user_id}")
def add_user(user_id: str, user_data: Person):
    return {"Message": f'User Added with name {user_data.name} and age {user_data.age}'}
```
<br>

### **Request body + path + query parameters**

```python
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

The function parameters will be recognized as follows:

- If the parameter is also declared in the **path**, it will be used as a path parameter.
- If the parameter is of a **singular type** (like `int`, `float`, `str`, `bool`, etc) it will be interpreted as a **query** parameter.
- If the parameter is declared to be of the type of a **Pydantic model**, it will be interpreted as a request **body**.

<br>

### Form Data

```python
from fastapi import FastAPI, Form
@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "message": "Succesfully Logged in"}
```

```html
<form action="http://127.0.0.1:8000/login" method="post">
        <label for="username">Username: </label>
        <input type="text" name="username" id=""> <br>
        <label for="password">Password: </label>
        <input type="text" name="password" id=""> <br>

        <input type="submit" value="Submit">
</form>
```
<br>

### jsonable_encoder

- There are some cases where you might need to convert a data type (like a Pydantic model) to something compatible with JSON (like a `dict`, `list`, etc).
- In this example, it would convert the Pydantic model to a `dict`, and the `datetime` to a `str`
.

```python
@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
```
<br>

### **CORS (Cross-Origin Resource Sharing)**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
<br>

### Uploading Files & Saving

- [https://levelup.gitconnected.com/how-to-save-uploaded-files-in-fastapi-90786851f1d3](https://levelup.gitconnected.com/how-to-save-uploaded-files-in-fastapi-90786851f1d3)

```python
from fastapi import FastAPI, File, UploadFile

@app.post("/upload_file")
def image(uploaded_file: UploadFile = File(...)):
		filename = uploaded_file.filename
    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    
    return {"filename": uploaded_file.filename}
```

<hr><hr>

## General Tips

- **Interactive API Docs** : [localhost:8000/](http://localhost:8000/)`docs`
- **Alternative API Docs** : [localhost:8000/](http://localhost:8000/)`redoc` [Swagger Doc]
- **PyDantic & Hint Types**
    
    ```python
    from pydantic import BaseModel
    
    # Create custom data type for hint checking
    class Person(BaseModel):
        age: int
        name: str
        gender: Optional[str] = None
    
    def test_function(name: str, age: float) -> str:
    		return "SOME STRING"
    ```
    
- **Uvicorn Server**
    - Its an **ASGI** [Asynchronous Server Gateway Interface] Server
    - Previously Flask used **WSGI** [Web Gatewat Interface] server
- **HTTP Methods**
    1. GET → Get some data 
    2. POST→ Create a new resource 
    3. PUT → Update resource
    4. DELETE → Delete data
