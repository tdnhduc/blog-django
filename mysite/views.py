from django.shortcuts import render
from .models import Topic, Post, CategoryPost


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'site/home.html', context)


def about(request):
    return render(request, 'site/about.html')


def codinglife(request):
    posts = GetPostFromTopic('codinglife')
    context ={
        'posts': posts
    }

    return render(request, 'site/codinglife.html', context)


def outdoor(request):
    context ={
        'posts': GetPostFromTopic('outdoor')
    }

    return render(request, 'site/outdoor.html', context)

def Query(topic_name, primarykey_post):
    posts = Post.objects.filter(topic__topic_name__contains=topic_name)
    topics = Topic.objects.filter(post__id__contains=primarykey_post)
    return (posts, topics)

def GetPostFromTopic(topic_name):
    return Post.objects.filter(topic__topic_name__contains=topic_name)