from django.db import models
from django.contrib import admin

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
