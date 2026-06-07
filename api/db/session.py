import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

VR_DB_NAME = os.getenv("POSTGRES_DB")
OPTIMIZER_DB_NAME = os.getenv("OPTIMIZER_DB")

VR_DSN = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{VR_DB_NAME}"
OPTIMIZER_DSN = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{OPTIMIZER_DB_NAME}"

vr_engine = create_engine(VR_DSN)
VRSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=vr_engine)
VRBase = declarative_base()

optimizer_engine = create_engine(OPTIMIZER_DSN)
OptimizerSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=optimizer_engine)
OptimizerBase = declarative_base()

def get_vr_db():
    db = VRSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_optimizer_db():
    db = OptimizerSessionLocal()
    try:
        yield db
    finally:
        db.close()
