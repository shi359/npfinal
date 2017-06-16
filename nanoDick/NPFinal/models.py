from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
	img_name = models.CharField(max_length=200)
	hash_tag = models.TextField()

