from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.utilities.flash import get_flashed_messages
from jinja2 import Environment, FileSystemLoader
from app.config import get_settings


template_env = Environment(loader = FileSystemLoader("app/templates",), )
template_env.globals['get_flashed_messages'] = get_flashed_messages
templates = Jinja2Templates(env=template_env)
static_files = StaticFiles(directory="app/static")

router = APIRouter(tags=["Jinja Based Endpoints"], include_in_schema=get_settings().env.lower() in ["dev","development"])
api_router = APIRouter(tags=["API Endpoints"], prefix="/api")

from . import (index, login, register, admin_home, user_home, users, logout,
               workout,trackcalories,routines,recipes,exercise,
               
               )
#include any extra routes in there so it can be accessed outside the folder