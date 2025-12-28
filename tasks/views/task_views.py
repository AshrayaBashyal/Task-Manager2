from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models.task import Task
from ..searializers.task_serializers import TaskSerializer
from ..permissions.task_permissions import IsTaskOwner


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):    #swagger problem
            return Task.objects.none()
        # First security layer: users only see their own tasks
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Prevent users from assigning tasks to other users
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]
    queryset = Task.objects.all()   # Needed for object-permission checking

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Task.objects.none()
        # Second security layer: limit DB queries to user-owned tasks
        return Task.objects.filter(user=self.request.user)
