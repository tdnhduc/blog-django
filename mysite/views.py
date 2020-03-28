from django.shortcuts import render, get_object_or_404, redirect
from blog.settings import EMAIL_HOST_USER
from django.contrib import messages
from . import forms
from .models import Post, Topic, Email



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'site/home.html', context)

def about(request):
    return render(request, 'site/about.html')

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


def subscribe(request):
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        if sub.is_valid():
            recepient = request.POST.get('email')
            if Email.objects.filter(email=recepient).exists():
                messages.warning(request, f'Your email has receive new post')
            else:    
                email = Email(email=recepient)
                email.save()
                messages.success(request, f'You will seen daily post in your email')
    else :
        messages.error(request, f'Failed')
    storage = messages.get_messages(request)
    storage.used = True
    return home(request)