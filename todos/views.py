from django.shortcuts import render
from todos.models import TodoList, TodoItem


# Create your views here.
def show_todo_list(request):
    todo_list = TodoList.objects.all()
    context = {"todo_list": todo_list}
    return render(request, "todos/list.html", context)
