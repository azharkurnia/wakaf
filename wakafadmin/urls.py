from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

#url for app
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/wakaf_admin'}, name='logout'),
    url(r'^tables/', tables, name='tables'),
    url(r'^uploadFotoDonasi/', uploadFotoDonasi, name='uploadFotoDonasi'),
    url(r'^pageFotoDonasi/', pageFotoDonasi, name='pageFotoDonasi'),
    url(r'^pageCarouselHome/', pageCarouselHome, name='pageCarouselHome'),
    url(r'^deleteCarouselHome/(?P<image_id>[0-9]+)/$', deleteCarouselHome, name='deleteCarouselHome'),
    url(r'^addCarouselHome/', addCarouselHome, name='addCarouselHome'),
    url(r'^addLayanan/', addLayanan, name='addLayanan'),

]
