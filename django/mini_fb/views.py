# mini_fb/views.py
# views to show the mini_fb application

from django.shortcuts import render

from . models import *
from django.views.generic import ListView

# this is a class based view
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'