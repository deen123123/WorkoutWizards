from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep, IsUserLoggedIn, get_current_user, is_admin
from . import router, templates

#jinja endpoint to return the workout template
@router.get("/recipes", response_class=HTMLResponse)
async def get_workout(
    user:AuthDep, db:SessionDep, request:Request
):
    return templates.TemplateResponse(
        request= request,
        name = "recipes.html",
        context = {

            "user":user
        }
    )