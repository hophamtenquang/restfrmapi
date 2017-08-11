from django.db import models

# from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255, null=False)
    body = models.TextField()


class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images')
    image = models.ImageField(upload_to='images')
