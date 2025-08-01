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

'''
from django.shortcuts import render
from .models import Quote

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

'''

from django.shortcuts import render, redirect  # Tools to show pages and redirect
from .forms import QuoteForm  # Import the form we just created
from .models import Quote


def home(request):
    # Get all quotes from the database
    quotes = Quote.objects.all()
    
    # Pass the quotes to the template
    return render(request, 'quotes/home.html', {'quotes': quotes})


# View for adding a new quote
def add_quote(request):
    if request.method == 'POST':
        # If the form was submitted, load data into the form
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new quote to the database
            return redirect('home')  # After saving, go back to home page
    else:
        # If it's a GET request, just show the empty form
        form = QuoteForm()
    
    return render(request, 'quotes/add_quote.html', {'form': form})
