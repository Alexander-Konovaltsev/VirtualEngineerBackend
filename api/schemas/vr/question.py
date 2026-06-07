from pydantic import BaseModel
from typing import Optional, List
from schemas.vr.question_type import QuestionTypeResponse
from schemas.vr.answers import AnswerResponse

class QuestionResponse(BaseModel):
    id: int
    question_text: str
    quiz_id: int
    model_id: Optional[int]
    question_type_id: int
    question_type: QuestionTypeResponse
    answers: List[AnswerResponse]

    class Config:
        from_attributes = True
