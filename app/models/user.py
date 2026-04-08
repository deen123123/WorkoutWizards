from sqlmodel import Field, SQLModel,Relationship
from typing import Optional, TYPE_CHECKING
from pydantic import EmailStr
if TYPE_CHECKING:
    from .models import Routine, Meal

class UserBase(SQLModel,):
    username: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str
    role:str = ""

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    height_m:Optional[int] = 0
    weight_kg:Optional[int] = 0
    hip_width:Optional[int] = 0
    neck_width:Optional[int] = 0
    age:Optional[int] = 0
    gender:Optional[str] = 0
    calorie_goal:Optional[float] = 0
    routines: list["Routine"] = Relationship(back_populates="user")
    meals: list["Meals"] = Relationship(back_populates="user")
    
    user_bmi:Optional[float] = 0
    #call this method to calculate the userBMI and just pass the value it returns
    #in the attribute above
    def calculate_bmi(self):
        return self.weight_kg/(self.height_m*self.height_m)
