from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from posts.models import Post

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    posts = Post.objects.filter(user=person)
    followings = person.followings.all()
    followers = person.followers.all()
    context = {
        'person': person,
        'followings': followings,
        'followers': followers,
        'posts': posts,
    }
    return render(request, 'accounts/profile.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)