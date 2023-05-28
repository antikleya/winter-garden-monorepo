from fastapi_users.db import SQLAlchemyBaseUserTable
from app.database import Base
from sqlalchemy import Column, Integer


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
