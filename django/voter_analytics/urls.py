# voter_analytics/urls.py

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for the voter_analytics app
urlpatterns = [
    path(r'', views.ResultsListView.as_view(), name='home'),
    path(r'results', views.ResultsListView.as_view(), name='results'),
    path(r'voter/<int:pk>', views.VoterDetailView.as_view(), name='voter_detail'),
    path(r'graphs', views.GraphsView.as_view(), name='graphs'),
]