from sqladmin import ModelView
from models.vr.question import Question
from models.vr.quiz import Quiz
from sqlalchemy import or_

class QuestionAdmin(ModelView, model=Question):
    name = "вопрос"
    name_plural = "Вопросы"

    column_list = [
        Question.id,
        Question.question_text,
        Question.question_type,
        Question.quiz
    ]

    column_labels = {
        Question.id: "ID",
        Question.question_text: "Вопрос",
        Question.question_type: "Тип",
        Question.quiz: "Тест",
        "answers": "Ответы"
        
    }

    column_sortable_list = [
        Question.id
    ]

    column_default_sort = [(Question.id, True)]

    form_columns = [
        Question.question_text,
        Question.question_type,
        Question.quiz
    ]

    column_details_list = [
        Question.question_text,
        Question.question_type,
        Question.quiz,
        "answers"
    ]

    column_searchable_list = [
        Question.id,
        Question.question_text,
        Question.quiz
    ]

    def search_query(self, stmt, term):
        stmt = stmt.join(Question.quiz)

        return stmt.where(
            or_(
                Question.id == int(term) if term.isdigit() else False,
                Question.question_text.ilike(f"%{term}%"),
                Quiz.title.ilike(f"%{term}%")
            )
        )
