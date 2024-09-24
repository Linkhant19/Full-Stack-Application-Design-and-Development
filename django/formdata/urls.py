# formdata/urls.py

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for the formdata app
urlpatterns = [
    path(r'', views.show_form, name='show_form'),
    path(r'submit', views.submit, name='submit'),
]