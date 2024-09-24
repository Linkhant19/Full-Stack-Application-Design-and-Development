# formdata/views.py

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def show_form(request):
    '''Show the HTML form to the client.'''

    # use this template to produce the response
    template_name = 'formdata/form.html'
    return render(request, template_name)

def submit(request):
    '''Handle the form submission. 
    Read out the form data. 
    Generate a response.'''

    template_name = 'formdata/confirmation.html'

    print(request)
    
    # check if the request is a POST (vs GET)
    if request.POST:
        # read the form data into python variables:
        name = request.POST['name']
        favorite_color = request.POST['favorite_color']

        # package the data up to be used in response
        context = {
            'name': name,
            'favorite_color': favorite_color,
        }

        # generate a response
        return render(request, template_name, context)

    # this is an OK solution: graceful failure.
    # return HttpResponse("Nope. Sorry.")

    # this is a better solution, but shows the wrong URL in the link.
    # if client got here by making a GET on this url, send back the form
    # template_name = 'formdata/form.html'
    # return render(request, template_name)

    # this is the "best" solution: redirect to the correct url. 
    return redirect("show_form")