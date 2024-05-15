from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("completed", views.completed, name="task_completed"),
    path("remaining", views.remaining, name="remaining_tasks"),
    path("add_task", views.add_task, name="add_task"),
    path("delete_task/<str:task_id>", views.delete_task, name="delete_task"),
    path("detail/<str:task_id>", views.task_detail, name="task_details"),
    path(
        "toggle_complete/<str:task_id>", views.toggle_complete, name="toggle_complete"
    ),
    path("remove_task/<str:task_id>", views.remove_task, name="remove_task"),
]
