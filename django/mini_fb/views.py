# mini_fb/views.py
# views to show the mini_fb application

from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse

from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
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

        # modify the form_valid method to handle the uploading of files as follows:
        sm = form.save()
        # read the file from the form:
        files = self.request.FILES.getlist('files')

        # loop through the files and save them
        for file in files:
        # create a new Image object
            img = Image(status_message=sm, image_file=file)
            img.save()

        # delegate work to the superclass version of this method
        return super().form_valid(form)

    # what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''

        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})


class UpdateProfileView(UpdateView):
    '''
    class-based view called UpdateProfileView, which inherits from the generic UpdateView class.
    '''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'


class DeleteStatusMessageView(DeleteView):
    '''
    class-based view called DeleteStatusMessageView, which inherits from the generic DeleteView class.
    '''
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful delete'''
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
        # return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})

class UpdateStatusMessageView(UpdateView):
    '''
    class-based view called UpdateStatusMessageView, which inherits from the generic UpdateView class.
    '''
    model = StatusMessage
    form_class = UpdateStatusForm
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful update'''
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})


class CreateFriendView(View):
    '''
    class-based view called AddFriendView, which inherits from the generic View class.
    '''
    def dispatch(self, request, pk, other_pk):
        '''
        read the URL parameters (from self.kwargs), use the object manager to find the requisite Profile objects, and then call the Profile‘s add_friend method (from step 2, above).
        '''
        p1 = Profile.objects.get(pk=pk)
        p2 = Profile.objects.get(pk=other_pk)
        p1.add_friend(p2)
        return redirect('show_profile', pk=pk)


class ShowFriendSuggestionsView(DetailView):
    '''
    class-based view called ShowFriendSuggestionsView, which inherits from the generic DetailView class.
    '''
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'


class ShowNewsFeedView(DetailView):
    '''
    class-based view called ShowNewsFeedView, which inherits from the generic DetailView class.
    '''
    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'

    
