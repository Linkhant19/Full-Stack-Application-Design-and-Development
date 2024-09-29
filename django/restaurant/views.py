from django.shortcuts import render, redirect, HttpResponse
import time
import random
# Create your views here.

Special_menu = ['Unicorn Horns', 'Pumpkin Spice Latte', 'Cinnamon Dolce Latte', 'Chocolate Chip Cookie']

def main(request):
    """
    main page for our restaurant.
    """
    template_name = 'restaurant/main.html'
    return render(request, template_name)

def order(request):
    """
    order page for our restaurant. This will handle the order form request.
    """
    template_name = 'restaurant/order.html'
    context = {
        'current_time': time.ctime(),
        # select a random item from the special menu
        'special_item': random.choice(Special_menu),
        
    }
    return render(request, template_name, context)

def confirmation(request):
    '''Handle the order submission. 
    Read out the order data. 
    Generate a response.'''

    template_name = 'restaurant/confirmation.html'
    
    # check if the request is a POST (vs GET)
    if request.POST:
        # read the form data into python variables:
        name = request.POST['name']

        # package the data up to be used in response
        context = {
            'name': name,
            'time': time.ctime(),
        }

        # generate a response
        return render(request, template_name, context)

    # this is the "best" solution: redirect to the correct url. 
    return redirect("show_form")

