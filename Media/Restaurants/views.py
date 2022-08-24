
from django.shortcuts import render, get_object_or_404
from django. db. models import Q
from django.http import HttpResponse
from .models import Restaurant
from django.views.generic import ListView, TemplateView, CreateView
from .forms import ModelForm

# def createNewRestaurant(request):
#     template_name = 'createForm.html'
#     context ={}
#     if request =='POST':

class CreateFormView(CreateView):
    form_class = ModelForm
    template_name = 'createForm.html'
    success_url ='/'
        




def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, "home.html", {'restaurants': restaurants})
  


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


# class chickenView(ListView):
#     template_name = 'restaurants.html'
#     context_object_name = 'restaurant_list'
#     queryset = Restaurant.objects.filter(category__iexact='chicken')
    
      


# class chipsView(ListView):
#     template_name = 'restaurants.html'
#     context_object_name = 'restaurant_list'
#     queryset = Restaurant.objects.filter(category__iexact='chips')
    


def single_restaurant(request, pk):
    id = Restaurant.objects.get(pk=pk)
    if pk:
        restaurant = Restaurant.objects.filter(id=pk)
    else: 
        restaurant = Restaurant.objects.all()

    return render(request, 'single_restaurant.html' ,{'restaurant' : restaurant})

