from pydantic import BaseModel
from typing import Optional


class UserProfile(BaseModel):
    name: str
    username: str
    age: str
    email: str
    password: str
    
class ShowUserProfile(BaseModel):
    name: str
    username: str
    age: str
    email: str