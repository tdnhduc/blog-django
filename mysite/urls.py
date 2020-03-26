from django.urls import path
from .views import (
    home,
    poststopic,
    postdetail,
)
urlpatterns = [
    path('', home, name='site-home'),

    path('topics/<str:topic>/', poststopic, name='topics-list'),
    path('articles/<int:pk>/', postdetail, name='post-detail')
]
