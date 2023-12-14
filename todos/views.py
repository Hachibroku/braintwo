from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


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


def todo_list_update(request, id):
    todo_list_updater = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list_updater)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list_updater)

    context = {"form": form, "updater": todo_list_updater}
    return render(request, "todos/update.html", context)


def todo_list_delete(request, id):
    model_instance = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form,
    }
    return render(request, "todos/todo_item_create.html", context)


def todo_item_update(request, id):
    item = TodoItem.objects.get(id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, "todos/todo_item_update.html", context)
