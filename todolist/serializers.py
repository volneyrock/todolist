from rest_framework import serializers

from todolist.models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ["id", "title", "description", "completed", "created_at", "updated_at"]

    def validate(self, attrs):
        title = attrs.get("title")
        description = attrs.get("description")
        errors = {}

        if title is None or title.strip() == "":
            errors["title"] = "Title cannot be empty"
        if description is None or description.strip() == "":
            errors["description"] = "Description cannot be empty"

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
