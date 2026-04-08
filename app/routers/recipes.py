from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep, IsUserLoggedIn, get_current_user, is_admin
from app.models.models import Recipe
from sqlmodel import select

router = APIRouter(prefix="/api/recipes", tags=["recipes"])

@router.get("/")
def get_recipes(db: SessionDep):
    return db.exec(select(Recipe)).all()

@router.get("/{recipe_id}")
def get_recipe(recipe_id: int, db: SessionDep):
    recipe = db.get(Recipe, recipe_id)
    
    if not recipe:
        return {"error":"Recipe not found"}

    return recipe

@router.post("/")
def create_recipe(recipe: Recipe, db: SessionDep):
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, updated_recipe: Recipe, db: SessionDep):
    recipe = db.get(Recipe, recipe_id)
    if not recipe:
        return {"error":"Recipe not found"}
    
    for key, value in updated_recipe.dict().items():
        setattr(recipe, key, value)
    
    db.commit()
    db.refresh(recipe)
    return recipe

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: SessionDep):
    recipe = db.get(Recipe, recipe_id)
    if not recipe:
        return {"error":"Recipe not found"}
    
    db.delete(recipe)
    db.commit()
    return {"message":"Recipe deleted"}
