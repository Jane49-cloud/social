from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from django.views.generic import ListView, TemplateView


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {'restaurants': restaurants})


class restaurantView(ListView):
    queryset = Restaurant.objects.all()
    template_name = 'restaurants.html'

    def get_context_data(self, *args, **kwargs):
        context = super(restaurantView, self).get_context_data(*args, **kwargs)
        return context


class chickenView(ListView):
    queryset = Restaurant.objects.filter(category__iexact='chicken')
    template_name = 'restaurants.html'


class chipsView(ListView):
    queryset = Restaurant.objects.filter(category__iexact='chips')
    template_name = 'restaurants.html'
