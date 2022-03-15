from django.db import models

# Create your models here.


#tabla de clientes
class Clientes(models.Model):
    nombre = models.CharField( max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=50)


#tabla de articulos
class Articulos(models.Model):
    nombre = models.CharField( max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()
    

#tabla de pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()