from django.urls import path

from .views import AllTaskApiView, TaskCreateApiView, TaskUpdateApiView, TaskDestroyApiView, TaskDetailApiView

urlpatterns = [
    path('list/', AllTaskApiView.as_view()),
    path('create/', TaskCreateApiView.as_view()),
    path('update/', TaskUpdateApiView.as_view()),
    path('destroy/', TaskDestroyApiView.as_view()),
    path('detail/<int:id>/', TaskDetailApiView.as_view()),

]