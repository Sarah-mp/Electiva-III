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
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        no_paginas = request.POST.get("no_paginas")
        fecha_publicacion = request.POST.get("fecha_publicacion")
        clasificacion = request.POST.get("clasificacion")

        # SQl
        # insert into libros() values(titulo, autor,...)
        try:
            query = Libro(
                titulo=titulo, 
                autor=autor, 
                no_paginas= no_paginas, 
                fecha_publicacion = fecha_publicacion,
                clasificacion=clasificacion
                )
            query.save()
            messages.success(request, "El libro fue agregado correctamente!!")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al agregar el libro{e}")
            
        return redirect(ver_libros)

    else:
        #pintar formulario
        return render(request,"libros/formulario_libro.html")
    
def editar_libros(request, id):
    if request.method == "POST":
        # procesar la actualización de datos
        try:
            query = Libro.objects.get(pk = id)
            query.titulo = request.POST.get("titulo")
            query.autor = request.POST.get("autor")
            query.no_paginas = request.POST.get("no_paginas")
            query.fecha_publicacion = request.POST.get("fecha_publicacion")
            query.clasificacion = request.POST.get("clasificacion")
            query.save()

            messages.success(request, "El libro fue actualizado correctamente!!")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al actualizar el libro{e}")
        return redirect("ver_libros")


    else:
        #consultar el registro y mostrar en el formulario los datos actuales
        query = Libro.objects.get(pk = id)
        contexto = {"libros": query}
        return render(request, "libros/formulario_libro.html",  contexto)
    