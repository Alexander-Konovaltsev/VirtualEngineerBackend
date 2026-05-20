from sqladmin import ModelView
from models.question_type import QuestionType

class QuestionTypeAdmin(ModelView, model=QuestionType):
    name = "тип вопроса"
    name_plural = "Типы вопроса"

    column_list = [
        QuestionType.id,
        QuestionType.name
    ]

    column_labels = {
        QuestionType.id: "ID",
        QuestionType.name: "Название"
    }

    column_sortable_list = [
        QuestionType.id
    ]

    column_default_sort = [(QuestionType.id, True)]

    form_columns = [
        QuestionType.name
    ]

    column_details_list = [
        QuestionType.name
    ]

    column_searchable_list = [
        QuestionType.id,
        QuestionType.name
    ]
