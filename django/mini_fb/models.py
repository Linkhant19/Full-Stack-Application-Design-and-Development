# mini_fb/models.py
# define data models (objects) for use in the mini_fb application

from django.db import models

class Profile(models.Model):
    '''Encapsulate the data for a user profile.'''
    # This Profile model will include the following data attributes: 
    # first name, last name, city, email address, and a profile image url.

    first_name = models.TextField(blank=False) # field is required
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    image_url = models.URLField(blank=True) # field is optional
