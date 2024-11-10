from django.urls import path
from . import views

urlpatterns = [
    path("todos/", view=views.todos ,name="todo"),
    path("create/", view=views.create ,name="create"),
    path("delete/<int:todo_id>/", view=views.delete, name="delete"),
    path("update/<int:todo_id>/", view=views.update, name="update")
]
