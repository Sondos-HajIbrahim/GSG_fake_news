from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

class UserLogin(BaseModel):
    email: str
    password: str

class UserLoginResponse(BaseModel):
    access_token: str

class NewsBase(BaseModel):
    title: str
    text: str
    added_by: str
    fake: bool

class News(NewsBase):
    id: int