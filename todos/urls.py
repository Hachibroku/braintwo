from django.urls import path
from todos.views import show_todo_list, detail_todo_list

urlpatterns = [
    path("", show_todo_list, name="todo_list_list"),
    path("<int:id>/", detail_todo_list, name="todo_list_detail"),
]
