from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
        author = models.CharField(max_length=200)
        img_name = models.CharField(max_length=200)
        hash_tag = models.TextField()

class Comment(models.Model):
        hash_tag = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        comment = models.TextField()

class Favor(models.Model):
        name = models.CharField(max_length=50)
        like = models.TextField()
