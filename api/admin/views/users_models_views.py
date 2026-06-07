from sqladmin import ModelView
from sqlalchemy import or_
from models.vr.user_model_view import UserModelView
from models.vr.user import User

class UserModelViewAdmin(ModelView, model=UserModelView):
    name = "лог изучения модели"
    name_plural = "Логи изучения моделей"

    column_list = [
        UserModelView.id,
        UserModelView.viewed_at,
        UserModelView.user,
        UserModelView.scene,
        UserModelView.model
    ]

    column_labels = {
        UserModelView.id: "ID",
        UserModelView.viewed_at: "Дата изучения",
        UserModelView.user: "Пользователь",
        UserModelView.scene: "Сцена",
        UserModelView.model: "Модель",
        User.last_name: "Фамилия"
    }

    column_sortable_list = [
        UserModelView.id
    ]

    column_default_sort = [(UserModelView.id, True)]

    form_excluded_columns = [
        UserModelView.viewed_at
    ]

    column_details_list = [
        UserModelView.user,
        UserModelView.scene,
        UserModelView.model,
        UserModelView.viewed_at,
    ]

    column_formatters_detail = {
        UserModelView.viewed_at: lambda m, a: (
            m.viewed_at.strftime("%d.%m.%Y %H:%M:%S")
            if m.viewed_at else ""
        )
    }

    column_formatters = {
        UserModelView.viewed_at: lambda m, a: (
            m.viewed_at.strftime("%d.%m.%Y %H:%M:%S")
            if m.viewed_at else ""
        )
    }

    column_searchable_list = [
        UserModelView.id,
        User.last_name
    ]

    def search_query(self, stmt, term):
        stmt = stmt.join(UserModelView.user)

        return stmt.where(
            or_(
                UserModelView.id == int(term) if term.isdigit() else False,
                User.last_name.ilike(f"%{term}%")
            )
        )
