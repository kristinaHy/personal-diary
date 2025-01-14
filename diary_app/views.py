from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import date
from .models import Post
from .forms import PostForm, SignUpForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def post_list(request):
    posts = Post.objects.filter(author=request.user).order_by('-date')
    if not posts:
        messages.warning(request, "You haven't posted anything yet.")
    return render(request, 'post_list.html', {'posts': posts})

@login_required(login_url="login")
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required(login_url="login")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = date.today()
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

@login_required(login_url="login")
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect('post-list')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required(login_url="login")
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "You do not have permission to delete this post.")
        return redirect('post-list')

    post.delete()
    messages.success(request, 'You have successfully deleted the post.')
    return redirect('post-list')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post-list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
