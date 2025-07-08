from fastapi import FastAPI
from app.api import routes_user

app = FastAPI()

app.include_router(routes_user.router)