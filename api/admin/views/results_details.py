from sqladmin import ModelView
from sqlalchemy import or_
from models.vr.result_detail import ResultDetail
from models.vr.user import User

class ResultDetailAdmin(ModelView, model=ResultDetail):
    name = "лог результата"
    name_plural = "Логи результатов"

    column_list = [
        ResultDetail.id,
        ResultDetail.created_at,
        ResultDetail.user,
        ResultDetail.result,
        ResultDetail.question,
        ResultDetail.answer
    ]

    column_labels = {
        ResultDetail.id: "ID",
        ResultDetail.user: "Пользователь",
        ResultDetail.result: "Результат",
        ResultDetail.question: "Вопрос",
        ResultDetail.answer: "Ответ",
        ResultDetail.created_at: "Дата создания",
        User.last_name: "Фамилия"
    }

    column_sortable_list = [
        ResultDetail.id
    ]

    column_default_sort = [(ResultDetail.id, True)]

    form_excluded_columns = [
        ResultDetail.created_at
    ]

    column_details_list = [
        ResultDetail.user,
        ResultDetail.result,
        ResultDetail.question,
        ResultDetail.answer,
        ResultDetail.created_at
    ]

    column_formatters_detail = {
        ResultDetail.created_at: lambda m, a: (
            m.created_at.strftime("%d.%m.%Y %H:%M:%S")
            if m.created_at else ""
        )
    }

    column_formatters = {
        ResultDetail.created_at: lambda m, a: (
            m.created_at.strftime("%d.%m.%Y %H:%M:%S")
            if m.created_at else ""
        )
    }

    column_searchable_list = [
        ResultDetail.id,
        User.last_name
    ]

    def search_query(self, stmt, term):
        stmt = stmt.join(ResultDetail.user)

        return stmt.where(
            or_(
                ResultDetail.id == int(term) if term.isdigit() else False,
                User.last_name.ilike(f"%{term}%")
            )
        )
