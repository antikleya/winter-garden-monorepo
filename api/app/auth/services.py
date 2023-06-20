from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import Depends
from app.auth.schemas import CodeRead
from app.database import get_async_session
from app.auth.models import User, Code
from datetime import datetime, timedelta
from app.config import TZ
from secrets import token_urlsafe

WEEK = timedelta(days=7)
TOKEN_LENGTH = 25


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def generate_code(user: User, db: AsyncSession) -> CodeRead:
    end_time = int((datetime.now(tz=TZ) + WEEK).timestamp())
    new_code = token_urlsafe(TOKEN_LENGTH)
    code = Code(ends_at=end_time, code=new_code)
    code.user = user
    try:
        db.add(code)
    except IntegrityError:
        await db.rollback()
        new_code = token_urlsafe(TOKEN_LENGTH)
        code = Code(ends_at=end_time, code=new_code)
        code.user = user
        db.add(code)
    await db.commit()
    await db.refresh(code)

    return CodeRead.from_orm(code)
