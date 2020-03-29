from django.db.models.signals import post_save
from django.dispatch import receiver
from mysite.models import Post, Email
from django.core.mail import send_mail
from blog.settings import EMAIL_HOST_USER


content = "This is auto email of blogger who is the most handsome in VN. \
            Please click on link bellow to see domain of blog \
            https://myfirstblogdjango.herokuapp.com/ \
            (Blog still in develop process. Wait for few time to see it. :D)"
@receiver(post_save, sender=Post)
def SendEmail(sender , instance, created, **kwargs):
    if created:
        emails = list(Email.objects.values('email'))
        recepients = []
        for i in range(0, len(emails)):
            recepients.append(emails[i]['email'])
            pass
        send_mail('New post on Alykes', content, EMAIL_HOST_USER, recepients, fail_silently=False)
        pass
