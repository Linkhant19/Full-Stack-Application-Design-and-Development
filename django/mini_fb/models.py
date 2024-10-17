# mini_fb/models.py
# define data models (objects) for use in the mini_fb application

from django.db import models
from django.urls import reverse

class Profile(models.Model):
    '''Encapsulate the data for a user profile.'''
    # This Profile model will include the following data attributes: 
    # first name, last name, city, email address, and a profile image url.

    first_name = models.TextField(blank=False) # field is required
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    image_url = models.URLField(blank=True) # field is optional

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.first_name} {self.last_name}"

    # an accessor method get_status_messages to obtain all status messages for this Profile.
    def get_status_messages(self):
        '''Return all status messages for this Profile.'''
        status_messages = StatusMessage.objects.filter(profile=self).order_by('-timestamp')
        return status_messages

    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        # return reverse('show_all_profiles')
        return reverse('show_profile', kwargs={'pk': self.pk})

class StatusMessage(models.Model):
    '''Encapsulate the data for a status message.'''
    # timestamp (the time at which this status message was created/saved)
    # message (the text of the status message)
    # profile (the foreign key to indicate the relationship to the Profile of the creator of this message)

    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.message}"
