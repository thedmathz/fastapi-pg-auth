from fastapi import FastAPI
from app.api import routes_authentication
from app.api import routes_user
from app.api import routes_configuration

app = FastAPI()

app.include_router(routes_authentication.router, tags=["Authentication"])
app.include_router(routes_user.router, prefix="/users", tags=["Users"])
app.include_router(routes_configuration.router, prefix="/configurations", tags=["Configurations"])