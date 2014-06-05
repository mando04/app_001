from django.shortcuts import render, redirect
from .blogforms import PostForm
from .models import Post
# Create your view here.

def about(request):
    return render(request, 'about.html')

def home(request):
    context = {
        'title': 'WWW',
        'posts': Post.objects.all(),
        'request': request
    }
    return render(request, 'index.html', context)

def post(request):
    context = {
        'title': 'Blog Post',
        'forms': PostForm()
    }
    if request.method == 'POST':
        context["forms"] = PostForm(request.POST)
        post = PostForm(request.POST)
        try:
            post.save()
            return redirect(home)
        except Exception as e:
            context["error"] = e
    return render(request, 'post.html', context)