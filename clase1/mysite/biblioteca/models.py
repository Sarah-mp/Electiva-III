from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=254)
    autor = models.CharField(max_length=100)
    no_paginas = models.IntegerField()
    fecha_publicacion = models.DateField(help_text= "Fecha Publicacion")
    CLASIFICAC = (
        (0, ""),
        (1, "Romance"),
        (2, "Aventura"),
        (3, "Ficción"),
    )
    clasificacion = models.IntegerField(choices=CLASIFICAC, default=0 )

    def __str__(self) -> str:
        return f"Título:{self.titulo} - Autor: {self.autor}"
    
