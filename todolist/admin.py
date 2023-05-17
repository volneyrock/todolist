from django.contrib import admin
from todolist.models import TaskModel


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created_at', 'updated_at']
    list_filter = ['completed', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
