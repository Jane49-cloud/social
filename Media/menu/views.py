from typing import ItemsView
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from .models import Item
from .form import ItemForm


class ItemListView(ListView):
    template_name = 'item_list.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


def ItemDetailsView(request, pk):
    template_name = 'detail.html'
    id = Item.objects.get(pk=pk)
    if pk:
        item = Item.objects.filter(id=pk)
    else:
        item = Item.objects.all()
    return render(request, template_name, {'item': item, 'item_id': id})


class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'item_create.html'
    success_url= '/'
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form) 
           
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
   
    
class ItemUpdateView(UpdateView):
    form_class= ItemForm
    template_name = 'update.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user) 
    def get_context_data(self, *args, **kwargs):
        context = super(ItemForm,self).get_context_data(*args, **kwargs)
        context['title'] ='Update Item'
        return context
    