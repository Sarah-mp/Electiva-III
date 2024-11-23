from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Modelo de Usuario con campo desplegable para el rol
class Usuario(models.Model):
    ADMINISTRADOR = 'Administrador'
    LIDER_PROYECTO = 'Líder de Proyecto'
    DESARROLLADOR = 'Desarrollador'

    ROLES = [
        (ADMINISTRADOR, 'Administrador'),
        (LIDER_PROYECTO, 'Líder de Proyecto'),
        (DESARROLLADOR, 'Desarrollador'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="Nombre predeterminado")
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, choices=ROLES, default=DESARROLLADOR)

    def __str__(self):
        return f"{self.nombre} ({self.correo_electronico}) - {self.rol}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripción")
    miembros = models.ManyToManyField(Usuario)  # Usar tu modelo Usuario

    def __str__(self):
        return self.nombre

# Modelo de Líder de Proyecto
class LiderProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
       return f"{self.usuario.nombre} - {self.equipo.nombre}"
    
# Modelo de Desarrollador
class Desarrollador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Desarrollador: {self.usuario.correo_electronico}" 

# Modelo de Tarea
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    observaciones = models.TextField(blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    asignado_a = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.tarea.titulo}"

