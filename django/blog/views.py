# blog/views.py
# views to show the blog application

from django.shortcuts import render

from . models import *
from django.views.generic import ListView

# this is a class based view
class ShowAllView(ListView):
    '''The view to show all articles.'''
    
    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'
