from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from datetime import datetime, timezone
from db.session import OptimizerBase

class LowPolyModel(OptimizerBase):
    __tablename__ = "low_poly_models"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    filename = Column(String(100), nullable=False)
    poly_count = Column(Integer, nullable=False)
    l_max = Column(Float, nullable=False)
    l_mid = Column(Float, nullable=False)
    l_min = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
