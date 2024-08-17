from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#vistas  basadas en

def index(request):
    print ("hola mundo...")
    return HttpResponse("<h1 style='color:blue;'>Hola mundo..</h1> <a href='vender/'>vender</a>")

def vender (request):
    return HttpResponse("Estamos vendiendo libros...")
