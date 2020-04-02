from django.db import models
from django.utils import timezone

class Topic(models.Model):
    topic_name = models.CharField(primary_key=True,unique=True, max_length=60)

    def __str__(self):
        return self.topic_name




ARTICLE_TYPE_CHOICE = [
    ('BT', 'Bình thường'),
    ('BH', 'Bài hay'),
    ('NM', 'Nhập môn'),
]
class Post(models.Model):
    title = models.CharField(unique=True, max_length=121)
    introduce = models.CharField(default='Introduce post', max_length=300)
    content = models.TextField()
    published = models.DateField(default=timezone.now)
    kind_post = models.CharField(max_length=2, choices=ARTICLE_TYPE_CHOICE, default='BT')
    topics = models.ManyToManyField(Topic)



    def __str__(self):
        return self.title
    


    


class Email(models.Model):
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.email

