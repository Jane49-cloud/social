from profile import Profile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.http import Http404
from Restaurants.models import Restaurant
from menu.models import Item
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

User = get_user_model()


class ProfileFollowToggle(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect("u/janen/")


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
        item_exists = Item.objects.filter(user=user).exists()
        qs = Restaurant.objects.filter(owner=user)
        if query:
            qs = qs.search(query)
        if item_exists and qs.exists():
            context['location'] = qs
        return context


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
