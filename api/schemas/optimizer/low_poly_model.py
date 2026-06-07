from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LowPolyModelResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    filename: str
    poly_count: int
    l_max: float
    l_mid: float
    l_min: float
    created_at: datetime

    class Config:
        from_attributes = True