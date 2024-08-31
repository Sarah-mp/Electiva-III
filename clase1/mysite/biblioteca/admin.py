from django.contrib import admin
from .models import*

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "autor", "no_paginas", "fecha_publicacion", "clasificacion"]
    search_fields =["titulo", "autor"]
    list_filter = ["clasificacion", "fecha_publicacion"]

admin.site.register(Libro, LibroAdmin)
