import os
from fastapi import FastAPI
from sqladmin import Admin
from db.session import engine
from admin.views.users import UserAdmin
from admin.views.roles import RoleAdmin
from admin.views.scenes import SceneAdmin
from admin.views.results import Resultdmin
from admin.views.quizzes import QuizAdmin
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
