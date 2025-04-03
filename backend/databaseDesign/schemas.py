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
    
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_toke: str
    token_type: str
    
class TokenData(BaseModel):
    email: Optional[str] = None