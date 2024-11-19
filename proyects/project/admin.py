from django.contrib import admin
from .models import Usuario, LiderProyecto, Desarrollador, Equipo, Tarea

# Configuración del modelo Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('correo_electronico', 'rol')
    list_filter = ('rol',)
    search_fields = ('correo_electronico',)
    fields = ('correo_electronico', 'contrasena', 'rol')
admin.site.register(Usuario, UsuarioAdmin)

# Configuración del modelo LiderProyecto
class LiderProyectoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'equipo')
    search_fields = ('usuario__correo_electronico',)

admin.site.register(LiderProyecto, LiderProyectoAdmin)

# Configuración del modelo Desarrollador
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    search_fields = ('usuario__correo_electronico',)

admin.site.register(Desarrollador, DesarrolladorAdmin)

# Configuración del modelo Equipo
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    filter_horizontal = ('miembros',)  # Para facilitar la selección de miembros

admin.site.register(Equipo, EquipoAdmin)

# Configuración del modelo Tarea
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'equipo', 'asignado_a', 'estado', 'fecha_limite')
    list_filter = ('estado', 'equipo')
    search_fields = ('titulo', 'descripcion')

admin.site.register(Tarea, TareaAdmin)

