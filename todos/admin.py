from django.contrib import admin
from todos.models import TodoList, TodoItem


# Register your models here.
admin.site.register(TodoList)


class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )


admin.site.register(TodoItem)


class TodoItem(admin.ModelAdmin):
    list_display = (
        "task",
        "due_date",
    )
