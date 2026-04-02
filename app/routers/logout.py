from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form
from app.dependencies.session import SessionDep
from . import router, templates
from app.services.auth_service import AuthService
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.config import get_settings

# View route responsible for UI
@router.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(url=request.url_for("login_view"), status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(
        key="access_token", 
        httponly=True,
        samesite="none",
        secure=True
    )
    return response