from xml.dom.minidom import Identified
from django.db import models

class Cliente(models.Model):
    tipo_identificacion = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=50, null=False)

class Producto(models.Model):
    codigo = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, null=False)
    costoUnitario = models.CharField(max_length=50, null=False)

class Factura(models.Model):
    nro = models.CharField(max_length=50, null=False)
    cantidad = models.CharField(max_length=50, null=False)
    costo = models.CharField(max_length=50, null=False)
    fecha = models.CharField(max_length=50, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

