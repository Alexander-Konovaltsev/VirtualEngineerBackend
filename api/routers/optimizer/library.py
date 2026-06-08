from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_optimizer_db
from schemas.optimizer.low_poly_model import LowPolyModelResponse
from models.optimizer.low_poly_model import LowPolyModel
from crud.optimizer.library import get_library
from fastapi.responses import FileResponse
import os
from pathlib import Path

router = APIRouter(prefix="/library", tags=["library"])

BASE_DIR = Path(__file__).resolve().parents[2]
MODELS_DIR = BASE_DIR / "low_poly_models"

@router.get("", response_model=list[LowPolyModelResponse])
def read_library(db: Session = Depends(get_optimizer_db)):
    return get_library(db)

@router.get("/{model_id}/download")
def download_model(model_id: int, db: Session = Depends(get_optimizer_db)):
    model = db.query(LowPolyModel).filter_by(id=model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Модель не найдена")

    file_path = MODELS_DIR / model.filename
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Файл не найден")

    return FileResponse(
        path=file_path,
        filename=model.filename,
        media_type="application/octet-stream"
    )
