from django.db import models

# Create your models here.

class Post(models.Model):
    uname = models.CharField(max_length=18, blank=True)
    title = models.CharField(max_length=150)
    descpt = models.TextField(max_length=1818)