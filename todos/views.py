from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm


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


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoListForm()

    context = {"form": form}
    return render(request, "todos/create.html", context)
