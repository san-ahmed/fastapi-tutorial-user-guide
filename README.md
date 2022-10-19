# Recap - FastAPI User Guide (Tutorial)

## First Steps

- Import FastAPI.
- Create an app instance.
- Write a path operation decorator (like @app.get("/")).
- Write a path operation function (like def root(): ... above).
- Run the development server (like uvicorn main:app --reload).

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## Path Parameters

With FastAPI, by using short, intuitive and standard Python type declarations, you get:

- Editor support: error checks, autocompletion, etc.
- Data "parsing"
- Data validation
- API annotation and automatic documentation
- And you only have to declare them once.

That's probably the main visible advantage of FastAPI compared to alternative frameworks (apart from the raw performance).
```
from fastapi import FastAPI

myapp = FastAPI()

users = {0:"Ahmed", 1:"Ghassen", 2:"Achref", 3:"Hatem", 4:"Fedi"}

@myapp.get("/users")
async def read_users():
    """Endpoint to read users"""
    return users

@myapp.get("/users/me")
async def read_user_me():
    """ Endpoint to read the current user."""
    return {"user": users[0]}

@myapp.get("/users/{user_id}")
async def read_user(user_id: int):
    """ Endpoint to read a user."""
    return {"user": users[user_id]}
```
```
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

```

## Query Parameters

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters. The query is the set of key-value pairs that go after the `?` in a URL, separated by `&` characters.

As they are part of the URL, they are "naturally" strings. But when you declare them with Python types they are converted to that type and validated against it.-> All the same process that applied for path parameters also applies for query parameters:

   - Editor support (obviously)
   - Data "parsing"
   - Data validation
   - Automatic documentation
   - You could also use Enums the same way as with Path Parameters.

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

```

In this case, there are 3 query parameters:

   - `needy`, a required `str`.
   - `skip`, an `int` with a default value of `0`.
   - `limit`, an optional `int`.

Request URL: `http://127.0.0.1:8000/items/1?needy=Ahmed&limit=10`

Response body: 
```
{"item_id": "1",
  "needy": "Ahmed",
  "skip": 0,
  "limit": 10}
```