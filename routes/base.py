from fastapi import APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
def welcome():
APP_NAME="mini-RAG"
    app_name = os.getenc('APP_NAME')
    app_versiom = os.getenv('APP_VERSION')

    return {
        'app_name': app_name,
        'app_version' : app_version 
    }
