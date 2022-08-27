from tkinter import CASCADE
from tokenize import Triple
from django.db import models
from django.conf import settings

from Restaurants.models import Restaurant

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    name = models.CharField(max_length= 120)
    contents =models.TextField(help_text='separate each item by comma')
    excludes =models.TextField(blank= True, help_text='separate each item by comma')
    public = models.BooleanField(default=True)  
    
    # class Meta:
    #     ordering = ['-updated', '-timestamp']
    def get_contents(self):
        return self.contents.splits(',')
    
    def get_excludes(self):
        return self.excludes.splits(',')
       
        
       