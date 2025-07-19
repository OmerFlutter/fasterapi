from pydantic import BaseModel, EmailStr, conint
from pydantic.types import conint
from datetime import datetime
from typing import Optional

class BaseUser(BaseModel):
    email: EmailStr
    password: str

class CreateUser(BaseUser):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(BasePost):
    pass

class PostResponse(BasePost):
    id: int
    created_at: datetime
    creator_id: int
    votes: int = 0
    creator: UserResponse

    class Config:
        from_attributes: True


class PostOut(BaseModel):
    post: PostResponse
    votes: int

    class Config:
        from_attributes = True



class LoginUser(BaseModel):
    email: EmailStr
    password: str

class AccessToken(BaseModel):
    access_token: str
    token_type: str = "Bearer"

class TokenData(BaseModel):
    id: Optional[int] = None



class Vote(BaseModel):
    post_id: int
    dir: int = conint(le=1)
