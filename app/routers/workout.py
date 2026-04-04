from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status
from sqlmodel import select
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep, IsUserLoggedIn, get_current_user, is_admin
from app.models.models import Routine
from . import router, templates

#jinja endpoint to return the workout template
@router.get("/workout", response_class=HTMLResponse)
async def get_workout(
    user:AuthDep, db:SessionDep, request:Request
):
    getUserRoutines = db.exec(select(Routine).where(Routine.user_id == user.id)).all()
    return templates.TemplateResponse(
        request= request,
        name = "workout.html",
        context = {
           "routines":getUserRoutines, 
            "user":user
        }
    )