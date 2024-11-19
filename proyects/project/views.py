from django.shortcuts import render, redirect, get_object_or_404
from .decorators import solo_admin, solo_lider
import json

from django.contrib.auth import authenticate, login, logout
from .models import Usuario, Equipo, Tarea, Desarrollador,  Comentario,  LiderProyecto 
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

# Vista de inicio de sesión
def login_view(request):
    error = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validar que los campos no estén vacíos
        if not email or not password:
            error = "Por favor, completa todos los campos."
        else:
            try:
                # Buscar el usuario por correo electrónico
                usuario = Usuario.objects.get(correo_electronico=email)
                # Verificar la contraseña (esto es simple; considera usar hashing más adelante)
                if usuario and usuario.contrasena == password:
                    # Guardar el usuario en la sesión
                    request.session['usuario_id'] = usuario.id
                    request.session['rol'] = usuario.rol

                    # Redirigir a la página correspondiente según el rol
                    if usuario.rol == 'Administrador':
                        return redirect('admin_home')
                    elif usuario.rol == 'Líder de Proyecto':
                        return redirect('lider_home')
                    elif usuario.rol == 'Desarrollador':
                        return redirect('desarrollador_home')
                else:
                    error = "Correo o contraseña incorrectos."
            except Usuario.DoesNotExist:
                error = "Usuario no encontrado."

    return render(request, "login.html", {"error": error})

# Vista de cierre de sesión
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de inicio de sesión


# Vista de inicio para el administrador
def admin_home(request):
    return render(request, 'admin_home.html')

# Vista de inicio para el líder de proyecto
def solo_lider(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('rol') == 'Líder de Proyecto':
            return view_func(request, *args, **kwargs)
        else:
            # Redirige al home si el usuario no es un líder de proyecto
            return redirect('index')  # Cambia 'index' por la URL de tu home
    return wrapper

def lider_home(request):
    return render(request, 'lider_home.html')

# Vista de inicio para el desarrollador
def desarrollador_home(request):
    return render(request, 'desarrollador_home.html')

from django.shortcuts import render, redirect
from .models import Usuario

def gestion_usuarios(request):
    # Obtener todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.POST.get("nombre")
        correo_electronico = request.POST.get("correo_electronico")
        contrasena = request.POST.get("contrasena")
        rol = request.POST.get("rol")

        # Crear un nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, correo_electronico=correo_electronico, contrasena=contrasena, rol=rol)
        nuevo_usuario.save()

        # Redirigir a la misma página después de la creación
        return redirect("gestion_usuarios")

    return render(request, "gestion_usuarios.html", {"usuarios": usuarios})

# Vista para editar un usuario
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == "POST":
        usuario.nombre = request.POST.get("nombre")
        usuario.correo_electronico = request.POST.get("correo_electronico")
        usuario.contrasena = request.POST.get("contrasena")
        usuario.rol = request.POST.get("rol")
        usuario.save()
        return redirect("gestion_usuarios")

    return render(request, "editar_usuario.html", {"usuario": usuario})

# Vista para eliminar un usuario
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect("gestion_usuarios")


from .models import Equipo

# Vista para listar equipos
def listar_equipos(request):
    equipos = Equipo.objects.all()
    usuarios = Usuario.objects.all()  # O filtra si solo necesitas desarrolladores
    return render(request, 'gestion_equipos.html', {'equipos': equipos, 'usuarios': usuarios})

# Vista para crear un equipo
def crear_equipo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        equipo = Equipo.objects.create(nombre=nombre, descripcion=descripcion)

        # Obtener los IDs de los usuarios seleccionados y añadirlos al equipo
        miembros_ids = request.POST.getlist('miembros')
        usuarios_seleccionados = Usuario.objects.filter(id__in=miembros_ids)
        equipo.miembros.set(usuarios_seleccionados)

        return redirect('listar_equipos')

    # Obtener todos los usuarios (modificar si necesitas filtrar solo desarrolladores)
    usuarios = Usuario.objects.all()
    return render(request, 'crear_equipo.html', {'usuarios': usuarios})

# Vista para editar un equipo
def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)

    if request.method == 'POST':
        equipo.nombre = request.POST['nombre']
        equipo.descripcion = request.POST['descripcion']
        equipo.save()

        miembros_ids = request.POST.getlist('miembros')
        usuarios_seleccionados = Usuario.objects.filter(id__in=miembros_ids)
        equipo.miembros.set(usuarios_seleccionados)

        return redirect('listar_equipos')
    

    # Consulta de los miembros actuales y desarrolladores disponibles
    miembros_actuales = equipo.miembros.all()
    desarrolladores_disponibles = Usuario.objects.exclude(id__in=miembros_actuales.values_list('id', flat=True))


    return render(request, 'editar_equipo.html', {
        'equipo': equipo,
        'miembros_actuales': miembros_actuales,
        'desarrolladores_disponibles': desarrolladores_disponibles,
    })

