from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import Field

class User(Base):
    __tablename__ = "users"

    name = Column(String, default=None)
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    address = relationship("Address", back_populates="user", cascade="all, delete", passive_deletes=True,)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="address")

    # def __repr__(self) -> str:
    #     return f"Address(id={self.id!r}, email_address={self.email_address!r})"