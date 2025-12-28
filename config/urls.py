from django.contrib import admin
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from tasks.views.task_views import TaskDetailView, TaskListCreateView
from tasks.views.auth_views import LoginView, LogoutView, RegisterView, MyProfileView


schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version="v1",
        description="API documentation for Task Manager",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Tasks
    path("api/tasks/", TaskListCreateView.as_view(), name="task-list"),
    path("api/tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),

    # Auth
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/profile/", MyProfileView.as_view(), name="profile"),

    # JWT
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

    # API Docs
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
