from sqlmodel import Field, SQLModel,Relationship
from typing import Optional



#NO LINK MODEL APPROACH FOR ROUTINEEXERCISE since attributes are added
class RoutineExercise(SQLModel, table =True):
   routine_id: int = Field(foreign_key="routine.id", primary_key = True)#
   exercise_id: int = Field(foreign_key="exercise.id", primary_key = True)
   sets: int = 0
   reps: int = 0
   rest_time: int = 0
   routine: Optional["Routine"] = Relationship(back_populates="exercises")
   exercise: Optional["Exercise"] = Relationship(back_populates="routines")
class Routine(SQLModel, table = True):
    id:int = Field(primary_key = True)
    name:str
    user_id:int = Field(foreign_key = "user.id")
    user: Optional["User"] = Relationship(back_populates = "routines")
    exercises: list["RoutineExercise"] = Relationship(back_populates="routine")

class Exercise(SQLModel, table = True):
    id:int = Field(primary_key = True)
    name:str
    type:str
    muscle:str
    difficulty:Optional[str]
    instructions:Optional[str]
    equip1:Optional[str] 
    equip2:Optional[str] 
    equip3:Optional[str] 
    safety:Optional[str]
    routines:list["RoutineExercise"] =Relationship(back_populates = "exercise")

  #USES LINK MODEL APPROACH for just the 2 keys  no attributes
class MealRecipe(SQLModel, table = True):
   recipe_id:int = Field(foreign_key = "recipe.id", primary_key=True)
   meal_id:int = Field(foreign_key = "meal.id", primary_key=True)
   

class Meal(SQLModel, table = True):
    id:int = Field(primary_key = True)
    name:str
    user_id:int = Field(foreign_key = "user.id")
    user: Optional["User"] = Relationship(back_populates = "meals")
    recipes: list["Recipe"] = Relationship(back_populates="meals",link_model=MealRecipe   )

class Recipe(SQLModel, table = True):
    id:int = Field(primary_key = True)
    name:str
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
    meals: list["Meal"] = Relationship(back_populates="recipes",link_model=MealRecipe )
    
