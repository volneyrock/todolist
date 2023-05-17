from rest_framework import serializers
from todolist.models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
