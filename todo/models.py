from django.db import models

# Create your models here.
class TodoItem(models.Model):
	content = models.TextField()
	done = models.BooleanField()
	desc = models.TextField()
