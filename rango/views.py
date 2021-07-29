from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category



def about(request):

    return render(request, 'rango/about.html')

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)