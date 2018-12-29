from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'assets/$', assets, name='assets'),
    url(r'volunteer/$', volunteer, name='volunteer'),
]
