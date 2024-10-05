from django.db import models
from django.contrib.auth.models import User

# Modelo de Perfil de Usuario
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario.username

# Modelo de Contrato
class Contrato(models.Model):
    OPCIONES_SERVICIO = [
        ('agua', 'Agua'),
        ('electricidad', 'Electricidad'),
        ('gas', 'Gas'),
        ('telefono', 'Telefonía'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contratos')
    tipo_servicio = models.CharField(max_length=50, choices=OPCIONES_SERVICIO)
    numero_contrato = models.CharField(max_length=50, unique=True)
    fecha_inicio = models.DateField()
    
    def __str__(self):
        return f'{self.tipo_servicio} - {self.numero_contrato}'

# Modelo de Factura
class Factura(models.Model):
    OPCIONES_ESTADO = [
        ('pagada', 'Pagada'),
        ('pendiente', 'Pendiente'),
    ]
    
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='facturas')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=50, choices=OPCIONES_ESTADO, default='pendiente')
    
    def __str__(self):
        return f'Factura {self.id} - {self.contrato.tipo_servicio} - {self.estado}'
