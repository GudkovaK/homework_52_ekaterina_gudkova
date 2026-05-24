from django.urls import path
from webapp.views import task_list, task_add, task_delete

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', task_add, name='task_add'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
]
