from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

#url for app
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/wakaf_admin'}, name='logout'),
    url(r'^tables/', tables, name='tables'),

]
