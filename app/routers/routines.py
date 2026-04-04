from fastapi import APIRouter, Form, HTTPException, Depends, Request,Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status
from sqlmodel import select
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep, IsUserLoggedIn, get_current_user, is_admin
from app.models.models import Routine,RoutineExercise
from . import router, templates
from app.utilities.flash import flash
#jinja endpoint to return the workout template
@router.get("/routines", response_class=HTMLResponse)
async def get_workout(
    user:AuthDep, db:SessionDep, request:Request
):
    return templates.TemplateResponse(
        request= request,
        name = "routines.html",
        context = {

            "user":user
        }
    )

#endpoint to create a routine
@router.post("/routines/")
async def create_routine(user: AuthDep, db: SessionDep,request:Request,
                         name = Form()):
    routine = Routine(user_id=user.id,name = name,user = user)
    db.add(routine)
    db.commit()
    db.refresh(routine)
    getroutines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()
    flash(request, "Routine created! Now add Workouts to Routine")
    return templates.TemplateResponse(
        request = request,
        name = "routines.html",
        context = {
            "user":user,
            #"selected_routine_id":routine.id
            "routines":getroutines
        }
    )

@router.get("/exercises/")
async def create_routine(user: AuthDep, db: SessionDep,request:Request,
                         routine_id = Query()):
    routine = db.get(Routine,routine_id)

    getroutines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()

    return templates.TemplateResponse(
        request = request,
        name = "workout.html",
        context = {
            "user":user,
            #"selected_routine_id":routine.id
            "routines":getroutines,
            "exercises":routine.exercises
        }
    )

@router.post("/edit-exercises/")
async def edit_exercise(
    user: AuthDep,
    db: SessionDep,
    request: Request,
    routine_id: int = Query(),
    exercise_id: int = Query(),
    name: str = Form(...),
    muscle: str = Form(...),
    difficulty: str = Form(...)
):
    # Get routine
    routine = db.get(Routine, routine_id)

    # Get the specific exercise in the routine
    routine_ex = db.get(RoutineExercise, (routine_id, exercise_id))
    if not routine_ex:
        raise HTTPException(status_code=404, detail="Exercise not found in this routine")

    # Update exercise
    routine_ex.exercise.name = name
    routine_ex.exercise.muscle = muscle
    routine_ex.exercise.difficulty = difficulty

    db.add(routine_ex.exercise)
    db.commit()
    db.refresh(routine_ex.exercise)

    # Reload routines for template
    getroutines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()

    return templates.TemplateResponse(
        request=request,
        name="workout.html",
        context={
            "user": user,
            "routines": getroutines,
        }
    )
@router.post("/edit-routine-name/")
async def edit_exercise(
    user: AuthDep,
    db: SessionDep,
    request: Request,
    routine_id: int = Query(),
    name: str = Form(...), 
):
    # Get routine
    routine = db.get(Routine, routine_id)
    # Update exercise
    routine.name = name
   

    db.add(routine)
    db.commit()
    db.refresh(routine)

    # Reload routines for template
    getroutines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()
    flash(request,"Routine Name Updated")
    return templates.TemplateResponse(
        request=request,
        name="workout.html",
        context={
            "user": user,
            "routines": getroutines,
        }
    )