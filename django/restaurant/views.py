from django.shortcuts import render, redirect, HttpResponse
import time
import random
# Create your views here.

Special_menu = ['Unicorn Horn Soup', 'Potato Spice Latte', 'Cinnamon Roll Icecream', 'Chocolate Flower Cookie']

def main(request):
    """
    main page for our restaurant.
    """
    template_name = 'restaurant/main.html'
    context = {
        'current_time': time.ctime(),
        'image': "../static/images/restaurant.jpg",
    }
    return render(request, template_name, context)

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
        
        # all the dishes
        wings = request.POST.get('wings')
        if wings:
            wings_price = 12.99
            wings_name = "chicken wings"
        else:
            wings_price = 0

        
        sushi = request.POST.get('sushi')
        if sushi:
            sushi_price = 15.99
        else:
            sushi_price = 0
        mario = request.POST.get('mario')
        if mario:
            mario_price = 34.99
        else:
            mario_price = 0
        brain = request.POST.get('brain')
        if brain:
            brain_price = 26.99
        else:
            brain_price = 0
        soup = request.POST.get('soup')
        if soup:
            soup_price = 6.99
        else:
            soup_price = 0
        special = request.POST.get('special')
        if special:
            special_price = 100
        else:
            special_price = 0

        # all the details
        details = request.POST.get('details')
        if details:
            instructions = details
        else:
            instructions = "No special instructions"


        # package the data up to be used in response
        context = {
            'name': name,
            'current_time': time.ctime(),
            # ready time will be randomly generated between 30 and 60 minutes from now.
            'ready_time': time.ctime(time.time() + random.randint(1800, 3600)),

            # calculate the total price
            'total_price': wings_price + sushi_price + mario_price + brain_price + soup_price + special_price,
            'details': instructions,
        }

        # generate a response
        return render(request, template_name, context)

    # this is the "best" solution: redirect to the correct url. 
    return redirect("order")

