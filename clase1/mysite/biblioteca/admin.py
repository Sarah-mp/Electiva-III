from django.contrib import admin
from .models import Libro, Reserva, Usuario, Prestamo

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "autor", "no_paginas", "fecha_publicacion", "clasificacion"]
    search_fields =["titulo", "autor"]
    list_filter = ["clasificacion", "fecha_publicacion"]

admin.site.register(Libro, LibroAdmin)

# Configuración del admin para Reserva
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'libro', 'fecha_reserva', 'fecha_devolucion']
    list_filter = ['fecha_reserva', 'fecha_devolucion']
    search_fields = ['libro__titulo', 'usuario__username']

admin.site.register(Reserva, ReservaAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_completo', 'correo', 'rol']

admin.site.register(Usuario, UserAdmin)


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'libro', 'fecha_reserva', 'fecha_devolucion', 'estado', 'observaciones']
    list_filter = ['estado', 'fecha_reserva', 'fecha_devolucion']
    search_fields = ['libro__titulo', 'usuario__username']