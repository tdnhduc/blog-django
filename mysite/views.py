from django.shortcuts import render, get_object_or_404
from .models import Post, Topic



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'site/home.html', context)


def poststopic(request, topic):
    context = {
        'posts': Post.objects.filter(topic__topic_name__contains=topic).order_by('-published')
    }
    return render(request, 'site/home.html', context)


def postdetail(request, pk):
    context = {
        'post': Post.objects.filter(id=pk).first()
    }
    return render(request, 'site/post_detail.html', context)
