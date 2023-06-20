from fastapi import Header, HTTPException
from app.config import ACCESS_HEADER


def authorized_source(x_token: str | None = Header()):
    if x_token != ACCESS_HEADER:
        raise HTTPException(403, 'This endpoint requires a special token')
