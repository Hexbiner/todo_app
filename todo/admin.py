from django.contrib import admin
from .models import Category, TodoList, ArchiveList

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
class ArchiveListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")

admin.site.register(Category)
admin.site.register(TodoList)
admin.site.register(ArchiveList)
