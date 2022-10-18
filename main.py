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