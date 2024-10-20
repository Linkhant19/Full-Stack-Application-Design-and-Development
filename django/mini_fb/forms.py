# mini_fb/forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create Profile data.'''
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.EmailField(label="Email", required=True)
    class Meta:
        '''associate this form with the Profile model'''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email', 'image_url']


class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create StatusMessage data.'''
    class Meta:
        '''associate this form with the StatusMessage model'''
        model = StatusMessage
        fields = ['message']


class UpdateProfileForm(forms.ModelForm):
    '''A form to update Profile data.'''
    class Meta:
        '''associate this form with the Profile model'''
        model = Profile
        fields = ['city', 'email', 'image_url']