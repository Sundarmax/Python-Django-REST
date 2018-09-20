from django.db import models

# Create your models here.
class post(models.Model):
    title =  models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=50)