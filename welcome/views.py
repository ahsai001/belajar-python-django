from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request, name):
    context = {
        'name': name
        
    }
    return render(request, 'welcome/index.html',  context)