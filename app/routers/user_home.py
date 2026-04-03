from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep, IsUserLoggedIn, get_current_user, is_admin
from . import router, templates


@router.get("/app", response_class=HTMLResponse)
async def user_home_view(
    request: Request,
    user: AuthDep,
    db:SessionDep
):
    return templates.TemplateResponse(
        request=request, 
        name="app.html",
        context={
            "user": user
        }
    )
@router.get("/authenticated-base", response_class = HTMLResponse)
async def auth_base(
    user:AuthDep,db:SessionDep,request:Request
):
    return templates.TemplateResponse(
        request = request,
        name = "authenticated-base.html",
        context = {
            "user":user
        }
    )