from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class add_news(models.Model):
	topic = models.CharField(max_length=25)
	text_message = models.TextField(verbose_name="message")
	date_created = models.DateTimeField(default=timezone.now(),verbose_name="data")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
