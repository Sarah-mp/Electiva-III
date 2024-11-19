from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

# Decorador para restringir acceso a usuarios que no sean administradores
def solo_admin(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.usuario.rol != 'Administrador':  # Verifica si el rol no es "Administrador"
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return view_func(request, *args, **kwargs)
    return wrapper

def solo_lider(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.usuario.rol != 'Líder de Proyecto':
            return redirect('login')  # Redirige al login o a una página de acceso denegado
        return func(request, *args, **kwargs)
    return wrapper


