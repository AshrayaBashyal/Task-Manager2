# config/urls.py
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from tasks.views.task_views import TaskDetailView, TaskListCreateView
from  tasks.views.auth_views import LoginView, LogoutView, RegisterView, MyProfileView


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Task endpoints
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Authentication endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/profile/', MyProfileView.as_view(), name='profile'),

    # Token endpoints
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]