from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.html import strip_tags
from .models import BlogPost
from datetime import datetime
import string
import random

# Create your views here.


def index(request):
    all_posts = BlogPost.objects.all()[::-1][:5]
    context = {
        'posts': all_posts
    }
    return render(request, 'index.html', context)


def loginUser(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def logoutUser(request):
    if not request.user.is_anonymous:
        logout(request)
        return redirect('login')


def about(request):
    return render(request, 'about.html')


def randomString():
    all_strings = string.ascii_lowercase + string.digits
    gen = ''
    for i in range(7):
        gen += random.choice(all_strings)
    return gen


def showBlogPost(request, identifier, blog_slug):
    requested_post = BlogPost.objects.get(
        blog_slug='posts/{}/{}'.format(identifier, blog_slug))
    context = {
        'post': requested_post
    }
    return render(request, "post.html", context)


def createBlogPost(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == 'POST':
        post_title = request.POST.get('title')
        if post_title.strip() == '':
            return redirect('createPost')
        post_body = request.POST.get('content')
        new_post = BlogPost()
        new_post.blog_slug = "".join(
            [x for x in post_title if x.isalnum() or x == ' '])[:15].lower()
        new_post.blog_slug = new_post.blog_slug.replace(' ', '-')
        new_post.blog_slug = 'posts/{}/{}'.format(
            randomString(), new_post.blog_slug)
        new_post.blog_title = post_title
        new_post.blog_text = post_body
        new_post.blog_owner = request.user.get_username()
        new_post.post_time = datetime.today()
        new_post.save()
        return redirect('/')
    return render(request, 'create_post.html')
