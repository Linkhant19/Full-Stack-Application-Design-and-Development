# The structure of this web application will involve the following URL patterns:

# / : the main page, which will display a picture of a famous or notable person of your choosing and a quote that this person said or wrote. The quote and image will be selected at random from a list of images/quote.

# /quote : the same as /, to generate one quote and one image at random.

# /show_all : an ancillary page which will show all quotes and images.

# /about : an about page with short biographical information about the person whose quotes you are displaying, as well as a note about the creator of this web application (you).

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for the quotes app
urlpatterns = [
    path(r'', views.quote, name='quote'), # the first URL. main page
    # path(r'quote', views.quotes, name='quote'), # new quote page
    path(r'show_all', views.show_all, name='show_all'), # new show_all page
    path(r'about', views.about, name='about'), # new about page
]
