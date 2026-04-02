from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form
from app.dependencies.session import SessionDep
from . import router, templates
from app.services.auth_service import AuthService
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.config import get_settings

# View route responsible for UI
@router.get("/login", response_class=HTMLResponse)
async def login_view(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="login.html",
    )

#Action route responsible for actually logging in the person
@router.post("/login", response_class=HTMLResponse)
async def login_action_ajax(
    db: SessionDep,
    request: Request,
    username: str = Form(),
    password: str = Form(),
):
    user_repo = UserRepository(db)
    auth_service = AuthService(user_repo)
    access_token =auth_service.authenticate_user(username, password)
    if not access_token:
        flash(request, "Incorrect username or password", "danger")
        return RedirectResponse(url=request.url_for("login_view"), status_code=status.HTTP_303_SEE_OTHER)
    
    response = RedirectResponse(url=request.url_for("index_view"), status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="none",
        secure=True,
    )
    return response
