from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.config import DATABASE_SYNC_URL, DATABASE_ASYNC_URL

Base: DeclarativeMeta = declarative_base()

sync_engine = create_engine(DATABASE_SYNC_URL)
async_engine = create_async_engine(DATABASE_ASYNC_URL)

sync_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
