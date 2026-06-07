from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_optimizer_db
from schemas.optimizer.low_poly_model import LowPolyModelResponse
from crud.optimizer.library import get_library

router = APIRouter(prefix="/library", tags=["library"])

@router.get("", response_model=list[LowPolyModelResponse])
def read_library(db: Session = Depends(get_optimizer_db)):
    return get_library(db)
