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