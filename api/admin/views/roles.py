from sqladmin import ModelView
from models.role import Role

class RoleAdmin(ModelView, model=Role):
    name = "роль"
    name_plural = "Роли"

    column_list = [
        Role.id,
        Role.name
    ]

    column_labels = {
        Role.id: "ID",
        Role.name: "Название"
    }

    column_sortable_list = [
        Role.id
    ]

    column_default_sort = [(Role.id, True)]

    form_columns = [
        Role.name
    ]

    column_details_list = [
        Role.name
    ]

    column_searchable_list = [
        Role.id,
        Role.name
    ]
