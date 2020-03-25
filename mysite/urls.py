from django.urls import path
from .views import (
    home,
    codinglife,
    outdoor,
)
urlpatterns = [
    path('', home, name='site-home'),
    path('codinglife/', codinglife, name='site-codinglife'),
    path('outdoor/', outdoor, name='site-outdoor'),
]
