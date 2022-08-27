from urllib import request
from django.shortcuts import render
from django.views.generic import ListView,DeleteView,UpdateView,CreateView,DetailView
from .models import Item
from .form  import ItemForm


class ItemListView(ListView):
    template_name='item_list.html'
    context_object_name = 'item_list'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user) 

class ItemDetailsView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user) 
    
class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name='item_create.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user) 
    
class ItemUpdateView(UpdateView):
    form_class= ItemForm
    template_name = 'update.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user) 
    