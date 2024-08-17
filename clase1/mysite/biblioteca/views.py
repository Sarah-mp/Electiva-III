from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#vistas  basadas en

def index(request):
    print ("hola mundo...")
    return HttpResponse("Hola mundo..")
