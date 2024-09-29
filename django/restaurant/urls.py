# restaurant/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), # the first URL. main page
    path('order/', views.order, name='order'), # new order page
    path('confirmation/', views.confirmation, name='confirmation'), # new submit page
]