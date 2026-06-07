from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_vr_db
from crud.vr.role import get_roles
from schemas.vr.role import GetRolesResponse

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("", response_model=list[GetRolesResponse])
def read_roles(db: Session = Depends(get_vr_db)):
    return get_roles(db)
