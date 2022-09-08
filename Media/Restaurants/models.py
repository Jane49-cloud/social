from django.db import models
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL


class RestaurantQuerySet(models.query.QuerySet):
    def search(self, query):  # Restaurant.objects.all().search()
        query = query.strip()
        return self.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(category__icontains=query) |
            Q(item__name__icontains=query) |
            Q(item__contents__icontains=query)
        ).distinct()


class RestaurantManager(models.Manager):
    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='assets')

    objects = RestaurantManager()  # adds to models.objects.all()

    def __str__(self):
        return self.name
