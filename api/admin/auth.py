from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from pydantic import EmailStr
from db.session import VRSessionLocal
from crud.vr.user import get_user_by_email, get_user_by_id
from services.security_service import SecurityService
from enums.role import RoleName


class AdminAuth(AuthenticationBackend):

    def __init__(self, secret_key: str):
        super().__init__(secret_key)

    async def login(self, request: Request):
        form = await request.form()

        email = form.get("username", "")
        password = form.get("password", "")

        request.session["form_data"] = {
            "username": email,
            "password": password
        }

        errors = {}

        if not email.strip():
            errors["email"] = "Необходимо заполнить «Email»"

        if not password.strip():
            errors["password"] = "Необходимо заполнить «Пароль»"

        if errors:
            request.session["login_errors"] = errors
            return False
        
        try:
            EmailStr._validate(email)
        except Exception:
            request.session["login_errors"] = {
                "email": "Некорректный email"
            }
            return False

        db = VRSessionLocal()

        try:
            admin = get_user_by_email(db, email)

            if not admin or not SecurityService.check_password(password, admin.password):
                request.session["login_errors"] = {
                    "password": "Неправильный email или пароль"
                }
                return False

            if admin.role.name != RoleName.ADMIN.value:
                request.session["login_errors"] = {
                    "email": "У Вас нет соответствующего доступа"
                }
                return False

            request.session.pop("login_errors", None)
            request.session.pop("form_data", None)
            
            request.session["admin_id"] = admin.id
            return True

        finally:
            db.close()

    async def logout(self, request: Request):
        request.session.clear()
        return True

    async def authenticate(self, request: Request):
        admin_id = request.session.get("admin_id")

        if not admin_id:
            return False

        db = VRSessionLocal()

        try:
            admin = get_user_by_id(db, admin_id)

            if not admin:
                return False

            if admin.role.name != RoleName.ADMIN.value:
                return False

            return True

        finally:
            db.close()
