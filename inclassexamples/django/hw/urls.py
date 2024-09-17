## hw/urls.py
## description: the app-specific URLs for the hw app

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for the hw app
urlpatterns = [
    path(r'', views.home, name='home'), # the first URL. main page
]