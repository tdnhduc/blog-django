from django.db import models
from django.utils import timezone

class Topic(models.Model):
    topic_name = models.CharField(max_length=121)

    class Meta:
        ordering = ['topic_name']

    def _str__(self):
        return self.topic_name


class Post(models.Model):
    title = models.CharField(max_length=121)
    description = models.TextField()
    published = models.DateField(default=timezone.now)
    topic = models.ManyToManyField(Topic)

    class Meta:
        ordering = ['title', 'published', 'description']

    def __str__(self):
        return self.title


class CategoryPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