# Vista para eliminar un equipo
def eliminar_equipo(request, equipo_id):

    equipo = get_object_or_404(Equipo, id=equipo_id)
    equipo.delete()
    return redirect('listar_equipos')


def gestion_tareas(request):
    tareas = Tarea.objects.all()
    desarrolladores = Desarrollador.objects.all()
    equipos = Equipo.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_limite = request.POST.get('fecha_limite')
        prioridad = request.POST.get('prioridad')
        estado = request.POST.get('estado')
        asignado_a_id = request.POST.get('asignado_a')
        equipo_id = request.POST.get('equipo')  # Nuevo campo

        if titulo and descripcion and fecha_limite and prioridad and estado and asignado_a_id and equipo_id:
            asignado_a = get_object_or_404(Desarrollador, id=asignado_a_id)
            equipo = get_object_or_404(Equipo, id=equipo_id)  # Obtener el equipo

            # Crear la tarea con el equipo asignado
            Tarea.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha_limite=fecha_limite,
                prioridad=prioridad,
                estado=estado,
                asignado_a=asignado_a,
                equipo=equipo  # Asignar el equipo
            )
            return redirect('gestion_tareas')
        else:
            print("Error: faltan campos en el formulario.")

    return render(request, 'gestion_tareas.html', {
        'tareas': tareas,
        'desarrolladores': desarrolladores,
        'equipos': equipos  # Pasar los equipos al contexto
    })

def añadir_comentario(request, tarea_id):
    if request.method == 'POST':
        texto = request.POST.get('comentario')
        if texto:
            tarea = get_object_or_404(Tarea, id=tarea_id)
            Comentario.objects.create(
                tarea=tarea,
                autor=request.user,  # Asegúrate de que `request.user` esté disponible
                texto=texto
            )
        return redirect('gestion_tareas')

def actualizar_tarea(request, tarea_id):
    if request.method == 'POST':
        tarea = get_object_or_404(Tarea, id=tarea_id)
        data = json.loads(request.body)  # Asegúrate de importar 'json' también
        estado = data.get('estado')
        comentario_texto = data.get('comentario')

        if estado:
            tarea.estado = estado
            tarea.save()

        # Si hay un comentario, guárdalo también
        if comentario_texto:
            Comentario.objects.create(tarea=tarea, texto=comentario_texto, autor=request.user)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

def asignar_lider(request):
    if request.method == 'POST':
        lider_id = request.POST.get('lider')
        equipo_id = request.POST.get('equipo')

        if lider_id and equipo_id:
            lider = get_object_or_404(Usuario, id=lider_id, rol='Líder de Proyecto')
            equipo = get_object_or_404(Equipo, id=equipo_id)

            # Crear o actualizar la asignación del líder
            lider_proyecto, created = LiderProyecto.objects.update_or_create(
                usuario=lider,
                defaults={'equipo': equipo}
            )

            return redirect('asignar_lider')

    # Aquí aplicamos el filtro para obtener solo los líderes
    lideres = Usuario.objects.filter(rol='Líder de Proyecto')
    equipos = Equipo.objects.all()

    return render(request, 'asignar_lider.html', {'lideres': lideres, 'equipos': equipos})
