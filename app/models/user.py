from sqlmodel import Field, SQLModel
from typing import Optional
from pydantic import EmailStr


class UserBase(SQLModel,):
    username: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str
    role:str = ""

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    height:Optional[int]
    weight:Optional[int]
    hip_width:Optional[int]
    neck_width:Optional[int]
    age:Optional[int]
    gender:Optional[str]
    calorie_goal:Optional[float]