from sqlalchemy import Column, Integer, String
from blog.database import Base


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255))
    username = Column(String(255))
    age = Column(String(40))
    email = Column(String(255))
    password = Column(String(255))
    