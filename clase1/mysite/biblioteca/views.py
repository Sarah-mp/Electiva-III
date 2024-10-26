from contextlib import redirect_stderr
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Libro, Reserva,Usuario, Prestamo
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')
        # select * form Usuario where email = '' and clave = ''
        try:
            q = Usuario.objects.get(correo=correo, clave=clave)
            messages.success(request, f'Bienvenido!!')
            datos = {
                "id":q.id,
                "nombre":q.nombre_completo,
                "rol":q.rol
            }
            request.session['logueado'] = datos
            return redirect('index')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña no válidos.')
            return redirect('login')
    else: 
        control = request.session.get('logueado', False)
        if not control:
         return render(request, 'login/login_form.html')
        else:
            return redirect('index')
    

def logout(request):
    try:
        del request.session['logueado']
        return redirect('login')
    except:
        messages.error(request, "Error, Intente de Nuevo...")
        return redirect('index')

def index(request):
    control = request.session.get('logueado', False)
    if control:
        return render(request, "index.html")
    else:
        messages.warning(request, "Por favor inicie sesión...")
        return redirect('login')


#vistas  basadas en

def vender (request):
    control = request.session.get('logueado', False)
    if control and control["rol"] == 'B':
        messages.info(request, "No estás autorizado para acceder a este módulo...")
        return redirect('index')
    else:
     return render(request, "vender.html",)

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
    control = request.session.get('logueado', False)
    if control:
        query = Libro.objects.all() # filter   get 
        contexto = {"libros": query}
        return render(request, "libros/ver_libros.html",  contexto)
    else:
        messages.warning(request, "Por favor inicie sesión...")
        return redirect('index')
    

 

def eliminar_libro(request, id):
    control = request.session.get('logueado', False)
    if control and control["rol"] == 'A':
        try:
            query = Libro.objects.get(pk = id)
            query.delete()
            messages.success(request, "El libro fue eliminado correctamente!!")
        except:
            messages.error(request, "Ocurrió un error, intente de nuevo...")
        return redirect(ver_libros)

    else:
        messages.warning(request, "No estás autorizado para acceder a este módulo...")
        return redirect('ver_libros')

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
    

# reservas 

def agregar_reserva(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        libro_id = request.POST.get("libro")
        fecha_reserva = request.POST.get("fecha_reserva")
        fecha_devolucion = request.POST.get("fecha_devolucion")
        try:
            libro = Libro.objects.get(id=libro_id)
            reserva = Reserva(
                usuario=usuario,
                libro=libro,
                fecha_reserva=fecha_reserva,
                fecha_devolucion=fecha_devolucion
            )
            reserva.save()
            messages.success(request, "La reserva fue creada correctamente.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al crear la reserva: {e}")
        return redirect('ver_reservas')
    else:
        libros = Libro.objects.all()
        return render(request, "libros/agregar_reserva.html", {'libros': libros})

# Vista para ver todas las reservas
def ver_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "libros/ver_reservas.html", {'reservas': reservas})

# Vista para eliminar una reserva
def eliminar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
        messages.success(request, "La reserva fue eliminada correctamente.")
    except Exception as e:
        messages.error(request, f"Ocurrió un error al eliminar la reserva: {e}")
    return redirect('ver_reservas')

# Vista para editar una reserva
def editar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        if request.method == "POST":
            reserva.usuario = request.POST.get("usuario")
            libro_id = request.POST.get("libro")
            reserva.fecha_reserva = request.POST.get("fecha_reserva")
            reserva.fecha_devolucion = request.POST.get("fecha_devolucion")
            reserva.libro = Libro.objects.get(id=libro_id)
            reserva.save()
            messages.success(request, "La reserva fue actualizada correctamente.")
            return redirect('ver_reservas')
        else:
            libros = Libro.objects.all()
            return render(request, "libros/editar_reserva.html", {'reserva': reserva, 'libros': libros})
    except Exception as e:
        messages.error(request, f"Ocurrió un error al editar la reserva: {e}")
        return redirect('ver_reservas')


def prestamos(request):
    q = Prestamo.objects.all()
    contexto = {"data": q}
    return render(request, 'libros/prestamos.html', contexto)

def eliminar_prestamo(request, id):
    control = request.session.get('logueado', False)
    if control and control["rol"] == 'A':
        try:
            query = Prestamo.objects.get(pk = id)
            query.delete()
            messages.success(request, "El préstamo fue eliminado correctamente!!")
        except:
            messages.error(request, "Ocurrió un error, intente de nuevo...")
        return redirect('prestamos')

    else:
        messages.warning(request, "No estás autorizado para acceder a este módulo...")
        return redirect('prestamos')

def agregar_prestamo(request):
    if request.method == "POST":
        #procesar datos 
        u = request.POST.get("usuario")
        usuario = Usuario.objects.get(pk = u)
        li = request.POST.get("libro")
        libro = Libro.objects.get(pk = li)
        fecha_devolucion = request.POST.get("fecha_devolucion")
        estado = request.POST.get("estado")
        observaciones = request.POST.get("observaciones")

        # SQl
        # insert into libros() values(titulo, autor,...)
        try:
            query = Prestamo(
                usuario=usuario, 
                libro=libro, 
                fecha_devolucion= fecha_devolucion, 
                estado = estado,
                observaciones=observaciones
                )
            query.save()
            messages.success(request, "El préstamo fue agregado correctamente!!")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al agregar el pretamo{e}")
            
        return redirect('ver_libros')

    else:
        #pintar formulario
        usuarios = Usuario.objects.all()
        libros = Libro.objects.all()
        contexto = {
            'users': usuarios, 
            'books': libros
        }
        return render(request,"libros/formulario_prestamos.html", contexto)

def editar_prestamo(request, id):
    if request.method == "POST":
        # procesar la actualización de datos
        try:
            query = Prestamo.objects.get(pk = id)
            query.usuario = request.POST.get("usuario")
            query.autor = request.POST.get("autor")
            query.fecha_devolucion = request.POST.get("fecha_devolucion")
            query.estado = request.POST.get("estado")
            query.observaciones = request.POST.get("observaciones")
            query.save()

            messages.success(request, "El préstamo fue actualizado correctamente!!")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al actualizar el préstamo{e}")

        return redirect("prestamos/")


    else:
        #consultar el registro y mostrar en el formulario los datos actuales
        query = Prestamo.objects.get(pk = id)
        usuarios = Usuario.objects.all()
        libros = Libro.objects.all()
        contexto = {
            "prestamos": query,
            'users': usuarios, 
            'books': libros
        }
        return render(request, "libros/formulario_prestamos.html",  contexto)
    