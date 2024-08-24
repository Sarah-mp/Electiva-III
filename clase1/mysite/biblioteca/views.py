from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

#vistas  basadas en

def index(request):
    print ("hola mundo...")
    return render(request, "index.html")

def vender (request):
    return render(request, "vender.html")

def prestar_libro (request):
    return render(request, "prestar_libro.html")

def leer(request, num1, num2):
    return HttpResponse(f"la suma es: {num1 + num2} ")

def sumadora(request):
    return render(request, "formulario_suma.html")

def suma(request):
    num1=int(request.POST.get("num1"))
    num2=int(request.POST.get("num2"))
    return HttpResponse(f"la suma es: {num1 + num2}")
