from sqladmin import ModelView
from models.user import User
from wtforms import PasswordField
from wtforms.validators import Email
from services.security_service import SecurityService
from db.session import SessionLocal
from crud.user import get_user_by_email

class UserAdmin(ModelView, model=User):
    name = "пользователя"
    name_plural = "Пользователи"

    column_list = [
        User.id,
        User.email,
        User.last_name,
        User.first_name,
        User.patronymic,
        User.role,
        User.workplace
    ]

    column_labels = {
        User.id: "ID", 
        User.email: "Email",
        User.last_name: "Фамилия",
        User.first_name: "Имя",
        User.patronymic: "Отчество",
        User.role: "Роль",
        User.workplace: "Место работы",
        User.password: "Пароль",
        User.created_at: "Дата регистрации",
        "results": "Результаты тестирований",
        "results_details": "Логи результатов",
        "models_views": "Логи изучения моделей"
    }

    column_sortable_list = [
        User.id
    ]

    column_default_sort = [(User.id, True)]

    column_searchable_list = [
        User.id,
        User.email,
        User.last_name
    ]

    form_columns = [
        "last_name",
        "first_name",
        "patronymic",
        "email",
        "password",
        "role",
        "workplace"
    ]

    form_overrides = {
        "password": PasswordField
    }

    form_args = {
        "email": {
            "validators": [
                Email(message="Некорректный email")
            ]
        }
    }

    column_details_list = [
        User.last_name,
        User.first_name,
        User.patronymic,
        User.email,
        User.role,
        User.workplace,
        User.created_at,
        "results",
        "models_views"
    ]

    column_formatters_detail = {
        User.created_at: lambda m, a: (
            m.created_at.strftime("%d.%m.%Y %H:%M:%S")
            if m.created_at else ""
        )
    }

    async def on_model_change(self, data, model, is_created, request):
        password = data.get("password", "").strip()
        email = data.get("email", "").strip()

        db = SessionLocal()

        try:
            user = get_user_by_email(db, email)

            if is_created:
                if user:
                    raise ValueError("Пользователь с таким email уже существует")
            else:
                if user and user.id != model.id:
                    raise ValueError("Пользователь с таким email уже существует")

        finally:
            db.close()

        if is_created:
            if not password:
                raise ValueError("Пароль обязателен")

            data["password"] = SecurityService.hash_password(password)
        else:
            if password:
                data["password"] = SecurityService.hash_password(password)
            else:
                data["password"] = model.password
