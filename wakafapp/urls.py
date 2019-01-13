from django.conf.urls import url
from .views import *
#url for app
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'program/$', program, name='program'),
    url(r'volunteer/$', volunteer, name='volunteer'),
    url(r'artikel/$', artikel, name='artikel'),
    url(r'aboutUs/$', aboutUs, name='aboutUs'),
    url(r'^add_donatur/', add_donatur, name='add_donatur'),
    url(r'^add_relawan/', add_relawan, name='add_relawan'),
    url(r'coba/$', coba, name='coba'),
]
