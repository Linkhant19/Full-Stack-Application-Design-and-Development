from django.shortcuts import render
from django.templatetags.static import static
import random
import time


# List of quotes and images
quotes_list = ["I think the perfection of love is that it's not perfect.", 
    "The worst kind of person is someone who makes someone feel bad, dumb or stupid for being excited about something", 
    "Love is a ruthless game, Unless you play it good and right.",
    "In one conversation, I tore down the whole sky.",
    "Was tonight the night you realized how solitary, how alone you really are, no matter how high you climb. The elevation just makes it colder.",
    "For all of us who have tossed and turned and decided to keep the lanterns lit and go searching. Hoping that just maybe, when the clock strikes twelve ... we'll meet ourselves.",
]
images_list = images_list = [
    static('images/taylor1.jpg'),
    static('images/taylor2.jpg'),
    static('images/taylor3.jpg'),
    static('images/taylor4.jpg'),
    static('images/taylor5.jpg'),
    static('images/taylor6.jpg'),
]

def quotes(request):
    """A function to respond to the /quote URL.
    This function will delegate work to an HTML template.
    """

    # templates is the default folder for django so no need to specify.
    # this template will present the response.
    template_name = 'quotes/quote.html'

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        'quote': random.choice(quotes_list),
        'image': images_list[random.randint(0, len(images_list)-1)],
    }
    return render(request, template_name, context)

# show_all : the view to show all quotes.
# This view will add the entire list of quotes and images to the context data for the view. Finally, delegate presentation to the show_all.html HTML template for display.

def show_all(request):
    """A function to respond to the /show_all URL.
    This function will delegate work to an HTML template.
    """

    # templates is the default folder for django so no need to specify.
    # this template will present the response.
    template_name = 'quotes/show_all.html'

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
        'quotes': quotes_list,
        'images': images_list,
    }
    return render(request, template_name, context)
