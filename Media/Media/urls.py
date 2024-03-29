from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView, \
    PasswordResetConfirmView
from django.contrib.auth import views as auth_views
from Restaurants.views import home, restaurantView, single_restaurant, CreateFormView, RestaurantUpdateView, \
    ListRestaurants
from menu.views import ItemListView, ItemDetailsView, ItemCreateView, ItemUpdateView, allItems
from profiles.views import ProfileDetails, ProfileFollowToggle, signup

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^restaurant/$', ListRestaurants.as_view(), name='restaurants'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^password_reset/$', PasswordResetView.as_view(),name='password_reset'),
    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(),
            name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', PasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
    re_path(r'^restaurants/create/$', CreateFormView.as_view()),
    re_path(r'^restaurants/(?P<slug>\w+)/$', restaurantView.as_view()),
    re_path(r'^restaurant/(?P<pk>\d+)/$',
            single_restaurant, name='single_restaurant'),
    re_path(r'^restaurant/(?P<pk>\d+)/edit/$',
            RestaurantUpdateView.as_view(), name='update_restaurant'),

    path('password_reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),

    # menu urls
    re_path(r'^menu/$', ItemCreateView.as_view(), name='create'),
    re_path(r'^menu/lists/$', allItems, name='list'),
    re_path(r'^menu/list/$', ItemListView.as_view(), name='personallist'),
    re_path(r'^menu/list/(?P<pk>\d+)/$', ItemDetailsView, name='details'),
    re_path(r'^menu/list/(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='update'),
    # profile urls

    re_path(r'^profile/(?P<username>[\w-]+)/$', ProfileDetails.as_view(), name='detail'),
    re_path(r'^follow/$', ProfileFollowToggle.as_view(), name='follow'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
