from fastapi import FastAPI
from db.session import Base, engine
from db.db_initializer import DBInitializer
from admin.admin import setup_admin
from setup.middleware import setup_middleware
from setup.routers import setup_routers

app = FastAPI()

setup_routers(app)
setup_middleware(app)
setup_admin(app)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    DBInitializer()
