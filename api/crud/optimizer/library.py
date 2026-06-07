from sqlalchemy.orm import Session
from models.optimizer.low_poly_model import LowPolyModel

def get_library(db: Session):
    return db.query(LowPolyModel).all()
