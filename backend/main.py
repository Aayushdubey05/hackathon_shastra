from fastapi import FastAPI,HTTPException



async def lifespan(app: FastAPI):
    print("Server is starting")
    yield
    print("Server is stopped ")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
    return {"message":"Home route"}