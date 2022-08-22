from django.shortcuts import render
from django. db. models import Q
from django.http import HttpResponse
from .models import Restaurant
from django.views.generic import ListView, TemplateView


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {'restaurants': restaurants})
    print(restaurants)


class restaurantView(ListView):
    template_name = 'restaurants.html'
    context_object_name = 'restaurant_list'

    def queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset =Restaurant.objects.all()
        return queryset


class chickenView(ListView):
    template_name = 'restaurants.html'
    context_object_name = 'restaurant_list'
    queryset = Restaurant.objects.filter(category__iexact='chicken')
    
      


class chipsView(ListView):
    template_name = 'restaurants.html'
    context_object_name = 'restaurant_list'
    queryset = Restaurant.objects.filter(category__iexact='chips')
    
