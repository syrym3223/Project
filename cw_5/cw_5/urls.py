from django.contrib import admin
from django.urls import path, include
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', posts_views.login_view, name='login'),
    path('', include('posts.urls')),
]
