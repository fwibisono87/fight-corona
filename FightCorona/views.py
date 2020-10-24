from django.shortcuts import render
from datetime import datetime, date

def landing_page(request):
    response = {}
    return render(request, 'global/home.html', response)