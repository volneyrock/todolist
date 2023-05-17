from todolist.models import TaskModel
from django.test import TestCase
from rest_framework.test import APITestCase


class TestTaskViewSet(APITestCase):
    def setUp(self) -> None:
        self.task = TaskModel.objects.create(title="Test Task", description="Test Description", completed=False)
        return super().setUp()
    
    def test_create_task(self):
        data = {
            "title": "Test Task",
            "description": "Test Description",
            "completed": False
        }
        response = self.client.post('/api/v1/tasks/', data=data)
        self.assertEqual(response.status_code, 201)
    
    def test_list_tasks(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_task(self):
        response = self.client.get(f'/api/v1/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        data = {
            "title": "Test Task",
            "description": "Test Description",
            "completed": True
        }
        response = self.client.put(f'/api/v1/tasks/{self.task.id}/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['completed'], True)

    def test_delete_task(self):
        response = self.client.delete(f'/api/v1/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(TaskModel.objects.count(), 0)

    def test_create_task_error(self):
        data = {
            "completed": False
        }
        response = self.client.post('/api/v1/tasks/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['title'][0], "Title cannot be empty")