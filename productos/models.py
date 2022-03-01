from email import charset
from pyexpat import model
from django.db import models


class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    imagen = models.ImageField()
    nombre = models.CharField(unique=True, max_length=60)
    categoria = models.CharField(max_length=20)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=False)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=30)
    condicion_iva = models.CharField(max_length=50)