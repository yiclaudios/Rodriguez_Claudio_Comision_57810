from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.matricula} - {self.marca} - {self.modelo}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email  = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email  = models.EmailField()
    direccion = models.CharField(max_length=100)

    #esto es para configurar que al momento de django hacer el pluran en lugar de poner ProveedorS, ponga Proveedores
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["nombre", "apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    documento = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"
