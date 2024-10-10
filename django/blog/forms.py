# blog/forms.py

from django import forms
from .models import Comment

class CreateCommentForm(forms.ModelForm):
    '''A form to create Comment data.'''

    class Meta:
        '''associate this form with the Comment model'''
        model = Comment

        # fields = ['article', 'author', 'text', ]
        # remove the field because we want to connect to article number
        fields = ['author', 'text', ]