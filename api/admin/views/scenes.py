from sqladmin import ModelView
from models.scene import Scene

class SceneAdmin(ModelView, model=Scene):
    name = "сцену"
    name_plural = "Сцены"

    column_list = [
        Scene.id,
        Scene.name,
        Scene.title
    ]

    column_labels = {
        Scene.id: "ID",
        Scene.name: "Имя объекта",
        Scene.title: "Название",
        Scene.description: "Описание",
        "scenes_models": "Модели на сцене",
        "quizzes": "Тесты"
    }

    column_sortable_list = [
        Scene.id
    ]

    column_default_sort = [(Scene.id, True)]

    form_columns = [
        Scene.name,
        Scene.title,
        Scene.description
    ]

    column_details_list = [
        Scene.name,
        Scene.title,
        Scene.description,
        "scenes_models",
        "quizzes"
    ]

    column_searchable_list = [
        Scene.id,
        Scene.name,
        Scene.title
    ]
