from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_vr_db
from dependencies.auth import get_current_user
from schemas.vr.user_model_view import UserModelViewCreateRequest, UserModelViewResponse
from crud.vr.user_model_view import create_user_model_view, get_user_models_views_by_scene_id
from crud.vr.scene import get_scene_by_id
from crud.vr.model import get_model_by_id

router = APIRouter(prefix="/models-views", tags=["models-views"])

@router.post("/create", response_model=UserModelViewResponse)
def create_models_views(models_views_data: UserModelViewCreateRequest, 
                        db: Session = Depends(get_vr_db), 
                        user: dict = Depends(get_current_user)):
    if not get_scene_by_id(db, models_views_data.scene_id):
        raise HTTPException(status_code=422, detail="Сцена с таким id не существует")
    
    model = get_model_by_id(db, models_views_data.model_id)
    if not model:
        raise HTTPException(status_code=422, detail="Модель с таким id не существует")
    if not model.is_informational:
        raise HTTPException(status_code=422, detail="У модели отсутствует возможность просмотра")

    return create_user_model_view(db, models_views_data, user["user_id"])

@router.get("/{scene_id}", response_model=list[UserModelViewResponse])
def get_user_models_views_by_scene(scene_id:int, db: Session = Depends(get_vr_db), user: dict = Depends(get_current_user)):
    user_models_views = get_user_models_views_by_scene_id(db, user["user_id"], scene_id)
    return user_models_views
