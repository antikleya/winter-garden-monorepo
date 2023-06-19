from typing import AsyncGenerator, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.config import DATABASE_SYNC_URL, DATABASE_ASYNC_URL

Base = declarative_base()

sync_engine = create_engine(DATABASE_SYNC_URL)
async_engine = create_async_engine(DATABASE_ASYNC_URL)

sync_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


def get_sync_session() -> Generator[Session, None, None]:
    with sync_session_maker() as session:
        yield session
