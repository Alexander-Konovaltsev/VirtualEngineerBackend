from sqladmin import ModelView
from models.quiz import Quiz
from models.scene import Scene
from sqlalchemy import or_

class QuizAdmin(ModelView, model=Quiz):
    name = "тест"
    name_plural = "Тесты"

    column_list = [
        Quiz.id,
        Quiz.title,
        Quiz.attempts_count,
        Quiz.questions_count,
        Quiz.time,
        Quiz.scene
    ]

    column_labels = {
        Quiz.id: "ID",
        Quiz.title: "Название",
        Quiz.attempts_count: "Кол-во попыток",
        Quiz.questions_count: "Кол-во вопросов",
        Quiz.time: "Время выполнения, мин",
        Quiz.scene: "Сцена",
        Quiz.description: "Описание",
        "questions": "Вопросы",
        
    }

    column_sortable_list = [
        Quiz.id
    ]

    column_default_sort = [(Quiz.id, True)]

    form_columns = [
        Quiz.title,
        Quiz.description,
        Quiz.attempts_count,
        Quiz.questions_count,
        Quiz.time,
        Quiz.scene
    ]

    column_details_list = [
        Quiz.title,
        Quiz.description,
        Quiz.attempts_count,
        Quiz.questions_count,
        Quiz.time,
        Quiz.scene,
        "questions"
    ]

    column_searchable_list = [
        Quiz.id,
        Quiz.title,
        Quiz.scene
    ]

    def search_query(self, stmt, term):
        stmt = stmt.join(Quiz.scene)

        return stmt.where(
            or_(
                Quiz.id == int(term) if term.isdigit() else False,
                Quiz.title.ilike(f"%{term}%"),
                Scene.title.ilike(f"%{term}%")
            )
        )
