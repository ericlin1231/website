from fastapi import FastAPI

from api import auth, users

app = FastAPI(
    title="Backend API",
    version="0.1.0",
)

app.include_router(auth.router)
app.include_router(users.router)
