from django.shortcuts import render
from .models import Quote
import random

def home(request):
    quotes = list(Quote.objects.all())  # Get all quotes from DB
    if quotes:
        quote = random.choice(quotes)   # Pick a random quote
    else:
        quote = None
    return render(request, 'quotes/home.html', {'quote': quote})
