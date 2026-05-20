from sqladmin import ModelView
from sqlalchemy import or_
from models.scene_model import SceneModel
from models.scene import Scene
from models.model import Model

class SceneModelAdmin(ModelView, model=SceneModel):
    name = "модель на сцене"
    name_plural = "Модели на сценах"

    column_list = [
        SceneModel.id,
        SceneModel.scene,
        SceneModel.model
    ]

    column_labels = {
        SceneModel.id: "ID",
        SceneModel.scene: "Сцена",
        SceneModel.model: "Модель"
    }

    column_sortable_list = [
        SceneModel.id
    ]

    column_default_sort = [(SceneModel.id, True)]

    column_details_list = [
        SceneModel.scene,
        SceneModel.model
    ]

    column_searchable_list = [
        SceneModel.id,
        SceneModel.scene,
        SceneModel.model
    ]

    def search_query(self, stmt, term):
        stmt = stmt.join(SceneModel.scene).join(SceneModel.model)

        return stmt.where(
            or_(
                SceneModel.id == int(term) if term.isdigit() else False,
                Scene.title.ilike(f"%{term}%"),
                Model.title.ilike(f"%{term}%")
            )
        )
