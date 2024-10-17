# mini_fb/views.py
# views to show the mini_fb application

from typing import Any
from django.shortcuts import render
from django.urls import reverse

from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView
import random

# this is a class based view
class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    '''
    class-based view called ShowProfilePageView, which inherits from the generic DetailView class.
    obtain data for one Profile record, and deleguate work to a template called show_profile.html to display that Profile.
    '''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    '''
    class-based view called CreateProfileView, which inherits from the generic CreateView class.
    on GET: send back the form
    on POST: read the form data,create an instance of Profile; save to database; redirect to a URL
    '''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_success_url(self):
        '''
        return the URL to redirect to after successful create
        '''
        return self.object.get_absolute_url()

class CreateStatusMessageView(CreateView):
    '''
    class-based view called CreateStatusMessageView, which inherits from the generic CreateView class.
    on GET: send back the form
    on POST: read the form data,create an instance of Status; save to database; redirect to a URL
    '''
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ''' 
        build the template context data --
        a dict of key-value pairs.
        '''

        # get the super class version of context data
        context = super().get_context_data(**kwargs)

        # find the profile with the primary key from the URL
        # self.kwargs is finding the profile PK from the URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        # add the profile to the context data
        context['profile'] = profile
        return context

    def form_valid(self, form):
        '''this method executes after form submission'''
        
        # find the profile with the primary key from the URL
        # self.kwargs is finding the profile PK from the URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        # attach the profile to the new Comment
        # form.instance is the new Comment
        form.instance.profile = profile

        # delegate work to the superclass version of this method
        return super().form_valid(form)

    # what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''

        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})
