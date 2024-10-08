from django.contrib import admin
from .models import Libro, Reserva, Usuario

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

admin.site.register(Usuario)