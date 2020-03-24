from django.urls import path
from .views import (
    about,
    home,
    codinglife,
    outdoor,
)


urlpatterns = [
    path('', home, name='site-home'),
    path('about/', about, name='site-about'),
    path('codinglife/', codinglife, name='site-codinglife'),
    path('outdoor/', outdoor, name='site-outdoor'),
]
