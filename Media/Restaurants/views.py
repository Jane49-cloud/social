from multiprocessing import context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Restaurant
from django.views.generic import ListView, UpdateView, CreateView
from .forms import ModelForm


class CreateFormView(LoginRequiredMixin, CreateView):
    form_class = ModelForm
    login = '/login/'
    template_name = 'createForm.html'
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(CreateFormView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateFormView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {'restaurants': restaurants})


class ListRestaurants(ListView):
    template_name = 'restaurants.html'
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.all(owner=self.request.user)


class restaurantView(LoginRequiredMixin, ListView):
    template_name = 'restaurants.html '
    context_object_name = 'restaurant_list'

    def queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = Restaurant.objects.all()
        return queryset


def single_restaurant(request, pk):
    id = Restaurant.objects.get(pk=pk)
    if pk:
        restaurant = Restaurant.objects.filter(id=pk)
    else:
        restaurant = Restaurant.objects.all()

    return render(request, 'single_restaurant.html', {'restaurant': restaurant})


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ModelForm
    login = '/login/'
    template_name = 'createForm.html'
    success_url = '/'

    def get_form_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_form_data(*args, **kwargs)
        context['title'] = "update Restaurant"
        return context

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)
