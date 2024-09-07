from contextlib import redirect_stderr
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import*
from django.contrib import messages


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


# Crud de libros

def ver_libros(request):
    query = Libro.objects.all() # filter   get 
    contexto = {"libros": query}
    return render(request, "libros/ver_libros.html",  contexto)

def eliminar_libro(request, id):
    try:
        query = Libro.objects.get(pk = id)
        query.delete()
        messages.success(request, "El libro fue eliminado correctamente!!")
    except:
        messages.error(request, "Ocurrió un error, intente de nuevo...")
    
    return redirect(ver_libros)

def agregar_libro(request):
    if request.method == "POST":
        #procesar datos
        pass
    else:
        #pintar formulario
        return render(request,"libros/formulario_libro.html")
    
       

