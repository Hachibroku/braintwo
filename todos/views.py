from django.shortcuts import render, get_object_or_404
from todos.models import TodoList, TodoItem


# Create your views here.
def show_todo_list(request):
    todo_list = TodoList.objects.all()
    context = {"todo_list": todo_list}
    return render(request, "todos/list.html", context)


def detail_todo_list(request, id):
    detail = get_object_or_404(TodoList, id=id)
    context = {
        "todo_detail": detail,
    }
    return render(request, "todos/detail.html", context)
