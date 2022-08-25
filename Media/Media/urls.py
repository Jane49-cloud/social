"""Media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from Restaurants.views import home, restaurantView, single_restaurant, CreateFormView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$',  home, name ='home'),
    re_path(r'^login/$', LoginView.as_view(), name ='login'),
      re_path(r'^login/$', LogoutView.as_view(), name ='logout'),
    re_path(r'^restaurants/create/$', CreateFormView.as_view()),
    re_path(r'^restaurants/(?P<slug>\w+)/$', restaurantView.as_view()),
     re_path(r'^restaurant/(?P<pk>\d+)/$', single_restaurant, name='single_restaurant'),
    # re_path(r'^restaurants/chicken/$', chickenView.as_view()),
    # re_path(r'^restaurants/chips/$', chipsView.as_view())
    ]

