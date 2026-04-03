from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form
from app.dependencies.session import SessionDep
from . import api_router
from app.services.user_service import UserService
from app.dependencies.auth import AuthDep
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.schemas import UserResponse
from . import router, templates

# API endpoint for listing users
@api_router.get("/users", response_model=list[UserResponse])
async def list_users(request: Request, db: SessionDep):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    return user_service.get_all_users()

@api_router.get("/app")
async def get_user(request:Request, db:SessionDep, user:AuthDep):

    return templates.TemplateResponse(
            request = Request,
            name = "app.html",
            context ={
                "get_user":user
            }
    )
