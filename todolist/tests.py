from todolist.models import TaskModel
from django.test import TestCase
from rest_framework.test import APITestCase


class TestTaskViewSet(APITestCase):
    def setUp(self) -> None:
        self.task = TaskModel.objects.create(title="Test Task", description="Test Description", completed=False)
        self.task_2 = TaskModel.objects.create(title="Test Task 2", description="Test Description 2", completed=True)
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
        self.assertEqual(TaskModel.objects.count(), 1)
    
    def test_list_tasks_filter(self):
        response = self.client.get('/api/v1/tasks/?completed=false')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
    
    def test_list_tasks_ordering_for_updated_at(self):
        response = self.client.get('/api/v1/tasks/?ordering=-updated_at')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['title'], self.task_2.title)
    
    def test_list_tasks_ordering_for_created_at(self):
        response = self.client.get('/api/v1/tasks/?ordering=created_at')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['title'], self.task.title)

    def test_create_task_error(self):
        data = {
            "completed": False
        }
        response = self.client.post('/api/v1/tasks/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['title'][0], "Title cannot be empty")

    def test_update_task_error_without_title(self):
        data = {
            "title": "",
            "description": "Test Description",
            "completed": True
        }
        response = self.client.put(f'/api/v1/tasks/{self.task.id}/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['title'][0], "Title cannot be empty")
    
    def test_update_task_error_without_description(self):
        data = {
            "title": "Test Task",
            "description": "",
            "completed": True
        }
        response = self.client.put(f'/api/v1/tasks/{self.task.id}/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['description'][0], "Description cannot be empty")
    
    def test_create_task_with_empty_title_and_description(self):
        data = {
            "title": "",
            "description": "",
            "completed": False
        }
        response = self.client.post('/api/v1/tasks/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Title cannot be empty", response.data['title'])
        self.assertIn("Description cannot be empty", response.data['description'])