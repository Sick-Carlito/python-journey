'''
from django.shortcuts import render

# Create your views here.


# quotes/views.py
import random
from django.http import HttpResponse

# List of quotes
quotes = [
    "Success is no accident.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones.",
    "Don’t stop until you’re proud."
]

# View function to show a random quote
def show_quote(request):
    quote = random.choice(quotes)
    return HttpResponse(f"<h2>{quote}</h2>")

'''

from django.shortcuts import render
from .models import Quote

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

