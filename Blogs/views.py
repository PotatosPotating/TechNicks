from django.shortcuts import render,redirect
from .models import BlogPost,Comments
from .forms import CommentForm,BlogForm
from django.db import models
import datetime

# Create your views here.

def index(request):
    all_blogs = BlogPost.objects.all()
    return render(request,'Blogs/index.html',{'all_blogs':all_blogs})

def viewBlog(request,title):
    blog = BlogPost.objects.get(title=title)
    comments = Comments.objects.filter(blog = title)
    all_blogs = BlogPost.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                new_comment = form.save(commit=False)
                new_comment.username = request.user.username
                new_comment.blog = BlogPost.objects.get(title=title)
                new_comment.save()
                form = CommentForm()
                return redirect('/blogs/'+title,{'blog':blog,'all_comments':comments,'all_blogs':all_blogs,'form':form})
            else:
                return redirect('/accounts/login',{'all_blogs':all_blogs})
    else:
        form = CommentForm()
    return render(request, 'Blogs/viewblog.html', {'blog':blog,'all_comments':comments,'all_blogs':all_blogs,'form':form})



def createBlog(request):
    all_blogs = BlogPost.objects.all()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                new_blog = form.save(commit=False)
                new_blog.author = request.user.username
                new_blog.save()
                return redirect('/blogs'
                                '/'+new_blog.title+'/',{'all_blogs':all_blogs})
            else:
                return redirect('/accounts/login',{'all_blogs':all_blogs})
    else:
        form = BlogForm()
    return render(request,'Blogs/createblog.html',{'all_blogs':all_blogs,'form':form})



def editBlog(request,title):
    all_blogs = BlogPost.objects.all()
    blog = BlogPost.objects.get(title=title)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                new_blog = form.save(commit=False)
                new_blog.author = request.user.username
                new_blog.save()
                return redirect('/blogs'
                                '/'+new_blog.title+'/',{'all_blogs':all_blogs})
            else:
                return redirect('/accounts/createblog',{'all_blogs':all_blogs})
    else:

        form = BlogForm()
    return render(request,'Blogs/createblog.html',{'all_blogs':all_blogs,'form':form})