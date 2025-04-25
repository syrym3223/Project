from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts_list')
        else:
            return render(request, 'login.html', {'error': 'Неверные данные!'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    can_edit = (post.author == request.user) or request.user.is_superuser
    return render(request, 'post_detail.html', {'post': post, 'can_edit': can_edit})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('posts_list')
    else:
        return redirect('post_detail', post_id=post.id)
