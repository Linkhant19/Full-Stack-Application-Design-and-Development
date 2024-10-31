# blog/views.py
# views to show the blog application

from typing import Any
from django.shortcuts import render
from django.urls import reverse

from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 

import random

# this is a class based view
class ShowAllView(ListView):
    '''The view to show all articles.'''
    
    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

    def dispatch(self, *args, **kwargs):
        '''
        implement this method to add some tracing.
        '''
        print(f'self.request.user={self.request.user}')
        return super().dispatch(*args, **kwargs)

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


# the order in which we provide these superclasses matter. In this case, LoginRequiredMixin has precedence. 
class CreateCommentView(LoginRequiredMixin, CreateView):
    '''a view to show/process the create comment form: 
    on GET: send back the form
    on POST: read the form data,create an instance of Comment; save to database; redirect to a URL'''
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    # what to do after form submission?
    def get_success_url(self) -> str: 
        '''return the URL to redirect to after successful create'''
        # return "/blog/show_all"
        # return reverse("show_all_articles")
        return reverse('article', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        '''this method executes after form submission'''

        print(f'CreateCommentView.form_valid: form={form.cleaned_data}')
        print(f'CreateCommentView.form_valid: self.kwargs={self.kwargs}')
        
        # find the article with the primary key from the URL
        # self.kwargs is finding the article PK from the URL
        article = Article.objects.get(pk=self.kwargs['pk'])

        # attach the article to the new Comment
        # form.instance is the new Comment
        form.instance.article = article

        # delegate work to the superclass version of this method
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ''' 
        build the template context data --
        a dict of key-value pairs.
        '''

        # get the super class version of context data
        context = super().get_context_data(**kwargs)


        # find the article with the primary key from the URL
        # self.kwargs is finding the article PK from the URL
        article = Article.objects.get(pk=self.kwargs['pk'])

        # add the article to the context data
        context['article'] = article
        return context

class CreateArticleView(LoginRequiredMixin, CreateView):
    '''View to create a new Article instance.'''

    form_class = CreateArticleForm
    template_name = 'blog/create_article_form.html'

    def get_login_url(self) -> str:
        '''return the URL required for login.'''
        return reverse('login')

    def form_valid(self, form):
        '''Add some debugging statements.'''
        print(f'CreateArticleView.form_valid: form.cleaned_data={form.cleaned_data}')

        # find which user is logged in
        user = self.request.user
        print(f'CreateArticleView.form_valid: user={user}')

        # attach user to the new article instance
        form.instance.user = user

        # delegate work to superclass
        return super().form_valid(form)