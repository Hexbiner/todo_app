from django.contrib import admin
from .models import Category, TodoList #Projects , Tasks

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Category)
admin.site.register(TodoList)
#admin.site.register(Projects)
#admin.site.register(Tasks)
