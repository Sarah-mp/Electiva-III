from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Rutas para las páginas de inicio de cada rol
    path('admin_home/', views.admin_home, name='admin_home'),
    path('lider_home/', views.lider_home, name='lider_home'),
    path('desarrollador_home/', views.desarrollador_home, name='desarrollador_home'),

    # Rutas para las funciones de administrador

    path('gestion-usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('editar-usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar-usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:equipo_id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('crear-equipo/', views.crear_equipo, name='crear_equipo'),
    path('tareas/', views.gestion_tareas, name='gestion_tareas'),
    path('tareas/<int:tarea_id>/añadir-comentario/', views.añadir_comentario, name='añadir_comentario'),
    path('tareas/actualizar/<int:tarea_id>/', views.actualizar_tarea, name='actualizar_tarea'),
    path('asignar-lider/', views.asignar_lider, name='asignar_lider'),
    




    # Rutas para las funciones de líder de proyecto
]