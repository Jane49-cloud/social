from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True)

