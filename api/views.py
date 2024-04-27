from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('hola mundo')

# Create your views here.
