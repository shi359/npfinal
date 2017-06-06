from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
	title = models.CharField(max_length=200)
	img_src = models.CharField(max_length=200)
	text = models.TextField()
	hash_tag = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
