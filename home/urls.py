"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('createPost', views.createBlogPost, name='createPost'),
    path('logout', views.logoutUser, name='logout'),
    path('posts/<identifier>/<blog_slug>/',
         views.showBlogPost, name='blogpost_display'),
    path('archive/<int:id>', views.showOldPosts, name='old_posts'),
    path('author/<str:username>/<int:id>', views.authorPosts, name='author_posts'),
    path('delete/posts/<identifier>/<blog_slug>/', views.deletePost, name='delete_post'),
    path('edit/posts/<identifier>/<blog_slug>/', views.updatePost, name='update_post'),
    path('sitemap.xml', views.prepareSitemap, name='auto_sitemap')
]
