import os
from fastapi import FastAPI
from sqladmin import Admin
from db.session import engine
from admin.views.users import UserAdmin
from admin.views.roles import RoleAdmin
from admin.views.scenes import SceneAdmin
from admin.views.results import Resultdmin
from admin.views.quizzes import QuizAdmin
from admin.views.answers import AnswerAdmin
from admin.views.questions import QuestionAdmin
from admin.views.models import ModelAdmin
from admin.views.questions_types import QuestionTypeAdmin
from admin.views.scenes_models import SceneModelAdmin
from admin.views.results_details import ResultDetailAdmin
from admin.auth import AdminAuth

def setup_admin(app: FastAPI):
    authentication_backend = AdminAuth(
        secret_key=os.getenv("SESSION_SECRET_KEY")
    )

    admin = Admin(
        app, 
        engine,
        title="Виртуальный 3D-инженер",
        templates_dir="templates",
        authentication_backend=authentication_backend
    )

    admin.add_view(UserAdmin)
    admin.add_view(RoleAdmin)
    admin.add_view(SceneAdmin)
    admin.add_view(Resultdmin)
    admin.add_view(QuizAdmin)
    admin.add_view(AnswerAdmin)
    admin.add_view(QuestionAdmin)
    admin.add_view(ModelAdmin)
    admin.add_view(QuestionTypeAdmin)
    admin.add_view(SceneModelAdmin)
    admin.add_view(ResultDetailAdmin)
