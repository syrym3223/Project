from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('my/', views.my_posts, name='my_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
