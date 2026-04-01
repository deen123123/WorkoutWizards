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
    height_m:Optional[int]
    weight_kg:Optional[int]
    hip_width:Optional[int]
    neck_width:Optional[int]
    age:Optional[int]
    gender:Optional[str]
    calorie_goal:Optional[float]
    user_bmi:Optional[float]
    def calculate_bmi(self):
        return weight_kg/(height_m*height_m)
