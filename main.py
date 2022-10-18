from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/")
async def root():
    """Main endpoint """
    return {"message":"Welcome to this tutorial user guide"}