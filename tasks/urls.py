from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('remaining/', views.remaining, name='remaining_tasks'),
    path('completed/', views.completed, name='task_completed'),
    path('add/', views.add, name='add_task'),
    path('delete/', views.delete, name='delete_task'),
    path('details/', views.details, name='task_details'),
]