from sqlmodel import Field, SQLModel,Relationship
from typing import Optional
from app.models.user import User

class UserExercise(SQLModel, table =True):
    id:int = Field(primary_key = True)
    routine_id: Optional[int] = Field(foreign_key="routine.id")#
    exercise_id: Optional[int] = Field(foreign_key="exercise.id")

class Routine(SQLModel, table = True):
    id:int = Field(primary_key = True)
    exercises:list["Excercise"] = Relationship(back_populates = "routines",
                                               link_model = UserExercise)

class Excercise(SQLModel, table = True):
    id:int = Field(primary_key = True)
    name:str
    type:str
    muscle:str
    difficulty:Optional[str]
    instructions:Optional[str]
    equip1:Optional[str] |None##
    equip2:Optional[str] |None
    equip3:Optional[str] |None
    safety:Optional[str]
    routines:list["Routine"] =Relationship(back_populates = "exercises",
                                        link_model = UserExercise)


    
class userMeal(SQLModel, table = True):
    user_id:int = Field(foreign_key = "user.id", primary_key=True)
    meal_id:int = Field(foreign_key = "meal.id", primary_key=True)

class Meal(SQLModel, table = True):
    id:int = Field(primary_key = True)
    recipes: list["Recipe"] = Relationship(back_populates="meals",link_model=userMeal   )

class Recipe(SQLModel, table = True):
    id:int = Field(primary_key = True)
    name:Optional[str]
    calories:float
    protein_g:float
    serving_size_g:Optional[float]
    fat_total_g:Optional[float]
    fat_saturated:Optional[float]
    sodium_mg:Optional[int]
    potassium_mg:Optional[int]
    cholesterol_mg:Optional[int]
    carb_total_g:Optional[float]
    fiber_g:Optional[float]
    sugar_g:Optional[float]
    meal: list["Meal"] = Relationship(back_populates="recipe",link_model=userMeal )
    
