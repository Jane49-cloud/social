from typing import ItemsView
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = 'item_create.html'
    success_url = '/'

    # associate with logged in user
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = 'update.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
