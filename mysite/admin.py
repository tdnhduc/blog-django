from django.contrib import admin
from .models import Topic, Post, CategoryPost

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(CategoryPost)
