from fastapi import FastAPI , APIRouter

base_router= APIRouter()
 
@app.get("/")
def welcome():
    return {
        "message": "Hello All"
    }