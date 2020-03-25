from django.shortcuts import render, get_object_or_404
from .models import Post, Topic

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'site/home.html', context)

def codinglife(request):
    context = {
        'posts': Post.objects.filter(topic__topic_name__contains='codinglife')
        
    }
    return render(request, 'site/topiclistview.html', context)

def outdoor(request):
    context = {
        'posts': Post.objects.filter(topic__topic_name__contains='outdoor')
    }
    return render(request, 'site/topiclistview.html', context)