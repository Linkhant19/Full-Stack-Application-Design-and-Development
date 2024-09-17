## hw/views.py
## description: the logic to handle URL requests

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time

# Create your views here.

# should match the name from the urls.py
def home(request):
    """A function to respond to the /hw URL.
    """

    # create some text
    response_text = f'''<html>
    <body>
    <h1>Hello, world!</h1>
    <p>This is our first django web page!</p>
    <hr>
    This page was generated at {time.ctime()}.
    </body></html>'''

    # return response to the client
    return HttpResponse(response_text)
