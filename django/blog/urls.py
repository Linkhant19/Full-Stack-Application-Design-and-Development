## blog/urls.py
## description: the app-specific URLs for the blog app

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for the blog app
urlpatterns = [
    # for a class-based view, use .as_view()
    path(r'', views.RandomArticleView.as_view(), name='random'),
    path(r'show_all_articles', views.ShowAllView.as_view(), name='show_all_articles'), 
    path(r'article/<int:pk>', views.ArticleView.as_view(), name='article'),
    # path(r'create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path(r'article/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'),
    path(r'create_article', views.CreateArticleView.as_view(), name='create_article'),
]