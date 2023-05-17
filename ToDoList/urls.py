from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from todolist.views import TaskViewSet

router_v1 = SimpleRouter()
router_v1.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = router_v1.urls

schema_view = get_schema_view(
    openapi.Info(
        title="ToDoList API",
        default_version="v1",
        description="ToDoList API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(urlpatterns), name="tasks"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
