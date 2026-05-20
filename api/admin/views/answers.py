from sqladmin import ModelView
from models.answer import Answer
from models.question import Question
from sqlalchemy import or_

class AnswerAdmin(ModelView, model=Answer):
    name = "ответ"
    name_plural = "Ответы"

    column_list = [
        Answer.id,
        Answer.text,
        Answer.is_correct,
        Answer.question
    ]

    column_labels = {
        Answer.id: "ID",
        Answer.text: "Ответ",
        Answer.is_correct: "Является правильным",
        Answer.question: "Вопрос",
        Answer.explanation: "Пояснение"
        
    }

    column_sortable_list = [
        Answer.id
    ]

    column_default_sort = [(Answer.id, True)]

    form_columns = [
        Answer.text,
        Answer.is_correct,
        Answer.explanation,
        Answer.question
    ]

    column_details_list = [
        Answer.text,
        Answer.is_correct,
        Answer.explanation,
        Answer.question
    ]

    column_searchable_list = [
        Answer.id,
        Answer.text,
        Answer.question
    ]

    def search_query(self, stmt, term):
        stmt = stmt.join(Answer.question)

        return stmt.where(
            or_(
                Answer.id == int(term) if term.isdigit() else False,
                Answer.text.ilike(f"%{term}%"),
                Question.question_text.ilike(f"%{term}%")
            )
        )
