from typing import Optional

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import HTTPException, Request, status, Form,Query
from sqlmodel import select
from app.dependencies.session import SessionDep
from . import api_router
from app.services.user_service import UserService
from app.dependencies.auth import AuthDep
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.schemas import UserResponse
from app.models.models import Exercise,Routine,RoutineExercise
from . import router, templates
import requests
import os
from dotenv import load_dotenv#new imports to hide api key
load_dotenv()
API_KEY_EXERCISES = os.getenv("API_KEY_EXERCISE")
# API endpoint to get all the exercises

  #route to return the api data to be displayed to the user   
@api_router.get("/exercises")
async def get_exercises(user:AuthDep,db:SessionDep, request:Request,
                        muscle = Query()):
    
    if muscle:
        response = requests.get(
            "https://api.api-ninjas.com/v1/exercises",
            headers={"X-Api-Key": API_KEY_EXERCISES},
            params={"muscle": muscle}
        )
        
        exercises = response.json()
    exercise_list = []
    for e in exercises:
        exist = db.exec(
            select(Exercise).where(Exercise.name == e["name"])
        ).one_or_none()
       
        if not exist:

            exercise = Exercise(
                name=e["name"],
                    type=e.get("type", ""),
                    muscle=e.get("muscle", ""),
                    difficulty=e.get("difficulty"),
                    instructions=e.get("instructions"),
            )
           
            db.add(exercise)
        exercise_list.append(exist) 
    db.commit()
    print(exercise_list)
    return templates.TemplateResponse(
        request = request,
        name = "routines.html",
        context = {
            "user":user,
              "exercises": exercises,
              "exercise_db":exercise_list,
                "muscle": muscle,
                
            }
    )
    

#endpoints to manipulate data in the tables

#list all routines for a  user
@router.get("/routines")
def list_routines(request: Request, user_id: int, db:SessionDep):
    routines = db.exec(select(Routine).where(Routine.user_id == user_id)).all()
    return templates.TemplateResponse("routines/list.html", {
        "request": request,
        "routines": routines
    })



#endpoint to add exercise
@router.post("/add_exercise/")
async def add_exercise_toroutine(user:AuthDep, db:SessionDep, request:Request,
                      routine_id = Form(), exercise_id = Form(),
                      name = Form(), type = Form(), muscle = Form(), 
                        difficulty = Form()
                        ):   
    exercise = db.get(Exercise,exercise_id)
    routine = db.get(Routine,routine_id)
    model_exercise = RoutineExercise(
        routine_id = routine_id,
        exercise_id = exercise_id)
    
    db.add(model_exercise)
    db.commit()
    db.refresh(model_exercise)
    flash(request, message = "Workout added to Your Routine")
    redirect_url = f"/api/exercises?muscle={muscle}"
    return RedirectResponse(
          url= redirect_url, status_code=status.HTTP_303_SEE_OTHER)

#endpoint to get all exercises for that routine id
@router.get("/get-routine/{routine_id}", response_model=list[Exercise])
async def view_routine(user:AuthDep, routine_id: int, db:SessionDep, request:Request):
    routine = db.get(Routine, routine_id)
    if not routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    # load exercises
    exercises = routine.exercises
    return templates.TemplateResponse(
        request = request,
        name = "routines/detail.html",
        context = {
        "routine": routine,
        "exercises": exercises
    })

@router.post("/update-routines", response_model=RoutineExercise)
def update_routine_exercise(user:AuthDep, db:SessionDep,request:Request,routine_id: int, exercise_id: int, sets: Optional[int] = None,
                            reps: Optional[int] = None, rest_time: Optional[int] = None
                            ):
    
    routine_exercise = db.get(RoutineExercise, (routine_id, exercise_id))
    if not routine_exercise:
        raise HTTPException(status_code=404, detail="Exercise in routine not found")
    if sets is not None:
        routine_exercise.sets = sets
    if reps is not None:
        routine_exercise.reps = reps
    if rest_time is not None:
        routine_exercise.rest_time = rest_time
    db.add(routine_exercise)
    db.commit()
    db.refresh(routine_exercise)
    flash(request, "Exercise Updated In That Routine")
    return templates.TemplateResponse(
        request = request,
        name = "workout.html",
        context = {
        "routine": routine_exercise.routine,#gets a routine object from the backpopulates
        "exercises": routine_exercise.routine.exercises
        #gets the exercises from the backpopulates relationship
    })