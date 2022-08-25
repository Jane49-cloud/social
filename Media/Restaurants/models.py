from tkinter import CASCADE
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True)
     
    def __str__(self):
        return self.name
      

