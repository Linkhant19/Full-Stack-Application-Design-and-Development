## mini_fb/urls.py
## description: the app-specific URLs for the mini_fb app

from django.urls import path
from . import views

# create a list of URLs for the mini_fb app
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name='show_all_fb'), # the first URL. main page
]