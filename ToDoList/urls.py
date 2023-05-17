from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from todolist.views import TaskViewSet

router_v1 = SimpleRouter()
router_v1.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = router_v1.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(urlpatterns), name="tasks"),
]
