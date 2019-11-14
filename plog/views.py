from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'plog/post_list.html', {'posts': posts})


def teaching(request):

    return render(request, 'plog/teaching.html') 

def research(request):

    return render(request, 'plog/research.html') 

def dprinting(request):

    return render(request, 'plog/dprinting.html') 

def seminars(request):

    return render(request, 'plog/seminars.html')
