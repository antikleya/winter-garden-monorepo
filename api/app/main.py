from fastapi import FastAPI
from app.auth.router import authRouter

app = FastAPI()

app.include_router(authRouter)
