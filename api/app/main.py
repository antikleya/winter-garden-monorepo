from fastapi import FastAPI
from app.auth.router import authRouter
from app.configService.router import configRouter
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app = FastAPI(prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=authRouter)
app.include_router(router=configRouter)
