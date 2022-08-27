from django.db import models

class Negocio(models.Model):
    nombre = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    codigo_postal = models.IntegerField()
    def __str__(self):
        return 'Negocio: ' + self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return 'Producto: ' + self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    edad = models.IntegerField()
    def __str__(self):
        return 'Empleado: ' + self.nombre + ' ' + self.apellido


# Create your models here.
