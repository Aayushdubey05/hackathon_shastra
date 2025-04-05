from fastapi import FastAPI
from databaseDesign import database,models,schemas
from databaseDesign.database import engine


async def lifespan(app: FastAPI):
    print("Server is starting")
    yield
    print("Server is stopped ")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
    return {"message":"Home route"}
