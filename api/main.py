from fastapi import FastAPI
from db.session import VRBase, vr_engine, OptimizerBase, optimizer_engine
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
    VRBase.metadata.create_all(bind=vr_engine)
    OptimizerBase.metadata.create_all(bind=optimizer_engine)
    DBInitializer()
