from django.urls import path
from .views import (
    home,
    poststopic,
    postdetail,
    about,
    subscribe,
    search,
)


urlpatterns = [
    path('', home, name='site-home'),
    path('about/', about, name='site-about'),
    path('subscribe/', subscribe, name='subcribe'),
    path('topics/<str:topic>/', poststopic, name='topics-list'),
    path('articles/<int:pk>/', postdetail, name='post-detail'),
    path('search/', search, name='search')
]
