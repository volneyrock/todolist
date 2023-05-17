import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True


class TaskModel(BaseModel):
    title = models.CharField(
        max_length=255, verbose_name="Title", blank=True, null=True
    )
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    completed = models.BooleanField(default=False, verbose_name="Completed")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title
