from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1')
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2')
    title = models.CharField(max_length=50)
    select1_content = models.CharField(max_length=100)
    select2_content = models.CharField(max_length=100)
    select1_image = models.ImageField(blank=True)
    select2_image = models.ImageField(blank=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.TextField(null=False)