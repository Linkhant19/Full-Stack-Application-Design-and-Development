# blog/views.py
# views to show the blog application

from django.shortcuts import render

from . models import *
from django.views.generic import ListView, DetailView
import random

# this is a class based view
class ShowAllView(ListView):
    '''The view to show all articles.'''
    
    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

class RandomArticleView(DetailView):
    '''Show one article selected at random.'''

    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article' # naming it singular

    # AttributeError: Generic detail view RandomArticleView must be called with either pk or slug
    # one solution: implement the get_object method
    def get_object(self):
        '''Return the instance of the Article object to show.'''

        # get all articles
        all_articles = Article.objects.all() # SELECT *

        # get a random article
        return random.choice(all_articles)

class ArticleView(DetailView):
    '''Show one article by its primary key.'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'


