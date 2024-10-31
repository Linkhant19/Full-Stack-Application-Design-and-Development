# blog/models.py
# define data models (objects) for use in the blog application

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    '''Encapsulate the data for a blog Article by some author.'''

    # create a 1 to many relationship with the User model
    # each Article will associate with one User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # data attributes:
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    # image_url = models.URLField(blank=True) 

    image_file = models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f"{self.title} by {self.author}"

    def get_comments(self):
        '''Retrieve all comments for this article.'''
        # use the ORM to filter Comments where this object is the FK
        # instance of Article is the FK
        comments = Comment.objects.filter(article=self)
        return comments

    def get_absolute_url(self):
        '''return the URL to view one instance of this object.'''
        # self.pk is the primary key of the object instance
        return reverse('article', kwargs={'pk': self.pk})

class Comment(models.Model):
    '''Encapsulate a comment on an article.'''

    # create a 1 to many relationship with the Article model
    article = models.ForeignKey("Article", on_delete=models.CASCADE) # if the article is deleted, delete all comments related to it
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the object.'''
        return f'{self.text}'
