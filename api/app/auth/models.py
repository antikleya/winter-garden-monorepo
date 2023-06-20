from fastapi_users.db import SQLAlchemyBaseUserTable
from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)

    codes = relationship("Code", back_populates="user")


class Code(Base):
    __tablename__ = 'codes'

    code = Column(String, primary_key=True)
    ends_at = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="codes")
