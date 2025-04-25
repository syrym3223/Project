from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todos/create/', views.add_todo, name='todo_create'),
    path('todos/<int:pk>/delete/', views.delete_todo, name='todo_delete'),
]
