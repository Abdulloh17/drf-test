from django.shortcuts import render
from rest_framework import generics

from .serializers import TaskSerializer
from .models import Task

# Create your views here.
class AllTaskApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateApiView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateApiView(generics.UpdateAPIView):
    queryset = Task.objects.get()
    serializer_class = TaskSerializer

class TaskDestroyApiView(generics.DestroyAPIView):
    queryset = Task.objects.get()
    serializer_class = TaskSerializer

class TaskDetailApiView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'