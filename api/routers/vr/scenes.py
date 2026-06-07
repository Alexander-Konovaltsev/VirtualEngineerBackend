from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_vr_db
from crud.vr.scene import get_scenes
from crud.vr.model import get_models_by_scene_id, get_all_models_by_scene_id
from schemas.vr.scene import SceneResponse
from schemas.vr.model import ModelResponse
from dependencies.auth import get_current_user

router = APIRouter(prefix="/scenes", tags=["scenes"])

@router.get("", response_model=list[SceneResponse])
def read_scenes(db: Session = Depends(get_vr_db), user: dict = Depends(get_current_user)):
    scenes = get_scenes(db)
    return scenes

@router.get("/{scene_id}/models", response_model=list[ModelResponse])
def get_models_by_scene(scene_id: int, db: Session = Depends(get_vr_db), user: dict = Depends(get_current_user)):
    models = get_models_by_scene_id(db, scene_id)
    return models

@router.get("/{scene_id}/models/all", response_model=list[ModelResponse])
def get_all_models_by_scene(scene_id: int, db: Session = Depends(get_vr_db), user: dict = Depends(get_current_user)):
    models = get_all_models_by_scene_id(db, scene_id)
    return models
