from sqlalchemy.orm import Session
from models.role import Role
from enums.role import RoleName

def get_roles(db: Session):
    return db.query(Role).filter(
        Role.name != RoleName.ADMIN.value
    ).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(
        Role.id == role_id,
        Role.name != RoleName.ADMIN.value
    ).first()
