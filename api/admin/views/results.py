from sqladmin import ModelView
from sqlalchemy import or_
from models.result import Result
from models.user import User
from models.quiz import Quiz

class Resultdmin(ModelView, model=Result):
    name = "результат"
    name_plural = "Результаты"

    column_list = [
        Result.id,
        Result.percent,
        Result.total_answers,
        Result.correct_answers,
        Result.user,
        Result.quiz
    ]

    column_labels = {
        Result.id: "ID",
        Result.percent: "Процент",
        Result.total_answers: "Всего ответов",
        Result.correct_answers: "Правильных ответов",
        Result.user: "Пользователь",
        Result.quiz: "Тест",
        User.last_name: "Фамилия",
        Quiz.title: "Тест",
        "results_details": "Логи результата",
        Result.created_at: "Дата прохождения"
    }

    column_sortable_list = [
        Result.id
    ]

    column_default_sort = [(Result.id, True)]

    form_columns = [
        "user",
        "quiz",
        Result.percent,
        Result.total_answers,
        Result.correct_answers,
    ]

    column_details_list = [
        "user",
        "quiz",
        Result.percent,
        Result.total_answers,
        Result.correct_answers,
        Result.created_at,
        "results_details"
    ]

    column_searchable_list = [
        Result.id,
        User.last_name,
        Quiz.title
    ]

    column_formatters_detail = {
        Result.created_at: lambda m, a: (
            m.created_at.strftime("%d.%m.%Y %H:%M:%S")
            if m.created_at else ""
        )
    }

    def search_query(self, stmt, term):
        stmt = stmt.join(Result.user).join(Result.quiz)

        return stmt.where(
            or_(
                Result.id == int(term) if term.isdigit() else False,
                User.last_name.ilike(f"%{term}%"),
                Quiz.title.ilike(f"%{term}%")
            )
        )
