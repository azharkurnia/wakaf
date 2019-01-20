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
    url(r'thankyouVolunteer/$', thankyouVolunteer, name='thankyouVolunteer'),
    url(r'thankyouDonasi/$', thankyouDonasi, name='thankyouDonasi'),
    url(r'konfirmasi', konfirmasi, name='konfirmasi'),
    url(r'addBuktiTransfer', addBuktiTransfer, name='addBuktiTransfer'),
    url(r'thankyouKonfirmasi', thankyouKonfirmasi, name='thankyouKonfirmasi'),
    url(r'coba/$', coba, name='coba'),
]
