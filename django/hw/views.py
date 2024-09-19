## hw/views.py
## description: the logic to handle URL requests

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# Create your views here.

# should match the name from the urls.py
# def home(request):
#     """A function to respond to the /hw URL.
#     """

#     # create some text
#     response_text = f'''<html>
#     <body>
#     <h1>Hello, world!</h1>
#     <p>This is our first django web page!</p>
#     <hr>
#     This page was generated at {time.ctime()}.
#     </body></html>'''

#     # return response to the client
#     return HttpResponse(response_text)

def home(request):
    """
    A function to respond to the /hw URL.
    This function will delegate work to an HTML template.
    """

    # templates is the default folder for django so no need to specify.
    # this template will present the response.
    template_name = 'hw/home.html'

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        'letter1': chr(random.randint(65, 90)), # A-Z
        'letter2': chr(random.randint(65, 90)), # A-Z
        'number': random.randint(0, 100), # 0-100
    }

    return render(request, template_name, context)

def about(request):
    """
    A function to respond to the /hw/about URL.
    This function will delegate work to an HTML template.
    """

    # templates is the default folder for django so no need to specify.
    # this template will present the response.
    template_name = 'hw/about.html'

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        
    }

    return render(request, template_name, context)

