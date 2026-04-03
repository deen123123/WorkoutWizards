from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form,Query
from app.dependencies.session import SessionDep
from . import api_router
from app.services.user_service import UserService
from app.dependencies.auth import AuthDep
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.schemas import UserResponse
from app.models.models import Exercise
from . import router, templates
import requests
import os
from dotenv import load_dotenv#new imports to hide api key
load_dotenv()
API_KEY_EXERCISE = os.getenv("API_KEY_EXERCISE")
# API endpoint to get all the exercises
@api_router.post("/add_exercise")
async def add_exercise(user:AuthDep, db:SessionDep, request:Request,
                      name = Form(), type = Form(), muscle = Form(),  difficulty = Form()
                        ):   
    
    model_exercise = Exercise(name = name, type = type, muscle = muscle,
                            difficulty = difficulty)
    db.add(model_exercise)
    db.commit()
    flash(request, message = "Workout added to Your Routine")
    return RedirectResponse(
          url= "/workout", status_code=status.HTTP_303_SEE_OTHER)
     
@api_router.get("/exercises")
async def get_exercises(user:AuthDep,db:SessionDep, request:Request,
                        muscle = Query()):
    exercises = []
    if muscle:
        response = requests.get(
            "https://api.api-ninjas.com/v1/exercises",
            headers={"X-Api-Key": API_KEY_EXERCISE},
            params={"muscle": muscle}
        )
        
        exercises = response.json()

    return templates.TemplateResponse(
        request = request,
        name = "routines.html",
        context = {
            "user":user,
              "exercises": exercises,
                "muscle": muscle
            }
    )
    
