import os
from starlette.middleware.sessions import SessionMiddleware

def setup_middleware(app):
    app.add_middleware(
        SessionMiddleware,
        secret_key=os.getenv("SESSION_SECRET_KEY")
    )
