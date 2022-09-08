from profile import Profile
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.http import Http404
from Restaurants.models import Restaurant
from menu.models import Item

User = get_user_model()


class ProfileDetails(DetailView):
    template_name = 'profile.html'
    # queryset = User.objects.filter(is_active=True)

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetails, self).get_context_data(*args, **kwargs)
        user = context['user']
        query = self.request.GET.get('q')
        Item_exists = Item.objects.filter(user=user).exists()
        qs = Restaurant.objects.filter(owner=user)
        if query:
            qs = qs.search(query)
        if Item_exists and qs.exists():
            context['location'] = qs
        return context
