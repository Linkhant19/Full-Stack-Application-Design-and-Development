## blog/urls.py
## description: the app-specific URLs for the blog app

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for the blog app
urlpatterns = [
    # for a class-based view, use .as_view()
    path(r'', views.ShowAllView.as_view(), name='show_all'), # the first URL. main page
]