from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_vr_db
from dependencies.auth import get_current_user
from schemas.vr.question import QuestionResponse
from crud.vr.question import get_questions_by_quiz_id

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/{quiz_id}", response_model=list[QuestionResponse])
def read_questions(quiz_id: int, db: Session = Depends(get_vr_db), user: dict = Depends(get_current_user)):
    questions = get_questions_by_quiz_id(db, quiz_id)
    return questions
