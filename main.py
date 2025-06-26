from fastapi import FastAPI, APIRouter, staticfiles
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import bg_remove_routes



APP = FastAPI(title="Server")

APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# routes
APP.include_router(bg_remove_routes.route)
APP.mount("/static", staticfiles.StaticFiles(directory="static/"), name="static")


@APP.get("/")
async def welcome():
    return {"message":"Welcome to server"}