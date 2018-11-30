from django.conf.urls import url
from .views import home
#url for app
urlpatterns = [
    url(r'^$', home, name='home'),
]
