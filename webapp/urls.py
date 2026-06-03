from django.urls import path
from django.views.generic import RedirectView
from webapp.views import task_list, task_detail, task_add, task_edit, task_delete

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='task_list'), name='index'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', task_add, name='task_add'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
]