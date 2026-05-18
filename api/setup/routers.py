from fastapi import APIRouter

from routers import (
    roles,
    users,
    scenes,
    models,
    models_views,
    quizzes,
    results,
    questions,
    results_details
)

def setup_routers(app):
    api_router = APIRouter(prefix="/api")

    api_router.include_router(roles.router)
    api_router.include_router(users.router)
    api_router.include_router(scenes.router)
    api_router.include_router(models.router)
    api_router.include_router(models_views.router)
    api_router.include_router(quizzes.router)
    api_router.include_router(results.router)
    api_router.include_router(questions.router)
    api_router.include_router(results_details.router)

    app.include_router(api_router)
