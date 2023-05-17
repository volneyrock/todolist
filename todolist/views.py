from rest_framework import viewsets
from todolist.models import TaskModel
from todolist.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all().order_by('-updated_at')
    serializer_class = TaskSerializer
