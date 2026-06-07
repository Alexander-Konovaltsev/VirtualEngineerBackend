from sqladmin import ModelView
from models.vr.model import Model

class ModelAdmin(ModelView, model=Model):
    name = "модель"
    name_plural = "Модели"

    column_list = [
        Model.id,
        Model.name,
        Model.title,
        Model.is_draggable,
        Model.is_assemblable,
        Model.is_informational,
        Model.parent
    ]

    column_labels = {
        Model.id: "ID",
        Model.name: "Имя объекта",
        Model.title: "Название",
        Model.is_draggable: "Является перетаскиваемой",
        Model.is_assemblable: "Является разбираемой",
        Model.is_informational: "Является информационной",
        Model.parent: "Родитель",
        Model.description: "Описание",
        "children": "Дочерние",
        "scenes_models": "Модель на сценах"
        
    }

    column_sortable_list = [
        Model.id
    ]

    column_default_sort = [(Model.id, True)]

    form_columns = [
        Model.name,
        Model.title,
        Model.description,
        Model.is_draggable,
        Model.is_assemblable,
        Model.is_informational,
        Model.parent
    ]

    column_details_list = [
        Model.name,
        Model.title,
        Model.description,
        Model.is_draggable,
        Model.is_assemblable,
        Model.is_informational,
        Model.parent,
        "children",
        "scenes_models"
    ]

    column_searchable_list = [
        Model.id,
        Model.name,
        Model.title
    ]
