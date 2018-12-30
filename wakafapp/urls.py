from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'program/$', program, name='program'),
    url(r'volunteer/$', volunteer, name='volunteer'),
    url(r'article/$', article, name='article')
]
