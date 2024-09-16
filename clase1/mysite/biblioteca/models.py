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
    

# crear modelo 2

class Reserva(models.Model):
    usuario = models.CharField(max_length=100, help_text="Nombre del usuario que realiza la reserva")
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE, help_text="Libro reservado")
    fecha_reserva = models.DateField(help_text="Fecha en que se realiza la reserva")
    fecha_devolucion = models.DateField(help_text="Fecha en que debe devolverse el libro")

    def __str__(self):
        return f"{self.libro.titulo} reservado por {self.usuario} hasta {self.fecha_devolucion}"